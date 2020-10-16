# Week 5: HTML5 Forms


## 5.7 Form validation API


### 5.7.0 Lecture Notes

+ [Visual feedback](#572-automatic-visual-feedback-while-typing)
  + most modern browsers proposing default behavior for validating input fields and forms
  + built-in validation system: HTML5 automatically adds a CSS pseudo class to all input fields
  + invalid fields: inherit the `:invalid` pseudo class
  + valid fields: inherit the `:valid` pseudo class
  + improving your HTML form
    + add some CSS rules to input fields
    + add visual feedback to the validity of input fields values, e.g.,
      + changing the color of the border of input fields
      + green/red icons on the right of the field
    + submitting the form: extra messages displayed as pop up text bubbles
      + default: providing default feedback on the input field's border
      + overridden by CSS rules
  + __best practice__: ALWAYS provide default CSS rules that give visual feedback to the user's input
  + example: styling "required', "valid" and "invalid" fields

    ```html
    <style>
      input:invalid { background-color: lightPink;}
      input:valid { background-color:lightGreen; }
      input:required {border: 2px solid red;}
      input:optional {border: 2px solid green;}
      fieldset {
        border:1px solid;
        padding:20px;
        }
      .formLabel { display: inline-block; width: 140px; text-align: right; }
    </style>
    ...
    <form>
      <fieldset>
        <legend>Type invalid values and see the result</legend>
        <label for="myEmail" class="formLabel">E-mail:</label>
          <input type="email" id="myEmail" required/><br>
        <label for="myURL" class="formLabel">Homepage (URL):</label> 
          <input type="url" id="myURL" required/><br>
        <label for="myPhone" class="formLabel">Phone number:</label> 
          <input type="tel" id="myPhone" pattern="[0-9]{3}-?[0-9]{3}-?[0-9]{4}"
          placeholder="e.g. 416-555-1234" required/><br>
          <button>Submit form</button><br />
      </fieldset>
    </form>
    ```

  + example: adding CSS transition & icon/marker to the right of the input field

    ```css
    .myForm input:focus {
      padding-right:70px;
    }
    .myForm input {
      transition: padding .25s;
    }
    .myForm input:required:valid {
      background:url('https://i.imgur.com/BJolppS.png') no-repeat right top;
    }
    .myForm input:required {
      background:url('https://i.imgur.com/7pIN7wz.png') no-repeat right top;
    }
    ```

    + `.myForm input:focus` class:  enlarge itself to the right when clicking on an input field
    + `.myForm input` class: making the file animated
    + `.myForm input:required:valid` class: display a green icon if valid at a required input field
    + `.myForm input:required` class: display a red icon if invalid at a required input field
  + [the `title` attribute for customized message](#use-the-title-attribute-for-specifying-a-custom-message)
    + simply using the input's title attribute to provide a message for pattern-mismatches
    + more generally for all validation errors
    + really neat and no JavaScript required
    + e.g., `<input type="email" id="myEmail" title="You don't know what an email address looks like, do you?" required/><br>`
    + browser dependent:
      + Chrome & Opera: display the `title` attribute value in error message bubbles
      + Safari and FireFox: ignore the `title` attribute
  + references:
    + [Cross Browser Styling of HTML5 Forms — Even In Older Browsers](https://tinyurl.com/ccyho8c)
    + [Creating Cross Browser HTML5 Forms Now, Using modernizr, webforms2 and html5Forms](https://tinyurl.com/c9omt6n)

+ [Javascript form validation](#573-javascript-form-validation-api)
  + allowing developers to use their own validation algorithm and customize error messages
  + together w/ some HTML/CSS/JavaScript to make own message bubbles
  + example: password checking

    ```html
    <form class="myForm">
      <fieldset>
        <legend>Example use of the validation API</legend>
        <label for="password1" >Password:</label> <input type="password" id="password1" oninput="checkPasswords()" required>
        <p>
        <label for="password2">Repeat password:</label> <input type="password" id="password2" oninput="checkPasswords()" required>
        <p>
        <button>Submit</button>
      </fieldset>
    </form>

    <script>
    function checkPasswords() {
      var password1 = document.getElementById('password1');
      var password2 = document.getElementById('password2');
      if (password1.value != password2.value) {
        password2.setCustomValidity('Passwords non identiques');
      } else {
          password2.setCustomValidity('');
        }
      }
    </script>
    ```

    + `setCustomValidity()` method:
      + syntax: `selectElt.setCustomValidity(string);`
      + allow developers to customize error messages
      + empty string: valid element
      + non-empty string: invalid field and valuation error message displayed in the bubble
    + input event listeners: call `checkPasswords()` function when typing
      + `<label for="password1" >Password:</label> <input type="password" id="password1" oninput="checkPasswords()" required>`
      + `<label for="password2">Repeat password:</label> <input type="password" id="password2" oninput="checkPasswords()" required>`
    + get the input fields' values: `var password1 = document.getElementById('password1'); var password2 = document.getElementById('password2');`
    + set the validity of the field using the validation API's method `setCustomValidity(error_message)`






### 5.7.1 Introduction

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4rdoace')"
    src    ="https://tinyurl.com/y432thju"
    alt    ="validation example"
    title  ="validation example"
  />
</figure>

In this section of the course, we will look at CSS pseudo classes that are useful for giving instant feedback when the user's input is not valid. We will also look at the new JavaScript API introduced by HTML5 for validating forms and form elements.

In the following pages, we will first illustrate the concept of form validation with the `<input type="email"/>` field. It can be generalized to all kind of input types, such as url, number, etc. Some form attributes, such as `pattern`,  will also affect input field validity!

Form validation is [supported](https://caniuse.com/#feat=form-validation) by all modern browsers.


### 5.7.2 Automatic visual feedback while typing

Most modern browsers propose default behavior for validating input fields and forms.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y387nwvw')"
    src    ="https://tinyurl.com/yy2pg5e9"
    alt    ="example of css pseudo class in use"
    title  ="example of css pseudo class in use"
  />
</figure>

The built-in validation system that comes with HTML5 automatically adds a CSS pseudo class to all input fields. Invalid fields (i.e. a badly worded email address in an `<input type="email">` input field), will inherit the `:invalid` pseudo class, valid fields will inherit the `:valid` pseudo class.

A first step to improve your HTML form is to add some CSS rules to your input fields. This adds visual feedback to the validity of input fields values - while the user is typing - such as changing the color of the border of input fields, or green/red icons on the right of the field, as shown in the small picture at the top right of this page.

Also, at the time of submitting the form, some extra messages may be displayed as pop up text bubbles.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y387nwvw')"
    src    ="https://tinyurl.com/y4pfxrkd"
    alt    ="bubble message exampleThe default bubble message and visual feedback differ from one implementation to another, but they may be customized, with some limitations that will be explained later."
    title  ="bubble message exampleThe default bubble message and visual feedback differ from one implementation to another, but they may be customized, with some limitations that will be explained later."
  />
</figure>

For example, browsers may provides default feedback on the input field's border (red = invalid, green = ok). This default behavior can be overridden by CSS rules as illustrated in the section about new input type attributes. 


#### Examples
 
__Example #1: styling "required", "valid" and" invalid" fields using CSS3 pseudo-classes__

Here is an [online example at JSBin](https://jsbin.com/palifuy/edit?html,output), or try it below in your browser: ([Local Example - Styling](src/5.7.2-example1.html))

<div class="exampleHTML"><form><fieldset><legend>Type invalid values and submit form to see the result</legend> <label class="formLabel" for="myEmail">E-mail:</label> <input id="myEmail" required="" type="email"><br> <label class="formLabel" for="myURL">Homepage (URL):</label> <input id="myURL" required="" type="url"><br> <label class="formLabel" for="myPhone">Phone number:</label> <input id="myPhone" required="" placeholder="e.g. 416-555-1234" pattern="[0-9]{3}-?[0-9]{3}-?[0-9]{4}" type="phone"><br> <button>Submit form</button></fieldset></form></div>

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;title&gt;</span><span class="pln">CSS3 pseudo-classes for form validation visual feedback</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span>&lt;style&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span>input</span><span class="pun">:</span><span class="pln">invalid </span><span class="pun">{</span><span class="pln"> background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightPink</span><span class="pun">;}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span>input</span><span class="pun">:</span><span class="pln">valid </span><span class="pun">{</span><span class="pln"> background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln">lightGreen</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span>input</span><span class="pun">:</span><span class="pln">required </span><span class="pun">{</span><span class="pln">border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid red</span><span class="pun">;}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span>input</span><span class="pun">:</span><span class="pln">optional </span><span class="pun">{</span><span class="pln">border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid green</span><span class="pun">;}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span>fieldset </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>border</span><span class="pun">:</span><span class="lit">1px</span><span class="pln"> solid</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>padding</span><span class="pun">:</span><span class="lit">20px</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">.</span><span class="pln">formLabel </span><span class="pun">{</span><span class="pln"> display</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">inline</span><span class="pun">-</span><span class="pln">block</span><span class="pun">;</span><span class="pln"> width</span><span class="pun">:</span><span class="pln"> </span><span class="lit">140px</span><span class="pun">;</span><span class="pln"> text</span><span class="pun">-</span><span class="pln">align</span><span class="pun">:</span><span class="pln"> right</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span>&lt;/style&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/head&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span>&lt;body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span>&lt;form&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;fieldset&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;legend&gt;</span><span class="pln">Type invalid values and see the result</span><span class="tag">&lt;/legend&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"myEmail"</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"formLabel"</span><span class="tag">&gt;</span><span class="pln">E-mail:</span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myEmail"</span><span class="pln"> </span><span class="atn">required</span><span class="tag">/&gt;&lt;br&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"myURL"</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"formLabel"</span><span class="tag">&gt;</span><span class="pln">Homepage (URL):</span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"url"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myURL"</span><span class="pln"> </span><span class="atn">required</span><span class="tag">/&gt;&lt;br&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"myPhone"</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"formLabel"</span><span class="tag">&gt;</span><span class="pln">Phone number:</span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"tel"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myPhone"</span><span class="pln"> </span><span class="atn">pattern</span><span class="pun">=</span><span class="atv">"[0-9]{3}-?[0-9]{3}-?[0-9]{4}"</span><span class="pln"> </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="pln"></span><span class="tag"></span><span class="tag"></span><span class="atn">placeholder</span><span class="pun">=</span><span class="atv">"e.g. 416-555-1234"</span><span class="pln"> </span><span class="atn">required</span><span class="tag">/&gt;&lt;br&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;button&gt;</span><span class="pln">Submit form</span><span class="tag">&lt;/button&gt;&lt;br</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/fieldset&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span>&lt;/form&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;p&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;</span></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span>&lt;/body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
</ol></div>
 
Try the online example with different Web browsers, both with and without the CSS rules. See the differences between FireFox/Chrome/Opera in the default visual feedback behavior. Don't worry: all default behavior can be overridden if you provide your own CSS rules.

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong><span style="color: #ff0000;">Best practice</span>: &nbsp;We recommend that&nbsp;you ALWAYS&nbsp;provide default CSS rules that give visual feedback to the user's input.</strong></p>


__Example #2: add CSS transitions + an icon/marker to the right of the input fields__

Try this [online example at JSBin](https://jsbin.com/zaxije/2/edit) or try it here in your browser. This example adds a small icon that changes depending on the validity of the input field: ([Local Example - Validation](src/5.7.2-example2.html))

<div class="exampleHTML"><form class="myForm"><fieldset><legend>Type invalid values and see the result</legend> <label class="formLabel" for="myEmail">E-mail:</label> <input id="myEmail" required="" type="email"><br> <label class="formLabel" for="myURL">Homepage (URL):</label> <input id="myURL" required="" type="url"><br> <label class="formLabel" for="myPhone">Phone number:</label> <input id="myPhone" required="" placeholder="e.g. 416-555-1234" pattern="[0-9]{3}-?[0-9]{3}-?[0-9]{4}" type="phone"><br> <button>Submit form</button></fieldset></form></div>

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">.</span><span class="pln">myForm input</span><span class="pun">:</span><span class="pln">focus </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>&nbsp;padding</strong></span><strong><span class="pun">-</span><span class="pln">right</span><span class="pun">:</span><span class="lit">70px</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">.</span><span class="pln">myForm input </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>&nbsp;transition</strong></span><strong><span class="pun">:</span><span class="pln"> padding </span><span class="pun">.</span><span class="lit">25s</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">.</span><span class="pln">myForm <strong>input</strong></span><strong><span class="pun">:</span><span class="pln">required</span><span class="pun">:</span><span class="pln">valid </span></strong><span class="pun">{</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;background</span><span class="pun">:</span><span class="pln">url</span><span class="pun">(</span><span class="str">'https://i.imgur.com/BJolppS.png'</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">no</span><span class="pun">-</span><span class="pln">repeat right top</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">.</span><span class="pln">myForm <strong>input</strong></span><strong><span class="pun">:</span><span class="pln">required </span></strong><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;background</span><span class="pun">:</span><span class="pln">url</span><span class="pun">(</span><span class="str">'https://i.imgur.com/7pIN7wz.png'</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">no</span><span class="pun">-</span><span class="pln">repeat right top</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

This time, we just added an attribute `class="myForm"` to our form, in order to avoid interfering with the other examples on this page, and we tweaked the CSS rules a little.

The rule at _line 1_ says that any time we click on an input field, it will enlarge itself to the right, while the rule at _line 4_ will make it animated.

The rules at _lines 8_ and _11_ target the input fields with a `required` attribute. They will change the background by displaying a small green or red icon, corresponding to the valid/invalid status of the input field.


#### Use the `title` attribute for specifying a custom message

You can simply use the input's `title` attribute to provide a message for pattern-mismatches, and more generally for all validation errors. This solution is really neat and doesn't require JavaScript!

Try the [online example at JSBin](https://jsbin.com/locedoy/1/edit?html,output), or try it here in your browser (type invalid values and look at the custom messages): ([Local Example - Message](src/5.7.2-example3.html))

<div class="exampleHTML"><form class="myForm"><fieldset><legend>Type invalid values and see the result, this time with custom messages!&nbsp;</legend> <label class="formLabel" for="myEmail">E-mail:</label> <input title="You don't know what an email address looks like do you?" id="myEmail" required="" type="email"><br> <label class="formLabel" for="myURL">Homepage (URL):</label> <input title="Please start with HTTP or HTTPS or you'll never get your degree!" id="myURL" required="" type="url"><br> <label class="formLabel" for="myPhone">Phone number:</label> <input title="can't you read the provided example?" id="myPhone" required="" placeholder="e.g. 416-555-1234" pattern="[0-9]{3}-?[0-9]{3}-?[0-9]{4}" type="phone"><br> <button>Submit form</button></fieldset></form></div>

Extract from source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;form</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"myForm"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;fieldset&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;legend&gt;</span><span class="pln">Type invalid values and see the result</span><span class="tag">&lt;/legend&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"myEmail"</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"formLabel"</span><span class="tag">&gt;</span><span class="pln">E-mail:</span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myEmail"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="atn">title</span><span class="pun">=</span><span class="atv">"You don't know what an email address looks like, do you?"</span></strong><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;required</span><span class="tag">/&gt;&lt;br&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;button&gt;</span><span class="pln">Submit form</span><span class="tag">&lt;/button&gt;&lt;br</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;/fieldset&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/form&gt;</span></li>
</ol></div>

_Beware_ that browser implementations may differ. Chrome, Opera will display the `title` attribute value in error message bubbles when the form is submitted, while Safari and FireFox (desktop and mobile) will simply ignore it.

You must also take care of the different languages, otherwise you will get error message bubbles that show some parts in the local language, and the message from the title attribute "as is".

Google Chrome on a French desktop computer:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y387nwvw')"
    src    ="https://tinyurl.com/yxpekwa3"
    alt    ="Chrome shows native error message localized and the title attribute content as is"
    title  ="Chrome shows native error message localized and the title attribute content as is"
  />
</figure>

Same example on FireFox, the `title` attribute is ignored:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y387nwvw')"
    src    ="https://tinyurl.com/y3ga6zro"
    alt    ="same example on firefox, the title attribute is ignored"
    title  ="same example on firefox, the title attribute is ignored"
  />
</figure>

<p style="border: 1px solid; padding: 15px;"><strong>The built-in validation system is an improvement on what existed before HTML5 (i.e., nothing), but additional work is required if you want fully localized, hand-made validation feedback.<br><br><span style="color: #ff0000;">We will show solutions in the last section of this week's course.</span><br> </strong></p>


### 5.7.3 JavaScript form validation API

There is a JavaScript API for form validation. This API will let you use your own validation algorithm (i.e. check that you have entered the same password in two different input fields), and customize error messages. Also, together with some HTML/CSS/JavaScript you will be able to make your own message bubbles.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y3hkpynf')"
    src    ="https://tinyurl.com/yxa7lsmg"
    alt    ="password custom validation example"
    title  ="password custom validation example"
  />
</figure>


#### Typical use

[Example of password checking at JSBin](https://jsbin.com/hovato/1/edit?html,output),  be careful to try this example in JS Bin standalone mode (click the small black arrow on the top right of the output tab). ([Local Example - Validation](src/5.7.3-example1.html))

Or you may try it here in your browser:

<div class="exampleHTML"><form class="myForm"><fieldset><legend>Example use of the validation API, enter different passwords and submit&nbsp;</legend> <label for="password1">Password:</label> <input id="password1" required="" oninput="checkPasswords()" type="password" style="background-image: url(&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACIUlEQVQ4EX2TOYhTURSG87IMihDsjGghBhFBmHFDHLWwSqcikk4RRKJgk0KL7C8bMpWpZtIqNkEUl1ZCgs0wOo0SxiLMDApWlgOPrH7/5b2QkYwX7jvn/uc//zl3edZ4PPbNGvF4fC4ajR5VrNvt/mo0Gr1ZPOtfgWw2e9Lv9+chX7cs64CS4Oxg3o9GI7tUKv0Q5o1dAiTfCgQCLwnOkfQOu+oSLyJ2A783HA7vIPLGxX0TgVwud4HKn0nc7Pf7N6vV6oZHkkX8FPG3uMfgXC0Wi2vCg/poUKGGcagQI3k7k8mcp5slcGswGDwpl8tfwGJg3xB6Dvey8vz6oH4C3iXcFYjbwiDeo1KafafkC3NjK7iL5ESFGQEUF7Sg+ifZdDp9GnMF/KGmfBdT2HCwZ7TwtrBPC7rQaav6Iv48rqZwg+F+p8hOMBj0IbxfMdMBrW5pAVGV/ztINByENkU0t5BIJEKRSOQ3Aj+Z57iFs1R5NK3EQS6HQqF1zmQdzpFWq3W42WwOTAf1er1PF2USFlC+qxMvFAr3HcexWX+QX6lUvsKpkTyPSEXJkw6MQ4S38Ljdbi8rmM/nY+CvgNcQqdH6U/xrYK9t244jZv6ByUOSiDdIfgBZ12U6dHEHu9TpdIr8F0OP692CtzaW/a6y3y0Wx5kbFHvGuXzkgf0xhKnPzA4UTyaTB8Ph8AvcHi3fnsrZ7Wore02YViqVOrRXXPhfqP8j6MYlawoAAAAASUVORK5CYII=&quot;); background-repeat: no-repeat; background-attachment: scroll; background-size: 16px 18px; background-position: 98% 50%;">
<p><label for="password2">Repeat password:</label> <input id="password2" required="" oninput="checkPasswords()" type="password" style="background-image: url(&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACIUlEQVQ4EX2TOYhTURSG87IMihDsjGghBhFBmHFDHLWwSqcikk4RRKJgk0KL7C8bMpWpZtIqNkEUl1ZCgs0wOo0SxiLMDApWlgOPrH7/5b2QkYwX7jvn/uc//zl3edZ4PPbNGvF4fC4ajR5VrNvt/mo0Gr1ZPOtfgWw2e9Lv9+chX7cs64CS4Oxg3o9GI7tUKv0Q5o1dAiTfCgQCLwnOkfQOu+oSLyJ2A783HA7vIPLGxX0TgVwud4HKn0nc7Pf7N6vV6oZHkkX8FPG3uMfgXC0Wi2vCg/poUKGGcagQI3k7k8mcp5slcGswGDwpl8tfwGJg3xB6Dvey8vz6oH4C3iXcFYjbwiDeo1KafafkC3NjK7iL5ESFGQEUF7Sg+ifZdDp9GnMF/KGmfBdT2HCwZ7TwtrBPC7rQaav6Iv48rqZwg+F+p8hOMBj0IbxfMdMBrW5pAVGV/ztINByENkU0t5BIJEKRSOQ3Aj+Z57iFs1R5NK3EQS6HQqF1zmQdzpFWq3W42WwOTAf1er1PF2USFlC+qxMvFAr3HcexWX+QX6lUvsKpkTyPSEXJkw6MQ4S38Ljdbi8rmM/nY+CvgNcQqdH6U/xrYK9t244jZv6ByUOSiDdIfgBZ12U6dHEHu9TpdIr8F0OP692CtzaW/a6y3y0Wx5kbFHvGuXzkgf0xhKnPzA4UTyaTB8Ph8AvcHi3fnsrZ7Wore02YViqVOrRXXPhfqP8j6MYlawoAAAAASUVORK5CYII=&quot;); background-repeat: no-repeat; background-attachment: scroll; background-size: 16px 18px; background-position: 98% 50%;"></p>
<p><button>Submit</button></p>
</fieldset></form>
<script>// <![CDATA[
function checkPasswords() {
 var password1 = document.getElementById('password1');
 var password2 = document.getElementById('password2');
 if (password1.value != password2.value) {
 password2.setCustomValidity('Passwords non identiques');
 } else {
 password2.setCustomValidity('');
 }
 }
// ]]></script>
</div>

Extract from source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;title&gt;</span><span class="pln">Example of using the validation API</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;style&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">.</span><span class="pln">myForm input</span><span class="pun">:</span><span class="pln">invalid </span><span class="pun">{</span><span class="pln"> background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightPink</span><span class="pun">;}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pun"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pun"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span>.</span><span class="pln">myForm input</span><span class="pun">:</span><span class="pln">valid </span><span class="pun">{</span><span class="pln"> background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln">lightGreen</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">.</span><span class="pln">myForm input</span><span class="pun">:</span><span class="pln">required </span><span class="pun">{</span><span class="pln">border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid red</span><span class="pun">;}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">.</span><span class="pln">myForm input</span><span class="pun">:</span><span class="pln">optional </span><span class="pun">{</span><span class="pln">border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid green</span><span class="pun">;}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pun"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pun"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span>.</span><span class="pln">myForm label </span><span class="pun">{</span><span class="pln"> display</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">inline</span><span class="pun">-</span><span class="pln">block</span><span class="pun">;</span><span class="pln"> width</span><span class="pun">:</span><span class="pln"> </span><span class="lit">140px</span><span class="pun">;</span><span class="pln"> text</span><span class="pun">-</span><span class="pln">align</span><span class="pun">:</span><span class="pln"> right</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span>&lt;/style&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;body&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span>&lt;form</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"myForm"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;fieldset&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;legend&gt;</span><span class="pln">Example use of the validation API</span><span class="tag">&lt;/legend&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"password1"</span><span class="pln"> </span><span class="tag">&gt;</span><span class="pln">Password:</span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"password"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"password1"</span><span class="pln"> </span><span class="atn">oninput</span><span class="pun">=</span><span class="atv">"</span><span class="pln">checkPasswords</span><span class="pun">()</span><span class="atv">"</span><span class="pln"> </span><span class="atn">required</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;p&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"password2"</span><span class="tag">&gt;</span><span class="pln">Repeat password:</span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"password"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"password2"</span><span class="pln"> </span><span class="atn">oninput</span><span class="pun">=</span><span class="atv">"</span><span class="pln">checkPasswords</span><span class="pun">()</span><span class="atv">"</span><span class="pln"> </span><span class="atn">required</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;button&gt;</span><span class="pln">Submit</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/fieldset&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span>&lt;/form&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span>&lt;script&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag"></span><span class="kwd">function</span><span class="pln"> checkPasswords</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> password1 </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'password1'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> password2 </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'password2'</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">password1</span><span class="pun">.</span><span class="pln">value </span><span class="pun">!=</span><span class="pln"> password2</span><span class="pun">.</span><span class="pln">value</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span>password2</span><span class="pun">.</span><span class="pln">setCustomValidity</span><span class="pun">(</span><span class="str">'Passwords non identiques'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="tag"></span></span>password2</span><span class="pun">.</span><span class="pln">setCustomValidity</span><span class="pun">(</span><span class="str">''</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span>&lt;/script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


__Explanations:__

The validity API proposes a `setCustomValidity()` method available on input DOM objects. This method allows you to customize error messages. It takes a string parameter. When this string is empty, the element is considered valid, when the string is not empty, the field is invalid and the validation error message displayed in the bubble will be equal to that string.

At lines 18 and 20 we added an input event listener: each time a key is typed, the `checkPasswords()` function is called.

Lines 28 and 29 get the input fields' values, and lines 30-35 check if the passwords are the same and set the validity of the field using the validation API's method `setCustomValidity(error_message)`.




 