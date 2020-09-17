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

+ `<article>` and `<section>`
  + `<article>`: designed for stand-alone parts of a document that could eventually be syndicated in RSS streams
  + `<section>`: used to cut a logical part into subparts
  + `<article>` able to be cut into different `<section>` elements
  + `<section>` may be cut into different `<article>` elements

+ Sectioning elements
  + headings: `<h1>...<h6>`
    + used to display headings with different sizes by default, when no CSS is used
    + define the header of a section
  + section elements: `<section>`, `<article>`, `<nav>` and `<aside>`
    + sections: a document cut into slides by sectioning elements
    + each potentially w/ a heading and an outline associated
  + multiple headings of different rank with sectioning content
    + 1st element of a heading content in an element of sectioning content representing the heading for that section
    + headings of _equal or higher rank_: new (implied) sections
    + headings of _lower rank_: implied subsections that are part of the previous one
    + `<h1>` inside a `<section>`: the browser lowers its default size automatically
  + best practices
    + always add a heading to explicit sectioning content
      + including a heading (a `<h1>, <h2>...<h6>`) in each sectioning element
      + the `<body>` element: sectioning root
      + example

        ```html
        <body>
            <h1>Example Blog</h1>
            <section>
              <header>
                  <h2>Blog post of April 2020</h2>
                  <p>Posted by Michel Buffa...</p>
              </header>
              <p>Content of the blog post...</p>
          </section>
        </body>
        ```

    + using `<section>`, `<article>`, etc. instead of just `<h1>...<h6>`, not to relying on implicit sectioning
      + `<header> `element
        + a container
        + not defining new sections of a document nor affecting the hierarchy levels
      + HTML not dedicated mechanism for marking up subheadings, alternative titles or taglines
      + example

        ```html
        <body>
        <h1>Apples</h1>
        <p>Apples are fruit.</p>
        <section>
            <h2>Taste</h2>
            <p>They taste lovely.</p>
            <section>
                <h3>Sweet</h3>
                <p>Red apples are sweeter than green ones.</p>
            </section>
        </section>
        <section>
            <h2>Color</h2>
            <p>Apples come in various colors.</p>
        </section>
        </body>
        ```

+ Table of contents
  + useful for debugging the structure of your page
  + checking the presence of headings after sectioning content
  + displaying some "untitled entries" $\to$ missing some headings


+ The `<main>` element
  + identify the main content of the document
  + provide a navigable document structure for assistive technology users as well as styling hooks for devs
  + supported by major modern browsers
  + constraints
    + no more than one `<main>` element in a document
    + not a descendant of an `<article>`, `<aside>`, `<footer>`, `<header>`, or `<nav>` element
  + best practice:
    + split page content into "regions" defined by the five 5 elements (`aside`, `footer`, `header`, `main` and `nav`)

+ Best practices
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
    + not using `display:none` or `visibility:hidden` in your CSS stylesheet
    + recommended technique

      ```css
      nav header {
          position: absolute !important;
          clip: rect(1px 1px 1px 1px); /* IE6, IE7 */
          clip: rect(1px, 1px, 1px, 1px);
          padding:0 !important;
          border:0 !important;
          height: 1px !important;
          width: 1px !important;
          overflow: hidden;
      }
      ```
  + Not advised to include interactive content (links, controls etc) hidden offscreen, all interactive content must have a visible focus indicator
  + Using H1 as top level headings only, using H2...H6 in sectioning content
    + risky to use nested H1s
    + browsers not correctly implement the "outline algorithm"

+ Page layout
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

The results of these surveys led to the addition of new structural elements in HTML5. For example, the very popular `<div class="header">` led to the creation of a `<header>` element, `<div class="aside">` to a `<aside>` element, etc.

