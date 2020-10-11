# Week 5: HTML5 Forms


## 5.2 Elements and attributes


### 5.2.0 Lecture Notes




### 5.2.1 Introduction

With HTML5, forms, which had shown little improvement since 1997, evolved considerably.  To achieve this, Web developers relied on many popular JavaScript frameworks for validating input formats, providing various input GUIs, such as calendars for dates, sliders, etc. Frameworks such as jQueryUI, Dojo, and Sencha, all provide a widget set for improving forms. Furthermore, it was time to take into account the specifics of mobile web applications, where the GUI of a date chooser cannot be the same as a 400x400 pixel wide calendar on a desktop. Contextual virtual keyboards provided the way forward on smartphones and tablets thanks to Apple, Google and others.

__HTML5 took all this into account and thus provides:__

+ A set of input fields that include a validation API and visual feedback, contextualized keyboards, etc. Of course the look and feel depends on the web browser's implementations, but the HTML5 forms specification introduced 13 new `<input type=.../>` fields:  `email`, `tel`, `color`, `url`, `date`, `datetime`, `datetime-local`, `month`, `week`, `time`, `range`, `number` and `search`.
+ Built-in validation system: JavaScript API for custom validation, CSS pseudo classes that are useful for changing an input field style depending on the validity of the input.
+ Other goodies, such as the option to set an input field out of a `<form>`, new elements such as `<datalist>` for autocompletion, `<output>` for feedback, etc.

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y4u8ud5e" ismap target="_blank">
    <img style="margin: 0.1em;" width=350
      src  ="https://tinyurl.com/y5a9kwn5" 
      alt  ="contextual keyboards" 
      title="contextual keyboards"
    >
    <img style="margin: 0.1em;" width=350
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

  Ans: 