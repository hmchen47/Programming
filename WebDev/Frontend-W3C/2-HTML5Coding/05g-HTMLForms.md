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
        <label for="password1" >Password:</label> <input type="password" 
          id="password1" oninput="checkPasswords()" required>
        <p>
        <label for="password2">Repeat password:</label> <input type="password" 
          id="password2" oninput="checkPasswords()" required>
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

+ [validity property](#574-the-validity-property-of-input-fields)
  + error details when the field is invalid
  + test the different types of validation error
  + typical usage: `var validityState_object = input.validity;`
  + possible values
    + `valueMissing`
    + `typeMismatch`
    + `patternMismatch`
    + `tooLong`
    + `rangeUnderflow`
    + `rangeOverflow`
    + `stepMismatch`
    + `valid`
    + `customError`
  + example:

    ```js
    if(validityState_object.valueMissing) {
        input.setCustomValidity('Please set an age (required)');
    } else if (validityState_object.rangeUnderflow) {
        input.setCustomValidity('Your value is too low');
    } else if (validityState_object.rangeOverflow) {
        input.setCustomValidity('Your value is too high');
    ...
    }
    ```

+ [validationMessage property](the-validationmessage-property)
  + the validation error messag
  + useful for making custom error messages
  + typical usage: `console.log("Validation message = " + input.validationMessage);`

+ [Customized validation](#575-changing-the-default-behavior)
  + changing the default behavior, aggregating error messages, removing bubbles, etc.
  + browser built-in validation
    + powerful technique to enhance HTML forms
    + provide interesting features
    + criticized by Web developers
      + not 100% complete, in particular, IE & Safari
      + not possible to aggregate error message, showing error bubble next to the first invalid
      + unable to style bubbles
  + validate API
    + providing enough power to make own validation behavior
    + overridden the default when necessary
    + ref: [Building HTML5 Form Validation Bubble Replacements](https://tinyurl.com/yy85v45z)
  + example: aggregation of error messages + overriding default behavior
    + add an empty unnumbered list (`<ul>`...`</ul>`) to the form in style: `<ul class="error-messages"></ul>`
    + use this class attribute for styling, and hiding by default, the error messages using CSS,: `.error-messages { display: none; ...}`
    + replace the validation UI for all forms via calling `replaceValidationUI(form)` function in JavaScript: 
   
      ```js
      var forms = document.querySelectorAll("form"); 
      for (var i = 0; i < forms.length; i++) {
          replaceValidationUI(forms[ i ]);
      }
      ```

    + disable all default behavior

      ```js
      function replaceValidationUI(form) {
      // Suppress the default bubbles
         form.addEventListener("invalid", function (event) {
         event.preventDefault();
      }, true);
       // Support Safari, iOS Safari, and the Android browser — each of which
      // do not prevent form submissions by default
      form.addEventListener("submit", function (event) {
         if (!this.checkValidity()) {
            event.preventDefault();
         }
      });
      ```

    + add a click listener to the submit button: `submitButton.addEventListener("click", function (event) {...}`
    + get all invalid input fields for that form: `var invalidFields = form.querySelectorAll("input:invalid");`
    + get the value of the name attribute of the corresponding label from each invalid field & build a list of `<li>`...`</li>` to the error message container

      ```js
      for (var i = 0; i < invalidFields.length; i++) {
          label = form.querySelector("label[for=" + invalidFields[ i ].id + "]");
          listHtml += "<li>" +
                      label.innerHTML +
                      " " +
                      invalidFields[ i ].validationMessage +
                      "</li>";
      }
      ```
    
    + pdate the list with the new error messages: `errorMessagesContainer.innerHTML = listHtml;`
    + give focus to the first invalid field and show the error messages container by setting its CSS property `display=block`

      ```js
      if (invalidFields.length > 0) {
        invalidFields[ 0 ].focus();
        errorMessagesContainer.style.display = "block";
      }
      ```


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


### 5.7.4 The validity property of input fields

The `validity` property of input fields helps to get error details when the field is _invalid_. This property tests the different types of validation error.

Here is how to get the `validity` property of an input field:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> input </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'IdOfField'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> validityState_object </span><span class="pun">=</span><strong><span class="pln"> input</span><span class="pun">.</span><span class="pln">validity</span><span class="pun">;</span></strong></li>
</ol></div>

The possible values for the `validity` property are:

+ `valueMissing`
+ `typeMismatch`
+ `patternMismatch`
+ `tooLong`
+ `rangeUnderflow`
+ `rangeOverflow` 
+ `stepMismatch`
+ `valid`
+ `customError`

Here is [an example at JSBin that shows how to test the different types of validation errors](https://jsbin.com/nalaxeg/1/edit?html,output), or you may try it here in your browser (enter bad values, too big, too small, enter invalid characters, etc.): ([Local Example - Types of Validation Errors](src/5.7.4-example1.html))

<div class="exampleHTML">
<script>// <![CDATA[
function validate() {
     var input = document.getElementById('b');
     var validityState_object = input.validity;
 
     if(validityState_object.valueMissing) {
         input.setCustomValidity('Please set an age (required)');
     } else if (validityState_object.rangeUnderflow) {
         input.setCustomValidity('Your value is too low');
     } else if (validityState_object.rangeOverflow) {
         input.setCustomValidity('Your value is too high');
     } else if (validityState_object.typeMismatch) {
         input.setCustomValidity('Type mismatch');
     } else if (validityState_object.tooLong) {
         input.setCustomValidity('Too long');
     } else if (validityState_object.stepMismatch) {
         input.setCustomValidity('stepMismatch');
     } else if (validityState_object.patternMismatch) {
         input.setCustomValidity('patternMismatch');
     } else {
         input.setCustomValidity('');
     }
 }
// ]]></script>
<form class="myForm"><label for="b">Enter a value between 10 and 20 </label> <input name="text" id="b" required="" oninput="validate()" min="10" max="20" type="number"> <input value="Submit Query" type="submit"></form></div>
 
Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;">...</li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> validate</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> input </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'b'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; <strong>&nbsp;var</strong></span><strong><span class="pln"> validityState_object </span><span class="pun">=</span><span class="pln"> input</span><span class="pun">.</span><span class="pln">validity</span><span class="pun">;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">validityState_object</span><span class="pun">.</span><span class="pln">valueMissing</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">.</span><span class="pln">setCustomValidity</span><span class="pun">(</span><span class="str">'Please set an age (required)'</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pun"><span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.</span><span class="pln">rangeUnderflow</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">.</span><span class="pln">setCustomValidity</span><span class="pun">(</span><span class="str">'Your value is too low'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pun"><span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.</span><span class="pln">rangeOverflow</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">.</span><span class="pln">setCustomValidity</span><span class="pun">(</span><span class="str">'Your value is too high'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pun"><span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.</span><span class="pln">typeMismatch</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">.</span><span class="pln">setCustomValidity</span><span class="pun">(</span><span class="str">'Type mismatch'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pun"><span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.</span><span class="pln">tooLong</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">.</span><span class="pln">setCustomValidity</span><span class="pun">(</span><span class="str">'Too long'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pun"><span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.</span><span class="pln">stepMismatch</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">.</span><span class="pln">setCustomValidity</span><span class="pun">(</span><span class="str">'stepMismatch'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pun"><span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.</span><span class="pln">patternMismatch</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">.</span><span class="pln">setCustomValidity</span><span class="pun">(</span><span class="str">'patternMismatch'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">.</span><span class="pln">setCustomValidity</span><span class="pun">(</span><span class="str">''</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;form</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"myForm"</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"b"</span><span class="tag">&gt;</span><span class="pln">Enter a value between 10 and 20: </span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"number"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"b"&nbsp;</span><span class="atn">min</span><span class="pun">=</span><span class="atv">"10"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"20"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">required</span><span class="pln"> </span><strong><span class="atn">oninput</span><span class="pun">=</span><span class="atv">'</span><span class="pln">validate</span><span class="pun">();</span><span class="atv">'</span></strong><span class="tag">/&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button&gt;</span><span class="pln">Submit</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/form&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


#### The `validationMessage` property

It is also possible to get the validation error message, using the `validationMessage` property of input fields.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> input </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'b'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Validation message = "</span><span class="pln"> </span><span class="pun">+</span><strong><span class="pln"> input</span><span class="pun">.</span></strong><span class="pln"><strong>validationMessage</strong>)</span><span class="pun">;</span></li>
</ol></div>

This is useful for making custom error messages. More about this topic in the next section of the course.


### 5.7.5 Changing the default behavior

#### Custom validation: changing the default behavior, aggregating error messages, removing bubbles, etc.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2mrwrec')"
    src    ="https://tinyurl.com/y3woj2rt"
    alt    ="Aggregating error message"
    title  ="Aggregating error message"
  />
</figure>


__Criticism of the default behavior of HTML5 built-in validation__

The techniques we have seen so far for enhancing HTML forms are powerful and provide interesting features, but are also criticized by Web developers:

+ Browser support is still not 100% complete (Safari and Internet Explorer still lack several important features),
+ It is not possible to aggregate error messages.  On submission, browsers show an error bubble next to the first invalid field, and there is no built-in way to _display all error messages for all invalid fields at the same time,_
+ You cannot style the bubbles.

__However, the validation API gives enough power to make your own validation behavior, overriding the default when necessary.__

Here is [an adaptation of work presented at the developer.telerik.com Web site](https://www.telerik.com/blogs/building-html5-form-validation-bubble-replacements).  This link is really worth reading, as it presents different approaches and gives external references for those who would like to go further.


#### Example that shows aggregation of error messages + overriding default behavior

Try the [online example at JSBin](https://jsbin.com/povekur/1/edit?html,output), or try it here in your browser: enter invalid values and submit with one or two invalid fields. ([Local Example - Error Messages](src/5.7.5-example1.html))

<div class="exampleHTML"><form class="myForm"><fieldset>
<ul class="error-messages"></ul>
<label for="name">Name:</label> <input name="name" id="name" required="" type="text">
<p><label for="email">Email:</label> <input name="email" id="email" required="" type="email"></p>
<p><button>Submit</button></p>
</fieldset></form>
<script>// <![CDATA[
function replaceValidationUI(form) {
    // Suppress the default bubbles
    form.addEventListener("invalid", function (event) {
        event.preventDefault();
    }, true);

    // Support Safari, iOS Safari, and the Android browser—each of which do not prevent
    // form submissions by default
    form.addEventListener("submit", function (event) {
        if (!this.checkValidity()) {
            event.preventDefault();
        }
    });

    // Container that holds error messages. By default it has a CSS display:none property
    var errorMessages = form.querySelector(".error-messages");

    var submitButton = form.querySelector("button:not([type=button]), input[type=submit]");

    submitButton.addEventListener("click", function (event) {
        var invalidFields = form.querySelectorAll("input:invalid"),
                listHtml = "",
                errorMessagesContainer = form.querySelector(".error-messages"),
                label;

        // Get the labels' values of their name attributes + the validation error
        // message of the corresponding input field using the validationMessage
        // property of input fields
        // We build a list of <li>...</li> that we add to the error message container
        for (var i = 0; i < invalidFields.length; i++) {
            label = form.querySelector("label[for=" + invalidFields[ i ].id + "]");
            listHtml += "<li>" +
                    label.innerHTML +
                    " " +
                    invalidFields[ i ].validationMessage +
                    "</li>";
        }

        // Update the list with the new error messages
        errorMessagesContainer.innerHTML = listHtml;

        // If there are errors, give focus to the first invalid field and show
        // the error messages container by setting its CSS property display=block
        if (invalidFields.length > 0) {
            invalidFields[ 0 ].focus();
            errorMessagesContainer.style.display = "block";
        }
    });
  }

  // Replace the validation UI for all forms
  var forms = document.querySelectorAll("form");

  for (var i = 0; i < forms.length; i++) {
      replaceValidationUI(forms[ i ]);
  }
// ]]></script>
</div>

Complete source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;title&gt;</span><span class="pln">Aggregating error messages</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;style&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">:</span><span class="pln">invalid </span><span class="pun">{</span><span class="pln"> background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightPink</span><span class="pun">;}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">:</span><span class="pln">valid </span><span class="pun">{</span><span class="pln"> background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln">lightGreen</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">:</span><span class="pln">required </span><span class="pun">{</span><span class="pln">border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid red</span><span class="pun">;}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;input</span><span class="pun">:</span><span class="pln">optional </span><span class="pun">{</span><span class="pln">border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid green</span><span class="pun">;}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">.</span><span class="pln">error</span><span class="pun">-</span><span class="pln">messages </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;display</span><span class="pun">:</span><span class="pln"> none</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;margin</span><span class="pun">:</span><span class="pln"> </span><span class="lit">0</span><span class="pln"> </span><span class="lit">10px</span><span class="pln"> </span><span class="lit">15px</span><span class="pln"> </span><span class="lit">10px</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;padding</span><span class="pun">:</span><span class="pln"> </span><span class="lit">8px</span><span class="pln"> </span><span class="lit">35px</span><span class="pln"> </span><span class="lit">8px</span><span class="pln"> </span><span class="lit">30px</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;color</span><span class="pun">:</span><span class="pln"> </span><span class="com">#B94A48;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> </span><span class="com">#F2DEDE;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid </span><span class="com">#EED3D7;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;border</span><span class="pun">-</span><span class="pln">radius</span><span class="pun">:</span><span class="pln"> </span><span class="lit">4px</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;fieldset </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border</span><span class="pun">:</span><span class="lit">1px</span><span class="pln"> solid</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; padding</span><span class="pun">:</span><span class="lit">20px</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;/style&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;form&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;fieldset&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;legend&gt;Submit with one or two&nbsp;invalid&nbsp;fields&lt;/legend&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="tag">&lt;ul</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"error-messages"</span><span class="tag">&gt;&lt;/ul&gt;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="tag"></span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"name"</span><span class="tag">&gt;</span><span class="pln">Name:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"name"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"name"</span><span class="pln"> </span><span class="atn">required</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;p&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"email"</span><span class="tag">&gt;</span><span class="pln">Email:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">required</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;p&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;button&gt;</span><span class="pln">Submit</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;/fieldset&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/form&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> replaceValidationUI</span><span class="pun">(</span><span class="pln">form</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Suppress the default bubbles</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; form</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">"invalid"</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">preventDefault</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Support Safari, iOS Safari, and the Android browser — each of which </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp;// do not prevent&nbsp;</span><span style="color: #880000; line-height: 28.4444465637207px; background-color: #eeeeee;">form submissions by default</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;form</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">"submit"</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(!</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">checkValidity</span><span class="pun">())</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event</span><span class="pun">.</span><span class="pln">preventDefault</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">});</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Container that holds error messages. By default it has a CSS </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp;// display:none property</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> errorMessages </span><span class="pun">=</span><span class="pln"> form</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">".error-messages"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> submitButton </span><span class="pun">=</span><span class="pln"> form</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"button:not([type=button]), </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; input[type=submit]"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;submitButton</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">"click"</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> invalidFields </span><span class="pun">=</span><span class="pln"> form</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"input:invalid"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var listHtml </span><span class="pun">=</span><span class="pln"> </span><span class="str">""<span style="color: #666600;" color="#666600">;</span></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var errorMessagesContainer </span><span class="pun">=</span><span class="pln"> form</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">".error-messages"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var label</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Get the labels' values of their name attributes + the validation error</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// message of the corresponding input field using the validationMessage</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// property of input fields</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// We build a list of &lt;li&gt;...&lt;/li&gt; that we add to the error message container</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> invalidFields</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label </span><span class="pun">=</span><span class="pln"> form</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"label[for="</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> invalidFields</span><span class="pun">[</span><span class="pln"> i </span><span class="pun">].</span><span class="pln">id </span><span class="pun">+</span><span class="pln"> </span><span class="str">"]"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;listHtml </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"&lt;li&gt;"</span><span class="pln"> </span><span class="pun">+</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="str">" "</span><span class="pln"> </span><span class="pun">+</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;invalidFields</span><span class="pun">[</span><span class="pln"> i </span><span class="pun">].</span><span class="pln">validationMessage </span><span class="pun">+</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="str">"&lt;/li&gt;"</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Update the list with the new error messages</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;errorMessagesContainer</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> listHtml</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// If there are errors, give focus to the first invalid field and show</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// the error messages container by setting its CSS property display=block</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">invalidFields</span><span class="pun">.</span><span class="pln">length </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; invalidFields</span><span class="pun">[</span><span class="pln"> </span><span class="lit">0</span><span class="pln"> </span><span class="pun">].</span><span class="pln">focus</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; errorMessagesContainer</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">display </span><span class="pun">=</span><span class="pln"> </span><span class="str">"block"</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">});</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Replace the validation UI for all forms</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> forms </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"form"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> forms</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;replaceValidationUI</span><span class="pun">(</span><span class="pln">forms</span><span class="pun">[</span><span class="pln"> i </span><span class="pun">]);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


__Explanations:__

+ _Line 32_: we added an empty unnumbered list (`<ul>`...`</ul>`) to the form, with the CSS class="error-messages". We will use this class attribute for styling, and hiding by default, the error messages using CSS (see _lines 12-20_, _line 13_ hides the messages by default).
+ _Lines 97-102_ look at all forms in the document and call a function that will replace the default validation behavior for all of them: the `replaceValidationUI(form)` function.
+ This function first disables all default behavior (no more display of bubbles during form submission), this is done at _lines 45-57_.
+ _Line 66_: we add a `click` listener to the submit button of the current form.
+ _Line 67_ gets all invalid input fields for that form,
+ _Lines 76-83_: For each invalid field, we get the value of the name attribute of the corresponding label, we also get the validation error message, and we build a list item(`<li>`...`</li>`).
+ _Line 86_: Then we add this list element (a formatted error message corresponding to an invalid input field) to the error message container.
+ _Lines 90-93_: The focus is given to the first invalid field that shows an error message.


### 5.7.6 Discussion and projects

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

Let us suggest some topics for discussion and optional projects:


#### Suggested topics

+ What do you think about the solution proposed at the end of the course? Why not use Bootstrap forms and have an easier life? Or maybe it's worth knowing the low level part and how Bootstrap implemented some of its features about form validation?
+ Have you heard of Web Components? Have you tried them? Also check this web site.


#### Optional projects

+ __Project 1 (easy):__ This time, let's systematically add some CSS3 rules for visual feedback as you type in your HTML5 input fields. Also try to implement in JavaScript some custom validation (i.e., password validation) and add custom error messages in bubbles (using the title attribute). 
+ __Project 2 (a bit harder):__ Investigate CSS3 transitions to make animated input fields (when they get the focus, when they become invalid). A good starting point is the small example that adds icons at the right of valid/invalid input fields, in section 5.7.2.
+ __Project 2 (harder):__ Modify a form of your own, so that it uses the custom techniques presented at the end of the course.


 