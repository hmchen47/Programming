# Week 1: HTML5 Basics


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
    + event: pop up a calendar application, etc w/ other types of microdata
  + attributes of microdata: `itemprop`, `itemscope` and `itemtype`

+ Microdata validation tools
  + [Google page about rich snippets and structured data](https://tinyurl.com/pns8cwr)
  + The [Live Microdata Web site](https://tinyurl.com/y35ozsyp) w/ JSON view

+ Microdata in HTML page
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
    <tr><th scope="”row”">HTML5 elements</th><th scope="”row”">microdata value associated</th></tr>
    </tbody>
    <tbody style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;a&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;area&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;audio&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;embed&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;iframe&gt;</code>,&nbsp;<br style="text-rendering: optimizelegibility; line-height: 1.4em;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;img&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;link&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;object&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;source&gt;</code>, or&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;video&gt;&nbsp;<br style="text-rendering: optimizelegibility; line-height: 1.4em;"></code>element</td>
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is the url in the element's&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">href</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">src</code>, or&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">data</code>&nbsp;attribute, as appropriate. For example, an image element inside a container of personal contact information can be recognized as that person's photo and downloaded accordingly.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;time&gt;</code>&nbsp;element</td>
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is the time in the element's&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">datetime</code>&nbsp;attribute. This lets you, for example, just say "last week" in your text content but still indicate exact date and time.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;meta&gt;</code>&nbsp;element</td>
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is whatever appears in the content attribute of the&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;meta&gt;</code>&nbsp;element. This is used when you need to include some data that isn't actually in the text of your page.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">anything else</td>
      <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is whatever is in the text of the element.<br><br></td>
    </tr>
    </tbody>
    </table>


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


### 1.5.3 Adding microdata to an HTML page

#### Basic steps

Adding microdata to an HTML page is a really simple task and requires only three attributes: `itemscope`, `itemtype`  and `itemprop`.


__1 - Define a container element by adding an itemscope attribute__

First, you need to add an `itemscope` attribute to an HTML element. This will define the "global object" for which we will define properties. This element can be of different types that we will describe later, but for now let us keep looking at the same example we used in previous sections:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;section</span><span class="pln"> </span><span class="atn">itemscope</span><span class="pln"> </span><span class="atn">itemtype</span><span class="pun">=</span><span class="atv">"https://schema.org/Person"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/section&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;section</span><span class="pln"> </span><span class="atn">itemscope</span><span class="pln"> </span><span class="atn">itemtype</span><span class="pun">=</span><span class="atv">"https://schema.org/Person"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;h1&gt;</span><span class="pln">Contact Information</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;dl&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;dt&gt;</span><span class="pln">Name</span><span class="tag">&lt;/dt&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;dd</span><span class="pln"> </span><strong><span style="text-decoration: underline; color: #ff0000;"><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"name"</span></span></strong><span class="tag">&gt;</span><span class="pln">Michel Buffa</span><span class="tag">&lt;/dd&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;dt&gt;</span><span class="pln">Position</span><span class="tag">&lt;/dt&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;dd&gt;&lt;span<span style="color: #000000;" color="#000000">&nbsp;</span></span><strong><span class="atn"><span style="text-decoration: underline; color: #ff0000;">itemprop</span></span><span style="text-decoration: underline; color: #ff0000;"><span class="pun">=</span><span class="atv">"jobTitle"</span></span></strong><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Professor/Researcher/Scientist</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;/span&gt;</span><span class="pln"> for</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;span</span><span class="pln"> </span><strong><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"affiliation"</span></span></span></strong><span class="tag">&gt;</span><span class="pln">University of Nice, </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; France</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;/span&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;/dd&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;/dl&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;h1&gt;</span><span class="pln">My different online public accounts</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;ul&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;li&gt;&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://www.twitter.com/micbuffa"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>&nbsp;<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></strong></span><strong><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="atv">"url"</span></span></span></strong><span class="tag">&gt;</span><span class="pln">Twitter profile</span><span class="tag">&lt;/a&gt;&lt;/li&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;li&gt;&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://www.blogger.com/micbuffa"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemprop</span></span></strong></span><strong><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="atv">"url"</span></span></span></strong><span class="tag">&gt;</span><span class="pln">Michel Buffa's blog</span><span class="tag">&lt;/a&gt;&lt;/li&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;/ul&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/section&gt;</span></li>
</ol></div>

In this example, the container is a `<section>` that corresponds to a Person (we have one clue here: the name of the vocabulary given by the `itemtype` attribute), and each property defined inside this section is identified by the value of the `itemprop` attribute of sub-elements.

The line: 

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;dd</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"name"</span><span class="tag">&gt;</span><span class="pln">Michel Buffa</span><span class="tag">&lt;/dd&gt;</span></li>
</ol></div>

...defines a property called "name" that has a value of "Michel Buffa" (the text value between the opening and closing tags of the `<dd>` element).


__Nesting microdata items__

As we saw with the Person/Address example at the beginning of this chapter, it is possible to nest microdata items inside one another.

Give an element inside a microdata container its own `itemscope` attribute with the recommended `itemtype` attribute for indicating the name of the vocabulary used by the nested microdata.

Again, look at the Person/Address example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&lt;/</span><span class="pln">dl</span><span class="pun">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&lt;!--</span><span class="pln"> SURFACE ADDRESS GOES HERE </span><span class="pun">--&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">dd itemprop</span><span class="pun">=</span><span class="str">"address"</span><span style="text-decoration: underline;"><span class="pln" style="color: #ff0000; text-decoration: underline;"> itemscope </span></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemtype</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="str">"https://schema.org/PostalAddress"</span></span></span><span class="pun">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">&lt;</span><span class="pln">span itemprop</span><span class="pun">=</span><span class="str">"streetAddress"</span><span class="pun">&gt;</span><span class="lit">10</span><span class="pln"> promenade des anglais</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;&lt;</span><span class="pln">br</span><span class="pun">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">&lt;</span><span class="pln">span itemprop</span><span class="pun">=</span><span class="str">"addressLocality"</span><span class="pun">&gt;</span><span class="typ">Nice</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;,</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">&lt;</span><span class="pln">span itemprop</span><span class="pun">=</span><span class="str">"addressRegion"</span><span class="pun">&gt;</span><span class="typ">Alpes</span><span class="pln"> maritimes</span><span class="pun">,</span><span class="pln"> </span><span class="typ">France</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">&lt;</span><span class="pln">span itemprop</span><span class="pun">=</span><span class="str">"postalCode"</span><span class="pun">&gt;</span><span class="lit">06410</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;&lt;</span><span class="pln">br</span><span class="pun">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">&lt;</span><span class="pln">span itemprop</span><span class="pun">=</span><span class="str">"addressCountry"</span><span class="pln" style="color: #ff0000;"> itemscope </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">itemtype</span></span></span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pun">=</span><span class="str">"https://schema.org/Country"</span></span></span><span class="pun">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">&lt;</span><span class="pln">span itemprop</span><span class="pun">=</span><span class="str">"name"</span><span class="pun">&gt;</span><span class="typ">France</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">&lt;/</span><span class="pln">span</span><span class="pun">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&lt;/</span><span class="pln">dd</span><span class="pun">&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">&lt;h1&gt;</span><span class="typ">My</span><span class="pln"> different online </span><span class="kwd">public</span><span class="pln"> accounts</span><span class="pun">&lt;/</span><span class="pln">h1</span><span class="pun">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">...</span></li>
</ol></div>

The properties at _lines 8-12_ refer to the address nested microdata (they are defined in the Address vocabulary, not the Person vocabulary), and "France" (_line 14_) is a property that refers to the Country vocabulary.


__Several properties with the same name but different values__

It is possible to use the same property name several times in one microdata object, but with different values:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">...</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">&lt;h1&gt;</span><span class="typ">My</span><span class="pln"> different online </span><span class="kwd">public</span><span class="pln"> accounts</span><span class="pun">&lt;/</span><span class="pln">h1</span><span class="pun">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">&lt;ul&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">&lt;li&gt;</span><span class="pun">&lt;</span><span class="pln">a href</span><span class="pun">=</span><span class="str">"https://www.twitter.com/micbuffa"</span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pln"> itemprop</span><span class="pun">=</span><span class="str">"url"</span></span></span><span class="pun">&gt;</span><span class="typ">Twitter</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; profile</span><span class="pun">&lt;</span><span class="str">/a&gt;&lt;/</span><span class="pln">li</span><span class="pun">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">&lt;li&gt;</span><span class="pun">&lt;</span><span class="pln">a href</span><span class="pun">=</span><span class="str">"https://www.blogger.com/micbuffa"</span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="pln"> itemprop</span><span class="pun">=</span><span class="str">"url"</span></span></span><span class="pun">&gt;</span><span class="typ">Michel</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="typ">&nbsp; &nbsp; &nbsp; Buffa</span><span class="str">'s blog&lt;/a&gt;&lt;/li&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str"> &lt;/ul&gt;</span></li>
</ol></div>

This defines the fact that Michel Buffa has two online accounts, and the two properties have the name `url`, each with its own value.


__It is possible to set more than one property at once, with the same value__

Here are some microdata that represent a song. In this example, at line 5 we set  two different properties: `genre` and `keywords` with the same value (see the [MusicRecording schema definition](https://tinyurl.com/yxlrrp22)):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">itemscope</span><span class="pln"> </span><span class="atn">itemtype</span><span class="pun">=</span><span class="atv">"https://schema.org/MusicRecording"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h2&gt;</span><span class="pln">The song I just published</span><span class="tag">&lt;/h2&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;ul&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;li&gt;</span><span class="pln">Name: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"name"</span><span class="tag">&gt;</span><span class="pln">Please buy me on itunes, I need money!</span><span class="tag">&lt;/span&gt;&lt;/li&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;li&gt;</span><span class="pln">Band: </span><span class="tag">&lt;span</span><span class="pln"> </span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"genre keywords"</span></span></span><span class="tag">&gt;</span><span style="text-decoration: underline;"><span class="pln" style="color: #ff0000; text-decoration: underline;">Punk, Ska</span></span><span class="tag">&lt;/span&gt;&lt;/li&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/ul&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/div&gt;</span></li>
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
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;a&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;area&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;audio&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;embed&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;iframe&gt;</code>,&nbsp;<br style="text-rendering: optimizelegibility; line-height: 1.4em;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;img&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;link&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;object&gt;</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;source&gt;</code>, or&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;video&gt;&nbsp;<br style="text-rendering: optimizelegibility; line-height: 1.4em;"></code>element</td>
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is the url in the element's&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">href</code>,&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">src</code>, or&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">data</code>&nbsp;attribute, as appropriate. For example, an image element inside a container of personal contact information can be recognized as that person's photo and downloaded accordingly.</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;time&gt;</code>&nbsp;element</td>
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is the time in the element's&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">datetime</code>&nbsp;attribute. This lets you, for example, just say "last week" in your text content but still indicate exact date and time.</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;"><code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;meta&gt;</code>&nbsp;element</td>
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is whatever appears in the content attribute of the&nbsp;<code style="text-rendering: optimizelegibility; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; margin: 0px; padding: 2px 4px; border: 1px solid #e1e1e8; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; border-radius: 3px; color: cyan; white-space: nowrap; background-color: gray;">&lt;meta&gt;</code>&nbsp;element. This is used when you need to include some data that isn't actually in the text of your page.</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">anything else</td>
  <td style="text-rendering: optimizelegibility; border-color: #000000; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The data is whatever is in the text of the element.<br><br></td>
</tr>
</tbody>
</table>

For example, the value of a property defined in an `<img>` element will be the value of the src attribute:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"image"</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"MichelBuffa.png"</span><span class="pln"> </span><span class="atn">alt</span><span class="pun">=</span><span class="atv">"A great professor"</span><span class="tag">&gt;</span></li>
</ol></div>

Or for a `<time>`, it will be the value of the datetime attribute:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;time</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"birthday"</span><span class="pln"> </span><span class="atn">datetime</span><span class="pun">=</span><span class="atv">"1965-04-16"</span><span class="tag">&gt;</span><span class="pln">April 16, 1965</span><span class="tag">&lt;/time&gt;</span></li>
</ol></div>

Or for an `<a>` element, the value will be the value of the href attribute:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://www.twitter.com/micbuffa"</span><span class="pln"> </span><span class="atn">itemprop</span><span class="pun">=</span><span class="atv">"url"</span><span class="tag">&gt;</span><span class="pln">profile</span><span class="tag">&lt;/a&gt;</span></li>
</ol></div>


#### Knowledge check 1.5.3

1. What is the correct schema from schema.org for describing a person's address?<br/>
  a. https://schema.org/LocalAddress<br/>
  b. https://schema.org/PostalAddress<br/>
  c. https://schema.org/SurfaceAddress<br/>
  d. https://schema.org/Address<br/>

  Ans: b<br/>
  Explanation: The right schema is https://schema.org/PostalAddress.







