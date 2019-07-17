# Reference Cards for Web Development - HTML5

## Best Practices

### The big three: HTML5, CSS and JavaScript

+ <p style="color: darkred; font-weight: 900;"><a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#what-is-html5-">HTML</a></p>
  + Containing all the content, organized into a logical structure
  + Hypertext: built on the idea of linking information together
  + Mark Up: annotate a document with extra information; organize document with links and define how to break it down into different segments (chapters, sections, paragraphs, tables, figures, etc.)
+ <p style="color: darkred; font-weight: 900;"><a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#css">CSS</a></p>
  + The presentation or style of the page
  + What it looks like without too much regard for the specific content
  + As a "theme" in a word processing document, setting fonts, sizes, indentations and whatever else may apply to what it looks like
+ <p style="color: darkred; font-weight: 900;"><a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#javascript">Javascript</a></p>
  + The actions a page can take such as interaction with the user, and customizing and changing the page according to any number of parameters
  + Allow a Web page to be more than just a document, but potentially a Web application, with nearly unlimited possibilities



### Template

```html
<!DOCTYPE html> <!-- HTML5 -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title> My Web Page Title </title>

  <!-- CSS Usage: link preferred ~ comment for HTML-->
  <link rel="stylesheet" type="text/css" href="css/my_styles.css">
  <style>
    /* CSS will go in this area ~ comment for CSS */
  </style>
</head>
<body>
  <!-- Contents within this area -->
</body>
</html>
```

### Useful References & Tool Links

