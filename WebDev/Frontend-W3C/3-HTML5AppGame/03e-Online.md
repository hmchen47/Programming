# Module 3: HTML5 file upload and download section


## 3.5 Forms and files


### 3.5.1 Introduction

We had many questions about how to submit a form with regular input fields AND benefit from the HTML5 built-in validation AND upload files AND monitor the file upload progress with a progress bar.

Many solutions proposed on the Web rely on jQuery plugins. However, coding such a behavior using only HTML5 APIs is easy AND faster AND has a lower page weight, as we will see.

This part of the course will describe different approaches for implementing file uploads associated with a form.

We have included PHP server-side code: this course focuses on HTML5 and front-end development - so, the PHP code is given "as is".


#### The problem

Imagine that we have a regular HTML5 form, but as well as the input fields for entering a name, address, age, etc., we also want to select and upload multiple files (which might include images). 


#### Serial approach

__Serial approach: upload the files as soon as they are selected or dragged and dropped__

Let's design an XHR2/Ajax, a form with an `<input type=file multiple>` input field, and one or more `<progress>` elements for monitoring file uploads. The form will also have input fields of different types.

An example of this kind of form is shown below: when the user drags and drops files, they will start being uploaded immediately. However,  the form will only be sent when all the fields are valid.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3hMSTZz')"
    src    = "https://bit.ly/3k1qf9M"
    alt    = "uploading files using Xhr2, drag'n'drop and progress bar"
    title  = "uploading files using Xhr2, drag'n'drop and progress bar"
  />
</figure>


This approach is similar to Gmail's behavior when you compose a message and add an attachment. The attachments are uploaded as soon as they are selected or dropped into the message window, but the message will only be sent when you press the "send" button. An empty field with a `required` attribute, if left empty, will cause an error message pop up in a bubble, and the form will not be submitted. Nice!

However, on the server side, we need a way to "join" the files that have been asynchronously uploaded with the rest of the form's values. This is easier to do than it sounds. Look at the provided PHP code provided with each of the examples.


#### Packaged approach

__Packaged approach: send all form content, including files, only when the form is submitted__

+ This method enables us to send all of the form's content (regular input field values + files selected) at once, _using a single Ajax request_ (we will need only one progress bar),
+ or we may _use multiple Ajax requests_, which we don't start until the submit button has been clicked.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3hMSTZz')"
    src    = "https://bit.ly/2TCV8XD"
    alt    = "Second approach, send files only when the sublit button has been clicked"
    title  = "Second approach, send files only when the sublit button has been clicked"
  />
</figure>


The difference between this and the first approach is that we are sending everything _at the same time_ using Ajax/JavaScript: the regular input field content and the selected files.

The next page provides the source code of several examples, as well as the server-side PHP code.








