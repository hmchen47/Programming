# Week 5: HTML5 Forms


## 5.8 Exercises - Week 5


### 5.8.1 Intro exercises - Week 5

Here is your opportunity to show that you understand how Web forms work, and are ready to proceed with the rest of the course.

As stated in the grading policy page, the following 23 questions count towards 15% of your final grade.


### 5.8.2 Accessible forms (1-2)

1. Make me accessible

  <pre><b> - Version 1 -</b>
  &lt;label for="firstname"&gt;First Name:&lt;/label&gt;
  &lt;input type="text" id="firstname" /&gt;
  <br>
  <b>- Version 2 -</b>
  &lt;label&gt;
  First Name:
  &lt;input type="text" id="firstname/&gt;
  &lt;/label&gt;
  <br>
  <b>- Version 3 -</b>
  &lt;label for="firstname"&gt;First Name:
  &lt;input type="text" id="firstname" /&gt;
  &lt;/label&gt;
  <br>
  <b>- Version 4 -</b>
  &lt;label for="firstname"&gt;&lt;span lang="en"&gt;First Name:&lt;/span&gt;
  &lt;input type="text" id="firstname" /&gt;
  &lt;/label&gt;
  </pre>

  Which version of the source code above __does not__ follow best practices in terms of accessibilty?

  a. Version 1<br/>
  b. Version 2<br/>
  c. Version 3<br/>
  d. Version 4<br/>

  Ans: b<br/>
  Explanation: Version 2 does not follow good practices as the for attribute of the label is not present. It should always match the id attribute of the corresponding input field. All other versions are correct. The second answer is correct.



2. Group me!

  Which of the following elements is useful for grouping form controls (i.e related checkboxes)?

  a. fieldset<br/>
  b. summary and details<br/>
  c. legend<br/>
  d. table<br/>
  
  Ans: a<br/>
  Explanation: Out of these elements, only `fieldset` is useful for grouping form controls.



### 5.8.3 Input types (3-8)

3. Only 3 colors in the French flag!

  With `<input type="color">`, it is possible (on browsers that support it) to offer a restricted set of color choices. How do we achieve this?

  a. It is not possible, as this input field pops up the color chooser widget of the native operating system.<br/>
  b. By using a `datalist` element associated to the input field.<br/>
  c. By using the color attribute.<br/>
  
  Ans: b<br/>
  Explanation: On browsers that support it, using a `<datalist>` with some `<option>` elements inside, it is possible to restrict the choice of colors and also to simplify the user interface, as explained in section 5.4.2 of the course.



__Source code for the next question (4):__

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Example of date picker&lt;/title&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp;&lt;label for="birthDate"&gt;Enter your birth date: &lt;/label&gt;&lt;p&gt;</li>
<li><strong> &lt;input type="date" id="birthDate" &gt;</strong></li>
<li> &lt;p&gt;</li>
<li> You picked: &lt;span id="pickedDate"&gt;&lt;/span&gt;&lt;p&gt;</li>
<li> &lt;span id="pastFuture"&gt;&lt;/span&gt;</li>
<li> &lt;/p&gt; </li>
<li> &lt;script&gt;</li>
<li> var field = document.querySelector("#birthDate");</li>
<li> var result = document.querySelector("#pickedDate");</li>
<li> var pastFuture = document.querySelector("#pastFuture");</li>
<li> </li>
<li> field.oninput = function(evt) {</li>
<li> var date = this.value;</li>
<li>&nbsp;pickedDate.innerHTML = "&lt;b&gt;"+date+"&lt;/b&gt;";</li>
<li> </li>
<li> if(this.<strong>AAAAAAAAAAA</strong>&nbsp;&lt;= new Date()) {</li>
<li>&nbsp; &nbsp; &nbsp;pastFuture.style.color = 'green';</li>
<li>&nbsp; &nbsp; &nbsp;pastFuture.innerHTML = "&lt;b&gt;Date in the past, ok!&lt;/b&gt;" </li>
<li> } else {</li>
<li>&nbsp; &nbsp; pastFuture.style.color = 'red';</li>
<li>&nbsp; &nbsp; pastFuture.innerHTML = "&lt;b&gt;Date in the future, you're not even born!&lt;/b&gt;"</li>
<li> }</li>
<li> }</li>
<li> &lt;/script&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