+ [W3C HTML5 specification](https://www.w3.org/TR/html5/)
+ [W3C cheatsheet](https://www.w3.org/2009/cheatsheet/)
+ [MDN attribute reference list](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)
+ [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
+ [CSS validator](https://jigsaw.w3.org/css-validator/)
+ [Unicorn](http://validator.w3.org/unicorn/)  
+ [W3C Internationalization Checker](https://validator.w3.org/i18n-checker/)
+ [W3C Link Checker](http://validator.w3.org/checklink)
+ [CodePen](http://codepen.io/)


### HTML Layout Elements

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/7e7a7ad104714c61b5b7bd35048b9ddc/dd9cc2d025bc4ac5b1a66481aac0db1b/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%4025b7c2657986416785cb4a8bb92fbfd2">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d4a392ddecb2dcc4b9a4c9efa613e6f3/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/structurecalledout-new.jpg" style="margin: 0.1em;" alt="Diagram explaining basic web page tags" title="Diagram explaining basic web page tags" width="550">
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

+ Ref: [Web page structure](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#web-page-structure)


### UTF-8: `<meta charset="utf-8">` in `head` section

+ Always use the Unicode character encoding UTF-8 for your Web pages
+ Ensure that your editor saves the file in UTF-8

### Named Characters

+ [WC3 Named character references](https://www.w3.org/TR/2011/WD-html5-20110113/named-character-references.html)

+ [HTML character codes](https://www.rapidtables.com/web/html/html-codes.html)

+ Frequent used codes

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
    <thead><tr>
      <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Symbol</th>
      <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Entity Name</th>
      <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Entity Number</th>
      <th style="background-color: #3d64ff; color: #ffffff; width: 20%">Usage</th>
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



### Recommendations & Misc.

+ Browser reality
  + the browser knows roughly what to expect in an HTML page, so if it sees a file ending in '.html' it will automatically stick some stuff in if it is not there already
  + undefined: not telling how the browser will decide to handle it; e.g., `<h1>Part of this header is<p>in the</h2> paragraph below</p>`

+ [Do's](../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#do-s-and-dont-s)
  + call for one to do it properly, and not depend on the browser to patch it for you
  + the open and close tags should always match
  + need the <!doctype> section and the &lt;html&gt; section with &lt;head&gt; and &lt;body&gt;
  + proper indentation is one way to make your code clearer and easier to understand
  + consistent quoting of strings is also helpful
  + projects will have coding styles that everyone is expected to use so that everything looks consistent and developers can more easily read each other's code

+ [Dont's](../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#do-s-and-dont-s)
  + the open and close tags should not be any overlap with other elements
  + never have a situation in which part of an element is in another, but the other part is not

+ Case Sensitive
  + [Tags](../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-are-case-insensitive): case insensitive
  + [Attributes](../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#don-t-worry-about-too-many-white-spaces): case sensitive

+ [Whitespace](../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#don-t-worry-about-too-many-white-spaces)
  + do not want to worry about the amount of white space (spaces, tabs and returns) in between words and lines and paragraphs 
  + most extra white space will be ignored
  + not matter to the browser how much white space there is, you can use white space to make your code more visibly organized and easier to read (note the use of indentation in the second `<H1>` element above)

+ [Quote](../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#any-kind-of-quotes-for-strings)
  + Single and double quotes are interchangeable, but not mixing
  + ' "quote" ' (single quotes containing a double quoted string), your string will have the letters `<space>-"-q-u-o-t-e-"-<space>` (with double quotes in the string and spaces outside those) as opposed to "quote" which will just have the letters q-u-o-t-e (no quotation marks or spaces in the string)
  + be consistent in your quotes, so it's best to quote them all the same way, even if the browser would understand it anyway

+ Headings are really useful for some assistive technology users and missing levels can be confusing.

+ Always declare the language of your page in the `<html>` tag


### Debugging

+ [Two opposite directions](../WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#identifying-html5-elements) correspond to an element
  + HTML5 code written and want to find out where on the Web page that code shows up
  + given a particular part of the page, what part of your code produced it

+ [Browsers Developer tool](../WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#modifying-html5-elements)
  + F12 or right click on mouse bu selecting `Inspect`
  + mouse hovers over an element -> highlight the corresponding element on the displayed page
  + ability to make temporary modifications to your code to try out different things and see what works the way you want it to
  + make style changes in the "Styles" panel, or use the "Computed" panel to see the values for each property and how they were determined
  + click on an element in your HTML5 source code to change the source code
  + add a "style" attribute to a particular element, which should override any other settings
  + 



## Element, Tag & Attribute

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.w3.org/community/webed/wiki/HTML/Training/Tag_syntax">
    <img src="https://www.w3.org/community/webed/wiki/images/3/39/Elements.png" style="margin: 0.1em;" alt="HTML elements usually come in tag pairs" title="HTML elements" width="350">
    <img src="https://www.w3.org/community/webed/wiki/images/b/bc/Option.png" style="margin: 0.1em;" alt="An element can have attributes to refine its meaning" title="HTML elements" width="350">
  </a></div>
</div>



### Elements

#### Definition and Characteristics of Elements

+ The pieces themselves, i.e. a paragraph is an element, or a header is an element, even the body is an element

+ [Elements](/WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#identifying-html5-elements): the intangible parts of your Web page, described by the text in tags and rendered on the screen of whatever device you're looking at your Web page with

+ Tree structure:
  + parent element: an element wholely containing any given element (except for the outermost 'html' element)
  + child element:  the elements that a given element contains
  + siblings: children of a common parent

+ Borrow from SGML to provide an easy way for a computer to determine which parts are "MarkUp" and which parts are the content

+ [Sementic element](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#introduction-to-semantic-elements)
  + elemets that suggest the purpose of the content within the tags along with id and class attributes
  + E.g., `<p>` for paragraph; `<h1>` ~ `<h6>` for heading; `<img>` for image; `<blockquote>` to wrap a quote; `<em>` to emphasize a part of your content; 
  + `<i>` and `<b>` suggest nothing about the content
  + beneficial to both the developer and browser
    + convey much more information about your HTML document's content and structure
    + e.g., heading like `<h1>` or `<h2>` likely the start of a new sub-section or topic
    + useful for a developer who can understand the markup structure better
    + browser better differentiate different types of data which results in better display of content in different devices
    + Assistive technology: read content and convey information about the content depending on the semantic meaning
  + Only a few semantic elements such as `<mark>`, `<em>`, `<strong>` and `<code>` provide some kind of visual change to the document.

+ 'header' vs 'h1' - 'h6'
  + `<header>`: an area to add any introductory content about your page
  + `<h1>` to `<h6>`: headings; Headings communicate the organization of the content on the page.
  + the header can and frequently does contain headings `<h1>` to `<h6>`
  + Headings are extremely helpful as a navigation tool for assistive technology users.
  + Assistive technology often relies on the semantics of headings to understand your document's structure.
  + [Using h1-h6 to identify headings](https://www.w3.org/TR/WCAG20-TECHS/H42.html)
  + Assistive technology uses heading markup, `<h1>` to `<h6>` to identify headings in a document.
  + [W3C resource page about headings](https://www.w3.org/WAI/tutorials/page-structure/headings/)

+ 'header', 'footer' and 'nav' elements
  + Header and footer elements are for the parent element (section, article, division or body)
  + one header and footer for each section or article
  + Global header and footer elements
    + used site-wide at the top and bottom of the body of the Web page
    + typically contain logos, main heading, a search area and site-wide navigation and the footer will typically include authoring information, references and other links, copyright information etc.
    + the header of a Web page typically with a template file
  + having the nav element in header

+ 'article' and 'section' elements
  + article and section elements are nestable
  + section element is used to section a page

+ 'div' and 'span' elements
  + `<div>`:
    + used to define a division or a section of the document
    + not a semantic element, but commonly used when there isn't a better semantic assignment for it
    + a generic container that can hold a variety of elements such as paragraphs, images, links, tables, etc.
    + ablt to be used to group elements for styling purposes
    + assigning an id or class attribute to the div element and then apply styles which will affect all elements in the div container
    + a block level element (for a block of space)
  + `<span>`
    + To add styling to part of a sentence (inline)
    + Manipulate part of a sentence using JavaScript
    + an inline element (for within a line or phrase)
  + When no other HTML element is applicable, you can use `<span>` (and `<div>`) to add attributes such as class and id
  + `<div>` and `<span>` serve the same purpose but should be applied at different levels

+ Nesting one paragraph tag in another is not valid because the browser will consider them as two paragraphs one after the other.


<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.oreilly.com/library/view/learning-web-design/9780596527525/ch04.html">
    <img src="https://www.oreilly.com/library/view/learning-web-design/9780596527525/graphics/lwd3_0406.jpg" style="margin: 0.1em;" alt="An element consists of both the content and its markup." title="The parts of an (X)HTML element" width="400">
  </a></div>
</div>


#### [Document metadata](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Document_metadata)

Metadata contains information about the page. This includes information about styles, scripts and data to help software (search engines, browsers, etc.) use and render the page. Metadata for styles and scripts may be defined in the page or link to another file that has the information. 

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/base" title="The HTML <base> element specifies the base URL to use for all relative URLs contained within a document. There can be only one <base> element in a document."><code>&lt;base&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;base&gt;</code> element</strong> specifies the base URL to use for all relative URLs contained within a document. There can be only one <code>&lt;base&gt;</code> element in a document.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/head" title="The HTML <head> element contains machine-readable information (metadata) about the document, like its title, scripts, and style sheets."><code>&lt;head&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;head&gt;</code> element</strong> contains machine-readable information (<a class="glossaryLink" href="/en-US/docs/Glossary/metadata" title="metadata: Metadata is — in its very simplest definition — data that describes data. For example, an HTML document is data, but HTML can also contain metadata in its <head> element that describes the document — for example who wrote it, and its summary.">metadata</a>) about the document, like its <a href="/en-US/docs/Web/HTML/Element/title">title</a>, <a href="/en-US/docs/Web/HTML/Element/script">scripts</a>, and <a href="/en-US/docs/Web/HTML/Element/style">style sheets</a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/link" title="The HTML External Resource Link element (<link>) specifies relationships between the current document and an external resource. This element is most commonly used to link to stylesheets, but is also used to establish site icons (both &quot;favicon&quot; style icons and icons for the home screen and apps on mobile devices) among other things."><code>&lt;link&gt;</code></a></td>
   <td>The <strong>HTML External Resource Link element (<code>&lt;link&gt;</code>)</strong> specifies relationships between the current document and an external resource. This element is most commonly used to link to <a class="glossaryLink" href="/en-US/docs/Glossary/CSS" title="stylesheets: CSS (Cascading Style Sheets) is a declarative language that controls how webpages look in the browser.">stylesheets</a>, but is also used to establish site icons (both "favicon" style icons and icons for the home screen and apps on mobile devices) among other things.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/meta" title="The HTML <meta> element represents metadata that cannot be represented by other HTML meta-related elements, like <base>, <link>, <script>, <style> or <title>."><code>&lt;meta&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;meta&gt;</code> element</strong> represents <a class="glossaryLink" href="/en-US/docs/Glossary/Metadata" title="metadata: Metadata is — in its very simplest definition — data that describes data. For example, an HTML document is data, but HTML can also contain metadata in its <head> element that describes the document — for example who wrote it, and its summary.">metadata</a> that cannot be represented by other HTML meta-related elements, like <a href="/en-US/docs/Web/HTML/Element/base" title="The HTML <base> element specifies the base URL to use for all relative URLs contained within a document. There can be only one <base> element in a document."><code>&lt;base&gt;</code></a>, <a href="/en-US/docs/Web/HTML/Element/link" title="The HTML External Resource Link element (&amp;lt;link&amp;gt;) specifies relationships between the current document and an external resource. This element is most commonly used to link to stylesheets, but is also used to establish site icons (both &quot;favicon&quot; style icons and icons for the home screen and apps on mobile devices) among other things."><code>&lt;link&gt;</code></a>, <a href="/en-US/docs/Web/HTML/Element/script" title="The HTML <script> element is used to embed or reference executable code; this is typically used to embed or refer to JavaScript code."><code>&lt;script&gt;</code></a>, <a href="/en-US/docs/Web/HTML/Element/style" title="The HTML <style> element contains style information for a document, or part of a document."><code>&lt;style&gt;</code></a> or <a href="/en-US/docs/Web/HTML/Element/title" title="The HTML Title element (<title>) defines the document's title that is shown in a browser's title bar or a page's tab."><code>&lt;title&gt;</code></a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/style" title="The HTML <style> element contains style information for a document, or part of a document."><code>&lt;style&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;style&gt;</code> element</strong> contains style information for a document, or part of a document.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/title" title="The HTML Title element (<title>) defines the document's title that is shown in a browser's title bar or a page's tab."><code>&lt;title&gt;</code></a></td>
   <td>The <strong>HTML Title element</strong> (<strong><code>&lt;title&gt;</code></strong>) defines the document's title that is shown in a <a class="glossaryLink" href="/en-US/docs/Glossary/Browser" title="browser: A Web browser or browser is a program that retrieves and displays pages from&nbsp;the Web, and lets users access further pages through hyperlinks. A browser is the most familiar type of user agent.">browser</a>'s title bar or a page's tab.</td>
  </tr>
 </tbody>
</table>


#### [Sectioning Root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Sectioning_root)

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
 <tbody>
   <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/body" title="The HTML <body> Element represents the content of an HTML&nbsp;document. There can be only one <body> element in a document."><code>&lt;body&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;body&gt;</code> Element</strong> represents the content of an HTML&nbsp;document. There can be only one <code>&lt;body&gt;</code> element in a document.</td>
  </tr>
 </tbody>
</table>


#### [Content sectioning](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Content_sectioning)

Content sectioning elements allow you to organize the document content into logical pieces. Use the sectioning elements to create a broad outline for your page content, including header and footer navigation, and heading elements to identify sections of content.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/address" title="The HTML <address> element indicates that the enclosed HTML provides contact information for a person or people, or for an organization."><code>&lt;address&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;address&gt;</code> element</strong> indicates that the enclosed HTML provides contact information for a person or people, or for an organization.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/article" title="The HTML <article> element represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable"><code>&lt;article&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;article&gt;</code> element</strong> represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/aside" title="The HTML <aside> element represents a portion of a document whose content is only indirectly related to the document's main content."><code>&lt;aside&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;aside&gt;</code> element</strong> represents a portion of a document whose content is only indirectly related to the document's main content.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/footer" title="The HTML <footer> element represents a footer for its nearest sectioning content or sectioning root element. A footer typically contains information about the author of the section, copyright data or links to related documents."><code>&lt;footer&gt;</code></a></td>
   <td>The<strong> HTML <code>&lt;footer&gt;</code> element</strong> represents a footer for its nearest <a href="/en-US/docs/Web/Guide/HTML/Sections_and_Outlines_of_an_HTML5_document#Defining_sections">sectioning content</a> or <a href="/en-US/docs/Web/Guide/HTML/Sections_and_Outlines_of_an_HTML5_document#Sectioning_roots" title="Sections and Outlines of an HTML5 document#Sectioning root">sectioning root</a> element. A footer typically contains information about the author of the section, copyright data or links to related documents.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/header" title="The HTML <header> element represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements."><code>&lt;header&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;header&gt;</code> element</strong> represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/h1" title="REDIRECT Heading elements [en-US]"><code>&lt;h1&gt;</code></a>, <a href="/en-US/docs/Web/HTML/Element/h2" title="REDIRECT Heading elements [en-US]"><code>&lt;h2&gt;</code></a>, <a href="/en-US/docs/Web/HTML/Element/h3" title="REDIRECT Heading elements [en-US]"><code>&lt;h3&gt;</code></a>, <a href="/en-US/docs/Web/HTML/Element/h4" title="REDIRECT Heading elements [en-US]"><code>&lt;h4&gt;</code></a>, <a href="/en-US/docs/Web/HTML/Element/h5" title="REDIRECT Heading elements [en-US]"><code>&lt;h5&gt;</code></a>, <a href="/en-US/docs/Web/HTML/Element/h6" title="REDIRECT Heading elements [en-US]"><code>&lt;h6&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;h1&gt;</code>–<code>&lt;h6&gt;</code> elements</strong> represent six levels of section headings. <code>&lt;h1&gt;</code> is the highest section level and <code>&lt;h6&gt;</code> is the lowest.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/hgroup" title="The HTML <hgroup> element represents a multi-level heading for a section of a document. It groups a set of <h1>–<h6> elements."><code>&lt;hgroup&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;hgroup&gt;</code> element</strong> represents a multi-level heading for a section of a document. It groups a set of <code><a href="/en-US/docs/Web/HTML/Element/Heading_Elements">&lt;h1&gt;–&lt;h6&gt;</a></code> elements.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/main" title="The HTML <main> element represents the dominant content of the <body> of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application."><code>&lt;main&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;main&gt;</code> element</strong> represents the dominant content of the <a href="/en-US/docs/Web/HTML/Element/body" title="The HTML <body> Element represents the content of an HTML&nbsp;document. There can be only one <body> element in a document."><code>&lt;body&gt;</code></a> of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/nav" title="The HTML <nav> element represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes."><code>&lt;nav&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;nav&gt;</code> element</strong> represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/section" title="The HTML <section> element represents a standalone section — which doesn't have a more specific semantic element to represent it — contained within an HTML document."><code>&lt;section&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;section&gt;</code> element</strong> represents a standalone section — which doesn't have a more specific semantic element to represent it — contained within an HTML document.</td>
  </tr>
 </tbody>
</table>


#### [Text content](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Text_content)

Use HTML text content elements to organize blocks or sections of content placed between the opening `<body>` and closing `</body>` tags. Important for accessibility and SEO, these elements identify the purpose or structure of that content.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/blockquote" title="The HTML <blockquote> Element (or HTML Block Quotation Element) indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation (see Notes for how to change it). A URL for the source of the quotation may be given using the cite attribute, while a text representation of the source can be given using the <cite> element."><code>&lt;blockquote&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or <em>HTML Block Quotation Element</em>) indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation (see <a href="#Usage_notes" rel="internal">Notes</a> for how to change it). A URL for the source of the quotation may be given using the <strong>cite</strong> attribute, while a text representation of the source can be given using the <a href="/en-US/docs/Web/HTML/Element/cite" title="The HTML Citation element (<cite>) is used to describe a reference to a cited creative work, and must include the title of that work."><code>&lt;cite&gt;</code></a> element.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/dd" title="The&nbsp;HTML <dd> element provides the details about or the definition of the preceding term (<dt>) in a description list (<dl>)."><code>&lt;dd&gt;</code></a></td>
   <td>The&nbsp;<strong>HTML <code>&lt;dd&gt;</code> element</strong> provides the details about or the definition of the preceding term (<a href="/en-US/docs/Web/HTML/Element/dt" title="The HTML <dt> element specifies a term in a description or definition list, and as such must be used inside a <dl> element."><code>&lt;dt&gt;</code></a>) in a description list (<a href="/en-US/docs/Web/HTML/Element/dl" title="The HTML <dl> element represents a description list. The element encloses a list of groups of terms (specified using the <dt> element) and descriptions (provided by <dd> elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs)."><code>&lt;dl&gt;</code></a>).</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/dir" title="The obsolete HTML Directory element (<dir>) is used as a container for a directory of files and/or folders, potentially with styles and icons applied by the user agent."><code>&lt;dir&gt;</code></a></td>
   <td>The obsolete <strong>HTML Directory element</strong> (<strong><code>&lt;dir&gt;</code></strong>) is used as a container for a directory of files and/or folders, potentially with styles and icons applied by the <a class="glossaryLink" href="/en-US/docs/Glossary/user_agent" title="user agent: A user agent is a computer program representing a person, for example, a browser in a Web context.">user agent</a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/div" title="The HTML Content Division element (<div>) is the generic container for flow content. It has no effect on the content or layout until styled using CSS."><code>&lt;div&gt;</code></a></td>
   <td>The <strong>HTML Content Division element</strong> (<strong><code>&lt;div&gt;</code></strong>) is the generic container for flow content. It has no effect on the content or layout until styled using <a class="glossaryLink" href="/en-US/docs/Glossary/CSS" title="CSS: CSS (Cascading Style Sheets) is a declarative language that controls how webpages look in the browser.">CSS</a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/dl" title="The HTML <dl> element represents a description list. The element encloses a list of groups of terms (specified using the <dt> element) and descriptions (provided by <dd> elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs)."><code>&lt;dl&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;dl&gt;</code> </strong>element represents a description list. The element encloses a list of groups of terms (specified using the <a href="/en-US/docs/Web/HTML/Element/dt" title="The HTML <dt> element specifies a term in a description or definition list, and as such must be used inside a <dl> element."><code>&lt;dt&gt;</code></a> element) and descriptions (provided by <a href="/en-US/docs/Web/HTML/Element/dd" title="The&nbsp;HTML <dd> element provides the details about or the definition of the preceding term (<dt>) in a description list (<dl>)."><code>&lt;dd&gt;</code></a> elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/dt" title="The HTML <dt> element specifies a term in a description or definition list, and as such must be used inside a <dl> element."><code>&lt;dt&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;dt&gt;</code> element</strong> specifies a term in a description or definition list, and as such must be used inside a <a href="/en-US/docs/Web/HTML/Element/dl" title="The HTML <dl> element represents a description list. The element encloses a list of groups of terms (specified using the <dt> element) and descriptions (provided by <dd> elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs)."><code>&lt;dl&gt;</code></a> element.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/figcaption" title="The HTML <figcaption> or Figure Caption element represents a caption or legend describing the rest of the contents of its parent <figure> element."><code>&lt;figcaption&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;figcaption&gt;</code> or Figure Caption element</strong> represents a caption or legend describing the rest of the contents of its parent <a href="/en-US/docs/Web/HTML/Element/figure" title="The HTML <figure> (Figure With Optional Caption) element represents self-contained content, potentially with an optional caption, which is specified using the (<figcaption>) element."><code>&lt;figure&gt;</code></a> element.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/figure" title="The HTML <figure> (Figure With Optional Caption) element represents self-contained content, potentially with an optional caption, which is specified using the (<figcaption>) element."><code>&lt;figure&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;figure&gt;</code> (Figure With Optional Caption) element</strong> represents self-contained content, potentially with an optional caption, which is specified using the (<a href="/en-US/docs/Web/HTML/Element/figcaption" title="The HTML <figcaption> or Figure Caption element represents a caption or legend describing the rest of the contents of its parent <figure> element."><code>&lt;figcaption&gt;</code></a>) element.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/hr" title="The HTML <hr> element represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section."><code>&lt;hr&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;hr&gt;</code> element</strong> represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/li" title="The HTML <li> element is used to represent an item in a list."><code>&lt;li&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;li&gt;</code> element</strong> is used to represent an item in a list.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/main" title="The HTML <main> element represents the dominant content of the <body> of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application."><code>&lt;main&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;main&gt;</code> element</strong> represents the dominant content of the <a href="/en-US/docs/Web/HTML/Element/body" title="The HTML <body> Element represents the content of an HTML&nbsp;document. There can be only one <body> element in a document."><code>&lt;body&gt;</code></a> of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/ol" title="The HTML <ol> element represents an ordered list of items, typically rendered as a numbered list."><code>&lt;ol&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;ol&gt;</code> element</strong> represents an ordered list of items, typically rendered as a numbered list.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/p" title="The HTML <p> element represents a paragraph."><code>&lt;p&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;p&gt;</code> element</strong> represents a paragraph.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/pre" title="The HTML <pre> element represents preformatted text which is to be presented exactly as written in the HTML file."><code>&lt;pre&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;pre&gt;</code> element</strong> represents preformatted text which is to be presented exactly as written in the HTML file.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/ul" title="The HTML <ul> element represents an unordered list of items, typically rendered as a bulleted list."><code>&lt;ul&gt;</code></a></td>
   <td>The<strong> HTML <code>&lt;ul&gt;</code> element</strong> represents an unordered list of items, typically rendered as a bulleted list.</td>
  </tr>

 </tbody>
</table>


#### [Inline text semantic](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Inline_text_semantics)

Use the HTML inline text semantic to define the meaning, structure, or style of a word, line, or any arbitrary piece of text.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
 <tbody>
   <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/a" title="The HTML <a> element (or anchor element), along with it's href attribute, creates a hyperlink to other web pages, files, locations within the same page, email addresses, or any other URL."><code>&lt;a&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;a&gt;</code> element</strong> (or <em>anchor</em> element), along with it's <a href="#href">href</a> attribute, creates a hyperlink to other web pages, files, locations within the same page, email addresses, or any other URL.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/abbr" title="The HTML Abbreviation element (<abbr>) represents an abbreviation or acronym; the optional title attribute can provide an expansion or description for the abbreviation."><code>&lt;abbr&gt;</code></a></td>
   <td>The <strong>HTML Abbreviation element </strong>(<strong><code>&lt;abbr&gt;</code></strong>) represents an abbreviation or acronym; the optional <code><a href="/en-US/docs/Web/HTML/Global_attributes#attr-title">title</a></code> attribute can provide an expansion or description for the abbreviation.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/b" title="The HTML Bring Attention To element (<b>)&nbsp; is used to draw the reader's attention to the element's contents, which are not otherwise granted special importance."><code>&lt;b&gt;</code></a></td>
   <td>The <strong>HTML Bring Attention To element (<code>&lt;b&gt;</code>)</strong>&nbsp; is used to draw the reader's attention to the element's contents, which are not otherwise granted special importance.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/bdi" title="The HTML Bidirectional Isolate element (<bdi>)&nbsp; tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text."><code>&lt;bdi&gt;</code></a></td>
   <td>The HTML <strong>Bidirectional Isolate element</strong> (<strong><code>&lt;bdi&gt;</code></strong>)&nbsp; tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/bdo" title="The HTML Bidirectional Text Override element (<bdo>) overrides the current directionality of text, so that the text within is rendered in a different direction."><code>&lt;bdo&gt;</code></a></td>
   <td>The <strong>HTML Bidirectional Text Override element</strong> (<strong><code>&lt;bdo&gt;</code></strong>) overrides the current directionality of text, so that the text within is rendered in a different direction.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/br" title="The HTML <br> element produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant."><code>&lt;br&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;br&gt;</code> element</strong> produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/cite" title="The HTML Citation element (<cite>) is used to describe a reference to a cited creative work, and must include the title of that work."><code>&lt;cite&gt;</code></a></td>
   <td>The <strong>HTML Citation element</strong> (<strong><code>&lt;cite&gt;</code></strong>) is used to describe a reference to a cited creative work, and must include the title of that work.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/code" title="The HTML <code> element displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code."><code>&lt;code&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;code&gt;</code> element</strong> displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/data" title="The HTML <data> element links a given content with a machine-readable translation. If the content is time- or date-related, the <time> element must be used."><code>&lt;data&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;data&gt;</code> element</strong> links a given content with a machine-readable translation. If the content is time- or date-related, the <a href="/en-US/docs/Web/HTML/Element/time" title="The HTML <time> element represents a specific period in time."><code>&lt;time&gt;</code></a> element must be used.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/dfn" title="The HTML Definition element (<dfn>) is used to indicate the term being defined within the context of a definition phrase or sentence."><code>&lt;dfn&gt;</code></a></td>
   <td>The <strong>HTML Definition element</strong> (<strong><dfn>&lt;dfn&gt;</dfn></strong>) is used to indicate the term being defined within the context of a definition phrase or sentence.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/em" title="The HTML <em> element marks text that has stress emphasis. The <em> element can be nested, with each level of nesting indicating a greater degree of emphasis."><code>&lt;em&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;em&gt;</code> element</strong> marks text that has stress emphasis. The <code>&lt;em&gt;</code> element can be nested, with each level of nesting indicating a greater degree of emphasis.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/i" title="The HTML <i> element represents a range of text that is set off from the normal text for some reason. Some examples include technical terms, foreign language phrases, or fictional character thoughts. It is typically displayed in italic type."><code>&lt;i&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;i&gt;</code> element</strong> represents a range of text that is set off from the normal text for some reason. Some examples include technical terms, foreign language phrases, or fictional character thoughts. It is typically displayed in italic type.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/kbd" title="The HTML Keyboard Input element (<kbd>) represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device."><code>&lt;kbd&gt;</code></a></td>
   <td>The <strong>HTML Keyboard Input element</strong> (<strong><code>&lt;kbd&gt;</code></strong>) represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/mark" title="The HTML Mark Text element (<mark>) represents text which is marked or highlighted for reference or notation purposes, due to the marked passage's relevance or importance in the enclosing context."><code>&lt;mark&gt;</code></a></td>
   <td>The <strong>HTML Mark Text element</strong> (<strong><code>&lt;mark&gt;</code></strong>) represents text which is <strong>marked</strong> or <strong>highlighted</strong> for reference or notation purposes, due to the marked passage's relevance or importance in the enclosing context.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/q" title="The HTML <q> element  indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. "><code>&lt;q&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;q&gt;</code> element </strong> indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. </td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/rb" title="The HTML Ruby Base (<rb>) element is used to delimit the base text component of a&nbsp; <ruby> annotation, i.e. the text that is being annotated."><code>&lt;rb&gt;</code></a></td>
   <td>The <strong>HTML Ruby Base (<code>&lt;rb&gt;</code>) element</strong> is used to delimit the base text component of a&nbsp; <a href="/en-US/docs/Web/HTML/Element/ruby" title="The HTML <ruby> element represents a ruby annotation. Ruby annotations are for showing pronunciation of East Asian characters."><code>&lt;ruby&gt;</code></a> annotation, i.e. the text that is being annotated.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/rp" title="The HTML Ruby Fallback Parenthesis (<rp>) element is used to provide fall-back parentheses for browsers that do not support display of ruby annotations using the <ruby> element."><code>&lt;rp&gt;</code></a></td>
   <td>The <strong>HTML Ruby Fallback Parenthesis (<code>&lt;rp&gt;</code>) element</strong> is used to provide fall-back parentheses for browsers that do not support display of ruby annotations using the <a href="/en-US/docs/Web/HTML/Element/ruby" title="The HTML <ruby> element represents a ruby annotation. Ruby annotations are for showing pronunciation of East Asian characters."><code>&lt;ruby&gt;</code></a> element.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/rt" title="The HTML Ruby Text (<rt>) element specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The <rt> element must always be contained within a <ruby> element."><code>&lt;rt&gt;</code></a></td>
   <td>The <strong>HTML Ruby Text (<code>&lt;rt&gt;</code>) element</strong> specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The <code>&lt;rt&gt;</code> element must always be contained within a <a href="/en-US/docs/Web/HTML/Element/ruby" title="The HTML <ruby> element represents a ruby annotation. Ruby annotations are for showing pronunciation of East Asian characters."><code>&lt;ruby&gt;</code></a> element.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/rtc" title="The HTML Ruby Text Container (<rtc>) element embraces semantic annotations of characters presented in a ruby of <rb> elements used inside of <ruby> element. <rb> elements can have both pronunciation (<rt>) and semantic (<rtc>) annotations."><code>&lt;rtc&gt;</code></a></td>
   <td>The <strong>HTML Ruby Text Container (<code>&lt;rtc&gt;</code>) element</strong> embraces semantic annotations of characters presented in a ruby of <a href="/en-US/docs/Web/HTML/Element/rb" title="The HTML Ruby Base (<rb>) element is used to delimit the base text component of a&nbsp; <ruby> annotation, i.e. the text that is being annotated."><code>&lt;rb&gt;</code></a> elements used inside of <a href="/en-US/docs/Web/HTML/Element/ruby" title="The HTML <ruby> element represents a ruby annotation. Ruby annotations are for showing pronunciation of East Asian characters."><code>&lt;ruby&gt;</code></a> element. <a href="/en-US/docs/Web/HTML/Element/rb" title="The HTML Ruby Base (<rb>) element is used to delimit the base text component of a&nbsp; <ruby> annotation, i.e. the text that is being annotated."><code>&lt;rb&gt;</code></a> elements can have both pronunciation (<a href="/en-US/docs/Web/HTML/Element/rt" title="The HTML Ruby Text (<rt>) element specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The <rt> element must always be contained within a <ruby> element."><code>&lt;rt&gt;</code></a>) and semantic (<a href="/en-US/docs/Web/HTML/Element/rtc" title="The HTML Ruby Text Container (<rtc>) element embraces semantic annotations of characters presented in a ruby of <rb> elements used inside of <ruby> element. <rb> elements can have both pronunciation (<rt>) and semantic (<rtc>) annotations."><code>&lt;rtc&gt;</code></a>) annotations.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/ruby" title="The HTML <ruby> element represents a ruby annotation. Ruby annotations are for showing pronunciation of East Asian characters."><code>&lt;ruby&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;ruby&gt;</code> element</strong> represents a ruby annotation. Ruby annotations are for showing pronunciation of East Asian characters.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/s" title="The HTML <s> element renders text with a strikethrough, or a line through it. Use the <s> element to represent things that are no longer relevant or no longer accurate. However, <s> is not appropriate when indicating document edits; for that, use the <del> and <ins> elements, as appropriate."><code>&lt;s&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;s&gt;</code> element</strong> renders text with a strikethrough, or a line through it. Use the <code>&lt;s&gt;</code> element to represent things that are no longer relevant or no longer accurate. However, <code>&lt;s&gt;</code> is not appropriate when indicating document edits; for that, use the <a href="/en-US/docs/Web/HTML/Element/del" title="The HTML <del> element represents a range of text that has been deleted from a document."><code>&lt;del&gt;</code></a> and <a href="/en-US/docs/Web/HTML/Element/ins" title="The HTML <ins> element represents a range of text that has been added to a document."><code>&lt;ins&gt;</code></a> elements, as appropriate.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/samp" title="The HTML Sample Element (<samp>) is used to enclose inline text which represents sample (or quoted) output from a computer program."><code>&lt;samp&gt;</code></a></td>
   <td>The <strong>HTML Sample Element</strong> (<strong><code>&lt;samp&gt;</code></strong>) is used to enclose inline text which represents sample (or quoted) output from a computer program.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/small" title="The HTML <small> element makes the text font size one size smaller (for example, from large to medium, or from small to x-small) down to the browser's minimum font size.&nbsp; In HTML5, this element is repurposed to represent side-comments and small print, including copyright and legal text, independent of its styled presentation."><code>&lt;small&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;small&gt;</code></strong> <strong>element </strong>makes the text <em>font size</em> one size smaller (for example, from large to medium, or from small to x-small) down to the browser's minimum font size.&nbsp; In HTML5, this element is repurposed to represent side-comments and small print, including copyright and legal text, independent of its styled presentation.</td>
  </tr>
  <tr>

   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/span" title="The HTML <span> element is a generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the class or id attributes), or because they share attribute values, such as lang."><code>&lt;span&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;span&gt;</code> element</strong> is a generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the <code><a href="/en-US/docs/Web/HTML/Global_attributes#attr-class">class</a></code> or <code><a href="/en-US/docs/Web/HTML/Global_attributes#attr-id">id</a></code> attributes), or because they share attribute values, such as <code><a href="/en-US/docs/Web/HTML/Global_attributes#attr-lang">lang</a></code>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/strong" title="The HTML Strong Importance Element (<strong>) indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type."><code>&lt;strong&gt;</code></a></td>
   <td>The HTML <strong>Strong Importance Element</strong> (<strong><code>&lt;strong&gt;</code></strong>) indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/sub" title="The HTML Subscript element (<sub>) specifies inline text which should be displayed as subscript for solely typographical reasons."><code>&lt;sub&gt;</code></a></td>
   <td>The HTML <strong>Subscript element</strong> (<strong><code>&lt;sub&gt;</code></strong>) specifies inline text which should be displayed as subscript for solely typographical reasons.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/sup" title="The HTML Superscript element (<sup>) specifies inline text which is to be displayed as superscript for solely typographical reasons."><code>&lt;sup&gt;</code></a></td>
   <td>The <strong>HTML Superscript element</strong> (<strong><code>&lt;sup&gt;</code></strong>) specifies inline text which is to be displayed as superscript for solely typographical reasons.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/time" title="The HTML <time> element represents a specific period in time."><code>&lt;time&gt;</code></a></td>
   <td>The HTML <strong><code>&lt;time&gt;</code> element</strong> represents a specific period in time.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/tt" title="The obsolete HTML Teletype Text element (<tt>) creates inline text which is presented using the user agent's default monospace font face."><code>&lt;tt&gt;</code></a></td>
   <td>The obsolete <strong>HTML Teletype Text element</strong> (<strong><code>&lt;tt&gt;</code></strong>) creates inline text which is presented using the <a class="glossaryLink" href="/en-US/docs/Glossary/user_agent" title="user agent's: A user agent is a computer program representing a person, for example, a browser in a Web context.">user agent's</a> default monospace font face.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/u" title="The HTML Unarticulated Annotation Element (<u>) represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation."><code>&lt;u&gt;</code></a></td>
   <td>The HTML <strong>Unarticulated Annotation Element</strong> (<strong><code>&lt;u&gt;</code></strong>) represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/var" title="The HTML Variable element (<var>) represents the name of a variable in a mathematical expression or a programming context."><code>&lt;var&gt;</code></a></td>
   <td>The HTML <strong>Variable element</strong> (<strong><code>&lt;var&gt;</code></strong>) represents the name of a variable in a mathematical expression or a programming context.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/wbr" title="The HTML <wbr> element represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location."><code>&lt;wbr&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;wbr&gt;</code> element</strong> represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.</td>
  </tr>
 </tbody>
</table>


#### [Image and multimedia](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Image_and_multimedia)

HTML supports various multimedia resources such as images, audio, and video.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
 <tbody>
   <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/area" title="The HTML <area> element defines a hot-spot region on an image, and optionally associates it with a hypertext link. This element is used only within a <map> element."><code>&lt;area&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;area&gt;</code> element</strong> defines a hot-spot region on an image, and optionally associates it with a <a class="glossaryLink" href="/en-US/docs/Glossary/Hyperlink" title="hypertext link: Hyperlinks connect webpages or data items to one another. In HTML, <a> elements define hyperlinks from a spot on a webpage (like a text string or image) to another spot on some other webpage (or even on the same page).">hypertext link</a>. This element is used only within a <a href="/en-US/docs/Web/HTML/Element/map" title="The HTML <map> element is used with <area> elements to define an image map (a clickable link area)."><code>&lt;map&gt;</code></a> element.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/audio" title="The HTML <audio> element is used to embed sound content in documents. It may contain one or more audio sources, represented using the src attribute or the <source> element:&nbsp;the browser will choose the most suitable one. It can also be the destination for streamed media, using a MediaStream."><code>&lt;audio&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;audio&gt;</code> element</strong> is used to embed sound content in documents. It may contain one or more audio sources, represented using the <code>src</code> attribute or the <a href="/en-US/docs/Web/HTML/Element/source" title="The HTML <source> element specifies multiple media resources for the <picture>, the <audio> element, or the <video> element."><code>&lt;source&gt;</code></a> element:&nbsp;the browser will choose the most suitable one. It can also be the destination for streamed media, using a <a href="/en-US/docs/Web/API/MediaStream" title="The MediaStream interface represents a stream of media content. A stream consists of several tracks such as&nbsp;video or audio tracks. Each track is specified as an instance of MediaStreamTrack."><code>MediaStream</code></a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/img" title="The HTML <img> element embeds an image into the document. It is a replaced element."><code>&lt;img&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;img&gt;</code> element</strong> embeds an image into the document. It is a <a href="/en-US/docs/Web/CSS/Replaced_element">replaced element</a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/map" title="The HTML <map> element is used with <area> elements to define an image map (a clickable link area)."><code>&lt;map&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;map&gt;</code> element</strong> is used with <a href="/en-US/docs/Web/HTML/Element/area" title="The HTML <area> element defines a hot-spot region on an image, and optionally associates it with a hypertext link. This element is used only within a <map> element."><code>&lt;area&gt;</code></a> elements to define an image map (a clickable link area).</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/track" title="The HTML <track> element is used as a child of the media elements <audio> and <video>. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in WebVTT format (.vtt files) — Web Video Text Tracks or&nbsp;Timed Text Markup Language (TTML)."><code>&lt;track&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;track&gt;</code> element</strong> is used as a child of the media elements <a href="/en-US/docs/Web/HTML/Element/audio" title="The HTML <audio> element is used to embed sound content in documents. It may contain one or more audio sources, represented using the src attribute or the <source> element:&nbsp;the browser will choose the most suitable one. It can also be the destination for streamed media, using a MediaStream."><code>&lt;audio&gt;</code></a> and <a href="/en-US/docs/Web/HTML/Element/video" title="The HTML Video element (<video>) embeds a media player which supports video playback into the document."><code>&lt;video&gt;</code></a>. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in <a href="/en-US/docs/Web/API/Web_Video_Text_Tracks_Format">WebVTT format</a> (<code>.vtt</code> files) — Web Video Text Tracks or&nbsp;<a class="external external-icon" href="https://w3c.github.io/ttml2/index.html" rel="noopener">Timed Text Markup Language (TTML).</a></td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/video" title="The HTML Video element (<video>) embeds a media player which supports video playback into the document."><code>&lt;video&gt;</code></a></td>
   <td>The <strong>HTML Video element</strong> (<strong><code>&lt;video&gt;</code></strong>) embeds a media player which supports video playback into the document.</td>
  </tr>
 </tbody>
</table>


#### [Embedded content](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Embedded_content)

In addition to regular multimedia content, HTML can include a variety of other content, even if it's not always easy to interact with.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/applet" title="The obsolete HTML Applet Element (<applet>) embeds a Java applet into the document; this element has been deprecated in favor of <object>."><code>&lt;applet&gt;</code></a></td>
   <td>The obsolete <strong>HTML Applet Element</strong> (<strong><code>&lt;applet&gt;</code></strong>) embeds a Java applet into the document; this element has been deprecated in favor of <a href="/en-US/docs/Web/HTML/Element/object" title="The HTML <object> element represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin."><code>&lt;object&gt;</code></a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/embed" title="The HTML <embed> element embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in."><code>&lt;embed&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;embed&gt;</code> element</strong> embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/iframe" title="The HTML Inline Frame element (<iframe>) represents a nested browsing context, embedding another HTML page into the current one."><code>&lt;iframe&gt;</code></a></td>
   <td>The <strong>HTML Inline Frame element (<code>&lt;iframe&gt;</code>)</strong> represents a nested <a class="glossaryLink" href="/en-US/docs/Glossary/browsing_context" title="browsing context: A browsing context is the environment in which a browser displays a Document (normally a tab nowadays, but possibly also a window or a frame within a page).">browsing context</a>, embedding another HTML page into the current one.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/noembed" title="The <noembed> element is an obsolete, non-standard way to provide alternative, or &quot;fallback&quot;, content for browsers that do not support the <embed> element or do not support the type of embedded content an author wishes to use."><code>&lt;noembed&gt;</code></a></td>
   <td>The <code><strong>&lt;noembed&gt;</strong></code> element is an obsolete, non-standard way to provide alternative, or "fallback", content for browsers that do not support the <a href="/en-US/docs/Web/HTML/Element/embed" title="The HTML <embed> element embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in."><code>&lt;embed&gt;</code></a> element or do not support the type of <a href="/en-US/docs/Web/Guide/HTML/Content_categories#Embedded_content">embedded content</a> an author wishes to use.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/object" title="The HTML <object> element represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin."><code>&lt;object&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;object&gt;</code> element</strong> represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/param" title="The HTML <param> element defines parameters for an <object> element."><code>&lt;param&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;param&gt;</code> element</strong> defines parameters for an <a href="/en-US/docs/Web/HTML/Element/object" title="The HTML <object> element represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin."><code>&lt;object&gt;</code></a> element.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/picture" title="The HTML <picture> element contains zero or more <source> elements and one <img> element to provide versions of an image for different display/device scenarios."><code>&lt;picture&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;picture&gt;</code> element</strong> contains zero or more <a href="/en-US/docs/Web/HTML/Element/source" title="The HTML <source> element specifies multiple media resources for the <picture>, the <audio> element, or the <video> element."><code>&lt;source&gt;</code></a> elements and one <a href="/en-US/docs/Web/HTML/Element/img" title="The HTML <img> element embeds an image into the document. It is a replaced element."><code>&lt;img&gt;</code></a> element to provide versions of an image for different display/device scenarios.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/source" title="The HTML <source> element specifies multiple media resources for the <picture>, the <audio> element, or the <video> element."><code>&lt;source&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;source&gt;</code> element</strong> specifies multiple media resources for the <a href="/en-US/docs/Web/HTML/Element/picture" title="The HTML <picture> element contains zero or more <source> elements and one <img> element to provide versions of an image for different display/device scenarios."><code>&lt;picture&gt;</code></a>, the <a href="/en-US/docs/Web/HTML/Element/audio" title="The HTML <audio> element is used to embed sound content in documents. It may contain one or more audio sources, represented using the src attribute or the <source> element:&nbsp;the browser will choose the most suitable one. It can also be the destination for streamed media, using a MediaStream."><code>&lt;audio&gt;</code></a> element, or the <a href="/en-US/docs/Web/HTML/Element/video" title="The HTML Video element (<video>) embeds a media player which supports video playback into the document."><code>&lt;video&gt;</code></a> element.</td>
  </tr>
 </tbody>
</table>


#### [Scripting](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Scripting)

In order to create dynamic content and Web applications, HTML supports the use of scripting languages, most prominently JavaScript. Certain elements support this capability.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/canvas" title="Use the HTML <canvas> element with either the canvas scripting API or the WebGL API to draw graphics and animations."><code>&lt;canvas&gt;</code></a></td>
   <td>Use the <strong>HTML <code>&lt;canvas&gt;</code> element</strong> with either the <a href="/en-US/docs/Web/API/Canvas_API">canvas scripting API</a> or the <a href="/en-US/docs/Web/API/WebGL_API">WebGL API</a> to draw graphics and animations.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/noscript" title="The HTML <noscript> element defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser."><code>&lt;noscript&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;noscript&gt;</code> element</strong> defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/script" title="The HTML <script> element is used to embed or reference executable code; this is typically used to embed or refer to JavaScript code."><code>&lt;script&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;script&gt;</code> element</strong> is used to embed or reference executable code; this is typically used to embed or refer to JavaScript code.</td>
  </tr>
 </tbody>
</table>


#### [Demarcating edits](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Demarcating_edits)

These elements let you provide indications that specific parts of the text have been altered.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/del" title="The HTML <del> element represents a range of text that has been deleted from a document."><code>&lt;del&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;del&gt;</code> element</strong> represents a range of text that has been deleted from a document.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/ins" title="The HTML <ins> element represents a range of text that has been added to a document."><code>&lt;ins&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;ins&gt;</code> element</strong> represents a range of text that has been added to a document.</td>
  </tr>
 </tbody>
</table>


#### [Table content](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Table_content)

The elements here are used to create and handle tabular data.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
 </thead>
 <tbody>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/caption" title="The HTML Table Caption element (<caption>) specifies the caption (or title) of a table, and if used is always the first child of a <table>."><code>&lt;caption&gt;</code></a></td>
   <td>The <strong>HTML Table Caption element</strong> (<strong><code>&lt;caption&gt;</code></strong>) specifies the caption (or title) of a table, and if used is <em>always</em> the first child of a <a href="/en-US/docs/Web/HTML/Element/table" title="The HTML <table> element represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data."><code>&lt;table&gt;</code></a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/col" title="The HTML <col> element defines a column within a table and is used for defining common semantics on all common cells. It is generally found within a <colgroup> element."><code>&lt;col&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;col&gt;</code> element</strong> defines a column within a table and is used for defining common semantics on all common cells. It is generally found within a <a href="/en-US/docs/Web/HTML/Element/colgroup" title="The HTML <colgroup> element defines a group of columns within a table."><code>&lt;colgroup&gt;</code></a> element.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/colgroup" title="The HTML <colgroup> element defines a group of columns within a table."><code>&lt;colgroup&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;colgroup&gt;</code> element</strong> defines a group of columns within a table.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/table" title="The HTML <table> element represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data."><code>&lt;table&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;table&gt;</code> element</strong> represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/tbody" title="The HTML Table Body element (<tbody>) encapsulates a set of table rows (<tr> elements), indicating that they comprise the body of the table (<table>)."><code>&lt;tbody&gt;</code></a></td>
   <td>The <strong>HTML Table Body element</strong> (<strong><code>&lt;tbody&gt;</code></strong>) encapsulates a set of table rows (<a href="/en-US/docs/Web/HTML/Element/tr" title="The HTML <tr> element defines a row of cells in a table. The row's cells can then be established using a mix of <td> (data cell) and <th> (header cell) elements.The HTML <tr> element specifies that the markup contained inside the <tr> block comprises one row of a table, inside which the <th> and <td> elements create header and data cells, respectively, within the row."><code>&lt;tr&gt;</code></a> elements), indicating that they comprise the body of the table (<a href="/en-US/docs/Web/HTML/Element/table" title="The HTML <table> element represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data."><code>&lt;table&gt;</code></a>).</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/td" title="The HTML <td> element defines a cell of a table that contains data. It participates in the table model."><code>&lt;td&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;td&gt;</code> element</strong> defines a cell of a table that contains data. It participates in the <em>table model</em>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/tfoot" title="The HTML <tfoot> element defines a set of rows summarizing the columns of the table."><code>&lt;tfoot&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;tfoot&gt;</code> element</strong> defines a set of rows summarizing the columns of the table.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/th" title="The HTML <th> element defines a cell as header of a group of table cells. The exact nature of this group is defined by the scope and headers attributes."><code>&lt;th&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;th&gt;</code> element</strong> defines a cell as header of a group of table cells. The exact nature of this group is defined by the <code><a href="/en-US/docs/Web/HTML/Element/th#attr-scope">scope</a></code> and <code><a href="/en-US/docs/Web/HTML/Element/th#attr-headers">headers</a></code> attributes.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/thead" title="The HTML <thead> element defines a set of rows defining the head of the columns of the table."><code>&lt;thead&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;thead&gt;</code> element</strong> defines a set of rows defining the head of the columns of the table.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/tr" title="The HTML <tr> element defines a row of cells in a table. The row's cells can then be established using a mix of <td> (data cell) and <th> (header cell) elements.The HTML <tr> element specifies that the markup contained inside the <tr> block comprises one row of a table, inside which the <th> and <td> elements create header and data cells, respectively, within the row."><code>&lt;tr&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;tr&gt;</code> element</strong> defines a row of cells in a table. The row's cells can then be established using a mix of <a href="/en-US/docs/Web/HTML/Element/td" title="The HTML <td> element defines a cell of a table that contains data. It participates in the table model."><code>&lt;td&gt;</code></a> (data cell) and <a href="/en-US/docs/Web/HTML/Element/th" title="The HTML <th> element defines a cell as header of a group of table cells. The exact nature of this group is defined by the scope and headers attributes."><code>&lt;th&gt;</code></a> (header cell) elements.The HTML <strong><code>&lt;tr&gt;</code></strong> element specifies that the markup contained inside the <code>&lt;tr&gt;</code> block comprises one row of a table, inside which the <a href="/en-US/docs/Web/HTML/Element/th" title="The HTML <th> element defines a cell as header of a group of table cells. The exact nature of this group is defined by the scope and headers attributes."><code>&lt;th&gt;</code></a> and <a href="/en-US/docs/Web/HTML/Element/td" title="The HTML <td> element defines a cell of a table that contains data. It participates in the table model."><code>&lt;td&gt;</code></a> elements create header and data cells, respectively, within the row.</td>
  </tr>
 </tbody>
</table>


#### [Forms](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Forms)

HTML provides a number of elements which can be used together to create forms which the user can fill out and submit to the Web site or application. There's a great deal of further information about this available in the HTML [forms guide](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms).

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr> </thead>
 <tbody>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/button" title="The HTML <button> element represents a clickable button, which can be used in forms or anywhere in a document that needs simple, standard button functionality."><code>&lt;button&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;button&gt;</code> element</strong> represents a clickable button, which can be used in <a href="/en-US/docs/Learn/HTML/Forms">forms</a> or anywhere in a document that needs simple, standard button functionality.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/datalist" title="The HTML <datalist> element contains a set of <option> elements that represent the values available for other controls."><code>&lt;datalist&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;datalist&gt;</code> element</strong> contains a set of <a href="/en-US/docs/Web/HTML/Element/option" title="The HTML <option> element is used to define an item contained in a <select>, an <optgroup>, or a <datalist>&nbsp;element. As such,&nbsp;<option>&nbsp;can represent menu items in popups and other lists of items in an HTML document."><code>&lt;option&gt;</code></a> elements that represent the values available for other controls.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/fieldset" title="The HTML <fieldset> element is used to group several controls as well as labels (<label>) within a web form."><code>&lt;fieldset&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;fieldset&gt;</code> element</strong> is used to group several controls as well as labels (<a href="/en-US/docs/Web/HTML/Element/label" title="The HTML <label> element represents a caption for an item in a user interface."><code>&lt;label&gt;</code></a>) within a web form.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/form" title="The HTML <form> element represents a document section that contains interactive controls for submitting information to a web server."><code>&lt;form&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;form&gt;</code> element</strong> represents a document section that contains interactive controls for submitting information to a web server.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/input" title="The HTML <input> element is used to create interactive controls for web-based forms in order to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent."><code>&lt;input&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;input&gt;</code> element</strong> is used to create interactive controls for web-based forms in order to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and <a class="glossaryLink" href="/en-US/docs/Glossary/user_agent" title="user agent: A user agent is a computer program representing a person, for example, a browser in a Web context.">user agent</a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/label" title="The HTML <label> element represents a caption for an item in a user interface."><code>&lt;label&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;label&gt;</code> element</strong> represents a caption for an item in a user interface.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/legend" title="The HTML <legend> element represents a caption for the content of its parent <fieldset>."><code>&lt;legend&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;legend&gt;</code> element</strong> represents a caption for the content of its parent <a href="/en-US/docs/Web/HTML/Element/fieldset" title="The HTML <fieldset> element is used to group several controls as well as labels (<label>) within a web form."><code>&lt;fieldset&gt;</code></a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/meter" title="The HTML <meter> element represents either a scalar value within a known range or a fractional value."><code>&lt;meter&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;meter&gt;</code> element</strong> represents either a scalar value within a known range or a fractional value.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/optgroup" title="The HTML <optgroup> element creates a grouping of options within a <select> element."><code>&lt;optgroup&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;optgroup&gt;</code> element</strong> creates a grouping of options within a <a href="/en-US/docs/Web/HTML/Element/select" title="The HTML <select> element represents a control that provides a menu of options"><code>&lt;select&gt;</code></a> element.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/option" title="The HTML <option> element is used to define an item contained in a <select>, an <optgroup>, or a <datalist>&nbsp;element. As such,&nbsp;<option>&nbsp;can represent menu items in popups and other lists of items in an HTML document."><code>&lt;option&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;option&gt;</code> element</strong> is used to define an item contained in a <a href="/en-US/docs/Web/HTML/Element/select" title="The HTML <select> element represents a control that provides a menu of options"><code>&lt;select&gt;</code></a>, an <a href="/en-US/docs/Web/HTML/Element/optgroup" title="The HTML <optgroup> element creates a grouping of options within a <select> element."><code>&lt;optgroup&gt;</code></a>, or a <a href="/en-US/docs/Web/HTML/Element/datalist" title="The HTML &amp;lt;datalist&amp;gt; element contains a set of {{HTMLElement(&quot;option&quot;)}} elements that represent the values available for other controls."><code>&lt;datalist&gt;</code></a>&nbsp;element. As such,&nbsp;<code>&lt;option&gt;</code>&nbsp;can represent menu items in popups and other lists of items in an HTML document.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/output" title="The HTML Output element (<output>) is a container element into which a site or app can inject the results of a calculation or the outcome of a user action."><code>&lt;output&gt;</code></a></td>
   <td>The <strong>HTML Output element</strong> (<strong><code>&lt;output&gt;</code></strong>) is a container element into which a site or app can inject the results of a calculation or the outcome of a user action.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/progress" title="The HTML <progress> element displays an indicator showing the completion progress of a task, typically displayed as a progress bar."><code>&lt;progress&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;progress&gt;</code> element</strong> displays an indicator showing the completion progress of a task, typically displayed as a progress bar.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/select" title="The HTML <select> element represents a control that provides a menu of options"><code>&lt;select&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;select&gt;</code> element</strong> represents a control that provides a menu of options</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/textarea" title="The HTML <textarea> element represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example a comment on a review or feedback form."><code>&lt;textarea&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;textarea&gt;</code> element</strong> represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example a comment on a review or feedback form.</td>
  </tr>
 </tbody>
</table>


#### [Interactive element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Interactive_elements)

HTML offers a selection of elements which help to create interactive user interface objects.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/details" title="The HTML Details Element (<details>) creates a disclosure widget in which information is visible only when the widget is toggled into an &quot;open&quot; state."><code>&lt;details&gt;</code></a></td>
   <td>The <strong>HTML Details Element (<code>&lt;details&gt;</code>)</strong> creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/dialog" title="The HTML <dialog> element represents a dialog box or other interactive component, such as an inspector or window."><code>&lt;dialog&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;dialog&gt;</code> element</strong> represents a dialog box or other interactive component, such as an inspector or window.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/menu" title="The HTML <menu> element represents a group of commands that a user can perform or activate. This includes both list menus, which might appear across the top of a screen, as well as context menus, such as those that might appear underneath a button after it has been clicked."><code>&lt;menu&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;menu&gt;</code> element</strong> represents a group of commands that a user can perform or activate. This includes both list menus, which might appear across the top of a screen, as well as context menus, such as those that might appear underneath a button after it has been clicked.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/menuitem" title="The HTML <menuitem> element represents a command that a user is able to invoke through a popup menu. This includes context menus, as well as menus that might be attached to a menu button."><code>&lt;menuitem&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;menuitem&gt;</code> element</strong> represents a command that a user is able to invoke through a popup menu. This includes context menus, as well as menus that might be attached to a menu button.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/summary" title="The HTML Disclosure Summary element (<summary>) element specifies a summary, caption, or legend for a <details> element's disclosure box."><code>&lt;summary&gt;</code></a></td>
   <td>The <strong>HTML Disclosure Summary element</strong> (<strong><code>&lt;summary&gt;</code></strong>) element specifies a summary, caption, or legend for a <a href="/en-US/docs/Web/HTML/Element/details" title="The HTML Details Element (&amp;lt;details&amp;gt;) creates a disclosure widget in which information is visible only when the widget is toggled into an &quot;open&quot; state."><code>&lt;details&gt;</code></a> element's disclosure box.</td>
  </tr>
 </tbody>
</table>


#### [Web Component](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Web_Components)

Web Components is an HTML-related technology which makes it possible to, essentially, create and use custom elements as if it were regular HTML. In addition, you can create custom versions of standard HTML elements.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/content" title="The HTML <content> element—an obsolete part of the Web Components suite of technologies—was used inside of Shadow DOM as an insertion point, and wasn't meant to be used in ordinary HTML."><code>&lt;content&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;content&gt;</code> element</strong>—an obsolete part of the <a href="/en-US/docs/Web/Web_Components">Web Components</a> suite of technologies—was used inside of <a href="/en-US/docs/Web/Web_Components/Shadow_DOM">Shadow DOM</a> as an <a class="glossaryLink new" href="/en-US/docs/Glossary/insertion_point" rel="nofollow" title="The definition of that term (insertion point) has not been written yet; please consider contributing it!">insertion point</a>, and wasn't meant to be used in ordinary HTML.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/element" title="The obsolete HTML <element> element was part of the Web Components specification; it was intended to be used to define new custom DOM elements."><code>&lt;element&gt;</code></a></td>
   <td>The obsolete <strong>HTML <code>&lt;element&gt;</code> element</strong> was part of the <a href="/en-US/docs/Web/Web_Components">Web Components</a> specification; it was intended to be used to define new custom DOM elements.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/shadow" title="The HTML <shadow> element—an obsolete part of the Web Components technology suite—was intended to be used as a shadow DOM insertion point."><code>&lt;shadow&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;shadow&gt;</code> element</strong>—an obsolete part of the <a href="/en-US/docs/Web/Web_Components">Web Components</a> technology suite—was intended to be used as a shadow DOM <a class="glossaryLink new" href="/en-US/docs/Glossary/insertion_point" rel="nofollow" title="The definition of that term (insertion point) has not been written yet; please consider contributing it!">insertion point</a>.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/slot" title="The HTML <slot> element—part of the Web Components technology suite—is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together."><code>&lt;slot&gt;</code></a></td>
   <td>The <strong>HTML <code>&lt;slot&gt;</code> element</strong>—part of the <a href="/en-US/docs/Web/Web_Components">Web Components</a> technology suite—is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.</td>
  </tr>
  <tr>
   <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/template" title="The HTML Content Template (<template>) element is a mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript."><code>&lt;template&gt;</code></a></td>
   <td>The <strong>HTML Content Template (<code>&lt;template&gt;</code>) element</strong> is a mechanism for holding <a class="glossaryLink" href="/en-US/docs/Glossary/HTML" title="HTML: HTML (HyperText Markup Language) is a descriptive language that specifies webpage structure.">HTML</a> that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.</td>
  </tr>
 </tbody>
</table>



#### List of Typical Semantic Elements


<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
 <thead>
  <tr style="border-bottom: double black;">
   <th style="background-color: #3d64ff; color: #ffffff; width: 05%">Element</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
   <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Link</th>
  </tr>
 </thead>
 <tbody>
  <tr>
    <td><code>&lt;header&gt;</code></td>
    <td>Introduction for the whole page or individual sections, article, nav, aside elements. Typically contains site name, logo, navigation. Does not have to be at the beginning of page.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#header-vs-h1---h6">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a></td>
  </tr>
  <tr>
    <td><code>&lt;footer&gt;</code></td>
    <td>Includes typical footer information like authoring, copyrights, contact information and a footer menu.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#new-html5-semantic-elements">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a></td>
  </tr>
  <tr>
    <td><code>&lt;nav&gt;</code></td>
    <td>Navigation links for the document. A page can have more than one &lt;nav&gt; element like table of contents, horizontal navigation in header and footer navigation.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#header-vs-h1---h6">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a></td>
  </tr>
  <tr>
    <td><code>&lt;section&gt;</code></td>
    <td>Defines sections in the document such as chapters, headers, etc. Typically used on content that cannot make sense on its own.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#article-and-section-elements">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a></td>
  </tr>
  <tr>
    <td><code>&lt;article&gt;</code></td>
    <td>Defines independent content that should make sense on its own outside of the document such as newspaper articles, blog posts, etc.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#article-and-section-elements">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a></td>
  </tr>
  <tr>
    <td><code>&lt;aside&gt;</code></td>
    <td>Side content other than main content, like a sidebar. These are not considered as part of the main page outline.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#effect-of-semantic-elements">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a></td>
  </tr>
  <tr>
    <td><code>&lt;details&gt;</code></td>
    <td>A way to provide additional information that the user can show or hide. Content that is shown to user by default. Other content is hidden and can be expanded to view.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#detail-element">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#-details-element">details</a></td>
  </tr>
  <tr>
    <td><code>&lt;figcaption&gt;</code></td>
    <td>Provides a caption (explanation) of an image. To be used within &lt;figure&gt;.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#figcaption-element">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#-figcaption-element">figcap</a></td>
  </tr>
  <tr>
    <td><code>&lt;figure&gt;</code></td>
    <td>Contains an image and can be used to group with an image's caption</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#figcaption-element">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a></td>
  </tr>
  <tr>
    <td><code>&lt;mark&gt;</code></td>
    <td>Defines a part of a text you want to highlight. The highlight styling is specified in CSS.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#mark-element">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#-mark-element">mark</a></td>
  </tr>
  <tr>
    <td><code>&lt;summary&gt;</code></td>
    <td>Used within the &lt;details&gt; tag. Specifies the visible content. The rest of the content in details is shown/hidden by user.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#detail-element">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a></td>
  </tr>
  <tr>
    <td><code>&lt;code&gt;</code></td>
    <td>Used to represent short computer code in a sentence. It displays code in default monospace font.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#lesser-known-semantic-elements">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#lesser-known-semantic-elements">Less</a></td>
  </tr>
  <tr>
    <td><code>&lt;abbr&gt;</code></td>
    <td>Used to indicate the occurrence of an abbreviation.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#lesser-known-semantic-elements">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#lesser-known-semantic-elements">Less</a></td>
  </tr>
  <tr>
    <td><code>&lt;br&gt;</code></td>
    <td>Used to introduce a line break in your HTML document.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#lesser-known-semantic-elements">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#lesser-known-semantic-elements">Less</a></td>
  </tr>
  <tr>
    <td><code>&lt;hr&gt;</code></td>
    <td>Used to introduce a horizontal line in your HTML document..</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#lesser-known-semantic-elements">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#lesser-known-semantic-elements">Less</a></td>
  </tr>
  <tr>
    <td><code>&lt;address&gt;</code></td>
    <td>Used to supply contact information for its nearest &lt;article&gt; or &lt;body&gt; ancestor.</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#lesser-known-semantic-elements">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#lesser-known-semantic-elements">Less</a></td>
  </tr>
  <tr>
    <td><code>&lt;div&gt;</code></td>
    <td>define a division or a section of the document; a block level element</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#div-and-span-elements">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a></td>
  </tr>
  <tr>
    <td><code>&lt;img&gt;</code></td>
    <td>embeds an image into the document</td>
    <td><a hreh="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-img-tag">HTML18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#new-html5-semantic-elements">HTML19</a></td>
  </tr>
 </tbody>
</table>



### Tags

#### Definition and Characteristics of Tags

+ The annotations with "<" amd ">" separated from the regular text

+ Use to organize a text file (which is just a long string of characters) such that it represents a tree of elements that make up the html document

+ The bits of text you use to tell the computer where an element begins and ends

+ HTML can indicate the beginning and end of a tag, i.e. the presence of '<' tells the browser 'this next bit is markup, pay attention'.

+ To stop using that tag and do something else, so '<' and '>' are again used by adding a '/' right after the '<' to indicated that it's a 'close tag'.

+ "self closing" tags: an element completely described by its attributes, and thus no need for other content

+ [Semantic vs Style tags](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#separating-content-style)
  + Style tags
    + focused purely on presentation and design in HTMl4
    + how the text should look like on the screen in HTMl4
    + not produce appropriate styling for some parts of the world, e.g., Chinese characters using underlining than bold
    + HTML5: recommend to use class attributes to identify the semantic intention of the markup; important for pages that get translated
    + Bold:
      + a style that makes letters thicker so it stands out among other text but it has no semantic meaning
      + for example for voice browsers, screen readers, and other types of ways to access the Web
      + HTML5: used as a stylistic offset such as keywords in a document, product names or action words without making them as important
    + Italic:
      + slants text
      + usually italicize names of magazine, books, TV shows etc.
      + purely for presentation purposes
      + HTML5: used for text in a different mood or voice, such as foreign words, a thought or technical terms
  + Semantic tags
    + referred to the meaning of words in a language in HTMl4
    + something about the semantic of the tag, meaning in HTMl4
    + netstable
    + E.g., `<em>`, `<strong>`
    + Strong:
      + an indication of how something should be
      + like bold in a browser, but mean 'speak with urgency or seriousness' when reading text aloud
      + represent importance, seriousness, or urgency for its content
    + Emphasis
      + used to stress emphasis of its contents
      + emphasizing word in a sentence able to change the whole meaning
      + HTML5: used for words and sentences you would pronounce differently
      + HTML5: not used to convey importance
  + Ref: [Using `<b>` and `<i>` elements](https://www.w3.org/International/questions/qa-b-and-i-tags)



<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/633117d2ef0f4bb59cda68d966b6d288/f36ef1f210bf460e9e0f43be78fb0bd5/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%40427074c031424e189e4898d969d7dcd9">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9df11f203d18addb831da2f379cb49a5/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/tags.png" style="margin: 0.1em;" alt="Diagram of an element" title="Diagram of an element" width="250">
  </a></div>
</div>


#### Comment Tags

+ Inline: `<!-- This is a comment -->`

+ Multiple lines:

  ```html
  <!--
  Beginning of comment
  ... 
  End of comment
  -->
  ```

+ Comments cannot be nested.


#### List of Typical Tags


<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<thead>
  <tr style="border-bottom: double black;">
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Tag</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 70%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Link</th>
  </tr>
</thead>
<tbody>
  <tr><td>&lt;!DOCTYPE html&gt;</td>
    <td> declaration "This is an HTML5 file, in case you were wondering"</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#all-together-now">DOC18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">DOC19</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">Tags18</a></td></tr>
  <tr><td> &lt;html&gt;</td>
    <td> where the actual HTML code begins and end</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#all-together-now">All18</a>, <a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">HTML19</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">Tags18</a></td></tr>
  <tr><td> &lt;meta&gt;</td>
    <td> metadata content; represent metadata that cannot be represented by other HTML meta-related elements</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#the-meta-tag">Meta</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta">MDN</a></td></tr>
  <tr><td> &lt;head&gt;</td>
    <td> where the browser can find style tips, and what the title of the page is</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#everything-in-html">HEAD18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">HEAD19</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">Tags18</a></td></tr>
  <tr><td> &lt;body&gt;</td>
    <td> contains all of the content of your page, essentially what the user sees</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#15-best-practices">Body18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">Body19</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">Tags18</a></td></tr>
  <tr><td> &lt;h1&gt; ~ &lt;h6&gt;</td>
    <td> a whole collection of heading tags</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">Heading18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">Heading19</a></td></tr>
  <tr><td> &lt;p&gt;</td>
    <td> paragraph; text wrapped in may be indented or have extra vertical white space before starting; typically be a new line</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">P18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">P19</a></td></tr>
  <tr><td> &lt;q&gt;</td>
    <td> quotes; used when you want to quote a person or written work in your Web page; customarily displayed using quotation marks, again unrelated to strings</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">Quote18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">Quote19</a></td></tr>
  <tr><td> &lt;blockquote&gt;</td>
    <td> quote a larger passage; typically set the quoted text apart from the surrounding text and indent it, to make clear that it is quoted text</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">BlkQuote18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">BlkQuote19</a></td></tr>
  <tr><td> &lt;ul&gt;, &lt;ol&gt;</td>
    <td> indicate a list of things; &lt;ol&gt;: "ordered" list; &lt;ul&gt;: "unordered" list</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">List18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">List19</a></td></tr>
  <tr><td> &lt;li&gt;</td>
    <td> List Item; nested inside a list (&lt;ul&gt; or &lt;ol&gt;)</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">Item18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">Item19</a></td></tr>
  <tr><td> &lt;hr&gt;</td>
    <td> Horizontal Rule; a horizontal line across the width of the text</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">Rule18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">Rule19</a></td></tr>
  <tr><td> &lt;br&gt;</td>
    <td> line break; break the "white space" rule: where spaces and carriage returns are generally treated the same; treated as a <i>required carriage return</i></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">Break18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">Break19</a></td></tr>
  <tr><td> &lt;pre&gt;</td>
    <td> "PREformatted text", meaning "I've set this up just the way I want it, don't mess with it."; monospace font, and none of the spaces, tabs or carriage-returns are ignored </td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">Format18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">Format19</a></td></tr>
  <tr><td> &lt;i&gt;</td>
    <td> italic text; used for text in a different mood or voice, such as foreign words, a thought or technical terms</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#changes-in-html5">Tags18</a>, <a href="">Tags19</a></td></tr>
  <tr><td> &lt;b&gt;</td>
    <td> bolded text; used as a stylistic offset such as keywords in a document, product names or action words without making them as important; can also be used as headings in list items</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#changes-in-html5">Tags18</a>, <a href="">Tags19</a></td></tr>
  <tr><td> &lt;em&gt;</td>
    <td> Emphasizes text; semantic tag; stress emphasis of its contents</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#semantic-vs-style-tags">Tags18</a>, <a href="">Tags19</a></td></tr>
  <tr><td> &lt;strong&gt;</td>
    <td> Important text; semantic tag; indication of how something should be</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#semantic-vs-style-tags">Tags18</a>, <a href="">Tags19</a></td></tr>
  <tr><td> &lt;a&gt;</td>
    <td> create a hyperlink to other web pages, files, locations within the same page, email addresses, or any other URL</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#anchor-element">Tags18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#anchor-element">Tags19</a></td></tr>
  <tr><td> &lt;style&gt;</td>
    <td> place CSS directly into an HTML document; anywhere in an HTML document;most common place: &lt;head&gt; section</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#3-2-css-basic-syntax">Tags18</a>, <a href="">Tags19</a></td></tr>
  <tr><td> &lt;link&gt;</td>
    <td> specify .css file within &lt;head&gt; section</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#3-2-css-basic-syntax">Tags18</a>, <a href="">Tags19</a></td></tr>
</tbody>
</table>



### Attributes

#### Definition and Characteristics 0f Attributes

+ __Attributes are used in tags to further define the tag__

+ A given element on your Web page can be distinguished by any number of unique or common attributes.

+ Identify attribute uniquely with an 'id' attribute, or group it with a class of other elements by setting the 'class' attribute

+ Syntax: Attribute name, equal sign, opening quote, attribute value, closing quote, e.g., `start="5"`, Attribute name: start; Attribute Value = 5

+ Boolean attribute: presence = true, omit = false

+ Reference: [Attribute List](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.oreilly.com/library/view/learning-web-design/9780596527525/ch04.html">
    <img src="https://www.oreilly.com/library/view/learning-web-design/9780596527525/graphics/lwd3_0411.jpg" style="margin: 0.1em;" alt="Attributes are instructions that clarify or modify an element." title="An element with attributes." width="350">
  </a></div>
</div>


#### List of Global Attributes

+ [Global attributes](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#global-)
  + applied to all tags
  + common attributes.
  + E.g., `id`, `class`

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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



#### Event-handler Attributes


<table  style="margin: 0 auto; border: 1px solid black; border-collapse: collapse; width: 70vw;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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


#### Non-global Attributes

+ [Non-global attributes](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#non-global-attributes)
  + applied to a specific instance of a tag
  + able to applied to one or more tags
  + E.g., `start` & `reversed` only for `<ol>`; `width` for `<img>`, `<video>` and `<input>`


<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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

## Hyperlink

### Characteristics of Hyperlink

+ Hyperlink: any text or image and will take you to another page
  + another Web page, e.g. https://en.wikipedia.org/wiki/Hyperlink
  + a bookmark (a specific part of a Web page), e.g. https://en.wikipedia.org/wiki/Hyperlink#History
  + the id attribute as a link target in the unit about attributes earlier; e.g. #History
  + a local link (link to another part of the same Web page); e.g. a_tag.asp
  + an email: e.g. mailto:helloauthor@w3c.com

+ Best practice
  + Apply hyperlinks to short phrases.
  + Make link phrase meaningful.
  + Don't use short link text.
  + Appearance - links have a default appearance in most browsers, blue and underlined.
  + image links with alternate text

+ States of a hyperlink (typical)
  + Unvisited: blue + underlined
  + Visited: purple + underlined
  + Active: red + underlined


### Attributes for Hyperlink

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Attribute</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Usage</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td><code>href</code></td>
    <td>The URL of a linked resource.</td>
    <td>&lt;a href="<span style="color: #339966;">https://qwant.com</span>"&gt; &lt;/a&gt;</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-table-tag"> href </a></td>
  </tr>
  <tr>
    <td rowspan="2"><code>target</code></td>
    <td><code>_self</code>: In the same view where the link resides. If no target is specified, this is the default behavior.</td>
    <td>&lt;a href="<span style="color: #339966;">https://qwant.com/</span>" target="<span style="color: #339966;">_self</span>"&gt;&lt;/a&gt;</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-target-attribute"> target </a></td>
  </tr>
  <tr>
    <td><code>_blank_</code>: In a new window or tab. This is very convenient if you want to link the user to a Web page without having the current page disappear. By clicking on the previous window or tab, they can redirect to the page where the link is.</td>
    <td>&lt;a href="<span style="color: #339966;">https://qwant.com/</span>" target="<span style="color: #339966;">_blank</span>"&gt;&lt;/a&gt;</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-target-attribute"> target </a></td>
  </tr>
  <tr>
    <td><code>media</code></td>
    <td>Specifies a hint of the media for which the linked resource was designed.</td>
    <td>&lt;a href="<span style="color: #339966;">https://en.wikipedia.org/wiki/Media_queries?output=print</span>" media="print and (resolution:250dpi)"&gt; Print wiki page about media queries &lt;/a&gt;</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-media-attribute">media</a></td>
  </tr>
  <tr>
    <td><code>download</code></td>
    <td>Indicates that the hyperlink is to be used for downloading a resource.</td>
    <td>&lt;a href="<span style="color: #339966;">/assets/hello.txt</span>" download&gt;</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-download-attribute">download</a></td>
  </tr>
  </tbody>
</table>



## Table Element

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 50vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Type</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Element</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 20%">Link</th>
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
    <td> <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-thead-tag"> Table Header </a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-tfoot-tag"> Table Footer </a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-tbody-tag"> Table Body </a></td>
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

### Characteristics of Image Element

+ [Concerns when using the `src` attribute](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#image-src-attribute):
  + no space in image path.
  + image path matches the capitalization of the actual path
  + use Unix (/) path name separator instead of Windows () style
  + ensure the image resides in the right location or the user is going to get a broken link
  + relative path best practice: always keep the images at the same level, or one level down
  + absolute paths: not recommended

+ [alt attribute](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#attribute-alt)
  + provide a short description of what the image is about
  + convey information about the image or its function in the page
  + important attribute:
    + the text alternative to the image for users who are unable to see the image, instead using assistive technology like screen readers that rely on the alt text
    + screen readers will typically announce that there is an image and read out the contents of the alt attribute
    + alternate text displayed if image not displayed if
      + the path in your source attribute is wrong
      + slow internet connection
      + image relocated or renamed
    + Search engines rely on the alt attribute to find out what the image is about.
    + tell mobile users what the image is about if images turn off

+ [reasons using images](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#purpose-of-the-image):
  + represent a concept, illustration or just a photograph that provide information
  + background for a button or link
  + display a quote or message in the form of text in an image
  + decorative images

+ Images used for decoration or presentation purposes should have an empty value for alt. `<img alt="">`

+ The alt attribute is meant to be an alternate source of information while the title attribute should provide additional information about the image.

+ 


### List of Attributes for Image Element

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Description</td>
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
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#image-src-attribute">Source18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-img-tag">src19</a></p>
    </td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>alt</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Provide a short description of what the image is about (must have)<br/>offer meaning to the image and suggests the purpose of the image content</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here"&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#the-alt-attribute">Alt Text</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#attribute-alt">alt</a></p>
    </td>
  </tr>
  <tr>
    <td>title</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">A global attribute to provide the title of the image</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" title="Add a title of the image"&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#the-title-attribute">Ttitle</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#global-attribute-title-">Global Ttitle</a>, <a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-title-attribute">title</a></p>
    </td>
  </tr>
  <tr>
    <td>height <br/><br/> width</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Resize the image in pixels without using an external editor</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" height="hhh"&gt;</span><br/><br/><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" width="www"&gt;</span><br/><br/><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" width="www" height="hhh"&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#the-height-width-attributes">Size</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-height-width-attributes">width&height</a></p>
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

### [Video Tag][040]

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


### [Source Tag][041]

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


### [Track Element][042]


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
  </tbody>
</table>


## Embedded Content

### [The iframe Tag][043]


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
[012]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#global-attributes-class
[013]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#global-attributes-lang
[014]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#global-attributes-title
[015]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#changes-in-html5
[016]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#semantic-vs-style-tags
[017]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#detail-element
[018]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#figcaption-element
[019]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#mark-element
[020]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#effect-of-semantic-elements
[021]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#new-html5-semantic-elements
[022]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#lesser-known-semantic-elements
[023]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#header-vs-h1---h6
[024]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#article-and-section-elements
[025]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#div-and-span-elements
[026]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#the-img-tag
[027]: ../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#image-src-attribute
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
[038]: ../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#audio-tag
[039]: ../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#source-element-for-multiple-source-files
[040]: ../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#video-element
[041]: ../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#source-element-for-multiple-source-files-1
[042]: ../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#track-element-for-captions-and-subtitles
[043]: ../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#the-iframes-tag

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
