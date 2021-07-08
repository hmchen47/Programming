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


#### Notes for 3.5.1 Introduction

+ Uploading forms and files
  + typical tasks
    + submit a form w/ regular input fields
    + benefit from the HTML5 built-in validation
    + upload files
    + monitor the file upload progress w/ a progress bar
  + solutions
    + typical: jQuery plugins
    + alternative: only HTML5 APIs, easy, faster, and lower page weight
  + typical design
    + a regular HTML5 form
    + the input fields for entering a name, address, age, etc.
    + selecting and uploading multiple files
  + approaches
    + serial approach
    + packaged approach

+ Serial approach
  + uploading the files as soon as selected or dragged and dropped
  + design
    + an Ajax/XHR2
    + a form w/ an `<input type=file multiple>` input field
    + one or more `<progress>` elements for monitoring file uploads
    + form w/ input fields of different types
  + interactions
    + user drag and drop files
    + start being uploaded immediately
    + form only sent all the fields valid
  + example: Gmail's behavior
    + commposing a message and adding an attachment
    + attachments uploaded as soon as selected or dropped into the message window
    + message only sent when the "send" button pressed
    + empty fields w/ `required` attribute $\to$ error message $\to$ noy submitted
    + server-side: join the files asynchronously uploaded w/ the resest of the form's value $\gets$ PHP code

+ Packaged approach
  + send all form content, including files, only when the form is submitted
  + design
    + send all of the form's content at once w/ a single Ajax request $\to$ only one progress bar
    + probably using multiple Ajax requests, not starting until the submit button clicked
  + sending everything at the same time using Ajax/JavaScript, including the regular input field conetnt and the selected fields


### 3.5.2 Installation guide

Please download all examples (authors: Michel Buffa, improvements and fixes by Vincent Mazenod): [Zip file containing all examples](https://bit.ly/3xw0Clq) (html + css + js + php + readmes)

[Local Demo 1](src/03e-forms_php_upload/upload1/upload.html)<br>
[Local Demo 2](src/03e-forms_php_upload/upload2/upload.html)<br>
[Local Demo 3](src/03e-forms_php_upload/upload3/upload.html)<br>
[Local Demo 4](src/03e-forms_php_upload/upload4/upload.html)<br>
[Local Demo 5](src/03e-forms_php_upload/upload5/upload.html)<br>

The examples can be tried online at JSBin (see in the following pages, but the upload is "faked". These online examples do not use a real server, but are useful for playing with the code and understanding how it works. You can try them and see uploads' progress, etc.

However, we also provide complete source code for these examples, including the server-side PHP code. The course is about HTML5, not PHP, so we provide this code "as is": it is only a few lines long per example, and has been tested with the latest version of PHP.  It should run out of the box with most WAMP, LAMP, and MAMP distributions (Apache / PHP).

Unzip the archive and follow the included READMEs. These examples propose __different implementations of the two approaches__ presented in the previous lecture, and both with an `<input type=file>` and drag and drop.

The HTML part of the examples is also using a technique, seen during the W3Cx HTML5 Coding Essentials course, that saves the input fields' content as you type, using `LocalStorage`. You can reload the page any time without losing what you typed. Initially, the examples all used a FormData object but at the time we encountered some incompatibilities with older versions of PHP, so we had to manually set a component of the HTTP header.

This part of the lesson is optional and is mainly useful for students who are also involved in the server side of the Web development.









