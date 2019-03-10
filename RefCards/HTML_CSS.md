# Reference Cards for Web Development

## HTML5

### Best Practices

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
    <a href="https://www.w3schools.com/html/html_layout.asp"> <br/>
        <img src="https://www.w3schools.com/html/img_sem_elements.gif" alt="HTML5 offers new semantic elements that define the different parts of a web page" title="HTML Layout" height="250" style="display: block; margin: auto; background-color: white"  alt="HTML Layout Elements" title="HTML Layout Elements" width="200">
    </a>
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

+ [Named Character Reference][002]

    | Symbol | Entity Name | Entity Number | Usage |
    |--------|-------------|---------------|-------|
    | Less than '<' | `&lt;` | `&#60;` | Div tag: `&lt;` |
    | Greater than '>' | `&gt;` | `&#62;` | Div tag: `&lt;div&gt;` |
    | Ampersand '&' | `&amp;` | `&#38;` | `Tom &amp; Jerry` |
    | Non-breaking space - space that will not create a new line | `&nbsp;` | `&#160;` | If you add multiple spaces, the browser will remove all but one. So you have to use this entity to add multiple spaces in your HTML page. |
    | Quotes " | `&quot;` | `&#34;` | Link to a another section on the same page using the id of the element: `&lt;a href=&quot;&num;timetable&quot;&gt;` <br/> Displayed as: `<a href="#timetable">` <br/> `&quot;` is generally encouraged for code. For an actual quotation, `<q>` or `<blockquote>` is preferred. |

+ Case Sensitive
    + Tags: case insensitive
    + Attributes: case sensitive

+ Single and double quotes are interchangeable, but not mixing

+ Headings are really useful for some assistive technology users and missing levels can be confusing.

+ Always declare the language of your page in the `<html>` tag

### HTML/Tag Syntax

<a href="https://www.w3.org/community/webed/wiki/HTML/Training/Tag_syntax">
    <img src="https://www.w3.org/community/webed/wiki/images/3/39/Elements.png"  style="margin-right: 0.3em;" alt="HTML elements usually come in tag pairs" title="HTML elements" width="350">
    <img src="https://www.w3.org/community/webed/wiki/images/b/bc/Option.png"  alt="An element can have attributes to refine its meaning." title="HTML elements" width="350">
</a>


### Tags

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
| `<style>` | place CSS directly into an HTML document; anywhere in an HTML document;most common place: `<head>` section | [I-3.1 Welcome]
| `<link>` | bin `.css` file within `<head>` section | [I-3.1 Welcome]



### Semantic Elements

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


### Attributes

+ __Attributes are used in tags to further define the tag__
+ Syntax: Attribute name, equal sign, opening quote, attribute value, closing quote, e.g., `start="5"`, Attribute name: start; Attribute Value = 5
+ Boolean attribute: presence = true, omit = false

#### [List of Global Attributes][008]

##### Core Attributes

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


#### [Event-handler Attributes][008]

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


### Non-global Attributes

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


### Table Element

| Type | Element | Link |
|------|---------|------|
| Table | `<table>` | [Table][066] |
| Caption | `<caption>` | [Tbl Caption][067] |
| Row groups | `<thead>`, `<tfoot>`, `<tbody>` | [Tbl Header][068], [Tbl Body][069], [Tbl Footer][070] |
| Column groups | `<colgroup>`, `<col>` | [Tbl Col][071] |
| Table row | `<tr>` | [Tbl Row][072] |
| Table cells | `<th>`, `<td>` | [Row Heading][073], [Tbl Data][074] |



#### The th tag

