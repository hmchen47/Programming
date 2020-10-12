# Week 5: HTML5 Forms


## 5.3 Accessible forms


### 5.3.0 Lecture Notes

+ [Accessible forms](#531-accessible-forms)
  + forms: commonly used to enable user interaction in Web sites and Web applications
  + guidelines for forms accessibility
    + a descriptive label provided and using the `<label>` element to identify each form control
    + using the `<fieldset>` and `<legend>` elements to respectively group and associate related form controls
  + [importance of accessibility](#532-why-is-this-important)
    + cognitive disability: better understand the form & how to complete it
    + speech input: using labels via voice commands to activate controls and move the focus tot he field
    + limit dexterity: large clickable areas
    + screen reader: identify and understand form controls more easily

+ [Forms Concepts](https://www.w3.org/WAI/tutorials/forms/)
  + __Labeling Controls:__ using the `<label>` element, and, in specific cases, other mechanisms to identify each form control
  + __Grouping Controls:__ using the `<fieldset>` and `<legend>` elements to group and associate related form controls
  + __Form Instructions__: providing instructions to help users understand how to complete the form and individual form controls
  + __Validating Input:__ validating input provided by the user and providing options to undo changes and confirm data entry
  + __User Notifications:__ notifying users about successful task completion, any errors, and providing instructions to help them correct mistakes
  + __Multi-Page Forms:__ dividing long forms into multiple smaller forms that constitute a series of logical steps or stages and inform users about their progress
  + __Custom Controls:__ using stylized form elements and other progressive enhancement techniques to provide custom controls



### 5.3.1 Accessible forms

Forms are commonly used to enable user interaction in Web sites and Web applications. For example, they are used for login, registering, commenting, and purchasing.

Since HTML5 provides functionalities to assist with accessibility, developers should make a concerted effort to mark up Web based forms. The following two guidelines are to give you a good start to make your forms accessible:

1. For every form field, ensure that a descriptive __label__ is provided and use the `<label> `element to identify each form control.
2. For larger or complex forms, use the `<fieldset>` and `<legend>` elements to respectively __group and associate__ related form controls.

Examples for each of these two basic guidelines are given in the following pages.


#### Further reading

The WAI Web site hosts a [Forms tutorial](https://www.w3.org/WAI/tutorials/forms/) where to find all guidelines to follow in order to make your forms truly accessible: labeling controls, grouping controls, form instructions, validating input, user notifications, multi-page forms, and custom controls.


### 5.3.2 Why is this important?

Forms can be visually and cognitively complex and difficult to use. Accessible forms are easier to use for everyone, including people with disabilities.

+ __People with cognitive disabilities__ can better understand the form and how to complete it, as making forms accessible improves the layout structure, instructions, and feedback.

+ __People using speech input__ can use the labels via voice commands to activate controls and move the focus to the fields that they need to complete.

+ __People with limited dexterity__ benefit from large clickable areas that include the labels, especially for smaller controls, such as radio buttons and checkboxes.

+ __People using screen readers__ can identify and understand form controls more easily because they are associated with labels, field sets, and other structural elements.


### 5.3.3 Labeling controls

#### Labels need to describe the purpose of the form control

Form fields and other form controls usually have visible labels, such as "E-mail Address:" as the label for a text field (see figure below).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y3g7fgkr')"
    src    ="https://tinyurl.com/y285thud"
    alt    ="form label text"
    title  ="form label text"
  />
</figure>

When these labels are marked up correctly, people can interact with them using only the keyboard, using voice input, and using screen readers. Also, the label itself becomes clickable, which enables a person who has difficulty clicking on small radio buttons or checkboxes to click anywhere on the label text.


#### Associating labels explicitly

Whenever possible, use the label element to explicitly associate text with form elements. The for attribute of the label must exactly match the id of the form control. 

__Example #1__

Click on the label, not on the input field to see the effect.

<p class="exampleHTML"><label class="label" for="first_name">First name: </label> <input name="firstname" id="first_name" type="text"></p>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"first_name"</span><span class="tag">&gt;</span><span class="pln">Your First Name</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"first_name"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"fname"</span><span class="tag">/&gt;</span></li>
</ol></div>


__Example #2__

Note that you can also include the `<input>` element inside the `<label>`...`</label>` element, and also add a `<span lang="en">` for example, to indicate the language used in the label. Sometimes, [nesting labels and inputs can also make CSS styling easier and produce better results with screen readers](https://tinyurl.com/yywsbnpg).

Source code (with `<input>` inside the `<label>`):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"first_name"</span><span class="tag">&gt;&lt;</span></strong><span class="pln"><strong>span lang=en"&gt;</strong>Your First Name</span><strong><span class="tag">&lt;/span&gt;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"first_name"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"fname"</span><span class="tag">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="tag">&lt;/label&gt;</span></strong></li>
</ol></div>

__Example #3__

Click on the label "Subscribe to newsletter" to see what this does.

<p class="exampleHTML"><label class="label" for="firstname">First name: </label> <input name="firstname" id="firstname" type="text"><br><label class="label" for="subscribe">Subscribe to newsletter</label> <input name="subscribe" id="subscribe" type="checkbox"></p>

 
Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"firstname"</span><span class="tag">&gt;</span><span class="pln">First name:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"firstname"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"firstname"</span><span class="tag">&gt;&lt;br&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;label</span><span class="pln">&nbsp;</span><span class="atn">for</span><span class="pun">=</span><span class="atv">"subscribe"</span><span class="tag">&gt;</span><span class="pln">Subscribe to newsletter</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"checkbox"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"subscribe"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"subscribe"</span><span class="tag">&gt;</span></li>
</ol></div>


#### Labeling buttons

The label of a `<button>` element is set inside the element and can include markup. This allows advanced accessibility hints to be included, such as marking up language change. Example: `<button>Mon <span lang="fr">button</span></button>`,for a button with a label in French.

When using the `<input>` element to create buttons, the label is set in the value attribute of the element. Example: `<input type="submit" value="Please submit">`, renders a button.

Source code for the "Submit" and "Cancel" buttons example:

<p class="exampleHTML"><em>Lines 1 and 2</em> render as:<br><button type="submit">Submit</button> <button type="button">Cancel</button><br><br>... while li<em>nes 3 and 4</em> render as:<br> <input value="Submit" type="submit"> <input value="Cancel" type="button"></p>

These give the same results:

<p class="exampleHTML"><em>Lines 1 and 2</em> render as:<br><button type="submit">Submit</button> <button type="button">Cancel</button><br><br>... while li<em>nes 3 and 4</em> render as:<br> <input value="Submit" type="submit"> <input value="Cancel" type="button"></p>
 
Labeling text areas
Enter your address:

Source code:

<label for="address">Enter your address:</label><br> <textarea id="address" name="addresstext"></textarea>




