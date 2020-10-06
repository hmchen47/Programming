# HTML5 - Basics


## The big three: HTML5, CSS and JavaScript

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

+ [HTML5](../WebDev/Frontend-W3C/2-HTML5Coding/01b-Basics.md#122-what-is-html5)
  + published on 28 October 2014
  + features
    + Web-based applications with more interaction
    + video support
    + graphics
    + more styling effects
    + full set of APIs
  + adapt to any device: desktop, mobile, tablet, or television device
  + open platform
  + typical two means
    + Open Web Platform: HTML5 specification, CSS, SVG, MathML, Geolocation, XMLHttpRequest, 2D Context, Web Fonts (WOFF) and others
    + HTML5 specification

+ [JavaScript & HTML5](../WebDev/Frontend-W3C/2-HTML5Coding/03b-Graphics.md#321-about-javascript-and-html5)
  + adding js code in HTML page: `<script>`...`</script>`
  + JavaScript code executed before the browser could see the rest of the page as the `<script></script>` located before the `<body>`
  + `console.log(...)`: display in the JavaScript console the message...
  + debug:
    + dev. tool on web browser &gt; console tab &gt; error/log msgs
    + allowing to type any JS command



## Tags, Elements and Attributes of HTML

<table style="width: 55vw; margin: auto;">
<thead>
  <tr>
    <th style="background-color: #0f9d58; width: 10%;">HTML Tags</th>
    <th style="background-color: #0f9d58; width: 10%;">HTML Elements</th>
    <th style="background-color: #0f9d58; width: 10%;">HTML Attributes</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>HTML tags are used to hold the HTML element.</td>
    <td>HTML element holds the content.</td>
    <td>HTML attributes are used to describe the characteristic of an HTML element in detail.</td>
  </tr>
  <tr>
    <td>HTML tag starts with &lt; and ends with &gt;</td>
    <td>Whatever  written within a HTML tag are HTML elements.</td>
    <td>HTML attributes are found only in the starting tag.</td>
  </tr>
  <tr>
    <td>HTML tags are almost like keywords where every single tag has unique meaning.</td>
    <td>HTML elements specifies the general content.</td>
    <td>HTML attributes specify various additional properties to the existing HTML element.</td>
  </tr>
</tbody>
</table>


<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.w3.org/community/webed/wiki/HTML/Training/Tag_syntax">
    <img src="https://www.w3.org/community/webed/wiki/images/3/39/Elements.png" style="margin: 0.1em;" alt="HTML elements usually come in tag pairs" title="HTML elements" width="350">
    <img src="https://www.w3.org/community/webed/wiki/images/b/bc/Option.png" style="margin: 0.1em;" alt="An element can have attributes to refine its meaning" title="HTML elements" width="350">
  </a></div>
</div>


+ [Categories of HTML elements](https://html.spec.whatwg.org/multipage/dom.html#content-categories)
	+ Metadata content
		+ set up the presentation or behavior of the rest of the content
		+ set up the relationship of the document w/ other documents
		+ convey other "out of band" information
		+ list of elements: base, link, meta, noscript, script, style, template, title
	+ flow content: most elements used in the body of documents and applications
	+ sectioning content
		+ define the scope of headings and footers
		+ list of element: article, aside, nav, section
	+ heading content
		+ define the header of a section
		+ list of elements: h1, h2, h3, h4, h5, h6, hgroup
	+ phrasing content
		+ the text of the document, as well as elements that mark up that text at the intra-paragraph level
		+ runs of phrasing content form paragraphs
	+ embedded content
		+ import another resource into the document, or content from another vocabulary that is inserted into the document
		+ list of element: audio, canvas, embed, iframe, img, math, object, picture, svg, video
	+ interactive content
		+ specifically intended for user interaction
		+ a (if the href attribute is present), audio (if the controls attribute is present), button, details, embed, iframeimg (if the usemap attribute is present), input (if the type attribute is not in the Hidden state), label, object (if the usemap attribute is present), select, textarea, video (if the controls attribute is present)



## Template

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

+ [Minimum HTML5 Document](../WebDev/Frontend-W3C/2-HTML5Coding/01c-Basics.md#a-minimal-html5-document)

    <div><ol>
    <li value="1">&lt;!DOCTYPE html&gt;</li>
    <li>&lt;html lang="en"&gt;</li>
    <li>&lt;head&gt;</li>
    <li>&nbsp; &nbsp;&lt;meta charset="utf-8"&gt;</li>
    <li>&nbsp; &nbsp;&lt;title&gt;Page Title&lt;/title&gt;</li>
    <li>&nbsp; &nbsp;&lt;link rel="stylesheet" href="style.css"&gt;</li>
    <li>&nbsp; &nbsp;&lt;script src="script.js"&gt;&lt;/script&gt;</li>
    <li>&lt;/head&gt;</li>
    <li>&lt;body&gt;</li>
    <li>... &lt;!-- The rest is content --&gt;</li>
    <li>&lt;/body&gt;</li>
    <li>&lt;/html&gt;</li>
    </ol></div>

  + `<!DOCTYPE html>`: used by tools and specifying the rules used by an HTML or an XHTML page
    + required but in practice not always need a doctype because any common web browser will render document regardless
    + rules in "Document Type Definitions" (DTDs)
    + not used by Web browsers to validate the structure of an HTML page
    + using only "rules" contained in their own "HTML engine"
    + used by web browser w/ different rendering engines
    + HTML4 more complicated and requiring selection from transitional, strict, or frameset; e.g., `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "https://www.w3.org/TR/html4/loose.dtd">`
  + type: attributes
    + optional, required in HTML4
    + `rel="stylesheet"` default value: `type="text/css"`
    + including JavaScript file" `<script src="script.js"></script>` w/o `type="text/javascript"` as old way
  + simplified syntax
    + able to omit quotes or use uppercase, lowercase or a combination of the two
    + no longer a closing tag required in many elements but __recommended__
    + quoted only if containing spaces or some non-alphanumeric characters but __recommended__, e.g., `<link rel=stylesheet href=style.css>`


## Useful References & Tool Links

+ Specifications
  + [MDN HTML elements reference list](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
  + [MDN attribute reference list](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)
  + [W3C HTML5 specification](https://www.w3.org/TR/html5/)
  + [W3C cheatsheet](https://www.w3.org/2009/cheatsheet/)

+ Tools
  + [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
  + [CSS validator](https://jigsaw.w3.org/css-validator/)
  + [Unicorn](http://validator.w3.org/unicorn/)  
  + [W3C Internationalization Checker](https://validator.w3.org/i18n-checker/)
  + [W3C Link Checker](http://validator.w3.org/checklink)
  + [Web Accessibility Evaluations Tools List](https://www.w3.org/WAI/ER/tools/)

+ Editors
  + [CodePen](http://codepen.io/)
  + [JS Bin](http://jsbin.com)

+ References
  + [Browser Compatibility]()
  + [WC3 Named character references](https://www.w3.org/TR/2011/WD-html5-20110113/named-character-references.html)
  + [HTML character codes](https://www.rapidtables.com/web/html/html-codes.html)
  + [Web Content Accessibility Guidelines (WCAG) Overview](https://www.w3.org/WAI/intro/wcag.php)
  + [Setting language preferences in a browser](http://www.w3.org/International/questions/qa-lang-priorities)


## HTML Layout Elements

+ Typical HTML Layout
  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://tinyurl.com/y4zj9brg">
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

+ Make whole Web page into one big table: [BAD IDEA](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#separating-content-and-style)
  + semantically incorrect for layout
  + making HTML larger
  + Accessibility: tables are not very screen reader friendly
  + harder to redesign
  + css easier to maintain consistency among pages

+ [Structural elements](../WebDev/Frontend-W3C/2-HTML5Coding/01c-Basics.md#132-structural-elements)

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
      <img src="https://tinyurl.com/y394s3ts" style="margin: 0.1em;" alt="Some of the new structural elements introduced by HTML5: section, article, etc." title="Some of the new structural elements introduced by HTML5: section, article, etc." width=350>
    </a>
  </div>

  + `<header>`
    + introduction of "sectioning elements"
    + typically on top of each page, or a header of a long `<article>` or of a long `<section>`
  + `<footer>`: the footer of a site, a long `<article>`, or a long `<section>`
  + `<nav>`: the main navigation links
  + `<article>`:
    + independent content: individually extracted from the document and syndicated without penalizing its understanding
    + typically a blog post
  + `<section>`:
    + generic section used to group different articles
    + generally used with a header
  + `<time>`: used for marking up times and dates
  + `<aside>`:
    + section not necessarily directly related to the main content
    + providing additional information
  + `<figure>` and `<figcaption>`: encapsulating a figure as a single item
  + `<main>`:
    + represent the main content of the body of a document or application
    + consist of content that is directly related to or expands upon the central topic of a document or central functionality of an application
    + __only one__ in a document


## Encoding

+ UTF-8: `<meta charset="utf-8">` in `head` section
+ Always use the Unicode character encoding UTF-8 for your Web pages
+ Ensure that your editor saves the file in UTF-8


## Named Characters

+ [WC3 Named character references](https://www.w3.org/TR/2011/WD-html5-20110113/named-character-references.html)

+ [HTML character codes](https://www.rapidtables.com/web/html/html-codes.html)

+ Frequent used codes

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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


## Accessibility

+ [Accessibility](../WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#accessibility): designing Web page with various disabilities in mind

+ Guidelines
  + not too small on font size
  + not too tight on line height
  + good color contrast for foregrounbd and background
  + not irregularly space text or make it jump around


## Recommendations & Misc.

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

+ [Accessibility Resources](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#wai-resources)

+ [International Language Resurces](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#internationalization-resources)


## Debugging

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


