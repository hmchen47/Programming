# HTML5 - Attributes


## Definition and Characteristics 0f Attributes

+ __Attributes are used in tags to further define the tag__

+ A given element on your Web page can be distinguished by any number of unique or common attributes.

+ Identify attribute uniquely with an 'id' attribute, or group it with a class of other elements by setting the 'class' attribute

+ Syntax: Attribute name, equal sign, opening quote, attribute value, closing quote, e.g., `start="5"`, Attribute name: start; Attribute Value = 5

+ [Boolean attribute](../WebDev/Frontend-W3C/2-HTML5Coding/02e-Multimedia.md#253-attributes-of-audio-and-video-5-8):
  + the presence of a boolean attribute on an element presents the true value
  + the absence of the attribute presents the false value
  + presence: either the empty string nor a value that is an ASCII case-incentive match for the attributes canonical name w/o leading or trailing whitespace
  + "false" and "true" not allowed on boolean attributes
  + e.g., `controls="false"` same as `control="true"` or `controls="controls"` or `controls` alone
  + bad practice: using `controls="true"`
  + <mark style="color: black; background-color: lightpink;">best practice</mark>: the presence of the attribute along

+ Reference: [Attribute List](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://www.oreilly.com/library/view/learning-web-design/9780596527525/ch04.html">
      <img src="https://www.oreilly.com/library/view/learning-web-design/9780596527525/graphics/lwd3_0411.jpg" style="margin: 0.1em;" alt="Attributes are instructions that clarify or modify an element." title="An element with attributes." width="350">
    </a></div>
  </div>


## List of Global Attributes

+ [Global attributes](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#global-)
  + applied to all tags
  + common attributes.
  + E.g., `id`, `class`

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<caption style="font-size: 1.6em; padding-bottom: 0.3em;"><a href="https://www.w3.org/wiki/HTML/Attributes/_Global#Core_Attributes">Table of Core Attributes</a></caption>
<thead>
  <tr style="border-bottom: double black;">
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Name</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Values</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 70%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Link</th>
  </tr>
</thead>
<tbody>
  <tr><td> <code>accesskey</code></td>
    <td> list of key labels</td>
    <td> A key label or list of key labels with which to associate the element; each key label represents a keyboard shortcut which UAs can use to activate the element or give focus to the element.<br>An ordered set of unique space-separated tokens, each of which must be exactly one Unicode code point in length.</td>
    <td><a href=""></a></td></tr>
  <tr><td> <code>class</code></td>
    <td> set of space-separated tokens</td>
    <td> A name of a classification, or list of names of classifications, to which the element belongs.</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#global-attributes-class">class18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#global-attribute-class-">class19</a></td></tr>
  <tr><td> <code>contenteditable</code></td>
    <td> "true" or "false" or "" (empty string) or empty</td>
    <td> Specifies whether the contents of the element are editable.</td>
    <td><a href=""></a></td></tr>
  <tr><td> <code>contextmenu</code></td>
    <td>  ID reference</td>
    <td> The value of the id attribute on the menu with which to associate the element as a context menu.</td>
    <td><a href=""></a></td></tr>
  <tr><td> <code>dir</code></td>
    <td> "ltr" or "rtl"</td>
    <td> Specifies the element’s text directionality.</td>
    <td><a href=""></a></td></tr>
  <tr><td> <code>draggable</code></td>
    <td>  "true" or "false"</td>
    <td> Specifies whether the element is draggable.</td>
    <td><a href=""></a></td></tr>
  <tr><td> <code>hidden</code></td>
    <td>  "hidden" or "" (empty string) or empty</td>
    <td> Specifies that the element represents an element that is not yet, or is no longer, relevant.</td>
    <td><a href=""></a></td></tr>
  <tr><td> <code>id</code></td>
    <td> ID</td>
    <td> A unique identifier for the element.<br>There must not be multiple elements in a document that have the same id value.<br>Any string, with the following restrictions: 1. must be at least one character long 2. must not contain any space characters</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#global-attributes-id">id18</a>, <a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#global-attribute-id-">id19</a></td></tr>
  <tr><td> <code>lang</code></td>
    <td> language tag</td>
    <td> Specifies the primary language for the contents of the element and for any of the element’s attributes that contain text.<br>A valid language tag, as defined in [BCP47].</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#global-attribute-lang-">lang</a></td></tr>
  <tr><td> <code>spellcheck</code></td>
    <td>  "true" or "false" or "" (empty string) or empty</td>
    <td> Specifies whether the element represents an element whose contents are subject to spell checking and grammar checking.</td>
    <td><a href=""></a></td></tr>
  <tr><td> <code>style</code></td>
    <td>  string</td>
    <td> Specifies zero or more CSS declarations that apply to the element [CSS].</td>
    <td><a href=""></a></td></tr>
  <tr><td> <code>tabindex</code></td>
    <td>  integer</td>
    <td> Specifies whether the element represents an element that is is focusable (that is, an element which is part of the sequence of focusable elements in the document), and the relative order of the element in the sequence of focusable elements in the document.</td>
    <td><a href=""></a></td></tr>
  <tr><td> <code>title</code></td>
    <td>  normal character data</td>
    <td> Advisory information associated with the element.</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-title-attribute">lang18</a>, <a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#global-attribute-title-">title19</a></td></tr>
</tbody>
</table>



## Event-handler Attributes


<table  style="margin: 0 auto; border: 1px solid black; border-collapse: collapse; width: 55vw;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<caption style="font-size: 1.6em; padding-bottom: 0.3em;"><a href="https://www.w3.org/wiki/HTML/Attributes/_Global#Event-handler_Attributes">Table of Event-handler Attributes</a></caption>
<thead>
  <tr style="border-bottom: double black;">
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Attributes</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
  </tr>
</thead>
<tbody>
  <tr><td> <code>onabort = string</code></td> <td>Load of element was aborted by the user.</td></tr>
  <tr><td> <code>onblur = string</code></td> <td> Element lost focus.</td></tr>
  <tr><td> <code>oncanplay = string</code></td> <td> The UA can resume playback of media data for this video or audio element, but estimates that if playback were to be started now, the video or audio could not be rendered at the current playback rate up to its end without having to stop for further buffering of content.</td></tr>
  <tr><td> <code>oncanplaythrough = string</code></td> <td> The UA estimates that if playback were to be started now, the video or audio element could be rendered at the current playback rate all the way to its end without having to stop for further buffering</td></tr>
  <tr><td> <code>onchange = string</code></td> <td> User committed a change to the value of element (form control).</td></tr>
  <tr><td> <code>onclick = string</code></td> <td> User pressed pointer button down and released pointer button over element, or otherwise activated the pointer in a manner that emulates such an action.</td></tr>
  <tr><td> <code>oncontextmenu = string</code></td> <td> User requested the context menu for element.</td></tr>
  <tr><td> <code>ondblclick = string</code></td>
    <td> User clicked pointer button twice over element, or otherwise activated the pointer in a manner that simulates such an action.</td></tr>
  <tr><td> <code>ondrag = string</code></td> <td> User is continuing to drag element.</td></tr>
  <tr><td> <code>ondragend = string</code></td> <td> User ended dragging element.</td></tr>
  <tr><td> <code>ondragenter = string</code></td> <td> User’s drag operation entered element.</td></tr>
  <tr><td> <code>ondragleave = string</code></td> <td> User’s drag operation left element.</td></tr>
  <tr><td> <code>ondragover = string</code></td> <td> User is continuing drag operation over element.</td></tr>
  <tr><td> <code>ondragstart = string</code></td> <td> User started dragging element.</td></tr>
  <tr><td> <code>ondrop = string</code></td> <td> User completed drop operation over element.</td></tr>
  <tr><td> <code>ondurationchange = string</code></td> <td> The DOM attribute duration on the video or audio element has been updated.</td></tr>
  <tr><td> <code>onemptied = string</code></td> <td> The video or audio element has returned to the uninitialized state.</td></tr>
  <tr><td> <code>onended = string</code></td> <td> The end of the video or audio element has been reached.</td></tr>
  <tr><td> <code>onerror = string</code></td> <td> Element failed to load properly.</td></tr>
  <tr><td> <code>onfocus = string</code></td> <td> Element received focus.</td></tr>
  <tr><td> <code>onformchange = string</code></td> <td> User committed a change to the value of a form control in the form to which the element belongs.</td></tr>
  <tr><td> <code>onforminput = string</code></td> <td> User changed the value of a form control in the form to which the element belongs.</td></tr>
  <tr><td> <code>oninput = string</code></td> <td> User changed the value of element (form control).</td></tr>
  <tr><td> <code>oninvalid = string</code></td> <td> Element (form control) did not meet validity constraints.</td></tr>
  <tr><td> <code>onkeydown = string</code></td> <td> User pressed down a key.</td></tr>
  <tr><td> <code>onkeypress = string</code></td> <td> User pressed down a key that is associated with a character value.</td></tr>
  <tr><td> <code>onkeyup = string</code></td> <td> User release a key.</td></tr>
  <tr><td> <code>onload = string</code></td> <td> Element finished loading.</td></tr>
  <tr><td> <code>onloadeddata = string</code></td> <td> UA can render the video or audio element at the current playback position for the first time.</td></tr>
  <tr><td> <code>onloadedmetadata = string</code></td> <td> UA has just determined the duration and dimensions of the video or audio element.</td></tr>
  <tr><td> <code>onloadstart = string</code></td> <td> UA has begun looking for media data in the video or audio element.</td></tr>
  <tr><td> <code>onmousedown = string</code></td> <td> User pressed down pointer button over element.</td></tr>
  <tr><td> <code>onmousemove = string</code></td> <td> User moved mouse.</td></tr>
  <tr><td> <code>onmouseout = string</code></td> <td> User moved pointer off boundaries of element.</td></tr>
  <tr><td> <code>onmouseover = string</code></td> <td> User moved pointer into boundaries of element or one of its descendant elements.</td></tr>
  <tr><td> <code>onmouseup = string</code></td> <td> User released pointer button over element.</td></tr>
  <tr><td> <code>onmousewheel = string</code></td> <td> User rotated wheel of mouse or other device in a manner that emulates such an action.</td></tr>
  <tr><td> <code>onpause = string</code></td> <td> User has paused playback of the video or audio element.</td></tr>
  <tr><td> <code>onplay = string</code></td> <td> UA has initiated playback of the video or audio element.</td></tr>
  <tr><td> <code>onplaying = string</code></td> <td> Playback of the video or audio element has started.</td></tr>
  <tr><td> <code>onprogress = string</code></td> <td> UA is fetching media data for the video or audio element.</td></tr>
  <tr><td> <code>onratechange = string</code></td> <td> Either the DOM attribute defaultPlaybackRate or the DOM attribute playbackRate on the video or audio element has been updated.</td></tr>
  <tr><td> <code>onreadystatechange = string</code></td> <td> Element and all its subresources have finished loading.</td></tr>
  <tr><td> <code>onscroll = string</code></td> <td> Element or document view was scrolled.</td></tr>
  <tr><td> <code>onseeked = string</code></td> <td> The value of the IDL attribute seeking changed to false (a seek operation on the video or audio element ended).</td></tr>
  <tr><td> <code>onseeking = string</code></td> <td> The value of the IDL attribute seeking changed to true, and the seek operation on the video or audio elements is taking long enough that the UA has time to fire the seeking event.</td></tr>
  <tr><td> <code>onselect = string</code></td> <td> User selected some text.</td></tr>
  <tr><td> <code>onshow = string</code></td> <td> User requested the element be shown as a context menu.</td></tr>
  <tr><td> <code>onstalled = string</code></td> <td> UA is attempting to fetch media data for the video or audio element, but that data is not forthcoming.</td></tr>
  <tr><td> <code>onsubmit = string</code></td> <td> The form element was submitted.</td></tr>
  <tr><td> <code>onsuspend = string</code></td> <td> UA is intentionally not currently fetching media data for the video or audio element, but does not yet have the entire contents downloaded.</td></tr>
  <tr><td> <code>ontimeupdate = string</code></td> <td> The current playback position of the video or audio element changed either as part of normal playback, or in an especially interesting way (for example, discontinuously).</td></tr>
  <tr><td> <code>onvolumechange = string</code></td> <td> Either the DOM attribute volume or the DOM attribute muted on the video or audio element has been changed.</td></tr>
  <tr><td> <code>onwaiting = string</code></td> <td> Playback of the video or audio element has stopped because the next frame is not yet available (but UA agent expects that frame to become available in due course).</td></tr>
</tbody>
</table>


## Non-global Attributes

+ [Non-global attributes](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#non-global-attributes)
  + applied to a specific instance of a tag
  + able to applied to one or more tags
  + E.g., `start` & `reversed` only for `<ol>`; `width` for `<img>`, `<video>` and `<input>`


<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<thead>
  <tr style="border-bottom: double black;">
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Attribute</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Element</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>start</code></td>
    <td><code>&lt;ol&gt;</code></td>
    <td>Defines the first number if other than 1</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#syntax">Start</a></td>
  </tr>
  <tr>
    <td><code>reversed</code></td>
    <td>code>&lt;ol&gt;</code></td>
    <td>Indicates whether the list should be displayed in a descending order instead of a ascending.</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#non---global-attributes">Reversed18</a>, <a href="">Reversed19</a></td>
  </tr>
  <tr>
    <td><code>src</code></td>
    <td><code>&lt;audio&gt;, &lt;embed&gt;, &lt;ifeame&gt;, &lt;img&gt;, &lt;input&gt;, &lt;script&gt;, &lt;source&gt;, &lt;track&gt;, &lt;video&gt;</code></td>
    <td>The URL of the embeddable content.</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#image-src-attribute">src18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#image-src-attribute">src19</a></td>
  </tr>
  <tr>
    <td><code>alt</code></td>
    <td><code>&lt;applet&gt;, &lt;area&gt;, &lt;img&gt;, &lt;input&gt;</code></td>
    <td>Alternative text in case an image can't be displayed.</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-alt-attribute">alt18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#attribute-alt">alt19</a></td>
  </tr>
  <tr>
    <td><code>height</code></td>
    <td><code>&lt;canvas&gt;, &lt;embed&gt;, &lt;ifeame&gt;, &lt;img&gt;, &lt;input&gt;, &lt;object&gt;, &lt;video&gt;</code></td>
    <td>Specifies the height of elements listed here. For all other elements, use the CSS height property.</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-height-weight-attributes">height18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-height-width-attributes">height19</a></td>
  </tr>
  <tr>
    <td><code>width</code></td>
    <td><code>&lt;canvas&gt;, &lt;embed&gt;, &lt;ifeame&gt;, &lt;img&gt;, &lt;input&gt;, &lt;object&gt;, &lt;video&gt;</code></td>
    <td>For the elements listed here, this establishes the element's width.</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-height-weight-attributes">width18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-height-width-attributes">width19</a></td>
  </tr>
  <tr>
    <td><code>href</code></td>
    <td><code>><code>&lt;a&gt;, &lt;area&gt;, &lt;base&gt;, &lt;link&gt;</code></td>
    <td>The URL of a linked resource.</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-href-attribute">href18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-href-attribute">href19</a></td>
  </tr>
  <tr>
    <td><code>target</code></td>
    <td><code>&lt;a&gt;, &lt;area&gt;, &lt;base&gt;, &lt;form&gt;</code></td>
    <td>specify the destination where the linked URL in href should be opened</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-target-attribute">span18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-href-attribute">span19</a></td>
  </tr>
  <tr>
    <td><code>media</code></td>
    <td><code>&lt;a&gt;, &lt;area&gt;, &lt;link&gt;, &lt;source&gt;, &lt;style&gt;</code></td>
    <td>Specifies a hint of the media for which the linked resource was designed.</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-media-attribute">media18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-media-attribute">media19</a></td>
  </tr>
  <tr>
    <td><code>download</code></td>
    <td><code>&lt;a&gt;, &lt;area&gt;</code></td>
    <td>Indicates that the hyperlink is to be used for downloading a resource.</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-download-attribute">download18</a>, <a href="">download19</a></td>
  </tr>
  <tr>
    <td><code>title</code></td>
    <td>Global</td>
    <td>Text to be displayed in a tooltip when hovering over the element.</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-title-attribute">title</a></td>
  </tr>
</tbody>
</table>


## The `translate` attribute

+ [The HTML5 `translate` attribute](../WebDev/Frontend-W3C/2-HTML5Coding/01d-Basics.md#the-html5-translate-attribute)
  + used to limit the impact of translation tools
  + useful scenarios
    + source code
    + video game Web sites proposing cheat codes
    + street names, author names, etc.
  + Google translate and Microsoft online translation services: able to prevent translation of content by themselves
  + providing a standard approach
  + enumerated attribute
    + used to specify whether an element's attribute values and the values of its Text node children to be translated when the page is localized, or whether to leave them unchanged
    + default: "no"
    + e.g., `<span translate="no">Michel Ham</span>`