Finally, the 20 most popular ids and class names found in Hickson's and Opera's surveys gave birth to these new elements (click on the element's name to go to the W3C specification about this element):

<table style="table-layout: auto; text-rendering: optimizelegibility; border-collapse: collapse; border-spacing: 0px; margin: 20px 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: 16px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;" cellpadding="10" border="1">
  <caption>HTML5 structural elements with descriptions.</caption>
  <tbody>
    <tr><th scope="”row”">HTML5 element</th><th scope="”row”">Description</th></tr>
  </tbody>
  <tbody style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="font-family: 'courier new', courier;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-header-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;header&gt;</strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Introduction of "sectioning elements": an article,&nbsp;a&nbsp;section, the entire document (header page). Typically the header of a Web site that appears on top of each page, or a header of a long <span style="font-family: 'courier new', courier;">&lt;article&gt; or of a long <span style="font-family: 'courier new', courier;">&lt;section&gt;</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="font-family: 'courier new', courier;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-footer-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;footer&gt;</strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Contains the footer of a site, a long <span style="font-family: 'courier new', courier;">&lt;article&gt;, or a long<span style="font-family: 'courier new', courier;"> &lt;section&gt;</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-nav-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;nav&gt;</strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Section that contains the main navigation links (within the document or to other pages).</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-article-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;article&gt;</strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <p style="text-rendering: optimizelegibility; margin: 0px 0px 1.416em; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: 1em; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.6em !important; vertical-align: baseline;">Independent content, which can be individually extracted from the document and syndicated (RSS or equivalent) without penalizing its understanding. Typically a blog post.</p>
      </td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-section-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;section&gt;</strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <p style="text-rendering: optimizelegibility; margin: 0px 0px 1.416em; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: 1em; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.6em !important; vertical-align: baseline;">Generic section used to group different articles for&nbsp;different purposes or subjects, or to define the different sections of a single article. Generally used&nbsp;with a header.</p>
      </td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/text-level-semantics.html#the-time-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time&gt;</strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Used for marking up times and dates.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-aside-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;aside&gt;</strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Section whose content is not necessarily directly related to the main content that surrounds it, but can provide additional information.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/grouping-content.html#the-figure-element" target="_blank"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;figure&gt;</strong></a>&nbsp;and&nbsp;<a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/grouping-content.html#the-figcaption-element" target="_blank"><br/><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;figcaption&gt;</strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Used to encapsulate a figure as a single item, and contains a caption for the figure, respectively.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><a style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; transition: color 0.25s ease-in-out 0s; -webkit-transition: color 0.25s ease-in-out 0s; text-decoration: none; color: #1d9dd9; background: transparent;" href="https://www.w3.org/TR/html5/sections.html#the-aside-element" target="_blank"><strong style="text-rendering: optimizelegibility; font-weight: bold; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'courier new', courier, monospace; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;main&gt;</strong></a></td>
      <td style="text-rendering: optimizelegibility; margin: 20px 0px; padding: 10px; border: 1px solid #cbcbcb; outline: 0px; font-family: inherit; font-size: 14px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The main element represents the main content of the body of a document or application. The main content area consists of content that is directly related to or expands upon the central topic of a document or central functionality of an application. <strong>There can be only one <span style="font-family: 'courier new', courier;">&lt;main&gt; element in a document.</strong></td>
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
            <h1>Simple HTML5 blog</h1>
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
   <h1>Simple HTML5 blog</h1>
</header>
<nav>
    <ul>
       <li>Blog</li>
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


### 1.3.4 More on `<article>` and `<section>`


#### Can an `<article>` contain a `<section>`?

It may not be clear whether a `<section>` may contain one or several `<article>` elements or if an `<article>` may contain one or several `<section>` elements.

+ The `<article>` element was designed for stand-alone parts of a document that could eventually be syndicated in RSS streams.
+ `<section>` elements are used to cut a logical part into subparts.

<div style="margin-left: 1.0em;">
  <p><strong><span style="font-size: 1em; line-height: 1.6em;">An <span style="font-family: 'courier new', courier;">&lt;article&gt; may be cut into different <span style="font-family: 'courier new', courier;">&lt;section&gt; elements!</strong></p>
</div>

Example of a blog post defined as a long `<article>`, that is in turn cut into smaller `<section>` elements:

```html
<article id="id1">
   <section id="id1part1">
     <h2>Introduction</h2>
   </section>
   <section id="id1part2">
     <h2>My travel to India</h2>
   </section>
   <section id="id1part3">
     <h2>Return to France</h2>
   </section>
</article>
```

The blog example from the previous part of the course, on the other hand, uses a single `<section>` that contains several `<article>` elements.

Indeed, we can also have a `<section>` that regroups all blog posts per month, each one being an `<article>` element.

<div style="margin-left: 1.0em;">
  <p><strong><span style="line-height: 25.6px;">A&nbsp;&lt;section&gt; may be cut into different <span style="font-family: 'courier new', courier;">&lt;article&gt; elements, too!</strong></p>
</div>


#### Can you put a `<nav>` in an `<article>`?

Yes you can, in case you would like to propose some navigation links with each blog post, for example:

```html
<article>
   <header>
     <h1>Blog post title</h1>
       <p>Author: Michel</p>
   </header>
   <nav>
       <ul>
           <li><a href="...">Next post</a></li>
           <li><a href="...">Previous post</a></li>
           <li><a href="...">Contact author</a></li>
       </ul>
   </nav>
   <p>Content...</p>
   <footer>
     <p>Posted by Michel, the <time datetime="2012-02-02">February 2,
     2012</time> </p>
   </footer>
</article>
```

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


#### Using headings and new sectioning elements (section, article, aside, nav)

__Definition of heading content and sectioning content__

The `<section>`, `<article>`, `<nav>` and `<aside>` elements are called "__sectioning elements__". They cut a document into slices we call "__sections__".

The HTML5 specification says that "each sectioning element potentially has a heading and has also an outline associated".

`<h1>...<h6>` are called __headings__, and define the header of a section (whether explicitly marked up using sectioning content elements, or implied by the heading content itself). This means that:

```html
<body>
    <h1>Title of my document</h1>
    ...
</body>
```

... defines the header of a section implicitly, while:

```html
<body>
   ...
   <section>
      <h1>Title of my section</h1>
      ...
   </section>
</body>
```

... defines the heading of the explicit section (its parent element `<section>`).


#### Use multiple headings of different rank with sectioning content

The first element of a heading content in an element of sectioning content represents the heading for that section (the `<section><h1>...</h1></section>` in the above example).

Subsequent headings of equal or higher rank start new (implied) sections, headings of lower rank start implied subsections that are part of the previous one. In both cases, the element represents the heading of the implied section.

Let's clarify this by looking at some example code:

```html
<body>
<section>
  <h1>This H1 is the heading of an explicit section</h1>
      ...
    <h2>(lower rank) This H2 is a subheading, part of the same section</h2>
        ....
  <h1>(equal or higher rank) This H1 starts an implicit new section in the explicit
      section </h1>
      ...
    <h2>This is a H2 heading in the new section that has just started</h2>
        ...
</section>
</body>
```

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

__Best practice #1: always add a heading to explicit sectioning content__

It's always better - mainly for accessibility reasons - to include a heading (a `<h1>, <h2>...<h6>`) in each sectioning element (`<section>`, `<article>`, `<nav>`, `<aside>`), but also after the `<body>` element (called a "sectioning root").

Here are some examples:

__Good (heading in each explicit section)__:

```html
<section>
    <h1>Blog post of April 2020</h1>
    ...
</section>
```

__Good (heading  in a `<header>` does not change anything)__

```html
<section>
   <header>
      <h1>Blog post of April 2020</h1>
      <p>Posted by Michel Buffa...</p>
   </header>
...
</section>
```

__Bad (there is no Hx after the `<section>` -> no heading)__:

```html
<section>
   <header>
      <p class="article title">Blog post of April 2020</p>
      <p>Posted by Michel Buffa...</p>
   </header>
   ...
</section>
```

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

```html
<body>
    <h1>Example Blog</h1>
    <section>
       <header>
          <h2>Blog post of April 2020</h2>
          <p>Posted by Michel Buffa...</p>
       </header>
      <p>Content of the blog post...</p>
   </section>
</body>
```

In red, the sectioning root (`<body>`) and the sectioning elements (`<section>` here...), each have a heading.

__To sum up:__
+ Always use a heading element after a sectioning element, for example `<section><Hx>...</Hx>...</section>`, and after `<body>`, where x can be 1..6,
+ Or, use a `<header>` element, like in `<section><header><Hx>...</Hx>.....</header>...</section>`


#### More about the `<header>` element

__The `<header>` element is just a container. It is not taken into account for defining new sections of a document nor does it affect the hierarchy levels.__

You can use heading elements `<h1>...<h6>` in a `<header>` but be careful if you use more than one, as the rules explained in the previous part of the course will apply and may generate implicit "sections" in the header.

This example has two headings in the `<header>`:

```html
<section>
   <header>
     <h1>Some text in a h1 in a header of a section</h1>
     <h2>This a h2 in the header...</h2>
   </header>
</section>
```

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

```html
<header>
    <h1>HTML 5.1 Nightly</h1>
    <p>A vocabulary and associated APIs for HTML and XHTML</p>
    <p>Editor's Draft 9 May 2013</p>
</header>
```

__Best practice #2: try not to rely on implicit sectioning, use `<section>`, `<article>`, etc. instead of just `<h1>...<h6>`__

The example below defines several implicit "sections" by using `<Hx>` directly (at lines 7 and 9):

Ok version (no explicit sections everywhere):

```html
<body>
<h4>Apples</h4>
<p>Apples are fruit.</p>
<section>
     <h2>Taste</h2>
     <p>They taste lovely.</p>
     <h6>Sweet</h6>
     <p>Red apples are sweeter than green ones.</p>
     <h1>Color</h1>
     <p>Apples come in various colors.</p>
</section>
</body>
```

Better version (best practice):

```html
<body>
<h1>Apples</h1>
<p>Apples are fruit.</p>
<section>
     <h2>Taste</h2>
     <p>They taste lovely.</p>
     <section>
         <h3>Sweet</h3>
         <p>Red apples are sweeter than green ones.</p>
     </section>
</section>
<section>
     <h2>Color</h2>
     <p>Apples come in various colors.</p>
</section>
</body>
```

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

```html
<section>
<header>
  <p class = "article title" > Blog post of April 2020 </p>
  <p> Posted by Michel Buffa... </p>
</header>
...
</section>
```

1. Does this example follow the best practices presented in this section of the course? (Yes/No)

  Ans: No<br/>
  Explanation: No, the section is not followed by at least one heading (in the header element)


### 1.3.7 Embedding a table of contents

Here we propose a small piece of JavaScript code you can use in your documents to display an embedded table of contents. 

This example is a simple document, with a hyperlink that, once clicked, displays the table of contents in an `<aside>` element in the main `<section>`. Just look at the source code and copy/paste the link into your own HTML documents.

[Online example at JsBin.](https://tinyurl.com/y3ab6zow)

[Local example](src/1.3.7-toc.html)

Extract of source code:

```html
<body>
<h1>This is an example of embedded table of content</h1>
<section>
     <header>
         <h1>First section of the document (this is a h1)</h1>
         This is a subheading...
     </header>
     <h2>First subsection of the first section (a h2)</h2>
     <p>Blah Blah...</p>
 </section>
<section>
     <h1>Second section of the document (a h1)</h1>
     <h2>First subsection (a h2)</h2>
</section>
<aside>
     <h3>Table of contents</h3>
     <a href="javascript:(function(){...})();"
        title="TableDeMatiere">
        Click here to display the table of contents!
     </a>
</aside>
</body>
```

__Best practice__: visualizing the table of contents is useful for debugging the structure of your page, and checking the presence of headings after sectioning content.

Indeed, tools that generate the table of contents are a good way to debug the structure of your page. Is the hierarchy correct? Is it what I wanted when I designed my page?

They are also useful for checking the presence of headings in each sectioning content. If some headings are missing, the table of contents will display some "untitled entries". Remember that having a heading after each sectioning content is a good practice in terms of accessibility.

#### Knowledge check 1.3.7

```
1. Simple HTML5 blog
2. Blog posts for April 2020
  1. Information about this example
  2. History
  3. HTML vs XHTML
  4. Untitled SECTION
3. Tag cloud
```

1. Is this outline ideal? (No/Yes)

  Ans: No <br/>
  Explanation: No, there is one untitled entry, meaning that a heading is missing.


### 1.3.8 The `<main>` element

If you use `<nav>` / `<header>` / `<footer>` etc. to structure your document, you can also use `<main>` to identify the main content of the document. Doing so provides a navigable document structure for assistive technology users as well as styling hooks for devs.

We have seen the different sectioning elements of HTML5, so why didn't we talk about the `<main>` element earlier in this part of the course? Shouldn't  `<main>...</main>` be used in place of  `<div class="main">...</div>`?

The `<main>` element is supported by major modern browsers (see the corresponding [support table](https://tinyurl.com/yyvj2uf6) on CanIUse and [MDN's brower compatibility page](https://tinyurl.com/q5dwuwe)).

This element is subject to some constraints:

There must not be more than one `<main>` element in a document,

+ It must not be a descendant of an `<article>`,`<aside>`, `<footer>`, `<header>`, or `<nav>` element.
+ And finally, here are some examples (from [the HTML5 specification](https://tinyurl.com/y2dt6kbn))  that mix the `<main>` element with the other sectioning elements already seen in the course:


```html
<!-- other content -->
<main>
   <h1>Skateboards</h1>
   <p>The skateboard helps kids to get around.</p>
   <article>
      <h2>Longboards</h2>
      <p>Longboards are a type of skateboard with a longer
wheelbase and larger, softer wheels.</p>
      <p>... </p>
      <p>... </p>
   </article>
   <article>
      <h2>Electric Skateboards</h2>
      <p>These no longer require the propelling of the skateboard by means of the feet; 
      rather an electric motor propels the board, fed by an electric battery.</p>
      <p>... </p>
      <p>... </p>
   </article>
</main>
 
<!-- other content -->
```

Here is another example (also from the specification). Here the `<main>` element contains a `<nav>` element consisting of links to subsections of the main content:

```html
<!DOCTYPE html>
   <html lang="en">
      <head>
         <meta charset="utf-8"/>
         <title>Graduation Ceremony Summer 2022</title>
      </head>
      <body>
       <header>The Lawson Academy:
         <nav>
            <h2>Click these links to navigate...</h2>
            <ul>
               <li><a href="courses.html">Courses</a></li>
               <li><a href="fees.html">Fees</a></li>
               <li><a>Graduation</a></li>
            </ul>
         </nav>
      </header>
      <main>
         <h1>Graduation</h1>
         <nav>
            <h2>Please choose:</h2>
            <ul>
               <li><a href="#ceremony">Ceremony</a></li>
               <li><a href="#graduates">Graduates</a></li>
               <li><a href="#awards">Awards</a></li>
            </ul>
         </nav>
         <h2 id="ceremony">Ceremony</h2>
         <p>Opening Procession</p>
         <p>Speech by Valedictorian</p>
         <p>Speech by Class President</p>
         <p>Presentation of Diplomas</p>
         <p>Closing Speech by Headmaster</p>
         <h2 id="graduates">Graduates</h2>
         <ul>
            <li>Eileen Williams</li>
            <li>Andy Maseyk</li>
            <li>Blanca Sainz Garcia</li>
            <li>Clara Faulkner</li>
            <li>Gez Lemon</li>
            <li>Eloisa Faulkner</li>
         </ul>
         <h2 id="awards">Awards</h2>
            <ul>
               <li>Clara Faulkner</li>
               <li>Eloisa Faulkner</li>
               <li>Blanca Sainz Garcia</li>
            </ul>
         </main>
      <footer>Copyright 2012 B.lawson</footer>
   </body>
</html>
```


#### Best practice

For accessibility matters, a best practice is to split your page content into "regions" defined by the five 5 elements (`aside`, `footer`, `header`, `main` and `nav`) learned this week. 

We recommend this article written by Steve Faulkner: "[Easy content organisation with HTML5](https://tinyurl.com/ovgv6sy)" (24 September 2015). Steve explains in details how to organize an HTML document into "regions" based on the semantic markup elements we have seen so far during Week 1 of this course.


#### External resources:

+ This [document](https://tinyurl.com/y2dt6kbn) has been written by the W3C HTML5 Working Group, which details the different use-cases for this element
+ [Rationale and use cases for standardizing a 'main content' HTML feature](https://tinyurl.com/y2gkl84y)
+ On MDN's Web Docs: the [main element](https://tinyurl.com/lgc2rsz)

#### Knowledge check 1.3.8

```html
<!-- other content -->
<article>
<main role = "main" >
<h2> Longboards </h2>
<p> Longboards are a type of skateboard with a longer
    wheelbase and larger, softer wheels. </p>
</main>
</article>
<!-- other content -->
```

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

```html
<section>
   <header>
     <h1>Blog posts for April 2012</h1>
   </header>
   <article>
     <header>
       <h1><a href="">Information about this example</a></h1>
       This example is a modified version of 
       <a href="https://example.com/blog/index.html">https://example.com/blog/index.html</a>
     </header>
     ...
   </article>
</section>
```

With this technique, parts of the document can be moved more easily, or integrated inside an RSS stream, without the need to renumber the headings.

Beware that this technique will require you to use some CSS styling, and may confuse some screen readers that do not yet take into account this way of computing the heading hierarchy. A simple fix is to use an H1 right after the `<body>` and use only H2...H6 inside `<section>`, `<article>`, `<nav>` and `<aside>`.


#### Let's fix the missing heading

We need to add a heading in the `<nav>` element. This will both fix the outline of the document by removing the untitled entry, and will also make screen readers happy as they will better vocalize the structure of the page (it will say "entering nav" followed by the vocalization of the heading content).

```html
<nav>
   <header>
     <h1>Navigation menu</h1>
   </header>
   <ul>
     <li>Blog</li>
     <li><a href="">About</a></li>
     <li><a href="">Contact</a></li>
   </ul>
</nav>
```

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

<p style="align: center; margin: 20px; padding: 20px; border: 1px solid red;"><strong>BEST PRACTICE #1: </strong>In order&nbsp;to&nbsp;<span style="line-height: 1.6;">NOT&nbsp;display the heading content on screen &nbsp;the recommended technique &nbsp;is described in&nbsp;<a href="https://www.paciellogroup.com/blog/2012/05/html5-accessibility-chops-hidden-and-aria-hidden/" target="_blank">this article by Steve Faulkner</a>.&nbsp;Do not use <span style="font-family: 'courier new', courier;">display:none or <span style="font-family: 'courier new', courier;">visibility:hidden in your CSS stylesheet, as in that case the heading content will never be vocalized by screen readers, and more generally by assistive technologies.&nbsp;<strong style="font-size: 1em; line-height: 1.6em;"><br><br></strong>As an illustration of the recommended technique, see&nbsp;<a href="https://jsbin.com/savabo/edit?html,output" target="_blank">this JSBin version of the blog example</a>&nbsp;that hides the <span style="font-family: 'courier new', courier;">&lt;h2&gt;Navigation menu&lt;/h2&gt; from the <span style="font-family: 'courier new', courier;">&lt;nav&gt;...&lt;/nav&gt; element, using the&nbsp;CSS technique&nbsp;explained in the above link.<strong style="font-size: 1em; line-height: 1.6em;"><br></strong><br/>
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

<p style="align: center; margin: 20px; padding: 20px; border: 1px solid red;"><strong>BEST PRACTICE #2:&nbsp;</strong>it is not advised to include interactive content (links, controls etc) that is hidden offscreen (it is in fact a violation of the <a href="https://www.w3.org/TR/WCAG20/" target="_blank">W3C WCAG 2.0 Guidelines</a>). All interactive content must have a visible focus indicator (and be on screen when focused).<strong><br></strong></p>


#### Embedding a table of contents and adding a `<main>` element

In the previous section, we saw how to embed a table of contents using some JavaScript code borrowed from the Google Chrome HTML5 outliner extension.

Let's add this piece of code (we removed the JS details from this extract):

```html
<aside>
   <h1>
     <a href="javascript:(function(){...});"
        title="TableOfContents">
        Click here to display the table of contents!
     </a>
   </h1>
</aside>
```

We also added a `<main>` element to identify the main content of the page composed of the big section with all blog posts:

```html
<main>
  <section>
     <header>
         <h2>Blog posts for April 2012</h2>
     </header>
     ...
</main>
```


#### Use H1 as top level headings only, use H2...H6 in sectioning content

As explained in the article [HTML5 Document Outline](https://tinyurl.com/z93l2fy) and in [the W3C HTML Wiki](https://tinyurl.com/y4b7jwq5), it is risky to use nested H1s, as browsers do not correctly implement the "outline algorithm".

The blog example uses nested H1’s. If you check it with [the W3C conformance checker](https://tinyurl.com/o8lnbsu), it issues a warning: "Consider using the h1 element as a top-level heading only (all h1 elements are treated as top-level headings by many screen readers and other tools)."

So, while this is just a warning, we do prefer to use H1s only as top level elements, and replace the H1s we had after `<section>`, `<article>`, `<nav>` and `<aside>` elements respectively by a H2s and H3s. 

Extract from source code:

```html
<nav>
   <header>
     <h2>Navigation menu</h2>
   </header>
   ...
</nav>
```

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

```html
<header>
<code>&lt;header&gt;</code>
</header>
 
<section>
<code>&lt;section&gt; <br> float: left;</code>
</section>
 
<aside>
<code>&lt;aside&gt; <br> float: right;</code>
</aside>
 
<footer>
<code>&lt;footer&gt;</code>
</footer>
```

Here we use the CSS rule `float:left` for the `<section>` and the CSS rule `float:right` for the `<aside>`. When an element floats, it goes out of the normal flow of the HTML element. Then by default it floats to the edge of its parent; and its size depends on the elements it contains. So, in order to fill the whole horizontal space, we prefer here to "force the width" by setting the CSS width property with a percentage.  So we took width: 63% for the `<section>` on the left and width:30% for the `<aside>` on the right.

You can look at the complete CSS code in the interactive example below (click on the CSS or HTML text in the menu bar below, or click "edit on codepen" to change the code and see the results):

[Local Example 1 - Layout](src/1.3.10-layout.html)

Example from the live coding video, a slight adaptation of the technique described above

[Also available online at JSBin.](https://tinyurl.com/y3jcm99u)

[Local Example 1 - Michel Buffa Home Page](src/1.3.10-Buffa.html)


__Example #2: three sections centered, of equal size, also using the float and width CSS properties__

Here we show how to make a 3 column layout using the CSS float property.

HTML code:

```html
<header>
<code>&lt;header&gt;</code>
</header>
 
<section>
<code>&lt;section&gt; <br> float: left;</code>
</section>
 
<section>
<code>&lt;section&gt; <br> float: left;</code>
</section>
 
<section>
<code>&lt;section&gt; <br> float: left;</code>
</section>
 
<footer>
<code>&lt;footer&gt;</code>
</footer>
```

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



## 1.4 Other elements and attributes


### 1.4.0 Lecture Notes

+ Foldable zone in an HTML document
  + `<details>` element:
    + generate a simple widget to show/hide element contents
    + able to be embedded inside one another
  + `<summary>` element: (optional) children element of `<details>` element
  + `<summary>...</summary>` located inside a `<details>...</details>` element

+ Styling summary icons w/ CSS
  + modifying color and background of the icon w/ `::-webkit-details-marker`

    ```css
    summary::-webkit-details-marker {
      color:#FF0000;
      background:#FFFFFF;
    }
    ```

  + `details[open]` selector handling the unfolded `<details>`

    ```css
    details[open] summary::-webkit-details-marker {
      color:#0000FF;
      background:#00FFFF;
    }
    ```

  + using `+` shaped icon for expansion

    ```css
    summary:after {
      content: "+";
      color: #FF00FF;
      float: left;
      font-size: 1.5em;
      font-weight: bold;
      margin: -5px 5px 0 0;
      padding: 0;
      text-align: center;
      width: 20px;
    }
    ```

  + using `-` shaped icon to callops details

    ```css
    details[open] summary:after {
      content: "-";
      color: #FFFFFF
    }
    ```

+ The `<time>` element
  + useful for marking a time or a duration in a document
  + expression
    + human readable part (the part between `<time>` and `</time>`)
    + machine readable part contained within a `datetime` attribute
    + date: expressed as `YYYY-MM-DD`
  + machine readable used by 
    + search engines for indexing
    + browsers or browser extensions
    + JavaScript code
  + useful scenarios
    + generating alerts for birthdays
    + automatically adding dates or events that contain `<time>` elements in a calendar

+ The `datetime` attribute
  + used for indicating a date/time or a duration
  + Different syntaxes of the datetime attribute

    <table style="text-rendering: optimizelegibility; border-spacing: 0px; margin: 20px 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'PT Sans', Arial, Helvetica, sans-serif; font-size: 13px; font-stretch: inherit; line-height: 25px; vertical-align: baseline; width: 814px; max-width: 100%; margin: auto;" cellpadding="10" border="1">
    <caption style="font-size: 1.2em;">Different syntaxes of the <span style="font-family: 'courier new', courier;">datetime attribute</caption>
    <tbody>
    <tr><th scope="”row”">datetime attribute values</th><th scope="”row”">Interpretation</th></tr>
    </tbody>
    <tbody style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The year 2020</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 2020</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="11-13"&gt;&nbsp;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 13th (any year)</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-W21"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Week 21 from year 2020</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11-13 09:00"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 13th year 2020, time = 9:00</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11-13<span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; color: #ff0000;">T09:00"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Same as previous example, both syntaxes are supported, with and without the "T" between date and time.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00Z"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00-05"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT minus 5 hours</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00+05:45"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT plus 5 hours 45 minutes, (for example, Nepal&nbsp;is 5:45 ahead of&nbsp; GMT)</td>
    </tr>
    </tbody>
    </table>

  + duration values
    + format: `<time datetime="P4D">` = `<time datetime="P 4 D">`
      + prefix “P” for “period”
      + a duration value that ends with another letter indicating the unit used
      + unit
        + "D" for "days"
        + “H” for hours
        + “M” for minutes
        + “S” for seconds
    + “T” after the “P” marker indicating a more accurate duration time, e.g., `<time datetime="PT4H 6M 12.55S">` a duration of 4 hours, 6 minutes and 12.55 seconds
    + the <time> element with no attributes
      + the value between the opening `<time>` and closing `</time>` should follow the syntax given by the specification
      + recommended to use a `datetime` attribute

+ The `<mark>` element
  + used for indicating text as marked or highlighted for reference purposes
  + useful cases
    + search results with search strings highlighted
    + highlight important parts of a text
    + replacing `<strong>` and `<em>` with `<mark>` when suitable
  + change default style: using `background-color` and `color`

+ The `download` attribute
  + download resources rather than navigating to them
  + example

    <div class="source-code"><ol class="linenums">
    <li style="margin-bottom: 0px;">&lt;a</span> </span>href</span>=</span>"normal.gif"</span></span> </span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">download</span>=</span>"MichelBuffa.gif"</span></span></span>&gt;</span></li>
    <li style="margin-bottom: 0px;">&nbsp; &nbsp; download a picture of Michel Buffa</span></li>
    <li style="margin-bottom: 0px;">&lt;/a&gt;</span></li>
    </ol></div>
  
    + force the download of an image with a filename different from its original filename on the server side
    + original image" "normal.gif"
    + downloaded file: "MichelBuffa.gif"
  + security: the image should be located on the same domain as the HTML page that contains the link

+ The HTML5 `translate` attribute
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
    + e.g., `<span translate="no" class="author">Michel Ham</span>`


### 1.4.1 The `<details>` and `<summary>` elements

These elements have been introduced for displaying a foldable zone in an HTML document.

In the screenshot below, taken from the W3C specification page, the text next to the horizontal arrow is a `<summary>` element, and the text displayed when we click on the summary part, is the `<details>` element. This is a sort of "accordion" with foldable content.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y43kqw9a"
    alt    ="Example of summary details elements from the W3C specification"
  />
  <figcaption> Example of summary details elements from the W3C specification </figcaption>
</figure>


The `<details>` element generates a simple widget to show/hide element contents, optionally by clicking on its child `<summary>` element.

Here is an example of what can be done using these elements ) see the [online version on JSBin](https://jsbin.com/yociyel/1/edit?html,css,js,output) or [local version](src/1.4.1-foldable.html):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y5m3tfwu"
    alt    ="Example of folded summary details"
  />
  <figcaption> Example of folded summary details </figcaption>
</figure>


And here is what is displayed after clicking on the small arrow-shaped icon to the left of the summary:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y39xph3f"
    alt    ="Example of summary details unfolded"
  />
  <figcaption> Example of summary details unfolded </figcaption>
</figure>


Here is the code of this example:

```html
<!DOCTYPE html>
<html lang="en"> ...
<body>
<details>
<summary>
```

How to beat the boss...spoiler alert !

```html
</summary>
<p> Just aim to the red spots near his eyes</p>
<p>Keep shooting at these spots until the eyes open, then hit quickly both eyes with your laser beam.</p>
</details>
</body>
</html>
```

The `<summary>...</summary>` is inside a `<details>...</details>` element. By clicking on the icon at the left of the summary, the content of the `<details>` value is displayed/hidden.

`<details>` blocks can be embedded inside one another, like in this [example](https://tinyurl.com/yxfd49zd) ([local example](src/1.4.1-foldable2.html)):

Step 1: all folded:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y466jecb"
    alt    ="Other example, unfolded"
  />
  <figcaption> Other example, unfolded </figcaption>
</figure>


Step 2: click on top level summary icon, the first "hidden" part appears...

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/yxfph294"
    alt    ="The unfolded content contains in turn a summary details folded"
  />
  <figcaption> The unfolded content contains in turn a summary details folded </figcaption>
</figure>

Step3: click on embedded summary icon inside the part that has been previously unfolded

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y6m5hp3q"
    alt    ="We unfolded the summary details inside the previous summary details. Recursive accordeons!"
  />
  <figcaption> We unfolded the summary details inside the previous summary details. Recursive accordeons! </figcaption>
</figure>


Source code of this example, see the summary/details inside another one:

```html
<details>
<summary>
  How to beat the boss...spoiler alert !
</summary>
  <p> Just aim to the red spots near his eyes</p>
  <p>Keep shooting at these spots until the eyes open, then hit quickly both 
    eyes with your laser beam.</p>
<details>
<summary>
  Bonus and spoiler No 2: get a new weapon by cutting the tail of the boss.
</summary>
  <p>Before finishing him, try to cut his trail, you will get a new weapon</p>
  <p>Just try to stay behind him as long as you can, hitting his tail with 
    your melee weapon, after a few hits the trail will fall and you will get 
    a new bonus weapon, then finish the boss.</p>
</details>
</details>
```


#### CSS pseudo classes for styling summary icons

There are CSS pseudo classes to style this icon when it is in the open or closed state. Support for these is still incomplete as of June 2020 (works on Google Chrome, Opera, Safari, not in FF).

Example 1 (see [online example](https://tinyurl.com/y3urv4kl) or [local example](src/1.4.1-example1.html)):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y3uydq7o"
    alt    ="Styling the open/close icon"
  />
  <figcaption> Styling the open/close icon </figcaption>
</figure>


The color and background of the icon on the left are specified by the following CSS rule, which uses the pseudo class `::-webkit-details-marker`

In this example: red arrow, white background.

```css
summary::-webkit-details-marker {
  color:#FF0000;
  background:#FFFFFF;
}
```

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y2mpn9ov"
    alt    ="Styled summary details icon, unfolded state"
  />
  <figcaption> Styled summary details icon, unfolded state </figcaption>
</figure>


Once opened, the selector `details[open]` can style the icon when `<details>` is unfolded. In this example: blue arrow, turquoise background. Here is the corresponding CSS rule:

```css
details[open] summary::-webkit-details-marker {
  color:#0000FF;
  background:#00FFFF;
}
```

It is also possible to change the icon itself using the CSS pseudo class `:after`

Example 2 (see it [online](https://jsbin.com/sajusop/edit?html,css,output) or [local example](src/1.4.1-example2.html)):

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2g33b8t" ismap target="_blank">
    <img style="margin: 0.1em;" width=250
      src  ="https://tinyurl.com/y466jecb" 
      alt  ="A + as a custom open icon for summary" 
      title="A + as a custom open icon for summary"
    >
    <img style="margin: 0.1em;" width=250
      src  ="https://tinyurl.com/y6blnkz5" 
      alt  ="A '-' as a custom close icon" 
      title="A '-' as a custom close icon"
    >
  </a>
</div>


CSS rules used in this example:

Use a "+" shaped icon, pink, bold, etc... :

```css
summary:after {
  content: "+";
  color: #FF00FF;
  float: left;
  font-size: 1.5em;
  font-weight: bold;
  margin: -5px 5px 0 0;
  padding: 0;
  text-align: center;
  width: 20px;
}
```

Use a "-" shaped icon, white, when details are displayed:

```css
details[open] summary:after {
  content: "-";
  color: #FFFFFF
}
```


#### Current browser support

+ On CanIUse: [compatibility table for details and summary elements](https://tinyurl.com/yy6tdwf8)


#### Knowledge check 1.4.1

1. Select the good way to define the widget:

  a.  
    ```html
    <summary>
    <details>
    How to beat the boss
    </detaill>
    </summary>
    ```

  b.  
    ```html
    <summary>
    How to beat the boss
    </summary>
    <details>
    <p> Just aim to the red spots near his eyes </p>
    </details>
    ```

  c.  
    ```html
    <details>
    <summary>
    How to beat the boss
    </summary>
    <p> Just aim to the red spots near his eyes </p>
    </details>
    ```
  
  Ans: c<br/>
  Explanation: The right answer is the third one. `<details>` contains one `<summary>`, and eventually other details/summary pairs.


### 1.4.2 The `<time>` and `<mark>` elements


#### The `<time>` element

The `<time>` element is useful for marking a time or a duration in a document.

It provides both a human readable part (the part between `<time>` and `</time>`) and a machine readable part contained within a datetime attribute. Dates are expressed as `YYYY-MM-DD`.

The machine readable part adds semantics that can be used by search engines for indexing, by browsers or by browser extensions, or by JavaScript code. Useful scenarios include generating alerts for birthdays, automatically adding dates or events that contain `<time>` elements in a calendar, etc.

Example:

```shell
We open at <time>10:00</time> every morning.

I have a meeting the <time datetime="2020-02-14">Monday 14/02/2020.</time>.
Blog posts from the year <time datetime="2020">2020</time>.
Archives, blog posts for <time datetime="2020-04">April 2020</time>
This recipe was published by Michel the <time datetime="2020-04-16">April 16, 2020</time>.
```

#### The `datetime` attribute

The `datetime` attribute can be used for indicating a date/time or a duration.

__Date/time values__

Supports different specifications of time such as "a year", "a month in a year", "a week in a year", "a time", etc... 

Here are some examples:


<table style="text-rendering: optimizelegibility; border-spacing: 0px; margin: 20px 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'PT Sans', Arial, Helvetica, sans-serif; font-size: 13px; font-stretch: inherit; line-height: 25px; vertical-align: baseline; width: 814px; max-width: 100%; margin: auto;" cellpadding="10" border="1">
<caption style="font-size: 1.2em;">Different syntaxes of the <span style="font-family: 'courier new', courier;">datetime attribute</span></caption>
<tbody>
<tr><th scope="”row”">datetime attribute values</th><th scope="”row”">Interpretation</th></tr>
</tbody>
<tbody style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The year 2020</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 2020</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="11-13"&gt;&nbsp;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 13th (any year)</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-W21"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Week 21 from year 2020</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11-13 09:00"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 13th year 2020, time = 9:00</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11-13<span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; color: #ff0000;">T09:00"&gt;</span></td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Same as previous example, both syntaxes are supported, with and without the "T" between date and time.</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00Z"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00-05"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT minus 5 hours</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00+05:45"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT plus 5 hours 45 minutes, (for example, Nepal&nbsp;is 5:45 ahead of&nbsp; GMT)</td>
</tr>
</tbody>
</table>


__Duration values__

Duration values use the prefix “P” for “period” as in `<time datetime="P4D">` (period = four days)...

So you start the attribute string value with a "P", followed by a duration value that ends with another letter indicating the unit used: "D" for "days",  “H” for hours, “M” for minutes and “S” for seconds. 

You can separate the different elements "P", value and unit with spaces, but this is optional. So `<time datetime="P4D">` is a duration of 4 days, as is `<time datetime="P 4 D">`.

Using a “T” after the “P” marker allows you to indicate a more accurate duration time: `<time datetime="PT4H 6M 12.55S">` is a duration of 4 hours, 6 minutes and 12.55 seconds.

Alternatively, you could use also a duration time component.

From Bruce Lawson's article : _"Whichever you choose, it’s represented internally as a number of seconds. Because of this, you can’t specify a duration in terms of months, because a month isn’t a precise number of seconds; a month can last from 28 to 31 days. Similarly, a year isn’t a precise number of seconds; it’s 12 months and February sometimes has an extra day._

_You still can’t represent dates before the Christian era, as years can’t be negative. Neither can you indicate date ranges. To mark up From “21/02/2012 to 25/02/2012″, use two separate `<time>` elements."_

Examples:

```html
<h2>Recipe:</h2>
<ul>
  <li> Preparation time: <time datetime="PT30M">30 minutes</time> </li>
  <li> Cooking time:     <time datetime="PT10M">10 minutes</time> </li>
</ul>
```

__The `<time>` element with no attributes__

Used without attributes, the value between the opening `<time>` and closing `</time>` should follow the syntax given by the specification so that machines can understand it (same syntax as the one presented for the datetime attribute in the previous section). However it is recommended to use a datetime attribute, as it gives more freedom in the way you can display the date/time/duration in a human-readable form. 

__External resources:__

+ From the [specification](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-time-element)
+ On [MDN's Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
  + MDN's browser compatibility [table](https://tinyurl.com/y4vc44nq) for `<time>`
+ Old but interesting [article](https://www.brucelawson.co.uk/2012/best-of-time/) by Bruce Lawson
+ A CSS Tricks' article: "[The 'time' element](https://tinyurl.com/y2wpzh64)"


#### The `<mark>` element

The HTML `<mark>` tag is used for indicating text as marked or highlighted for reference purposes, due to its relevance in another context.

Some use cases:

+ Display search results with search strings highlighted in the results.
+ &gt; Highlight important parts of a text, such as "quoting parts", etc.
+ Replace `<strong>` and `<em>` with `<mark>` when suitable.

Example 1: [jsBin online example](https://jsbin.com/tafelic/edit?html,output) and [local example](src/1.4.2-mark.html)

Source code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset=utf-8 />
<title>JS Bin</title>
</head>
<body>
  <p>Project is due in <mark>.zip format</mark> next monday.</p>
</body>
</html>
```

Example 2:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yy4j8cp3')"
    src    ="https://tinyurl.com/y4bdq5jq"
    alt    ="Another example for marking code"
    title  ="Another example for marking code"
  />
</figure>


Source code:

```html
<body>
<pre>
<code><mark>var</mark> i = 3;</code>
</pre>
<p>The var keyword is used to declare a variable in JavaScript.</p>
</body>
```

__Change the default style of the `<mark>` element__

If you don't like the default yellow background, you may use CSS to change the style of the `<mark>` element:

For example:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yy4j8cp3')"
    src    ="https://tinyurl.com/y6cmeaog"
    alt    ="style the mark element with CSS"
    title  ="style the mark element with CSS"
  />
</figure>


... comes with this CSS rule:

```css
mark {
    background-color: green;
    color: yellow;
}
```

__External resources:__

+ From the [specification](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-mark-element)
+ On [MDN's Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
  + MDN's browser compatibility [table](https://tinyurl.com/yydyaomy) for `<time>`
+ An article on Web Platform News: "[The `<mark>` element could help make your text more scannable](https://tinyurl.com/y3awtyhc)"


#### Knowledge check 1.4.3 

1. When would you use the mark element?<br/>
  a. To download a file<br/>
  b. To highlight a text<br/>
  c. To add a link<br/>
  d. To make a text bigger<br/>

  Ans: b


### 1.4.3 The download and translate attributes

Everyone knows the classic way to make hyperlinks, using `<a href="...">some text</a>`. What happens when you click on the hyperlink depends on the MIME type received by the browser. If you link to a file the browser knows how to render (an html page, a gif, jpg, or png image, etc.) there is a good chance that the MIME type received by the browser will be something like this:

<div><ol>
<li style="margin-bottom: 0px;" value="1">Content-type: text/html, text/plain, image/gif, image/jpg, etc.</li>
</ol></div>

For example,  HTML code such as this:

<div><ol>
<li style="margin-bottom: 0px;" value="1">&lt;a href="toto.jpg"&gt;</li>
<li style="margin-bottom: 0px;" value="2">&nbsp; &nbsp; please right click this link to download </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; the toto.jpg picture&lt;/a&gt;</li>
</ol></div>

...will ask the remote HTTP server to send back the `toto.jpg` file. The browser will receive in the response HTTP header from the server (and by default the browser will display the image in a new tab):

<div><ol>
<li style="margin-bottom: 0px;" value="1">...</li>
<li style="margin-bottom: 0px;"> Content-type: image/jpg</li>
<li style="margin-bottom: 0px;">...</li>
</ol></div>

However, if the link points to some PHP code, Java servlet code, or any kind of script/application on the server side, this remote server code can send in its HTTP response a `Content-type` that may force the browser to download the image instead of rendering it.

It may also propose a name for the file to be downloaded that may be different from the one that appears in the URL of the `href` attribute. This can be done by generating, in addition to the Content-type line in the response HTTP header, a `Content-Disposition` line that looks like this:

<div><ol>
<li style="margin-bottom: 0px;" value="1">Content-Disposition: attachment; filename="<span style="color:green;">MyImage.png</span>";</li>
</ol></div>

Here are some extracts from a Java Servlet that generate a zip file and forces the browser to propose downloading it using a specified name:

<div><ol>
<li style="margin-bottom: 0px;" value="1">protected void doGet(HttpServletRequest request, HttpServletResponse response) </li>
<li style="margin-bottom: 0px;"> throws ServletException, IOException { </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp;try {</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp;// Build the zip file</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;String path = getServletContext().getRealPath("data");</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;File directory = new File(path); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;String[] files = directory.list(); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;if (files != null &amp;&amp; files.length &gt; 0) { </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;byte[] zip = zipFiles(directory, files); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ServletOutputStream sos = response.getOutputStream(); </li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// generate a HTTP response that forces the download</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">response<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">.setContentType("application/zip"); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">response<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">.setHeader("Content-Disposition", </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">"attachment; filename=\"DATA.ZIP\""); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;sos.write(zip); sos.flush(); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;} </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp;&nbsp;} catch (Exception e) { </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;e.printStackTrace(); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp;&nbsp;} </li>
<li style="margin-bottom: 0px;"> }</li>
</ol></div>

The above example will cause the browser that invoked this server-side code to start the download of a file named "DATA.ZIP".


#### To download a file using an arbitrary name: the download attribute

HTML5 proposes the use of a new attribute named `download` to download resources rather than navigating to them. The example below shows how to trigger the download of an image by the browser (instead of rendering it, which is the default behavior) with a name different from the name of the resource.

<div><ol>
<li style="margin-bottom: 0px;">&lt;a href="normal.gif" <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">download="MichelBuffa.gif"&gt;</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; download a picture of Michel Buffa</li>
<li style="margin-bottom: 0px;">&lt;/a&gt;</li>
</ol></div>

This will indeed force the download of an image with a filename different from its original filename on the server side. Here is a screen capture of the Web browser while downloading the picture. We can see in the status bar the name of the link (the image is "`normal.gif`") and the downloaded file is "`MichelBuffa.gif`":

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y6rsz7qo')"
    src    ="https://tinyurl.com/y5nv7ert"
    alt    ="Image saved with another names thanks to the download attribute"
    title  ="Image saved with another names thanks to the download attribute"
  />
</figure>

<p style="border: 1px solid red; magin: 20px; padding: 20px; text-align: center;"><mark style="color:red;">WARNING</mark>: since 2015, and for security reasons, <strong>the image should be located on the same domain as the HTML page that contains the link</strong> (using a relative URL works well, for example, but linking a page on another domain will not work -&nbsp;it will keep its original name).</p>

__Interesting applications: serverless download__

Serverless download demo (by E.Bilderman)

This demo shows the use of the `download` attribute together with the HTML5 File, FileSystem and FileWriter APIs (to be studied later in this course) for generating on-the-fly content from JavaScript code, and proposing downloading it to a file.  

We won't detail this demo here, but take a look if you are curious to see what can be done with this new download attribute. As the FileWriter and FileSystem APIs are still supported only by Google Chrome (other browsers need polyfills), you will need Google Chrome to try it.

We have also put the simplified [source code of this demo on JSBin.com](https://jsbin.com/muluwey/1/edit?html,css,js,output) ([local demo](src/1.4.3-serverless.html)) for you to play with. See also the [original demo by E. Bilderman](https://tinyurl.com/y5x2avow).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y6rsz7qo')"
    src    ="https://tinyurl.com/y3t5k7pf"
    alt    ="Serverless download demo: type text in a text area, press download, enter a filename and voilà! you can download the textarea content into a file, without any server."
    title  ="Serverless download demo: type text in a text area, press download, enter a filename and voilà! you can download the textarea content into a file, without any server."
  />
</figure>


__External resources:__

+ From the specification: [downloading resources](https://tinyurl.com/y6ouvh6m)
+ From CanIUse: the [browser support of the `download` attribute](https://tinyurl.com/ybqjemqh)


#### The HTML5 translate attribute

HTML5 gives us a new `translate` attribute. This attribute is used to limit the impact of  translation tools such as [Google Translate](https://translate.google.com/) by prohibiting the translation of certain content. In many cases some parts of a document should not be translated.

Use cases include:

+ HTML pages that contain source code: you would certainly not like to see the Java or PHP or whatever programming language parts of your page translated into another spoken language!
+ Video game Web sites that propose cheat codes; the codes do not have to be translated,
+ Street names, author names in an "about" page must not be translated,
+ etc.

Both [Google translate](https://translate.google.com/) and [Microsoft online translation services](https://www.microsofttranslator.com/) already offer the ability to prevent translation of content by adding markup to your content, although they do it in (multiple) different ways. Hopefully, the new attribute will help significantly by providing a standard approach.


__Principle: give hints to translating tools__

[The specification about the translate attribute](https://tinyurl.com/y2hlgqyl) tells us that  "The translate attribute is an enumerated attribute that is used to specify whether an element's attribute values and the values of its Text node children are to be translated when the page is localized, or whether to leave them unchanged.

_The attribute's keywords are the empty string, yes, and no. The empty string and the yes keyword map to the yes state. The no keyword maps to the no state. In addition, there is a third state, the inherit state, which is the missing value default (and the invalid value default)."_


__Example illustrating how to specify parts of an HTML element that should not be translated:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;span</span><span class="pln"> </span><strong><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">translate</span><span class="pun">=</span><span class="atv">"no"</span></span></span></strong><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"author"</span><span class="tag">&gt;</span><span style="text-decoration: underline;"><span class="pln" style="color: #ff0000; text-decoration: underline;">Michel Ham</span></span><span class="tag">&lt;/span&gt;</span></li>
</ol></div>

In the above example, a `<span>` element defines an author (of a blog, for example) who is named Michel Ham. However, his family name is the same as pork and would be translated to "Michel Jambon" in French, or Michel Jamón in Spanish...

Using the translate="no" attribute should prevent this behavior...

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;span</span><span class="pln"> </span><strong><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">translate</span><span class="pun">=</span><span class="atv">"no"</span></span></span></strong><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"author"</span><span class="tag">&gt;</span><span style="text-decoration: underline;"><span class="pln" style="color: #ff0000; text-decoration: underline;">Michel Ham</span></span><span class="tag">&lt;/span&gt;</span><span class="pln"> is a professor </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> from the University of Nice,France. </span></li>
</ol></div>

Will be correctly translated into French by:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="str">"<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">Michel Ham</span></span> est un professeur de l'Université de Nice, France."</span></li>
</ol></div>

...where all of the end of the sentence has been translated except the author's name.


__Inheritance between elements__

When you define an element as not being translatable, its children inherit this behavior and are themselves not translatable. The reverse is also true. 

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;p</span><span class="pln"> </span><strong><span style="text-decoration: underline;"><span style="color: lightblue; text-decoration: underline;"><span class="atn">translate</span><span class="pun">=</span><span class="atv">"no"</span></span></span></strong><span class="tag">&gt;</span><span class="pln">This is a text in a paragraph element, that should not be translated: the p element has a translate="no" attribute.</span><span style="text-decoration: underline;"><span style="color: lightblue; text-decoration: underline;"><span class="tag">&lt;span&gt;</span><span class="pln"> This part that is in a span element embedded within the paragraph. It does not have a translate attribute but inherits the translation-mode of the p and will not be translated too</span><span class="tag">&lt;/span&gt;</span></span></span><span class="pln">. This is the end of the paragraph...&lt;/ p&gt;</span></li>
</ol></div>


#### External resources:

+ From the specification: [the translate attribute](https://tinyurl.com/yyzqajeg)
+ From [MDN's Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/translate)
  + Its corresponding [browser compatibility table](https://tinyurl.com/yxsvwpum)
+ An article from W3C's Internationalization Activity: ["Using HTML's translate attribute"](https://tinyurl.com/yy5pjwtp)


#### Knowledge check 1.4.4

<div class="source-code">
      <ol class="linenums">
        <li style="margin-bottom:0px;" class="L0" value="1">
          <span class="tag">&lt;a</span> <span class="pln"> </span> <span class="atn">href</span> <span class="pun">=</span> <span class="atv">"/images/batman_robin_car_superpower_007.rar"</span>
        </li>
        <li style="margin-bottom:0px;" class="L1">
          <span class="pln">    </span> <span class="atn">download</span> <span class="pun">=</span> <span class="atv">"Batmobile.rar"</span> <span class="tag">&gt;</span>
        </li>
        <li style="margin-bottom:0px;" class="L2">
          <span class="pln">    download a picture of Michel Buffa</span>
        </li>
        <li style="margin-bottom:0px;" class="L3">
          <span class="tag">&lt;/a&gt;</span>
        </li>
      </ol>
  </div>

1. What will be the name of the downloaded file?<br/>
  a. Batmobile.rar<br/>
  b. batman_robin_car_superpower_007.rar<br/>
  
  Ans: a



## 1.5 Microdata


### 1.5.0 Lecture Notes

+ machine-readable content embedded in a classical Web document:
  + HTML+RDFa
  + microformats
  + microdata

+ Macrodata
  + help search engines to better understand the pages' content, their topics, etc
  + main purpose: Search Engine Optimization (SEO)
  + pure semantic information
  + popular kinds of microdata
    + events
    + person's profile
    + description of an organization
    + details of a recipe
    + product description
    + geographical location
    + etc.
  + example use cases: `<dd itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">`
    + browser or browser extension: interpret an address and possibly propose to send it to a map application
    + web crawler: interpret as an address and display in its responses using a dedicated presentation layou
    + JavaScript code: access this data
    + event: pop up a calendar application, etc w/ other types of macrodata
  + attributes of macrodata: `itemprop`, `itemscope` and `itemtype`



### 1.5.1 Introduction

There are 3 ways to provide machine-readable content embedded in a classical Web document: [HTML+RDFa](https://www.w3.org/TR/html-rdfa/), [microformats](http://microformats.org/) and microdata. In this section, we focus on microdata.

Adding microdata to Web pages helps search engines to better understand the pages' content, their topics, etc. The main purpose of microdata is [Search Engine Optimization](https://tinyurl.com/kzk7kh4) (SEO).

This information is not visible to humans: it is pure _semantic information_. Popular kinds of microdata are events, a person's profile, the description of an organization, the details of a recipe, a product description, a geographical location, etc. 


#### Quick example of microdata that describes a person

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;section</span><span class="pln"> </span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">itemscope</span><span class="pln"> </span><span class="atn">itemtype</span><span class="pun">=</span><span class="atv">"https://schema.org/Person"</span></span></span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;h1&gt;</span><span class="pln">Contact Information</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;dl&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;dt&gt;</span><span class="pln">Name</span><span class="tag">&lt;/dt&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;dd</span><span class="pln"> </span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"name"</span></span></span><span class="tag">&gt;</span><span class="pln">Michel Buffa</span><span class="tag">&lt;/dd&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &lt;dt&gt;</span><span class="pln">Position</span><span class="tag">&lt;/dt&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="tag">&lt;dd&gt;&lt;span<span style="color: #000000;" color="#000000">&nbsp;</span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"jobTitle"</span></span></span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Professor/Researcher/Scientist</span><span class="tag">&lt;/span&gt;</span><span class="pln"> for</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="tag">&lt;span</span><span class="pln"> </span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"affiliation"</span></span></span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; University of Côte d'Azur, France</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;/span&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &lt;/dd&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;/dl&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">&lt;!-- SURFACE ADDRESS GOES HERE --&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;h1&gt;</span><span class="pln">My different online public accounts</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;ul&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;li&gt;&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://www.twitter.com/micbuffa"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="atv">"url"</span></span></span><span class="tag">&gt;</span><span class="pln">Twitter profile</span><span class="tag">&lt;/a&gt;&lt;/li&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;li&gt;&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://www.blogger.com/micbuffa"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="atv">"url"</span></span></span><span class="tag">&gt;</span><span class="pln">Michel Buffa's blog</span><span class="tag">&lt;/a&gt;&lt;/li&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;/ul&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/section&gt;</span></li>
</ol></div>

We can also add  another embedded data item in the middle, such as the person's address:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&lt;/</span><span class="pln">dl</span><span class="pun">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&lt;!--</span><span class="pln"> SURFACE ADDRESS GOES HERE </span><span class="pun">--&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">dd <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="str">"address"</span><span class="pln"> itemscope </span></span></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <span style="color: #ff0000;">itemtype</span></span><span style="color: #ff0000;"><span class="pun">=</span><span class="str">"https://schema.org/PostalAddress"</span></span><span class="pun">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">&lt;</span><span class="pln">span <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="str">"streetAddress"</span></span></span><span class="pun">&gt;</span><span class="lit">10</span><span class="pln"> promenade des anglais</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;&lt;</span><span class="pln">br</span><span class="pun">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">&lt;</span><span class="pln">span <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="str">"addressLocality"</span></span></span><span class="pun">&gt;</span><span class="typ">Nice</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;,</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">&lt;</span><span class="pln">span <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="str">"addressRegion"</span></span></span><span class="pun">&gt;</span><span class="typ">Alpes</span><span class="pln"> maritimes</span><span class="pun">,</span><span class="pln"> </span><span class="typ">France</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">&lt;</span><span class="pln">span <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="str">"postalCode"</span></span></span><span class="pun">&gt;</span><span class="lit">06410</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;&lt;</span><span class="pln">br</span><span class="pun">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">&lt;</span><span class="pln">span <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="str">"addressCountry"</span></span></span><span class="pln"><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"> itemscope</span></span> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="text-decoration: underline;">itemtype</span></span><span style="text-decoration: underline;"><span class="pun">=</span><span class="str">"https://schema.org/Country"</span></span><span class="pun">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">&lt;</span><span class="pln">span <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="str">"name"</span></span></span><span class="pun">&gt;</span><span class="typ">France</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&lt;/</span><span class="pln">dd</span><span class="pun">&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">&lt;h1&gt;</span><span class="typ">My</span><span class="pln"> different online </span><span class="kwd">public</span><span class="pln"> accounts</span><span class="pun">&lt;/</span><span class="pln">h1</span><span class="pun">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">...</span></li>
</ol></div>

In the following sections, we look more closely at the `itemprop`, `itemscope` and `itemtype` attributes.


#### Data that can be processed, organized, structured, or presented in a given context

Different use cases:

+ The browser, or a browser extension, may interpret the last example as an address and may propose to send it to a map application,
+ A Web crawler may interpret this as an address and display it in its responses using a dedicated presentation layout,
+ Some JavaScript code in the page can access this data,
+ With other types of microdata, for events, for example, the browser may pop up a calendar application, etc.

__Note__: For advanced users, Microdata is very similar to [microformats](http://microformats.org/), which use HTML classes, or to [RDFa](https://www.w3.org/TR/xhtml-rdfa-primer/), which doesn’t validate in HTML4 or HTML5. Because RDFa was considered to be too hard for authors to write, microdata is HTML5's answer to help embed semantics into html documents.


#### External resources

+ [W3C's HTML Microdata Working Draft](https://tinyurl.com/y4c2hgc9)
+ MDN's Web Docs: [Microdata](https://tinyurl.com/y6rmp6vj)
+ Very good [Microdata](https://tinyurl.com/y5nnjavp) paper from code{4}lib journal
+ [Microdata and the microdata DOM API](https://tinyurl.com/y8rkzlsp), old article from dev.opera.com
+ [Chapter from Mark Pilgrim's book about microdata](https://tinyurl.com/yy6bmkyb), very detailed introduction about semantic metadata in general, contains full examples with explanations about how to describe a Person, etc.


#### Knowledge check 1.5.1 

1. What is the correct proposition to define a city?<br/>
  a. `itemtype="http://schema.org/PostalAddress" and itemprop = "<br/>postalCode"`<br/>
  b. `itemtype="http://schema.org/Country" and itemprop = "name"`<br/>
  c. `itemtype="http://schema.org/PostalAddress" and itemprop = "addressLo<br/>cality"`<br/>
  d. `itemtype="http://schema.org/Country" and itemprop = "addressRegion"`<br/>

  Ans: c<br/>
  Explanation: A surface address is described with the http://schema.org/PostalAddress schema. The property that corresponds to the city is `addressLocality`. Visit the URL of the schema and read carefully the explanations for addressLocality.


### 1.5.2 Testing tools


#### Introduction

After seeing the principle of embedding microdata in an HTML page, we now present some structured data test tools you can use to check if your data are correct.

One of the most popular resources for testing microdata (as well as microformats and RDFa) is this [Google page about understanding how structured data works](https://tinyurl.com/pns8cwr). This page contains a link to a structured data testing tool that you can use to see how Google recognizes the semantic data you embed in your HTML code.


#### Testing a real interactive example with an "about page" for Michel Buffa

Let's have a look now at a (small) example of an about page. It renders as a very simple paragraph that explains who Michel Buffa is... But we embedded Microdata, so it's interesting to see how a search engine sees it, and how it may produce "augmented search results".

[Online example at JsBin](https://jsbin.com/gunuzus/1/edit?html,output) ([local example](src/1.5.2-about.html))

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">utf-8</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;title&gt;</span><span class="pln">Michel Buffa</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">itemscope</span><span class="pln"> </span><span class="atn">itemtype</span><span class="pun">=</span><span class="atv">"https://schema.org/Person"</span></span></span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; My name is </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"name"</span><span class="tag">&gt;</span><span class="pln">Michel Buffa</span><span class="tag">&lt;/span&gt;</span><span class="pln">,</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; And I'm a </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"jobTitle"</span><span class="tag">&gt;</span><span class="pln">professor/researcher</span><span class="tag">&lt;/span&gt;</span><span class="pln"> at</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://www.i3s.unice.fr/"</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"affiliation"</span><span class="tag">&gt;</span><span class="pln">I3S </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Laboratory</span><span class="tag">&lt;/a&gt;</span><span class="pln"> in the south of France, near the city of Nice. My </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; email </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; is : </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"email"</span><span class="tag">&gt;</span><span class="pln">micbuffa@gmail.com</span><span class="tag">&lt;/span&gt;</span><span class="pln">.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; I live in the city of </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;span</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"address"</span><span class="pln"> </span><span class="atn">itemscope</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span style="color: #ff0000;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; </span></span><span style="text-decoration: underline; color: #ff0000;"><span class="atn">itemtype</span><span class="pun">=</span><span class="atv">"https://schema.org/PostalAddress"</span></span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"addressLocality"</span><span class="tag">&gt;</span><span class="pln">Biot</span><span class="tag">&lt;/span&gt;</span><span class="pln">, in a region named</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"addressRegion"</span><span class="tag">&gt;</span><span class="pln">Alpes Maritimes</span><span class="tag">&lt;/span&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;/span&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/div&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

Rendering of the page in a browser:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yxkf4k76')"
    src    ="https://tinyurl.com/y3mrtrxs"
    alt    ="Microdata of the example, as seen by Google"
    title  ="Microdata of the example, as seen by Google"
  />
</figure>

Here is what Google sees of the page. We just entered its [URL](https://tinyurl.com/yyz7sy98) in the [Google page about rich snippets and structured data](https://tinyurl.com/pns8cwr):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yxkf4k76')"
    src    ="https://tinyurl.com/yyw2w52u"
    alt    ="Microdata of the example, as seen by Google"
    title  ="Microdata of the example, as seen by Google"
  />
</figure>

Note that the address is a fully featured embedded object in the Person's description.


#### Live Microdata

The [Live Microdata Web site](https://tinyurl.com/y35ozsyp) is a bit similar to the previous one except that it shows the extracted metadata as JSON objects and the JSON view of the microdata:: 

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/yxkf4k76" ismap target="_blank">
    <img style="margin: 0.1em;" height=250
      src  ="https://tinyurl.com/y5d3fmmo" 
      alt  ="example of live microdata from the previous example. Microdata are displayed as json objects" 
      title="example of live microdata from the previous example. Microdata are displayed as json objects"
    >
    <img style="margin: 0.1em;" height=250
      src  ="https://tinyurl.com/y5ud76hq" 
      alt  ="JSON view of the microdata" 
      title="JSON view of the microdata"
    >
  </a>
</div>






## 1.6 Exercises - Week 1







