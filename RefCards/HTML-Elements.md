# HTML5 - Elements


## Definition and Characteristics of Elements

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



##  Metadata

+ [Document metadata](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Document_metadata)

  + Metadata contains information about the page. This includes information about styles, scripts and data to help software (search engines, browsers, etc.) use and render the page. Metadata for styles and scripts may be defined in the page or link to another file that has the information. 

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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



## Microdata

+ [Machine-readable content embedded in a classical Web document](../WebDev/Frontend-W3C/2-HTML5Coding/01e-Basics.md#151-introduction)
  + HTML+RDFa
  + microformats
  + microdata

+ [Microdata](../WebDev/Frontend-W3C/2-HTML5Coding/01e-Basics.md#151-introduction)
  + help search engines to better understand the pages' content, their topics, etc
  + main purpose: Search Engine Optimization (SEO)
  + pure semantic information
  + example use cases: `<dd itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">`
  + attributes of microdata: `itemprop`, `itemscope` and `itemtype`

+ [Microdata validation tools](../WebDev/Frontend-W3C/2-HTML5Coding/01e-Basics.md#152-testing-tools)
  + [Google page about rich snippets and structured data](https://tinyurl.com/pns8cwr)
  + The [Live Microdata Web site](https://tinyurl.com/y35ozsyp) w/ JSON view

+ [Microdata in HTML page](../WebDev/Frontend-W3C/2-HTML5Coding/01e-Basics.md#153-adding-microdata-to-an-html-page)
  + adding microdata requires only three attributes: `itemscope`, `itemtype` and `itemprop`
  + `itemscope` attribute
    + define a container element
    + define the "global object" for which properties defined
    + enable to add properties inside this element, e.g., the first name, last name, etc.
  + `itemtype` attribute:
    + specify the vocabulary used for the microdata container
    + HTML5 proposes
      + semantic elements for representing sections, articles, headers, etc.
      + none specific elements or attributes to describe an address, a product, a person, etc.
    + special vocabulary to represent a person or a physical address
      + define one's own vocabulary
      + reuse one of the existing popular vocabularies, such as [schema.org](https://schema.org/)
    + microdata with properties defined as name/value pairs
      + name: defined in the corresponding vocabulary
      + schema: a set of 'types', each associated with a set of properties
    + vocabulary probably links to another vocabulary
    + inheritance existed between vocabularies
    + analogy: properties as class attributes and vocabularies as classes
    + reuse vocabulary as the most popular vocabularies are becoming de facto standards
    + able to define a microdata vocabulary and embedding custom properties in one's own Web pages
  + `itemprop` attribute
    + each property defined inside element identified by the value
  + possible to nest microdata items inside one another
  + possible several properties with the same name but different values
  + possible to set more than one property at once, with the same value
  + Elements that can be associated with microdata

    <table style="table-layout: auto; text-rendering: optimizelegibility; border-spacing: 0px; margin: 20px 0px; padding: 0px; border: 1px solid #05050f; outline: 0px; font-family: 'PT Sans', Arial, Helvetica, sans-serif; font-stretch: inherit; line-height: 25px; vertical-align: baseline; max-width: 100%; width: 60vw; margin: auto;" frame="box" border="1">
    <tbody>
    <tr><th scope="”row”" style="width: 60%;">HTML5 elements</th><th scope="”row”" style="width: 40%;">microdata value associated</th></tr>
    </tbody>
    <tbody style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;a&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;area&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;audio&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;embed&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;iframe&gt;</code>,&nbsp;<br style="text-rendering: optimizelegibility; line-height: 1.4em;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;img&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;link&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;object&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;source&gt;</code>, or&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;video&gt;&nbsp;<br style="text-rendering: optimizelegibility; line-height: 1.4em;"></code>element</td>
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is the url in the element's&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">href</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">src</code>, or&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">data</code>&nbsp;attribute, as appropriate.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;time&gt;</code>&nbsp;element</td>
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is the time in the element's &nbsp; <code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">datetime</code> &nbsp;attribute.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"> <code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;"> &lt;meta&gt; </code> &nbsp;element</td>
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is whatever appears in the content attribute of the&nbsp; <code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;meta&gt;</code> &nbsp;element.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">anything else</td>
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is whatever is in the text of the element.<br><br></td>
    </tr>
    </tbody>
    </table>

+ [Microdata tools](../WebDev/Frontend-W3C/2-HTML5Coding/01e-Basics.md#154-microdata-tools)
  + The [Ultimate Microdata Generator](https://tinyurl.com/yaxpeuoq)
  + The [MicroData Generator](https://tinyurl.com/yyrpwsg7)
  + The [Schema Markup Generator (JSON-LD)](https://tinyurl.com/y6aupftz)


## Sectioning elements

+ [Sectioning Root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Sectioning_root)

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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

+ [Content sectioning elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Content_sectioning)
  + allow you to organize the document content into logical pieces. Use the sectioning elements to create a broad outline for your page content, including header and footer navigation, and heading elements to identify sections of content.

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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

+ [Sectioning elements](../WebDev/Frontend-W3C/2-HTML5Coding/01c-Basics.md#135-headings-and-structural-elements)
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
  + default content: anything not embedded in one of the sectioning elements

+ [Best practices of sectioning elements](../WebDev/Frontend-W3C/2-HTML5Coding/01c-Basics.md#136-best-practices-when-using-sectioning-elements)
  + always add a heading to explicit sectioning content
    + including a heading (a `<h1>, <h2>...<h6>`) in each sectioning element
    + the `<body>` element: sectioning root

  + using `<section>`, `<article>`, etc. instead of just `<h1>...<h6>`, not to rely  on implicit sectioning
    + `<header> `element
      + a container
      + not defining new sections of a document nor affecting the hierarchy levels
    + HTML not dedicated mechanism for marking up subheadings, alternative titles or taglines

+ [Table of contents](../WebDev/Frontend-W3C/2-HTML5Coding/01c-Basics.md#137-embedding-a-table-of-contents)
  + useful for debugging the structure of a page
  + checking the presence of headings after sectioning content
  + displaying some "untitled entries" $\to$ missing some headings

+ [The `<main>` element](../WebDev/Frontend-W3C/2-HTML5Coding/01c-Basics.md#138-the-main-element)
  + identify the main content of the document
  + provide a navigable document structure for assistive technology users as well as styling hooks for devs
  + supported by major modern browsers
  + constraints
    + no more than one `<main>` element in a document
    + not a descendant of an `<article>`, `<aside>`, `<footer>`, `<header>`, or `<nav>` element
  + best practice:
    + split page content into "regions" defined by the 5 elements (`aside`, `footer`, `header`, `main` and `nav`)
    + add a `<main>` to document if other sectioning elemets used

+ [Best practices](../WebDev/Frontend-W3C/2-HTML5Coding/01c-Basics.md#139-the-blog-example-applying-best-practices)
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

+ [Page layout](../WebDev/Frontend-W3C/2-HTML5Coding/01c-Basics.md#1310-examples-of-page-layouts)
  + 2 columns:
    + a `<section>` on the left and an `<aside>` on the right
    + using the float and width CSS properties
  + 3 columns:
    + centered, of equal size
    + using the float and width CSS properties
    + using the CSS flex property


## [Text content](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Text_content)

Use HTML text content elements to organize blocks or sections of content placed between the opening `<body>` and closing `</body>` tags. Important for accessibility and SEO, these elements identify the purpose or structure of that content.

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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


## Inline text semantic

+ [Inline text semantic](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Inline_text_semantics)

  + Use the HTML inline text semantic to define the meaning, structure, or style of a word, line, or any arbitrary piece of text.

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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


## Embedded content

+ [Embedded content](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Embedded_content)

  + In addition to regular multimedia content, HTML can include a variety of other content, even if it's not always easy to interact with.

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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


## Scripting

+ [Scripting](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Scripting)

  + In order to create dynamic content and Web applications, HTML supports the use of scripting languages, most prominently JavaScript. Certain elements support this capability.

    <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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


## Demarcaring edits

+ [Demarcating edits](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Demarcating_edits)

  + These elements let you provide indications that specific parts of the text have been altered.

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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


## Forms

+ [Forms](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Forms)

  + HTML provides a number of elements which can be used together to create forms which the user can fill out and submit to the Web site or application. There's a great deal of further information about this available in the HTML [forms guide](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms).

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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


## Interactive element

+ [Interactive element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Interactive_elements)

  + HTML offers a selection of elements which help to create interactive user interface objects.

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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

### The `download` attribute

+ [The `download` attribute](../WebDev/Frontend-W3C/2-HTML5Coding/01d-Basics.md#to-download-a-file-using-an-arbitrary-name-the-download-attribute)
  + download resources rather than navigating to them
  + example

    <div><ol>
    <li style="margin-bottom: 0px;">&lt;a href="normal.gif" <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">download</span>="MichelBuffa.gif"&gt;</li>
    <li style="margin-bottom: 0px;">&nbsp; &nbsp; download a picture of Michel Buffa</li>
    <li style="margin-bottom: 0px;">&lt;/a&gt;</li>
    </ol></div>
  
    + force the download of an image with a filename different from its original filename on the server side
    + original image: "normal.gif"
    + downloaded file: "MichelBuffa.gif"
  + security: the image should be located on the same domain as the HTML page that contains the link



## Embedded Content

### Characteristics of Embedded Elements

+ The [iframe](/WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#the-iframes-tag) tag
  + HTML Inline Frame Element
  + generally used in Web pages to show external content/resources
  + content not limited to other Web pages
  + ablt to styled just like other elements, with borders, margins, sizes specified with CSS rules
  + unable to identify if no borders, paddings, or margins specified
  + accessibility: some Web sites disallow their inclusion, including facebook, google
  + [W3C Specification](https://www.w3.org/TR/html5/embedded-content-0.html#the-iframe-element)
  + [W3S Specification](https://www.w3schools.com/tags/tag_iframe.asp)
  + Pros:
    + Iframes load separately from the main page.
      + block the main page's load command until its content finishes loading
      + overcome with JS script
    + Sandboxing provides security.
    + Great for third party content.
    + Convenient to use if requiring one part of a page static while the other changed
  + Cons: 
    + easy to misuse them
    + poor accessibility:
      + Screenreaders do not process them well
      + overcome by notices for tthe reader
    + no control over the content in an iframe to display
    + search engines having trouble to access


### The `iframe` Tag


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <caption style="font-size: 1.5em;"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#the-iframes-tag">Attributes of &lt;iframe&gt; tag</a></caption>
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


## The `<summary>` and `<details>` element

+ [Foldable zone in an HTML document](../WebDev/Frontend-W3C/2-HTML5Coding/01d-Basics.md#css-pseudo-classes-for-styling-summary-icons)
  + `<details>` element:
    + generate a simple widget to show/hide element contents
    + able to be embedded inside one another
  + `<summary>` element: (optional) children element of `<details>` element
  + `<summary>...</summary>` located inside a `<details>...</details>` element

+ [Styling summary icons w/ CSS](../WebDev/Frontend-W3C/2-HTML5Coding/01d-Basics.md#css-pseudo-classes-for-styling-summary-icons)
  + modifying color and background of the icon w/ `::-webkit-details-marker`

    <div><ol>
      <li style="margin-bottom: 0px;" value="1">summary::-webkit-details-marker {</li>
      <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;color:#FF0000; </li>
      <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;background:#FFFFFF; </li>
      <li style="margin-bottom: 0px;">}</li>
    </ol></div>

  + `details[open]` selector handling the unfolded `<details>`

    <div><ol>
    <li style="margin-bottom: 0px;" value="1">details[open] summary::-webkit-details-marker {</li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;color:#0000FF; </li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;background:#00FFFF;</li>
    <li style="margin-bottom: 0px;">}</li>
    </ol></div>

  + using `+` shaped icon for expansion

    <div><ol>
    <li style="margin-bottom: 0px;" value="1">summary:<span style="color: hotpink;">after {</li>
    <li style="margin-bottom: 0px;"> <span style="color: hotpink;">&nbsp;&nbsp;&nbsp;&nbsp;content<span style="color: hotpink;">: "+";</li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;color: #FF00FF;</li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;float: left;</li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;font-size: 1.5em;</li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;font-weight: bold;</li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;margin: -5px 5px 0 0;</li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;padding: 0;</li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;text-align: center;</li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;width: 20px;</li>
    <li style="margin-bottom: 0px;">}</li>
    </ol></div>

  + using `-` shaped icon to collapse details

    <div><ol>
    <li style="margin-bottom: 0px;" value="1">details<span style="color: hotpink;">[open]</span> summary:<span style="color: hotpink;">after {</li>
    <li style="margin-bottom: 0px;"> <span style="color: hotpink;">&nbsp;&nbsp;&nbsp;&nbsp;content: "-";</li>
    <li style="margin-bottom: 0px;"> &nbsp;&nbsp;&nbsp;&nbsp;color: #FFFFFF</li>
    <li style="margin-bottom: 0px;">}</li>
    </ol></div>


## The `<time>` element

+ [The `<time>` element](../WebDev/Frontend-W3C/2-HTML5Coding/01d-Basics.md#the-time-element)
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

+ [The `datetime` attribute](../WebDev/Frontend-W3C/2-HTML5Coding/01d-Basics.md#the-datetime-attribute)
  + used for indicating a date/time or a duration
  + Different syntaxes of the `datetime` attribute

    <table style="text-rendering: optimizelegibility; border-spacing: 0px; margin: 20px 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'PT Sans', Arial, Helvetica, sans-serif; font-stretch: inherit; line-height: 25px; vertical-align: baseline; width: 814px; max-width: 100%; margin: auto;" cellpadding="10" border="1">
    <caption style="font-size: 1.5em;">Different syntaxes of the <span style="font-family: 'courier new', courier;">datetime attribute</caption>
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
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11-13<span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; color: hotpink;">T</span>09:00"&gt;</td>
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
    + the <time> element w/o attributes
      + the value between the opening `<time>` and closing `</time>` should follow the syntax given by the specification
      + recommended to use a `datetime` attribute


## The `<mark>` element

+ [The `<mark>` element](#the-mark-element)
  + used for indicating text as marked or highlighted for reference purposes
  + useful cases
    + search results with search strings highlighted
    + highlight important parts of a text
    + replacing `<strong>` and `<em>` with `<mark>` when suitable
  + change default style: using `background-color` and `color`




