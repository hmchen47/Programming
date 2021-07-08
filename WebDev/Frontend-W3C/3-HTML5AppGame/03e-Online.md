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


### 3.5.3 Serial approach

We made two examples that rely on the serial approach:

1. one that uses only a file selector,
2. one that uses drag and drop.

We could have merged file selector + drag and drop, as we did in examples earlier in the course, but the code would have been longer and more difficult to follow.


#### Uploading files w/ file selector

__Example #1: auto-loading of the files, regular form submission, benefits of the HTML5 form validation system__

Example using a file selector (`<input type="file">`):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3hrB2sd')"
    src    = "https://bit.ly/3yxP5lG"
    alt    = "example 1 of file upload"
    title  = "example 1 of file upload"
  />
</figure>


Try the [online example at JSBin](https://jsbin.com/rozanow/edit?html,css,js,output) (this one does not have the PHP code running, but works anyway, even if the files are not uploaded - it "fakes the upload"). Look at the online example for the code and the following explanations.

In this example, the "send" button is disabled and becomes enabled as soon as all the files are completely uploaded. Also, note that the form is saved as the user types, by using localStorage. Accordingly, it can be restored on page reload, as in the example from the localStorage topic of the HTML5 Part 1 course.

Note that the full working source code of this example corresponds to "example 1" in [the zip archive that contains all examples](https://bit.ly/3r0lP4O).


#### Uploading files with drag and drop

__Example #2: similar example but using drag and drop instead of a file selector__

Here is much the same code, but this time it uses drag and drop to collect the filenames, not an input field. [Try it at JSBin](https://jsbin.com/qijoza/edit?html,css,js,output) and look at the source code - there are plenty of comments.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3hrB2sd')"
    src    = "https://bit.ly/36pNX7Y"
    alt    = "example 2 of file uploads, uses drag'n'drop"
    title  = "example 2 of file uploads, uses drag'n'drop"
  />
</figure>


#### PHP code for uploading files

__And here is the PHP code for the server-side part of examples #1 and #2__

This code is given "as is":

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&lt;?</span><span class="pln">php</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">isset</span><span class="pun">(</span><span class="pln">$_POST</span><span class="pun">[</span><span class="str">'givenname'</span><span class="pun">])</span><span class="pln"> </span><span class="pun">&amp;&amp;</span><span class="pln"> isset</span><span class="pun">(</span><span class="pln">$_POST</span><span class="pun">[</span><span class="str">'familyname'</span><span class="pun">]))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;echo $_POST</span><span class="pun">[</span><span class="str">'givenname'</span><span class="pun">].</span><span class="str">' '</span><span class="pun">.</span><span class="pln">$_POST</span><span class="pun">[</span><span class="str">'familyname'</span><span class="pun">].</span><span class="str">' uploaded file(s).&lt;br /&gt;'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">isset</span><span class="pun">(</span><span class="pln">$_POST</span><span class="pun">[</span><span class="str">'namesAllFiles'</span><span class="pun">])</span><span class="pln"> </span><span class="pun">&amp;&amp;</span><span class="pln"> $_POST</span><span class="pun">[</span><span class="str">'namesAllFiles'</span><span class="pun">]</span><span class="pln"> </span><span class="pun">!=</span><span class="pln"> </span><span class="str">""</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; $folderName </span><span class="pun">=</span><span class="pln"> date</span><span class="pun">(</span><span class="str">"m.d.Y"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(!</span><span class="pln">is_dir</span><span class="pun">(</span><span class="str">'upload/'</span><span class="pun">.</span><span class="pln">$folderName</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;mkdir</span><span class="pun">(</span><span class="str">'upload/'</span><span class="pun">.</span><span class="pln">$folderName</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> $filesName </span><span class="pun">=</span><span class="pln"> explode</span><span class="pun">(</span><span class="str">"::"</span><span class="pun">,</span><span class="pln"> $_POST</span><span class="pun">[</span><span class="str">'namesAllFiles'</span><span class="pun">]);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="pln">$i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> $i </span><span class="pun">&lt;</span><span class="pln"> count</span><span class="pun">(</span><span class="pln">$filesName</span><span class="pun">);</span><span class="pln"> $i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; copy</span><span class="pun">(</span><span class="str">'upload/RecycleBin/'</span><span class="pun">.</span><span class="pln">$filesName</span><span class="pun">[</span><span class="pln">$i</span><span class="pun">],</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;'upload/'</span><span class="pun">.</span><span class="pln">$folderName</span><span class="pun">.</span><span class="str">'/'</span><span class="pun">.</span><span class="pln">$filesName</span><span class="pun">[</span><span class="pln">$i</span><span class="pun">]);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; unlink</span><span class="pun">(</span><span class="str">'upload/RecycleBin/'</span><span class="pun">.</span><span class="pln">$filesName</span><span class="pun">[</span><span class="pln">$i</span><span class="pun">]);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; echo </span><span class="str">"$filesName[$i] uploaded&lt;br /&gt;"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">$fn </span><span class="pun">=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">isset</span><span class="pun">(</span><span class="pln">$_SERVER</span><span class="pun">[</span><span class="str">'HTTP_X_FILENAME'</span><span class="pun">])</span><span class="pln"> </span><span class="pun">?</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;$_SERVER</span><span class="pun">[</span><span class="str">'HTTP_X_FILENAME'</span><span class="pun">]</span><span class="pln"> </span><span class="pun">:</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">$fn</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(!</span><span class="pln">is_dir</span><span class="pun">(</span><span class="str">'upload/RecycleBin'</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; mkdir</span><span class="pun">(</span><span class="str">'upload/RecycleBin'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; file_put_contents</span><span class="pun">(</span><span class="str">'upload/RecycleBin/'</span><span class="pun">.</span><span class="pln">$fn</span><span class="pun">,</span><span class="pln">&nbsp; &nbsp; &nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; file_get_contents</span><span class="pun">(</span><span class="str">'php://input'</span><span class="pun">));</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">exit</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">?&gt;</span></li>
</ol></div>

__Explanations:__

+ When files are first uploaded, they are stored in a directory called `upload/RecycleBin`. If it does not exist, this directory is created (_lines 22-32_).
+ When the form is submitted, a directory whose name is today's date is created, and the files located in the RecycleBin directory are moved to that directory. If it does not already exist, the directory will be created  (_lines 7-20_).








