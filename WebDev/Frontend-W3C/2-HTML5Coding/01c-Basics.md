# Week 1: HTML5 Basics


## 1.3 Structural elements


### 1.3.0 Lecture Notes

+ [Minimum HTML5 Document](#a-minimal-html5-document)

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

  + `<meta charset="utf-8">`: <mark style="color: black; background-color: lightpink;">best practice</mark> to declare the character set
  + `<!DOCTYPE html>`: used by tools and specifying the rules used by an HTML or an XHTML page
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

+ [Structural elements](#132-structural-elements)

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

+ [`<article>` and `<section>` elements](#134-more-on-article-and-section)
  + `<article>`
    + designed for stand-alone parts of a document eventually syndicated in RSS streams
    + able to be cut into different `<section>` elements
  + `<section>`
    + used to cut a logical part into subparts
    + probably cut into different `<article>` elements

+ [Sectioning elements](#135-headings-and-structural-elements)
  + headings: `<h1>...<h6>`
    + used to display headings with different sizes by default, when no CSS used
    + define the header of a section
  + section elements: `<section>`, `<article>`, `<nav>` and `<aside>`
    + sections: a document cut into slides by sectioning elements
    + each potentially w/ a heading and an outline associated
  + multiple headings of different rank with sectioning content
    + 1st element of a heading content in an element of sectioning content representing the heading for that section
    + headings of _equal or higher rank_: new (implied) sections
    + headings of _lower rank_: implied subsections that are part of the previous one
    + `<h1>` inside a `<section>`: the browser lowers its default size automatically

+ [Best practices of sectioning elements](#136-best-practices-when-using-sectioning-elements)
  + always add a heading to explicit sectioning content
    + including a heading (a `<h1>, <h2>...<h6>`) in each sectioning element
    + the `<body>` element: sectioning root
    + example

      <div><ol>
      <li value="1"><span style="color: hotpink;">&lt;body&gt;</li>
      <li>&nbsp; &nbsp;&nbsp;<strong style="color: olive;">&lt;h1&gt;Example Blog&lt;/h1&gt;</strong></li>
      <li>&nbsp; &nbsp; <span style="color: hotpink;">&lt;section&gt;</li>
      <li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;header&gt;</li>
      <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong style="color: olive;">&lt;h2&gt;Blog post of April 2020&lt;/h2&gt;</strong></li>
      <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&lt;p&gt;Posted by Michel Buffa...&lt;/p&gt;</li>
      <li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;/header&gt;</li>
      <li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;p&gt;Content of the blog post...&lt;/p&gt;</li>
      <li>&nbsp; &nbsp;&lt;/section&gt;</li>
      <li> &lt;/body&gt;</li>
      </ol></div>

  + using `<section>`, `<article>`, etc. instead of just `<h1>...<h6>`, not to rely  on implicit sectioning
    + `<header> `element
      + a container
      + not defining new sections of a document nor affecting the hierarchy levels
    + HTML not dedicated mechanism for marking up subheadings, alternative titles or taglines
    + example

      <div><ol>
      <li value="1">&lt;body&gt;</li>
      <li>&lt;h1&gt;Apples&lt;/h1&gt;</li>
      <li>&lt;p&gt;Apples are fruit.&lt;/p&gt;</li>
      <li><strong style="color: olive;">&lt;section&gt;</strong></li>
      <li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h2&gt;Taste&lt;/h2&gt;</strong></li>
      <li>&nbsp; &nbsp; &nbsp;&lt;p&gt;They taste lovely.&lt;/p&gt;</li>
      <li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;section&gt;</strong></li>
      <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h3&gt;Sweet&lt;/h3&gt;</strong></li>
      <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;p&gt;Red apples are sweeter than green ones.&lt;/p&gt;</li>
      <li>&nbsp; &nbsp; &nbsp;&lt;/section&gt;</li>
      <li>&lt;/section&gt;</li>
      <li><strong style="color: olive;">&lt;section&gt;</strong></li>
      <li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h2&gt;Color&lt;/h2&gt;</strong></li>
      <li>&nbsp; &nbsp; &nbsp;&lt;p&gt;Apples come in various colors.&lt;/p&gt;</li>
      <li>&lt;/section&gt;</li>
      <li>&lt;/body&gt;</li>
      </ol></div>


+ [Table of contents](#137-embedding-a-table-of-contents)
  + useful for debugging the structure of a page
  + checking the presence of headings after sectioning content
  + displaying some "untitled entries" $\to$ missing some headings


+ [The `<main>` element](#138-the-main-element)
  + identify the main content of the document
  + provide a navigable document structure for assistive technology users as well as styling hooks for devs
  + supported by major modern browsers
  + constraints
    + no more than one `<main>` element in a document
    + not a descendant of an `<article>`, `<aside>`, `<footer>`, `<header>`, or `<nav>` element
  + <mark style="color: black; background-color: lightpink;">best practice</mark>:
    + split page content into "regions" defined by the 5 elements (`aside`, `footer`, `header`, `main` and `nav`)
    + add a `<main>` to document if other sectioning elemets used

+ [Best practices](#139-the-blog-example-applying-best-practices)
  + some H1s inside an `<article>` in a `<section>`
    + documents moved more easily or integrated inside an RSS stream
    + no need to renumber the headings
    + constraints:
      + use some CSS styling
      + may confuse some screen readers not yet taking into account of computing the heading hierarchy
    + solution: use an H1 right after the `<body>` and use only H2...H6 inside `<section>`, `<article>`, `<nav>` and `<aside>`
  + add a heading in the `<nav>` element
    + fix the outline of the document by removing the untitled entry
    + make screen readers happy as they will better vocalize the structure of the page
  + NOT display the heading content on screen
    + not using `display:none` or `visibility:hidden` in CSS stylesheet
    + recommended technique

      <code>
      nav header {<br/>
      &nbsp;&nbsp;&nbsp;&nbsp; position: absolute !important;<br/>
      &nbsp;&nbsp;&nbsp;&nbsp;  clip: rect(1px 1px 1px 1px); /* IE6, IE7 */<br/>
      &nbsp;&nbsp;&nbsp;&nbsp;  clip: rect(1px, 1px, 1px, 1px);<br/>
      &nbsp;&nbsp;&nbsp;&nbsp;  padding:0 !important;<br/>
      &nbsp;&nbsp;&nbsp;&nbsp;  border:0 !important;<br/>
      &nbsp;&nbsp;&nbsp;&nbsp;  height: 1px !important; <br/>
      &nbsp;&nbsp;&nbsp;&nbsp;  width: 1px !important; <br/>
      &nbsp;&nbsp;&nbsp;&nbsp;  overflow: hidden;<br/>
      }       
      </code>

  + Not advised to include interactive content (links, controls etc) hidden offscreen, all interactive content must have a visible focus indicator
  + Using H1 as top level headings only, using H2...H6 in sectioning content
    + risky to use nested H1s
    + browsers not correctly implement the "outline algorithm"

+ [Page layout](#1310-examples-of-page-layouts)
  + 2 columns:
    + a `<section>` on the left and an `<aside>` on the right
    + using the float and width CSS properties
  + 3 columns:
    + centered, of equal size
    + using the float and width CSS properties
    + using the CSS flex property



### 1.3.1 Greater simplicity

Changes have been made to particular elements in HTML5 making it simpler to use. In this section, we will look at some examples highlighting these improvements, including:

+ the new doctype definition;
+ the fact that the "type" attribute of elements such as `<link>` or `<script>` are now  optional;
+ the syntax constraints that have been relaxed;
+ the new structural elements that have been added, etc.


#### A minimal HTML5 document

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


Let's compare it to the HTML4 minimal document below (taken from this source). Differences are underlined in red:

<div><ol>
<li value="1"><span style="text-decoration: underline; color: hotpink;">&lt;!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "https://www.w3.org/TR/html4/strict.dtd"&gt;</span> </li>
<li>&lt;html lang="en"&gt; </li>
<li> &lt;head&gt; </li>
<li>&nbsp; &nbsp;&nbsp;&lt;meta <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">http-equiv="content-type" content=</span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">"text/html"</span></span>&nbsp;charset="utf-8"&gt; </li>
<li>&nbsp; &nbsp;&nbsp;&lt;title&gt;title&lt;/title&gt; </li>
<li>&nbsp; &nbsp;&nbsp;&lt;link rel="stylesheet" <strong style="color: olive;"><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">type="text/css"</span></span></strong> href="style.css"&gt; </li>
<li>&nbsp; &nbsp;&nbsp;&lt;script <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">type="text/javascript"</span></span> src="script.js"&gt;&lt;/script&gt; </li>
<li> &lt;/head&gt; </li>
<li>&lt;body&gt; </li>
<li>...</li>
<li>&lt;/body&gt; </li>
<li>&lt;/html&gt;</li>
</ol></div>


#### Simpler character set definition

One word about the `<meta charset="utf-8">` at line 4 in the HTML5 version: it is a __best practice__ to declare the character set of your document to protect against [a serious security risk](https://tinyurl.com/yy47zgqw). For more details, please refer to the "Why Internationalization is important" section in the Course intro chapter.


#### No more complicated DOCTYPE definitions

The "DOCTYPE" (Document Type Declaration) is used by tools such as HTML validators (i.e. [the W3C validator](https://validator.w3.org/)), and specifies the rules used by  an HTML or an XHTML page. These rules are contained in special documents called "Document Type Definitions" (also abbreviated as DTDs), written in a language that may seem a bit barbaric to humans (they are intended to be read by software), and hosted by W3C.

DTDs are not used by current Web browsers to  validate the structure of an HTML page, as  they "read" the code without using the DTD to decipher it, using only "rules" contained in their own "HTML engine", but it is still preferable to indicate the doctype as modern browsers have several rendering engines that are chosen depending on the doctype.

Old HTML1 Web pages will not be rendered the same way as new HTML5 pages, since, in the 90's, some of them were written by hand and may contain errors, embedded HTML elements, etc.

With HTML4, doctype definitions looked like this: `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "https://www.w3.org/TR/html4/loose.dtd">`, which was even more complicated as one had to choose between three different possibilities (doctypes could be transitional, strict, or frameset). Most of the time, the doctype definition was copied and pasted from one document to another and was nearly impossible to memorize.

With HTML5, there is only one way to indicate the doctype, and it's so simple there is no reason to forget it:

<div><ol>
<li value="1">&lt;!doctype html&gt;</li>
</ol></div>



#### The "TYPE" attribute is optional

With a `rel="stylesheet"` attribute, it is no longer necessary to indicate `type="text/css"` (from [the specification](https://tinyurl.com/yxnfw3he): "the default type for resources given by the `stylesheet` keyword is `text/css`.")

The "type" attribute is not needed in HTML5, and even old browsers will use text/css as the default type for stylesheets today. So, either way, you can omit the "type" attribute altogether and use:

<div><ol>
<li value="1">&lt;link href="file.css" rel="stylesheet"/&gt;</li>
</ol></div>

instead of:

<div><ol>
<li value="1">&lt;link href="file.css" rel="stylesheet" type="text/css"/&gt;</li>
</ol></div>

We will not go into detail about the <link> element, but the fact that the type attribute is becoming optional shows the current direction taken by HTML5: towards greater simplicity.

Please see how to include a JavaScript file in our page:

<div><ol>
<li value="1">&lt;script src="script.js"&gt;&lt;/script&gt; </li>
</ol></div>

Here again, the type attribute has been omitted. Just as a reminder, the old way to do the same thing is: 

<div><ol>
<li value="1">&lt;script type="text/javascript" src="script.js"&gt;&lt;/script&gt;</li>
</ol></div>


#### More flexible syntax constraints

If you look at the "minimal document" example, or at other examples in this course, you won't find a lot of differences compared to the same code in XHTML: attribute values are surrounded by quotes, all elements are written in lower case, etc. This is because we are used to writing this way, but HTML5 also supports a simplified syntax:

+ Thanks to HTML5, you can omit quotes (not always, but most of the time) or use uppercase, lowercase or a combination of the two.
+ Many elements no longer need a closing tag: `</li>`, `</dt>`, `</dd>`, `</tr>`, `</th>`, `</td>`, `</thead>`, `</tfoot>`, `</tbody>`, `</option>`, `</optgroup>`, `</p>` (in most cases), `</head>`, `</body>` and `</html>`. Older browsers often add closing tags automatically at render time. We recommend, however, closing tags that would naturally be closed: the ones that delimit a particular zone in the document.
+ Attribute values only need to be quoted if they contain spaces or some non-alphanumeric characters, instead of writing `<link rel="stylesheet" href="style.css">`, we could have used `<link rel=stylesheet href=style.css>`. However, for compatibility with older browsers, it is wiser to still use quotes...


#### Knowledge check 1.3.1 

1. Did you read this page? Aha, let's check!

  What is the minimal code to define DOCTYPE in HTML5?

  a. `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">`<br/>
  b. `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">`<br/>
  c. `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">`<br/>
  d. `<!DOCTYPE html>`<br/>

  Ans: d


### 1.3.2 Structural elements

#### Video: new structural elements

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V003100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" width=100/>
</a><br/><br/>

[Transcript](https://tinyurl.com/yycsb5a5)


#### New structural elements

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/y394s3ts" style="margin: 0.1em;" alt="Some of the new structural elements introduced by HTML5: section, article, etc." title="Some of the new structural elements introduced by HTML5: section, article, etc." width=350>
  </a>
</div>


##### History

As Web site layouts evolve, HTML5 structural elements such as lists, paragraphs, tables, etc. show their limits. Today, many Web sites offer navigation menus, tabbed panels, headers, footers, and so on. The way these "parts"' are implemented relies heavily on `<div>` and `` elements with different id and class attributes, lots of CSS and lots of JavaScript code to apply custom styles and behaviors.

However, there are some issues with this approach:

+ id and class names differ from one developer to another, from one country to another, etc.
+ Even with the same ids and class names, the css rules may be different
+ JavaScript libraries have become increasingly heavy over the years
+ Web pages have become increasingly heavy over the years!
+ These elements can not be handled by the Web browser natively...

Even if differences exist between ids, classes and css/js implementations, they also share common behaviors, layouts, and "ways of doing things" that could be guessed at first glance by a human.

So various studies have been conducted in order to identify the most popular ids, class names, widgets, etc. used on the Web:

Quoting from this [article](https://tinyurl.com/y4fnq97k): "During the creation of HTML5, Ian Hickson used Google's tools to mine data from over a billion Web pages, surveying what ids and class names are most commonly used on the real world Web. Opera did a similar study of 3.5 million URLs, calling it MAMA ("Metadata Analysis and Mining Application"). MAMA, as structural Web-paged search engine, had a smaller URL set, but looked at a larger and wider variety of Web page statistics".


##### New elements added to the HTML5 set

The results of these surveys led to the addition of new structural elements in HTML5. For example, the very popular `<div>` led to the creation of a `<header>` element, `<div>` to a `<aside>` element, etc.

Finally, the 20 most popular ids and class names found in Hickson's and Opera's surveys gave birth to these new elements (click on the element's name to go to the W3C specification about this element):

<table style="table-layout: auto; text-rendering: optimizelegibility; border-collapse: collapse; border-spacing: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; margin: auto; width:60vw;" cellpadding="10" border="1">
  <caption>HTML5 structural elements with descriptions.</caption>
  <tbody>
    <tr><th scope="”row”">HTML5 element</th><th scope="”row”">Description</th></tr>
  </tbody>
  <tbody style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="font-family: 'courier new', courier;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-header-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;header&gt;</span></strong></a></span></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Introduction of "sectioning elements": an article,&nbsp;a&nbsp;section, the entire document (header page). Typically the header of a Web site that appears on top of each page, or a header of a long <span style="font-family: 'courier new', courier;">&lt;article&gt; or of a long <span style="font-family: 'courier new', courier;">&lt;section&gt;</span></span></td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="font-family: 'courier new', courier;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-footer-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;footer&gt;</span></strong></a></span></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Contains the footer of a site, a long <span style="font-family: 'courier new', courier;">&lt;article&gt;, or a long<span style="font-family: 'courier new', courier;"> &lt;section&gt;</span></span></td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-nav-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;nav&gt;</span></strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Section that contains the main navigation links (within the document or to other pages).</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-article-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;article&gt;</span></strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <p style="text-rendering: optimizelegibility; margin: 0px 0px 1.416em; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: 1em; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.6em !important; vertical-align: baseline;">Independent content, which can be individually extracted from the document and syndicated (RSS or equivalent) without penalizing its understanding. Typically a blog post.</p>
      </td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-section-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;section&gt;</span></strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <p style="text-rendering: optimizelegibility; margin: 0px 0px 1.416em; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: 1em; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.6em !important; vertical-align: baseline;">Generic section used to group different articles for&nbsp;different purposes or subjects, or to define the different sections of a single article. Generally used&nbsp;with a header.</p>
      </td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/text-level-semantics.html#the-time-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time&gt;</span></strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Used for marking up times and dates.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-aside-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;aside&gt;</span></strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Section whose content is not necessarily directly related to the main content that surrounds it, but can provide additional information.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/grouping-content.html#the-figure-element" target="_blank"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;figure&gt;</strong></a>&nbsp;and&nbsp;<a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/grouping-content.html#the-figcaption-element" target="_blank"><br/><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;figcaption&gt;</span></strong></a></span></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Used to encapsulate a figure as a single item, and contains a caption for the figure, respectively.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-aside-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;main&gt;</span></strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The main element represents the main content of the body of a document or application. The main content area consists of content that is directly related to or expands upon the central topic of a document or central functionality of an application. <strong style="color: olive;">There can be only one <span style="font-family: 'courier new', courier;">&lt;main&gt; element in a document.</span></strong></td>
    </tr>
  </tbody>
</table>

And there is no `<content>` element even though the `<div>` was very popular. Instead, the HTML5 group decided that anything not embedded in one of the elements from the above table is "default content". If the content is of a type that corresponds to one of the elements from the table, i.e. if the content is an article, it should be embedded between `<article>` and `</article>`.

Read also at the end of this section about the new `<main>` element.  This element is [part of the HTML5 recommendation](https://tinyurl.com/y2dt6kbn) and  an integral part of the HTML document structure.


#### External resources:

+ A Smashing Magazine article: [Structural Semantics: The Importance Of HTML5 Sectioning Elements](https://tinyurl.com/yy6mubq8)
+ A Dev. Opera article: [New Structural Elements in HTML5](https://tinyurl.com/yy6mubq8)


#### Knowledge check 1.3.2

1. Which of the following is not a structural element in HTML5?<br/>
  a. nav<br/>
  b. footer<br/>
  c. title<br/>
  d. header<br/>

  Ans: c


### 1.3.3 Mixing all elements together: a blog example


#### Live coding video: a blog example

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V003200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" width=100/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y3qqqtyp)


#### A blog example that uses the structural elements

Let's study [an example we put on JsBin](https://jsbin.com/bucokav/edit?html,output) (all examples we have cooked up are available on the jsbin.com Web site and can be modified freely: you can save your own version using the "Bins/create milestone" menu, share your version with others in the forums, etc. Don't  hesitate to play with the source code, you will never break anything).

Example: [HTML code](src/1.3.3-blog.html)


#### Use a `<header>` at the top of the blog

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/yy4lq6ug" style="margin: 0.1em;" alt="image of the header element at the top of the blog" title="image of the header element at the top of the blog" width=150>
  </a>
</div>


This is an example of one way to organize a blog. Here, we have designed the HTML page using a `<header>` element that contains the "Simple HTML5 blog" text that appears on top of the page.

HTML code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&nbsp;&nbsp; &lt;html lang="en"&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;head&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;meta charset="utf-8"/&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;title&gt;Simple HTML5 blog&lt;/title&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;/head&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;body&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;header&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;h1&gt;Simple &lt;span&gt;HTML5&lt;/span&gt; blog&lt;/h1&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;/header&gt;</li>
<li>...</li>
</ol></div>


The CSS rules we used:

<div><ol>
<li value="1">header&nbsp;<span style="color: #666600;">{</span></li>
<li>&nbsp; &nbsp; color<span style="color: #666600;">:&nbsp;</span><span style="color: #880000;">#007e99;</span></li>
<li>&nbsp; &nbsp; font<span style="color: #666600;">-size</span><span style="color: #666600;">:&nbsp;</span><span style="color: #006666;">2.5em</span><span style="color: #666600;">;</span></li>
<li>&nbsp; &nbsp; padding<span style="color: #666600;">:&nbsp;</span><span style="color: #006666;">20px&nbsp;</span><span style="color: #006666;">50px</span></li>
<li><span style="color: #666600;">}</span></li>
<li>header span&nbsp;<span style="color: #666600;">{</span></li>
<li>&nbsp; &nbsp; color<span style="color: #666600;">:&nbsp;</span><span style="color: #880000;">#722</span></li>
<li><span style="color: #666600;">}</span></li>
</ol></div>


#### Use a `<nav>` for the navigation menu just below the header

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/y5w747zv" style="margin: 0.1em;" alt="image of the navigation menu" title="image of the navigation menu" width=200>
  </a>
</div>


The navigation menu just below the header is a `<nav>` element. For the purpose of this example we haven't provided any value for the hyperlinks...

HTML code:

<div><ol>
<li value="1"><span style="color: pink;">&lt;!DOCTYPE html&gt;</li>
<li><span style="color: lightblue;">&lt;html lang="en"&gt;</li>
<li><span style="color: lightblue;">&lt;head&gt;</li>
<li>&nbsp;&nbsp; &lt;meta charset="utf-8"/&gt;</li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;title&gt;Simple HTML5 blog<span style="color: lightblue;">&lt;/title&gt;</li>
<li><span style="color: lightblue;">&lt;/head&gt;</li>
<li><span style="color: lightblue;">&lt;body&gt;</li>
<li><span style="color: lightblue;">&lt;header&gt;</li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;h1&gt;Simple&nbsp;<span style="color: lightblue;">&lt;span&gt;HTML5<span style="color: lightblue;">&lt;/span&gt;&nbsp;blog<span style="color: lightblue;">&lt;/h1&gt;</li>
<li><span style="color: lightblue;">&lt;/header&gt;</li>
<li><strong style="color: olive;"><span style="color: hotpink;">&lt;nav&gt;</strong></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: lightblue;">&lt;ul&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;li&gt;&lt;span&gt;Blog&lt;/span&gt;&lt;/li&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;li&gt;&lt;a&nbsp;<span style="color: pink;">href<span style="color: #666600;">=<span style="color: #008800;">""<span style="color: lightblue;">&gt;About<span style="color: lightblue;">&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;li&gt;&lt;a&nbsp;<span style="color: pink;">href<span style="color: #666600;">=<span style="color: #008800;">""<span style="color: lightblue;">&gt;Contact<span style="color: lightblue;">&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: lightblue;">&lt;/ul&gt;</li>
<li><strong style="color: olive;"><span style="color: hotpink;">&lt;/nav&gt;</strong></li>
</ol></div>


And here is the CSS we used in this example for the `<nav>` element:

<div><ol>
<li value="1">nav&nbsp;<span style="color: #666600;">{</li>
<li>&nbsp; &nbsp; font<span style="color: #666600;">-size:&nbsp;1.5em;</span></li>
<li>&nbsp; &nbsp; margin<span style="color: #666600;">:&nbsp;5px&nbsp;0;</span></li>
<li>&nbsp; &nbsp; padding<span style="color: #666600;">:&nbsp;20px&nbsp;50px</span></li>
<li><span style="color: #666600;">}</span></li>
<li>nav li&nbsp;<span style="color: #666600;">{</span></li>
<li>&nbsp; &nbsp; display<span style="color: #666600;">:&nbsp;inline;</span></li>
<li>&nbsp; &nbsp; margin<span style="color: #666600;">:&nbsp;0&nbsp;15px</span></li>
<li><span style="color: #666600;">}</span></li>
<li>nav li<span style="color: #666600;">:first-child&nbsp;{</span></li>
<li>&nbsp; &nbsp; margin<span style="color: #666600;">-left:&nbsp;0</span></li>
<li><span style="color: #666600;">}</li>
<li><span style="color: #666600;">*&nbsp;html nav ul&nbsp;{</span></li>
<li>&nbsp; &nbsp; margin<span style="color: #666600;">-left:&nbsp;-15px</span></li>
<li><span style="color: #666600;">}</li>
<li>nav span<span style="color: #666600;">,&nbsp;nav a&nbsp;{</span></li>
<li>&nbsp; &nbsp; padding<span style="color: #666600;">:&nbsp;3px&nbsp;15px&nbsp;4px</span></li>
<li><span style="color: #666600;">}</span></li>
<li>nav span&nbsp;<span style="color: #666600;">{</span></li>
<li>&nbsp; &nbsp; background<span style="color: #666600;">:&nbsp;#722;</span></li>
<li>&nbsp; &nbsp; color<span style="color: #666600;">:#fff</span></li>
<li><span style="color: #666600;">}</span></li>
</ol></div>


#### A `<section>` for each month and an `<article>` for each post in the blog

Now, we have one big `<section>` element that contains a set of `<article>` elements...

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/y26lwg8j" style="margin: 0.1em;" alt="image of sections that contain articles" title="image of sections that contain articles" width=300>
  </a>
</div>


HTML code:

<div><ol>
<li value="1"><span style="color: lightblue;">&lt;section&gt;</span></li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;article&gt;</span></li>
<li>&nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;/article&gt;</span></li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;article&gt;</span></li>
<li>&nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;/article&gt;</span></li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;article&gt;</span></li>
<li>&nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;/article&gt;</span></li>
<li></li>
<li><span style="color: lightblue;">&lt;/section&gt;</span></li>
</ol></div>


And here is the CSS:

<div><ol>
<li value="1">section&nbsp;<span style="color: #666600;">{</span></li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">float:&nbsp;left;</span></li>
<li>&nbsp; &nbsp;padding<span style="color: #666600;">:&nbsp;35px&nbsp;0;</span></li>
<li>&nbsp; &nbsp;position<span style="color: #666600;">:&nbsp;relative;</span></li>
<li>&nbsp; &nbsp;width<span style="color: #666600;">:&nbsp;70</span>%</span></li>
<li><span style="color: #666600;">}</span></li>
<li>section article&nbsp;<span style="color: #666600;">{</span></li>
<li>&nbsp; &nbsp;margin<span style="color: #666600;">:&nbsp;0&nbsp;50px&nbsp;40px;</span></li>
<li>&nbsp; &nbsp;padding<span style="color: #666600;">:&nbsp;25px&nbsp;0&nbsp;0;</span></li>
<li>&nbsp; &nbsp;position<span style="color: #666600;">:&nbsp;relative</span></li>
<li><span style="color: #666600;">}</span></li>
<li>section header&nbsp;<span style="color: #666600;">{</span></li>
<li>&nbsp; &nbsp;font<span style="color: #666600;">-size:&nbsp;1em;</span></li>
<li>&nbsp; &nbsp;padding<span style="color: #666600;">:&nbsp;0;</span></li>
<li><span style="color: #666600;">}</span></li>
<li>section h2&nbsp;<span style="color: #666600;">{</span></li>
<li>&nbsp; &nbsp;font<span style="color: #666600;">-size:&nbsp;2.3em;</span></li>
<li><span style="color: #666600;">}</span></li>
</ol></div>


Note that the H2, article, article header, etc. will be styled using these rules.


#### Add a `<header>` at the beginning of each `<article>`

<figure style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <img style="margin: 0.1em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5ug9vol')"
    src  ="https://tinyurl.com/yye6m9f5"
    alt  ="image of the header at the top of each article"
    title="image of the header at the top of each article"
  />
</figure>


Next, in each article in the section we have a header (to display the article title), paragraphs (article content), and so on.

Example for the first blog article:

<div><ol>
<li value="1"><span style="color: lightblue;">&lt;section&gt;</span></li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;article&gt;</span></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;header&gt;</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;h2&gt;&lt;a&nbsp;<span style="color: pink;">href</span><span style="color: #666600;">=</span><span style="color: #008800;">""</span><span style="color: lightblue;">&gt;Information about this example</span><span style="color: lightblue;">&lt;/a&gt;&lt;/h2&gt;</span></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;/header&gt;</span></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;p&gt;</span>Try to move the mouse on different elements. The structure will be </li>
<li>&nbsp; &nbsp; &nbsp;highlighted&nbsp;and you will be able</li>
<li>&nbsp; &nbsp; &nbsp;to see the different inclusions of elements one in each other. If you </li>
<li>&nbsp; &nbsp; &nbsp;move the&nbsp;cursor to this sentence,&nbsp;it will be highlighted in dark grey, </li>
<li>&nbsp; &nbsp; &nbsp;showing the&nbsp;presence of an &amp;lt;<span style="color: lightblue;">article&amp;gt; element,&nbsp;surrounded by a</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&amp;lt;section</span><span style="color: lightblue;">&amp;gt; element (light grey), etc. So we have some articles in </li>
<li>&nbsp; &nbsp; &nbsp;a single section&nbsp;element. The page&nbsp;title at the top is a&nbsp;<span style="color: lightblue;">&amp;lt;header<span style="color: lightblue;">&amp;gt; <br></li>
<li>&nbsp; &nbsp; &nbsp;element, while the tag cloud on the right is a&nbsp;<span style="color: lightblue;">&amp;lt;aside<span style="color: lightblue;">&amp;gt; element. The</li>
<li>&nbsp; &nbsp; &nbsp;main menu on top (with Blog, About, Contact) is a&nbsp;<span style="color: lightblue;">&amp;lt;nav<span style="color: lightblue;">&amp;gt; element.<span style="color: lightblue;">&lt;/p&gt;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;figure&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;img&nbsp;</span><span style="color: pink;">src</span><span style="color: #666600;">=</span><span style="color: #008800;">"<span style="color: #008800;">HTML5-tags.png"</span></li>
<li><span style="color: pink;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;alt<span style="color: #666600;">=<span style="color: #008800;">"Example of HTML5 structural <span style="line-height: 1.6; background-color: #ffffff;">tags"<span style="line-height: 1.6; background-color: #ffffff;">&nbsp;<span style="line-height: 1.6; background-color: #ffffff;">/&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;figcaption&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Fig. 1 : an example of how new structural elements could </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;be used. This&nbsp;page put a &amp;lt;<span style="color: lightblue;">nav</span><span style="color: lightblue;">&amp;gt;</span> on top, and&nbsp;does not have</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;headers and footer for each&nbsp;article, like in this figure,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;but it could... By the way&nbsp;this is a</li>
<li><span style="color: lightblue;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; <span style="color: lightblue;">&amp;lt;figcaption</span><span style="color: lightblue;">&amp;gt; inside a&nbsp;</span><span style="color: lightblue;">&amp;lt;figure</span><span style="color: lightblue;">&amp;gt; element...</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;/figcaption&gt;</span></li>
<li><span style="color: lightblue;">&nbsp; &nbsp; &lt;/figure&gt;</span></li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;/article&gt;</span></li>
<li>&nbsp; &nbsp;...</li>
<li><span style="color: lightblue;">&lt;/section&gt;</span></li>
</ol></div>


#### Use `<figure>` and `<figcaption>` and embed `<img>` inside

Also note the way we included a figure using the new "HTML5" method, using a `<figure>..</figure>` element that embedded a `<img src=.../>` element together with a `<figcaption>` element. 

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/yxktruxu" style="margin: 0.1em;" alt="image of figure and figcaption that embed an img" title="image of figure and figcaption that embed an img" width=350>
  </a>
</div>

Here is the CSS for the `<figcaption>` element we have used in the example (we did not apply any style to the `<figure>` element):

HTML code:

<div><ol>
<li value="1"> &lt;figure&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;img src="<span style="color: #008800;"><span style="color: #008800;"><span style="color: #008800;">HTML5-tags.png" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;alt="Example of HTML5 structural tags" /&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;figcaption&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; Fig. 1 : an example of how .....</li>
<li>&nbsp; &nbsp; &lt;/figcaption&gt;</li>
<li>&lt;/figure&gt;</li>
</ol></div>


CSS code:

<div><ol>
<li value="1">figcaption&nbsp;<span style="color: #666600;">{</li>
<li>&nbsp; &nbsp; font<span style="color: #666600;">-style:italic;</span></li>
<li>&nbsp; &nbsp; font<span style="color: #666600;">-size:&nbsp;0.8em;</span></li>
<li>&nbsp; &nbsp; width<span style="color: #666600;">:&nbsp;100%</span></li>
<li><span style="color: #666600;">}</span></li>
</ol></div>


#### Use an `<aside>` element to display a tag cloud on the ... side of the main content

After the long `<section>` element that contains all the blog articles displayed in the page, we added the HTML code for the tag cloud that is displayed on the right of the page, "aside"! This is done using - you already guessed it - an `<aside>` element:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/y2x3vtng" style="margin: 0.1em;" alt="image of the tag cloud defined as an aside element" title="image of the tag cloud defined as an aside element" width=150>
  </a>
</div>


<div><ol>
<li value="1"><span style="color: lightblue;">&lt;section&gt;</li>
<li>.... all&nbsp;<span style="color: lightblue;">&lt;article&gt;...&nbsp;&lt;/article&gt;&nbsp;here....</span></li>
<li><span style="color: lightblue;">&lt;/section&gt;</li>
<li><strong style="color: olive;"><span style="color: hotpink;">&lt;aside&gt;</strong></span></li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;h2&gt;Tag cloud</span><span style="color: lightblue;">&lt;/h2&gt;</span></li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;ul&nbsp;<span style="color: pink;">class<span style="color: #666600;">=<span style="color: #008800;">"tag-cloud"<span style="color: lightblue;">&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;li&gt;&lt;a&nbsp;<span style="color: pink;">href<span style="color: #666600;">=<span style="color: #008800;">""&nbsp;<span style="color: pink;">rel<span style="color: #666600;">=<span style="color: #008800;">"tag"&nbsp;<span style="color: pink;">class<span style="color: #666600;">=<span style="color: #008800;">"w2"<span style="color: lightblue;">&gt;ajax<span style="color: lightblue;">&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;li&gt;&lt;a&nbsp;<span style="color: pink;">href<span style="color: #666600;">=<span style="color: #008800;">""&nbsp;<span style="color: pink;">rel<span style="color: #666600;">=<span style="color: #008800;">"tag"&nbsp;<span style="color: pink;">class<span style="color: #666600;">=<span style="color: #008800;">"w8"<span style="color: lightblue;">&gt;apple<span style="color: lightblue;">&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: lightblue;">&lt;li&gt;&lt;a&nbsp;<span style="color: pink;">href<span style="color: #666600;">=<span style="color: #008800;">""&nbsp;<span style="color: pink;">rel<span style="color: #666600;">=<span style="color: #008800;">"tag"&nbsp;<span style="color: pink;">class<span style="color: #666600;">=<span style="color: #008800;">"w3"<span style="color: lightblue;">&gt;css<span style="color: lightblue;">&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;/ul&gt;</li>
<li><strong style="color: olive;"><span style="color: hotpink;">&lt;/aside&gt;</strong></li>
<li>...</li>
</ol></div>


We are not going to show the complete CSS here as it uses some tricks to display the list as a "real tag cloud" that uses JavaScript for handling events, etc. Those who are curious can look at the code of the online example.

Here is the CSS for the `<aside>` element:

<div><ol>
<li value="1">aside&nbsp;<span style="color: #666600;">{</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: lightblue;">float<span style="color: #666600;">:&nbsp;right<span style="color: #666600;">;</li>
<li>&nbsp; &nbsp; padding<span style="color: #666600;">:&nbsp;<span style="color: #006666;">70px&nbsp;<span style="color: #006666;">0&nbsp;<span style="color: #006666;">30px<span style="color: #666600;">;</li>
<li>&nbsp; &nbsp; position<span style="color: #666600;">:&nbsp;relative<span style="color: #666600;">;</li>
<li>&nbsp; &nbsp; width<span style="color: #666600;">:&nbsp;<span style="color: #006666;">25<span style="color: #666600;">%</li>
<li><span style="color: #666600;">}</li>
<li></li>
<li>aside h2&nbsp;<span style="color: #666600;">{</li>
<li>&nbsp; &nbsp; color<span style="color: #666600;">:&nbsp;<span style="color: #880000;">#888;</li>
<li>&nbsp; &nbsp; font<span style="color: #666600;">-size<span style="color: #666600;">:&nbsp;<span style="color: #006666;">1.8em</li>
<li><span style="color: #666600;">}</li>
<li>aside&nbsp;<span style="color: #666600;">.tag<span style="color: #666600;">-cloud&nbsp;<span style="color: #666600;">{</li>
<li>&nbsp; &nbsp; padding<span style="color: #666600;">:&nbsp;<span style="color: #006666;">15px&nbsp;<span style="color: #006666;">35px&nbsp;<span style="color: #006666;">10px&nbsp;<span style="color: #006666;">0<span style="color: #666600;">;</li>
<li>&nbsp; &nbsp; text<span style="color: #666600;">-align<span style="color: #666600;">:&nbsp;center</li>
<li><span style="color: #666600;">}</li>
<li><span style="color: #666600;">...</li>
</ol></div>


We used a `float:right` CSS rule to put the tag cloud on the right... In a following section we will provide several examples that explain how to make a nice layout with the new structural elements, using simple CSS rules.

Here is the result:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/y6rhtxvq" style="margin: 0.1em;" alt="The aside tag cloud on the right" title="The aside tag cloud on the right" width=450>
  </a>
</div>



#### Add a `<footer>` at the end of the blog

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/yy32q5zh" style="margin: 0.1em;" alt="image of the blog footer" title="image of the blog footer" width=150>
  </a>
</div>

Finally, we added a `<footer>` element (lines 12-14 below) after the tag cloud definition, to display a page footer:

<div><ol>
<li value="1"><span style="color: lightblue;">&lt;html&gt;</li>
<li>...</li>
<li><span style="color: lightblue;">&lt;body&gt;</li>
<li>...</li>
<li><span style="color: lightblue;">&lt;section&gt;</li>
<li>...</li>
<li><span style="color: lightblue;">&lt;/section&gt;</li>
<li><span style="color: lightblue;">&lt;aside&gt;</li>
<li>...</li>
<li><span style="color: lightblue;">&lt;/aside&gt;</li>
<li></li>
<li><span style="color: hotpink;">&lt;footer&gt;</li>
<li>&nbsp; &nbsp;<span style="color: lightblue;">&lt;p&gt;&amp;copy; 2009 Some blog<span style="color: lightblue;">&lt;/p&gt;</li>
<li><span style="color: hotpink;">&lt;/footer&gt;</li>
<li></li>
<li><span style="color: lightblue;">&lt;/body&gt;</li>
<li><span style="color: lightblue;">&lt;/html&gt;</li>
</ol></div>


With this CSS rule:

<div><ol>
<li value="1">footer&nbsp;<span style="color: #666600;">{</li>
<li>&nbsp; &nbsp; clear<span style="color: #666600;">:&nbsp;both<span style="color: #666600;">;</li>
<li>&nbsp; &nbsp; color<span style="color: #666600;">:&nbsp;<span style="color: #880000;">#777;</li>
<li>&nbsp; &nbsp; padding<span style="color: #666600;">:&nbsp;<span style="color: #006666;">10px&nbsp;<span style="color: #006666;">50px</li>
<li><span style="color: #666600;">}</li>
</ol></div>


And here is the result at the bottom of the page:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/y654dvkp" style="margin: 0.1em;" alt="The resulting footer at the bottom of the page" title="The resulting footer at the bottom of the page" width=350>
  </a>
</div>



#### Knowledge check 1.3.3

1. What is a figcaption?<br/>
  a. An image link<br/>
  b. A caption under a figure<br/>
  c. A tool for catching figs<br/>
  d. A tool for taking a selfie<br/>

  Ans: b


### 1.3.4 More on `<article>` and `<section>`


#### Can an `<article>` contain a `<section>`?

It may not be clear whether a `<section>` may contain one or several `<article>` elements or if an `<article>` may contain one or several `<section>` elements.

+ The `<article>` element was designed for stand-alone parts of a document that could eventually be syndicated in RSS streams.
+ `<section>` elements are used to cut a logical part into subparts.

<div style="margin-left: 1.0em;">
  <p><strong style="color: olive;"><span style="font-size: 1em; line-height: 1.6em;">An </span><span style="font-family: 'courier new', courier;">&lt;article&gt; may be cut into different </span><span style="font-family: 'courier new', courier;">&lt;section&gt; elements!</span></strong></p>
</div>

Example of a blog post defined as a long `<article>`, that is in turn cut into smaller `<section>` elements:

<div><ol>
<li value="1">&lt;article id="id1"&gt; </li>
<li> </li>
<li>&nbsp; &nbsp;&lt;section id="id1part1"&gt; </li>
<li>&nbsp; &nbsp; &nbsp;&lt;h2&gt;Introduction&lt;/h2&gt; </li>
<li>&nbsp; &nbsp;&lt;/section&gt; </li>
<li> </li>
<li>&nbsp; &nbsp;&lt;section id="id1part2"&gt; </li>
<li>&nbsp; &nbsp; &nbsp;&lt;h2&gt;My travel to India&lt;/h2&gt; </li>
<li>&nbsp; &nbsp;&lt;/section&gt; </li>
<li> </li>
<li>&nbsp; &nbsp;&lt;section id="id1part3"&gt; </li>
<li>&nbsp; &nbsp; &nbsp;&lt;h2&gt;Return to France&lt;/h2&gt; </li>
<li>&nbsp; &nbsp;&lt;/section&gt; </li>
<li> </li>
<li>&lt;/article&gt;</li>
</ol></div>


The blog example from the previous part of the course, on the other hand, uses a single `<section>` that contains several `<article>` elements.

Indeed, we can also have a `<section>` that regroups all blog posts per month, each one being an `<article>` element.

<div style="margin-left: 1.0em;">
  <p><strong style="color: olive;"><span style="line-height: 25.6px;">A&nbsp;&lt;section&gt; may be cut into different </span><span style="font-family: 'courier new', courier;">&lt;article&gt; elements, too!</span></strong></p>
</div>


#### Can you put a `<nav>` in an `<article>`?

Yes you can, in case you would like to propose some navigation links with each blog post, for example:

<div><ol>
<li value="1">&lt;article&gt;</li>
<li>&nbsp; &nbsp;&lt;header&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;h1&gt;Blog post title&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;p&gt;Author: Michel&lt;/p&gt;</li>
<li>&nbsp; &nbsp;&lt;/header&gt;</li>
<li>&nbsp; &nbsp;<strong style="color: olive;"><span style="color: hotpink;">&lt;nav&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: olive;"><span style="color: hotpink;">&lt;ul&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: hotpink;">&lt;li&gt;&lt;a href="..."&gt;Next post&lt;/a&gt;&lt;/li&gt;</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;li&gt;&lt;a href="..."&gt;Previous post&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;li&gt;&lt;a href="..."&gt;Contact author&lt;/a&gt;&lt;/li&gt; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: olive;"><span style="color: hotpink;">&lt;/ul&gt;</strong></li>
<li>&nbsp; &nbsp;<strong style="color: olive;"><span style="color: hotpink;">&lt;/nav&gt;</strong></li>
<li>&nbsp; &nbsp;&lt;p&gt;Content...&lt;/p&gt;</li>
<li>&nbsp; &nbsp;&lt;footer&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;p&gt;Posted by Michel, the &lt;time datetime="2012-02-02"&gt;February 2, <br></li>
<li>&nbsp; &nbsp; &nbsp;2012&lt;/time&gt; &lt;/p&gt;</li>
<li>&nbsp; &nbsp;&lt;/footer&gt;</li>
<li>&lt;/article&gt;</li>
</ol></div>


In  that case, the `<nav>` element proposes navigation links to the next or previous blog post, as well as a link to contact the author of the blog post.

Also note that we used in that example a `<footer>` element in the blog post.


#### What about the `<div>` element? Is it still useful?

The new elements have been primarily designed to better structure the code of HTML pages such as those generated by blog or CMS software, however do not forget that they add new semantics and will be taken into account by :

+ Browsers natively or browsers' extensions, i.e. for automatically generating a table of contents, an outline view of the document, for applying default CSS rules to these elements, etc. See for example the [table-of-contents-crx extension](https://tinyurl.com/y4em5khm) (Chrome extension). More on that in the next section of the course.
+ Text to speech: https://www.w3.org/WAI/perspective-videos/speech/
+ Web crawlers, etc.

You can use `<div>` elements in all cases where the proposed structural elements do not fit your needs: for defining some content that should be styled, for example.

This chart from the HTML5 Doctor Web site may help you decide whether or not to use a `<div>`:

<figure style="text-align: center; margin: 0.5em;">
  <img style="margin: 0.1em; padding-top: 0.3em; width: 50vw;"
    onclick="window.open('https://tinyurl.com/y5ug9vol')"
    src    ="https://tinyurl.com/y6sshtgc"
    alt    ="flow chart about using header, H1, etc."
  >
  <figcaption>Flow chart about using header, H1, etc.</figcaption>
</figure>


#### Knowledge check 1.3.4

1. Can a section contain an article? (Yes/No)

  Ans: Yes


### 1.3.5 Headings and structural elements

Update: In the video below, Michel presents the Chrome extension "HTML5 Outliner". This extension has been removed since from the Chrome Web store.

There are many other equivalent browser extensions you can install instead of the one presented in the video and screenshots. For example, there are the [table-of-contents-crx](https://tinyurl.com/y4em5khm) for Chrome and the "[Outline sidebar](https://tinyurl.com/y2bw2stx)" for Firefox.


#### Live coding video: headings, TOC, etc.

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V003400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" width=150/>
</a><br/>

[Transcript](https://tinyurl.com/y39lft4n)

We will now present some best practices for starting to use `<section>`, `<article>`, `<nav>`, `<aside>`, in particular concerning the use of headings (h1, h2, h3, h4, h5 and h6).


#### Use `<h1>...<h6>` for the headings

Since the very beginning, HTML has had heading elements: `<h1>...<h6>`. These elements are used to display headings with different sizes by default, when no CSS is used.  The following example shows 6 sentences that are surrounded by `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>` and `<h6>`:

<div style="border: 1px solid black; margin: 20px; padding: 20px;">
  <h1>This is a H1 heading</h1>
  <h2>This is a H2 heading</h2>
  <h3>This is a H3 heading</h3>
  <h4>This is a H4 heading</h4>
  <h5>This is a H5 heading</h5>
  <h6>This is a H6 heading</h6>
</div>

These headings define a hierarchy, as shown by the default sizes given by the browser. This hierarchy can also be used to define an outline of the document. To illustrate this, we have used a browser extension. Here is the result for the previous example:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5ug9vol')"
    src    ="https://tinyurl.com/yxrh335h"
    alt    ="outliner in action from the previous example"
    title  ="outliner in action from the previous example"
  />
</figure>


In the above outline, note that we have only used H1... H6 elements, without any new HTML5 structural elements such as `<section>` or `<article>`.

Here is a list of browser extensions you can try, for visualizing the outline of a document: [table-of-contents-crx](https://tinyurl.com/y4em5khm) Chrome extension or [this Firefox extension](https://tinyurl.com/y2bw2stx).


#### Using headings and new sectioning elements (`section`, `article`, `aside`, `nav`)

__Definition of heading content and sectioning content__

The `<section>`, `<article>`, `<nav>` and `<aside>` elements are called "__sectioning elements__". They cut a document into slices we call "__sections__".

The HTML5 specification says that "each sectioning element potentially has a heading and has also an outline associated".

`<h1>...<h6>` are called __headings__, and define the header of a section (whether explicitly marked up using sectioning content elements, or implied by the heading content itself). This means that:

<div><ol>
<li value="1">&lt;body&gt;</li>
<li>&nbsp; &nbsp; &lt;h1&gt;Title of my document&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; ...</li>
<li>&lt;/body&gt;</li>
</ol></div>


... defines the header of a section implicitly, while:

<div><ol>
<li value="1">&lt;body&gt;</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;&lt;section&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;h1&gt;Title of my section&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp;&lt;/section&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>

... defines the heading of the explicit section (its parent element `<section>`).


#### Use multiple headings of different rank with sectioning content

The first element of a heading content in an element of sectioning content represents the heading for that section (the `<section><h1>...</h1></section>` in the above example).

Subsequent headings of equal or higher rank start new (implied) sections, headings of lower rank start implied subsections that are part of the previous one. In both cases, the element represents the heading of the implied section.

Let's clarify this by looking at some example code:

<div><ol>
<li value="1">&lt;body&gt;</li>
<li> &lt;section&gt;</li>
<li>&nbsp; &nbsp; &lt;h1&gt;This H1 is the heading of an explicit section&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;h2&gt;This H2 is a subheading, part of the same section </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;(lower rank)&lt;/h2&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ....</li>
<li>&nbsp; &nbsp; &lt;h1&gt;This H1 starts an implicit new section in the explicit </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; section (equal or higher rank)&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;h2&gt;This is a H2 heading in the new section that has </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; just started&lt;/h2&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ...</li>
<li> &lt;/section&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>


The corresponding outline is:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5ug9vol')"
    src    ="https://tinyurl.com/yxjobfw3"
    alt    ="outline of previous example"
    title  ="outline of previous example"
  />
</figure>

In the above example, please note two things:

1. The outline shows an "Untitled body" at the root of the hierarchy,
2. The default size for the H1 and H2 is the same (!). Indeed, when we start a `<h1>` inside a `<section>` the browser lowers its default size automatically, as if a new hierarchy level has been added artificially. We will discuss this further in the following sections, as we introduce some best practices.


#### Knowledge check 1.3.5

1. Before HTML5, how many levels of headings were available?<br/>
  a. 7<br/>
  b. 5<br/>
  c. 6<br/>
  d. 4<br/>

  Ans: c


### 1.3.6 Best practices when using sectioning elements

__<mark style="color: black; background-color: lightpink;">Best practice #1</mark>: always add a heading to explicit sectioning content__

It's always better - mainly for accessibility reasons - to include a heading (a `<h1>, <h2>...<h6>`) in each sectioning element (`<section>`, `<article>`, `<nav>`, `<aside>`), but also after the `<body>` element (called a "sectioning root").

Here are some examples:

__Good (heading in each explicit section)__:

<div><ol>
<li value="1">&lt;section&gt;</li>
<li>&nbsp; &nbsp; <strong style="color: olive;">&lt;h1&gt;</strong><strong style="color: olive;">Blog post of April 2020&lt;/h1&gt;</strong></li>
<li>&nbsp; &nbsp; ...</li>
<li>&lt;/section&gt;</li>
</ol></div>


__Good (heading  in a `<header>` does not change anything)__

<div><ol>
<li value="1">&lt;section&gt;</li>
<li>&nbsp; &nbsp;<strong style="color: olive;">&lt;header&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong style="color: olive;">&lt;h1&gt;</strong><strong style="color: olive;">Blog post of April 2020&lt;/h1&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong style="color: olive;">&lt;p&gt;</strong><strong style="color: olive;">Posted by Michel Buffa...&lt;/p&gt;</strong></li>
<li>&nbsp; &nbsp;<strong style="color: olive;">&lt;/header&gt;</strong></li>
<li>...</li>
<li>&lt;/section&gt;</li>
</ol></div>


__Bad (there is no Hx after the `<section>` -> no heading)__:

<div><ol>
<li value="1">&lt;section&gt;</li>
<li>&nbsp; &nbsp;&lt;header&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;p class="article title"&gt;Blog post of April 2020&lt;/p&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;p&gt;Posted by Michel Buffa...&lt;/p&gt;</li>
<li>&nbsp; &nbsp;&lt;/header&gt;</li>
<li>&nbsp; &nbsp;...</li>
<li>&lt;/section&gt;</li>
</ol></div>


The last example is bad for accessibility reasons. A screen reader that vocalizes the page will just say "Entering section", while in the previous two good examples it would say "entering section with heading Blog Posts of April 2020". You can also check if your headings and sectioning elements are ok by using a browser extension that displays the outline of the document (just search for "html5 outliner" in your browser's extension search engine).

__UPDATE__: For the course screenshots, we used the Google Chrome HTML5 outliner extension that is no more available (it has been removed by its developer), but you can use any other equivalent extension such as [table-of-contents-crx](https://tinyurl.com/y4em5khm) for Chrome or [Outline sidebar](https://tinyurl.com/y2bw2stx) for Firefox.

The outline of the last example looks like this:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5ug9vol')"
    src    ="https://tinyurl.com/y33dqxrw"
    alt    ="outline of last example"
    title  ="outline of last example"
  />
</figure>


Notice that <body> is also a sectioning element. It's called a "sectioning root", and would also need a heading.

Final good version:

<div><ol>
<li value="1"> <span style="color: hotpink;">&lt;body&gt;</li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: olive;">&lt;h1&gt;Example Blog&lt;/h1&gt;</strong></li>
<li>&nbsp; &nbsp; <span style="color: hotpink;">&lt;section&gt;</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;header&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong style="color: olive;">&lt;h2&gt;Blog post of April 2020&lt;/h2&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&lt;p&gt;Posted by Michel Buffa...&lt;/p&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;/header&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;p&gt;Content of the blog post...&lt;/p&gt;</li>
<li>&nbsp; &nbsp;&lt;/section&gt;</li>
<li> &lt;/body&gt;</li>
</ol></div>


In red, the sectioning root (`<body>`) and the sectioning elements (`<section>` here...), each have a heading.

__To sum up:__
+ Always use a heading element after a sectioning element, for example `<section><Hx>...</Hx>...</section>`, and after `<body>`, where x can be 1..6,
+ Or, use a `<header>` element, like in `<section><header><Hx>...</Hx>.....</header>...</section>`


#### More about the `<header>` element

__The `<header>` element is just a container. It is not taken into account for defining new sections of a document nor does it affect the hierarchy levels.__

You can use heading elements `<h1>...<h6>` in a `<header>` but be careful if you use more than one, as the rules explained in the previous part of the course will apply and may generate implicit "sections" in the header.

This example has two headings in the `<header>`:

<div style="line-height: 23.2727279663086px;"><ol>
<li value="1">&lt;section&gt;</li>
<li>&nbsp; &nbsp;&lt;header&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;h1&gt;Some text in a h1 in a header of a section&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: hotpink;">&lt;h2&gt;This a h2 in the header...&lt;/h2&gt;</span></li>
<li>&nbsp; &nbsp;&lt;/header&gt;</li>
<li>&lt;/section&gt;</li>
</ol></div>


Here is the resulting table of contents, notice the two subsections that appear, one for the H1, one for the H2:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5ug9vol')"
    src    ="https://tinyurl.com/y3ezx2r8"
    alt    ="Example of table of contents"
    title  ="Example of table of contents"
  />
</figure>

Indeed, HTML does not have a dedicated mechanism for marking up subheadings, alternative titles or taglines. 

If you do not want the subtitles to be included in the table of contents, just use standard markup, for example <p> elements, as shown in the next example. Of course, CSS rules can be applied to change colors, sizes, etc.

<div><ol>
<li value="1">&lt;header&gt;</li>
<li>&nbsp; &nbsp; &lt;h1&gt;HTML 5.1 Nightly&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; &lt;p&gt;A vocabulary and associated APIs for HTML and XHTML&lt;/p&gt;</li>
<li>&nbsp; &nbsp; &lt;p&gt;Editor's Draft 9 May 2013&lt;/p&gt;</li>
<li>&lt;/header&gt;</li>
</ol></div>


__<mark style="color: black; background-color: lightpink;">Best practice #2</mark>: try not to rely on implicit sectioning, use `<section>`, `<article>`, etc. instead of just `<h1>...<h6>`__

The example below defines several implicit "sections" by using `<Hx>` directly (at lines 7 and 9):

Ok version (no explicit sections everywhere):

<div><ol>
<li value="1">&lt;body&gt;</li>
<li> <strong style="color: olive;">&lt;h4&gt;Apples&lt;/h4&gt;</strong></li>
<li> &lt;p&gt;Apples are fruit.&lt;/p&gt;</li>
<li> &lt;section&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;h2&gt;Taste&lt;/h2&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;p&gt;They taste lovely.&lt;/p&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;h6&gt;Sweet&lt;/h6&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;p&gt;Red apples are sweeter than green ones.&lt;/p&gt;</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h1&gt;Color&lt;/h1&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp;&lt;p&gt;Apples come in various colors.&lt;/p&gt;</li>
<li> &lt;/section&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>


Better version (best practice):

<div><ol>
<li value="1">&lt;body&gt;</li>
<li> &lt;h1&gt;Apples&lt;/h1&gt;</li>
<li> &lt;p&gt;Apples are fruit.&lt;/p&gt;</li>
<li> <strong style="color: olive;">&lt;section&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h2&gt;Taste&lt;/h2&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp;&lt;p&gt;They taste lovely.&lt;/p&gt;</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;section&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h3&gt;Sweet&lt;/h3&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;p&gt;Red apples are sweeter than green ones.&lt;/p&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;/section&gt;</li>
<li> &lt;/section&gt;</li>
<li> <strong style="color: olive;">&lt;section&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h2&gt;Color&lt;/h2&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp;&lt;p&gt;Apples come in various colors.&lt;/p&gt;</li>
<li> &lt;/section&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>


Both of the examples above are semantically identical and produce the same outline:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5ug9vol')"
    src    ="https://tinyurl.com/y6jg6qla"
    alt    ="outline of previous examples"
    title  ="outline of previous examples"
  />
</figure>


#### Knowledge check 1.3.6

<div>
      <ol>
        <li value="1" style="margin-bottom:0px;">
          &lt;section&gt;
        </li>
        <li style="margin-bottom:0px;">
          &lt;header&gt;
        </li>
        <li style="margin-bottom:0px;">   
          &lt;p
          class
          =
          "article title"
          &gt;
          Blog post of April 2020
          &lt;/p&gt;
        </li>
        <li style="margin-bottom:0px;">
          &lt;p&gt;
          Posted by Michel Buffa...
          &lt;/p&gt;
        </li>
        <li style="margin-bottom:0px;">
          &lt;/header&gt;
        </li>
        <li style="margin-bottom:0px;">
             ...
        </li>
        <li style="margin-bottom:0px;">
          &lt;/section&gt;
        </li>
      </ol>
  </div>

1. Does this example follow the best practices presented in this section of the course? (Yes/No)

  Ans: No<br/>
  Explanation: No, the section is not followed by at least one heading (in the header element)


### 1.3.7 Embedding a table of contents

Here we propose a small piece of JavaScript code you can use in your documents to display an embedded table of contents. 

This example is a simple document, with a hyperlink that, once clicked, displays the table of contents in an `<aside>` element in the main `<section>`. Just look at the source code and copy/paste the link into your own HTML documents.

[Online example at JsBin.](https://tinyurl.com/y3ab6zow)

[Local example](src/1.3.7-toc.html)

Extract of source code:
<div><ol>
<li value="1">&lt;body&gt;</li>
<li>&lt;h1&gt;This is an example of embedded table of content&lt;/h1&gt;</li>
<li> &lt;section&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;header&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;h1&gt;First section of the document (this is a h1)&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;This is a subheading...</li>
<li>&nbsp; &nbsp; &nbsp;&lt;/header&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;h2&gt;First subsection of the first section (a h2)&lt;/h2&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;p&gt;Blah Blah...&lt;/p&gt;</li>
<li>&nbsp;&lt;/section&gt;</li>
<li> &lt;section&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;h1&gt;Second section of the document (a h1)&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;h2&gt;First subsection (a h2)&lt;/h2&gt;</li>
<li> &lt;/section&gt;</li>
<li> &lt;aside&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;h3&gt;Table of contents&lt;/h3&gt;</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;a href="javascript:(function(){...})();" </strong></li>
<li><strong style="color: olive;">&nbsp; &nbsp; &nbsp; &nbsp; title="TableDeMatiere"&gt;</strong></li>
<li><strong style="color: olive;">&nbsp; &nbsp; &nbsp; &nbsp; Click here to display the table of contents!</strong></li>
<li><strong style="color: olive;">&nbsp; &nbsp; &nbsp;&lt;/a&gt;</strong></li>
<li> &lt;/aside&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>


__Best practice__: visualizing the table of contents is useful for debugging the structure of your page, and checking the presence of headings after sectioning content.

Indeed, tools that generate the table of contents are a good way to debug the structure of your page. Is the hierarchy correct? Is it what I wanted when I designed my page?

They are also useful for checking the presence of headings in each sectioning content. If some headings are missing, the table of contents will display some "untitled entries". Remember that having a heading after each sectioning content is a good practice in terms of accessibility.

#### Knowledge check 1.3.7

<div class="wrapper-problem-response" tabindex="-1" aria-label="Question 1" role="group"><pre>
1. Simple HTML5 blog
2. Blog posts for April 2020
  1. Information about this example
  2. History
  3. HTML vs XHTML
  4. Untitled SECTION
3. Tag cloud
</pre></div>


1. Is this outline ideal? (No/Yes)

  Ans: No <br/>
  Explanation: No, there is one untitled entry, meaning that a heading is missing.


### 1.3.8 The `<main>` element

If you use `<nav>` / `<header>` / `<footer>` etc. to structure your document, you can also use `<main>` to identify the main content of the document. Doing so provides a navigable document structure for assistive technology users as well as styling hooks for devs.

We have seen the different sectioning elements of HTML5, so why didn't we talk about the `<main>` element earlier in this part of the course? Shouldn't  `<main>...</main>` be used in place of  `<div>...</div>`?

The `<main>` element is supported by major modern browsers (see the corresponding [support table](https://tinyurl.com/yyvj2uf6) on CanIUse and [MDN's brower compatibility page](https://tinyurl.com/q5dwuwe)).

This element is subject to some constraints:

There must not be more than one `<main>` element in a document,

+ It must not be a descendant of an `<article>`,`<aside>`, `<footer>`, `<header>`, or `<nav>` element.
+ And finally, here are some examples (from [the HTML5 specification](https://tinyurl.com/y2dt6kbn))  that mix the `<main>` element with the other sectioning elements already seen in the course:

<div><ol>
<li value="1">&lt;!-- other content --&gt;</li>
<li> </li>
<li>&lt;main&gt;</li>
<li> </li>
<li>&nbsp; &nbsp;&lt;h1&gt;Skateboards&lt;/h1&gt;</li>
<li>&nbsp; &nbsp;&lt;p&gt;The skateboard helps kids to get around.&lt;/p&gt;</li>
<li> </li>
<li>&nbsp; &nbsp;&lt;article&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;h2&gt;Longboards&lt;/h2&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;p&gt;Longboards are a type of skateboard with a longer </li>
<li>wheelbase and larger, softer wheels.&lt;/p&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;p&gt;... &lt;/p&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;p&gt;... &lt;/p&gt;</li>
<li>&nbsp; &nbsp;&lt;/article&gt;</li>
<li> </li>
<li>&nbsp; &nbsp;&lt;article&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;h2&gt;Electric Skateboards&lt;/h2&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;p&gt;These no longer require the propelling of the skateboard by means of the feet; rather an electric motor propels the board, fed by an electric battery.&lt;/p&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;p&gt;... &lt;/p&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;p&gt;... &lt;/p&gt;</li>
<li>&nbsp; &nbsp;&lt;/article&gt;</li>
<li> </li>
<li>&lt;/main&gt;</li>
<li>&nbsp;</li>
<li>&lt;!-- other content --&gt;</li>
</ol></div>


Here is another example (also from the specification). Here the `<main>` element contains a `<nav>` element consisting of links to subsections of the main content:

<div><ol>
<li value="1"> &lt;!DOCTYPE html&gt;</li>
<li>&nbsp;&nbsp; &lt;html lang="en"&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;head&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;meta charset="utf-8"/&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;title&gt;Graduation Ceremony Summer 2022&lt;/title&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;/head&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;body&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &lt;header&gt;The Lawson Academy:</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;nav&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;h2&gt;Click these links to navigate...&lt;/h2&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;ul&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;&lt;a href="courses.html"&gt;Courses&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;&lt;a href="fees.html"&gt;Fees&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;&lt;a&gt;Graduation&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;/ul&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;/nav&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;/header&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;main&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;h1&gt;Graduation&lt;/h1&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;nav&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;h2&gt;Please choose:&lt;/h2&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;ul&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;&lt;a href="#ceremony"&gt;Ceremony&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;&lt;a href="#graduates"&gt;Graduates&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;&lt;a href="#awards"&gt;Awards&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;/ul&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;/nav&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;h2 id="ceremony"&gt;Ceremony&lt;/h2&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;p&gt;Opening Procession&lt;/p&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;p&gt;Speech by Valedictorian&lt;/p&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;p&gt;Speech by Class President&lt;/p&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;p&gt;Presentation of Diplomas&lt;/p&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;p&gt;Closing Speech by Headmaster&lt;/p&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;h2 id="graduates"&gt;Graduates&lt;/h2&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;ul&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;Eileen Williams&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;Andy Maseyk&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;Blanca Sainz Garcia&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;Clara Faulkner&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;Gez Lemon&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;Eloisa Faulkner&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;/ul&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;h2 id="awards"&gt;Awards&lt;/h2&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;ul&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;Clara Faulkner&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;Eloisa Faulkner&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;li&gt;Blanca Sainz Garcia&lt;/li&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;/ul&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;/main&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;footer&gt;Copyright 2012 B.lawson&lt;/footer&gt;</li>
<li>&nbsp;&nbsp; &lt;/body&gt;</li>
<li> &lt;/html&gt;</li>
</ol></div>



#### Best practice

For accessibility matters, a best practice is to split your page content into "regions" defined by the five 5 elements (`aside`, `footer`, `header`, `main` and `nav`) learned this week. 

We recommend this article written by Steve Faulkner: "[Easy content organisation with HTML5](https://tinyurl.com/ovgv6sy)" (24 September 2015). Steve explains in details how to organize an HTML document into "regions" based on the semantic markup elements we have seen so far during Week 1 of this course.


#### External resources:

+ This [document](https://tinyurl.com/y2dt6kbn) has been written by the W3C HTML5 Working Group, which details the different use-cases for this element
+ [Rationale and use cases for standardizing a 'main content' HTML feature](https://tinyurl.com/y2gkl84y)
+ On MDN's Web Docs: the [main element](https://tinyurl.com/lgc2rsz)

#### Knowledge check 1.3.8

<div>
      <ol>
        <li style="margin-bottom:0px;" value="1">
          &lt;!-- other content --&gt;
        </li>
        <li style="margin-bottom:0px;">
             
          &lt;article&gt;
        </li>
        <li style="margin-bottom:0px;">
                 
          &lt;main
           
          role
          =
          "main"
          &gt;
        </li>
        <li style="margin-bottom:0px;">
                    
          &lt;h2&gt;
          Longboards
          &lt;/h2&gt;
        </li>
        <li style="margin-bottom:0px;">
                    
          &lt;p&gt;
          Longboards are a type of skateboard with a longer
        </li>
        <li style="margin-bottom:0px;">
                    wheelbase and larger, softer wheels.
          &lt;/p&gt;
        </li>
        <li style="margin-bottom:0px;">
                 
          &lt;/main&gt;
        </li>
        <li style="margin-bottom:0px;">
             
          &lt;/article&gt;
        </li>
        <li style="margin-bottom:0px;">
           
          &lt;!-- other content --&gt;
        </li>
      </ol>
  </div>

1. Is this code correct? (No/Yes)

  Ans: No<br/>
  Explanation: A main can't be included in an article element.



### 1.3.9 The blog example, applying best practices

Let's go back to our blog example and see what can be improved:

+ Do we have a heading after each sectioning element?
+ Did we use sectioning elements or implicit sections?
+ Can we embed a table of contents?

[The blog example is online at JsBin](https://jsbin.com/heboke/edit?html,output): let's see below what the Google Chrome HTML5 Outliner extension showed.

[Local blog example](src/1.3.9-blog1.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y5ug9vol')"
    src    ="https://tinyurl.com/y6hj3ekp"
    alt    ="image of the blog table of content, that shows an untitled nav entry"
    title  ="image of the blog table of content, that shows an untitled nav entry"
  />
</figure>

Also note that in this example, we used H1s after each sectioning element, and we still get a hierarchy, some H1s are inside an `<article>` that is in a `<section>` (this corresponds to the third example given in the "heading and sectioning elements" part of the course):

<div><ol>
<li value="1"><strong style="color: olive;">&lt;section&gt;</strong></li>
<li>&nbsp; &nbsp;&lt;header&gt; </li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h1&gt;Blog posts for April 2012&lt;/h1&gt;</strong> </li>
<li>&nbsp; &nbsp;&lt;/header&gt;</li>
<li>&nbsp; &nbsp;<strong style="color: olive;">&lt;article&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp;&lt;header&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h1&gt;&lt;a href=""&gt;Information about this example&lt;/a&gt;&lt;/h1&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;This example is a modified version of &lt;a href="https://example.com/blog/index.html"&gt;https://example.com/blog/index.html&lt;/a&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;/header&gt;</li>
<li>&nbsp; &nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;&lt;/article&gt;</li>
<li>&lt;/section&gt;</li>
</ol></div>


With this technique, parts of the document can be moved more easily, or integrated inside an RSS stream, without the need to renumber the headings.

Beware that this technique will require you to use some CSS styling, and may confuse some screen readers that do not yet take into account this way of computing the heading hierarchy. A simple fix is to use an H1 right after the `<body>` and use only H2...H6 inside `<section>`, `<article>`, `<nav>` and `<aside>`.


#### Let's fix the missing heading

We need to add a heading in the `<nav>` element. This will both fix the outline of the document by removing the untitled entry, and will also make screen readers happy as they will better vocalize the structure of the page (it will say "entering nav" followed by the vocalization of the heading content).

<div><ol>
<li value="1">&lt;nav&gt;</li>
<li>&nbsp; &nbsp;<strong style="color: olive;">&lt;header&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h1&gt;Navigation menu&lt;/h1&gt;</strong></li>
<li>&nbsp; &nbsp;<strong style="color: olive;">&lt;/header&gt;</strong></li>
<li>&nbsp; &nbsp;&lt;ul&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;li&gt;&lt;span&gt;Blog&lt;/span&gt;&lt;/li&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;li&gt;&lt;a href=""&gt;About&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;li&gt;&lt;a href=""&gt;Contact&lt;/a&gt;&lt;/li&gt;</li>
<li>&nbsp; &nbsp;&lt;/ul&gt;</li>
<li>&lt;/nav&gt;</li>
</ol></div>


Here is the fixed result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y5ug9vol')"
    src    ="https://tinyurl.com/y4r87tgd"
    alt    ="good outline without the untitled nav"
    title  ="good outline without the untitled nav"
  />
</figure>

A common remark from Web designers is: "we do not want a heading content displayed systematically after a `<nav>`, or an `<aside>` element..."

<p style="align: center; margin: 20px; padding: 20px; border: 1px solid red;"><strong style="color: olive;">BEST PRACTICE #1: </strong>In order&nbsp;to&nbsp;<span style="line-height: 1.6;">NOT&nbsp;display the heading content on screen &nbsp;the recommended technique &nbsp;is described in&nbsp;<a href="https://www.paciellogroup.com/blog/2012/05/html5-accessibility-chops-hidden-and-aria-hidden/" target="_blank">this article by Steve Faulkner</a>.&nbsp;Do not use <span style="font-family: 'courier new', courier;">display:none </span>or <span style="font-family: 'courier new', courier;">visibility:hidden</span> in your CSS stylesheet, as in that case the heading content will never be vocalized by screen readers, and more generally by assistive technologies.&nbsp;<strong style="font-size: 1em; line-height: 1.6em;"><br><br></strong>As an illustration of the recommended technique, see&nbsp;<a href="https://jsbin.com/savabo/edit?html,output" target="_blank">this JSBin version of the blog example</a>&nbsp;that hides the <span style="font-family: 'courier new', courier;">&lt;h2&gt;Navigation menu&lt;/h2&gt;</span> from the <span style="font-family: 'courier new', courier;">&lt;nav&gt;...&lt;/nav&gt;</span> element, using the&nbsp;CSS technique&nbsp;explained in the above link.<strong style="font-size: 1em; line-height: 1.6em;"><br></strong><br/>
<code>
nav header {<br/>
&nbsp;&nbsp;&nbsp;&nbsp; position: absolute !important;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  clip: rect(1px 1px 1px 1px); /* IE6, IE7 */<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  clip: rect(1px, 1px, 1px, 1px);<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  padding:0 !important;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  border:0 !important;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  height: 1px !important; <br/>
&nbsp;&nbsp;&nbsp;&nbsp;  width: 1px !important; <br/>
&nbsp;&nbsp;&nbsp;&nbsp;  overflow: hidden;<br/>
}       
</code></p>

<p style="align: center; margin: 20px; padding: 20px; border: 1px solid red;"><strong style="color: olive;">BEST PRACTICE #2:&nbsp;</strong>it is not advised to include interactive content (links, controls etc) that is hidden offscreen (it is in fact a violation of the <a href="https://www.w3.org/TR/WCAG20/" target="_blank">W3C WCAG 2.0 Guidelines</a>). All interactive content must have a visible focus indicator (and be on screen when focused).<strong style="color: olive;"><br></strong></p>


#### Embedding a table of contents and adding a `<main>` element

In the previous section, we saw how to embed a table of contents using some JavaScript code borrowed from the Google Chrome HTML5 outliner extension.

Let's add this piece of code (we removed the JS details from this extract):

<div><ol>
<li value="1">&lt;aside&gt;</li>
<li>&nbsp; &nbsp;&lt;h1&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;a href="javascript:(function(){...});" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;title="TableOfContents"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; Click here to display the table of contents!</li>
<li>&nbsp; &nbsp; &nbsp;&lt;/a&gt;</li>
<li>&nbsp; &nbsp;&lt;/h1&gt;</li>
<li> &lt;/aside&gt; </li>
</ol></div>


We also added a `<main>` element to identify the main content of the page composed of the big section with all blog posts:

<div><ol>
<li value="1">&lt;main&gt;</li>
<li>&nbsp; &lt;section&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;header&gt; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;h2&gt;Blog posts for April 2012&lt;/h2&gt; </li>
<li>&nbsp; &nbsp; &nbsp;&lt;/header&gt;</li>
<li>&nbsp; &nbsp; &nbsp;...</li>
<li>&lt;/main&gt;</li>
</ol></div>


#### Use H1 as top level headings only, use H2...H6 in sectioning content

As explained in the article [HTML5 Document Outline](https://tinyurl.com/z93l2fy) and in [the W3C HTML Wiki](https://tinyurl.com/y4b7jwq5), it is risky to use nested H1s, as browsers do not correctly implement the "outline algorithm".

The blog example uses nested H1’s. If you check it with [the W3C conformance checker](https://tinyurl.com/o8lnbsu), it issues a warning: "Consider using the h1 element as a top-level heading only (all h1 elements are treated as top-level headings by many screen readers and other tools)."

So, while this is just a warning, we do prefer to use H1s only as top level elements, and replace the H1s we had after `<section>`, `<article>`, `<nav>` and `<aside>` elements respectively by a H2s and H3s. 

Extract from source code:

<div><ol>
<li value="1">&lt;nav&gt;</li>
<li>&nbsp; &nbsp;&lt;header&gt;</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: olive;">&lt;h2&gt;Navigation menu&lt;/h2&gt;</strong></li>
<li>&nbsp; &nbsp;&lt;/header&gt;</li>
<li>&nbsp; &nbsp;...</li>
<li>&lt;/nav&gt;</li>
</ol></div>


Finally, the fixed example

[Check it online with this JsBin](https://tinyurl.com/y695yryn)

[Local example](src/1.3.9-blog2.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5ug9vol')"
    src    ="https://tinyurl.com/y5r2ucuu"
    alt    ="blog with embedded table of contents"
    title  ="blog with embedded table of contents"
  />
</figure>


#### Knowledge check 1.3.9

1. I have a heading after a `<nav>` or an `<aside>` element. What is to be done if I do not want it to appear on the page?<br/>
  a. Prefer not to use a heading in `<nav>` or `<aside>` elements.<br/>
  b. Hide it using the CSS `<display:none>` rule.<br/>
  c. Use CSS, as this is a best practice described in an article (by Steve Faulkner) we refer to in this course.<br/>
  d. Hide it using the CSS `<visibility:hidden>` rule.<br/>

  Ans: c<br/>
  Explanation: The right answer is the third one. The two first answers are not good at all because screen readers will simply ignore the heading and never vocalize it, and as such rendering a badly accessible page. The last answer is also wrong for the same reasons: no heading implies bad accessibility.


### 1.3.10 Examples of page layouts


#### Introduction: simple layouts using the new structuring elements and CSS3

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V002900_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" width=150/>
</a><br/>

[Transcript](https://tinyurl.com/yxu2nvsm)


#### Live coding video: a simple layout based on the CSS float property

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V003300_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" width=150/>
</a><br/>

[Transcript](https://tinyurl.com/y3beda3z)

In this section, we show some "classic" CSS layout techniques for designing an HTML page that uses the new sectioning elements. 

We embed examples from this [very good post about "Positioning content"](https://tinyurl.com/ybkg4vrk). This is a recommended reading as it details how to use the CSS float property to layout a Web page.

The 4 examples below are given "as is" to give you some hints. There are lots of other possibilities on using CSS to position element.

__Example #1: a `<section>` on the left and an `<aside>` on the right, using the float and width CSS properties__

This example uses the following HTML structure (notice that we use the "HTML entity syntax" for displaying "<" or ">". For example, `&lt;` displays a "<" character).

<div><ol>
<li value="1">&lt;header&gt;</li>
<li> &lt;code&gt;&amp;lt;header&amp;gt;&lt;/code&gt;</li>
<li>&lt;/header&gt;</li>
<li>&nbsp;</li>
<li>&lt;section&gt;</li>
<li> &lt;code&gt;&amp;lt;section&amp;gt;&nbsp;&lt;br&gt; float: left;&lt;/code&gt;</li>
<li>&lt;/section&gt;</li>
<li>&nbsp;</li>
<li>&lt;aside&gt;</li>
<li> &lt;code&gt;&amp;lt;aside&amp;gt;&nbsp;&lt;br&gt; float: right;&lt;/code&gt;</li>
<li>&lt;/aside&gt;</li>
<li>&nbsp;</li>
<li>&lt;footer&gt;</li>
<li> &lt;code&gt;&amp;lt;footer&amp;gt;&lt;/code&gt;</li>
<li>&lt;/footer&gt;</li>
</ol></div>


Here we use the CSS rule `float:left` for the `<section>` and the CSS rule `float:right` for the `<aside>`. When an element floats, it goes out of the normal flow of the HTML element. Then by default it floats to the edge of its parent; and its size depends on the elements it contains. So, in order to fill the whole horizontal space, we prefer here to "force the width" by setting the CSS width property with a percentage.  So we took width: 63% for the `<section>` on the left and width:30% for the `<aside>` on the right.

You can look at the complete CSS code in the interactive example below (click on the CSS or HTML text in the menu bar below, or click "edit on codepen" to change the code and see the results):

[Local Example 1 - Layout](src/1.3.10-layout.html)

Example from the live coding video, a slight adaptation of the technique described above

[Also available online at JSBin.](https://tinyurl.com/y3jcm99u)

[Local Example 1 - Michel Buffa Home Page](src/1.3.10-Buffa.html)


__Example #2: three sections centered, of equal size, also using the float and width CSS properties__

Here we show how to make a 3 column layout using the CSS float property.

HTML code:

<div><ol>
<li value="1">&lt;header&gt;</li>
<li> &lt;code&gt;&amp;lt;header&amp;gt;&lt;/code&gt;</li>
<li>&lt;/header&gt;</li>
<li>&nbsp;</li>
<li>&lt;section&gt;</li>
<li> &lt;code&gt;<span style="line-height: 23.2727279663086px;">&amp;lt;</span>section<span style="color: lightblue; line-height: 23.2727279663086px;">&amp;gt;</span>&nbsp;&lt;br&gt; float: left;&lt;/code&gt;</li>
<li>&lt;/section&gt;</li>
<li>&nbsp;</li>
<li>&lt;section&gt;</li>
<li> &lt;code&gt;<span style="line-height: 23.2727279663086px;">&amp;lt;</span>section<span style="color: lightblue; line-height: 23.2727279663086px;">&amp;gt;</span>&nbsp;&lt;br&gt; float: left;&lt;/code&gt;</li>
<li>&lt;/section&gt;</li>
<li>&nbsp;</li>
<li>&lt;section&gt;</li>
<li> &lt;code&gt;<span style="line-height: 23.2727279663086px;">&amp;lt;</span>section<span style="color: lightblue; line-height: 23.2727279663086px;">&amp;gt;</span>&nbsp;&lt;br&gt; float: left;&lt;/code&gt;</li>
<li>&lt;/section&gt;</li>
<li>&nbsp;</li>
<li>&lt;footer&gt;</li>
<li> &lt;code&gt;<span style="line-height: 23.2727279663086px;">&amp;lt;</span>footer<span style="line-height: 23.2727279663086px;">&amp;gt;</span>&lt;/code&gt;</li>
<li>&lt;/footer&gt;</li>
</ol></div>


Instead of having one element with a float:left and one element with a float:right property, we instead use float:left for all three of them, and we give a  width:30% CSS property value to each `<section>`. We also set a small margin so that the colums have a gap between them.

Look at the CSS code in the example below:

[Local Example 2](src/1.3.10-example2.html)


__Example #3: same result using the CSS flex property__

This example uses the CSS flex property to achieve a result similar to the one shown in Example 2.

There are many articles on Flexbox and we recommend those from Rachel Andrew on Smashing Magazine: "Use cases for Flexbox", "Flexbox: how big is that flexible box", etc.

[Local Example 3 ](src/1.3.10-example3.html)


__Example #4: another example written by a student, that uses the flex property__

This example also uses all the structuring elements we saw: main, article, section, etc. It uses only the simplest parts of the FlexBox CSS module, so it should be easy to understand, even for CSS beginners:

[Local Example 4](src/1.3.10-example4.html)


#### External resources

+ An article on CSS Tricks: [All about floats](https://tinyurl.com/nftw559)
+ Old but good article on "A List Apart" (ALA): [CSS Floats 101](https://tinyurl.com/y2gmkbo9)
+ Another article on Lifewire: [Understanding CSS float](https://tinyurl.com/y56oljtx)
+ On MDN's Web Docs: [the float CSS property](https://tinyurl.com/lh9fe44) and [the clear CSS property](https://tinyurl.com/ovkcbf7)


