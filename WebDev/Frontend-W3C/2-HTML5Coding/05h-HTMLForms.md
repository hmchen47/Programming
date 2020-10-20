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



Source code for the next question (4):
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







