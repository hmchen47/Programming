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

In the following video, you will hear from Bert Bos, the co-creator of CSS, about how he and Håkon Lie developed CSS.

Before CSS, the appearance of a Web page was dictated by HTML, which had very few visual styling tools, meaning most Web pages were looking simple. For example, here is what www.msn.com looked like in 1996:

<div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/b8efea36f1874c2a8a0fc6843d20b063/db3538e67b894874ace354d59ba6bf64/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40e1a1b7b99e4541f99c4aa3338277bac2">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f15f683b3186c39f5fb38a7e084e1d56/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/1-2-old_msn.PNG" style="margin: 0.1em;" alt="Image of msn.com from 1996" title="www.msn.com looked like in 1996" width="150">
  </a></div>
</div>

Link via [Web archive](http://web.archive.org/web/19961022175327/http://msn.com/)

For a fun time, warp check out an [archived version of that link above](http://web.archive.org/web/19961026005907/http://msn.com/tutorial/default.html) for anyone "new to the internet".

And here is what [www.msn.com](http://www.msn.com/) (made with lots of CSS) looks like now!

<div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/b8efea36f1874c2a8a0fc6843d20b063/db3538e67b894874ace354d59ba6bf64/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40e1a1b7b99e4541f99c4aa3338277bac2">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/dbbeddd8255315f712c52478e1328bdd/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/1-2_new_msn.PNG" style="margin: 0.1em;" alt="image of msn.com home page on 10/31/2016" title="www.msn.com appearance now!" width="250">
  </a></div>
</div>

#### Video: The history of CSS, by Bert Bos, co-inventor of CSS

<video src="https://edx-video.net/W3CCSS0I2016-V001700_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@c71419af1068400eaf481eee033ea084/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>

#### Before and after CSS

__Before CSS:__

+ all documents looked very similar - it was difficult for different companies to express their brand identities in documents
+ possibilities for styling were very limited and style was difficult to control and maintain - style had to be applied to content directly, so you couldn't update style without having to touch content and vice versa.

__After CSS:__

+ Content authors didn't have to worry about style, they could just focus on content
+ Content authors didn't have to worry about what device users would view their document on, those considerations could be handled by the CSS
+ Style became much more efficient- a single rule could apply to multiple elements and a single style sheet could apply to multiple documents.

#### CSS pioneers Bert Bos and Håkon Wium Lie

Bert Bos (W3C) and Håkon Wium Lie (YesLogic) were invited by [CWI](https://www.cwi.nl/) on Thursday 15 June 2017. They gave a lecture and a masterclass on these topics: 'A walk-through of CSS Grid' and 'CSS in print'.

They tweeted the following!

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://twitter.com/wiumlie/status/875659040851755008">
    <img src="https://pbs.twimg.com/media/DCb21_wWAAAa-o6.jpg" style="margin: 0.1em;" alt="The first mainstream #CSS implementation was by @chriswilson in IE3. WIthout it, CSS would just have been a spec. Chris left, Bert center." title="View image on Twitter" width="250">
  </a></div>
</div>



### Definitions

CSS, or Cascading Style Sheets, is a style sheet language used to describe the way an HTML or XML document should look to a user. CSS is where you specifiy the color, size, spacing, font and other visual aspects of the content that you create in your markup language document.

Most often you will see CSS used alongside HTML to describe the way a Web page looks and feels. You can have a Web page without CSS, but it would be very difficult to make it look the way you want with just HTML. This is why almost every Web page is a combination of HTML and CSS.

#### CSS • /si-ɛs-ɛs/ • noun 

Stands for "<b>C</b>ascading <b>S</b>tyle <b>S</b>heets". A style sheet language for describing how to display an HTML document.

Sample CSS document:

```css
body {
   background-color: #d0e4fe;
}
h1 {
   color: orange;
   text-align: center;
}
p {
   font-family: "Times New Roman";
   font-size: 20px;
}
```

#### HTML • /eɪʧ-ti-ɛm-ɛl/ • noun 

Stands for "<b>H</b>yper<b>T</b>ext </b>M</b>arkup <b>L</b>anguage", and it is the primary document format on the Web. It is a standardized system for tagging content on a web page so that a web browser knows how to present it properly to the viewer. It is a standardized way to describe a document's structure and the roles of the different parts of that document. 

Sample HTML document:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>My HTML page</title>
    </head>
    <body>
        <p> This is an HTML document </p>
    </body>
</html>
```

#### Web page • /wɛb peɪʤ/ • noun 

A hypertext document connected to the World Wide Web.

_synonyms: website, home page, landing page_

#### Internet

A global system of computer networks that connect to one another so that billions of different devices all over the world can share data. The internet is a collection of smaller networks that all combined create one large, all-inclusive global network.

#### World Wide Web

A collection of documents linked together by hypertext links, addressed using `Uniform Resource Locators (URLs)` accessible on the Internet. The World Wide Web is an application of the internet. 

_abbreviated as WWW or "the Web"_

#### Web browser • /wɛb ˈbraʊzər/ • noun

A software application for retrieving, presenting and traversing information resources on the World Wide Web.

_examples: edge, chrome, Firefox, internet explorer, safari, opera_


#### HTTP

Stands for "<b>H</b>yper<b>t</b>ext <b>T</b>ransfer <b>P</b>rotocol". It is a protocol managed by the W3C to dictate the manner in which Web pages share data on the World Wide Web. You might recognize this from the start of many Web addresses.

#### HTTPS

Stands for "<b>H</b>yper<b>t</b>ext <b>T</b>ransfer <b>P</b>rotocol <b>S</b>ecure". It  is the secure version of __HTTP__, the protocol over which data is sent between your browser and the Web site that you are connected to. It means all communications between your browser and the Web site are encrypted. Some examples of sites that use HTTPS include the W3C and Microsoft Web sites: https://www.microsoft.com/ - https://www.w3.org/



### Activity 1.2 - The Web before CSS

Now it's your turn to do some exploration! For this activity, your job is to find examples of Web sites before and after CSS.

A great place to start is at [archive.org](http://archive.org/) (aka, the "WayBack machine") which stores copies of web pages throughout history. You can search for some of your favorite websites and see if they have stored copies older than 1996. You should find that any Web page made before 1996 will look very different than Web sites we typically see today. When you find a real retro gem, please share it in this week's discussion (see below).

Here's one of my personal favorite vintage sites (which is still live!): http://www.warnerbros.com/archive/spacejam/movie/jam.htm

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/b8efea36f1874c2a8a0fc6843d20b063/db3538e67b894874ace354d59ba6bf64/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40e1a1b7b99e4541f99c4aa3338277bac2">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9b699b24c510fe8398ede6913f661b56/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/Space_Jam.jpg" style="margin: 0.1em;" alt="snapshot of a Web page showing SpaceJam" title="SpaceJam" width="250">
  </a></div>
</div>


Search result: NASA

+ Dec. 31, 1996: https://web.archive.org/web/19961231235847/http://nasa.gov/
+ Jul. 05, 1998: https://web.archive.org/web/19970605230559/http://www.nasa.gov:80/
+ Mar. 10, 2019: https://web.archive.org/web/20190310163403/https://www.nasa.gov/



## 1.3 Why CSS is important

### Separating content from presentation

Up until now, we have been discussing CSS's role within a Web site as the "presentation" component, but what is that and why is it so important?

From the history of CSS, we learned why CSS came about, but the short answer is simply because HTML was never designed to describe the way a Web page was supposed to look. When we use HTML for what it was intended to do, describe content, it leaves space for CSS to properly control a page's visuals. This makes it very easy to update or add content without having to even touch the style. 

#### Some benefits of CSS:

+ CSS has a host of specialized tools to give you powerful control over the look and feel of your Web site, much more powerful than the tools provided by HTML.
+ Designers can style many HTML pages with a single CSS document for a consistent look and feel across an entire Web page and less code to maintain.
+ Separation of content and presentation makes Web site maintenance much simpler as you can address updates in isolation.
+ Over time more and more devices have become internet-capable, and now there are so many different orientations in which your user can view your content. With CSS, you can specifically cater the style to each device to ensure an optimal experience.
+ Some users have specific presentation needs based on personal or technological limitations or preferences. Separating content from presentation allows these users the option to control how they view content.
+ Before CSS visual elements were almost always achieved with static images, which can have a big affect on network performance. CSS provides an optimized way to style your page so it can load complex visuals quickly. 

#### External resources:

+ [CSS design principles](https://www.w3.org/TR/CSS22/intro.html#design-principles)(CSS 2.2)
    + Forward and backward compatibility.
    + Complementary to structured documents.
    + Vendor, platform, and device independence.
    + Maintainability.
    + Simplicity.
    + Network performance.
    + Flexibility
    + Richness
    + Alternative language binding.
    + Accessibility
+ [Effective Use of Style Sheets](https://www.nngroup.com/articles/effective-use-of-style-sheets/) (updated regularly since 1997!)
    + Generalized Style
        + single style sheet for all of the pages on your site
        + linked style sheets
        + centralized design
        + active evangelism program
        + plenty of examples
        + page authors should be allowed to create additional embedded styles for their own pages
    + Implementation advice
        + continue to work when style sheets are disabled
        + Do not use more than two fonts
        + Do not use absolute font sizes
        + Do not use the `!important` attribute
        + use the same CLASS names for the same concept in all of the style sheets
+ [Repurposing of content](https://www.w3.org/People/Bos/DesignGuide/repurposing)
    <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="urhttps://www.w3.org/People/Bos/DesignGuide/repurposingl">
        <img src="https://www.w3.org/People/Bos/DesignGuide/communication.png" style="margin: 0.1em;" alt="The large circle in the diagram represents human communication with the Web as an intermediary: somebody has an idea (at the top); he represents it in a machine-readable way and enters it into the Web (the red part); the Web transports it and displays it to somebody; that somebody interprets what he sees (at the bottom) and may in turn become the originator of new ideas. There are various smaller circles in the diagram, that each represent modifications of the information, hopefully enhancements, but possibly degradations. The top circle, reflection, is a process under the control of the author; the bottom circle, different views, is controlled by the reader; but the circles in between can be done by either of them, by other people, or automatically by programs such as Web spiders. It is these smaller circles that represent the extra value that the Web can bring to human communication. But for them to work well, the original representation has to be suitable for manipulation by software. The collective name for the manipulations done in these smaller circles is repurposing, i.e., the adaptation of some piece of data for a new purpose." title="Repurposing of content" width="450">
    </a></div>
    </div>


### Meet CSS Zen Garden

These videos will introduce you to a web project titled "CSS Zen Garden". You can explore the project [here](http://www.csszengarden.com/)

Here is a bit about the project in their own words:

    "CSS Zen Garden is a demonstration of what can be accomplished through CSS-based design. Littering a dark and dreary road lay the past relics of browser-specific tags, incompatible DOMs, broken CSS support, and abandoned browsers. We must clear the mind of the past. Web enlightenment has been achieved thanks to the tireless efforts of folk like the W3C, WASP, and the major browser creators. There is a continuing need to show the power of CSS. The Zen Garden aims to excite, inspire, and encourage participation".

    - Dave Shea, Creator of CSS Zen Garden

#### Video: Meet CSS Zen Garden

<video src="https://edx-video.net/W3CCSS0I2016-V001300_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@27fc27d6d099462ca92f7bc8ff82edcc/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element. <br/>
  (Caption will be displayed when you start playing the video.) <br/>
  Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed 1.25xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Downloads and transcripts
</video>
 
<video src="https://edx-video.net/W3CCSS0I2016-V001200_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@8545c4f90be5473b922c2fb94a698c4c/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


#### View source and browser tools

In the above demo, you saw me using what is called the "developer tool" within my Edge Web browser to inspect and real-time change the style of a page's CSS. You can actually right click on any site and choose to look at the code that creates it. This feature exists in both Chrome and Firefox. Here is what I see when I _right click_ on a Web page in my browser.

As you can see, in this right click menu, there are two options: "Inspect element" and "View source". When you select view source, you can see the HTML and CSS powering that Web page. Here is what it looks like when I view the source of [W3C's Web site](https://www.w3.org/):

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/b8efea36f1874c2a8a0fc6843d20b063/7831c13150a1448e89fa66891665f6b3/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40067d426fc3c144dd925ae7bacb1c66fa">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/39801ab5481a246021dace754232588d/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/1-3-3_view_source.png" style="margin: 0.1em;" alt="Edge Web browser with view source window open" title="Web browser development tool" width="500">
  </a></div>
</div>


You can see a window that popped up from the bottom with all the HTML code for that site. Other Web browsers might pop this up in a separate window. 

You can also get more specific and look at individual HTML elements with the "Inspect element" option. Here is what it looks like in Edge when I inspect a specific title:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/b8efea36f1874c2a8a0fc6843d20b063/7831c13150a1448e89fa66891665f6b3/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40067d426fc3c144dd925ae7bacb1c66fa">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/79b1f75d786b6f5c411abe0621317f56/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/1-3-3_DOM_explorer.png" style="margin: 0.1em;" alt="Edge inspect element view highlighting a specific title" title="Web browser development tool-inspection & hightlight" width="500">
  </a></div>
</div>

As you can see, not only is the element highlighted on the page, but this also highlights the HTML code and shows you the CSS for that element on the right-hand side. In the video above, you can see me use this view to change the CSS and HTML real-time, which can be a very convenient way to play around with your designs.

As you work in your own sites you might want to use both of these features of your browser to understand what is happening in your own code, or in Web pages you find on the internet.


### Activity 1.3 - CSS Zen Garden critique

Now that you’ve gotten a good idea of what CSS Zen Garden is, take a closer look. Go to http://www.mezzoblue.com/zengarden/alldesigns/ and look through the different CSS Zen Garden designs for inspiration. Which is your favorite design? Pick one design and share your critiques with the discussion. 

For your chosen design, please answer the following questions:

+ What made this design stand out to you?
+ What do you like best about this design?
+ What is one thing you don't like about this design?

Ans:

Here is the design preferred: http://www.csszengarden.com/144/

The design mainly is soft green color what makes me feel comfortable.  A workd title section and followed with a banner photo.  The main section are with two columns while the main column (left one) using light green and the left navigation column with a slightly deeper green color.  

For my most browsing behavior is reading,  I usually look at screen for a long time.  Such a soft green them will easy my eyes while I read the contents for a long period of time.  

The main disadvantage is about the viewport width that is only about one third of the screen.  At least 90 percent of the viewport will make reading more easily.

## 1.4 Project 1 - Your first CSS

### "Hello beautiful world"

#### Video: "Hello beautiful world" Intro

<video src="https://edx-video.net/W3CCSS0I2016-V001100_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@359a8797107d4e54abe7c33db7e7031a/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>

#### Live coding video: "Hello beautiful world" Demo

<video src="https://edx-video.net/W3CCSS0I2016-V001500_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@2dd75d2bc0c348eaad01dc2b131a7c86/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>

#### Demo

Here is the [code](https://codepen.io/techie4good/pen/oxQaVN) we wrote in this demo.

Here is the HTML part:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <p>
      Hello Beautiful World
    </p>
  </body>
</html>
```

... and the CSS file (style.css) is below:

```css
p {
  color: blue;
  font-family:Helvetica;
}
```

... and here is the "output":

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/b8efea36f1874c2a8a0fc6843d20b063/137b958c31b147438258263a359ee926/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4012f12928c41749328bd588f657aab9bf">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/4fda62c8d7111a005f0871712d979395/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/1-4-1_hello_beautiful_world.PNG" style="margin: 0.1em;" alt="text" title="caption" width="200">
  </a></div>
</div>

### Comments

As you write your CSS, you might end up with a pretty large document that can be hard to manage, or you might find yourself working on a team and having to read CSS someone else has written. In these cases, it helps to leave "notes" for the humans that read the file.

There is a way to leave notes that the Web browser will ignore when it is reading your CSS code, they're called "comments". In fact, leaving comments in your code is considered a best practice by developers and is a habit we highly recommend you develop now.

To add comments to your CSS file, you need to surround any text you want the computer to ignore with a set of slashes and asterisks like so:

```css
/* those two symbols start my comment block
 I can have more comment text here
and the following two symbols end my comment */
```

As you can see, you can put as much text between the open and close symbols as you need, you can even have multiple lines. If you are working in an editor like Visual Studio code, you will notice that when you turn text into a comment, it turns green to indicate that the computer ignores that code.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="urhttps://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/b8efea36f1874c2a8a0fc6843d20b063/137b958c31b147438258263a359ee926/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4012f12928c41749328bd588f657aab9bfl">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9adb288f759490dc188a3c7484aa4896/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/1-4-2_Comments.PNG" style="margin: 0.1em;" alt="Image of Visual Studio Code Comments" title="Example of CSS comment" width="250">
  </a></div>
</div>

Generally, it is a good idea to put a comment at the top of each CSS rule, or at the very least at the top of sets of rules that apply to a single category or section of your Web page. 




### Module 1 project - Hello your world




## 1.5 Conclusion and exercises

### Module learnings




### Exercises (1-5)




### Exercises (6-9)




### Exercises (10-15)