4. Back to the future

  To check whether a selected date is in the past or in the future, what property should we test? Please enter below the exact name of the property you should put at line 23 instead of __AAAAAAAAAAA__ (11 characters. Be careful: type the exact name with lower and upper case at the right places).

  Ans: valueAsDate<br/>
  Explanation: The correct property for getting the date value as a JavaScript object comparable with the current date - as returned by new Date() - is: `valueAsDate`


5. HTML5 or not?

  Which of these input field types have been introduced with HTML5? (5 correct answers)

  a. text<br/>
  b. search<br/>
  c. url<br/>
  d. file<br/>
  e. email<br/>
  f. tel<br/>
  g. password<br/>
  h. range<br/>

  Ans: bcefh<br/>
  Explanation: `search`, `url`, `email`, `tel`, `range` are correct answers. Input fields of type text, file, password existed before html5. [Ref](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#%3Cinput%3E_types)



6. 35 = 7 x 5

  <pre>&lt;input type="number" value="25" min="0" step="5" max="500"/&gt;</pre>

  In the above code if we enter the value 7, will this make the field invalid? (Yes/No)

  Ans: Yes<br/>
  Explanation: The input field is valid only when multiples of the step value are entered. 7 is not a multiple of 5, so the field is invalid. The correct answer is "Yes" (the field is invalid).



7. Show me your value

  <pre>&lt;input id="slider1" type="range"
        min="100" max="500" step="10" value="150"
        oninput="printValue('slider1','rangeValue1')"/&gt;
     &lt;<b style="color:red">?</b> for="slider1" id="rangeValue1"&gt;&lt;/<b style="color:red">?</b>&gt;
  </pre>

  Which <strong> <u>new</u></strong> element introduced by HTML5 is often used to display the value of an `<input type="range">` element? Which element name would you put instead of the red "?" in the above code?

  a. p<br/>
  b. div<br/>
  c. output<br/>
  d. span<br/>

  Ans: c<br/>
  Explanation: The element introduced by HTML5, often used to display the value of a range attribute is... `<output>`! The other elements existed previously, before HTML5, and were not especially designed for displaying an input field's outputs.


8. Floating point range

  <figure style="margin: 0.5em; text-align: center;">
    <img style=" margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick="window.open('https://tinyurl.com/y6p74dyg')"
      src    ="https://tinyurl.com/y6nsftkf"
      alt    ="example of input type equal range with float value displayed"
      title  ="example of input type equal range with float value displayed"
    />
  </figure>

  <pre>&lt; input type="range" min=? max=? value=? step=? /&gt;</pre>

  <legend id="9f9ab7ecbfe140c2b93ec5ba7f30c844_2_1-legend"><input type="range"> can have a floating point value when we move the slider if...</legend>

  can have a floating point value when we move the slider if... (3 correct answers)

  a. The min attribute has a floating point value, even if the step attribute value is an integer,<br/>
  b. The step attribute is defined with step="any" or step=any,<br/>
  c. The step attribute has a floating point value, for example step="0.1",<br/>
  d. The value attribute is a floating point value, even if the value of the step attribute, and of the min attribute are integer values.<br/>

  Ans: <span style="color: magenta;">abc, xbcd<br/>
  Explanation: Answers 1, 2 and 3 are correct. 
    + Answer 3 is correct: if the step attribute value is a float, then we can have a floating point value for the input field when the slider is moved. 
    + Answer 2 is correct: with a value of "any", even if the min attribute is an integer, the value of the input field can be a float.
    + Answer 1 is also correct, the min attribute plays a role in the type of the input element's value: if min is a floating point value, and even if step is an integer, then the value of the input field will be a float. Example: min=0.4 step=1 will give 0.4, 1.4, 2.4 etc. Try with [this JS Bin example](http://jsbin.com/vowudo/edit?html,output).



### 5.8.4 Form attributes (9-15)

9. Please put me outside

  The form attribute of input fields is useful for putting input fields _outside the form itself._ This `form` attribute should match the value of another attribute in the `<form>` element the input field belongs to. Which one?

  a. form<br/>
  b. for<br/>
  c. id<br/>
  d. name<br/>

  Ans: c<br/>
  Explanation: The `form` attribute of input fields is useful for putting input fields outside the form itself. The `form` attribute of an external input field must share the same value as the `id` of the form the field belongs to. The correct answer is `id`.


__Source code for the next question (10):__

<div><ol>
<li value="1"> &lt;form submit="test.php" method="post" <strong>autocomplete="on"</strong>&gt;</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;&nbsp;&lt;label for="address"&gt;Enter your address:&lt;/label&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;input type="text" id="address"<span color="#000000" style="color: #000000;">&nbsp;<span style="color: #ff0000;"><strong>?</strong>&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;p&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;label for="address1"&gt;Enter your address:&lt;/label&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;input type="text" id="address1"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;p&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;button type="submit"&gt;Submit&lt;/button&gt;</li>
<li>&nbsp;<span color="#000088" style="color: #000088;">&nbsp; &nbsp;...</span></li>
<li> &lt;/form&gt;</li>
</ol></div>

10. Complete auto repair

  Suppose that the autocomplete feature has not been disabled in the browser preferences.

  In the above code, what would you put instead of the red "?" _at line 4_, if we do not want the browser to complete the user's input based on the history of the user's previous input?

  a. We should add focus="off".<br/>
  b. We should add autocomplete="off",<br/>
  c. Nothing, the autocompletion is not automatically turned on,<br/>

  Ans: b<br/>
  Explanation:
    + If applied to the `<form>` element, all input fields attached to the form (inside or linked to it using the form attribute), will have auto-completion set by default to the value of the autocomplete attribute of the form.
    + This default behavior can be overriden by setting it individually to any input field inside. In other words: it is possible to have autocomplete "on" for the form, and "off" for specific input fields, or vice-versa


11. Multiple focus...

  The `autofocus` attribute is useful for putting the focus to another field other than the first in a page/form (default behavior = the first input field has the focus).

  Can we have more than one input field in a form with the `autofocus` attribute? (Yes/No)

  Ans: No<br/>
  Explanation: Note: there cannot be more than one element in the document with the autofocus attribute specified! The second answer is "No".


12. Match my datalist!

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick="window.open('https://tinyurl.com/y5usqoxn')"
      src    ="https://tinyurl.com/y5w4c3c4"
      alt    ="combo bow with autocompletion"
      title  ="combo bow with autocompletion"
    />
  </figure>

  <pre>&lt;input list="browsers" id="mybrowser"/&gt;
  &lt;datalist ...&gt;
  ...
  &lt;/datalist&gt;
  </pre>

  The `list` attribute of the input field must match an attribute of the corresponding `datalist` element in order to make the local autocompletion work. Which one?

  a. id<br/>
  b. name<br/>
  c. list<br/>

  Ans: <span style="color: magenta;">a</span><br/>
  Explanation: The value of the `list` attribute of the input field must match the value of the `id` of the `<datalist>` element.


13. Give me the list!

  Which of these HTML elements can have the `list` attribute? (3 correct answers)

  a. ul<br/>
  b. input type=date<br/>
  c. li<br/>
  d. form<br/>
  e. input type=color<br/>
  f. input type=text<br/>

  Ans: <span style="color: magenta;">bef</span>, xbde<br/>
  Explanation: The `list` attribute is used with some input elements. In the above list, all proposed input types can have this attribute. Together with a `<datalist>` element, it can be used for autocompletion, or for restricting the proposed list of dates or colors.


14. Why :// ???? Why not :!! or ::@ or :-)

  <pre>&lt;input
      id="website"
      name="url"
      type="url"
      placeholder="http://www.domain.com"
      title="http, https or ftp allowed"
      pattern="(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*"
  /&gt;</pre>

  Which sort of input will make the above input field valid?

  a. Values that do not start with http://, https:// or ftp://, followed by any alphanumeric characters<br/>
  b. Values that start with http://, https:// or ftp://, followed by any alphanumeric characters<br/>
  c. Values that do not start with http, https or ftp, followed by any alphanumeric characters<br/>
  d. Values that start with http, https or ftp, followed by any alphanumeric characters<br/>

  Ans: b<br/>
  Explanation: This example from the course accepts only values that start with http://, https:// or ftp://, followed by any alphanumeric characters.



15. Do not spam me please!

  <pre>&lt;input type="email" name="myemail" <b>multiple</b>&gt;</pre>

  What does the multiple attribute mean here?

  a. A user can enter multiple email addresses separated by commas, with the same suffix. For example, values such as "michel@buffa.com, john@buffa.com" will make the field valid but "michel@buffa.com and john@smith.com" will not be valid<br/>
  b. A user can enter multiple email addresses separated by commas, and the field will be valid<br/>
  c. A user can enter multiple email addresses separated by one or more spaces - no commas - and the field will be valid<br/>

  Ans: <span style="color: magenta;">b</span>, xa<br/>
  Explanation: With the `<input type="email">`, the multiple attribute allows us to enter a set of addresses separated by commas, instead of just a single address. Entering several addresses will keep the input field valid.



### 5.8.5 Elements related to forms (16-18)

16. A * B = C

  <pre>&lt;form oninput="o.value=a.value*b.value"&gt;
      &lt;input type="number" name="a" id="a" value="2"&gt; x
      &lt;input type="number" name="b" id="b" value="3"&gt; =
      &lt;output <b style="color:red;">for="a b"</b> name="o"&gt;6&lt;/output&gt;
  &lt;/form&gt;
  </pre>

  Is the above code correct? (Yes/No)

  Ans: yes<br/>
  Explanation: Indeed, the value of the `for` attribute in red might look strange, but it is correct. The specification says that the `for` attribute of an input field can get as value "a space-separated list containing the elements' ids whose values went into the calculation". The correct answer is "Yes".


17. Find the element

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick="window.open('https://tinyurl.com/y6akl5km')"
      src    ="https://tinyurl.com/y49nr9xx"
      alt    ="small progress blue bar"
      title  ="small progress blue bar"
    />
  </figure>

  Which HTML5 element has been designed to show progress: download progress etc?

  a. input type="range"<br/>
  b. progress<br/>
  c. meter<br/>

  Ans: <span style="color: magenta;">b</span><br/>
  Explanation: The `<progress>` element is similar to `<meter>` but it is used for progress bars (i.e., a percentage of a file being uploaded, etc.). Example: `<progress id=pr value=50 min=0 max=100>`



18. Give me ticks

  The `<datalist>` element, when used with `<input type=range>`, is useful for?

  a. Adding ticks to the slider bar<br/>
  b . autocompletion<br/>

  Ans: <span style="color: magenta;">a</span>, xb<br/>
  Explanation: The `<datalist>` element can be used to display ticks when used together with an `<input type=range>`. See [this example at JS Bin](http://jsbin.com/xeravi/1/edit).


### 5.8.6 Form validation API (19-23)

__Source code for the next 2 questions (19 and 20):__

<div><ol>
<li value="1">&lt;html&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;title&gt;CSS3 pseudo-classes for form validation visual feedback&lt;/title&gt;</li>
<li>&nbsp; &nbsp;&lt;style&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>input</strong><strong>:invalid { background-color: lightPink;}</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>input</strong><strong>:valid { background-color:lightGreen; }</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>input</strong><strong>:required {border: 2px solid red;}</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>input</strong><strong>:optional {border: 2px solid green;}</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;fieldset {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border:1px solid;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; padding:20px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;.formLabel { display: inline-block; width: 140px; text-align: right; } </li>
<li>&nbsp; &nbsp;&lt;/style&gt;</li>
<li> &lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&lt;form&gt;</li>
<li> &lt;fieldset&gt;</li>
<li>&nbsp; &nbsp;&lt;legend&gt;Type invalid values and see the result&lt;/legend&gt;</li>
<li>&nbsp; &nbsp;&lt;label for="myEmail" class="formLabel"&gt;E-mail:&lt;/label&gt; </li>
<li>&nbsp; &nbsp;&lt;input <strong>type="email"</strong> id="myEmail" <strong>required</strong>/&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp;&lt;label for="myURL" class="formLabel"&gt;Homepage (URL):&lt;/label&gt; </li>
<li>&nbsp; &nbsp;&lt;input <strong>type="url"</strong> id="myURL" <strong>required</strong>/&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp;&lt;label for="myPhone" class="formLabel"&gt;Phone number:&lt;/label&gt; </li>
<li>&nbsp; &nbsp;&lt;input <strong>type="phone"</strong> id="myPhone" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>pattern</strong><strong>="[0-9]{3}-?[0-9]{3}-?[0-9]{4}"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; placeholder="e.g. 416-555-1234" <strong>required</strong>/&gt;</li>
<li>&nbsp; &nbsp;&lt;br&gt;</li>
<li>&nbsp; &nbsp;&lt;button&gt;Submit form&lt;/button&gt;&lt;br /&gt;</li>
<li> &lt;/fieldset&gt;</li>
<li>&lt;/form&gt;</li>
</ol></div>

19. To submit or not to submit, that is the question...

  If we enter incorrect values in multiple input fields and submit this form, what will happen?

  a. the form will not be submitted without any error message<br/>
  b. The form will not be submitted, a text bubble will appear next to the first invalid field of the form, showing an error message that explains why the field is invalid<br/>
  c. The form will be submitted, and all invalid form fields will show error bubbles<br/>

  Ans: b<br/>
  Explanation: The form will not be submitted, and only the first invalid field will show an error message in a small bubble. Safari is the only exception, as of June 2015. We must use a polyfill with this browser if we want it to behave correctly.



20. Change this color

  If we enter invalid entries in several input fields of this form, what will happen?

  a. Input fields will change their background color only when the form is submitted. The invalid fields will have a light pink background color while the valid ones will have a light green background color<br/>
  b. The invalid fields will have a light pink background color while the valid ones will have a light green background color. Colors will change on the fly, as the user is typing<br/>
  c. Only the first invalid field will have a light pink background color<br/>

  Ans: <span style="color: magenta;">b, xa<br/>
  Explanation: As a user types, the input field will inherit the CSS pseudo classes `:invalid` or `:valid`. There is no need to submit the form, these CSS pseudo classes are added on the fly. As the source code of the example contains CSS rules for `input:valid` and `input:invalid`, the background color of the fields will change on the fly, as the user enters values.


21. Additional error messages

  Errors in form input fields may be displayed in small bubbles. Which input field attribute can be used to add additional text to the default error messages?

  a. no attribute can do that<br/>
  b. title<br/>
  c. error<br/>

  Ans: b<br/>
  Explanation: Adding a `title` attribute to input fields is good practice: it will display additional text in the message located in the small bubbles that will pop up when the field is invalid (after at least one submission of the form).


22. Bubble style

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick="window.open('https://tinyurl.com/y5mqxm3q')"
      src    ="https://tinyurl.com/y4lzxvs2"
      alt    ="3 different error message in bubbles"
      title  ="3 different error message in bubbles"
    />
  </figure>

  Is there a standard way to style - using CSS - the look'n'feel of the error message bubbles? (Yes/No)

  Ans: No<br/>
  Explanation: How can we change the style of the bubbles in a standard way, without using JavaScript? Unfortunately we can’t.


23. Custom validation

  <pre>&lt;script&gt;
    function checkPasswords() {
        var password1 = document.getElementById('password1');
        var password2 = document.getElementById('password2');
        if (password1.value != password2.value) {
            <b style="color:red">password2.?('Passwords do not match!');</b>
        } else {
          <b style="color:red">password2.?('');</b>
        }
    }
  &lt;/script&gt;
  </pre>  

  The HTML5 validation API proposes a method available on input DOM objects. This method allows you to customize error messages displayed in the bubbles that pop up when a field is invalid.

  What is the name of this method? look at the bold red lines in the source code above...

  a. setCustomValidity<br/>
  b. setError<br/>
  c. error<br/>

  Ans: a<br/>
  Explanation: The validity API proposes a `setCustomValidity()` method available on input DOM objects. This method allows you to customize error messages. It takes a string parameter. When this string is empty, the element is considered valid, when the string is not empty, the field is invalid and the validation error message displayed in the bubble will be equal to that string.


