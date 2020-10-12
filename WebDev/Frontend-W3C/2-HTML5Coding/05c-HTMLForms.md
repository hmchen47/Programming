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






