# Week 1: HTML5 Basics


## 1.5 Microdata


### 1.5.0 Lecture Notes

+ [Machine-readable content embedded in a classical Web document](#151-introduction)
  + HTML+RDFa
  + microformats
  + microdata

+ [Microdata](#151-introduction)
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
    + web crawler: interpret as an address and display in its responses using a dedicated presentation layout
    + JavaScript code: access this data
    + event: pop up a calendar application, etc w/ other types of microdata
  + attributes of microdata: `itemprop`, `itemscope` and `itemtype`

+ [Microdata validation tools](#152-testing-tools)
  + [Google page about rich snippets and structured data](https://tinyurl.com/pns8cwr)
  + The [Live Microdata Web site](https://tinyurl.com/y35ozsyp) w/ JSON view

+ [Microdata in HTML page](#153-adding-microdata-to-an-html-page)
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
      + e.g., [Person](https://tinyurl.com/yyyljzue) defines a set of property names, including
        + name: `Person`
        + address: defined by another vocabulary named `PostalAddress`
        + affiliation: defined by another vocabulary named `Organization`
        + etc.
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

+ [Microdata tools](#154-microdata-tools) - generators
  + The [Ultimate Microdata Generator](https://tinyurl.com/yaxpeuoq)
  + The [MicroData Generator](https://tinyurl.com/yyrpwsg7)
  + The [Schema Markup Generator (JSON-LD)](https://tinyurl.com/y6aupftz)



### 1.5.1 Introduction

There are 3 ways to provide machine-readable content embedded in a classical Web document: [HTML+RDFa](https://www.w3.org/TR/html-rdfa/), [microformats](http://microformats.org/) and microdata. In this section, we focus on microdata.

Adding microdata to Web pages helps search engines to better understand the pages' content, their topics, etc. The main purpose of microdata is [Search Engine Optimization](https://tinyurl.com/kzk7kh4) (SEO).

This information is not visible to humans: it is pure _semantic information_. Popular kinds of microdata are events, a person's profile, the description of an organization, the details of a recipe, a product description, a geographical location, etc. 


#### Quick example of microdata that describes a person

<div><ol>
<li value="1"><span>&lt;section</span><span> </span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>itemscope</span><span> </span><span>itemtype</span><span>=</span><span>"https://schema.org/Person"</span></span></span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;h1&gt;</span><span>Contact Information</span><span>&lt;/h1&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;dl&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;dt&gt;</span><span>Name</span><span>&lt;/dt&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;dd</span><span> </span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>itemprop</span><span>=</span><span>"name"</span></span></span><span>&gt;</span><span>Michel Buffa</span><span>&lt;/dd&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &lt;dt&gt;</span><span>Position</span><span>&lt;/dt&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; </span><span>&lt;dd&gt;&lt;span<span style="color: #000000;" color="#000000">&nbsp;</span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>itemprop</span><span>=</span><span>"jobTitle"</span></span></span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Professor/Researcher/Scientist</span><span>&lt;/span&gt;</span><span> for</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span>&lt;span</span><span> </span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>itemprop</span><span>=</span><span>"affiliation"</span></span></span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; University of Côte d'Azur, France</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;/span&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &lt;/dd&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;/dl&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;!-- SURFACE ADDRESS GOES HERE --&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;h1&gt;</span><span>My different online public accounts</span><span>&lt;/h1&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;ul&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;li&gt;&lt;a</span><span> </span><span>href</span><span>=</span><span>"https://www.twitter.com/micbuffa"</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"url"</span></span></span><span>&gt;</span><span>Twitter profile</span><span>&lt;/a&gt;&lt;/li&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;li&gt;&lt;a</span><span> </span><span>href</span><span>=</span><span>"https://www.blogger.com/micbuffa"</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"url"</span></span></span><span>&gt;</span><span>Michel Buffa's blog</span><span>&lt;/a&gt;&lt;/li&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;/ul&gt;</span></li>
<li><span>&lt;/section&gt;</span></li>
</ol></div>

We can also add  another embedded data item in the middle, such as the person's address:

<div><ol>
<li value="1"><span>...</span></li>
<li><span>&lt;/</span><span>dl</span><span>&gt;</span></li>
<li><span> </span></li>
<li><span>&lt;!--</span><span> SURFACE ADDRESS GOES HERE </span><span>--&gt;</span></li>
<li><span> </span></li>
<li><span>&lt;</span><span>dd <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"address"</span><span> itemscope </span></span></span></li>
<li><span>&nbsp; &nbsp; <span style="color: hotpink;">itemtype</span></span><span style="color: hotpink;"><span>=</span><span>"https://schema.org/PostalAddress"</span></span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;</span><span>span <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"streetAddress"</span></span></span><span>&gt;</span><span>10</span><span> promenade des anglais</span><span>&lt;/</span><span>span</span><span>&gt;&lt;</span><span>br</span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;</span><span>span <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"addressLocality"</span></span></span><span>&gt;</span><span>Nice</span><span>&lt;/</span><span>span</span><span>&gt;,</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;</span><span>span <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"addressRegion"</span></span></span><span>&gt;</span><span>Alpes</span><span> maritimes</span><span>,</span><span> </span><span>France</span><span>&lt;/</span><span>span</span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;</span><span>span <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"postalCode"</span></span></span><span>&gt;</span><span>06410</span><span>&lt;/</span><span>span</span><span>&gt;&lt;</span><span>br</span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;</span><span>span <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"addressCountry"</span></span></span><span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"> itemscope</span></span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="text-decoration: underline;">itemtype</span></span><span style="text-decoration: underline;"><span>=</span><span>"https://schema.org/Country"</span></span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;</span><span>span <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"name"</span></span></span><span>&gt;</span><span>France</span><span>&lt;/</span><span>span</span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;/</span><span>span</span><span>&gt;</span></li>
<li><span>&lt;/</span><span>dd</span><span>&gt;</span><span> </span></li>
<li><span> </span></li>
<li><span>&lt;h1&gt;</span><span>My</span><span> different online </span><span>public</span><span> accounts</span><span>&lt;/</span><span>h1</span><span>&gt;</span></li>
<li><span> </span></li>
<li><span>...</span></li>
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

<div><ol>
<li value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li><span>&lt;html lang="en"&gt;</span></li>
<li><span>&lt;head&gt;</span></li>
<li><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>utf-8</span><span> </span><span>/&gt;</span></li>
<li><span>&lt;title&gt;</span><span>Michel Buffa</span><span>&lt;/title&gt;</span></li>
<li><span>&lt;/head&gt;</span></li>
<li><span>&lt;body&gt;</span></li>
<li><span> </span><span>&lt;div</span><span> </span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>itemscope</span><span> </span><span>itemtype</span><span>=</span><span>"https://schema.org/Person"</span></span></span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; My name is </span><span>&lt;span</span><span> </span><span>itemprop</span><span>=</span><span>"name"</span><span>&gt;</span><span>Michel Buffa</span><span>&lt;/span&gt;</span><span>,</span></li>
<li><span>&nbsp; &nbsp; And I'm a </span><span>&lt;span</span><span> </span><span>itemprop</span><span>=</span><span>"jobTitle"</span><span>&gt;</span><span>professor/researcher</span><span>&lt;/span&gt;</span><span> at</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;a</span><span> </span><span>href</span><span>=</span><span>"https://www.i3s.unice.fr/"</span><span> </span><span>itemprop</span><span>=</span><span>"affiliation"</span><span>&gt;</span><span>I3S </span></li>
<li><span>&nbsp; &nbsp; Laboratory</span><span>&lt;/a&gt;</span><span> in the south of France, near the city of Nice. My </span></li>
<li><span>&nbsp; &nbsp; email </span></li>
<li><span>&nbsp; &nbsp; is : </span><span>&lt;span</span><span> </span><span>itemprop</span><span>=</span><span>"email"</span><span>&gt;</span><span>micbuffa@gmail.com</span><span>&lt;/span&gt;</span><span>.</span></li>
<li><span>&nbsp; &nbsp; I live in the city of </span></li>
<li><span>&nbsp; &nbsp; &lt;span</span><span> </span><span>itemprop</span><span>=</span><span>"address"</span><span> </span><span>itemscope</span><span> </span></li>
<li><span style="color: hotpink;"><span>&nbsp; &nbsp; &nbsp; &nbsp; </span></span><span style="text-decoration: underline; color: hotpink;"><span>itemtype</span><span>=</span><span>"https://schema.org/PostalAddress"</span></span><span>&gt;</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;span</span><span> </span><span>itemprop</span><span>=</span><span>"addressLocality"</span><span>&gt;</span><span>Biot</span><span>&lt;/span&gt;</span><span>, in a region named</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;span</span><span> </span><span>itemprop</span><span>=</span><span>"addressRegion"</span><span>&gt;</span><span>Alpes Maritimes</span><span>&lt;/span&gt;</span></li>
<li><span>&nbsp; &nbsp; &lt;/span&gt;</span></li>
<li><span> </span><span>&lt;/div&gt;</span></li>
<li><span>&lt;/body&gt;</span></li>
<li><span>&lt;/html&gt;</span></li>
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


### 1.5.3 Adding microdata to an HTML page

#### Basic steps

Adding microdata to an HTML page is a really simple task and requires only three attributes: `itemscope`, `itemtype`  and `itemprop`.


__1 - Define a container element by adding an itemscope attribute__

First, you need to add an `itemscope` attribute to an HTML element. This will define the "global object" for which we will define properties. This element can be of different types that we will describe later, but for now let us keep looking at the same example we used in previous sections:

<div><ol>
<li value="1"><span>&lt;section</span><span> </span><span>itemscope</span><span> </span><span>itemtype</span><span>=</span><span>"https://schema.org/Person"</span><span>&gt;</span></li>
<li><span>...</span></li>
<li><span>&lt;/section&gt;</span></li>
</ol></div>

We will look at the itemtype attribute later. Now that we have defined a global wrapper object/element (a Person in this case), we can  add properties inside this element to define the first name, last name, etc.


__2 - Specify the vocabulary used for your microdata with the itemtype attribute of the container element__

HTML5 proposes semantic elements for representing sections, articles, headers, etc, but it does not propose any specific elements or attributes to describe an address, a product, a person, etc.

We need a special vocabulary to represent a person or a physical address. With microdata you can define your own vocabulary or better, reuse one of the existing popular vocabularies, such as [schema.org](https://schema.org/). 

Microdata works with properties defined as name/value pairs. The names are defined in the corresponding vocabulary. For example, the vocabulary for representing a [Person](https://tinyurl.com/yyyljzue) defines a set of property names.

As you can see in this small extract from the vocabulary (also called a "schema"), a Person can have a name (some text), an Address (the type is defined by another vocabulary named PostalAddress), an affiliation (defined by another vocabulary named Organization) and so on.

We notice that one property, such as the address of a Person, may use another vocabulary. Yes, a vocabulary may link to another vocabulary! There is also inheritance between vocabularies! The above screenshot shows that the Person vocabulary inherits from a Thing vocabulary, and the five first properties of the table come from this vocabulary that describes things.

If you are a developer and if you are familiar with object oriented programming, think of properties as class attributes and think of vocabularies as classes.


__Vocabularies are meant to be shared__

If one of the existing vocabularies available at the schema.org Web site fits your needs, you should reuse it, as the most popular vocabularies are becoming de facto standards and will be taken into account by Web crawlers, browsers, and browser extensions.

However, if you do not find a vocabulary corresponding to your needs, keep in mind that anyone can define a microdata vocabulary and start embedding custom properties in their own Web pages. You need to define a namespace and put a description of your vocabulary in a Web page that has the name of your vocabulary.

__3 - Add properties using the itemprop attribute in HTML elements inside the container__


__Basics:__

Now that you have defined a container element, you may add properties to the HTML inside:

<div><ol>
<li value="1"><span>&lt;section</span><span> </span><span>itemscope</span><span> </span><span>itemtype</span><span>=</span><span>"https://schema.org/Person"</span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;h1&gt;</span><span>Contact Information</span><span>&lt;/h1&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;dl&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;dt&gt;</span><span>Name</span><span>&lt;/dt&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;dd</span><span> </span><strong><span style="text-decoration: underline; color: hotpink;"><span>itemprop</span><span>=</span><span>"name"</span></span></strong><span>&gt;</span><span>Michel Buffa</span><span>&lt;/dd&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;dt&gt;</span><span>Position</span><span>&lt;/dt&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;dd&gt;&lt;span<span style="color: #000000;" color="#000000">&nbsp;</span></span><strong><span><span style="text-decoration: underline; color: hotpink;">itemprop</span></span><span style="text-decoration: underline; color: hotpink;"><span>=</span><span>"jobTitle"</span></span></strong><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Professor/Researcher/Scientist</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;/span&gt;</span><span> for</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;span</span><span> </span><strong><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>itemprop</span><span>=</span><span>"affiliation"</span></span></span></strong><span>&gt;</span><span>University of Nice, </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; France</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;/span&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;/dd&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;/dl&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;h1&gt;</span><span>My different online public accounts</span><span>&lt;/h1&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;ul&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;li&gt;&lt;a</span><span> </span><span>href</span><span>=</span><span>"https://www.twitter.com/micbuffa"</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>&nbsp;<span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></strong></span><strong><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"url"</span></span></span></strong><span>&gt;</span><span>Twitter profile</span><span>&lt;/a&gt;&lt;/li&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;li&gt;&lt;a</span><span> </span><span>href</span><span>=</span><span>"https://www.blogger.com/micbuffa"</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemprop</span></span></strong></span><strong><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"url"</span></span></span></strong><span>&gt;</span><span>Michel Buffa's blog</span><span>&lt;/a&gt;&lt;/li&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;/ul&gt;</span></li>
<li><span>&lt;/section&gt;</span></li>
</ol></div>

In this example, the container is a `<section>` that corresponds to a Person (we have one clue here: the name of the vocabulary given by the `itemtype` attribute), and each property defined inside this section is identified by the value of the `itemprop` attribute of sub-elements.

The line: 

<div><ol>
<li value="1"><span>&lt;dd</span><span> </span><span>itemprop</span><span>=</span><span>"name"</span><span>&gt;</span><span>Michel Buffa</span><span>&lt;/dd&gt;</span></li>
</ol></div>

...defines a property called "name" that has a value of "Michel Buffa" (the text value between the opening and closing tags of the `<dd>` element).


__Nesting microdata items__

As we saw with the Person/Address example at the beginning of this chapter, it is possible to nest microdata items inside one another.

Give an element inside a microdata container its own `itemscope` attribute with the recommended `itemtype` attribute for indicating the name of the vocabulary used by the nested microdata.

Again, look at the Person/Address example:

<div><ol>
<li value="1"><span>...</span></li>
<li><span>&lt;/</span><span>dl</span><span>&gt;</span></li>
<li><span> </span></li>
<li><span>&lt;!--</span><span> SURFACE ADDRESS GOES HERE </span><span>--&gt;</span></li>
<li><span> </span></li>
<li><span>&lt;</span><span>dd itemprop</span><span>=</span><span>"address"</span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"> itemscope </span></span></li>
<li><span>&nbsp; &nbsp; <span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemtype</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"https://schema.org/PostalAddress"</span></span></span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;</span><span>span itemprop</span><span>=</span><span>"streetAddress"</span><span>&gt;</span><span>10</span><span> promenade des anglais</span><span>&lt;/</span><span>span</span><span>&gt;&lt;</span><span>br</span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;</span><span>span itemprop</span><span>=</span><span>"addressLocality"</span><span>&gt;</span><span>Nice</span><span>&lt;/</span><span>span</span><span>&gt;,</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;</span><span>span itemprop</span><span>=</span><span>"addressRegion"</span><span>&gt;</span><span>Alpes</span><span> maritimes</span><span>,</span><span> </span><span>France</span><span>&lt;/</span><span>span</span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;</span><span>span itemprop</span><span>=</span><span>"postalCode"</span><span>&gt;</span><span>06410</span><span>&lt;/</span><span>span</span><span>&gt;&lt;</span><span>br</span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;</span><span>span itemprop</span><span>=</span><span>"addressCountry"</span><span style="color: hotpink;"> itemscope </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">itemtype</span></span></span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>=</span><span>"https://schema.org/Country"</span></span></span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;</span><span>span itemprop</span><span>=</span><span>"name"</span><span>&gt;</span><span>France</span><span>&lt;/</span><span>span</span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;/</span><span>span</span><span>&gt;</span></li>
<li><span>&lt;/</span><span>dd</span><span>&gt;</span><span> </span></li>
<li><span> </span></li>
<li><span>&lt;h1&gt;</span><span>My</span><span> different online </span><span>public</span><span> accounts</span><span>&lt;/</span><span>h1</span><span>&gt;</span></li>
<li><span> </span></li>
<li><span>...</span></li>
</ol></div>

The properties at _lines 8-12_ refer to the address nested microdata (they are defined in the Address vocabulary, not the Person vocabulary), and "France" (_line 14_) is a property that refers to the Country vocabulary.


__Several properties with the same name but different values__

It is possible to use the same property name several times in one microdata object, but with different values:

<div><ol>
<li value="1"><span>...</span><span> </span></li>
<li><span> </span><span>&lt;h1&gt;</span><span>My</span><span> different online </span><span>public</span><span> accounts</span><span>&lt;/</span><span>h1</span><span>&gt;</span></li>
<li><span> </span><span>&lt;ul&gt;</span></li>
<li><span> </span><span>&lt;li&gt;</span><span>&lt;</span><span>a href</span><span>=</span><span>"https://www.twitter.com/micbuffa"</span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span> itemprop</span><span>=</span><span>"url"</span></span></span><span>&gt;</span><span>Twitter</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; profile</span><span>&lt;</span><span>/a&gt;&lt;/</span><span>li</span><span>&gt;</span></li>
<li><span> </span><span>&lt;li&gt;</span><span>&lt;</span><span>a href</span><span>=</span><span>"https://www.blogger.com/micbuffa"</span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span> itemprop</span><span>=</span><span>"url"</span></span></span><span>&gt;</span><span>Michel</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; Buffa</span><span>'s blog&lt;/a&gt;&lt;/li&gt;</span></li>
<li><span> &lt;/ul&gt;</span></li>
</ol></div>

This defines the fact that Michel Buffa has two online accounts, and the two properties have the name `url`, each with its own value.


__It is possible to set more than one property at once, with the same value__

Here are some microdata that represent a song. In this example, at line 5 we set  two different properties: `genre` and `keywords` with the same value (see the [MusicRecording schema definition](https://tinyurl.com/yxlrrp22)):

<div><ol>
<li value="1"><span>&lt;div</span><span> </span><span>itemscope</span><span> </span><span>itemtype</span><span>=</span><span>"https://schema.org/MusicRecording"</span><span>&gt;</span></li>
<li><span> </span><span>&lt;h2&gt;</span><span>The song I just published</span><span>&lt;/h2&gt;</span></li>
<li><span> </span><span>&lt;ul&gt;</span></li>
<li><span> </span><span>&lt;li&gt;</span><span>Name: </span><span>&lt;span</span><span> </span><span>itemprop</span><span>=</span><span>"name"</span><span>&gt;</span><span>Please buy me on itunes, I need money!</span><span>&lt;/span&gt;&lt;/li&gt;</span></li>
<li><span> </span><span>&lt;li&gt;</span><span>Band: </span><span>&lt;span</span><span> </span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;"><span>itemprop</span><span>=</span><span>"genre keywords"</span></span></span><span>&gt;</span><span style="text-decoration: underline;"><span style="color: hotpink; text-decoration: underline;">Punk, Ska</span></span><span>&lt;/span&gt;&lt;/li&gt;</span></li>
<li><span> </span><span>&lt;/ul&gt;</span></li>
<li><span>&lt;/div&gt;</span></li>
</ol></div>

And so on...

Now, let's see what elements are compatible with the `itemprop` attribute and where the values of the properties are located, depending on each element type.


#### The HTML elements compatible with the `itemprop` attribute

If the `itemprop` attribute appears on a:

<table style="table-layout: auto; text-rendering: optimizelegibility; border-spacing: 0px; margin: 20px 0px; padding: 0px; border: 1px solid #05050f; outline: 0px; font-family: 'PT Sans', Arial, Helvetica, sans-serif; font-stretch: inherit; line-height: 25px; vertical-align: baseline; max-width: 100%; width: 60vw; margin: auto;" frame="box" border="1"><caption>Elements that can be associated with microdata</caption>
<tbody>
<tr><th scope="”row”">HTML5 elements</th><th scope="”row”">microdata value associated</th></tr>
</tbody>
<tbody style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;a&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;area&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;audio&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;embed&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;iframe&gt;</code>,&nbsp;<br style="text-rendering: optimizelegibility; line-height: 1.4em;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;img&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;link&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;object&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;source&gt;</code>, or&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;video&gt;&nbsp;<br style="text-rendering: optimizelegibility; line-height: 1.4em;"></code>element</td>
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is the url in the element's&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">href</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">src</code>, or&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">data</code>&nbsp;attribute, as appropriate. For example, an image element inside a container of personal contact information can be recognized as that person's photo and downloaded accordingly.</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;time&gt;</code>&nbsp;element</td>
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is the time in the element's&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">datetime</code>&nbsp;attribute. This lets you, for example, just say "last week" in your text content but still indicate exact date and time.</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;meta&gt;</code>&nbsp;element</td>
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is whatever appears in the content attribute of the&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;meta&gt;</code>&nbsp;element. This is used when you need to include some data that isn't actually in the text of your page.</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">anything else</td>
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is whatever is in the text of the element.<br><br></td>
</tr>
</tbody>
</table>

For example, the value of a property defined in an `<img>` element will be the value of the src attribute:

<div><ol>
<li value="1"><span>&lt;img</span><span> </span><span>itemprop</span><span>=</span><span>"image"</span><span> </span><span>src</span><span>=</span><span>"MichelBuffa.png"</span><span> </span><span>alt</span><span>=</span><span>"A great professor"</span><span>&gt;</span></li>
</ol></div>

Or for a `<time>`, it will be the value of the datetime attribute:

<div><ol>
<li value="1"><span>&lt;time</span><span> </span><span>itemprop</span><span>=</span><span>"birthday"</span><span> </span><span>datetime</span><span>=</span><span>"1965-04-16"</span><span>&gt;</span><span>April 16, 1965</span><span>&lt;/time&gt;</span></li>
</ol></div>

Or for an `<a>` element, the value will be the value of the href attribute:

<div><ol>
<li value="1"><span>&lt;a</span><span> </span><span>href</span><span>=</span><span>"https://www.twitter.com/micbuffa"</span><span> </span><span>itemprop</span><span>=</span><span>"url"</span><span>&gt;</span><span>profile</span><span>&lt;/a&gt;</span></li>
</ol></div>


#### Knowledge check 1.5.3

1. What is the correct schema from schema.org for describing a person's address?<br/>
  a. https://schema.org/LocalAddress<br/>
  b. https://schema.org/PostalAddress<br/>
  c. https://schema.org/SurfaceAddress<br/>
  d. https://schema.org/Address<br/>

  Ans: b<br/>
  Explanation: The right schema is https://schema.org/PostalAddress.


### 1.5.4 Microdata tools

There are many tools available (most are free) that you can use for generating, visualizing and debugging microdata. We list some of them in this page, but feel free to share the tools you find / like in the forums.

__Microdata generators__

To automatically generate microdata for describing persons, restaurants, movies, products, organizations, etc., there is a wide variety of microdata generators such as these listed below (but do not hesitate to search for "microdata generators" using your favorite search engine, and you will find lots!):

+ The [Ultimate Microdata Generator](https://tinyurl.com/yaxpeuoq)
+ The [MicroData Generator](https://tinyurl.com/yyrpwsg7)
+ The [Schema Markup Generator (JSON-LD)](https://tinyurl.com/y6aupftz)

Example:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y3rbjs4c')"
    src    ="https://tinyurl.com/y4vxghlf"
    alt    ="Example of generator. I entered my name, job, city in a form and a text area next to it shows the corresponding HTML microdata"
    title  ="Example of generator. I entered my name, job, city in a form and a text area next to it shows the corresponding HTML microdata"
  />
</figure>


### 1.5.5 Examples of well structured documents with Microdata

Here, we propose a few links to Web pages that were created by students of previous editions of this course).

The students had to create a Web page to introduce themselves, with some information including: name, job, employer, location, etc., and of course enrich the page with microdata. They also had to follow the best practices concerning the new structural elements, headings, etc.

Click on these pages and look at the source code...

__Example #1__

Visit the [example #1 online](https://jsbin.com/cuzipa/edit?html,css,output) ([local example 1](src/1.5.5-example1.html))

Structure & Microdata:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/yxsjbyxd" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/y2uehosl"
      alt  ="picture of the first about me page example. Shows the table of content" 
      title="picture of the first about me page example. Shows the table of content"
    >
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/y43pha94"
      alt  ="microdata from the example page" 
      title="microdata from the example page"
    >
  </a>
</div>


__Example #2__

View the [example #2 online](https://jsbin.com/karemi/1/edit?html,output) ([local example 2](src/1.5.5-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yxsjbyxd')"
    src    ="https://tinyurl.com/yycvd4du"
    alt    ="Example page, shows table of content"
    title  ="Example page, shows table of content"
  />
</figure>




