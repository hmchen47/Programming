# Module 2: [Building CSS rules](02-CSSRules.md)

## 2.1 Introduction

### Welcome to Module 2

In this module, we will...

1. Review the basics of HTML
1. Introduce you to the anatomy of a CSS "rule"
1. Introduce you to the concept of a property and give you a set of properties to get started
1. Introduce you to selectors and how you can directly attach them to HTML tags
1. Finally, for your module project, you'll get a get a chance to build the CSS for an HTML page from scratch

<video src="https://edx-video.net/W3CCSS0I2016-V001400_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@85d748fe0d994db0b2ccc5974d3a09df/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


## 2.2 HTML review

### HTML to get you started

#### Video: What is HTML?

<video src="https://edx-video.net/W3CCSS0I2016-V002300_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@96a429c1768f4ddea4d95f730135f9ea/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


#### HTML 101

HTML (<b>H</b>yper <b>T</b>ext <b>M</b>arkup <b>L</b>anguage) documents are made up of content and tags. These tags describe the content so that the web browser understands the structure of the page. HTML tags typically come in pairs, an opening tag before and a closing tag after content like so:

```html
<tagname>
    My content
</tagname>
```

When these three pieces are combined (start tag, content, and end tag), you have what is called an HTML __element__.

Here is a sample HTML doc:

```html
<!DOCTYPE html> <!-- Doctype declares the document to be HTML 5 type-->
<html lang="en"> <!--All your HTML content must be within this tag-->
    <head> <!--Anything in the header provides information about the document, no content here-->
        <meta charset="utf-8">
        <title>Page Title</title> <!--This text will show up on the tab of the browser for this page-->
    </head> <!--end for the header section-->
    <body> <!--start tag for the body section, this is where to put all your content to be displayed-->
        <h1>My First Heading</h1> <!--content in a h1 tag is a “heading” of the top level-->
        <p>My first paragraph.</p> <!--content in a p tag is normal or “paragraph” level text-->
    </body>
</html>
```

*NOTE: In the code above, the red text contained within the `<!--` and `-->` start and end sequences are comments. Each of them is explaining each tag.

Tags can be nested inside of other tags. This creates a parent/child relationship between HTML elements and forms the overall structure of your HTML document into a tree. This structure has a big affect on your CSS as styles are typically inherited from parent to child. We will take a closer look at style inheritance later in this unit.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/9dee69c0a62b4adea75199d9f4cef463/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40video%2Bblock%4096a429c1768f4ddea4d95f730135f9ea">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/62899e355f2553adbc85f3484da304dc/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-2-1_html_review.PNG" style="margin: 0.1em;" alt="Tags can be nested inside of other tags. This creates a parent/child relationship between HTML elements and forms the overall structure of your HTML document into a tree. This structure has a big affect on your CSS as styles are typically inherited from parent to child." title="HTML document anatomy" width="350">
  </a></div>
</div>


There are other types of tags that are called "self-closing", meaning they don't come in an open/close pair. Typically self-closing tags insert content into your page as opposed to surround content. They look like this:

```html
<img src="images/pic1.png" alt="pic1" />
```

As you can see these types of tags rely on "attributes", these are added modifiers on the tag that have their own values. In the above example, we use the src attribute to set the source for the image. You will also see attributes on the start tags of tag pairs and they can include a wide variety of added functionality for a tag.


### Common HTML tags




### Next steps - learn more HTML




### Activity 2.2




## 2.3 Building a CSS rule

### The anatomy of a CSS rule




### Constructing your CSS rules




### Activity 2.3 - Building your first CSS rule set




## 2.4 Attaching CSS to HTML using selectors

### What is a selector?




### Inheriting style




### Combining multiple selectors




### Activity 2.4 - Apply your own selectors




## 2.5 Applying styles using CSS properties

### What is a property?




### Color properties




### Font properties




### Spacing properties




## Activity 2.5 - Adding your own properties

### 2.6 Style studies




### Style studies




### Titles




### Buttons




### Activity 2.6




## 2.7 Project 2 - About me page

### Module 2 project - About me page




## 2.8 Conclusion and exercises

### After Module 2 you should be able to...




### Exercises (1-4)




### Exercises (5-10)




### Exercises (11-12)



