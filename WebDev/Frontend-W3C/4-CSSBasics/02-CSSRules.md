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

There are many HTML tags to choose from depending on what elements you want to structure on your page. [You can always look up HTML tags here](https://www.w3.org/TR/html52/). However, here is a short list of some of the most common HTML tags, ones you'll see us use throughout this course.


#### html tag

The root element of a document is `<html>`, and this is the first tag you'll need in your document (after the DOCTYPE, of course!). All your other HTML tags should go inside this one, meaning all HTML documents should start with `<html>` at the top and end with `</html>` at the bottom.

You'll notice in the below code that we set the language to English (<`html lang="en">`) . You can [set another language](https://www.w3.org/International/tutorials/language-decl/#Slide0140) of the text in your page using language attributes (see also [this resource](https://www.w3.org/International/questions/qa-html-language-declarations)).

It is important that you take care to use the lang attribute to indicate the actual language of text in your page because many CSS features will function differently, depending on what language is declared here.

```html
<!DOCTYPE html>
<html lang="en">
   <body>
      <p> Hello World</p>
   </body>
</html>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/semantics.html#the-html-element)

#### head tag

This is the element that contains all the metadata for your site, such as your link to your CSS, the page's title and links to other files. This should be the first tag in your document, and there should only be one per document.

Note that this is where you will also set the charset to "utf-8" (<meta charset="utf-8">). This shows that you saved the markup using the UTF-8 character encoding, which has many characters outside English, so it should be able to display characters not in the English alphabet.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>My First Page</title>
    </head>
    <body>
        <p> Hello World</p>
    </body>
</html>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/document-metadata.html#the-head-element)


#### body tag

The section element that contains all the visible content for your site like your text, images, links etc. There should only be one body tag per document and it should come after the head tag.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>My First Page</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <p> Hello World</p>
    </body>
</html>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/sections.html#the-body-element)

#### Paragraph tag

"p" stands for "paragraph" which is a block of text that is physically separated from adjacent blocks through blank lines. This is the most basic way to group text content.

```html
<p>
   This is my introductory paragraph to my Web page! This text will wrap around in a single 
   block and then after the paragraph is done there will be a line of white space.
</p>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/grouping-content.html#the-p-element)


#### Anchor tag

By surrounding text with an `<a>` tag you turn it into a hyperlink. You will want to use the "href" attribute to indicate to which target the link should take the user when clicked. The default style of the a tag is to turn the text blue and underlined, and then change the color to purple after you have clicked the link. You can adjust all these styles with CSS.

```html
<a href="http://www.microsoft.com">Microsoft Main Page</a>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/textlevel-semantics.html#elementdef-a)


#### Image tag

This tag will insert an image based on the source you provide via the "src" attribute. If the source is inaccessible, you can also specify "fall back" options via the "alt" attribute. You will __always__ want to specify the "alt" attribute with a short phrase describing the image. This text is what will be read aloud if your user is using a screen reader, or will be displayed if the user's browser will not load images. Note that this is an example of a "self-closing" tag meaning there is no closing tag, you just end the opening tag with a forward slash. 

```html
<img src="images/proPic.jpg" alt="a headshot of the instructor" />
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/semantics-embedded-content.html#the-img-element)


#### Unordered-list tag

The UL tag creates an "unordered list" element, meaning a collection of elements in which the order is meaningless. This is a tag that sets the framework for you to add list elements inside it. You will want to add your elements within the ul tag each surrounded your content with list item or `<li>` tags like in the below example.

```html
<ul>
   <li>This is one element in the list</li>
   <li>One of the elements</li>
   <li>Another element</li>
</ul>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/grouping-content.html#the-ul-element)


#### Ordered-list tag

The OL tag works exactly like the UL tag, except that the list element order matters. OL stands for "ordered list" and by default, the list element items are displayed with a number preceding them.

```html
<ol>
   <li>This is the first element</li>
   <li>The second element</li>
   <li>Finally, this is the third element</li>
</ol>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/grouping-content.html#the-ol-element)


#### Link break tag

The br element is a self-closing tag that inserts a line break. This is most evident when placed in a block of text as it essentially represents a carriage return or hitting the "enter" key.

```html
<p>
   this is my text.
   <br />
   this text will appear on the next line down.
</p>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/textlevel-semantics.html#the-br-element)


#### Header tag

The header tag is one of the section elements, it's role is to group other HTML elements according to their role on their page. The header element contains all the introductory content on the page typically a title and tagline or navigational elements.

```html
<body>
   <header>
      <h1> Welcome to my page!</h1>
      <h2> My very first web page</h2>
   </header>
</body>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/sections.html#the-header-element)


#### Section tag

Another sectioning element, the "section" tag is a general-purpose grouping element. It most often should include a header tag at the top. This typically will come after a header tag and before a footer tag.

```html
<body>
   <header>
      <h1> My Page </h1>
   </header>
   <section>
      <h2> My Blog </h2>
   </section>
</body>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/sections.html#the-section-element)


#### Footer tag

Another sectioning element, the "footer" tag is supposed to organize the final content on the page such as the credits or contact info. 

```html
<body>
   <header>
      <h1>My Page</h1>
   </header>
   <section>
      <h2>My Blog</h2>
   </section>
   <footer>
      <p>
         copyright 2016
      </p>
   </footer>
</body>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/sections.html#the-footer-element)


#### Div tag

The div element is a generic element to hold content. It is considered a last resort, for when no other element is suitable but is often used to collect together large portions of a site that contain multiple different types of content. 

```html
<div>
   <h1> Title for Content </h1>
   <img src="images/contentImage.jpg" />
   <p> This is a paragraph explaining this section of content associated with the above image and title </p>
</div>
```

[Documentation](https://www.w3.org/TR/2016/WD-html52-20160818/grouping-content.html#the-div-element)


### Next steps - learn more HTML

Note that, as this CSS Introduction course focuses on CSS, we will always provide you with the complete HTML for whatever content you will be asked to style. However, to become proficient in Web development, you are going to need a good handle on HTML. You can start by looking into some of these links:

+ [Introduction section of the W3C HTML5 specification](https://www.w3.org/TR/html5/introduction.html#introduction)
+ [HTML educational material for beginners](https://www.w3.org/community/webed/wiki/HTML/Training) (W3C resource)

Or of you are looking for more in-depth training, we suggest you check out one of these other W3Cx courses to better understand how to structure your pages with HTML and more:

+ [HTML5&CSS Fundamentals](https://www.edx.org/course/html5-and-css-fundamentals) (beginner level)
+ [HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) (intermediate level)
+ [HTML5 Apps and Games](https://www.edx.org/course/html5-apps-and-games) (advanced level)


### Activity 2.2 - Practice with HTML Validator

HTML has been available to the public since 1991, but since then a lot has changed. One of the ways to make sure your HTML is well structured and up to date is to use the W3C HTML Validator. As you are developing your pages, it's a good idea to regularly check if your HTML is written according to W3C standards.

You can find the validator [here](https://validator.w3.org/)

You can pass any URL on the Web into the validator, and it will tell you how the HTML for that page stacks up against Web Standards. If you pass in https://www.w3.org (the W3C's homepage), you see the following:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/9dee69c0a62b4adea75199d9f4cef463/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4031b574414af74ae0a881d3601d7b4664">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/aa9d7a414b88b72a0071f979112f27a0/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-2-4_validator.PNG" style="margin: 0.1em;" alt="You can pass any URL on the Web into the validator, and it will tell you how the HTML for that page stacks up against Web Standards. If you pass in https://www.w3.org (the W3C's homepage)." title="HTML validator output for w3.org" width="350">
  </a></div>
</div>

If you start to try out other URLs, you might find this is a very rare result ;) <br/>
Try passing in your favorite Web address and see what comes up. For example, If you pass in https://www.microsoft.com/en-us/, you get 567 warnings and errors!

One of the more common errors is using an HTML tag that is considered obsolete. Often the error points you to this wiki page "[Use CSS instead](https://wiki.whatwg.org/wiki/Presentational_elements_and_attributes)".

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/9dee69c0a62b4adea75199d9f4cef463/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4031b574414af74ae0a881d3601d7b4664">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0b22b4d9104262183dc5677196d3a455/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-2-4_error.PNG" style="margin: 0.1em;" alt="One of the more common errors is using an HTML tag that is considered obsolete. Often the error points you to this wiki page "Use CSS instead"." title="Image of obsolete HTML error" width="350">
  </a></div>
</div>

For this activity, please try out some of your favorite Web addresses in this validator and see what happens. Find a page that has one of these types of errors and answer the following questions in the discussion board:

+ What URL gave you errors?
+ How many warnings and errors does this site have?
+ What HTML attribute does it use when it should use CSS instead?

Ans:

1. url: https://softnshare.com/brief-two-ux-teams-story/?fbclid=IwAR3W9P5hXii-KHVXDNgYhJxIey34YYwifukoqFMgZE35nvW_Qsn5SfE5lWw
2. 26 errors; 15 warnings
3. None


## 2.3 Building a CSS rule

### The anatomy of a CSS rule

#### Video: The anatomy of a CSS rule

<video src="https://edx-video.net/W3CCSS0I2016-V001600_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@60910593f9834ed897a0a15610f73f1b/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>
 

#### Live coding video: The anatomy of a CSS rule - Demo

<video src="https://edx-video.net/W3CCSS0I2016-V001800_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@cdb5f4a677cd45d2a28c60d11ef0285e/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>

[Here's the code from the video in a Code Pen for you to play around with](https://codepen.io/techie4good/pen/JXwWvr)

-----------------------------------

The HTML code is shown below:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My HTML page</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1> Welcome to my first CSS Website</h1>
    <h2> I'm glad you're here</h2>
    <img src="designer.png" alt="designer"/>
    <p>
      This is my first site using CSS, or Cascading Style Sheets. I'm still learning and 
      I have a long way to go, but doesn't it still look nice?
      It's amazing what a difference just some colors and fonts can make!
    </p>
  </body>
</html>
```

And the attached CSS file (style.css):

```css
body {
  background-color: #83AF9B;
  text-align: center;
  font-family: Arial;
  padding: 0;
  margin: 0;
}
h1 {
  background-color: #FE4365;
  color: #F9CDAD;
  font-size: 8em;
  padding: 50px;
}
h2 {
  color: #FE4365;
  background-color: #F9CDAD;
}
img {
  height: 250px;
}
p {
  background-color: #FC9D9A;
  color: white;
  padding: 50px;
  font-size: 2em;
}
```


### Constructing your CSS rules

Here is an example CSS "rule":

```css
p {
  color: blue;
}
```

This rule tells the browser to make all text within a paragraph tag blue. A CSS rule is broken into two parts: the __selector__ and the __property__

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/fa2e67e5afb94de3981b22805acd686c/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4098c09f586c9c45349fe25ca9e1742a14">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/39ef39b8e6685b816badb923520fa827/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-3-1_css_anatomy.PNG" style="margin: 0.1em;" alt="A CSS rule is broken into two parts: the selector and the property" title="css anatomy" width="250">
  </a></div>
</div>

#### Selector

This is the portion of the rule before the first open curly brace ( "{" character). This is what tells the browser what HTML tags this rule applies to. Often, you'll just see a selector that matches an HTML tag, like in this instance- our selector is just "p". However, as we get further into this course, you'll find that there are many ways to target specific HTML elements and many different ways to structure selectors so that you are targeting exactly the part of your site you want to style.

#### Property

This is the portion of the rule between the two curly braces. This is what tells the browser how to style the HTML tag that has been selected. This can be as many lines of code as you choose, each of which has two parts- the property and the value you want that property to be. For our example, "color" is the property and "blue" is the value, but we could also have had a value of "black" or "#FFFFFF" (which is HEX code for white). Each property line is constructed so:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/fa2e67e5afb94de3981b22805acd686c/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4098c09f586c9c45349fe25ca9e1742a14">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/989b2e8ecef6fec3fcc6fd02a5baed58/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-3-1_property_anatomy.PNG" style="margin: 0.1em;" alt="This is what tells the browser how to style the HTML tag that has been selected. This can be as many lines of code as you choose, each of which has two parts- the property and the value you want that property to be." title="property anatomy" width="250">
  </a></div>
</div>

The style for your page will consist of a list of many CSS rules put together. As we move through this course we will help you build up these rules to style your entire page.


### Activity 2.3 - Building your first CSS rule set

Now that you have a basic understanding of how to put the pieces of a CSS rule together, let's do some practice. Here is some HTML for a page you will style:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My HTML page</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>My H1 header</h1>
    <p> This is a block of text to represent a paragraph that you will want to style. 
    This might be an explanation of of the list that follows, it is all contained within 
    a single paragraph tag.
    </p>
    <ul>
      <li>This is list item 1</li>
      <li>Item 2 in the list</li>
      <li>The third item in the list</li>
      <li>Item 4 completes the list</li>
     </ul>
  </body>
</html>
```

[HTML in Code Pen](https://codepen.io/w3devcampus/pen/zovzwE)

Your goal is to get this HTML to look like the following image in the browser:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/fa2e67e5afb94de3981b22805acd686c/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4098c09f586c9c45349fe25ca9e1742a14">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/281e5aca6aa05f7826bc32210e8200a4/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/css-intro-2-3-1-final.png" style="margin: 0.1em;" alt="Your goal is to get this HTML to look like the following image in the browser" title="CodePen resulting image (Activity 2.3)" width="350">
  </a></div>
</div>

To do so, you will need to write 4 CSS Rules. You will need to use the following 4 selectors:

+ body
+ h1
+ p
+ ul

And you will need the following properties:

+ `background-color: silver;`
+ `background-color: purple;`
+ `color: white;`
+ `color: fuchsia;`

Now it's up to you to combine these selectors and properties into 4 rules to achieve the final style.


## 2.4 Attaching CSS to HTML using selectors

### What is a selector?

In unit 2.3, we defined a CSS selector as the portion of the CSS rule that tells the browser on which HTML element to apply the defined style.

When your HTML is simple, the selectors can be simple as well. The most basic selectors simply mirror the __HTML tag__. For example "p" attaches to all `<p>` tags, "img" will attach to all `<img>` tags and so on. As you can imagine, there will often be times when you don't want every single HTML element of a particular type to have identical style. In Module 3, we'll discuss a variety of ways to use selectors to attach to specific HTML elements.

In unit 2.2, we briefly mentioned the fact that properties apply to the entire hierarchy of HTML elements to which they are attached. This means that you will have to be very careful which selectors you choose to use in combination with your chosen style. When choosing your selector you might want to keep the following aspects of an HTML element in mind:

+ How many of these HTML elements are on my page? Do I want this style to apply to every one of these elements?
+ What are this HTML element's children, and do I want this style to apply to them as well?
+ Is this element a block element or an inline element, and does this style make sense in that context?

It is possible to independently target every HTML element on the page using selectors, but for this module we are going to stick to basics and only use selectors that match the HTML tag name. For example, here are some example selectors we'll use in this module:

```css
a {
 /* style for a tags */
}
```

This would affect the style of all link tags on the page.

```css
p {
 /* style for p tags */
}
```

This would affect the style of all paragraph tags on the page and the style of elements contained within the paragraph tag. 

```css
body {
 /* style for all elements in the body */
}
```

This would apply style to the body tag as well as allow the elements inside the body tag to inherit certain styles applied here. 

[Here is a Code Pen that demonstrates how styles apply to different selectors.](https://codepen.io/techie4good/pen/pEzLrd)

HTML code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="utf-8">
      <title>My HTML page</title>
      <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Title</h1>
    <p>In unit 2.3, we defined a CSS selector as the portion of the CSS rule that tells the 
      browser on which HTML element to apply the defined style.
      <a href="http://www.microsoft.com">Click Here!</a>
    </p>
    <ul>
      <li>When your HTML is simple, the selectors can be simple as well</li>
      <li>he most basic selectors simply mirror the HTML tag</li>
      <li>For example "p" attaches to all tags, "img" will attach to all tags and so on</li>
      <li>As you can imagine, there will often be times</li>
      <li>when you don't want every single HTML element of a particular type to have identical style</li>
    </ul>
    <p> 
In Module 3, we'll discuss a variety of ways to use selectors to attach to specific HTML elements. 
In unit 2.2, we briefly mentioned the fact that properties apply to the entire hierarchy of HTML 
elements to which they are attached. This means that you will have to be very careful which 
selectors you choose to use in combination with your chosen style 
 <br />
<a href="http://www.w3.org">Check this out</a>
It is possible to independently target every HTML element on the page using selectors, but for 
this module we are going to stick to basics and only use selectors that match the HTML tag name. 
For example, here are some example selectors we'll use in this module:
    </p>
    <ol>
      <li>This would affect the style of all link tags on the page</li>
      <li>This would affect the style of all paragraph tags on the page</li>
      <li>and the style of elements contained within the paragraph tag</li>
      <li>This would apply style to the body tag</li>
      <li>as well as allow the elements inside the body tag to inherit certain styles applied here. </li>
    </ol>
  </body>
</html>
```

CSS code:

```css
body {
  color: red; /* every element inherits this except those with more specific style */
}
ul {
  color: blue;/* li elements inherit this color */
}
p {
  font-style: italic; /* this even the a tags inherit within the paragraphs */
}
li {
  text-decoration: line-through; /* applies to all li elements, in both ul and ol tags */
}
```

### Inheriting style

Part of the reason a well structured HTML document is so important is because HTML elements inherit stylistic properties.

Let's say we have an HTML document (see the corresponding [Code Pen](https://codepen.io/techie4good/pen/mAVVkY?editors=1100#0)).

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My HTML page</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <header>
      <h1> Title </h1>
      <h2> sub title </h2>
    </header>
    <section>
      <p> This is my paragraph text </p>
      <ul>
        <li> list item 1 </li>
        <li> list item 2 </li>
        <li> list item 3 </li>
        </ul>
    </section>
  </body>
</html>
```

You can see it's basic structure from the way I have formatted the tags with tabbing, but here is a more visual representation of the hierarchy of tags. Tags that contain other tags are parents, and the tags inside of them are their children in the following tree representation:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/0e1bd16d542e4a1085cb8d9b305f8e59/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40833b012fc6dd41f68fa5fd6e3b93e8a8">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c3441bd3d744e14d5d1c0c663d7ad1dc/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-4-2_inheritance_tree.PNG" style="margin: 0.1em;" alt="ags that contain other tags are parents, and the tags inside of them are their children in the following tree representation." title="HTML inheritance structure" width="250">
  </a></div>
</div>


Through inheritance, CSS property values set on one element will be transferred down the tree to that element's children. In this example, every element gets the same font because we applied it to the body tag. Since the body element is a common parent for all visible elements is a convenient selector for when you want to set stylistic rules for the entire document.

Then, we applied different styles at different levels of the tree so that the "li" or list element tag ends up with three different styles (font, underline and green) without us actually applying any style directly to that tag. 

```css
body {
  font-family: "Century Gothic", sans-serif;
}
header {
  font-style: italic;
}
section {
  text-decoration: underline;
}
ul {
  color: green;
}
```

Not every property is inherited, but many are. The CSS specification tell you, for each property, whether it is inheritable. It's a good idea to keep in mind the structure of your HTML document when choosing your selectors so you can use inheritance to your advantage by applying styles to the top most element and save yourself extra CSS code.

Output:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/0e1bd16d542e4a1085cb8d9b305f8e59/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40833b012fc6dd41f68fa5fd6e3b93e8a8">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0eec708dce63466019c5b9d6988caa65/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/css-intro-2-4-2.png" style="margin: 0.1em;" alt="The CSS specification tell you, for each property, whether it is inheritable." title="CodePen image snapshot (Inheriting style)" width="100">
  </a></div>
</div>


### Combining multiple selectors

You can imagine that multiple HTML elements on your page will have similar style. If you write a separate CSS rule with the same properties for each of these elements, your CSS file can get very large and hard to manage. When designing CSS, the authors wanted to help make it as easy as possible to write and edit style sheets "by hand", so there are a number of features that help keep your styles succinct.

For example, what if you want to change the font that is consistent across many elements? You would have to change it in many places. Instead, you can combine multiple selectors on the same rule like so:

```css
p, ul, ol {
  color: blue;
  background-color: pink;
}
```

The comma means that each of these elements should have the same, duplicated style. No need to have repeated style! Of course, you could simply apply this style to an element that contains all of these, say the body element, but not all properties are inherited so using the comma is a direct way to apply consistent style across multiple categories of HTML elements. 

[Here is a Code Pen that explores using the comma to combine selectors.](https://codepen.io/w3devcampus/pen/PVJLEm)

HTML code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My HTML page</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Title 1</h1>
    <h2>Title 2</h2>
    <ul>
      <li>Part of the reason a well structured HTML document is so important</li>
      <li>is because HTML elements inherit stylistic properties</li>
      <li>You can see it's basic structure from the way I have formatted the tags with tabbing</li>
    </ul>
    <h3>Title 3</h3>
    <ol>
      <li>but here is a more visual representation of the hierarchy of tags</li>
      <li>Tags that contain other tags are parents</li>
      <li>and the tags inside of them are their children in the following tree representation</li>
    </ol>
  </body>
</html>
```

CSS code:

```css
body {
  color: #660099;
}
 
h1,h2,h3 {
  font-family: Impact, sans-serif;
}
 
ul,ol {
  font-family: helvetica, sans-serif;
}
 
h2,ul {
  font-style: italic;
}
 
h3,ol {
  text-decoration: underline;
}
```

Output:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/0e1bd16d542e4a1085cb8d9b305f8e59/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40833b012fc6dd41f68fa5fd6e3b93e8a8">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5ec613c3818f6c12089c5073749b4cbb/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-4-3_combining_selectors.PNG" style="margin: 0.1em;" alt="text" title="Output from multiple selectors code example" width="250">
  </a></div>
</div>


### Activity 2.4 - Apply your own selectors

Now it's your turn to practice with some selectors of your own. 

Let's say you have the following HTML and CSS (see the [Code Pen](http://codepen.io/w3devcampus/pen/RoKLKE/)), or see below:

HTML

```html
<!DOCTYPE html>
    <!-- It's a best practice to always declare your document! -->
<html lang="en">
  <head>
      <meta charset="utf-8">
      <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Main Title</h1>
    <p>In unit 2.3, we defined a CSS selector as the portion of the CSS rule that tells the 
    browser on which HTML element to apply the defined style.

When your HTML is simple, the selectors can be simple as well. The most basic selectors 
simply mirror the HTML tag. For example "p" attaches to all &lt;p&gt; tags, "img" will 
attach to all &lt;img&gt; tags and so on. As you can imagine, there will often be times 
when you don't want every single HTML element of a particular type to have identical 
style. In Module 3, we'll discuss a variety of ways to use selectors to attach to 
specific HTML elements. 

In unit 2.2, we briefly mentioned the fact that properties apply to the entire hierarchy 
of HTML elements to which they are attached. This means that you will have to be very 
careful which selectors you choose to use in combination with your chosen style. When 
choosing your selector you might want to keep the following aspects of an HTML element in mind</p>
    <h2>Sub Title 1</h2>
    <ul>
      <li>How many of these HTML elements are on my page?</li>
      <li>Do I want this style to apply to every one of these elements?</li>
      <li>What are this HTML element's children</li>
    </ul>
    <h2>Sub Title 2</h2>
    <ol>
      <li> and do I want this style to apply to them as well?</li>
      <li>Is this element a block element or an inline element</li>
      <li>and does this style make sense in that context?</li>
    </ol>
  </body>
</html>
```

CSS

```css
/*selector here*/    {
  background-color: #ccffcc;
  color: #336600;
}

 /*selector here*/   {
  background-color: #336600;
  color: #ccffcc;
}

/*selector here*/    {
  border: 3px solid;
}

 /*selector here*/   {
  background-color: #ffff99;
}

 /*selector here*/   {
  text-decoration: underline;
}
```

As you can see, there is HTML and some CSS rules, but the rules are missing their selectors.

You will need to figure out which selectors belong on top of each of the 5 rules so that your final site looks exactly like this:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/0e1bd16d542e4a1085cb8d9b305f8e59/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40833b012fc6dd41f68fa5fd6e3b93e8a8">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7a94f41eeffe7790d4fa52b20165a4d4/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-4-4_sol.PNG" style="margin: 0.1em;" alt="text" title="caption" width="350">
  </a></div>
</div>

Final result after you apply your own selectors

HINT: Some of the rules require multiple comma separated selectors.


## 2.5 Applying styles using CSS properties

### What is a property?

In unit 2.3, we briefly introduced you to "properties", the part of the CSS rule that tells the browser how to style specific aspects of the selected HTML element.

There is a huge array of different aspects you can style: color, font, size, spacing and much more! You can find the complete list of CSS properties at the W3C's official site [here](https://www.w3.org/Style/CSS/all-properties#list), or check out [Meiert's list here](http://meiert.com/en/indices/css-properties/).

Every property has its own collection of possible values. Some require text input, some specific keywords, some numerical input, etc.

Here are some examples of properties that each accept a different style of value:

```css
body {
  background-color: purple; /* key word */
  color: #FFFFFF; /* HEX code */
  width: 60%; /* percentage */
  font-size: 20pt; /* numerical value */
}
```

[CodePen of above style](https://codepen.io/techie4good/pen/bwbLJP)

Make sure to look up what the available values are before using a property, because if the browser doesn't understand your value it will typically just skip applying any style. This is where programs like Visual Studio Code come in handy because as you type out the property, the program will automatically suggest possible values for you like so:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/b51f656fe5bd47a7b2f24fe7617b7870/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40021c5be913ac42348edca84f9a89bf46">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/75ab908267b82d94ffa9b0bc9ffbd4d7/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-5-1_property_suggestions.png" style="margin: 0.1em;" alt="text" title="property suggestions" width="300">
  </a></div>
</div>

Sometimes the easiest way to learn about different properties is to explore the style on one of your favorite Web sites. You can use your browser tool to inspect an HTML element. Here is an example of inspecting a title:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/b51f656fe5bd47a7b2f24fe7617b7870/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40021c5be913ac42348edca84f9a89bf46">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/93820e63bdf7f44e865bffb7126582f9/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-5-1_browser_tool.png" style="margin: 0.1em;" alt="text" title="browser tool" width="350">
  </a></div>
</div>

If you are not sure how to do this, please refer to the demo in unit 1.3 to see this in action while inspecting CSS Zen Garden designs. 

As you can see, the browser tools display the value of the properties, and if you click into that space it will even give you some of the different value options and you can even change them and watch the Web site update dynamically. 



### Color properties

Color is one of the first things you'll want to explore when designing your Web site. Thankfully, CSS provides a wide array of tools for you to control the color of different HTML elements. There are basic color properties:

#### color

This property sets the foreground color of an element's text content. By default, all text content will be set to black. If you set the color on one HTML element it will be inherited by all HTML elements within that. For example, if you set the color property on the body tag to blue, all text on your web page will be changed to blue, unless that text has a more specific color property that will override it. 

[Documentation](https://www.w3.org/TR/css3-color/#foreground)


#### background-color

This property sets the background color of an element. This color then represents the exact space the element takes up, which is always a rectangular area. The default value is 'transparent' which means whatever is behind the element will shine through. Note that background-color is one example of a property that is not inherited, so you will have to directly set the background-color on each element. To set the overall color of your page, apply a background color to the body tag, and since all other element's background colors will be transparent by default, it will appear as if everything has that same background color. 

[Documentation](https://www.w3.org/TR/css3-background/#the-background-color)


#### color as a value

These color properties take in a color as their value, and there are three different ways you can define that color: keyword, a HEX code or an rgb value.

__keyword__

Probably the simplest and least flexible way to set colors is using a keyword. A keyword is one of the predefined colors like "blue" or "green". 

```css
body {
  background-color: teal; 
}
```

The list of color keywords is: aqua, black, blue, fuchsia, gray, green, lime, maroon, navy, olive, orange, purple, red, silver, teal, white, and yellow. You can read more about these keyword colors [here](https://www.w3.org/TR/CSS22/syndata.html#value-def-color).


__HEX__

A HEX code is a 6 character code to represent the color, giving you a lot more options. The 6 characters of the code are broken into 3 sets of 2, where each set of 2 represents the amount of either red, green or blue that makes up the color. These sets are hexadecimal numbers, which means that each ranges between 00 to FF where 00 means no color and FF means all of that color. Thus #000000 represents pure black and #FFFFFF represents pure white.

When using a hex code in CSS you must put a hash character in front of the 6 characters like so:

```css
body {
  background-color: #00CC00; /* green */
}
```

__decimal__

You can also specify colors using rgb in decimal form like so:

```css
body {
  background-color: rgb(0,204,0); /*same green as above*/
}
```

This will give you the same range as HEX values. This method is a less common, but it's up to you which method of specifying colors you prefer. 

[Documentation](https://www.w3.org/TR/CSS22/syndata.html#value-def-color)

Here are some of the colors you can use, and the three different ways you can set their value in the color or color-background property:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/b51f656fe5bd47a7b2f24fe7617b7870/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40021c5be913ac42348edca84f9a89bf46">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f3568defc277a8c99de86bd557a17f68/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/colors-rgb.png" style="margin: 0.1em;" alt="text" title="color swatches" width="500">
  </a></div>
</div>

You can see these color properties in action using all three approaches to setting the value [in this CodePen](https://codepen.io/techie4good/pen/PGYRYL).

#### Other resources

+ color paletteWe will discuss how to pick a good color palette for your site in Module 5, but in the mean time [here is a good wiki article from the W3C](https://www.w3.org/wiki/Colour_theory) discussing the general use of colors on the Web.
+ More color units are described in the [CSS3 specification](https://www.w3.org/TR/css3-color/#colorunits).

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/b51f656fe5bd47a7b2f24fe7617b7870/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40021c5be913ac42348edca84f9a89bf46">
    <img src="https://www.w3.org/wiki/images/d/d2/10000000.jpg" style="margin: 0.1em;" alt="Colours, or hues, have historically been divided into primary, secondary, and tertiary colours. The primary colours consist of red, yellow and blue, and they’re called primary colours because you don’t need to mix colours to make these three hues. If you want to translate these colours into web colours, you can recreate them using their hex (hexadecimal) equivalents of #ff0000, #ffff00, and #0033cc. Secondary colours are mixed from primary colours." title="the primary and secondary colours, and their hex equivalents" width="350">
  </a></div>
</div>

<br/>
<table style="display: table;border-collapse: separate;border-spacing: 2px;border-color: grey;text-align: center;">
   <caption><b><a href="https://www.w3.org/TR/css-color-3/#html4">Color names and <span class="index-inst" id="srgbval">sRGB</span>
    values</a></b><br>
   </caption>
   <tbody>
    <tr><th style="background:black;">Named</th><th>Numeric</th><th>Color name</th><th>Hex rgb</th><th>Decimal</th></tr>
    <tr><td style="background:black;"></td><td style="background:#000000"></td><td><dfn id="black">black</dfn></td><td >#000000</td><td >0,0,0
    </td></tr>
    <tr><td style="background:silver;"></td><td style="background:#C0C0C0"></td><td><dfn id="silver">silver</dfn></td><td >#C0C0C0</td><td >192,192,192
    </td></tr>
    <tr><td style="background:gray;"></td><td style="background:#808080"></td><td><dfn id="gray">gray</dfn></td><td >#808080</td><td >128,128,128
    </td></tr>
    <tr><td style="background:white;"></td><td style="background:#FFFFFF"></td><td><dfn id="white">white</dfn></td><td >#FFFFFF</td><td >255,255,255
    </td></tr>
    <tr><td style="background:maroon;"></td><td style="background:#800000"></td><td><dfn id="maroon">maroon</dfn></td><td >#800000</td><td >128,0,0
    </td></tr>
    <tr><td style="background:red;"></td><td style="background:#FF0000"></td><td><dfn id="red">red</dfn></td><td >#FF0000</td><td >255,0,0
    </td></tr>
    <tr><td style="background:purple;"></td><td style="background:#800080"></td><td><dfn id="purple">purple</dfn></td><td >#800080</td><td >128,0,128
    </td></tr>
    <tr><td style="background:fuchsia;"></td><td style="background:#FF00FF"></td><td><dfn id="fuchsia">fuchsia</dfn></td><td >#FF00FF</td><td >255,0,255
    </td></tr>
    <tr><td style="background:green;"></td><td style="background:#008000"></td><td><dfn id="green">green</dfn></td><td >#008000</td><td >0,128,0
    </td></tr>
    <tr><td style="background:lime;"></td><td style="background:#00FF00"></td><td><dfn id="lime">lime</dfn></td><td >#00FF00</td><td >0,255,0
    </td></tr>
    <tr><td style="background:olive;"></td><td style="background:#808000"></td><td><dfn id="olive">olive</dfn></td><td >#808000</td><td >128,128,0
    </td></tr>
    <tr><td style="background:yellow;"></td><td style="background:#FFFF00"></td><td><dfn id="yellow">yellow</dfn></td><td >#FFFF00</td><td >255,255,0
    </td></tr>
    <tr><td style="background:navy;"></td><td style="background:#000080"></td><td><dfn id="navy">navy</dfn></td><td >#000080</td><td >0,0,128
    </td></tr>
    <tr><td style="background:blue;"></td><td style="background:#0000FF"></td><td><dfn id="blue">blue</dfn></td><td >#0000FF</td><td >0,0,255
    </td></tr>
    <tr><td style="background:teal;"></td><td style="background:#008080"></td><td><dfn id="teal">teal</dfn></td><td >#008080</td><td >0,128,128
    </td></tr>
    <tr><td style="background:aqua;"></td><td style="background:#00FFFF"></td><td><dfn id="aqua">aqua</dfn></td><td >#00FFFF</td><td >0,255,255
   </td></tr>
  </tbody>
</table>


### Font properties

Font is an extremely important part of how you communicate content to your user. As you are likely aware there are many different aspects to font, and with CSS you can explicitly style each aspect. [Here is a quick reference for what the fonts look like with different properties.](https://www.w3.org/Style/Examples/007/fonts)


#### font-family

```css
p {
  font-family: Helvetica, Verdana, sans-serif;
}
```

This property sets the font face. There are a collection of Web safe fonts that generally each browser has agreed to support, but there is an infinite number of different fonts. The problem is they might not all look the way you want them to on different browsers.

That is why this property "font-__family__" allows a list of fonts in the order of your preference. This comma-separated list orders your font preference from left to right. In our above example, our first choice is Helvetica, if the browser doesn't support that it will move to the next on the list, Verdana, and if it still doesn't support that it will just pick any sans-serif font it does support. You should always end your font family with fonts that are likely to be supported by the browser, this way you are guaranteed to have control over the font-family.

Something to keep in mind: some fonts have names with multiple words like "Times New Roman" or "Century Gothic". When using these fonts you'll need to surround the entire name with quotes so the browser understands that is a single font name like so:

```css
p {
  font-family: "Times New Roman", "New Century Schoolbook", serif;
}
```

[Documentation](https://www.w3.org/TR/css-fonts/#font-family-prop%20%20%20%20%20%20%20https://www.w3.org/Style/Examples/007/fonts.en.html)


#### font-size

```css
h1 {
  font-size: 2.5em;
}
```

Font-size sets the overall scale of your text. You can use a lot of different units to set the font size. Some of these units you are probably familiar with if you have used text editors before such as pt size or you can use px size. However, these methods are not advised because they are static and will not adapt based on screen size. 

The ideal way to set text size is to use "em". Em is a way to set your text size based on the system settings of the device in which you are viewing that font. This becomes especially important for users who have special font preferences due to accessibility requirements. To use em do not set font-size on the body tag, but instead set the size for each element in relation to the user's default. For example, 1em is the default, 2em is twice as big, 0.5em is half as big etc. [Here are some more font sizing tips and tricks.](https://www.w3.org/Style/Examples/007/units.en.html)

<table>
  <colgroup><col><col><col><col>
    </colgroup><thead>
     <tr>
      <th>
      </th><th>Rec­om­mended
      </th><th>Oc­ca­sional use
      </th><th>Not rec­om­mended
    </th></tr></thead><tbody>
     <tr>
      <th>Screen
      </th><td>em, px, %
      </td><td>ex
      </td><td>pt, cm, mm, in, pc
     </td></tr><tr>
      <th>Print
      </th><td>em, cm, mm, in, pt, pc, %
      </td><td>px, ex
      </td><td>
    </td></tr>
  </tbody>
</table>

[Documentation](https://www.w3.org/TR/css-fonts/#font-size-prop)


#### font-weight

```css
p {
  font-weight: bold;
}
```

The weight of a font is the thickness of the letters. You can set this property using keywords with which you might be familiar: `bold`, `normal` or `lighter`. You can also set this property more specifically using numerical values 100, 200, 300, 400, 500, 600, 700, 800 or 900. Normal is represented as 400, whereas bold is 700.

Note that few fonts have settings for all values. If the value is not available, the browser will use the nearest available one. For example, if 800 is not available but 700 is, then the browser will display 700. [You can try out different fonts in this code pen to see how they look at each weight setting.](https://codepen.io/techie4good/pen/XNdrMw)

[Documentation](https://www.w3.org/TR/css-fonts/#font-weight-prop)


#### font-style

```css
p {
  font-style: italic;
}
```

The font style property adjusts the angle of the letters in relation to the horizontal plane. Italic forms are generally cursive in nature while oblique faces are typically sloped versions of the regular face.

[Documentation](https://www.w3.org/TR/css-fonts/#font-style-prop)


#### text-decoration

```css
p {
  text-decoration: underline;
}
```

Text-decoration adds a line across your text. You can set this line to be underneath your text, underline, through your text, line-through, or on top, overline.

[Documentation](http://www.w3.org/TR/css-text-decor-3/#text-decoration-property)

#### Example:

[Here is a CodePen exploring each of these styles.](https://codepen.io/techie4good/pen/ozvqxy)

HTML code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My HTML page</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Main title</h1>
    <h2>Sub title</h2>
    <p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lacinia consequat nibh, non commodo 
neque maximus semper. Vivamus non ultricies massa, vel convallis nunc. Aenean tempus risus at orci 
faucibus, eget hendrerit elit sodales. Quisque imperdiet diam nibh, ut semper enim dapibus et. 
Interdum et malesuada fames ac ante ipsum primis in faucibus. Aenean in feugiat neque. Nunc eget 
libero mauris. Maecenas condimentum luctus nulla.

Nulla a sem orci. Cras eget neque viverra, condimentum nulla et, tincidunt libero. In sit amet 
quam purus. Aliquam erat volutpat. Sed hendrerit urna quis sapien mattis dictum. Etiam vehicula 
tortor eu libero finibus dapibus. Mauris nunc neque, sodales nec est sed, gravida convallis sem. 
Nam vulputate sed est sed eleifend. Quisque sodales elit at ornare vulputate.

Morbi quis metus tortor. Cras dapibus nisl urna, et pretium risus rutrum at. Maecenas a sollicitudin 
elit. Ut suscipit neque ligula. Nam aliquam massa in pretium ullamcorper. Sed id nisl et mauris 
maximus suscipit. Suspendisse potenti. Nulla interdum, magna eu facilisis aliquam, tellus nulla 
luctus nisi, eu cursus magna sapien sed mi.
      </p>
  </body>
</html>
```

CSS code:

```css
body {
  font-family: Helvetica, Verdana, sans-serif;
  font-size: 12pt;
}
h1 {
  font-size: 3em;
  font-style: italic;
}
h2 {
  font-size: 2em;
  text-decoration: underline;
}
p {
  font-weight: bold;
}
```

Output:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/b51f656fe5bd47a7b2f24fe7617b7870/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40021c5be913ac42348edca84f9a89bf46">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5c78c149b787fe19d78703a7aa07a75d/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/css-intro-2.5.png" style="margin: 0.1em;" alt="text" title="CodePen resulting image (Font properties)" width="250">
  </a></div>
</div>

#### External resources:

There are even more ways to adjust text appearance and you can read more about them here: 

+ [CSS Fonts Module Level 4](https://www.w3.org/TR/css-fonts/)
+ [CSS Text Decoration Module Level 4](http://www.w3.org/TR/css-text-decor/)



### Spacing properties

CSS provides a great set of tools to help you position the HTML elements on your page, and we will cover that in depth in Module 4. For now we will talk about how to apply white space around individual HTML elements.

There are two different ways you can define white space:

+ in absolute terms: using an exact number of pixels,
+ and in relative terms: using percentages or ems.

For now, we'll use pixels because that is easier to learn. However, ultimately you will want to use percentages and ems so your content adapts to different screens. We will discuss how to use percentages in Module 4.

When you view an element in your browser tools you can see the white space around it represented like so:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/b51f656fe5bd47a7b2f24fe7617b7870/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40021c5be913ac42348edca84f9a89bf46">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f6f6c946356774ddb886956cd94df4c9/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/margin__padding__border.png" style="margin: 0.1em;" alt="Diagram presenting the relationship of margin, padding and brider" title="margin padding border" width="300">
  </a></div>
</div>


The above image is called the "__box model__", which we will get into more detail about in Module 4. For now, you can see that the space around the content is broken into three distinct regions.


#### Padding

```css
p {
  padding: 20px;
}
```

"Padding" is the white space that sits closest to an HTML element. Many elements already have a default padding defined. For example, `ul` elements by default are indented to the left a bit because they have a left padding.

You can set the padding on an element's four sides independently using `padding-top`, `padding-right`, `padding-bottom` and `padding-left`. Or you can use the more compact padding: 10px 15px 20px 25px. In this case, the order of the numbers sets the `top`, `right`, `bottom` and `left` paddings. In the above example, I collapsed all of these and just set the padding on all four sides to be 20px. [Here is a code pen that demonstrates all these different ways to set padding.](https://codepen.io/w3devcampus/pen/zeEXao)

[Documentation](https://www.w3.org/TR/CSS2/box.html#propdef-padding-top)


#### Border

```css
p {
  border: 1px black solid;
}
```

The "border" is the area outside the padding of an HTML element. By default, borders are set to be empty, but you can set their width, color, pattern, even an image! Like padding, you can even adjust the four sides of a border independent of one another using `border-top`, `border-right`, `border-bottom` or `border-left`. You can also adjust the different aspects of a border with `border-width`, `border-color`, and `border-style`. In the above example, I collapsed all of these properties into a single simple property and value set. 

[Documentation](https://www.w3.org/TR/css3-background/#borders)


#### Margin

```css
p {
  margin-bottom: 50px;
}
```

An HTML element's "margin" is the white space that sits outside the border. Margins of HTML elements interact with other another on the page to determine how they are arranged on the page. A lot of elements have default margins applied.

For example, the body tag typically has a margin that causes any content to not extend all the way to the extreme edge of the page. Be careful, margins can be tricky. When two margins touch they "collapse" such that the space between the elements is equivalent to the larger of the two margins. Like the above properties, you can also set the margins on each side independently using `margin-top`, `margin-left`, `margin-bottom` and `margin-right`.

[Documentation](https://www.w3.org/TR/CSS2/box.html#propdef-margin)


#### Example

[Here is a CodePen exploring padding, border and margin.](https://codepen.io/techie4good/pen/vXBRJP)

HTML code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My HTML page</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Main Title</h1>
    <ul>
      <li> List element 1</li>
      <li> List element 2</li>
      <li> List element 3</li>
    </ul>
    <p>
      Integer euismod at lectus vel placerat. Nam laoreet a quam in maximus. Duis turpis tellus, 
      accumsan ac efficitur in, tempus vel augue. Aenean vitae venenatis tortor. Praesent dignissim 
      nisl id odio fringilla, ac dapibus enim euismod. Sed id tellus vel est blandit finibus non 
      vel magna. Nullam mattis, odio in suscipit dapibus, mauris dolor mollis nisl, et ultricies 
      sem justo ac dui. Etiam ut turpis ipsum. Vivamus sodales vel nibh ut gravida. Pellentesque 
      eu nunc elementum, sodales diam dictum, lobortis magna. Suspendisse id mattis ipsum. Vivamus 
      scelerisque facilisis justo, id facilisis dui auctor sed.
    </p>
  </body>
</html>
```

CSS code:

```css
body {
  background-color: #99ffff;
  margin-top: 20px;
  margin-left: 70px;
}
h1 {
  background-color: #ff6699;
  border-bottom: 20px #ff0066 solid;
  margin-bottom: 10px;
  padding: 5px;
}
ul {
  background-color: #ff9933;
  border-left: 5px black dashed;
  margin: 50px;
}
li {
  background-color: #ffcc66;
  margin: 10px;
  padding: 10px;
}
p {
  background-color: #ccff99;
  border: 10px white double;
  padding: 0px;
  margin: 0px;
}
```
Output:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/b51f656fe5bd47a7b2f24fe7617b7870/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40021c5be913ac42348edca84f9a89bf46">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/aa7902a4786441d8d4dcdda4ac175a79/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/css-intro-2-5-2.png" style="margin: 0.1em;" alt=" exploring padding, border and margin" title="CodePen resulting image (Spacing properties)" width="250">
  </a></div>
</div>


In this code pen, you can see that I used background color to illustrate where there was padding and where there was margin. An element's background color extends over its padding but not over its margin.



### Activity 2.5 - Adding your own properties

Now that you have a few properties in your CSS toolbox, let's practice using them.

Here is some HTML and CSS, but as you can see the CSS rules have selectors but no properties. See this [Code Pen of Code Stub](https://codepen.io/techie4good/pen/EgYEAp).

HTML code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My HTML page</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Adding Properties</h1>
    <h2>Using Colors, Fonts and Spacing</h2>
    <p>          
      There is a huge array of different aspects you can style: color, font, size, spacing and much 
      more! For a complete list of official CSS properties look here: 
      https://www.w3.org/Style/CSS/all-properties#list or http://meiert.com/en/indices/css-properties/
    </p>
    <ol>
      <li>Make sure to look up what the available values are before using a property</li>
      <li>because if the browser doesn't understand your value it will typically just skip 
        applying any style</li>
      <li>This is where programs like Visual Studio Code come in handy</li>
      <li>because as you type out the property the program will automatically suggest possible 
        values for you </li>
      <li>Sometimes the easiest way to learn about different properties is to explore the style 
        on one of your favorite websites</li>
    </ol>
    <p>     
If you aren't sure how to do this refer to the demo in unit 1.3 to see this in action while inspecting 
CSS Zen Garden designs. As you can see, the browser tools display the value of the properties, and if 
you click into that space it will even give you some of the different value options and you can even 
change them and watch the Web site update dynamically.
    </p>
  </body>
</html>
```

As you can see, these CSS rules have selectors, but no properties. For this activity, it is up to you to add the correct properties and set their values appropriately to achieve this final style:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/b51f656fe5bd47a7b2f24fe7617b7870/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40021c5be913ac42348edca84f9a89bf46">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a1594384f91556ed990dff48f258fb76/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-5-5_Activity.PNG" style="margin: 0.1em;" alt="text" title="Final image of web site with proper CSS properties applied" width="450">
  </a></div>
</div>

Here are the color HEX code used above:

+ light yellow: #ffff99
+ medium yellow: #ffcc00
+ orange: #ff6600

Here are the fonts used above:

+ Helvetica
+ Impact
+ Courier New


## 2.6 Style studies

### Style studies

In each unit, we will have a section like this one where we profile specific aspects of Web sites and the various ways you can use CSS to style them. This is intended to give you practical examples of how to apply the CSS you are developing along the way. 

Each style study will discuss the different concerns of styling a given element and three sample styles.


### Titles

There are a couple different categories of text on a Web page: titles, body text, links, captions, etc.

You'll want to style each of these differently to help your user understand the proper context for your text. One of the most important categories of text to stand out are your titles.

There are different aspects of text you can alter to make it stand out.

+ size
+ font
+ capitalization
+ color
+ emphasis
+ weight

However, you should only alter a few of these following aspects at a time to prevent your titles from being too distracting. The below is an example of using too many different aspects of font for emphasis:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/19f23422b5574f43953df1259e27c6f4/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40488524f351ba487aa19204de45b0d496">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3d61e59f7c40b29e950c2954ade93c81/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-6-1_title_ugly.PNG" style="margin: 0.1em;" alt="Image of too busy title" title="Image of too busy title" width="450">
  </a></div>
</div>


```css
#busyTitle h1{
  font-size: 2em;
  font-family: Impact;
  color: yellow;
  background-color: gray;
  font-style: italic;
  font-variant: small-caps;
  font-weight: bold;
  text-decoration: underlinel;
}
```

#### Title 1

This title uses soft clean colors based on print media, so we chose a serif font. We also increased the size and color to help the title appear more prominent than the body text.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/19f23422b5574f43953df1259e27c6f4/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40488524f351ba487aa19204de45b0d496">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7b4d131e7d9b1d7256b9eb940fc8c2aa/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-6-1_title_1.PNG" style="margin: 0.1em;" alt="title 1" title="title 1" width="450">
  </a></div>
</div>


```css
#design1 {
  background-color: #F4F4F4;
  font-family: "Lucidia Sans Unicode", sans-serif;
}
 
#design1 h1 {
  color: #C0B283;
  font-size: 4em;
  font-weight: 700;
  font-family: Garamond;
  width: 300px;
}
 
#design1 p {
  color: #373737;
  font-size: 1.2em;
}
```


#### Title 2

This design is intended to look futuristic, so it only uses sans-serif, thin font with high contrast colors.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/19f23422b5574f43953df1259e27c6f4/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40488524f351ba487aa19204de45b0d496">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6ae804aa364c30d81afe6a6c824a98cf/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-6-1_title_2.PNG" style="margin: 0.1em;" alt="title 2" title="title 2" width="450">
  </a></div>
</div>


```css
#design2 {
  font-family: Century Gothic, sans-serif;
  background-color: #0E0B16;
}
 
#design2 h1 {
  font-weight: 400;
  font-size: 2.3em;
  color: #A239CA;
  font-style: italic;
}
 
#design2 p {
  color: #E7DFDD;
}
```

#### Title 3

This design is based on pastel primary colors and uses color as a highlight against the default white background. We have achieved the separation between title and body text by setting its background color separately and giving it a bottom border. 

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/19f23422b5574f43953df1259e27c6f4/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40488524f351ba487aa19204de45b0d496">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ec1b9e7c51052441da84f9736e3acd0e/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-6-1_title_3.PNG" style="margin: 0.1em;" alt="title 3" title="title 3" width="450">
  </a></div>
</div>


```css
#design3 {
  color: #DF744A;
  font-family: Arial, sans-serif;
}
 
#design3 h1 {
  background-color: #BFD8D2;
  text-align: center;
  font-size: 4em;
  font-weight: 100;
  padding: 30px;
  border-bottom: 5px #DCB239 solid;
  font-family: Helvetica, sans-serif;
}
 
#design3 p {
  background-color: #FEDCD2;
  padding: 50px;
}
```

[Here is a code pen of all the above examples of different title designs for you to play around with.](https://codepen.io/techie4good/pen/ZpOvBd?editors=1100#0)



### Buttons

Buttons are a key way that your users will interact with your page. Often buttons are a call to action for your user- so you will want them to stand out!

When styling a button you aren't just styling the text, but also the area around it, including the border. By giving them a distinct background color or border you make it clear that this whole area is "clickable".

Typically your user will expect your button to be wider than it is tall, to accomplish this you'll want to set the left and right padding to be greater than the top and bottom paddings.

Here is an example of a button where it's not immediately clear that it is actually a button.

#### Button 1

This design is a pretty traditional button where it has a distinct background-color and border-color to help it stand out from both the background and the body text.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/19f23422b5574f43953df1259e27c6f4/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40488524f351ba487aa19204de45b0d496">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/71258305acbafe9ca8d4bcd0d5aebe10/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-6-2_button_1.PNG" style="margin: 0.1em;" alt="button design 1 image" title="button design 1 image" width="450">
  </a></div>
</div>


```css
#design1 {
  background-color: #94618E;
  color: #F8EEE7;
  font-family: Corbel;
}
#design1 button {
  background-color: #F4DECB;
  padding: 10px 25px;
  border: 5px solid #F8EEE7;
  color: #49274A;
  font-weight: bold;
  font-size: 1.2em;
 }
```


#### Button 2

This is a more modern button design where there is no distinct border, but just a flat color background.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/19f23422b5574f43953df1259e27c6f4/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40488524f351ba487aa19204de45b0d496">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/546df96b5a1e929d2b85b95614013c05/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-6-2_button_2.PNG" style="margin: 0.1em;" alt="button design 2 image" title="button design 2 image" width="450">
  </a></div>
</div>


```css
#design2 {
  background-color: #D9D9D9;
  color: white;
  font-family: "Century Gothic", sans-serif;
}
#design2 button {
  background-color: #4484CE;
  border: 0px;
  color: white;
  padding: 10px 50px;
  font-family: Impact, sans-serif;
  font-size: 1.3em;
}
```

#### Button 3

This is a big graphic button that uses border-radius to give the button rounded corners.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/19f23422b5574f43953df1259e27c6f4/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40488524f351ba487aa19204de45b0d496">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7f2cfe384e3c3678086d305452ffa48c/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-6-2_button_3.PNG" style="margin: 0.1em;" alt="button 3 design image" title="button 3 design image" width="450">
  </a></div>
</div>


```css
#design3 {
  font-family: Impact, sans-serif;
  font-size: 2em;
}
 
#design3 button {
  font-family: Impact, sans-serif;
  font-weight: 100;
  background-color: white;
  border: 7px #EC576B solid;
  border-radius: 20px;
  font-size: 0.8em;
}
```

[Here are three different ways to style buttons you can play around with.](https://codepen.io/techie4good/pen/ORXzoo?editors=1100#0)


### Activity 2.6 - Effective titles and buttons

Now that you know a bit more about how CSS is written, you will start to understand and notice more of the design elements as you navigate around the Web.

In this module's style studies section, you learned some effective ways to style titles and buttons. You also learned about some design choices that make your titles and buttons not as effective...

+ Titles shouldn't be overly styled. They should only have a few properties set to help them stand out from body text, but not too many otherwise they will be too busy.
+ Buttons should send a clear message that they need to be interacted with. If a button doesn't show up as a rectangle, a user typically won't understand that it's a button.

For this activity, please find a Web page that has either titles or buttons and discuss how effectively they are styled. In the discussion below, answer the following questions:

+ Which Web page are you evaluating?
+ Is their use of titles or buttons as effective as they can be?
+ What do you like about their title or button design?
+ What would you change about their title or button design to be more effective?


Ans: 
1. The web page evaluated: https://www.packtpub.com/packt/offers/free-learning/?login=1
2. Yes, the title banner and the button are standout with contrast color.  Theya re easy to spot and lead us to take action.
3. The title banner color with a dark background and big fonts for us to read.  The timer banner is with orange that alerts users the time is runing out.  The entire page looks neat and carries message clear.
4. The button might consider bigger fount and increase font weight.


## 2.7 Project 2 - About me page

### Module 2 project - About me page

Now that you have played around with applying selectors and properties, you have the tools to make a much more sophisticated Web page than "Hello Your World". 

For your module project, you are going to create a page describing yourself using your favorite colors. Your Web page must have the following content:

+ an h1 title with your name
+ an h2 title with your favorite quote
+ a paragraph describing your favorite hobbies
+ an ordered list of your favorite foods
+ an unordered list of your favorite websites, including links to them

And in addition, you must employ the following styles:

+ 3 different font colors
+ 2 different background colors
+ a serif font
+ a sans-serif font
+ italic text
+ bold text
+ 1 border
+ extra margin between the edge of the screen and your content
+ extra padding around your list items

For example, here is what my page looks like:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/a266d0919e0f4e31afa5a0c2abb25edf/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4069a34ed95d0a4b4683e10efb32d63db8">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/152ba1416a059133e7dcd8af8480df6b/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/css-intro-2-6-1.png" style="margin: 0.1em;" alt="CodePen resulting image (Module 2 project)" title="CodePen resulting image (Module 2 project)" width="350">
  </a></div>
</div>


Note: you are welcome to look up other styles and apply them however you like as long as you at least have the above requirements met.

We've set up a discussion forum below, in case you want to share your work!


## 2.8 Conclusion and exercises

### After Module 2 you should be able to...

+ understand the how HTML and CSS work together to create Web content
+ describe what the different parts of a CSS rule are
+ employ basic selectors and combine them using the comma
+ apply properties that style color, font and spacing

In module 3, you will then learn:
+ classes, IDs
+ contextual selectors
+ pseudo classes


### Exercises (1-4)

1. CSS anatomy

  The part of a CSS rule that attaches the style to the HTML element is called the:

  Ans:selector


Use the following code for questions 2 and 3

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My HTML page</title>
    <link rel="stylesheet" href="style.css">
    <p> This is HTML element 2 </p>
  </head>
  <body>
    <p> This is HTML element 1 </p>
    <div> This is HTML element 3 </div>
  </body>
</html>
```

2. Style inheritance

    ```css
    p {
      color: red;
    }
    ```

    After this rule is attached to the above HTML, which elements would have red text?
    1. element 2
    2. all three elements
    3. element 3
    4. elements 1 and 2
    5. element 1

    Ans: 4


3. Style inheritance again

    ```css
    body {
      color: green;
    }
    ```

    This rule was attached to the above HTML, which elements would have green text?
    1. element 2
    2. all three elements
    3. element 3
    4. elements 1 and 2
    5. element 1

    Ans: 2


Code for question 4

Here is some redundant CSS code:

```css
p {
color: blue;
font-family: Arial, sans-serif;
}
 
h1 {
color:blue;
font-family: Arial, sans-serif;
font-style: italic;
}
 
a {
font-style: italic;
}
```

4. Combining rules

    Which of the following CSS documents is equivalent to the above code?

    1. 
      ```css
      p { color: blue; } 
      h1, a { font-style: italic; font-family: Arial, sans-serif;}
      ```
    2. 
      ```css
      p, h1, a { font-family: Arial, sans-serif; } 
      h1 { font-style: italic; color: blue}
      ```
    3. 
      ```css
      p, h1 { color: blue; font-family: Arial, sans-serif; } 
      h1, a { font-style: italic; }
      ```
    Ans: 3


### Exercises (5-10)

5. Color as a value

    Which of the following values will set a color property to black? (2 correct answers!)

    1. `#000000;`
    2. `"black";`
    3. `black;`
    4. `#FFFFFF;`
    5. `rgb(255,255,255);`

    Ans: 13 <br/>
    Explanation: Beware: color keyword (such as "black") do not have quotes around them, otherwise it is interpreted as text. `#FFFFFF;` and `rgb(255,255,255);` each gives the color white.


6. Color inheritance

    True or False? "background-color" is inherited from parent to child HTML element (if the parent is not a body element).

    Ans: False <br/>
    Explanation: "background-color" is not inherited, but note that the background of elements is normally transparent so you see the background of the parent behind them.


7. font-family

    What will happen to the text affected by the following CSS rule?

    ```css
    body {
      font-family: "Century Gothic", Arial, sans-serif;
    }
    ```

    1. The browser will try to use each font, starting with Century Gothic and moving to the right until it finds a supported font.
    2. The browser will try to use each font, starting with sans-serif and moving to the left until it finds a supported font.
    3. Text will use all three different fonts based on the different tags it lives within.

    Ans: 1 <br/>
    Explanation: The prefered font is mentioned first and the other fonts are fallbacks.


8. font-size

    Which of the following font-size units is recommended as a best practice to maximize accessibility?

    1. in
    2. px
    3. em
    4. pt

    Ans: 3 <br/>
    Explanation: It is best to use relative sizes instead of using absolute ones, so that the reader's preferences (the font sizes configured in the browser) are respected.


9. Border aspects

    When adding a border, what are the three aspects that can be styled? (3 correct answers!)

    1. border-weight
    2. border-color
    3. border-style
    4. border-height
    5. border-width

    Ans: 235 <br/>
    Explanation: The three aspects are width (for the thickness), style (solid, dashed, etc.) and color.


10. Margins

    When two vertical margins meet, what happens?
    1. the space between the two elements is the larger of the two margins. correct
    2. the space between the two elements is the smaller of the two margins.
    3. the space between the two elements is the sum of the two margins. incorrect

    Ans: 1 <br/>
    Explanation: When two vertical margins meet, they "collapse": the smaller one disappears inside the larger one. The right answer is : the space between the two elements is the larger of the two margins.


### Exercises (11-12)

Use the following code for the next 2 questions

Given the following HTML:

```html
<body>
    <header>
       <h1> My Page </h1>
    </header>
    <section>
       <h2> My Content </h2>
       <p> This is where my page's content will be </p>
    </section>
</body>
```

And the following CSS:

```css
body {
   color: green;
}
header {
   background-color: blue;
}
section {
   font-weight: bold;
}
p {
   text-decoration: underline;
}
```

11. Styling the p tag

    Which of the following styles will be applied to the p tag? (Select all that apply, 3 correct answers!)

    1. green text
    2. blue background
    3. bold text
    4. underlined text

    Ans: 134 <br/>
    Explanation: P has 'text-decoration: underline' applied, and inherits the color green and the font-weight bold, but it is not inside the header so it is not blue.


12. Styling the h1 tag

    From the style sheet above, how does the h1 look? (Select all that apply, 2 correct answers!)

    1. green text
    2. blue background
    3. underlined text

    Ans: 12 <br/>
    Explanation: H1 inherits the green color from the body, and it has the blue background of the header because its own background is transparent.<br/>
    Note that h1 is also bold, because the browser default style for h1 is bold.




