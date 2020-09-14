# Week 1: HTML5 Basics


## 1.1 Video introduction - Week 1


### 1.1.1 What you will learn in Week 1

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V000800_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" width=100/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y2qy69hb)


## 1.2 From HTML1.0 to HTML5


### 1.2.0 Lecture Notes

+ HTML
  + a.k.a. HyperText Markup Language
  + the authoring language used to create documents on the World Wide Web
  + defining the structure and layout of a Web page
  + using tags w/ attributes
  + `DOCTYPE`: Document Type Declaration, a piece of HTML code that states which version of HTML
  + e.g., `<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">`
  + version
    + HTML: 1991
    + HTML+: 1993
    + HTML2.0: 1995
    + HTML3.2: 1997
    + HTML4.01: 1999
    + XHTML1/0: 2000
    + HTML5: Oct. 2014

+ HTML5
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



### 1.2.1 History of HTML versions

HTML stands for __HyperText Markup Language__, and it is the authoring language used to create documents on the World Wide Web. HTML is used to define the structure and layout of a Web page, how a page looks and any special functions. HTML does this by using tags that have attributes. For example `<p>` means a paragraph. As the viewer of a Web page you don't see the HTML as it is hidden from your view - you just see the results. But you all know that!


#### HTML 1.0

Below is a screenshot of Tim Berners-Lee's Browser Editor as developed in 1991-1992.

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/yxqy752v" ismap target="_blank">
    <img src="https://tinyurl.com/y4sspls2" style="margin: 0.1em;" alt="screenshot of Tim Berners-Lee's Browser Editor" title="screenshot of Tim Berners-Lee's Browser Editor" width=400>
  </a>
</div>

This was a true browser editor for the first version of HTML and ran on a NeXT workstation. Implemented in Objective-C, this very first browser in Web history made it easy to create, view and edit web documents. Hypertext Markup Language (First Version of HTML) was formally published in June 1993.


#### HTML versions

HTML is an evolving language. For Web sites and pages created since 1991, however, it is easy to find out which HTML version they use. A Document Type Declaration, or DOCTYPE, is a piece of HTML code that states which version of HTML is being used. This declaration must appear at the very top of every Web page.

For example: `<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">` tells that the document uses the HTML4.01 version.

<table style="table-layout: auto; border: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif; width: 60%" cellspacing="0" cellpadding="0" border="0" align="center">
  <tbody>
  <tr>
    <td style="padding: 0px; background-color: lightslategray; color: white; font-size: 150%; text-align: center;" colspan="2">HTML Versions</td>
  </tr>
  <tr>
    <td style="background-color: lightslategray; color: white; font-size: 1.2em; width:10%;" valign="top">HTML</td>
    <td style="background-color: white; width: 10%;" valign="center">1991</td>
  </tr>
  <tr>
    <td style="background-color: lightslategray; color: white; font-size: 1.2em;" valign="top">HTML+</td>
    <td style="background-color: white;" valign="center">1993</td>
  </tr>
  <tr>
    <td style="background-color: lightslategray; color: white; font-size: 1.2em;" valign="top">HTML2.0</td>
    <td style="background-color: white;" valign="center">1995</td>
  </tr>
  <tr>
    <td style="background-color: lightslategray; color: white; font-size: 1.2em;" valign="top">HTML3.2</td>
    <td style="background-color: white;" valign="center">1997</td>
  </tr>
  <tr>
    <td style="background-color: lightslategray; color: white; font-size: 1.2em;" valign="top">HTML4.01</td>
    <td style="background-color: white;" valign="center">1999</td>
  </tr>
  <tr>
    <td style="background-color: lightslategray; color: white; font-size: 1.2em;" valign="top">XHTML1.0</td>
    <td style="background-color: white;" valign="center">2000</td>
  </tr>
  <tr>
    <td style="background-color: lightslategray; color: white; font-size: 1.2em;" valign="top">HTML5</td>
    <td style="background-color: white;" valign="center">October 2014</td>
  </tr>
  </tbody>
</table>

