# Module 3: HTML5 file upload and download section


## 3.2 File API and Ajax / XHR2 requests


### 3.2.1 Ajax and XHR2

We present below a short history of Ajax: an introduction to XMLHttpRequest level 2 (XHR2).

> __Wikipedia definition:__ "Ajax, short for Asynchronous JavaScript and XML), is a group of interrelated Web development techniques used on the client-side to create asynchronous Web applications. With Ajax, Web applications can send data to and retrieve from a server asynchronously (in the background) without interfering with the display and behavior of the existing page. Data can be retrieved using the XMLHttpRequest object. Despite the name, the use of XML is not required (JSON is often used), and the requests do not need to be asynchronous."

Ajax appeared around 2005 with Google Maps, and is now widely used. We are not going to teach you Ajax programming, but instead focus on the relationships between "the new version of Ajax", known as XHR2 (for XmlHttpRequest level 2) and the [File API](https://www.w3.org/TR/FileAPI/) (seen in the W3Cx [HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) MOOC). Also, you will discover that the HTML5 `<progress>` element is of great use for monitoring the progress of file uploads (or downloads).

We recommend reading [this article from HTML5Rocks.com](https://www.html5rocks.com/en/tutorials/file/xhr2/) that presents the main features of XHR2.

Briefly, these improvements include:

+ New, easier to use syntax,
+ In-browser encoding/decoding of binary files,
+ Progress monitoring of uploads and downloads.

The following sections of this course present a few examples of file downloads/uploads together with the file API and show how to monitor progress.

The current support of XHR2 is excellent: see related [CanIUse's browser compatibility table](https://caniuse.com/#feat=xhr2).


#### Notes for 3.2.1 Ajax and XHR2

+ Asynchronous JavaScript and XML (Ajax)
  + a group of interrelated Web development techniques
  + used on the client-side to create asynchronous Web application
  + Web applications able to send data to and retrieve from a server asynchronously w/o interfering w/ the display and behavior of the existing page
  + data retrieved via the `XMLHttpRequest` object, usually JSON format used than XML
  + the new version of Ajax
    + XmlHttpRequest level 2 (XHR2)
    + improvement
      + easier to use syntax
      + in-browser encoding/decoding of binary files
      + progress monitoring of uploads and downloads