| Attributes for `<th>` | Purpose | Usage | Output | Link |
|-----------------------|---------|-------|--------|------|
| `colspan` | Specifies the number of cells you want that column to span (cover) <br/> Possible values: positive integer number | `<th colspan="2">` | [View example](https://codepen.io/w3devcampus/pen/xXERVo) | [Row Heading][073] |
| `rowspan` | Specifies the number of cells you want the row to span (cover) <br/> Possible values: positive integer number | `<th rowspan="2">` | [View example](https://codepen.io/w3devcampus/pen/WZGojz) | [Row Heading][073] |
| `scope` | Specifies if a header cell is the header for a `row`, `column`, `rowgroup` or `colgroup` <br/> Possible values: `row`, `col`, `rowgroup`, `colgroup`, `auto` | `<th scope="row">` | [View example](https://codepen.io/w3devcampus/pen/YrGpEG) | [Row Heading][073] |


#### The td tag

| Attributes for `<td>` | Purpose | Usage | Output | Link |
|-----------------------|---------|-------|--------|------|
| `colspan` | Specifies the number of cells you want that column to span (cover) <br/> Possible values: positive integer number | `<td colspan="2">` | [View example](https://codepen.io/w3devcampus/pen/zEKoRg) | [Tbl Data][074] |
| `rowspan` | Specifies the number of cells you want the row to span (cover) <br/> Possible values: positive integer number | `<td rowspan="2">` | [View example](https://codepen.io/w3devcampus/pen/PJGbeJ) | [Tbl Data][074] |
| `headers` | Value is the 'id' of the `<th>` tag it corresponds to if any | `<tr>` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `<th id="header-id">` <br/> `</tr>` <br/> `<tr>` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `<td headers="header-id">` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `<td headers="header-id">` <br/> `</tr>` | [View example](https://codepen.io/w3devcampus/pen/KXgNxr) | [Tbl Data][074] |


### Image Element

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


### Audio Element

#### [Audio Tag][085]

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


#### [Source Tag][086]


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


### Video Element

#### [Video Tag][087]

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


#### [Source Tag][088]

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


#### [Track Element][089]


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
  </tr>
  <tr>
    <td>kind</td>
      <td>Specifies the kind of the source&nbsp;file. <br>Values: subtitles (default value), captions, descriptions (textual description of the video best suited for the blind who cannot be seen), chapters (meant for chapter titles), metadata (kind of track that is used by scripts and is not visible to the user).</td>
    <td>
      <p>&lt;track src="captions/small-en.vtt" kind="captions"&gt;</p>
    </td>
  </tr>
  <tr>
    <td>label</td>
    <td>Label of the track.&nbsp;Browser uses the label value to display track options for user to select.&nbsp;</td>
    <td>
      <p>&lt;track src="captions/small-en.vtt" label="English"&gt;<br/>
      <span style="line-height: 22.4px;">&lt;track src="captions/small-fr.vtt" label="French"&gt;</span></p>
    </td>
  </tr>
  <tr>
    <td>src</td>
    <td>URL of track. The <strong>file must be on a Web server</strong>. The .vtt file cannot be loaded from a file (file://) protocol.</td>
    <td>
      <p>&lt;track src="http://www.xyz.org/small-en.vtt"&gt;</p>
    </td>
  </tr>
  <tr>
    <td>srclang</td>
    <td>Language of text track. Eg: en, fr. <br>If kind&nbsp;is 'subtitles', then the srclang attribute must be specified.</td>
    <td>
      <p>&lt;track src="captions/small-en.vtt" kind="subtitles" srclang="en"&gt;</p>
    </td>
  </tr>
  </tbody>
</table>


### Embedded Content

#### [The iframe Tag][090]

## CSS3

### CSS Syntax

<a href="https://www.w3schools.com/css/css_syntax.asp">
    <img src="https://www.w3schools.com/css/selector.gif" alt="The selector points to the HTML element you want to style. The declaration block contains one or more declarations separated by semicolons. Each declaration includes a CSS property name and a value, separated by a colon. A CSS declaration always ends with a semicolon, and declaration blocks are surrounded by curly braces." title="CSS rule-set consists of a selector and a declaration block" height="80">
</a>

### [Selectors][054]

| Selector | HTML | CSS | Link |
|----------|------|-----|------|
| tag | `<li>` | `li {list-style_type: circle;}` | [Selector][055] |
| id | `<p id="p18"> Ulysses </p>` | `#p18 {color: blue;}` | [Selector][056] |
| class | `<li class="bird flying">eagle</li>` | `.bird   { color: blue; }` <br/> `.flying { text-decoration: underline; }` | [Selector][057] |
| Comma separated |  | `blockquote,` <br/> `q,` <br/> `.speech {` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `color: red;` <br/>&nbsp;&nbsp;&nbsp;&nbsp; `font-style: italic;` <br/> `}` <br/> `.speech { font-weight: bold; }` | [Selector][058] |
| Specialized | `<li class="insect flying">wasp</li>` | `.insect.flying {` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `text-decoration: underline;` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `font-weight: bold;` <br/>   `}` | [Selector][059] |
| Descendant  | `<section id="intro">Welcome to <a href="#palaceland">PalaceLand</a>` | `#intro a { color: red; }` | [Selector][060] |
| Direct descendant | `<section id="intro">Welcome to <a href="#palaceland">PalaceLand</a>` | `#intro > a { font-size: large; }` | [Selector][061] |

<br/><br/>



### [Properties][038]

| Property | Description | Value Options | Link |
|----------|-------------|---------------|------|
| `color` | text color | `blue`, `lightblue`, `darkblue`, `red`, etc. | |
| `font-size` | size the text of a tag | `px`, `em`, `%`, `vh` | [Common Prty][039] |
| `line-height` | height of the space | `<number>` | [Common Prty][040] |
| `text-align` | alignment | `left`, `center`, `right`, `justify`, `justify-all` | [Common Prty][041] |
| `text-decoration` | the decoration added to text | `underline`, `overline`, `line-through`, `none` | [Common Prty][042] |
| `font-weight` | text bolder (or less bold) | `normal`, `bold`, `bolder`, `lighter`, `<number>` | [Common Prty][043] |
| `font-family` | font for an element | `serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`, etc. | [Common Prty][044] |
| `list-style-type` | list marker, usually positioned to the left of any list item | ul: `disc`, `circle`, `square`, `none`; <br/>ol: `decimal`, `decimal-leading-zero`, `lower-roman`, `upper-roman`, `lower-alpha`, `upper-alpha`, `armenian`, `georgian`, `simp-chinese-formal`, etc. | [List][051] |
| `list-style-position` | how closely it is positioned to the list itself | `inside`, `outside` | [List][052] |
| `list-style-image` | customized little markers on a list | `url("path/fig.png")` | [List][053] |





### Measurement Units

| Unit | Specification | Link |
|------|---------------|------|
| `px` | pixel, a single dot on the screen | [Units][046] |
| `em` | vertical dimensions, height of capital letter in the _parent_ context | [Units][047] |
| `rem` | vertical dimensions, size relative to the _root_ | [Units][048] |
| `%` | relative to the _parent_ dimension | [Units][049] |
| `vh` | viewport height, percentage of the screen | [Units][050] |
| `vw` | viewport width, percentage of the screen | [Units][050] |

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

## CSS3

### CSS Syntax

<a href="https://www.w3schools.com/css/css_syntax.asp">
    <img src="https://www.w3schools.com/css/selector.gif" style="display: block; margin: auto; background-color: white" alt="The selector points to the HTML element you want to style. The declaration block contains one or more declarations separated by semicolons. Each declaration includes a CSS property name and a value, separated by a colon. A CSS declaration always ends with a semicolon, and declaration blocks are surrounded by curly braces." title="CSS rule-set consists of a selector and a declaration block" height="80">
</a>


### Selectors

#### [CSS Selector Reference](https://www.w3schools.com/cssref/css_selectors.asp)

<table  style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%">Selector</th>    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%">Example</th>    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;">Example description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="sel_class.asp">.<i>class</i></a></td>    <td>.intro</td>    <td>Selects all elements with class="intro"</td>
  </tr>
  <tr>
    <td><a href="sel_id.asp">#<i>id</i></a></td>    <td>#firstname</td>    <td>Selects the element with id="firstname"</td>
  </tr>  <tr>
    <td><a href="sel_all.asp">*</a></td>    <td>*</td>    <td>Selects all elements</td>
  </tr>
  <tr>
    <td><i><a href="sel_element.asp">element</a></i></td>    <td>p</td>    <td>Selects all &lt;p&gt; elements</td>
  </tr>
  <tr>
    <td><i><a href="sel_element_comma.asp">element,element</a></i></td>    <td>div, p</td>    <td>Selects all &lt;div&gt; elements and all &lt;p&gt; elements</td>
  </tr>
  <tr>
    <td><a href="sel_element_element.asp"><i>element</i> <i>element</i></a></td>    <td>div p</td>    <td>Selects all &lt;p&gt; elements inside &lt;div&gt; elements</td>
  </tr>
  <tr>
    <td><a href="sel_element_gt.asp"><i>element</i>&gt;<i>element</i></a></td>    <td>div &gt; p</td>    <td>Selects all &lt;p&gt; elements where the parent is a &lt;div&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_element_pluss.asp"><i>element</i>+<i>element</i></a></td>    <td>div + p</td>    <td>Selects all &lt;p&gt; elements that are placed immediately after &lt;div&gt; elements</td>
  </tr>
  <tr>
    <td><a href="sel_gen_sibling.asp"><i>element1</i>~<i>element2</i></a></td>    <td>p ~ ul</td>    <td>Selects every &lt;ul&gt; element that are preceded by a &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_attribute.asp">[<i>attribute</i>]</a></td>    <td>[target]</td>    <td>Selects all elements with a target attribute</td>
  </tr>
  <tr>
    <td><a href="sel_attribute_value.asp">[<i>attribute</i>=<i>value</i>]</a></td>    <td>[target=_blank]</td>    <td>Selects all elements with target="_blank"</td>
  </tr>
  <tr>
    <td><a href="sel_attribute_value_contains.&#x24;asp">[<i>attribute</i>~=<i>value</i>]</a></td>    <td>[title~=flower]</td>    <td>Selects all elements with a title attribute containing the word "flower"</td>
  </tr>
  <tr>
    <td><a href="sel_attribute_value_lang.asp">[<i>attribute</i>|=<i>value</i>]</a></td>    <td>[lang|=en]</td>    <td>Selects all elements with a lang attribute value starting with "en"</td>
  </tr>
  <tr>
    <td><a href="sel_attr_begin.asp">[<i>attribute</i>^=<i>value</i>]</a></td>    <td>a[href^="https"]</td>    <td>Selects every &lt;a&gt; element whose href attribute value begins with "https"</td>
  </tr>
  <tr>
    <td><a href="sel_attr_end.asp">[<i>attribute</i>&#x24;=<i>value</i>]</a></td>    <td>a[href$=".pdf"]</td>    <td>Selects every &lt;a&gt; element whose href attribute value ends with ".pdf"</td>
  </tr>
  <tr>
    <td><a href="sel_attr_contain.asp">[<i>attribute</i>*=<i>value</i>]</a></td>    <td>a[href*="w3schools"]</td>    <td>Selects every &lt;a&gt; element whose href attribute value contains the substring "w3schools"</td>
  </tr>
  <tr>
    <td><a href="sel_active.asp">:active</a></td>    <td>a:active</td>    <td>Selects the active link</td>
  </tr>
  <tr>
    <td><a href="sel_after.asp">::after</a></td>    <td>p::after</td>    <td>Insert something after the content of each &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_before.asp">::before</a></td>    <td>p::before</td>    <td>Insert something before&nbsp;the content of each &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_checked.asp">:checked</a></td>    <td>input:checked</td>    <td>Selects every checked &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_default.asp">:default</a></td>    <td>input:default</td>    <td>Selects the default &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_disabled.asp">:disabled</a></td>    <td>input:disabled</td>    <td>Selects every disabled &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_empty.asp">:empty</a></td>    <td>p:empty</td>    <td>Selects every &lt;p&gt; element that has no children (including text nodes)</td>
  </tr>
  <tr>
    <td><a href="sel_enabled.asp">:enabled</a></td>    <td>input:enabled</td>    <td>Selects every enabled &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_firstchild.asp">:first-child</a></td>    <td>p:first-child</td>    <td>Selects every &lt;p&gt; element that is the first child of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_firstletter.asp">::first-letter</a></td>    <td>p::first-letter</td>    <td>Selects the first letter of every &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_firstline.asp">::first-line</a></td>    <td>p::first-line</td>    <td>Selects the first line of every &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_first-of-type.asp">:first-of-type</a></td>    <td>p:first-of-type</td>    <td>Selects every &lt;p&gt; element that is the first &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_focus.asp">:focus</a></td>    <td>input:focus</td>    <td>Selects the input element which has focus</td>
  </tr>
  <tr>
    <td><a href="sel_hover.asp">:hover</a></td>    <td>a:hover</td>    <td>Selects links on mouse over</td>
  </tr>
  <tr>
    <td><a href="sel_in-range.asp">:in-range</a></td>    <td>input:in-range</td>    <td>Selects input elements with a value within a specified range</td>
  </tr>
  <tr>
    <td><a href="sel_indeterminate.asp">:indeterminate</a></td>    <td>input:indeterminate</td>    <td>Selects input elements that are in an indeterminate state</td>
  </tr>
  <tr>
    <td><a href="sel_invalid.asp">:invalid</a></td>    <td>input:invalid</td>    <td>Selects all input elements with an invalid value</td>
  </tr>
  <tr>
    <td><a href="sel_lang.asp">:lang(<i>language</i>)</a></td>    <td>p:lang(it)</td>    <td>Selects every &lt;p&gt; element with a lang attribute equal to "it" (Italian)</td>
  </tr>
  <tr>
    <td><a href="sel_last-child.asp">:last-child</a></td>    <td>p:last-child</td>    <td>Selects every &lt;p&gt; element that is the last child of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_last-of-type.asp">:last-of-type</a></td>    <td>p:last-of-type</td>    <td>Selects every &lt;p&gt; element that is the last &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_link.asp">:link</a></td>    <td>a:link</td>    <td>Selects all unvisited links</td>
  </tr>
  <tr>
    <td><a href="sel_not.asp">:not(<i>selector</i>)</a></td>    <td>:not(p)</td>    <td>Selects every element that is not a &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_nth-child.asp">:nth-child(<i>n</i>)</a></td>    <td>p:nth-child(2)</td>    <td>Selects every &lt;p&gt; element that is the second child of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_nth-last-child.asp">:nth-last-child(<i>n</i>)</a></td>    <td>p:nth-last-child(2)</td>    <td>Selects every &lt;p&gt; element that is the second child of its parent, counting from the last child</td>
  </tr>
  <tr>
    <td><a href="sel_nth-last-of-type.asp">:nth-last-of-type(<i>n</i>)</a></td>    <td>p:nth-last-of-type(2)</td>    <td>Selects every &lt;p&gt; element that is the second &lt;p&gt; element of its parent, counting from the last child</td>
  </tr>
  <tr>
    <td><a href="sel_nth-of-type.asp">:nth-of-type(<i>n</i>)</a></td>    <td>p:nth-of-type(2)</td>    <td>Selects every &lt;p&gt; element that is the second &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_only-of-type.asp">:only-of-type</a></td>    <td>p:only-of-type</td>    <td>Selects every &lt;p&gt; element that is the only &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_only-child.asp">:only-child</a></td>    <td>p:only-child</td>    <td>Selects every &lt;p&gt; element that is the only child of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_optional.asp">:optional</a></td>    <td>input:optional</td>    <td>Selects input elements with no "required" attribute</td>
  </tr>
  <tr>
    <td><a href="sel_out-of-range.asp">:out-of-range</a></td>    <td>input:out-of-range</td>    <td>Selects input elements with a value outside a specified range</td>
  </tr>
  <tr>
    <td><a href="sel_placeholder.asp">::placeholder</a></td>    <td>input::placeholder</td>    <td>Selects input elements with placeholder text</td>
  </tr>
  <tr>
    <td><a href="sel_read-only.asp">:read-only</a></td>    <td>input:read-only</td>    <td>Selects input elements with the "readonly" attribute specified</td>
  </tr>
  <tr>
    <td><a href="sel_read-write.asp">:read-write</a></td>    <td>input:read-write</td>    <td>Selects input elements with the "readonly" attribute NOT specified</td>
  </tr>
  <tr>
    <td><a href="sel_required.asp">:required</a></td>    <td>input:required</td>    <td>Selects input elements with the "required" attribute specified</td>
  </tr>
  <tr>
    <td><a href="sel_root.asp">:root</a></td>    <td>:root</td>    <td>Selects the document's root element</td>
  </tr>
  <tr>
    <td><a href="sel_selection.asp">::selection</a></td>    <td>::selection</td>    <td>Selects the portion of an element that is selected by a user</td>
  </tr>
  <tr>
    <td><a href="sel_target.asp">:target</a></td>    <td>#news:target </td>    <td>Selects the current active #news element (clicked on a URL containing that anchor name)</td>
  </tr>
  <tr>
    <td><a href="sel_valid.asp">:valid</a></td>    <td>input:valid</td>    <td>Selects all input elements with a valid value</td>
  </tr>
  <tr>
    <td><a href="sel_visited.asp">:visited</a></td>    <td>a:visited</td>    <td>Selects all visited links</td>
  </tr>
</tbody></table>

<br/>

#### Lecture Note

| Selector | HTML | CSS | Link |
|----------|------|-----|------|
| tag | `<li>` | `li {list-style_type: circle;}` | [Selector][055] |
| id | `<p id="p18"> Ulysses </p>` | `#p18 {color: blue;}` | [Selector][056] |
| class | `<li class="bird flying">eagle</li>` | `.bird   { color: blue; }` <br/> `.flying { text-decoration: underline; }` | [Selector][057] |
| Comma separated | `,` | `blockquote,` <br/> `q,` <br/> `.speech {` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `color: red;` <br/>&nbsp;&nbsp;&nbsp;&nbsp; `font-style: italic;` <br/> `}` <br/> `.speech { font-weight: bold; }` | [Selector][058] |
| Specialized | `<li class="insect flying">wasp</li>` | `.insect.flying {` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `text-decoration: underline;` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `font-weight: bold;` <br/>   `}` | [Selector][059] |
| Descendant  | `<section id="intro">Welcome to <a href="#palaceland">PalaceLand</a>` | `#intro a { color: red; }` | [Selector][060] |
| Direct descendant | `<section id="intro">Welcome to <a href="#palaceland">PalaceLand</a>` | `#intro > a { font-size: large; }` | [Selector][061] |


### CSS Precedence

Rules:

1. __inline > style/css file__: inline css ( html style attribute ) overrides css rules in style tag and css file
2. __specific > less-specific__: a more specific selector takes precedence over a less specific one
3. __later > earlier__: rules that appear later in the code override earlier rules if both have the same specificity.
4. __`!important`__ highest: A css rule with `!important` always takes precedence.


Four categories which define the [specificity level](https://www.w3schools.com/css/css_specificity.asp) of a selector:

1. __Inline styles__ - An inline style is attached directly to the element to be styled. Example: `<h1 style="color: #ffffff;">`.
2. __IDs__ - An ID is a unique identifier for the page elements, such as `#navbar`.
3. __Classes, attributes and pseudo-classes__ - This category includes `.classes`, `[attributes]` and pseudo-classes such as `:hover`, `:focus` etc.
4. __Elements__ and __pseudo-elements__ - This category includes element names and pseudo-elements, such as `h1`, `div`, `:before` and `:after`.

[selector's specificity calculation](https://www.w3.org/TR/selectors-3/#specificity):

+ count the number of ID selectors in the selector (= a)
+ count the number of class selectors, attributes selectors, and pseudo-classes in the selector (= b)
+ count the number of type selectors and pseudo-elements in the selector (= c)
+ ignore the universal selector

  Examples:

  ```ssh
  *               /* a=0 b=0 c=0 -> specificity =   0 */
  LI              /* a=0 b=0 c=1 -> specificity =   1 */
  UL LI           /* a=0 b=0 c=2 -> specificity =   2 */
  UL OL+LI        /* a=0 b=0 c=3 -> specificity =   3 */
  H1 + *[REL=up]  /* a=0 b=1 c=1 -> specificity =  11 */
  UL OL LI.red    /* a=0 b=1 c=3 -> specificity =  13 */
  LI.red.level    /* a=0 b=2 c=1 -> specificity =  21 */
  #x34y           /* a=1 b=0 c=0 -> specificity = 100 */
  #s12:not(FOO)   /* a=1 b=0 c=1 -> specificity = 101 */
  ```



### CSS Website Layout - Example

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.w3schools.com/css/css_website_layout.asp">
    <img src="css-layout.png" style="margin: 0.1em;" alt="There are tons of different layout designs to choose from. However, the structure above, is one of the most common, and we will take a closer look at it in this tutorial." title="A website is often divided into headers, menus, content and a footer" width="400">
  </a></div>
</div>


### [Font Properties][038]

| Property | Description | Value Options | Link |
|----------|-------------|---------------|------|
| `color` | text color | `blue`, `lightblue`, `darkblue`, `red`, etc. | |
| `font-size` | size the text of a tag | `px`, `em`, `%`, `vh` | [Common Prty][039] |
| `line-height` | height of the space | `<number>` | [Common Prty][040] |
| `text-align` | alignment | `left`, `center`, `right`, `justify`, `justify-all` | [Common Prty][041] |
| `text-decoration` | the decoration added to text | `underline`, `overline`, `line-through`, `none` | [Common Prty][042] |
| `font-weight` | text bolder (or less bold) | `normal`, `bold`, `bolder`, `lighter`, `<number>` | [Common Prty][043] |
| `font-family` | font for an element | `serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`, etc. | [Common Prty][044] |
| `list-style-type` | list marker, usually positioned to the left of any list item | ul: `disc`, `circle`, `square`, `none`; <br/>ol: `decimal`, `decimal-leading-zero`, `lower-roman`, `upper-roman`, `lower-alpha`, `upper-alpha`, `armenian`, `georgian`, `simp-chinese-formal`, etc. | [List][051] |
| `list-style-position` | how closely it is positioned to the list itself | `inside`, `outside` | [List][052] |
| `list-style-image` | customized little markers on a list | `url("path/fig.png")` | [List][053] |





### Measurement Units

| Unit | Specification | Link |
|------|---------------|------|
| `px` | pixel, a single dot on the screen | [Units][046] |
| `em` | vertical dimensions, height of capital letter in the _parent_ context | [Units][047] |
| `rem` | vertical dimensions, size relative to the _root_ | [Units][048] |
| `%` | relative to the _parent_ dimension | [Units][049] |
| `vh` | viewport height, percentage of the screen | [Units][050] |
| `vw` | viewport width, percentage of the screen | [Units][050] |


### Table Properties

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.tallcomponents.com/tallpdf/help/guide/tables?build=net40">
    <img src="https://www.tallcomponents.com/tallpdf5/content/guide/tallpdf/media/table-border-padding-and-margin.png" style="margin: 0.1em;" alt="The extra space outside a border is set by a left, right, top and bottom margin. The extra space inside a border is set by a left, right, top and bottom padding. These attributes are part of the table, row or cell. The following figure makes this clear." title="Padding, Margins and Border Width" width="400">
  </a></div>
  <div><a href="http://learningspot.altervista.org/html-table-tag-attributes/">
    <img src="http://learningspot.altervista.org/wp-content/uploads/2017/07/HTML_cellpadding_cellspacing.png" style="margin: 0.1em;" alt="The size indicated in cellpadding and cellspacing, once set, affects all sides of the cell." title="Table cell padding and spacing" width="345">
  </a></div>
</div>

#### Table Properties

| Property | Applied To | Description | Possible Value | Link |
|----------|------------|-------------|----------------|------|
| `border` | `<table>`, `<th>` `<td>` | sets border-width, border-style and border-color in order | `<width, style, color>`: width = pixel, style = none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset; color = color name or color values, transparent | [Border][075] |
| `border-collapse` | `<table>`, `<th>`, `<td>` | to collapse border or not | separate - default value <br/> collapse - border are collapsed into a single border <br/> initial - sets to default value (separate) | [Collapse][076] |
| `width`; `height` | `<td>` | set the width and height for the rows and columns for your table based on the content in your cells | units of length like pixels, percentage; auto: the browser will calculate and select a width for the specified element (default value) | [Size][077] |
| `text-align` | `<th>`, `<td>` | align the text of and cells left, right or center |  left, right or center; Default: `<th>` - center, `<td>` - left | [Horizontal][078] |
| `vertical-align` | `<th>`, `<td>` | align the text of and cells top, bottom or middle | top, bottom or middle; default: middle | [Vertical][079] |
| `padding` | `<th>`, `<td>` | provide some space between border and content in cell | units of length like px, cm, % - relative to parent container's width | [Padding][080] | border-spacing | `<table>`, `<td>`, `<th>` | space between content in cell and border | units of length like px, cm, % - relative to parent container's width | [Space][081] |
| `border-top`, `border-right`, `border-bottom`, `border-left` | `<th>`, `<td>` | set borders to individual sides | `<width, style, color>` | [Side][082] |


#### Styling with Pseudo Class

| Class | Description | Possible Property/Values | Link |
|-------|-------------|-------------------|------|
| `tr:nth-child(even)`, `tr:nth-child(odd)` | alternating colors for table rows making it easier to differentiate data between rows | `background-color: color;` | [Zebra][083] |
| `tr.hover` | mouse over rows in your table to highlight them in the color specified | `background-color: black;` | [Hover][084] |






### Box Model

<a href="https://www.w3.org/TR/CSS22/box.html"> 
    <img src="https://www.w3.org/TR/CSS22/images/boxdim.png" alt="Each box has a content area (e.g., text, an image, etc.) and optional surrounding padding, border, and margin areas; the size of each area is specified by properties defined below. The following diagram shows how these areas relate and the terminology used to refer to pieces of margin, border, and padding. The margin, border, and padding can be broken down into top, right, bottom, and left segments (e.g., in the diagram, 'LM' for left margin, 'RP' for right padding, 'TB' for top border, etc.)." title="The four areas of the generic CSS box: content, padding, border, and margin." width="350" style="display: block; margin: auto; background-color: white"> <br/>
</a>


<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 20%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>padding</td>
    <td>padding for all sides of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-top</td>
    <td>padding for top side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-right</td>
    <td>padding for right side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-bottom</td>
    <td>padding for bottom side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-left</td>
    <td>padding for left side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border</td>
    <td>the style, width, and color of an element's border</td>
    <td>border-width, border-style (required), border-color</td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-style</td>
    <td>what kind of border to display</td>
    <td>dotted, dashed, solid, double, groove, ridge, inset, outset, none, hidden <br/><br/>Examples: <br/><ul><li>border-style: dotted solid double dashed;</li>  <li>border-style: dotted solid double;</li>, <li>border-style: dotted solid;</li>,  <li>border-style: dotted;</li></ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-width</td>
    <td>the width of the four borders</td>
    <td>px, pt, cm, em, thin, medium, thick</td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-color</td>
    <td>the color of the four borders</td>
    <td>name, Hex, RGB, transparent</td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin</td>
    <td>space around elements, outside of any defined borders</td>
    <td>#px, auto <br/><br/> Example: <br/><ul><li>margin: top right bottom left;</li>  <li>margin: top right bottom</li> <li>margin: top right</li></ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-top</td>
    <td>space on top of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-right</td>
    <td>space on right of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-bottom</td>
    <td>space on bottom of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-left</td>
    <td>space on left of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  </tbody>
</table>



### Display: Block and Inline Elements

#### [Display Elements](../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#display-property):


### Display Flow Layout

+ Normal Flow / Flow Layout
  + the way that Block and Inline elements are displayed on a page before any changes are made to their layout
  + essentially a set of things that are all working together and know about each other in your layout

+ Block-level vs. inline
  + Content model:
    + block-level element may contain inline elements and other block-level elements
    + block elements create "larger" structures than inline elements
  + Default formating:
    + block-level elements begin on new lines
    + in-line elements can start anywhere in a line

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements#Elements"> Block-level Element </a></td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements#Elements">Inline Element</a></td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>&lt;address&gt;: Contact information<br/>&lt;article&gt;: Article content<br/>&lt;aside&gt;: Aside content<br/>&lt;blockquote&gt;: Long ("block") quotation<br/>&lt;details&gt;: Disclosure widget<br/>&lt;dialog&gt;: Dialog box<br/>&lt;dd&gt;: Describes a term in a description list<br/>&lt;div&gt;: Document division<br/>&lt;dl&gt;: Description list<br/>&lt;dt&gt;: Description list term<br/>&lt;fieldset&gt;: Field set label<br/>&lt;figcaption&gt;: Figure caption<br/>&lt;figure&gt;: Groups media content with a caption (see &lt;figcaption&gt;)<br/>&lt;footer&gt;: Section or page footer<br/>&lt;form&gt;: Input form<br/>&lt;h1&gt;, &lt;h2&gt;, &lt;h3&gt;, &lt;h4&gt;, &lt;h5&gt;, &lt;h6&gt;: Heading levels 1-6<br/>&lt;header&gt;: Section or page header; &lt;hgroup&gt;: Groups header information<br/>&lt;hr&gt;: Horizontal rule (dividing line)<br/>&lt;li&gt;: List item<br/>&lt;main&gt;: Contains the central content unique to this document<br/>&lt;nav&gt;: Contains navigation links<br/>&lt;ol&gt;: Ordered list<br/>&lt;p&gt;: Paragraph<br/>&lt;pre&gt;: Preformatted text<br/>&lt;section&gt;: Section of a web page<br/>&lt;table&gt;: Table<br/>&lt;ul&gt;: Unordered list</td>
    <td>&lt;a&gt;, &lt;abbr&gt;, &lt;acronym&gt;, &lt;audio&gt;, &lt;b&gt;<br/>&lt;bdi&gt;, &lt;bdo&gt;, &lt;big&gt;, &lt;br&gt;, &lt;button&gt;<br/>&lt;canvas&gt;, &lt;cite&gt;, &lt;code&gt;, &lt;data&gt;, &lt;datalist&gt;<br/>&lt;del&gt;, &lt;dfn&gt;, &lt;em&gt;, &lt;embed&gt;, &lt;i&gt;<br/>&lt;iframe&gt;, &lt;img&gt;, &lt;input&gt;, &lt;ins&gt;, &lt;kbd&gt;<br/>&lt;label&gt;, &lt;map&gt;, &lt;mark&gt;, &lt;meter&gt;, &lt;noscript&gt;<br/>&lt;object&gt;, &lt;output&gt;, &lt;picture&gt;, &lt;progress&gt;, &lt;q&gt;<br/>&lt;ruby&gt;, &lt;s&gt;, &lt;samp&gt;, &lt;script&gt;, &lt;select&gt;<br/>&lt;slot&gt;, &lt;small&gt;, &lt;span&gt;, &lt;strong&gt;, &lt;sub&gt;<br/>&lt;sup&gt;, &lt;svg&gt;, &lt;template&gt;, &lt;textarea&gt;, &lt;time&gt;<br/>&lt;u&gt;, &lt;tt&gt;, &lt;var&gt;, &lt;video&gt;, &lt;wbr&gt;</td>
  </tr>
  </tbody>
</table>

#### [Display Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/display#Syntax)

```css
/* <display-outside> values */
display: block;
display: inline;
display: run-in;

/* <display-inside> values */
display: flow;
display: flow-root;
display: table;
display: flex;
display: grid;
display: ruby;

/* <display-outside> plus <display-inside> values */
display: block flow;
display: inline table;
display: flex run-in;

/* <display-listitem> values */
display: list-item;
display: list-item block;
display: list-item inline;
display: list-item flow;
display: list-item flow-root;
display: list-item block flow;
display: list-item block flow-root;
display: flow list-item block;

/* <display-internal> values */
display: table-row-group;
display: table-header-group;
display: table-footer-group;
display: table-row;
display: table-cell;
display: table-column-group;
display: table-column;
display: table-caption;
display: ruby-base;
display: ruby-text;
display: ruby-base-container;
display: ruby-text-container;

/* <display-box> values */
display: contents;
display: none;

/* <display-legacy> values */
display: inline-block;
display: inline-table;
display: inline-flex;
display: inline-grid;
```

+ Categories
  1. `<display-outside>`: specify the element’s outer display type, which is essentially its role in flow layout
  2. `<display-inside>`: specify the element’s inner display type, which defines the type of formatting context that its contents are laid out in (assuming it is a non-replaced element)
  3. `<display-listitem>`: generate a block box for the content and a separate list-item inline box
  4. `<display-internal>`: Some layout models such as table and ruby have a complex internal structure, with several different roles that their children and descendants can fill
  5. `<display-box>`: define whether an element generates display boxes at all
  6. `<display-legacy>`: used a single-keyword syntax for the display property, requiring separate keywords for block-level and inline-level variants of the same layout mode.


#### Display Characteristics

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Property</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%"><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#block-level">Block Level</a></td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%"><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#inline-elements">Inline Element</a></td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%"><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#nline-block">Inline-Block</a></td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>Position</td>
    <td><ul> <li> below and left of their block level neighbors </li> </ul></td>
    <td><ul> <li> right of their preceding inline elements </li> <li> cleave to the baseline where they are being placed </li></ul></td>
    <td><ul> <li> cleave to the text baseline </li> </ul></td>
  </tr>
  <tr>
    <td>Width</td>
    <td><ul> <li> expand to fill the width of the parent container by default </li> <li> make width narrower and wrap, but not crop </li> <li>take the width of their parent</li> <li> centering - <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#block">"margin: auto;" </li> </ul></td>
    <td><ul> <li>width of the content of the element, plus any padding</li> <li> no width properties </li> <li> subject to CSS white-space settings </li> <li> centering - <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#inline">"text-align: center;"</a> </li> </ul></td>
    <td><ul> <li> adjusted to make room respect to width properties </li> </ul></td>
  </tr>
  <tr>
    <td>Height</td>
    <td><ul> <li>take on the height of all its children</li> <li> no vertical-align property</li> <li>take the height of their content </li> <li>centering - <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#inline-1">"vertical-align: center;" </a></li> </ul></td>
    <td><ul> <li>no height properties</li> <li> subject to vertical-align property </li> <li>line-height property</li> <li>centering - <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#inline-1">flexbox</a> </li></ul></td>
    <td><ul> <li> adjusted to make room respect to height properties </li> </ul></td>
  </tr>
  <tr>
    <td>Margin</td>
    <td><ul> <li> respect all margin properties</li> </ul></td>
    <td><ul> <li>no top and bottom margin</li> </ul></td>
    <td><ul> <li> adjusted to make room respect to margin-top and margin-bottom </li> </ul></td>
  </tr>
  <tr>
    <td>Padding</td>
    <td><ul> <li>all padding properties</li> </ul></td>
    <td><ul> <li>padding properties, but any padding-top or padding-bottom</li> <li> keep neighbors away horizontally </li></ul></td>
    <td><ul> <li> vertical padding contribute to the calculation of the height of the line it falls on </li> </ul></td>
  </tr>
  </tbody>
</table>


### Positioned Property

<table table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>left, top, right, bottom</td>
    <td><ul> <li>adjust or set the position of an element</li> <li>determine the final location of positioned elements</li></ul></td>
    <td>length-value, percentage, auto</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-left-top-right-and-bottom-properties">Position</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/left">Left</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/top">Top</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/bottom">Bottom</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/right">Right</a></td>
  </tr>
  <tr>
    <td>z-index</td>
    <td><ul> <li>control overlapping - whether or not an element is in front of or behind other sibling positioned elements</li> <li>The higher the number, the more "topmost" or "overlapping" the element will be.</li></ul></td>
    <td>auto, integer</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#-z-index-">Z-Index</a></td>
  </tr>
  <tr>
    <td>float</td>
    <td><ul> <li>place an element on the left or right side of its container, allowing text and inline elements to wrap around it</li> <li>removed from the normal flow of the page, though still remaining a part of the flow</li></ul></td>
    <td>none, left, right, inline-start, inline-end</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/float">Float</a></td>
  </tr>
  <tr>
    <td>clear</td>
    <td><ul> <li>applied to floating and non-floating elements</li></ul></td>
    <td>none, left, right, both, inline-start, inline-end</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/clear">Clear</a></td>
  </tr>
  <tr>
    <td>position</td>
    <td><ul> <li>applied to floating and non-floating elements</li></ul></td>
    <td>none, left, right, both, inline-start, inline-end</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">Position</a></td>
  </tr>
  </tbody>
</table>


#### Position Characteristics

<table table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>static</td>
    <td><ul> <li>follow the "flowing text" model of layout </li> <li>influenced by margins, padding</li> <li>block level layout, inline or inline-block</li> <li>default value</li> </ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#static">Static</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html"> Positioning </a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"> MDN </a></td>
  </tr>
  <tr>
    <td>fixed</td>
    <td><ul><li>positioned against the window rectangle (aka the viewport) </li> <li>Best practice: use both a horizontal and a vertical positioning property on every fixed positioned element</li> <li> etermined by the values of top, right, bottom, and left</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#fixed">Fixed</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html"> Positioning </a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"> MDN </a></td>
  </tr>
  <tr>
    <td>relative</td>
    <td><ul><li>exactly like static in that the "flowing text" model of layout is setting the initial position for the element (including margins and display) but move the named edge of the element from its initial position </li> <li>positioned according to the normal flow of the document is positioned relative to its normal position, and then offset relative to itself based on the values of top, right, bottom, and left</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#relative">Relative</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html"> Positioning </a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"> MDN </a></td>
  </tr>
  <tr>
    <td>absolute</td>
    <td><ul><li>taken out of the normal text "flow" that governs elements positioned statically or relatively </li> <li>positioned by the left, top, right, and/or bottom properties </li> <li>relative to the closest positioned ancestor, if there is any; otherwise, it is placed relative to the initial containing block and its final position is determined by the values of top, right, bottom, and left</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#absolute">Absolute</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html"> Positioning </a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"> MDN </a></td>
  </tr>
  <tr>
    <td>sticky</td>
    <td><ul><li>positioned corresponding to the normal flow of the document, and then offset relative to its closest ascending block-level, including table-related elements, according to the values of top, right, bottom, and left</td>
    <td><a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html"> Positioning </a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"> MDN </a></td>
  </tr>
  </tbody>
</table>


### Sizing Properties

#### Global Sizing

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 20%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>height</td>
    <td>Sets the height of an element</td>
  </tr>
  <tr>
    <td>max-height</td>box-sizing
    <td>Sets the maximubox-sizingent</td>
  </tr>
  <tr>
    <td>max-width</td>
    <td>Sets the maximum width of an element</td>
  </tr>
  <tr>
    <td>min-height</td>
    <td>Sets the minimum height of an element</td>
  </tr>
  <tr>
    <td>min-width</td>
    <td>Sets the minimum width of an element</td>
  </tr>
  <tr>
    <td>width</td>
    <td>Sets the width of an element</td>
  </tr>
  </tbody>
</table>


#### Box Sizing


<table table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Example</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>content-box</td>
    <td><ul> <li>the default CSS box-sizing behavior</li> <li>including width and height, but not padding, border, or margin</li><li> the dimensions of the element: width = width of the content; height = height of the content</li></ul></td>
    <td><div>box-sizing: content-box;<br/>width: 100%</div><br/><div>box-sizing: content-box;<br/>width: 100%;<br/>border: solid #5B6DCD 10px;</div></td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing">MDN</a>, <a href="/WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-box-model-and-box-sizing">Box-sizing</a></td>
  </tr>
  <tr>
    <td>border-box</td>
    <td><ul><li>telling the browser to account for any border and padding in the values specified for an element's width and height</li><li>including width and height, padding & border, but not margin</li><li> the dimensions of the element: width = border + padding + width of the content, height = border + padding + height of the content</li></ul></td>
    <td><div>box-sizing: content-box;<br/>width: 100%</div><div>box-sizing: content-box;<br/>width: 100%;<br/>border: solid #5B6DCD 10px;</div></td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing">MDN</a>, <a href="/WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-box-model-and-box-sizing">Box-sizing</a></td>
  </tr>
  </tbody>
</table>



### Cropping and scrolling

<table table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>overflow</td>
    <td><ul> <li>specified as one or two keywords chosen from the list of values below</li> <li>two keywords: (overflow-x, overflow-y)</li><li>create a new block formatting context except visible </li><li>if a float intersected with the scrolling element it would forcibly rewrap the content after each scroll step, leading to a slow scrolling experience</li><li>the block-level container must have either a set height (height or max-height) or white-space set to nowrap</li></ul></td>
    <td>visible, hidden, auto, scroll, clip, hidden visible</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow">Overflow</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Lecture</a></td>
  </tr>
  <tr>
    <td>overflow-block</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows a block-level element's block start and block end edge</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-block">Overflow-Block</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Lecture</a></td>
  </tr>
  <tr>
    <td>overflow-inline</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows an inline element's start and end edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-inline">Overflow-Inline</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Lecture</a></td>
  </tr>
  <tr>
    <td>overflow-x</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows a block-level element's left and right edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-x">Overflow-X</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Lecture</a></td>
  </tr>
  <tr>
    <td>overflow-y</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows an inline element's top and bottom edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-y">Overflow-Y</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Lecture</a></td>
  </tr>
  </tbody>
</table>


### The Flexible Box Layout

#### Basic Concepts of flexbox

+ Layout and Axes
  + __main axis__:
    + the axis running in the direction the flex items are being laid out in
    + __main start__ and __main end__: the start and end of main axis
  + __cross axis__:
    + the axis running perpendicular to the direction the flex items are being laid out in
    + __cross start__ and __cross end__:  start and end of cross axis
  + __flex container__: set parent element w/ `display: fex`
  + __flex items__: the items being laid out as flexible boxes inside the flex container

+ main axis defined by __flex-direction__
  + row: along the row in the inline direction from left to right
  + row-reverse: along the row in the inline direction from right to left
  + column: from the top of the page to the bottom
  + column-reverse: from the bottom of the page to the top

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox">
      <img src="https://mdn.mozillademos.org/files/15614/Basics1.png" style="margin: 0.1em;" alt="row or row-reverse: main axis will run along the row in the inline direction" title="Inline directon: row or row-reverse" width="250">
      <img src="https://mdn.mozillademos.org/files/15615/Basics2.png" style="margin: 0.1em;" alt="column or column-reverse: main axis will run from the top of the page to the bottom — in the block direction" title="Block direction: column or column-reverse" width="250">
      <img src="https://mdn.mozillademos.org/files/15616/Basics3.png" style="margin: 0.1em;" alt=" flex-direction (main axis) is set to row or row-reverse the cross axis runs down the columns" title="The cross axis runs perpendicular to the main axis" width="250">
      <img src="https://mdn.mozillademos.org/files/15617/Basics4.png" style="margin: 0.1em;" alt="main axis is column or column-reverse then the cross axis runs along the rows" title="main axis is column or column-reverse then the cross axis runs along the rows" width="250">
    </a></div>
  </div>

+ [The flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox#The_flex_container)
  + An area of a document laid out using flexbox
  + set the value of the area's container's display property to `flex` or `inline-flex`
  + flex items: the direct children of that container
  + ways to create a flex container all of the contained flex items
    + Items display in a row (the `flex-direction` property's default is `row`).
    + The items start from the start edge of the main axis.
    + The items do not stretch on the main dimension, but can shrink.
    + The items will stretch to fill the size of the cross axis.
    + The `flex-basis` property is set to `auto`.
    + The `flex-wrap `property is set to `nowrap`.

+ [Multi-line flex containers with flex-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox#The_flex_container)
  + While flexbox is a one dimensional model, it is possible to cause our flex items to wrap onto multiple lines.
  + To cause wrapping behaviour add the property `flex-wrap` with a value of `wrap`.
  + guide to wrap flex items: [Mastering Wrapping of Flex Items](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Mastering_Wrapping_of_Flex_Items)



#### Flexbox Property


<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>flex</td>
    <td>specified using one, two, or three values:<ul> <li><strong>One-value syntax:</strong><ul><li>&lt;number&gt;: interpreted as &lt;flex-grow&gt;</li><li>value for width: interpreted as &lt;flex-basis&gt;</li><li>keywords: none, auto, or initial</li></ul></li> <li><strong>Two-value syntax</strong>: the first value, &lt;number&gt;, interpreted as &lt;flex-grow&gt;. The second value must be one of: <ul><li>&lt;number&gt;: interpreted as &lt;flex-shrink&gt;</li><li>value for width: interpreted as &lt;flex-basis&gt;</li></ul></li><li><strong>Three-value syntax</strong> (order): <ol><li>&lt;number&gt; for &lt;flex-grow&gt;</li><li>&lt;number&gt; for &lt;flex-shrink&gt;</li><li>value for width: interpreted as &lt;flex-basis&gt;</li></ol></li></ul></td>
    <td>init, auto, none, &lt;flex-grow&gt;, &lt;flex-shrink&gt;, &lt;flex-basis&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-minimum">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-direction</td>
    <td>set how flex items placed in the flex container defining the main axis and the direction (normal or reversed)</td>
    <td>row, row-reverse, column, column-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-wrap</td>
    <td>set whether flex items are forced onto one line or can wrap onto multiple lines</td>
    <td>nowrap, wrap, wrap-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-flow</td>
    <td>a shorthand property for <strong>flex-direction</strong> and <strong>flex-wrap</strong> properties</td>
    <td>nowrap, wrap, wrap-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-flow">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-basis</td>
    <td><ul><li>set the initial main size of a flex item</li><li>content: automatic sizing, based on the flex item’s content</li></ul></td>
    <td>&lt;width&gt;, content</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-grow</td>
    <td><ul><li>set how much of the remaining space in the flex container should be assigned to that item (the flex grow factor)</li><li>remaining space: the size of the flex container minus the size of all flex items together</li><li>sibling items: <ul><li>all items with the same share of remaining space with the same grow factor</li><li>distributed according tot he ratio defined by the different flex grow factors</li></ul></ul></td>
    <td>&lt;number&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-shrink</td>
    <td>set the flex shrink factor of a flex item</td>
    <td>&lt;number&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  </tbody>
</table>



------------------------

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
[038]: https://www.w3.org/Style/CSS/all-properties.en.html#list
[039]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#font-size
[040]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#line-height
[041]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#text-align
[042]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#text-decoration-underline
[043]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#font-weight-bold
[044]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#font-weight-bold
[045]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#font-family
[046]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#px
[047]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#em
[048]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#rem
[049]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#
[050]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#vh--vw
[051]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#list-style-type
[052]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#list-style-position
[053]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#list-style-image
[054]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#selectors
[055]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#tag-selector
[056]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#id-selector
[057]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#class-selector
[058]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#comma-separated-selectors
[059]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#specialized-selectors
[060]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#descendant-selectors
[061]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#direct-descendant-selectors---
[062]: ../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model
[063]: https://www.w3schools.com/css/css_padding.asp
[064]: https://www.w3schools.com/css/css_border.asp
[065]: https://www.w3schools.com/css/css_margin.asp

[070]: ../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-left-top-right-and-bottom-properties
[071]: ../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#-z-index-
[072]: https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html
[073]: https://developer.mozilla.org/en-US/docs/Web/CSS/position
[074]: https://developer.mozilla.org/en-US/docs/Web/CSS/left
[075]: https://developer.mozilla.org/en-US/docs/Web/CSS/top
[076]: https://developer.mozilla.org/en-US/docs/Web/CSS/right
[077]: https://developer.mozilla.org/en-US/docs/Web/CSS/bottom
[078]: https://developer.mozilla.org/en-US/docs/Web/CSS/float
[079]: https://developer.mozilla.org/en-US/docs/Web/CSS/position
[080]: https://developer.mozilla.org/en-US/docs/Web/CSS/clear
[081]: https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements#Elements
[082]: https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements#Elements
