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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Example of date picker</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"birthDate"</span><span class="tag">&gt;</span><span class="pln">Enter your birth date: </span><span class="tag">&lt;/label&gt;&lt;p&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"date"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"birthDate"</span><span class="pln"> </span><span class="tag">&gt;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> You picked: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"pickedDate"</span><span class="tag">&gt;&lt;/span&gt;&lt;p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"pastFuture"</span><span class="tag">&gt;&lt;/span&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/p&gt;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> field </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#birthDate"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> result </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#pickedDate"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> pastFuture </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#pastFuture"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> field</span><span class="pun">.</span><span class="pln">oninput </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> date </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;pickedDate</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;b&gt;"</span><span class="pun">+</span><span class="pln">date</span><span class="pun">+</span><span class="str">"&lt;/b&gt;"</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">if</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.<strong>AAAAAAAAAAA</strong></span><span class="pln">&nbsp;</span><span class="pun">&lt;=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Date</span><span class="pun">())</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;pastFuture</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;pastFuture</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;b&gt;Date in the past, ok!&lt;/b&gt;"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; pastFuture</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; pastFuture</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;b&gt;Date in the future, you're not even born!&lt;/b&gt;"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
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

  Which <strong<<u>new</u></strong> element introduced by HTML5 is often used to display the value of an `<input type="range">` element? Which element name would you put instead of the red "?" in the above code?

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

  <legend id="9f9ab7ecbfe140c2b93ec5ba7f30c844_2_1-legend" class="response-fieldset-legend field-group-hd"><input type="range"> can have a floating point value when we move the slider if...</legend>

  can have a floating point value when we move the slider if... (3 correct answers)

  a. The min attribute has a floating point value, even if the step attribute value is an integer,<br/>
  b. The step attribute is defined with step="any" or step=any,<br/>
  c. The step attribute has a floating point value, for example step="0.1",<br/>
  d. The value attribute is a floating point value, even if the value of the step attribute, and of the min attribute are integer values.<br/>

  Ans: <span style="color: magenta;">abc</span>, xbcd<br/>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;form</span><span class="pln"> </span><span class="atn">submit</span><span class="pun">=</span><span class="atv">"test.php"</span><span class="pln"> </span><span class="atn">method</span><span class="pun">=</span><span class="atv">"post"</span><span class="pln"> </span><strong><span class="atn">autocomplete</span><span class="pun">=</span><span class="atv">"on"</span></strong><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"address"</span><span class="tag">&gt;</span><span class="pln">Enter your address</span><span class="pln">:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"address"<span color="#000000" style="color: #000000;">&nbsp;<span style="color: #ff0000;"><strong>?</strong></span></span></span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;p&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"address1"</span><span class="tag">&gt;</span><span class="pln">Enter your address</span><span class="pln">:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"address1"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;p&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"submit"</span><span class="tag">&gt;</span><span class="pln">Submit</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;<span color="#000088" style="color: #000088;">&nbsp; &nbsp;...</span></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/form&gt;</span></li>
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
  a. name<br/>
  a. list<br/>

  Ans: a<br/>
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

  Ans: b<br/>
  Explanation: The `<progress>` element is similar to `<meter>` but it is used for progress bars (i.e., a percentage of a file being uploaded, etc.). Example: `<progress id=pr value=50 min=0 max=100>`



18. Give me ticks

  The `<datalist>` element, when used with `<input type=range>`, is useful for?

  a. Adding ticks to the slider bar<br/>
  a. autocompletion<br/>

  Ans: <span style="color: magenta;">a</span>, xb<br/>
  Explanation: The `<datalist>` element can be used to display ticks when used together with an `<input type=range>`. See [this example at JS Bin](http://jsbin.com/xeravi/1/edit).





