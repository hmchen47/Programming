# Week 5: HTML5 Forms


## 5.7 Form validation API


### 5.7.0 Lecture Notes

+ [Visual feedback](#572-automatic-visual-feedback-while-typing)
  + most modern browsers proposing default behavior for validating input fields and forms
  + built-in validation system: HTML5 automatically add a CSS pseudo class to all input fields
  + invalid fields: inherit the `:invalid` pseudo class
  + valid fields: inherit the `:valid` pseudo class
  + improving your HTML form
    + adding some CSS rules to input fields
    + adding visual feedback to the validity of input field values, e.g.,
      + changing the color of the border of input fields
      + green/red icons on the right of the field
    + submitting the form: extra messages displayed as pop up text bubbles
      + default: providing default feedback on the input field's border
      + overridden by CSS rules
  + __<mark style="color: black; background-color: lightpink;">best practice</mark>__: ALWAYS provide default CSS rules that give visual feedback to the user's input
  + example: styling "required", "valid" and "invalid" fields 

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
        <label for="myEmail">E-mail:</label>
          <input type="email" id="myEmail" required/><br>
        <label for="myURL">Homepage (URL):</label> 
          <input type="url" id="myURL" required/><br>
        <label for="myPhone">Phone number:</label> 
          <input type="tel" id="myPhone" pattern="[0-9]{3}-?[0-9]{3}-?[0-9]{4}"
          placeholder="e.g. 416-555-1234" required/><br>
          <button>Submit form</button><br/>
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

+ [`title` attribute for customized message](#use-the-title-attribute-for-specifying-a-custom-message)
  + simply using the input's title attribute to provide a message for pattern-mismatches
  + more generally for all validation errors
  + really neat and no JavaScript required
  + e.g., `<input type="email" id="myEmail" title="You don't know what an email address looks like, do you?" required/><br>`
  + browser dependent:
    + Chrome & Opera: display the `title` attribute value in error message bubbles
    + Safari and FireFox: ignore the `title` attribute
  + references:
    + [Cross Browser Styling of HTML5 Forms — Even In Older Browsers](https://tinyurl.com/ccyho8c)
    + [Creating Cross Browser HTML5 Forms Now, Using modernize, webforms2 and html5Forms](https://tinyurl.com/c9omt6n)
 
+ [Javascript form validation](#573-javascript-form-validation-api)
  + allowing developers to use their own validation algorithm and customize error messages
  + together w/ some HTML/CSS/JavaScript to make own message bubbles
  + example: password checking

    ```html
    <form>
      <fieldset>
        <legend>Example use of the validation API</legend>
        <label for="password1" >Password:</label> <input type="password" 
          id="password1" oninput="checkPasswords()" required>
        <p>
          <label for="password2">Repeat password:</label>
          <input type="password" id="password2" oninput="checkPasswords()" required>
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

+ [validationMessage property](#the-validationmessage-property)
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
    + add an empty unnumbered list (`<ul>`...`</ul>`) to the form in style: `<ul></ul>`
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
          label = form.querySelector("label[for=" + invalidFields[i].id + "]");
          listHtml += "<li>" + label.innerHTML + " " + invalidFields[i].validationMessage + "</li>";
      }
      ```

    + update the list with the new error messages: `errorMessagesContainer.innerHTML = listHtml;`
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

<div><form><fieldset><legend>Type invalid values and submit form to see the result</legend> <label for="myEmail">E-mail:</label> <input id="myEmail" required="" type="email"><br> <label for="myURL">Homepage (URL):</label> <input id="myURL" required="" type="url"><br> <label for="myPhone">Phone number:</label> <input id="myPhone" required="" placeholder="e.g. 416-555-1234" pattern="[0-9]{3}-?[0-9]{3}-?[0-9]{4}" type="phone"><br> <button>Submit form</button></fieldset></form></div>

Source code extract:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&nbsp; &lt;head&gt;</li>
<li>&nbsp; &nbsp; &lt;meta charset="utf-8"&gt;</li>
<li>&nbsp; &nbsp; &lt;title&gt;CSS3 pseudo-classes for form validation visual feedback&lt;/title&gt;</li>
<li>&nbsp; &nbsp; &lt;style&gt;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; input:invalid { background-color: lightPink;}</li>
<li>&nbsp; &nbsp; &nbsp; input:valid { background-color:lightGreen; }</li>
<li>&nbsp; &nbsp; &nbsp; input:required {border: 2px solid red;}</li>
<li>&nbsp; &nbsp; &nbsp; input:optional {border: 2px solid green;}</li>
<li>&nbsp; &nbsp; &nbsp; fieldset {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; border:1px solid;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; padding:20px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; }</li>
<li>&nbsp; &nbsp; &nbsp; .formLabel { display: inline-block; width: 140px; text-align: right; } </li>
<li>&nbsp; &nbsp; &lt;/style&gt;</li>
<li>&nbsp; &lt;/head&gt;</li>
<li>&nbsp; &lt;body&gt;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &lt;form&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;fieldset&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;legend&gt;Type invalid values and see the result&lt;/legend&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;label for="myEmail" class="formLabel"&gt;E-mail:&lt;/label&gt; &lt;input type="email" id="myEmail" required/&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;label for="myURL" class="formLabel"&gt;Homepage (URL):&lt;/label&gt; &lt;input type="url" id="myURL" required/&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;label for="myPhone" class="formLabel"&gt;Phone number:&lt;/label&gt; &lt;input type="tel" id="myPhone" pattern="[0-9]{3}-?[0-9]{3}-?[0-9]{4}" &nbsp;&nbsp; &nbsp; &nbsp; placeholder="e.g. 416-555-1234" required/&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;button&gt;Submit form&lt;/button&gt;&lt;br /&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;/fieldset&gt;</li>
<li>&nbsp; &nbsp; &lt;/form&gt;</li>
<li>&nbsp; &lt;p&gt;</li>
<li>&nbsp;</li>
<li>&nbsp; &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
<li>&nbsp;</li>
</ol></div>
 
Try the online example with different Web browsers, both with and without the CSS rules. See the differences between FireFox/Chrome/Opera in the default visual feedback behavior. Don't worry: all default behavior can be overridden if you provide your own CSS rules.

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong><span style="color: #ff0000;"><mark style="color: black; background-color: lightpink;">best practice</mark></span>: &nbsp;We recommend that&nbsp;you ALWAYS&nbsp;provide default CSS rules that give visual feedback to the user's input.</strong></p>


__Example #2: add CSS transitions + an icon/marker to the right of the input fields__

Try this [online example at JSBin](https://jsbin.com/zaxije/2/edit) or try it here in your browser. This example adds a small icon that changes depending on the validity of the input field: ([Local Example - Validation](src/5.7.2-example2.html))

<div><form><fieldset><legend>Type invalid values and see the result</legend> <label for="myEmail">E-mail:</label> <input id="myEmail" required="" type="email"><br> <label for="myURL">Homepage (URL):</label> <input id="myURL" required="" type="url"><br> <label for="myPhone">Phone number:</label> <input id="myPhone" required="" placeholder="e.g. 416-555-1234" pattern="[0-9]{3}-?[0-9]{3}-?[0-9]{4}" type="phone"><br> <button>Submit form</button></fieldset></form></div>

Source code extract:

<div><ol>
<li value="1">.myForm input:focus {</li>
<li>&nbsp; <strong>&nbsp;padding</strong><strong>-right:70px;</strong></li>
<li>}</li>
<li> .myForm input {</li>
<li>&nbsp; <strong>&nbsp;transition</strong><strong>: padding .25s;</strong></li>
<li>}</li>
<li> </li>
<li>.myForm <strong>input</strong><strong>:required:valid </strong>{ </li>
<li>&nbsp; &nbsp;background:url('https://i.imgur.com/BJolppS.png') no-repeat right top;</li>
<li>}</li>
<li>.myForm <strong>input</strong><strong>:required </strong>{</li>
<li>&nbsp; &nbsp;background:url('https://i.imgur.com/7pIN7wz.png') no-repeat right top;</li>
<li>}</li>
</ol></div>

This time, we just added an attribute `class="myForm"` to our form, in order to avoid interfering with the other examples on this page, and we tweaked the CSS rules a little.

The rule at _line 1_ says that any time we click on an input field, it will enlarge itself to the right, while the rule at _line 4_ will make it animated.

The rules at _lines 8_ and _11_ target the input fields with a `required` attribute. They will change the background by displaying a small green or red icon, corresponding to the valid/invalid status of the input field.


#### Use the `title` attribute for specifying a custom message

You can simply use the input's `title` attribute to provide a message for pattern-mismatches, and more generally for all validation errors. This solution is really neat and doesn't require JavaScript!

Try the [online example at JSBin](https://jsbin.com/locedoy/1/edit?html,output), or try it here in your browser (type invalid values and look at the custom messages): ([Local Example - Message](src/5.7.2-example3.html))

<div><form><fieldset><legend>Type invalid values and see the result, this time with custom messages!&nbsp;</legend> <label for="myEmail">E-mail:</label> <input title="You don't know what an email address looks like do you?" id="myEmail" required="" type="email"><br> <label for="myURL">Homepage (URL):</label> <input title="Please start with HTTP or HTTPS or you'll never get your degree!" id="myURL" required="" type="url"><br> <label for="myPhone">Phone number:</label> <input title="can't you read the provided example?" id="myPhone" required="" placeholder="e.g. 416-555-1234" pattern="[0-9]{3}-?[0-9]{3}-?[0-9]{4}" type="phone"><br> <button>Submit form</button></fieldset></form></div>

Extract from source code:

<div><ol>
<li value="1">&lt;form class="myForm"&gt;</li>
<li>&nbsp;&nbsp;&lt;fieldset&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;legend&gt;Type invalid values and see the result&lt;/legend&gt;</li>
<li>&nbsp; &nbsp; &lt;label for="myEmail" class="formLabel"&gt;E-mail:&lt;/label&gt; </li>
<li>&nbsp; &nbsp; &lt;input type="email" id="myEmail" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>title="You don't know what an email address looks like, do you?"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;required/&gt;&lt;br&gt;</li>
<li>...</li>
<li>&nbsp; &nbsp;&nbsp;&lt;button&gt;Submit form&lt;/button&gt;&lt;br /&gt;</li>
<li>&nbsp;&nbsp;&lt;/fieldset&gt;</li>
<li>&lt;/form&gt;</li>
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

<div><form><fieldset><legend>Example use of the validation API, enter different passwords and submit&nbsp;</legend> <label for="password1">Password:</label> <input id="password1" required="" oninput="checkPasswords()" type="password" style="background-image: url(&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACIUlEQVQ4EX2TOYhTURSG87IMihDsjGghBhFBmHFDHLWwSqcikk4RRKJgk0KL7C8bMpWpZtIqNkEUl1ZCgs0wOo0SxiLMDApWlgOPrH7/5b2QkYwX7jvn/uc//zl3edZ4PPbNGvF4fC4ajR5VrNvt/mo0Gr1ZPOtfgWw2e9Lv9+chX7cs64CS4Oxg3o9GI7tUKv0Q5o1dAiTfCgQCLwnOkfQOu+oSLyJ2A783HA7vIPLGxX0TgVwud4HKn0nc7Pf7N6vV6oZHkkX8FPG3uMfgXC0Wi2vCg/poUKGGcagQI3k7k8mcp5slcGswGDwpl8tfwGJg3xB6Dvey8vz6oH4C3iXcFYjbwiDeo1KafafkC3NjK7iL5ESFGQEUF7Sg+ifZdDp9GnMF/KGmfBdT2HCwZ7TwtrBPC7rQaav6Iv48rqZwg+F+p8hOMBj0IbxfMdMBrW5pAVGV/ztINByENkU0t5BIJEKRSOQ3Aj+Z57iFs1R5NK3EQS6HQqF1zmQdzpFWq3W42WwOTAf1er1PF2USFlC+qxMvFAr3HcexWX+QX6lUvsKpkTyPSEXJkw6MQ4S38Ljdbi8rmM/nY+CvgNcQqdH6U/xrYK9t244jZv6ByUOSiDdIfgBZ12U6dHEHu9TpdIr8F0OP692CtzaW/a6y3y0Wx5kbFHvGuXzkgf0xhKnPzA4UTyaTB8Ph8AvcHi3fnsrZ7Wore02YViqVOrRXXPhfqP8j6MYlawoAAAAASUVORK5CYII=&quot;); background-repeat: no-repeat; background-attachment: scroll; background-size: 16px 18px; background-position: 98% 50%;">
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

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&nbsp; &lt;head&gt;</li>
<li>&nbsp; &nbsp; &lt;meta charset="utf-8"&gt;</li>
<li>&nbsp; &nbsp; &lt;title&gt;Example of using the validation API&lt;/title&gt;</li>
<li>&nbsp; &nbsp; &lt;style&gt;</li>
<li>&nbsp; &nbsp; &nbsp; .myForm input:invalid { background-color: lightPink;}</li>
<li>&nbsp; &nbsp; &nbsp; .myForm input:valid { background-color:lightGreen; }</li>
<li>&nbsp; &nbsp; &nbsp; .myForm input:required {border: 2px solid red;}</li>
<li>&nbsp; &nbsp; &nbsp; .myForm input:optional {border: 2px solid green;}</li>
<li>&nbsp; &nbsp; &nbsp; .myForm label { display: inline-block; width: 140px; text-align: right; } </li>
<li>&nbsp; &nbsp; &lt;/style&gt;</li>
<li>&nbsp; &lt;/head&gt;</li>
<li>&nbsp; &lt;body&gt;</li>
<li>&nbsp; &nbsp; &lt;form class="myForm"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;fieldset&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;legend&gt;Example use of the validation API&lt;/legend&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;label for="password1" &gt;Password:&lt;/label&gt; &lt;input type="password" id="password1" oninput="checkPasswords()" required&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;p&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;label for="password2"&gt;Repeat password:&lt;/label&gt; &lt;input type="password" id="password2" oninput="checkPasswords()" required&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;p&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;button&gt;Submit&lt;/button&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;/fieldset&gt;</li>
<li>&nbsp; &nbsp; &lt;/form&gt;</li>
<li>&nbsp;</li>
<li>&nbsp; &lt;script&gt; </li>
<li>&nbsp; function checkPasswords() {</li>
<li>&nbsp; &nbsp; var password1 = document.getElementById('password1');</li>
<li>&nbsp; &nbsp; var password2 = document.getElementById('password2');</li>
<li>&nbsp; &nbsp; if (password1.value != password2.value) {</li>
<li>&nbsp; &nbsp; &nbsp; password2.setCustomValidity('Passwords non identiques');</li>
<li>&nbsp;&nbsp; &nbsp; } else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; password2.setCustomValidity('');</li>
<li>&nbsp; &nbsp; &nbsp; }</li>
<li>&nbsp; &nbsp; }</li>
<li>&nbsp; &lt;/script&gt;</li>
<li>&nbsp; &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


__Explanations:__

The validity API proposes a `setCustomValidity()` method available on input DOM objects. This method allows you to customize error messages. It takes a string parameter. When this string is empty, the element is considered valid, when the string is not empty, the field is invalid and the validation error message displayed in the bubble will be equal to that string.

At lines 18 and 20 we added an input event listener: each time a key is typed, the `checkPasswords()` function is called.

Lines 28 and 29 get the input fields' values, and lines 30-35 check if the passwords are the same and set the validity of the field using the validation API's method `setCustomValidity(error_message)`.


### 5.7.4 The validity property of input fields

The `validity` property of input fields helps to get error details when the field is _invalid_. This property tests the different types of validation error.

Here is how to get the `validity` property of an input field:

<div><ol>
<li value="1">var input = document.getElementById('IdOfField');</li>
<li> </li>
<li>var validityState_object =<strong> input.validity;</strong></li>
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

<div>
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
<form><label for="b">Enter a value between 10 and 20 </label> <input name="text" id="b" required="" oninput="validate()" min="10" max="20" type="number"> <input value="Submit Query" type="submit"></form></div>
 
Source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>...</li>
<li>&lt;body&gt;</li>
<li> </li>
<li> &lt;script&gt;</li>
<li> function validate() {</li>
<li>&nbsp; &nbsp; &nbsp;var input = document.getElementById('b');</li>
<li>&nbsp; &nbsp; <strong>&nbsp;var</strong><strong> validityState_object = input.validity;</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;if(validityState_object.valueMissing) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input.setCustomValidity('Please set an age (required)'); </li>
<li>&nbsp; &nbsp; &nbsp;} else if (<span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.rangeUnderflow) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input.setCustomValidity('Your value is too low');</li>
<li>&nbsp; &nbsp; &nbsp;} else if (<span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.rangeOverflow) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input.setCustomValidity('Your value is too high');</li>
<li>&nbsp; &nbsp; &nbsp;} else if (<span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.typeMismatch) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input.setCustomValidity('Type mismatch');</li>
<li>&nbsp; &nbsp; &nbsp;} else if (<span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.tooLong) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input.setCustomValidity('Too long');</li>
<li>&nbsp; &nbsp; &nbsp;} else if (<span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.stepMismatch) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input.setCustomValidity('stepMismatch');</li>
<li>&nbsp; &nbsp; &nbsp;} else if (<span style="color: #3d64ff; line-height: 23.2727279663086px;">validityState_object</span>.patternMismatch) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input.setCustomValidity('patternMismatch');</li>
<li>&nbsp; &nbsp; &nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;input.setCustomValidity('');</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> }</li>
<li> &lt;/script&gt;</li>
<li> &lt;form class="myForm"&gt;</li>
<li> &lt;label for="b"&gt;Enter a value between 10 and 20: &lt;/label&gt; </li>
<li>&nbsp;</li>
<li> &lt;input type="number" name="text" id="b"&nbsp;min="10" max="20"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;required <strong>oninput='validate();'</strong>/&gt; </li>
<li> &lt;button&gt;Submit&lt;/button&gt;</li>
<li> &lt;/form&gt;</li>
<li> </li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


