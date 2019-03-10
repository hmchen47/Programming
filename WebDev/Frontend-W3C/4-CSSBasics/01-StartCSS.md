# Module 1: Getting started with CSS

## 1.1 Introduction

### Welcome to Module 1

In this module, we'll...
1. Answer the question "What is CSS?"
1. Review the state of the Web before CSS, and how it came about
1. Show different examples of the amazing things you can do with CSS
1. Help you write your first CSS styles

<video src="https://edx-video.net/W3CCSS0I2016-V001000_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@4382c98f4ada46a78e8e2a5d3145519f/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


## 1.2 What is CSS?

### What is W3C?

<div style="font-size:1.2em;text-color: grey;">As steward of global Web standards, W3C's mission is to safeguard the openness, accessibility, and freedom of the World Wide Web from a technical perspective.</div>

W3C's primary activity is to develop protocols and guidelines that ensure long-term growth for the Web. This includes the development and maintenance of CSS. The widely adopted Web standards define key parts of what actually makes the World Wide Web work.

#### A few history bits

[Tim Berners-Lee](http://www.w3.org/People/Berners-Lee/) wrote a [proposal](http://www.w3.org/History/1989/proposal.html) in 1989 for a system called the World Wide Web. He then created the first Web browser, server, and Web page. He wrote the first specifications for URLs, HTTP, and HTML.

In October 1994, Tim Berners-Lee founded the World Wide Web Consortium (W3C) at the Massachusetts Institute of Technology, Laboratory for Computer Science [MIT/LCS] in collaboration with [CERN](http://www.cern.ch/), where the Web originated (see information on the [original CERN Server](http://www.w3.org/Daemon/)), with support from DARPA and the [European Commission](http://ec.europa.eu/index_en.htm).

In April 1995, [Inria](http://www.inria.fr/) became the first European W3C host, followed by [Keio University of Japan](http://www.keio.ac.jp/) (Shonan Fujisawa Campus) in Asia in 1996. In 2003, [ERCIM](http://www.ercim.org/) took over the role of European W3C Host from Inria. In 2013, W3C announced [Beihang University](http://ev.buaa.edu.cn/) as the fourth Host.

In addition to these four Host locations that employ [W3C staff](http://www.w3.org/Consortium/Offices/staff), there are W3C Offices around the globe that support the developer communities in their regions and organize local events. Find the one next to your place!

#### A few figures

As of September 2018, W3C is:

+ A [member](http://www.w3.org/Consortium/Member/List-driven organization composed of over 475 companies, universities, start-ups, etc. from all over the world.
+ 42 [technical groups](http://www.w3.org/Consortium/activities), including Working, and Interest Groups where technical specifications are discussed and developed.
+ Over 6428 [published technical reports](http://www.w3.org/TR/), including 407 Web standards (or W3C Recommendations) - since January 1st ,1995.
+ About 316 [Community and Business Groups](https://www.w3.org/community/groups/), where developers, designers, and anyone passionate about the Web have a place to hold discussions and publish ideas.
+ Near 12,034 active participants constituting the W3C community.
+ A [technical staff](http://www.w3.org/People/) composed of about 61 people, spread on all five continents.


#### LATEST NEWS!

Sir Tim Berners-Lee named recipient of the ACM A.M. Turing Award

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/b8efea36f1874c2a8a0fc6843d20b063/db3538e67b894874ace354d59ba6bf64/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40e1a1b7b99e4541f99c4aa3338277bac2">
    <img src="https://www.w3.org/2017/04/Timbl-medium.jpg" style="margin: 0.1em;" alt="Picture of Sir Tim Berners-Lee, ACM Turing Award logo" title="Sir Tim Berners-Lee" height="100">
    <img src="https://www.w3.org/2017/04/acm-turing-award.png" style="margin: 0.1em;" alt="Picture of Sir Tim Berners-Lee, ACM Turing Award logo" title="the ACM A.M. Turing Award" height="100">
  </a></div>
</div>

On Tuesday 4 April 2017, the ACM, the Association for Computing Machinery, named Sir Tim Berners-Lee, inventor of the Web and Director of the World Wide Web Consortium, as the recipient of the 2016 [ACM A.M. Turing Award](http://amturing.acm.org/). The Turing award is recognized as the highest distinction in Computer Science and is often referred to as the “Nobel Prize of Computing”.

Sir Tim is being given this award for inventing the World Wide Web, the first Web browser, and the fundamental protocols and algorithms allowing the Web to scale. The Web is considered one of the most influential computing innovations in history.


### The Web is amazing!

People often use the words "Internet" and "Web" interchangeably, but this usage is technically incorrect.

The Web is an application of the Internet. The Web is the most popular way of accessing the Internet, but other applications of the Internet are [e-mail](https://en.wikipedia.org/wiki/Email) and [ftp](https://en.wikipedia.org/wiki/File_Transfer_Protocol) for example. One analogy equates the Internet to a road network where the Web is a car, the email is a bicycle, etc.  Read [this article](https://www.lifewire.com/difference-between-the-internet-and-the-web-2483335) for more details about the difference between Internet and the Web.

The W3C community is passionate about creating free and open Web standards. This course discusses one of these Web standards, CSS, in detail. The next video, created in partnership with Microsoft, explains why standards are important to maintain a royalty-free, Open Web Platform, as well as to help shape the Web of the future.

<video src="https://edx-video.net/W3CHTML5/W3CHTML5T315-V000100_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@d5a6f51e6ebe4f6aba2ca7d71693f9fe/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


### The history of CSS




### Definitions




### Activity 1.2

## 1.3 Why CSS is important




### Separating content from presentation




### Meet CSS Zen Garden




### Activity 1.3




## 1.4 Project 1 - Your first CSS

### "Hello beautiful world"




### Comments




### Module 1 project - Hello your world




## 1.5 Conclusion and exercises

### Module learnings




### Exercises (1-5)




### Exercises (6-9)




### Exercises (10-15)



