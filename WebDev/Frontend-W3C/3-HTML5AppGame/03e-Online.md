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
    + empty fields w/ `required` attribute &#36;\to&#36; error message &#36;\to&#36; not submitted
    + server-side: join the files asynchronously uploaded w/ the rest of the form's value &#36;\gets&#36; PHP code

+ Packaged approach
  + send all form content, including files, only when the form is submitted
  + design
    + send all of the form's content at once w/ a single Ajax request &#36;\to&#36; only one progress bar
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


#### File selector for uploading files

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

[Local Demo](src/03e-example01.html)

In this example, the "send" button is disabled and becomes enabled as soon as all the files are completely uploaded. Also, note that the form is saved as the user types, by using localStorage. Accordingly, it can be restored on page reload, as in the example from the localStorage topic of the HTML5 Part 1 course.

Note that the full working source code of this example corresponds to "example 1" in [the zip archive that contains all examples](https://bit.ly/3r0lP4O).


#### Drag and drop for uploading files

__Example #2: similar example but using drag and drop instead of a file selector__

Here is much the same code, but this time it uses drag and drop to collect the filenames, not an input field. [Try it at JSBin](https://jsbin.com/qijoza/edit?html,css,js,output) and look at the source code - there are plenty of comments.

[Local Demo](src/03e-example02.html)

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

<div><ol>
<li value="1">&lt;?php</li>
<li> </li>
<li>if (isset(&#36;_POST['givenname']) &amp;&amp; isset(&#36;_POST['familyname'])) {</li>
<li>&nbsp; &nbsp;echo &#36;_POST['givenname'].' '.&#36;_POST['familyname'].' uploaded file(s).&lt;br /&gt;';</li>
<li>}</li>
<li> </li>
<li>if (isset(&#36;_POST['namesAllFiles']) &amp;&amp; &#36;_POST['namesAllFiles'] != "") {</li>
<li>&nbsp; &#36;folderName = date("m.d.Y");</li>
<li>&nbsp;&nbsp;if (!is_dir('upload/'.&#36;folderName)) {</li>
<li>&nbsp; &nbsp; &nbsp;mkdir('upload/'.&#36;folderName);</li>
<li> }</li>
<li> </li>
<li> &#36;filesName = explode("::", &#36;_POST['namesAllFiles']);</li>
<li>&nbsp; for (&#36;i=0; &#36;i &lt; count(&#36;filesName); &#36;i++) {</li>
<li>&nbsp; &nbsp; copy('upload/RecycleBin/'.&#36;filesName[&#36;i], </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;'upload/'.&#36;folderName.'/'.&#36;filesName[&#36;i]);</li>
<li>&nbsp; &nbsp; unlink('upload/RecycleBin/'.&#36;filesName[&#36;i]);</li>
<li>&nbsp; &nbsp; echo "&#36;filesName[&#36;i] uploaded&lt;br /&gt;";</li>
<li>&nbsp;&nbsp;}</li>
<li>}</li>
<li> </li>
<li>&#36;fn = (isset(&#36;_SERVER['HTTP_X_FILENAME']) ? </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&#36;_SERVER['HTTP_X_FILENAME'] : false);</li>
<li> </li>
<li>if (&#36;fn) {</li>
<li>&nbsp;&nbsp;if (!is_dir('upload/RecycleBin')) {</li>
<li>&nbsp; &nbsp; mkdir('upload/RecycleBin');</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp; file_put_contents('upload/RecycleBin/'.&#36;fn,&nbsp; &nbsp; &nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; file_get_contents('php://input'));</li>
<li>&nbsp;&nbsp;exit();</li>
<li>}</li>
<li> </li>
<li>?&gt;</li>
</ol></div>



__Explanations:__

+ When files are first uploaded, they are stored in a directory called `upload/RecycleBin`. If it does not exist, this directory is created (_lines 22-32_).
+ When the form is submitted, a directory whose name is today's date is created, and the files located in the RecycleBin directory are moved to that directory. If it does not already exist, the directory will be created  (_lines 7-20_).


#### Notes for 3.5.3 Serial approach

+ Example: server-side PHP code w/ serial approach

  ```php
  <?php
  
  if (isset($_POST['firstname']) && isset($_POST['lastname'])) {
      echo $_POST['firstname'].' '.$_POST['lastname'].' uploaded file(s).<br />';
  }
  
  if (isset($_POST['namesAllFiles']) && $_POST['namesAllFiles'] != "") {
      $folderName = date("m.d.Y");
      if (!is_dir('upload/'.$folderName)) {
          mkdir('upload/'.$folderName);
      }
  
      $filesName = explode("::", $_POST['namesAllFiles']);
      for ($i=0; $i < count($filesName); $i++) {
          copy('upload/RecycleBin/'.$filesName[$i], 'upload/'.$folderName.'/'.$filesName[$i]);
          unlink('upload/RecycleBin/'.$filesName[$i]);
          echo "$filesName[$i] uploaded<br />";
      }
  }
  
  $fn = (isset($_SERVER['HTTP_X_FILENAME']) ? $_SERVER['HTTP_X_FILENAME'] : false);
  
  if ($fn) {
      if (!is_dir('upload/RecycleBin')) {
          mkdir('upload/RecycleBin');
      }
      file_put_contents('upload/RecycleBin/'.$fn, file_get_contents('php://input'));
      exit();
  }
  
  ?>
  ```

### 3.5.4 Package approach

Let's use the previous two examples as a basis for two further examples:

1. one that uses only a file selector,
2. one that uses drag and drop.


#### File selector for uploading files at once

__Example #3: uploading everything at once using a file selector__

A file selector (`<input type="file">`).

This time, we add the files to an HTML5 FormData object before sending XHR2 Ajax requests to the server (one for each file + one for the rest of the form).  The uploads only start once the form is submitted.

You can [try this example at JSBin](https://jsbin.com/quzohi/edit?html,css,js,output), and look at the source code and comments for details.

[Local Demo](src/03e-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3xt7jou')"
    src    = "https://bit.ly/3dUP57p"
    alt    = "Example 3 of file uploads"
    title  = "Example 3 of file uploads"
  />
</figure>


#### Drag and Drop for uploading files at once

__Example #4: uploading using drag and drop__

[Try the example at JSBin](https://jsbin.com/xonemow/edit?html,css,output) and look at source code and comments.

[Local Demo](src/03e-example04.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3xt7jou')"
    src    = "https://bit.ly/3r18nxl"
    alt    = "Example 4: uses drag'n'drop of files"
    title  = "Example 4: uses drag'n'drop of files"
  />
</figure>



#### PHP code for uploading files at once

__PHP code for the single-packaged examples (with and without drag and drop, the PHP is the same)__

This code is given "as is". The principle is the same as with the examples given in the previous section, except that this time we do not have to deal with a temporary "RecycleBin" directory.

<div><ol>
<li value="1">&lt;?php</li>
<li> </li>
<li>if (isset(&#36;_POST['givenname']) &amp;&amp; isset(&#36;_POST['familyname'])) {</li>
<li>&nbsp; &nbsp; echo &#36;_POST['givenname'] . ' ' . &#36;_POST['familyname'] . ' try to upload </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;file(s).';</li>
<li>}</li>
<li> </li>
<li>&#36;folderName = date("m.d.Y");</li>
<li>if (!is_dir('upload/'.&#36;folderName)) {</li>
<li>&nbsp; &nbsp; mkdir('upload/'.&#36;folderName);</li>
<li>}</li>
<li> </li>
<li>&#36;fn = (isset(&#36;_SERVER['HTTP_X_FILENAME']) ? &#36;_SERVER['HTTP_X_FILENAME'] : </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; false);</li>
<li>if (&#36;fn)</li>
<li>{</li>
<li>&nbsp; &nbsp; file_put_contents('upload/' . &#36;folderName . '/' . &#36;fn,&nbsp; &nbsp; &nbsp; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; file_get_contents('php://input'));</li>
<li>&nbsp; &nbsp; echo "&#36;fn uploaded";</li>
<li>&nbsp; &nbsp;&nbsp;exit();</li>
<li>}</li>
<li>else {</li>
<li>&nbsp; &nbsp;if (isset(&#36;_FILES) &amp;&amp; is_array(&#36;_FILES) &amp;&amp; array_key_exists('formFiles', </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#36;_FILES)) {</li>
<li>&nbsp; &nbsp; &nbsp; &#36;number_files_send = count(&#36;_FILES['formFiles']['name']);</li>
<li>&nbsp; &nbsp; &nbsp; &#36;dir = realpath('.') . '/upload/' . &#36;folderName . '/';</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;if (&#36;number_files_send &gt; 0) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;for (&#36;i = 0; &#36;i &lt; &#36;number_files_send; &#36;i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; echo '&lt;br/&gt;Reception of : ' . &#36;_FILES['formFiles']['name'][&#36;i];</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#36;copy = move_uploaded_file(&#36;_FILES['formFiles']['tmp_name']</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [&#36;i], &#36;dir . &#36;_FILES['formFiles']['name'][&#36;i]);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;if (&#36;copy) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; echo '&lt;br /&gt;File ' . &#36;_FILES['formFiles']['name'][&#36;i] . </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;' copy';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; echo '&lt;br /&gt;No file to upload';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;} </li>
<li>}</li>
<li> </li>
<li>?&gt;</li>
</ol></div>


#### Notes for 3.5.4 Package approach

+ Example: server-side PHP code for packaged approach

  ```php
  <?php

  if (isset($_POST['firstname']) && isset($_POST['lastname'])) {
    echo $_POST['firstname'] . ' ' . $_POST['lastname'] . ' try to upload file(s).';
  }

  $folderName = date("m.d.Y");
  if (!is_dir('upload/'.$folderName)) {
    mkdir('upload/'.$folderName);
  }

  $fn = (isset($_SERVER['HTTP_X_FILENAME']) ? $_SERVER['HTTP_X_FILENAME'] : false);
  if ($fn)
  {
    file_put_contents('upload/' . $folderName . '/' . $fn, file_get_contents('php://input'));
    echo "$fn uploaded";
    exit();
  }
  else {
    if (isset($_FILES) && is_array($_FILES) && array_key_exists('formFiles', $_FILES)) {
      $number_files_send = count($_FILES['formFiles']['name']);
      $dir = realpath('.') . '/upload/' . $folderName . '/';
      
      if ($number_files_send > 0) {
        for ($i = 0; $i < $number_files_send; $i++) {
          echo '<br/>Reception of : ' . $_FILES['formFiles']['name'][$i];
          $copy = move_uploaded_file($_FILES['formFiles']['tmp_name'][$i], 
            $dir . $_FILES['formFiles']['name'][$i]);
          if ($copy) {
            echo '<br />File ' . $_FILES['formFiles']['name'][$i] . ' copy';
          }
          else {
            echo '<br />No file to upload';
          }
        }
      }
    }   
  }

  ?>
  ```


### 3.5.5 Discussion

Here is the discussion forum for this part of the course.

#### Suggested topics of discussion:

+ The given examples come with PHP code. If you adapt them to work with another server side languages, please share!
+ There are many possible improvements to the provided examples in the client code: monitoring the speed of upload/downloads, canceling an upload, etc. The examples are given "as is"... if you improve them, as usual, share them in the forum!