#### The `validationMessage` property

It is also possible to get the validation error message, using the `validationMessage` property of input fields.

<div><ol>
<li value="1">var input = document.getElementById('b');</li>
<li>&nbsp;</li>
<li>console.log("Validation message = " +<strong> input.</strong><strong>validationMessage</strong>);</li>
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

<div><form><fieldset>
<ul></ul>
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

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;meta charset="utf-8"&gt;</li>
<li>&nbsp; &nbsp;&lt;title&gt;Aggregating error messages&lt;/title&gt;</li>
<li>&nbsp; &nbsp;&lt;style&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;input:invalid { background-color: lightPink;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;input:valid { background-color:lightGreen; }</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;input:required {border: 2px solid red;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;input:optional {border: 2px solid green;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;.error-messages {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;display: none;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;margin: 0 10px 15px 10px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;padding: 8px 35px 8px 30px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;color: #B94A48;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;background-color: #F2DEDE;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;border: 2px solid #EED3D7;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;border-radius: 4px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;fieldset {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border:1px solid;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; padding:20px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;&nbsp;&lt;/style&gt;</li>
<li> &lt;/head&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;form&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;fieldset&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;legend&gt;Submit with one or two&nbsp;invalid&nbsp;fields&lt;/legend&gt;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>&lt;ul class="error-messages"&gt;&lt;/ul&gt;</strong></li>
<li><strong></strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;label for="name"&gt;Name:&lt;/label&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;input id="name" name="name" required&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;p&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;label for="email"&gt;Email:&lt;/label&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;input id="email" name="email" type="email" required&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;p&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;button&gt;Submit&lt;/button&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;/fieldset&gt;</li>
<li> &lt;/form&gt;</li>
<li>&nbsp;</li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp;&nbsp;function replaceValidationUI(form) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Suppress the default bubbles</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; form.addEventListener("invalid", function (event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.preventDefault();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}, true);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Support Safari, iOS Safari, and the Android browser — each of which </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// do not prevent&nbsp;<span style="color: #880000; line-height: 28.4444465637207px; background-color: #eeeeee;">form submissions by default</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;form.addEventListener("submit", function (event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;if (!this.checkValidity()) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event.preventDefault();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;});</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Container that holds error messages. By default it has a CSS </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// display:none property</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var errorMessages = form.querySelector(".error-messages");</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var submitButton = form.querySelector("button:not([type=button]), </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; input[type=submit]");</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;submitButton.addEventListener("click", function (event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var invalidFields = form.querySelectorAll("input:invalid");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var listHtml = ""<span style="color: #666600;" color="#666600">;</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var errorMessagesContainer = form.querySelector(".error-messages");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var label;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Get the labels' values of their name attributes + the validation error</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// message of the corresponding input field using the validationMessage</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// property of input fields</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// We build a list of &lt;li&gt;...&lt;/li&gt; that we add to the error message container</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;for (var i = 0; i &lt; invalidFields.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label = form.querySelector("label[for=" + invalidFields[ i ].id + "]");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;listHtml += "&lt;li&gt;" +</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label.innerHTML +</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;" " +</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;invalidFields[ i ].validationMessage +</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"&lt;/li&gt;";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Update the list with the new error messages</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;errorMessagesContainer.innerHTML = listHtml;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// If there are errors, give focus to the first invalid field and show</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// the error messages container by setting its CSS property display=block</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if (invalidFields.length &gt; 0) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; invalidFields[ 0 ].focus();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; errorMessagesContainer.style.display = "block";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;});</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// Replace the validation UI for all forms</li>
<li>&nbsp; &nbsp;var forms = document.querySelectorAll("form");</li>
<li> </li>
<li>&nbsp; &nbsp;for (var i = 0; i &lt; forms.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;replaceValidationUI(forms[ i ]);</li>
<li>&nbsp; &nbsp;}</li>
<li> &lt;/script&gt;</li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


__Explanations:__

+ _Line 32_: we added an empty unnumbered list (`<ul>`...`</ul>`) to the form, with the CSS. We will use this class attribute for styling, and hiding by default, the error messages using CSS (see _lines 12-20_, _line 13_ hides the messages by default).
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


 