# Week 5: HTML5 Forms


## 5.7 Form validation API


### 5.7.0 Lecture Notes




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


#### Use the title attribute for specifying a custom message

You can simply use the input's title attribute to provide a message for pattern-mismatches, and more generally for all validation errors. This solution is really neat and doesn't require JavaScript!

Try the [online example at JSBin](https://jsbin.com/locedoy/1/edit?html,output), or try it here in your browser (type invalid values and look at the custom messages): ([Local Example - title](src/5.7.2-example3.html))

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





