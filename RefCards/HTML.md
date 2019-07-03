# Reference Cards for Web Development - HTML5

## Best Practices

+ Template

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="utf-8">
    <title> My Web Page Title </title>

    <!-- CSS Usage: link preferred ~ comment for HTML-->
    <link rel="stylesheet" href="css/my_styles.css">
    <style>
      /* CSS will go in this area ~ comment for CSS */
    </style>
  </head>
  <body>
    <!-- Contents within this area -->
  </body>
  </html>
  ```

+ Useful Reference& Tool Links
  + [W3C HTML5 specification](https://www.w3.org/TR/html5/)
  + [W3C cheatsheet](https://www.w3.org/2009/cheatsheet/)
  + [MDN attribute reference list](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)
  + [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
  + [CSS validator](https://jigsaw.w3.org/css-validator/)
  + [Unicorn](http://validator.w3.org/unicorn/)  
  + [W3C Internationalization Checker](https://validator.w3.org/i18n-checker/)
  + [W3C Link Checker](http://validator.w3.org/checklink)
  + [CodePen](http://codepen.io/)


+ HTML Layout Elements

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://www.w3schools.com/html/html_layout.asp">
      <img src="https://www.w3schools.com/html/img_sem_elements.gif" style="margin: 0.1em;" alt="HTML5 offers new semantic elements that define the different parts of a web page" title="HTML Layout" width="200">
    </a></div>
  </div>

  + `<header>` - Defines a header for a document or a section
  + `<nav>` - Defines a container for navigation links
  + `<section>` - Defines a section in a document
  + `<article>` - Defines an independent self-contained article
  + `<aside>` - Defines content aside from the content (like a sidebar)
  + `<footer>` - Defines a footer for a document or a section
  + `<details>` - Defines additional details
  + `<summary>` - Defines a heading for the `<details>` element



+ Comments:
  + Inline: `<!-- This is a comment -->`
  + Multiple lines:

    ```html
    <!--
    Beginning of comment
    ... 
    End of comment
    -->
    ```

+ UTF-8: `<meta charset="utf-8">` in `head` section
  + Always use the Unicode character encoding UTF-8 for your Web pages
  + Ensure that your editor saves the file in UTF-8

+ Named Characters

  + [WC3 Named character references](https://www.w3.org/TR/2011/WD-html5-20110113/named-character-references.html)

  + [HTML character codes](https://www.rapidtables.com/web/html/html-codes.html)

  + Frequent used codes

    <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 60vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
      <thead><tr>
        <th style="background-color: #3d64ff; color: #ffffff; width: 10vw">Symbol</th>
        <th style="background-color: #3d64ff; color: #ffffff; width: 5vw">Entity Name</th>
        <th style="background-color: #3d64ff; color: #ffffff; width: 5vw">Entity Number</th>
        <th style="background-color: #3d64ff; color: #ffffff; width: 20vw">Usage</th>
      </tr></thead>
      <tbody>
      <tr>
        <td style="text-align:left;">Less than '&lt;'</td>
        <td style="text-align:center;"> &#38;lt; </td>
        <td style="text-align:center;"> &#38;&#35;60; </td>
        <td>Div tag: &#38;lt; </td>
      </tr>
      <tr>
        <td style="text-align:left;">Greater than '&gt;'</td>
        <td style="text-align:center;"> &#38;gt; </td>
        <td style="text-align:center;"> &#38;&#35;62; </td>
        <td>Div tag: &#38;gt; </td>
      </tr>
      <tr>
        <td style="text-align:left;">Ampersand '&' </td>
        <td style="text-align:center;"> &#38;amp; </td>
        <td style="text-align:center;"> &#38;&#35;38; </td>
        <td>Tome &#38;amp; Jerry </td>
      </tr>
      <tr>
        <td style="text-align:left;">Non-breaking space - space that will not create a new line </td>
        <td style="text-align:center;"> &#38;nbsp; </td>
        <td style="text-align:center;"> &#38;&#35;160; </td>
        <td>If you add multiple spaces, the browser will remove all but one. So you have to use this entity to add multiple spaces in your HTML page. </td>
      </tr>
      <tr>
        <td style="text-align:left;">Quotes " </td>
        <td style="text-align:center;"> &#38;quot; </td>
        <td style="text-align:center;"> &#38;&#35;34; </td>
        <td>Link to a another section on the same page using the id of the element: '&lt;a href="#timetable"&gt;' <br/> Displayed as: '<a href="#timetable"> timetable </a>' <br/><br/> &quot; is generally encouraged for code. For an actual quotation, '&lt;q&gt;' or '&lt;blockquote&gt;' is preferred. </td>
      </tr>
      </tbody>
    </table>


+ Case Sensitive
  + Tags: case insensitive
  + Attributes: case sensitive

+ Single and double quotes are interchangeable, but not mixing

+ Headings are really useful for some assistive technology users and missing levels can be confusing.

+ Always declare the language of your page in the `<html>` tag

## Element, Tag & Attribute Syntax

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.w3.org/community/webed/wiki/HTML/Training/Tag_syntax">
    <img src="https://www.w3.org/community/webed/wiki/images/3/39/Elements.png" style="margin: 0.1em;" alt="HTML elements usually come in tag pairs" title="HTML elements" width="350">
    <img src="https://www.w3.org/community/webed/wiki/images/b/bc/Option.png" style="margin: 0.1em;" alt="An element can have attributes to refine its meaning" title="HTML elements" width="350">
  </a></div>
</div>


## Tags

| Tag | Description | Link |
|-----|-------------|------|
| `<!DOCTYPE html>` | declaration "This is an HTML5 file, in case you were wondering" | [I-1.3 Elements, tags and attributes][000]; [I-1.6 More on tags][004] |
| `<html>` | where the actual HTML code begins and end | | [I-1.3 Elements, tags and attributes][001]; [I-1.6 More on tags][004] |
| `<head>` | where the browser can find style tips, and what the title of the page is | [I-1.3 Elements, tags and attributes][001]; [I-1.6 More on tags][004] |
| `<body>` | contains all of the content of your page, essentially what the user sees |[I-1.5 Best practices][003]; [I-1.6 More on tags][004] |
| `<h1> ~ <h6>` | a whole collection of heading tags | [I-1.6 More on tags][004] |
| `<p>` | paragraph; text wrapped in may be indented or have extra vertical white space before starting; typically be a new line | [I-1.6 More on tags][004] |
| `<q>` | quotes; used when you want to quote a person or written work in your Web page; customarily displayed using quotation marks, again unrelated to strings | [I-1.6 More on tags][005] |
| `<blockquote>` | quote a larger passage; typically set the quoted text apart from the surrounding text and indent it, to make clear that it is quoted text | [I-1.6 More on tags][005] |
| `<ul>`, `<ol>` | indicate a list of things; `<ol>`: "ordered" list; `<ul>`: "unordered" list | [I-1.6 More on tags][005] |
| `<li>` | List Item; nested inside a list (`<ul>` or `<ol>`) | [I-1.6 More on tags][005] |
| `<hr>` | Horizontal Rule; a horizontal line across the width of the text | [I-1.6 More on tags][005] |
| `<br>` | line break; break the "white space" rule: where spaces and carriage returns are generally treated the same; treated as a _required carriage return_ | [I-1.6 More on tags][005] |
| `<pre>` | "PREformatted text", meaning "I've set this up just the way I want it, don't mess with it."; monospace font, and none of the spaces, tabs or carriage-returns are ignored | [I-1.6 More on tags][005] |
| `<i>` | italic text; used for text in a different mood or voice, such as foreign words, a thought or technical terms | [I-2.3 Semantic Meaning][015] |
| `<b>` | bolded text; used as a stylistic offset such as keywords in a document, product names or action words without making them as important; can also be used as headings in list items | [I-2.3 Semantic Meaning][015] |
| `<em>` | Emphasizes text; semantic tag; stress emphasis of its contents | [I-2.3 Semantic Meaning][016] |
| `<strong>` | Important text; semantic tag; indication of how something should be | [I-2.3 Semantic Meaning][016] |
| `<a>` | create a hyperlink to other web pages, files, locations within the same page, email addresses, or any other URL | [I-2.5 Hyperlinks][031] |
| `<style>` | place CSS directly into an HTML document; anywhere in an HTML document;most common place: `<head>` section | [I-3.2 CSS Basic][066] |
| `<link>` | bin `.css` file within `<head>` section | [I-3.2 CSS Basic][066] |



## Semantic Elements

| Semantic Element | Description | Link |
|------------------|-------------|---------|
| `<header>` | Introduction for the whole page or individual sections, article, nav, aside elements. Typically contains site name, logo, navigation. Does not have to be at the beginning of page. | [I-2.3 Semantic Meaning][023] |
| `<footer>` | Includes typical footer information like authoring, copyrights, contact information and a footer menu. | [I-2.3 Semantic Meaning][021] | 
| `<nav>` | Navigation links for the document. A page can have more than one `<nav>` element like table of contents, horizontal navigation in header and footer navigation. | [I-2.3 Semantic Meaning][021] |
| `<section>` | Defines sections in the document such as chapters, headers, etc. Typically used on content that cannot make sense on its own.  | [I-2.3 Semantic Meaning][024] |
| `<article>` | Defines independent content that should make sense on its own outside of the document such as newspaper articles, blog posts, etc. | [I-2.3 Semantic Meaning][024] |
| `<aside>` | Side content other than main content, like a sidebar. These are not considered as part of the main page outline. | [I-2.3 Semantic Meaning][020] |
| `<details>` *see example below | A way to provide additional information that the user can show or hide. Content that is shown to user by default. Other content is hidden and can be expanded to view. | [I-2.3 Semantic Meaning][017] |
| `<figcaption>` *see example below | Provides a caption (explanation) of an image. To be used within `<figure>`. | [I-2.3 Semantic Meaning][018] |
| `<figure>` | Contains an image and can be used to group with an image's caption | [I-2.3 Semantic Meaning][018] |
| `<mark>` *see example below | Defines a part of a text you want to highlight. The highlight styling is specified in CSS. | [I-2.3 Semantic Meaning][019] |
| `<summary>` | Used within the `<details>` tag. Specifies the visible content. The rest of the content in details is shown/hidden by user. | [I-2.3 Semantic Meaning][017] |
| `<code>` | Used to represent short computer code in a sentence. It displays code in default monospace font.  | [I-2.3 Semantic Meaning][022] |
| `<abbr>` | Used to indicate the occurrence of an abbreviation. | [I-2.3 Semantic Meaning][022] |
| `<br>` | Used to introduce a line break in your HTML document. | [I-2.3 Semantic Meaning][022] |
| `<address>` | Used to supply contact information for its nearest `<article>` or `<body>` ancestor. | [I-2.3 Semantic Meaning][022] |
| `<hr>` | Used to introduce a horizontal line in your HTML document. | [I-2.3 Semantic Meaning][022] |


## Attributes

+ __Attributes are used in tags to further define the tag__
+ Syntax: Attribute name, equal sign, opening quote, attribute value, closing quote, e.g., `start="5"`, Attribute name: start; Attribute Value = 5
+ Boolean attribute: presence = true, omit = false

### [List of Global Attributes][008]

| Name | Values | Description | Lecture |
|------|--------|-------------|---------|
| `accesskey` | list of key labels | A key label or list of key labels with which to associate the element; each key label represents a keyboard shortcut which UAs can use to activate the element or give focus to the element. <br/> An ordered set of unique space-separated tokens, each of which must be exactly one Unicode code point in length. |  |
| `class` | set of space-separated tokens | A name of a classification, or list of names of classifications, to which the element belongs. | [I-2.1 Welcome][007], [I-2.2 Attributes][012] |
| `contenteditable` | "true" or "false" or "" (empty string) or empty | Specifies whether the contents of the element are editable. |  |
| `contextmenu` | ID reference | The value of the id attribute on the menu with which to associate the element as a context menu. |  |
| `dir` | "ltr" or "rtl" | Specifies the element’s text directionality. |  |
| `draggable` | "true" or "false" | Specifies whether the element is draggable. |  |
| `hidden` | "hidden" or "" (empty string) or empty | Specifies that the element represents an element that is not yet, or is no longer, relevant. |  |
| `id` | ID | A unique identifier for the element. <br/> There must not be multiple elements in a document that have the same id value. <br/> Any string, with the following restrictions: 1. must be at least one character long 2. must not contain any space characters | [I-2.1 Welcome][006], [I-2.2 Attributes][011] |
| `lang` | language tag | Specifies the primary language for the contents of the element and for any of the element’s attributes that contain text. <br/> A valid language tag, as defined in [BCP47].  | [I-2.2 Attributes][013] |
| `spellcheck` | "true" or "false" or "" (empty string) or empty | Specifies whether the element represents an element whose contents are subject to spell checking and grammar checking.  |
| `style` | string | Specifies zero or more CSS declarations that apply to the element [CSS].  | |
| `tabindex` | integer | Specifies whether the element represents an element that is is focusable (that is, an element which is part of the sequence of focusable elements in the document), and the relative order of the element in the sequence of focusable elements in the document.  | |
| `title` | normal character data | Advisory information associated with the element. | [I-2.2 Attributes][014], [I-2.4 Images][029] |


### [Event-handler Attributes][008]

| Attributes | Description |
|------------|-------------|
| `onabort = string` |Load of element was aborted by the user. |
| `onblur = string` |Element lost focus. |
| `oncanplay = string` |The UA can resume playback of media data for this video or audio element, but estimates that if playback were to be started now, the video or audio could not be rendered at the current playback rate up to its end without having to stop for further buffering of content. |
| `oncanplaythrough = string` |The UA estimates that if playback were to be started now, the video or audio element could be rendered at the current playback rate all the way to its end without having to stop for further buffering |
| `onchange = string` |User committed a change to the value of element (form control). |
| `onclick = string` |User pressed pointer button down and released pointer button over element, or otherwise activated the pointer in a manner that emulates such an action. |
| `oncontextmenu = string` |User requested the context menu for element. |
| `ondblclick = string` |User clicked pointer button twice over element, or otherwise activated the pointer in a manner that simulates such an action. |
| `ondrag = string` |User is continuing to drag element. |
| `ondragend = string` |User ended dragging element. |
| `ondragenter = string` |User’s drag operation entered element. |
| `ondragleave = string` |User’s drag operation left element. |
| `ondragover = string` |User is continuing drag operation over element. |
| `ondragstart = string` |User started dragging element. |
| `ondrop = string` |User completed drop operation over element. |
| `ondurationchange = string` |The DOM attribute duration on the video or audio element has been updated. |
| `onemptied = string` |The video or audio element has returned to the uninitialized state. |
| `onended = string` |The end of the video or audio element has been reached. |
| `onerror = string` |Element failed to load properly. |
| `onfocus = string` |Element received focus. |
| `onformchange = string` |User committed a change to the value of a form control in the form to which the element belongs. |
| `onforminput = string` |User changed the value of a form control in the form to which the element belongs. |
| `oninput = string` |User changed the value of element (form control). |
| `oninvalid = string` |Element (form control) did not meet validity constraints. |
| `onkeydown = string` |User pressed down a key. |
| `onkeypress = string` |User pressed down a key that is associated with a character value. |
| `onkeyup = string` |User release a key. |
| `onload = string` |Element finished loading. |
| `onloadeddata = string` |UA can render the video or audio element at the current playback position for the first time. |
| `onloadedmetadata = string` |UA has just determined the duration and dimensions of the video or audio element. |
| `onloadstart = string` |UA has begun looking for media data in the video or audio element. |
| `onmousedown = string` |User pressed down pointer button over element. |
| `onmousemove = string` |User moved mouse. |
| `onmouseout = string` |User moved pointer off boundaries of element. |
| `onmouseover = string` |User moved pointer into boundaries of element or one of its descendant elements. |
| `onmouseup = string` |User released pointer button over element. |
| `onmousewheel = string` |User rotated wheel of mouse or other device in a manner that emulates such an action. |
| `onpause = string` |User has paused playback of the video or audio element. |
| `onplay = string` |UA has initiated playback of the video or audio element. |
| `onplaying = string` |Playback of the video or audio element has started. |
| `onprogress = string` |UA is fetching media data for the video or audio element. |
| `onratechange = string` |Either the DOM attribute defaultPlaybackRate or the DOM attribute playbackRate on the video or audio element has been updated. |
| `onreadystatechange = string` |Element and all its subresources have finished loading. |
| `onscroll = string` |Element or document view was scrolled. |
| `onseeked = string` |The value of the IDL attribute seeking changed to false (a seek operation on the video or audio element ended). |
| `onseeking = string` |The value of the IDL attribute seeking changed to true, and the seek operation on the video or audio elements is taking long enough that the UA has time to fire the seeking event. |
| `onselect = string` |User selected some text. |
| `onshow = string` |User requested the element be shown as a context menu. |
| `onstalled = string` |UA is attempting to fetch media data for the video or audio element, but that data is not forthcoming. |
| `onsubmit = string` |The form element was submitted. |
| `onsuspend = string` |UA is intentionally not currently fetching media data for the video or audio element, but does not yet have the entire contents downloaded. |
| `ontimeupdate = string` |The current playback position of the video or audio element changed either as part of normal playback, or in an especially interesting way (for example, discontinuously). |
| `onvolumechange = string` |Either the DOM attribute volume or the DOM attribute muted on the video or audio element has been changed. |
| `onwaiting = string` |Playback of the video or audio element has stopped because the next frame is not yet available (but UA agent expects that frame to become available in due course). |


## Non-global Attributes

[__MDN Attribute List__](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)

| Attribute | Element | Description | Link |
|-----------|---------|-------------|------| 
| `<start>` | `<ol>` | Defines the first number if other than 1. |  |
| `<reversed>` | `<ol>` | Indicates whether the list should be displayed in a descending order instead of a ascending. | [I-2. Attributes][009] |
| `<div>` | G | define a division or a section of the document; a block level element | [2.3 Semantic Meaning][025] | 
| `<span>` | similar to `<div>` but different; an inline element | [2.3 Semantic Meaning][025| |
| `<img>` | G | embeds an image into the document | [I-2.4 Images][026] |
| `<src>` | `<audio>`, `<embed>`, `<iframe>`, `<img>`, `<input>`, `<script>`, `<source>`, `<track>`, `<video>` |  The URL of the embeddable content. | [I-2.4 Images][027] |
| `<alt>` | `<applet>`, `<area>`, `<img>`, `<input>` | Alternative text in case an image can't be displayed. |  [I-2.4 Images][028] |
| `<height>` | `<canvas>`, `<embed>`, `<iframe>`, `<img>`, `<input>`, `<object>`, `<video>` | Specifies the height of elements listed here. For all other elements, use the CSS height property. | [I-2.4 Images][030] |
| `<width>` | `<canvas>`, `<embed>`, `<iframe>`, `<img>`, `<input>`, `<object>`, `<video>` | For the elements listed here, this establishes the element's width. | [I-2.4 Images][030] |
| `<href>` | `<a>`, `<area>`, `<base>`, `<link>` | The URL of a linked resource. | [I-2.5 Hyperlinks][032] |
| `<target>` | `<a>`, `<area>`, `<base>`, `<form>` | specify the destination where the linked URL in href should be opened | [I-2.5 Hyperlinks][033] |
| `<media>` | `<a>`, `<area>`, `<link>`, `<source>`, `<style>` | Specifies a hint of the media for which the linked resource was designed. | [I-2.5 Hyperlinks][034] |
| `<download>` | `<a>`, `<area>` | Indicates that the hyperlink is to be used for downloading a resource. | [I-2.5 Hyperlinks][035] |


## Table Element

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 60vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10vw">Type</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 20vw">Element</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10vw">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>Table</td>
    <td> &lt;table&gt; </td>
    <td> <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-table-tag"> Table </a></td>
  </tr>
  <tr>
    <td>Caption</td>
    <td> &lt;caption&gt; </td>
    <td> <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-caption-tag"> Table Caption </a></td>
  </tr>
  <tr>
    <td>Row groups</td>
    <td> &lt;thead&gt;, &lt;tfoot&gt;, &lt;tbody&gt; </td>
    <td> <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-thead-tag"> Table Header </a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-tfoot-tag"> Table Footer </a>, , <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-tbody-tag"> Table Body </a></td>
  </tr>
  <tr>
    <td>Column groups</td>
    <td> &lt;colgroup&gt;, &lt;col&gt; </td>
    <td> <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-colgroup-and-col-tags"> Table Column </a></td>
  </tr>
  <tr>
    <td>Table row</td>
    <td> &lt;tr&gt; </td>
    <td> <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-tr-tags"> Table Row </a></td>
  </tr>
  <tr>
    <td>Table cells</td>
    <td> &lt;th&gt;, &lt;td&gt; </td>
    <td> <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-th-tags"> Row Heading </a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-td-tags"> Table Data </a></td>
  </tr>
  </tbody>
</table>



### The th tag

| Attributes for `<th>` | Purpose | Usage | Output | 
|-----------------------|---------|-------|--------|
| `colspan` | Specifies the number of cells you want that column to span (cover) <br/> Possible values: positive integer number | `<th colspan="2">` | [View example](https://codepen.io/w3devcampus/pen/xXERVo) |
| `rowspan` | Specifies the number of cells you want the row to span (cover) <br/> Possible values: positive integer number | `<th rowspan="2">` | [View example](https://codepen.io/w3devcampus/pen/WZGojz) |
| `scope` | Specifies if a header cell is the header for a `row`, `column`, `rowgroup` or `colgroup` <br/> Possible values: `row`, `col`, `rowgroup`, `colgroup`, `auto` | `<th scope="row">` | [View example](https://codepen.io/w3devcampus/pen/YrGpEG) |


### The td tag

| Attributes for `<td>` | Purpose | Usage | Output |
|-----------------------|---------|-------|--------|
| `colspan` | Specifies the number of cells you want that column to span (cover) <br/> Possible values: positive integer number | `<td colspan="2">` | [View example](https://codepen.io/w3devcampus/pen/zEKoRg) | 
| `rowspan` | Specifies the number of cells you want the row to span (cover) <br/> Possible values: positive integer number | `<td rowspan="2">` | [View example](https://codepen.io/w3devcampus/pen/PJGbeJ) | 
| `headers` | Value is the 'id' of the `<th>` tag it corresponds to if any | `<tr>` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `<th id="header-id">` <br/> `</tr>` <br/> `<tr>` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `<td headers="header-id">` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `<td headers="header-id">` <br/> `</tr>` | [View example](https://codepen.io/w3devcampus/pen/KXgNxr) | 




## Image Element

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="35%">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="30%">Usage</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Link</td>
  </tr>
  <tr>
    <td>src</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Where to fetch the image from (must have)</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">Values:</span></p>
      <ul>
        <li><span style="font-family: arial,helvetica,sans-serif;">Path to an image file within your Web site</span></li>
        <li><span style="font-family: arial,helvetica,sans-serif;">Path to an image file that resides elsewhere on the Web</span></li>
      </ul>
    </td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="example.png" alt="Example Tutorial Image"&gt;</span></p>
    </td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#image-src-attribute">Source</a></p>
    </td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>alt</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Provide a short description of what the image is about (must have)</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here"&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#the-alt-attribute">Alternative Text</a></p>
    </td>
  </tr>
  <tr>
    <td>title</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">A global attribute to provide the title of the image</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" title="Add a title of the image"&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#the-title-attribute">Image Ttitle</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#global-attribute-title-">Global Ttitle</a></p>
    </td>
  </tr>
  <tr>
    <td>height <br/><br/> width</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Resize the image in pixels without using an external editor</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" height="hhh"&gt;</span><br/><br/><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" width="www"&gt;</span><br/><br/><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" width="www" height="hhh"&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#the-height-width-attributes">Size</a></p>
    </td>
  </tr>
</tbody>
</table>



## Audio Element

### [Audio Tag][038]

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="30%">Usage</td>
  </tr>
  <tr>
    <td>src</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Used to specify the URL of the audio file to embed.</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">Values:</span></p>
      <ul>
        <li><span style="font-family: arial,helvetica,sans-serif;">absolute URL (file residing somewhere on the Web)</span></li>
        <li><span style="font-family: arial,helvetica,sans-serif;">relative URL (within your Web site)</span></li>
      </ul>
    </td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3"&gt;&lt;/audio&gt;</span></p>
    </td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>controls</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified provides controls for the user like play, pause, seek bar and volume</span></p>
      <p><img alt="Controls from HTML5 audio" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/327f2b7346ed0f5b804d41e3d49dd8ea/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/audio-controls.PNG" type="saveimage" target="[object Object]" isimmediatepropagationstopped="function t(){return!1}" ispropagationstopped="function t(){return!1}" isdefaultprevented="function t(){return!1}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" stoppropagation="function (){r.isPropagationStopped=n}" preventdefault="function (){r.isDefaultPrevented=n}" width="263" height="26"></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls&gt;&lt;/audio&gt;</span></td>
  </tr>
  <tr>
    <td>loop</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified loops media content</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls loop&gt;&lt;/audio&gt;</span></td>
  </tr>
  <tr>
    <td>muted</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified mutes media when playback begins</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls muted&gt;&lt;/audio&gt;</span></td>
  </tr>
  <tr>
<td>preload</td>
<td>
<p><span style="font-family: arial,helvetica,sans-serif;">Allows author to communicate to the browser which settings will work best - audio should not be preloaded (none), only audio metadata is fetched (metadata), audio file can be downloaded when page loads (auto)</span><br><span style="font-family: arial,helvetica,sans-serif;">values: none, metadata, auto</span></p>
</td>
<td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls preload="auto"&gt;&lt;/audio&gt;</span></td>
</tr>
<tr>
<td>autoplay</td>
<td>
<p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified will automatically begin playing the source file as soon as it can without waiting for the entire audio file to finish downloading</span></p>
<p></p>
</td>
<td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls autoplay&gt;&lt;/audio&gt;</span><audio autoplay="autoplay"></audio></td>
</tr>
</tbody>
</table>


### [Source Tag][039]


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<tbody>
  <tr>
    <th style="text-align: left; background-color: #3d64ff; color: #ffffff;" width="15%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="30%">Usage</td>
  </tr>
  <tr>
    <td>src</td>
    <td><span style="font-family: arial,helvetica,sans-serif;">Specifies the URL of the media file</span></td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;source src="sounds/flute.mp3"&gt;</span></td>
  </tr>
  <tr>
    <td>type</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Specifies the internet media type, also known as the MIME type for the audio resource. A media type is an identifier for file formats and format contents transmitted over the internet like text and audio files.</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">It consists of a type and a sub-type. Eg: "audio/mpeg" - <strong>audio</strong> is the type and <strong>mpeg</strong> is the subtype. It can also take optional parameters that can be specified after a semicolon - "audio/ogg; codecs=opus" means the audio is in the ogg format and uses the opus codec. If the browser supports the Ogg format but not the Opus codec, the audio file will not load.</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">If the type attribute is not specified, the media type is retrieved from the server.</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;source src="sounds/flute.mp3" type="audio/mpeg"&gt;</span></td>
  </tr>
</tbody>
</table>


## Video Element

### [Video Tag][087]

<table style="font-family: arial,helvetica,sans-serif; max-width: 100%;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;"  width="40%">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="35%">Usage</td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>src</td>
    <td>specifies the URL or location of the media file</td>
    <td width="40%">&lt;video&nbsp;src="multimedia/running.mp4"&gt;&lt;/video&gt;</td>
  </tr>
  <tr>
    <td>autoplay</td>
    <td>Boolean attribute when specified will automatically begin playing source file as soon as it can without waiting for the entire video&nbsp;file to finish downloading. Note: Some versions of chrome support autostart instead of autoplay</td>
    <td width="40%">
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;autoplay&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>controls</td>
    <td>
      <p>Boolean attribute when specified provides controls for the user like play, pause, seek bar and volume</p>
      <p><img alt="Image of HTML5 video controls" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b30f1164c96da183a2c339b152ebe472/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/video-controls.PNG" type="saveimage" target="[object Object]" isimmediatepropagationstopped="function t(){return!1}" ispropagationstopped="function t(){return!1}" isdefaultprevented="function t(){return!1}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" stoppropagation="function (){r.isPropagationStopped=n}" preventdefault="function (){r.isDefaultPrevented=n}" width="232" height="26"></p>
    </td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>loop</td>
    <td>Boolean attribute when specified loops media content</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&nbsp;loop&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>muted</td>
    <td>Boolean attribute when specified mutes media when playback begins</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&nbsp;muted&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>preload</td>
    <td>Allows author to communicate to the browser which settings will work best - video&nbsp;should not be preloaded (none), only video&nbsp;metadata is fetched (metadata), video&nbsp;file can be downloaded (auto)<br>values: none, metadata, auto</td>
    <td>
      <p>&lt;video&gt; src="multimedia/running.mp4"&nbsp;controls&nbsp;preload="auto"&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>poster</td>
    <td>Specifies the URL of the frame you want to display as&nbsp;the video cover until the user starts or seeks the video. By default, the first frame is considered the poster frame. &nbsp;The poster can also be an arbitrary image, not necessarily in any frame of the video.</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;poster="/images/video-screenshot.png" controls&gt;</p>
    </td>
  </tr>
  <tr>
    <td>height, width</td>
    <td>height and width of the video's play area in pixels. Always set height and width for a video so the browser can allocate the specified space for it when it loads the page.&nbsp;</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&nbsp;width="320" height="240"&gt;&lt;/video&gt;</p>
    </td>
  </tr>
</tbody>
</table>


### [Source Tag][088]

<table style="font-family: arial,helvetica,sans-serif; max-width: 100%;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; min-width: 5em;">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; min-width: 13em;">Usage</td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>src</td>
    <td>Specifies the URL or location of the media file</td>
    <td>&lt;source src="multimedia/small.mp4"&gt;&lt;/source&gt;</td>
  </tr>
  <tr>
    <td>type</td>
    <td>
      <p>Specifies the internet media type, also known as the MIME type for the audio/video resource. A media type is an identifier for file formats and format contents transmitted over the internet like text and audio files.</p>
      <p>It consists of a type and a sub-type. Eg: "video/mp4" - <b>video</b>&nbsp;is the type and <strong>mp4</strong>&nbsp;is the subtype. It can also take optional parameters that can be specified after a semicolon - "video/mp4; codecs="avc1.42E01E, mp4a.40.2"" means the video&nbsp;is in the mp4 format and uses the codecs -&nbsp;avc1.42E01E, mp4a.40.2. If the browser supports the mp4&nbsp;format but none of the&nbsp;avc1.42E01E, mp4a.40.2&nbsp;codecs, the video file will not load.</p>
      <p>If the type attribute is not specified, the media type is retrieved from the server.</p>
    </td>
    <td>&lt;source src="multimedia/small.mp4" type="video/mp4"&gt;&lt;/source&gt;</td>
  </tr>
</tbody>
</table>


### [Track Element][089]


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="35%">Usage</td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>default</td>
    <td>It is a boolean attribute. If you have multiple tracks for the same video file, you can specify which one is the default using this attribute. It can be used on one track element in a video. If you only have one track element, default should still be added to deliver the video with captions turned on in most browsers.</td>
    <td>
      <p>&lt;video src="multimedia/small.mp4" controls&gt; <br/>
      &nbsp; &lt;track src="captions/small-en.vtt" label="english" default&gt;<br/>
      &nbsp; &lt;track src="captions/small-fr.vtt" label="French"&gt;<br/>
      &lt;/video&gt;</p>
    </td>


## Embedded Content

### [The iframe Tag][090]


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="35%">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%">Value</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%">Example</td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>src</td>
    <td>Specifies the address of the page you want to display in your frame. This is the primary attribute of interest in the iframe.</td>
    <td>URL</td>
    <td>&lt;iframe src="https://www.w3.org/"&gt;&lt;/iframe&gt;</td>
  </tr>
  <tr>
    <td>allowfullscreen</td>
    <td>This will allow the iframe to open "Full screen mode", often used with videos. Without this attribute, full screen mode is disabled for the iframe.</td>
    <td>no value</td>
    <td><span style="line-height: 22.4px;">&lt;iframe src="https://www.w3.org/" allowfullscreen&gt;&lt;/iframe&gt;</span></td>
  </tr>
  <tr>
    <td>name</td>
    <td>Specifies a name for the iframe. Using the name attribute, the iframe can act as a target for a link. Just as the 'self' target will replace the current window with the site at the href URL, and "_blank" will open a new window at that URL, if you set the name attribute, that name can be used as a target so that when you click on it, the new page will open up in that iframe.</td>
    <td>text</td>
    <td>
      <p>&lt;iframe name="frame-one" src="https://www.w3.org/"&gt;&lt;/iframe&gt;</p>
      <p>&lt;a href="https://www.wikipedia.org/" target="frame-one"&gt;&lt;/a&gt;</p>
    </td>
  </tr>
  <tr>
    <td>sandbox</td>
    <td>
      <p>This can&nbsp;apply a number of restrictions on the iframe, preventing the site in the iframe from using pop-ups, running scripts, automatically running videos and numerous other things. &nbsp;This helps avoid some of the potential security issues that iframes may be prone to.</p>
    </td>
    <td><no value="">no value (applies all restrictions)<br>allow-forms<br>allow-modals<br>allow-orientation-lock<br>allow-pointer-lock<br>allow-popups<br>allow-same-origin<br>allow-scripts<br>allow-top-navigation<br></no></td>
    <td>
      <p>&lt;iframe src="https://www.w3.org/" sandbox&gt;&lt;/iframe&gt;</p>
      <p>OR</p>
      <p>&lt;iframe src="https://www.w3.org/" sandox="allow-popups"&gt;&lt;/iframe&gt;</p>
    </td>
  </tr>
  <tr>
    <td>width, height</td>
    <td>While width and height are valid attributes for an iframe, they should be avoided in favor of CSS properties.</td>
    <td>pixels</td>
    <td>&lt;iframe src="https://www.w3.org/" width="500"&gt;&lt;/iframe&gt;</td>
  </tr>
  </tbody>
</table>





<br/><br/>

---------------------------------------------

<!--

[083]: 
[084]: 
[085]: 
[086]: 
[087]: 
[088]: 
[089]: 
[090]: 
[091]: 
[092]: 
[093]: 
[094]: 
[095]: 
[096]: 
[097]: 
[098]: 
[099]: 
[100]: 
[101]: 
[102]: 
[103]: 
[104]: 
[105]: 
[106]: 
[107]: 
[108]: 
[109]: 
[110]: 
[111]: 
[112]: 
[113]: 
[114]: 
[115]: 
[116]: 
[117]: 
[118]: 
[119]: 
[120]: 
[121]: 
[122]: 
[123]: 
[124]: 
[125]: 
[126]: 
[127]: 
[128]: 
[129]: 
[130]: 
[131]: 
[132]: 
[133]: 
[134]: 
[135]: 
[136]: 
[137]: 
[138]: 
[139]: 
[140]: 
[141]: 
[142]: 
[143]: 
[144]: 
[145]: 
[146]: 
[147]: 
[148]: 
[149]: 
[150]: 
[151]: 
[152]: 
[153]: 
[154]: 
[155]: 
[156]: 
[157]: 
[158]: 
[159]: 
[160]: 
[161]: 
[162]: 
[163]: 
[164]: 
[165]: 
[166]: 
[167]: 
[168]: 
[169]: 
[170]: 
[171]: 
[172]: 
[173]: 
[174]: 
[175]: 
[176]: 
[177]: 
[178]: 
[179]: 
[180]: 
[181]: 
[182]: 
[183]: 
[184]: 
[185]: 
[186]: 
[187]: 
[188]: 
[189]: 
[190]: 
[191]: 
[192]: 
[193]: 
[194]: 
[195]: 
[196]: 
[197]: 
[198]: 
[199]: 
-->



[000]: ../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#all-together-now
[001]: ../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#everything-in-html
[002]: https://www.w3.org/TR/2011/WD-html5-20110113/named-character-references.html
[003]: ../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#15-best-practices
[004]: ../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used
[005]: ../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn
[006]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#example-1-the-id-attribute
[007]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#example-2-the-class-attribute
[008]: https://www.w3.org/wiki/HTML/Attributes/_Global
[009]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#non---global-attributes
[010]: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes
[011]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#global-attributes-id
[012]:  ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#global-attributes-class
[013]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#global-attributes-lang
[014]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#global-attributes-title
[015]:  ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#changes-in-html5
[016]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#semantic-vs-style-tags
[017]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#detail-element
[018]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#figcaption-element
[019]:  ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#mark-element
[020]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#effect-of-semantic-elements
[021]:  ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#new-html5-semantic-elements
[022]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#lesser-known-semantic-elements
[023]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#header-vs-h1---h6
[024]:  ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#article-and-section-elements
[025]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#div-and-span-elements
[026]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-img-tag
[027]:  ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#image-src-attribute
[028]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-alt-attribute
[029]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-title-attribute
[030]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-height-weight-attributes
[031]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#anchor-element
[032]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-href-attribute
[033]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-target-attribute
[034]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-media-attribute
[035]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-download-attribute
[036]: ../WebDev/Frontend-W3C/1.HTML5CSS/03-CSS.md#
[037]: ../WebDev/Frontend-W3C/1.HTML5CSS/03-CSS.md#
[038]: /WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#audio-tag
[039]: /WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#source-element-for-multiple-source-files

[062]: ../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model
[063]: https://www.w3schools.com/css/css_padding.asp
[064]: https://www.w3schools.com/css/css_border.asp
[065]: https://www.w3schools.com/css/css_margin.asp
[066]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#3-2-css-basic-syntax



[070]: ../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-left-top-right-and-bottom-properties
[071]: ../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#-z-index-
[072]: https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html
[073]: https://developer.mozilla.org/en-US/docs/Web/CSS/position
[074]: https://developer.mozilla.org/en-US/docs/Web/CSS/left


