# Week 5: HTML5 Forms


## 5.2 Elements and attributes


### 5.2.0 Lecture Notes

+ [HTML5 Forms](#521-introduction)
  + a set of input fields including a validation API and visual feedback, contextualized keyboards, etc.
    + 13 HTML5 new `<input type=.../>` fields: email, tel, color, url, date, datetime, datetime-local, month, week, time, range, number and search
  + built-in validation system
    + JavaScript API for custom validation
    + CSS pseudo classes useful for changing an input field style depending on the validity of the input
  + other goodies
    + the option to set an input field out of a `<form>`
    + new elements such as `<datalist>` for autocompletion
    + `<output>` for feedback
    + etc.

+ [Reference of Form elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Forms)<br/><br/>

  <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 55vw;" cellspacing="0" cellpadding="5" border="1">
    <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Forms">Elements of Forms</a></caption>
    <thead>
    <tr style="font-size: 1.2em;">
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Element</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
    </thead>
  <tbody>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button" title="The HTML <button> element represents a clickable button, used to submit forms or anywhere in a document for accessible, standard button functionality."><code>&lt;button&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;button&gt;</code> element</strong> represents a clickable button, used to submit <a href="https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms">forms</a> or anywhere in a document for accessible, standard button functionality.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist" title="The HTML <datalist> element contains a set of <option> elements that represent the permissible or recommended options available to choose from within other controls."><code>&lt;datalist&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;datalist&gt;</code> element</strong> contains a set of <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option" title="The HTML <option> element is used to define an item contained in a <select>, an <optgroup>, or a <datalist>&nbsp;element. As such,&nbsp;<option>&nbsp;can represent menu items in popups and other lists of items in an HTML document."><code>&lt;option&gt;</code></a> elements that represent the permissible or recommended options available to choose from within other controls.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset" title="The HTML <fieldset> element is used to group several controls as well as labels (<label>) within a web form."><code>&lt;fieldset&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;fieldset&gt;</code> element</strong> is used to group several controls as well as labels (<a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label" title="The HTML <label> element represents a caption for an item in a user interface."><code>&lt;label&gt;</code></a>) within a web form.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form" title="The HTML <form> element represents a document section containing interactive controls for submitting information."><code>&lt;form&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;form&gt;</code> element</strong> represents a document section containing interactive controls for submitting information.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input" title="The HTML <input> element is used to create interactive controls for web-based forms in order to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. "><code>&lt;input&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;input&gt;</code> element</strong> is used to create interactive controls for web-based forms in order to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and <a href="https://developer.mozilla.org/en-US/docs/Glossary/user_agent">user agent</a>. </td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label" title="The HTML <label> element represents a caption for an item in a user interface."><code>&lt;label&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;label&gt;</code> element</strong> represents a caption for an item in a user interface.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend" title="The HTML <legend> element represents a caption for the content of its parent <fieldset>."><code>&lt;legend&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;legend&gt;</code> element</strong> represents a caption for the content of its parent <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset" title="The HTML <fieldset> element is used to group several controls as well as labels (<label>) within a web form."><code>&lt;fieldset&gt;</code></a>.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter" title="The HTML <meter> element represents either a scalar value within a known range or a fractional value."><code>&lt;meter&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;meter&gt;</code> element</strong> represents either a scalar value within a known range or a fractional value.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup" title="The HTML <optgroup> element creates a grouping of options within a <select> element."><code>&lt;optgroup&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;optgroup&gt;</code> element</strong> creates a grouping of options within a <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select" title="The HTML <select> element represents a control that provides a menu of options"><code>&lt;select&gt;</code></a> element.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option" title="The HTML <option> element is used to define an item contained in a <select>, an <optgroup>, or a <datalist>&nbsp;element. As such,&nbsp;<option>&nbsp;can represent menu items in popups and other lists of items in an HTML document."><code>&lt;option&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;option&gt;</code> element</strong> is used to define an item contained in a <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select" title="The HTML <select> element represents a control that provides a menu of options"><code>&lt;select&gt;</code></a>, an <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup" title="The HTML <optgroup> element creates a grouping of options within a <select> element."><code>&lt;optgroup&gt;</code></a>, or a <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist" title="The HTML <datalist> element contains a set of <option> elements that represent the permissible or recommended options available to choose from within other controls."><code>&lt;datalist&gt;</code></a>&nbsp;element. As such,&nbsp;<code>&lt;option&gt;</code>&nbsp;can represent menu items in popups and other lists of items in an HTML document.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output" title="The HTML Output element (<output>) is a container element into which a site or app can inject the results of a calculation or the outcome of a user action."><code>&lt;output&gt;</code></a></td>
    <td>The <strong>HTML Output element</strong> (<strong><code>&lt;output&gt;</code></strong>) is a container element into which a site or app can inject the results of a calculation or the outcome of a user action.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress" title="The HTML <progress> element displays an indicator showing the completion progress of a task, typically displayed as a progress bar."><code>&lt;progress&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;progress&gt;</code> element</strong> displays an indicator showing the completion progress of a task, typically displayed as a progress bar.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select" title="The HTML <select> element represents a control that provides a menu of options"><code>&lt;select&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;select&gt;</code> element</strong> represents a control that provides a menu of options</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea" title="The HTML <textarea> element represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example a comment on a review or feedback form."><code>&lt;textarea&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;textarea&gt;</code> element</strong> represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example a comment on a review or feedback form.</td>
    </tr>
  </tbody>
  </table>




### 5.2.1 Introduction

With HTML5, forms, which had shown little improvement since 1997, evolved considerably.  To achieve this, Web developers relied on many popular JavaScript frameworks for validating input formats, providing various input GUIs, such as calendars for dates, sliders, etc. Frameworks such as jQueryUI, Dojo, and Sencha, all provide a widget set for improving forms. Furthermore, it was time to take into account the specifics of mobile web applications, where the GUI of a date chooser cannot be the same as a 400x400 pixel wide calendar on a desktop. Contextual virtual keyboards provided the way forward on smartphones and tablets thanks to Apple, Google and others.

__HTML5 took all this into account and thus provides:__

+ A set of input fields that include a validation API and visual feedback, contextualized keyboards, etc. Of course the look and feel depends on the web browser's implementations, but the HTML5 forms specification introduced 13 new `<input type=.../>` fields:  `email`, `tel`, `color`, `url`, `date`, `datetime`, `datetime-local`, `month`, `week`, `time`, `range`, `number` and `search`.
+ Built-in validation system: JavaScript API for custom validation, CSS pseudo classes that are useful for changing an input field style depending on the validity of the input.
+ Other goodies, such as the option to set an input field out of a `<form>`, new elements such as `<datalist>` for autocompletion, `<output>` for feedback, etc.

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://developer.mozilla.org/https://tinyurl.com/y4u8ud5e" ismap target="_blank">
    <img style="margin: 0.1em;" height=200 
      src  ="https://tinyurl.com/y5a9kwn5" 
      alt  ="contextual keyboards" 
      title="contextual keyboards"
    >
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/yypemwax" 
    alt    ="date picker on a smartphone"
    title  ="date picker on a smartphone"
    >
  </a>
</div>


Examples of contextual keyboards are shown above; they differ depending on the type of  `<input>` fields in the `<form>`.

In the examples, we can see: email, URL, and phone number. Look at the different keyboard layouts. The last picture is a date picker from an IOS phone.


#### External resources:

+ From the specification: [Forms](https://html.spec.whatwg.org/multipage/forms.html)
+ From MDN's Web Docs: [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)


#### Knowledge check 5.2.1

1. Which of the following statements is true about HTML5 forms? (2 correct answers)

  a. On mobile devices, contextual keyboard will appear when a user interacts with the new input types<br/>
  b. HTML5 introduced 25 new input types which replace all the old ones from HTML4<br/>
  c. There is a built-in validation system for input elements<br/>
  d. Some HTML5 input types work only on mobile devices<br/>

  Ans: ac<br/>
  Explanantion: The new input types (email, url, tel etc.) will indeed pop up a contextual keyboard on mobile devices. HTML5 introduced new input types but they do not replace the old ones, they complete them. There is a built-in validation system. And no, no specific input types work only on mobile devices. Correct answers are 1 and 3.