For those of you who are curious, the W3C published a document laying down the [HTML5 Differences from HTML4](https://www.w3.org/TR/html5-diff/) (the document was published in December 2014, shortly after the release of HTML5). Read also the [history section](https://tinyurl.com/yxuafev4) available in the HTML5.1 specification document.


#### Knowledge check 1.2.1

1. What does the HTML acronym mean?<br/>
  a. Hacker Table Making Loot<br/>
  b. HyperText Multiple Language<br/>
  c. HyperText Markup Language<br/>
  d. Hot Text Maker Language<br/>

  Ans: c


### 1.2.2 What is HTML5?

On 28 October 2014, the W3C officially published HTML5 as a Web standard (or recommendation of HTML5). HTML5 is the fifth major revision of the format used to build Web pages and applications.

HTML5 contains __powerful capabilities for Web-based applications__ with more interaction, video support, graphics, more styling effects, and a full set of APIs. __HTML5 adapts to any device__, be it a desktop, mobile, tablet, or television device. HTML5 is an open platform developed under royalty free licensing terms.

People use the term HTML5 in two ways:

+ __to refer to a set of technologies that together form the future Open Web Platform.__ These technologies include [HTML5 specification](https://www.w3.org/TR/html5), [CSS](https://www.w3.org/Style/CSS/current-work), [SVG](https://www.w3.org/TR/SVG/), [MathML](https://www.w3.org/TR/MathML/), [Geolocation](https://www.w3.org/TR/geolocation-API/), [XMLHttpRequest](https://www.w3.org/TR/XMLHttpRequest/), [2D Context](https://www.w3.org/TR/2dcontext/), [Web Fonts (WOFF)](https://www.w3.org/TR/WOFF) and others. The boundary of this set of technologies is informal and changes over time.
+ __to refer to the [HTML5 specification](https://www.w3.org/TR/html5)__, which is, of course, also part of the Open Web Platform.

Although it would be great if people used one term to refer to the specification and another term to refer to the set of specifications, in practice people use the term both ways.

When HTML5 became a Web standard, Tim Berners-Lee, Web inventor and W3C Director said:

> "Today we think nothing of watching video and audio natively in the browser, and nothing of running a browser on a phone. We expect to be able to share photos, shop, read the news, and look up information anywhere, on any device. Though they remain invisible to most users, HTML5 and the Open Web Platform are driving these growing user expectations."


#### Knowledge check 1.2.2

1. When did the W3C officially published the HTML5 standard?<br/>
  a. 28 october 2015<br/>
  b. 18 october 2014<br/>
  c. 28 october 2014<br/>
  d. 8 october 2000<br/>

  Ans: c


### 1.2.3 Philippe Le Hégaret video

[Philippe Le Hégaret](https://tinyurl.com/yxdztua4) is W3C's Project Management Lead. He was the former W3C Interaction Domain lead, which produced front-end Web technologies including HTML5, CSS3, SVG, WOFF, or Web APIs.

In the video below, Philippe tells the story on how HTML5 has been developed by the Web community.

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V003500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" width=100/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y52o9rdo)


### 1.2.4 The HTML5 logo

Here is the HTML5 logo! It has been [unveiled on 18 January 2011](https://tinyurl.com/y2tc2m7u), so way before HTML5 became a Web standard. This logo represents HTML5, the cornerstone for modern Web applications.

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/yxqy752v" ismap target="_blank">
    <img src="https://tinyurl.com/y4tw5k68" style="margin: 0.1em;" alt="HTML5 logo" title="HTML5 logo" width=200>
  </a>
</div>


Please check out both the HTML5 [logo home page](https://www.w3.org/html/logo/) and the [FAQ page](https://www.w3.org/html/logo/faq.html) for more information on how to use the logo, etc. You will notably find out that this logo does not imply validity or conformance, and that you are welcome to be creative and make it fit into your own designs. 



## 1.3 Structural elements


### 1.3.0 Lecture Notes

+ Minimum HTML5 Document

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Page Title</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
  </head>
  <body>
  ... <!-- The rest is content -->
  </body>
  </html>
  ```

  + `<meta charset="utf-8">`: best practice to declare the character set
  + `<!DOCTYPE html>`: used by tools and specifying the rules used by an HTML or an XHTML page
    + rules in "Document Type Definitions" (DTDs)
    + not used by Web browsers to validate the structure of an HTML page
    + using only "rules" contained in their own "HTML engine"
    + used by web browser w/ different rendering engines
    + HTML4 more complicated and requiring selection from transitional, strict, or frameset; e.g., `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "https://www.w3.org/TR/html4/loose.dtd">`
  + "type: attributes 
    + optional, required in HTML4
    + `rel="stylesheet"` default value: `type="text/css"`
    + including JavaScript file" `<script src="script.js"></script>` w/o `type="text/javascript"` as old way
  + simplified syntax
    + able to omit quotes or use uppercase, lowercase or a combination of the two
    + no longer a closing tag required in many elements but __recommended__
    + quoted only if containing spaces or some non-alphanumeric characters but __recommended__, e.g., `<link rel=stylesheet href=style.css>`

+ Structural elements

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



### 1.3.1 Greater simplicity

Changes have been made to particular elements in HTML5 making it simpler to use. In this section, we will look at some examples highlighting these improvements, including:

+ the new doctype definition;
+ the fact that the "type" attribute of elements such as `<link>` or `<script>` are now  optional;
+ the syntax constraints that have been relaxed;
+ the new structural elements that have been added, etc.


#### A minimal HTML5 document

```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="utf-8">
   <title>Page Title</title>
   <link rel="stylesheet" href="style.css">
   <script src="script.js"></script>
</head>
<body>
... <!-- The rest is content -->
</body>
</html>
```

Let's compare it to the HTML4 minimal document below (taken from this source). Differences are underlined in red:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "https://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html" charset="utf-8">
    <title>title</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <script type="text/javascript" src="script.js"></script>
</head>
<body>
...
</body>
</html>
```


#### Simpler character set definition

One word about the `<meta charset="utf-8">` at line 4 in the HTML5 version: it is a __best practice__ to declare the character set of your document to protect against [a serious security risk](https://tinyurl.com/yy47zgqw). For more details, please refer to the "Why Internationalization is important" section in the Course intro chapter.


#### No more complicated DOCTYPE definitions

The "DOCTYPE" (Document Type Declaration) is used by tools such as HTML validators (i.e. [the W3C validator](https://validator.w3.org/)), and specifies the rules used by  an HTML or an XHTML page. These rules are contained in special documents called "Document Type Definitions" (also abbreviated as DTDs), written in a language that may seem a bit barbaric to humans (they are intended to be read by software), and hosted by W3C.

DTDs are not used by current Web browsers to  validate the structure of an HTML page, as  they "read" the code without using the DTD to decipher it, using only "rules" contained in their own "HTML engine", but it is still preferable to indicate the doctype as modern browsers have several rendering engines that are chosen depending on the doctype.

Old HTML1 Web pages will not be rendered the same way as new HTML5 pages, since, in the 90's, some of them were written by hand and may contain errors, embedded HTML elements, etc.

With HTML4, doctype definitions looked like this: `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "https://www.w3.org/TR/html4/loose.dtd">`, which was even more complicated as one had to choose between three different possibilities (doctypes could be transitional, strict, or frameset). Most of the time, the doctype definition was copied and pasted from one document to another and was nearly impossible to memorize.

With HTML5, there is only one way to indicate the doctype, and it's so simple there is no reason to forget it:

```html
<!doctype html>
```


#### The "TYPE" attribute is optional

With a `rel="stylesheet"` attribute, it is no longer necessary to indicate `type="text/css"` (from [the specification](https://tinyurl.com/yxnfw3he): "the default type for resources given by the `stylesheet` keyword is `text/css`.")

The "type" attribute is not needed in HTML5, and even old browsers will use text/css as the default type for stylesheets today. So, either way, you can omit the "type" attribute altogether and use:

```html
<link href="file.css" rel="stylesheet"/>
```

instead of:

```html
<link href="file.css" rel="stylesheet" type="text/css"/>
```

We will not go into detail about the <link> element, but the fact that the type attribute is becoming optional shows the current direction taken by HTML5: towards greater simplicity.

Please see how to include a JavaScript file in our page:

```html
<script src="script.js"></script>
```

Here again, the type attribute has been omitted. Just as a reminder, the old way to do the same thing is: 

```html
<script type="text/javascript" src="script.js"></script>
```

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

As Web site layouts evolve, HTML5 structural elements such as lists, paragraphs, tables, etc. show their limits. Today, many Web sites offer navigation menus, tabbed panels, headers, footers, and so on. The way these "parts"' are implemented relies heavily on `<div>` and `<span>` elements with different id and class attributes, lots of CSS and lots of JavaScript code to apply custom styles and behaviors.

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

The results of these surveys led to the addition of new structural elements in HTML5. For example, the very popular `<div class="header">` led to the creation of a `<header>` element, `<div class="aside">` to a `<aside>` element, etc.

Finally, the 20 most popular ids and class names found in Hickson's and Opera's surveys gave birth to these new elements (click on the element's name to go to the W3C specification about this element):

<table style="table-layout: auto; text-rendering: optimizelegibility; border-collapse: collapse; border-spacing: 0px; margin: 20px 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: 16px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;" cellpadding="10" border="1">
  <caption>HTML5 structural elements with descriptions.</caption>
  <tbody>
    <tr><th scope="”row”">HTML5 element</th><th scope="”row”">Description</th></tr>
  </tbody>
  <tbody style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="font-family: 'courier new', courier;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-header-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;header&gt;</span></strong></a></span></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Introduction of "sectioning elements": an article,&nbsp;a&nbsp;section, the entire document (header page). Typically the header of a Web site that appears on top of each page, or a header of a long <span style="font-family: 'courier new', courier;">&lt;article&gt;</span> or of a long <span style="font-family: 'courier new', courier;">&lt;section&gt;</span></td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="font-family: 'courier new', courier;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-footer-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;footer&gt;</span></strong></a></span></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Contains the footer of a site, a long <span style="font-family: 'courier new', courier;">&lt;article&gt;</span>, or a long<span style="font-family: 'courier new', courier;"> &lt;section&gt;</span></td>
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
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/grouping-content.html#the-figure-element" target="_blank"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;figure&gt;</strong></span></a>&nbsp;and&nbsp;<a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/grouping-content.html#the-figcaption-element" target="_blank"><br/><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;figcaption&gt;</span></strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Used to encapsulate a figure as a single item, and contains a caption for the figure, respectively.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-aside-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;main&gt;</span></strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The main element represents the main content of the body of a document or application. The main content area consists of content that is directly related to or expands upon the central topic of a document or central functionality of an application. <strong>There can be only one <span style="font-family: 'courier new', courier;">&lt;main&gt;</span> element in a document.</strong></td>
    </tr>
  </tbody>
</table>

And there is no `<content>` element even though the `<div class="content">` was very popular. Instead, the HTML5 group decided that anything not embedded in one of the elements from the above table is "default content". If the content is of a type that corresponds to one of the elements from the table, i.e. if the content is an article, it should be embedded between `<article>` and `</article>`.

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

```html
<!DOCTYPE html>
   <html lang="en">
      <head>
         <meta charset="utf-8"/>
         <title>Simple HTML5 blog</title>
      </head>
      <body>
         <header>
            <h1>Simple <span>HTML5</span> blog</h1>
         </header>
...
```

The CSS rules we used:

```css
header {
    color: #007e99;
    font-size: 2.5em;
    padding: 20px 50px;
}
header span {
    color: #722;
}
```

#### Use a `<nav>` for the navigation menu just below the header

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/y5w747zv" style="margin: 0.1em;" alt="image of the navigation menu" title="image of the navigation menu" width=200>
  </a>
</div>


The navigation menu just below the header is a `<nav>` element. For the purpose of this example we haven't provided any value for the hyperlinks...

HTML code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="utf-8"/>
   <title>Simple HTML5 blog</title>
</head>
<body>
<header>
   <h1>Simple <span>HTML5</span> blog</h1>
</header>
<nav>
    <ul>
       <li><span>Blog</span></li>
       <li><a href="">About</a></li>
       <li><a href="">Contact</a></li>
    </ul>
</nav>
```

And here is the CSS we used in this example for the `<nav>` element:

```css
nav {
    font-size: 1.5em;
    margin: 5px 0;
    padding: 20px 50px;
}
nav li {
    display: inline;
    margin: 0 15px;
}
nav li:first-child {
    margin-left: 0;
}
* html nav ul {
    margin-left: -15px;
}
nav span, nav a {
    padding: 3px 15px 4px;
}
nav span {
    background: #722;
    color: #fff;
}
```


#### A `<section>` for each month and an `<article>` for each post in the blog

Now, we have one big `<section>` element that contains a set of `<article>` elements...

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/y26lwg8j" style="margin: 0.1em;" alt="image of sections that contain articles" title="image of sections that contain articles" width=300>
  </a>
</div>


HTML code:

```html
<section>
   <article>
    ...
   </article>
   <article>
    ...
   </article>
   <article>
    ...
   </article>
</section>
```

And here is the CSS:

```css
section {
   float: left;
   padding: 35px 0;
   position: relative;
   width: 70%;
}
section article {
   margin: 0 50px 40px;
   padding: 25px 0 0;
   position: relative;
}
section header {
   font-size: 1em;
   padding: 0;
}
section h2 {
   font-size: 2.3em;
}
```

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

```html
<section>
  <article>
    <header>
      <h2><a href="">Information about this example</a></h2>
    </header>
    <p>Try to move the mouse on different elements. The structure will be ...</p>
    <figure>
      <img src="HTML5-tags.png" alt="Example of HTML5 structural tags" />
      <figcaption>
        Fig. 1: an example of how new structural elements could be used. This ...
      </figcaption>
    </figure>
  </article>
  ...
</section>
```


#### Use `<figure>` and `<figcaption>` and embed `<img>` inside

Also note the way we included a figure using the new "HTML5" method, using a `<figure>..</figure>` element that embedded a `<img src=.../>` element together with a `<figcaption>` element. 

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/yxktruxu" style="margin: 0.1em;" alt="image of figure and figcaption that embed an img" title="image of figure and figcaption that embed an img" width=350>
  </a>
</div>

Here is the CSS for the `<figcaption>` element we have used in the example (we did not apply any style to the `<figure>` element):

HTML code:

```html
<figure>
    <img src="HTML5-tags.png"
         alt="Example of HTML5 structural tags" />
    <figcaption>
        Fig. 1 : an example of how .....
    </figcaption>
</figure>
```

CSS code:

```css
figcaption {
    font-style:italic;
    font-size: 0.8em;
    width: 100%;
}
```


#### Use an `<aside>` element to display a tag cloud on the ... side of the main content

After the long `<section>` element that contains all the blog articles displayed in the page, we added the HTML code for the tag cloud that is displayed on the right of the page, "aside"! This is done using - you already guessed it - an `<aside>` element:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ug9vol" ismap target="_blank">
    <img src="https://tinyurl.com/y2x3vtng" style="margin: 0.1em;" alt="image of the tag cloud defined as an aside element" title="image of the tag cloud defined as an aside element" width=150>
  </a>
</div>


```html
<section>
.... all <article>... </article> here....
</section>
<aside>
   <h2>Tag cloud</h2>
   <ul class="tag-cloud">
       <li><a href="" rel="tag" class="w2">ajax</a></li>
       <li><a href="" rel="tag" class="w8">apple</a></li>
       <li><a href="" rel="tag" class="w3">css</a></li>
       ...
   </ul>
</aside>
...
```

We are not going to show the complete CSS here as it uses some tricks to display the list as a "real tag cloud" that uses JavaScript for handling events, etc. Those who are curious can look at the code of the online example.

Here is the CSS for the `<aside>` element:

```css
aside {
    float: right;
    padding: 70px 0 30px;
    position: relative;
    width: 25%;
}
aside h2 {
    color: #888;
    font-size: 1.8em;
}
aside .tag-cloud {
    padding: 15px 35px 10px 0;
    text-align: center;
}
...
```

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

```html
<html>
...
<body>
...
<section>
...
</section>
<aside>
...
</aside>
<footer>
   <p>&copy; 2009 Some blog</p>
</footer>
</body>
</html>
```

With this CSS rule:

```css
footer {
    clear: both;
    color: #777;
    padding: 10px 50px;
}
```

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




## 1.4 Other elements and attributes








## 1.5 Microdata








## 1.6 Exercises - Week 1







