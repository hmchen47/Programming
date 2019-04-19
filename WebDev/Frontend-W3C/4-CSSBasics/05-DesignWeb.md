# Module 5: Designing your Web site for your audience

## 5.1 Introduction

### Welcome to Module 5

#### Video: welcome to Module 5

<video src="https://edx-video.net/W3CCSS0I2016-V005100_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@ff57fabe3b184e809f8cb9b31a2d3bb7/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


#### In this module, we'll...

+ Learn how to apply basic design principals based on the context of your HTML elements
+ Explore CSS and HTML's accessibility features and how you can design your page to accommodate a diverse audience
+ Introduce you to features to help internationalize your page and make it easier for those viewing it in different languages
+ Discuss the lessons learned from historical Web design trends and give you the new tech we use instead
+ Meet the newest fashions in Web design to help you give your Web pages a modern look and feel



### The importance of design

#### Video: the importance of design

<video src="https://edx-video.net/W3CCSS0I2016-V005200_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@05f1d31c3812439f84c6020adf4c1c8b/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


#### Web stats

Numerous studies have been done to determine exactly how important Web design is. Here are a few interesting stats to guide you:

+ 38% of people will stop engaging with a website if the content/layout is unattractive
+ 2 out of every 3 minutes spent on the Web are via a mobile device



### CSS best practices

You will find below an excerpt of CSS best practices (see the [full slide set](http://fantasai.inkedblade.net/style/talks/best-practices/#title)) that were written by Elika J. Etemad (also known as [fantasai](http://fantasai.inkedblade.net/)). Elika is an expert on the [W3C CSS Working Group](http://www.w3.org/Style/CSS/) (since 2004!) and a longtime contributor to the Mozilla Project. In addition to editing many of the CSS3 specifications, she’s worked on layout engine testing and development for Gecko and managing the CSS test suites at W3C.

#### Executive summary

+ __Logical source order__: The order of the HTML content should make sense even without the CSS: for accessibility, mobile optimization, device adaptability, and long-term maintainability.
+ __Liquid layouts and relativity__: Use smart relative sizing: to optimize layouts while minimizing media query code forks.
+ __Media queries__: Adapt to screen size changes; get font size adaptation free by using `em`s.
+ __Prevent zombie code__: Dead code may come alive as CSS changes. Delete it before it does, and ruins your layout.
+ __Test in multiple browsers__: Your favorite browser is not always right.
+ __Don't use proprietary features!__ Keep the Web open to everyone! Don't rely on the latest -WebKit- invention.
+ __Turn off CSS__: A well-coded page will be understandable without it.


#### Foundations

+ Indent your code for readability ease
+ Learn how to code CSS before relying on frameworks (such as Bootstrap, etc.)
+ __Separate content and style__
  + Use semantic markup, ie., "classes for meaning, not for show".  
    The following article is helpful to understand this concept: [Meaningful CSS: Style Like You Mean It](http://alistapart.com/article/meaningful-css-style-like-you-mean-it) (Tim Baxter, May 2016 - A list apart). It is also fully described in the [HTML5&CSS Fundamentals course](https://www.edx.org/course/html5-css-fundamentals-w3cx-html5-0x).
  + Use `<table>` for tabular data: don't use tables for layout, but if your content is tabular like a catalog, a calendar, or a price list, then the table element is the correct markup.
+ __Linearized logical source order__
  + The order of the HTML content should make sense even without the CSS.  
    Benefits are numerous as it _works best_:
    + for long-term site maintainability
    + for mobile
    + for accessibility
    + as a foundation for device adaptation (media queries)
+ __Linguistic variations__: set the language correctly for better typography (see the section entitled "[why Internationalization is important](https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+1T2017/courseware/12e8f1585d88470e95f54cf0ff6a1a00/ce75a56f15a940fe8b10d4e1650d85c0/3)")


#### Testing

+ __Test without CSS__: turn off CSS, and if the page makes no sense, fix your markup.
+ __Test in multiple environments__:
  + Resize the window
  + Zoom the text
  + Try a mobile browser
  + Navigate by keyboard
+ __Test in multiple browsers__: remember that just testing in Chrome does not work for everyone!  ;)


#### Adaptability

+ __Media queries__: set media query breakpoints in `em` or `ch`, not always in `px`.
+ __Liquid layouts and relativity__: what is your sizing based on?
  + Containing block size? → Use percents.
  + Viewport size? → Use viewport units: `vw`, `vh`, `vmin`, `vmax`
  + Font height? → Use `em` or `rem`.
  + Font pitch? → Use `em` or `ch`.
  + Content size? → Use `auto` or `min-content`/`max-content`.
  + Combination of the above? → Use the appropriate layout formulas: `flex`, `min-width`, `max-width`, etc.

Absolute units are usually the wrong answer.


#### Defensive Coding

+ `!important` means never override- to use with caution
+ Use `!important` to define overriding rules, not for fixups
+ Duplicate selectors if you need to increase specificity, or
+ Simplify selectors if you need to decrease specificity
+ __Don't over-escalate__: understand your code, and don't overkill.  
  For example, avoid:
  + `z-index: 9999999999999999999999999999999999999;`
  + `position: absolute; left: -10000000000px`
+ __Drop dead code__: you tried something and it didn't work? Delete it right away!
+ Code to Standard
+ Don't rely on proprietary extensions
+ Don't use experimental features in production or commit to keeping up-to-date.
+ Provide fallbacks / use @supports.



### The W3C CSS WG



## 5.2 The basics of design

### Applying basic design principals



### Typography



### Color



### White space



### Activity 5.2



## 5.3 Designing for your audience

### Intro to Web accessibility



### Inclusive design



### What is internationalization?



### Activity 5.3



## 5.4 Historical Web design trends

### The history of Web design



### Moving pieces



### Rigid layouts



### Heavy content



### Activity 5.4



## 5.5 Current Web design trends

### The current state of Web design



### Minimalism



### Long scrolling



### New layout techniques (OPTIONAL)



### CSS Grid layout (OPTIONAL)



### Activity 5.5



## 5.6 Project 5 - Apply good design

### Apply good design


