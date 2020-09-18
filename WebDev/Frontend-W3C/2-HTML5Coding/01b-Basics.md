# Week 1: HTML5 Basics

## 1.2 From HTML1.0 to HTML5


### 1.2.0 Lecture Notes

+ [HTML](#121-history-of-html-versions)
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

+ [HTML5](#122-what-is-html5)
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





