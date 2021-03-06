# Module 3: Adding style with CSS

## 3.1 Introduction to Module 3

### Welcome to Module 3

<video src="https://edx-video.net/W3CHTM502016-V010200_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@7bc6cf214b7b44b5884013b7a14dbdfa/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>



### Module 3 - Content

3.1 __Introduction to Module 3__: Get an overview of what CSS (Cascading Style Sheets) can do for your Web pages.

3.2 __CSS basic syntax__: Understanding the language of CSS: style tags, links tags, rules, and comments.

3.3 __CSS properties__: Here, you will be introduced to just a few of the many properties that make CSS such a powerful tool.

3.4 __Lists and selectors__: List markup tags (`<ul>`, `<ol>` and `<li>`) are some of the most frequently used specific purpose tags in HTML, and selectors are what allows you to target specific HTML elements and apply style to them

3.5 __Exercises - Module 3__: Let's see what you learned in Module 3 of the course.


### The CSS language

__CSS__ stands for 'Cascading Style Sheets'. For now, do not worry about what the 'Cascading' part means and just focus on the 'Style Sheets'.
Using CSS, we can determine the visual appearance of our HTML elements independent of the HTML itself.

Recall the metaphor we used for HTML with the journalist and the publisher. Where HTML represents the author's work, CSS corresponds to the work the designer does: deciding how things look.

In the early days, there was no CSS, so any control over what the page looked like was done with tags that controlled the form of the Web page. Tags like `<font>` to choose a font, `<b>` for bold, `<i>` for italic were added to have some control, and that let your page be at the mercy of whatever browser the reader was using. There are several problems with this approach. First, it violates our paradigm of HTML containing only content. Second, and more practically, the tags only applied where they were used.

For instance, if you originally wrote your document with all the paragraphs indented with a certain amount and then later you were decided to change the indentation, then you would have to modify every single paragraph in your document. It would be nice if there were a central way to set such rules, i.e. one place that said "I want all my paragraphs to be indented this much", much like master sheets in a word processor. CSS helps to solve this problem.



### The W3C CSS WG

The CSS Working Group (Cascading Style Sheets Working Group) is a [working group](https://en.wikipedia.org/wiki/Working_group) created by the W3C in 1997 to tackle issues that had not been addressed with [CSS](https://en.wikipedia.org/wiki/CSS) level 1. The [number of members](https://www.w3.org/Style/CSS/members) reaches 126 in December 2017!

<figure>
<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/93b25250542a4c7898d9184a93558f59/d01e4fccca73417fae77b8612cb8c9b5/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%40e05233c61bc842c9baad63c23ecc8ec6">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/399b45274a039620a540a7faca602183/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/CSSWG-TPAC16.jpg" style="margin: 0.1em;" alt="CSS groupe TPAC" title="CSS groupe TPAC" width=350>
  </a></div>
</div>
<figcaption>The CSS WG meeting in Lisbon, November 2016. The working group is co-chaired by Rossen Atanassov and Alan Stearns. (Photo credit: Marie-Claire Forgue)</figcaption>
</figure>

The CSS WG members are working on a [whole range of specifications](https://www.w3.org/Style/CSS/current-work), but their core document is [CSS snapshot 2017](https://www.w3.org/TR/css-2017/). This document collects together into one definition all the specs that together form the current state of Cascading Style Sheets (CSS) as of 2017. The primary audience is CSS implementers, not CSS authors, as this definition includes modules by specification stability, not Web browser adoption rate.



### An example

Let's see CSS in action. Below, we see two identical copies of HTML, however, styled differently.

Here is the HTML:

```html
<p>She looked over the top of her book and whispered <q>I'm hungry.</q> My heart stopped.</p>
```

And now two very different looks:

<hr>
<p></p>
<div>
<p style="padding: 20px; font-size: 1.4em; line-height: 1.44em;">She looked over the top of her book and whispered <q style="margin-left:30px; margin-right:30px; font-size: .6em; line-height: 1.44em; vertical-align: baseline;">I'm hungry.</q> My heart stopped.</p>
</div>
<p></p>
<hr>

<div>
<p style="font-family: Serif; padding: 20px 20px; margin-left: 20%; margin-right: 20%; font-size:1.7em; line-height:.8em; border: 1px dotted darkgray; border-radius: 20px; background-color: rgb(250,250,250);">She looked over the top of her book and whispered <q style="display: block; margin-top: 10px; margin-bottom: 30px; color: lightgray; font-size: 1.8em; font-weight:bold; text-align: center; line-height: 2em; padding: 20px; text-shadow: 0px 0px 10px black; font-family: sanserif, monospace; text-transform:lowercase;">I'm hungry.</q> My heart stopped.</p>
</div>

Both of these use the exact same HTML. It is the CSS that makes them so different. So let's get started.



## 3.2 CSS basic syntax

### Style and link tags

#### 'style' tag

The best practice when working with CSS is to keep it in an external file using the `<link>` tag, however, when starting, it is simpler to merely place it directly into the document under edit.  

To place CSS directly into an HTML document, we use the `<style>` tag.  This tag can appear anywhere in an HTML document, however, the most common practice is to place it in the `<head>` section.  Such as:

```html
<!DOCTYPE html>
<html lang="en">
 
  <head>
    <meta charset="UTF-8">
    <title>Style and link tags</title>
    <style>
      /* CSS will go in this area */
    </style>
  </head>
 
  <body>
  </body>
</html>
```

#### 'link' tag

While `<style>` is convenient, the better practice is to put the CSS into a separate file. One of the key advantages of using a separate file is that the CSS styles can easily be re-used between your different .html pages.  Many authors further divide their CSS up into different files (for example: one for text styles and another one for layout).  

Simply put your CSS into a separate file. This file does not need any HTML markup (i.e., no `<style>` tag required).  Use the .css file extension and use a `<link>` tag to bind it in. The `<link>` tag must appear in the `<head>` section.  By convention, css files are kept in a directory named css.

Use this `<link>` as a template:

```html
<link rel="stylesheet" href="css/my_styles.css">
```

Here is an example HTML document.

```html
<!DOCTYPE html>
<html lang="en">
 
  <head>
    <meta charset="UTF-8">
    <title>Style and link tags</title>
    <link rel="stylesheet" href="css/my_styles.css">
  </head>
  <body>
  </body>
</html>
```


### Selectors and declarations

At its simplest, CSS is just a list of rules.  Each rule consists of a selector and a declaration.  Here is an example:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/93b25250542a4c7898d9184a93558f59/5ca9519c008c4fe7b6ada01210cae4bf/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%404331dbb577ba4efc97fb9fff6686037b">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7aeb1eae7e4bc674083b56e47c0fa9f1/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/select-declare.jpg" style="margin: 0.1em;" alt="selector declaration diagram" title="selector declaration diagram" width=250>
  </a></div>
</div>


#### Selector

In the above, the selector is <strong>p</strong>.  When a selector appears unprefixed by any punctuation, then it is assumed to match to an HTML tag.  Thus, the <strong>p</strong> selector will apply the CSS rule to all `<p>` tags in the document. 

We will cover more selector possibilities in the future.


#### Declaration

The declaration part of a CSS rule opens and closes with curly braces: __{  }__<br>
_And between them, you can put any number of property value pairs._


#### Properties and Values

There are hundreds of different visual properties that may be set via CSS.  And each property has a range of possible values that it can be set to.  Syntactically, property value pairs are simple. Each pair consists of a _property_, followed by a colon : followed by a _value_ and terminated by a semi-colon ;

<p><code><span style="color: #333399;">font-size</span>: <span style="color: #008000;">12px</span>;</code></p>


#### Best practice

In the example above, the entire CSS rule is written on one line.  This is not uncommon when the declaration of the CSS rule only has one property.  If a CSS rule has several properties, then it should be written to use one line per property value pair. For example:

```css
p {
  font-size: 12px;
  line-height: 15px;
  color: #223344;
}
```


### Comments

CSS can include "comments" as well, by which you, the developer today, can leave notes and reminders to you, a different developer tomorrow. Or to others who might read your CSS.  

Comments begin with /* and must end with */ and they can span several lines. But they cannot be nested.

```css
p {
  font-size: 8px; /* client insists small text makes them more 'professional'. */
  /* I hope his idea of 'professional' includes paying on time. */

  line-height: 24px; /* see above */

  /* none of the stuff below is working. I don't know why.

  margin-top: 5%;
  margin-bottom:6%;
  */
}
```


### Knowledge checks


1. Tag support

  Which tag supports CSS code between its opening and closing tag?

  1. `<div> ... </div>`
  2. `<css> ... </css>`
  3. `<style> ... </style>`
  4. `<link> ... </link>`

  Ans: 3 <br/>
  Explanation: The `<style>` tag is used to place CSS code directly into an HTML document. While not considered a best practice it is convenient, especially for testing or exploration.


2. Link use

  Which of the following uses of the `<link>` tag is correct?

  1. `<link rel="stylesheet" href="css/my_styles.css" >`
  2. `<link rel="stylesheet" src="css/my_styles.css" >`
  3. `<link rel="css" >`
  4. `<link href="css/my_styles.css" >`

  Ans: 1 <br/>
  Explanation: The `<link>` tag needs two attributes specified, `rel` which must be "stylesheet" and `href` which names the CSS file.


3. Leveraging CSS

  What is the general best practice for leveraging CSS from a Web page?

  1. Bind in CSS from an external file with a `<link>` tag
  2. Enter CSS directly into a `<style>` block

  Ans: 1 <br/>
  Explanation: Keeping CSS in an external file is generally considered the best practice. CSS in an external file can be used by several different Web pages.


4. External CSS file

  Does the CSS in an external CSS file, like `my_file.css`, need to be surrounded by `<style> ... </style>` tags?

  Ans: No <br/>
  Explanation: An external `.css` file is not an HTML document and needs no tagged markup. The CSS can be included directly. Though, a good practice is to leave a comment at the top of the CSS file.

  ```css
  /* 
  my_styles.css 
  Jan 1, 2016 -- defining basic styles for website. 
  Jan 9, 2016 -- client wants color scheme changed to match favorite sports team (Go Barca!). 
  */
  ```



### Activity - use CSS

Use CSS on the following HTML code. Try various styles, experiment, and have fun. We have a live coding demonstration below working with the same source.

You are welcome to edit the following [CodePen](https://codepen.io/w3devcampus/pen/QvQgbr) sample file.

... or work from the lines of code below (to paste in your favorite Web editor):

```html
<!DOCTYPE html>
   <html lang="en">
     <head>
         <meta charset="UTF-8">
         <title>On the Inventor of Gunpowder</title>
         <style>
            /* CSS */
      </style>
    </head>
 
   <body>
      <h1>On the Inventor of Gunpowder.</h1>
 
      <address rel="author">By John Milton</address>
 
      <p>Praise in old time the sage Prometheus won,<br>
      Who stole ethereal radiance from the sun;<br>
      But greater he, whose bold invention strove<br>
      To emulate the fiery bolts of Jove.</p>
   </body>
</html>
```

You could also take another short text (such as a poem) and apply the styles you like on it.


### CSS rules

<video src="https://edx-video.net/W3CHTM502016-V013900_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@cf67dfbd406b464c9d65214edfd1cb46/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>

[Example code](src/3.2.5-UseCSS.html)



## 3.3 CSS properties

### Common CSS properties

There are hundreds of CSS properties for you to use. The [complete list](https://www.w3.org/Style/CSS/all-properties.en.html) is available on the W3C Web site (or also, see the [CSS reference page on the MDN Web site](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)).

Below we've gathered a more manageable list of the most useful and common CSS properties: `font-size`, `line-height`, `text-align`, `text-decoration`, `font-weight`, `font-style` and `font-family`.


#### font-size

`font-size` can be used to size the text of a tag.  The value for the font-size has two parts: a number and a unit.  Some of the most common units are: `px`, `em`, `%`, `vh`.  For example:

```css
p { font-size: 18px; }
q { font-size: .8em; }
blockquote { font-size: 10vh; }
```

These units are discussed below.

Additionally, `font-size` supports a more readable set of values that many authors prefer: <span style="color: #ff6600;">xx-small</span>, <span style="color: #ff6600;">x-small</span>, <span style="color: #ff6600;">small</span>, <span style="color: #ff6600;">medium</span>, <span style="color: #ff6600;">large</span>, <span style="color: #ff6600;">x-large</span>, <span style="color: #ff6600;">xx-large</span><br/>
and relative sizing (relative to the text of the parent): <span style="color: #ff6600;">larger</span>, <span style="color: #ff6600;">smaller</span>. For example:

```css
p { font-size: medium; }
q { font-size: small; }
blockquote { font-size: larger; }
```


#### line-height

Whereas `font-size` may drive the size of the text itself, the `line-height` property drives the height of the space it is drawn into.  A large `line-height` will give the text more spacing. A small line-height will smash the text lines together.  

For example, all of the Middlemarch text below has `font-size:16px;` <br/>
But on the left, we see `line-height:0.5;` and on the right, `line-height:3;` 

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<tbody>
  <tr><th style="text-align: left;"><span style="color: #333399;">line-height</span>: <span style="color: #008000;">0.5</span>;</th><th style="text-align: left;"><span style="color: #333399;">line-height</span>: <span style="color: #008000;">3</span>;</th></tr>
  <tr>
    <td style="font-size: 16px !important; line-height: 8px !important;">Miss Brooke had that kind of beauty which seems to be thrown into relief by poor dress.</td>
    <td style="font-size: 16px !important; line-height: 30px !important;">Miss Brooke had that kind of beauty which seems to be thrown into relief by poor dress.</td>
  </tr>
</tbody>
</table>


The used value is this unitless `<number>` multiplied by the element's font size. The computed value is the same as the specified `<number>`. In most cases __this is the preferred way__ to set `line-height` with no unexpected results in case of inheritance. Read more on the MDN Web site.


#### text-align

Anyone familiar with a text editor will be familiar with this property. It can be used to align the text <span style="color: #ff6600;">left</span>, <span style="color: #ff6600;">center</span> or <span style="color: #ff6600;">right</span>.  There are additional possible values like justify and justify-all . It usually defaults to left. However, remember that you shouldn't  use text-align unnecessarily.

Note that text-align may __not__ work as expected if applied to elements that are the same width as their text, or whose width is determined by the text within them (i.e., inline elements).  The tags `<span>`, `<a>`, `<i>`, `<b>`, `<q>` and others are considered "inline" because they do not receive their own new line when used. And text-align is often not useful on these tags.

But it is useful on block level text tags, such as `<p>`, `<li>`, `<ul>`, `<ol>`, `<div>`, and `<blockquote>`

```css
p { text-align: left; }
blockquote { text-align: right; }
```

Bear in mind, also, that you should only use `text-align` when the alignment really needs to be changed, since it can cause additional work to reverse all the values when translating into languages that use Arabic, Hebrew, Thaana scripts, scripts (the default alignment for those languages is right).  The new values <span style="color: #ff6600; font-weight: bold;">start</span> and <span style="color: #ff6600; font-weight: bold;">end</span> are currently being implemented in browsers, and those will be a much better choice than <span style="color: #ff6600;">left</span> and <span style="color: #ff6600;">right</span> once Internet Explorer supports them.

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<tbody>
  <tr><th style="background-color: lightgray;">left</th><th style="background-color: lightgray;">center</th></tr>
  <tr>
    <td style="text-align: left;">It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair.</td>
    <td  style="text-align: center;">It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair.</td>
  </tr>
  <tr><th style="background-color: lightgray;">right</th><th style="background-color: lightgray;">justify</th></tr>
  <tr>
    <td  style="text-align: right;">It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair.</td>
    <td  style="text-align: justify;">It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair.</td>
  </tr>
</tbody>
</table>

Note that CSS will in the future provide better support for justification in languages where words are not separated by spaces, such as Chinese and Thai, or languages where words are separated by special marks, such as in Amharic. For more information about different approaches to justification see [this article](https://www.w3.org/International/articles/typography/justification). Once you finish this course, look out for these and other international features of CSS as you explore its features further.


#### Text-decoration (underline)

How do I underline text? This is a common question. In CSS, this is done via the text-decoration property.  The values for this are: `underline`, `overline`, `line-through`, and `none`;  They can combined.

```css
p { text-decoration: underline; }
a { text-decoration: none; } /* hyperlinks are underlined by default, but that can be removed */ 
span { text-decoration: overline; }
span { text-decoration: underline overline; } /* apply two with just a space between the values */
span { text-decoration: underline overline line-through; } /* everything */
```

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<tbody>
  <tr><th style="background-color: lightgray; width: 10%; text-align: left;">underline</th><th style="background-color: lightgray; width: 10%; text-align: left;">overline</th><th style="background-color: lightgray; width: 10%; text-align: left;">line-through</th><th style="background-color: lightgray; width: 10%; text-align: left;"><span>underline overline line-through</span></th></tr>
  <tr>
    <td style="text-decoration: underline;">Middlemarch</td>
    <td style="text-decoration: overline;">Middlemarch</td>
    <td style="text-decoration: strike;">Middlemarch</td>
    <td style="text-decoration: underline overline line-through;">Middlemarch</td>
  </tr>
</tbody>
</table>

Note: there are other properties that can help customize the text decoration, such as `text-decoration-color` and `text-decoration-style`, but they are not well supported across browsers (see [related caniuse table](https://caniuse.com/#search=text-decoration))


#### font-weight (bold)

Earlier we saw that the `<b>` and `<strong>` tags would make text bold-faced. However, semantically speaking, that is a mere side-effect of the tag. Any tag can make the text bolder (or less bold) via the `font-weight` CSS property.  While common values are <span style="color: #ff6600;">normal</span> and <span style="color: #ff6600;">bold</span>, text can also be made bolder (or less bold) than its parent with the values bolder and lighter. Lastly, the font-weight can be set explicitly as a numeric value. The choices are: <span style="color: #ff6600;">100, 200, 300, 400, 500, 600, 700, 800</span> and <span style="color: #ff6600;">900</span>.

<span style="color: #ff6600;">normal</span> maps to <span style="color: #ff6600;">400</span> and <span style="color: #ff6600;">bold</span> to <span style="color: #ff6600;">700</span>. However, the different numeric choices will only work for fonts that support a full range of font-weights. Many times the numeric weights will simply be mapped back to bold or normal.

```css
p { font-weight: bold; }
blockquote { font-weight: 900; }
```

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<tbody>
  <tr><th style="background-color: lightgray; width: 10%; text-align: left; line-height: 1.2rem;">normal</th><th style="background-color: lightgray; width: 10%; text-align: left; line-height: 1.2rem;">bold</th><th style="background-color: lightgray; width: 10%; text-align: left; line-height: 1.2rem;">200</th><th style="background-color: lightgray; width: 10%; text-align: left; line-height: 1.2rem;">500</th><th style="background-color: lightgray; width: 10%; text-align: left; line-height: 1.2rem;">700</th><th style="background-color: lightgray; width: 10%; text-align: left; line-height: 1.2rem;">900</th></tr>
  <tr>
    <td style="font-weight: norm">A Tale of Two Cities</td>
    <td style="font-weight: bold">A Tale of Two Cities</td>
    <td style="font-weight: 200">A Tale of Two Cities</td>
    <td style="font-weight: 500">A Tale of Two Cities</td>
    <td style="font-weight: 700">A Tale of Two Cities</td>
    <td style="font-weight: 900">A Tale of Two Cities</td>
  </tr>
</tbody>
</table>


#### FONT-STYLE (italic)

Earlier we saw that the `<i>` and `<em>` tags could make text italicized. But, just as we saw when discussing font-weight, this can be changed with CSS, and any tag can make its text italic or oblique with the font-style property.  The choices of values for this property are <span style="color: #ff6600;">normal</span> and <span style="color: #ff6600;">italic</span>.  

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<tbody>
  <tr style="background-color: lightgray; text-align: left; line-height: 1.2rem;"><th>font-style: normal;</th><th>font-style: italic;</th></tr>
  <tr>
    <td style="font-style: normal;">Many years later, as he faced the firing squad, Colonel Aureliano Buendía was to remember that distant afternoon when his father took him to discover ice.</td>
    <td style="font-style: italic;">Many years later, as he faced the firing squad, Colonel Aureliano Buendía was to remember that distant afternoon when his father took him to discover ice.</td>
  </tr>
</tbody>
</table>



#### font-family

Want to set the font for an item on the page?   The `font-family` is the correct property for the task, but there are caveats:

+ the various browsers only guarantee a few standard choices: <span style="color: #008080;">serif</span>, <span style="color: #008080;">sans-serif</span>, <span style="color: #008080;">monospace</span>, <span style="color: #008080;">cursive</span>, and <span style="color: #008080;">fantasy</span>.
+ any other choice must be already installed on the users machine.
+ or you may use a "Web font", but your choices, while plentiful, may not match the choices you are used to.  
+ your favorite font on your machine is probably encumbered by licensing limitations and is not available. You can certainly specify it to be used, but if the end user doesn't have it themselves, they won't see it. And you can't "give" it to them. Again, "Web fonts" are the alternative here. 

To help ameliorate these limitations, the font-family property accepts a list of possible font choices.  The browser will start with trying the first font listed, and if not available (or not having a needed glyph) it will then proceed to the next font in the list, and so on.  Here is a typical font-family declaration:

```css
p { font-family: "Helvetica", "Verdana", "Arial", sans-serif; }
```

The rule above says to first try the font named "Helvetica". If it isn't available, try "Verdana", failing that "Arial", and lastly fall back to the built in `sans-serif` browser font.

+ each of the named font families is separated by a comma ( , )
+ if the font family name contains any spaces (or certain other characters) it __must__ be surrounded by quotes. Font names tend to be complex, and the exact rules for when quotes are required are arcane, so the simplest and best practice is to __always surround the font family name in quotes__, excepting the five built-ins (serif, sans-serif, etc.)

Web fonts are outside the scope of this course. Google provides a nice selection of licensed free Web fonts. Type "_google Web font tutorial_" into any search engine to learn more.  


### Margin and color

#### Margin

We will examine layout in a later unit. But the `margin` property is the lynch-pin for positioning elements. Whenever you want to move something a little the `margin` property should be your first thought, when having layout problems, it is the first thing you should check.  

The margin can be a bit confusing.  Depending upon context, it will space an item away from its immediate neighbors (in the HTML) or from the edges of its parent. Also, there is not only one `margin` property, but five:

``` css
p { margin: 10px; }  /* a 10 pixel margin will be applied around all four sides of the item */

p {
 margin-left:   10px;
 margin-right:  10px;
 margin-top:    10px;
 margin-bottom: 10px;
}  
```

#### Color

The `color` property can be used to set the text color of an element. There are several possible formats for the value.


##### Named colors

```css
p { color: blue; }
b { color: transparent; } /* transparent */
i { color: lightgrey; }
```

There are scores of different names. The most common English names for colors are all supported, plus many others.

One of the more interesting is transparent, which will make the text invisible. However, if you want to make an HTML element invisible, then the <span style="color: #333399;">display</span>:<span style="color: #ff6600;">none</span>; or <span style="color: #333399;">visibility</span>:<span style="color: #ff6600;">hidden</span>; rules are preferred. They are discussed in a future section.


##### rgb/rgba

```css
p { color: rgb(10, 200, 255); }
p { color: rgb(0, 0, 0); }       /* 0,0,0 is black */
p { color: rgb(255, 255, 255); } /* 255,255,255 is white */
b { color: rgba(10, 200, 255, 0.5); }  /* semi-transparent */
```

Generally, any color on a computer is exactly specified by mixing three components together: red, green, and blue. The amount of each component falls within a range between 0 and 255.   So the rgb() function can be used to specify a color.  

+  <span style="color: #ff6600;">rgb</span>(  <span style="color: #008000;">red, green, blue</span>);  
+ parenthesis required, commas between each component.

Similarly, the `rgba()` function can be used for semi-transparent colors. The fourth value is for the "alpha channel" (thus the "a" in "rgba") and means the opacity. It is a number between 0 and 1 (for example, 0.5 ).


##### Hex code

```css
p { color: #3A2BFF; }
```

Quicker than the lengthy rgb() function is simply providing an [hexadecimal (hex) code](https://en.wikipedia.org/wiki/Hexadecimal). This always starts with the pound sign (#) and is followed by three pairs of hex number, ranging 00 to FF. Constructing rgb triplets is hard enough, and deciphering and generating hex codes is even harder. However, almost every editor and color picker will at least show you red, green and blue values and many have hex code displayed as well.  


### Units

`font-size`, `line-height`, `margins` and many other CSS properties expect some sort of dimension value. Dimension values support a wide variety of units. But the most common and useful ones are: <span style="color: #008000;">px, em, rem, %, vh</span> and <span style="color: #008000;">vw</span>.


#### px

'px' is short for 'pixel', which is a single dot on the screen.   So text with `font-size:20px` is 20 pixels tall on-screen. In actuality, due to browser zooming, retina displays, or other factors, this may or may not match to 20 physical on-screen pixels.

px are useful for both horizontal and vertical dimensions.


#### em

'em' is a typographic term that has come to the Web. On the Web, em units are usually used for vertical dimensions.  One 'em' maps to the height of one capital letter in the parent context.

```csss
li { font-size: 0.9em; }  /* text in a list item is smaller than its parents */
h1 { font-size: 1.2em; }  /* but an h1 will be bigger than the parent */
i  { font-size: 0.5em; }  /* and any italicized text will be half as big. */
```

All the text sizes above are relative to the pages base sizes.  You'll see radically different results on the rest of the page from either of these rules applied to the body, but relative to one another they'll remain sized correctly.

<table style="border-spacing: 0px; table-layout: auto; line-height: 22.4px; width: 100%; margin: 20px 0px; color: #222222; font-family: 'Open Sans', Verdana, Geneva, sans-serif, sans-serif;">
<tbody style="line-height: 1.4em;">
  <tr style="line-height: 1.4em;">
    <td style="vertical-align: top; line-height: 1.4em; border-color: #c8c8c8;"><code style="font-size: 1em; line-height: 1.4em;"><span style="font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; color: #0000ff;">html, body</span>&nbsp;{&nbsp;<span style="font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; color: #333399;">font-size</span>:&nbsp;<span style="font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; color: #008080;">50px</span>; }&nbsp;<span style="font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; color: #808080;">/* 50 px&nbsp;base text size */</span></code></td>
    <td style="vertical-align: top; line-height: 1.4em; border-color: #c8c8c8;"><code style="font-size: 1em; line-height: 1.4em;"><span style="font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; color: #0000ff;">html, body</span>&nbsp;{&nbsp;<span style="font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; color: #333399;">font-size</span>:&nbsp;<span style="font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; color: #008080;">20px</span>; }&nbsp;<span style="font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; color: #808080;">/* 20 px&nbsp;base text size */</span></code></td>
  </tr>
</tbody>
</table>



#### rem

'rem' is much like 'em', except that 'em' sizes an element relative to its parent, and 'rem' always derives its size relative to the root.  In an HTML document with lots of nested elements, 'rem' will generally prove to be more reliable than 'em'.  'rem' is supported in all modern day browsers, including mobile, but not older ones. 

Using the CSS rules from the em section immediately above, nested list items (`<li>birds<ul><li>hawk</li></ul></li>`)would get increasingly smaller. And if 'rem' units were used, they would be the same size.

Note: to ensure you are setting the root size, use __both__ the `html` and `body` selectors.

```css
html, body { font-size: 20px; }
```


#### %

Whereas em is a measure relative to the parents text size, the percentage unit (%) is relative to the parent dimension.  This is a useful unit for both horizontal and vertical dimensions, though often more useful in the horizontal.  

```css
p {
  margin-left:  10%;
  margin-right: 10%;  /* 10% of parent width will be spent on the two side margins */
 }
```

Initially, the percentage unit may seem very handy (and it is), and many developers fall in love with it. But the love affair is usually short lived. One of the limitations of this rule is that for it to work correctly, the parent must have an explicit width or height set. This limitation is particularly noticeable in the vertical dimension. If the parent element doesn't have an explicit height set then child percentages may be percentages of 0. 


#### vh / vw

'vh' stands for viewport height, and 'vw' for viewport width.  The vh and vw units work much like the percentage ( % ) unit. But instead of percentage of the parent, it is percentage of the screen (aka viewport).  Obviously, vh is for vertical dimensions, and vw for horizontal dimensions.

vh and vw do not suffer the parent limitation that the % unit does.  Most modern browsers support these units, but there are some exceptions on older mobile browsers. 

```css
p { 
  margin-left:  10vw;
  margin-right: 10vw;  /* 10% of screen width will be spent on the two side margins */
 }
 ```


#### External Resources

The list of CSS units above is not exhaustive. There are various tutorials and explanations about CSS units on the internet. Here are a few that you might find helpful.

+ This CSS Tricks article from March 2016: "[Use rem for Global Sizing; Use  em  for Local Sizing](https://css-tricks.com/rem-global-em-local/)"
+ New CSS3 Units: [Root EM and Viewport Units](http://www.cssmine.com/css3-units)
+ From the W3C specification: [Viewport-percentage lengths](https://www.w3.org/TR/css3-values/#viewport-relative-lengths)


### Accessible typography

#### With great power comes great responsibility

The CSS rules with which we've started are fun and easily understandable. They are mostly concerned with typography. Later, we will see how to use CSS to include decorative images, look at other decorative properties, and take up the topic of layout.

But even with our modest start we must, once again, take up the topic of accessibility.  In Module 2, we learned that using the correct tag with the best semantic meaning is very important for a variety of reasons, one of which included visitors who may have a disability. If you clearly put your page navigation in a `<nav>` block, and use the header tags and others (like `<article>` or `<main>`), then this can greatly enhance the page experience for certain disabled visitors, like the blind who might be having the page read aloud to them with a screen reader.

Accessibility concerns are important for CSS usage as well. Perhaps doubly so. As page authors, if we don't use CSS, then the page visitor just sees the page with the default typography, and perhaps assisted by tools that can help zoom in on pages, make text bigger, invert colors for the light-sensitive, etc. But as we start to customize the look of the page with CSS, we may unintentionally thwart those tools or make the reading experience less comfortable for those with vision problems.


#### Guidelines

For accessible typography, there are really just a few things to avoid:

+ do not make text too small
+ do not make lines of text too tight
+ do not use foreground and background colors that are too close to one another, in other words, ensure there is good color contrast
+ do not irregularly space text or make it jump around

Look at those four guidelines. Can you match each guideline to one or more CSS property from earlier? Take a moment and think about it. We'll touch on specific rules below.


#### Properties

##### Font-size

Misuse of `font-size` might make text too small. So be wary of that. Furthermore, in the past the gold standard practice was to use `em` units instead of `px`. This is no longer as true as it was, but the practice of using `em` or `rem` units is definitely to be encouraged and it should be your default unit when working with text.


##### Line-height

An overly small `line-height` will cause lines to become cramped and difficult to read. Even the largest text can be rendered unreadable by a too small `line-height`. Generally, your `line-height` should always be at least one and a half times the `font-size` (ie, `line-height` should be greater than `1.5em`).


##### Color

Color contrast can be easily undone by misuse of the color property.  The exact rules for contrast are rather advanced. For example, "wide stroke" text is allowed to have less contrast than narrow stroke text.  But, regardless of rules, the overall concept is easy to understand: keep your text high contrast to the background. There are further color guidelines concerning certain combinations (like bright blue text on a bright red background), but the rule of thumb is that, if the text is at all hard for you to read, then just assume it is unreadable to someone with a visual disability. If you are interested, there are tools that can help such as [Tanaguru Contrast-Finder](http://contrast-finder.tanaguru.com/) or [Juicy Studio Luminosity Colour Contrast Ratio Analyser](http://juicystudio.com/services/luminositycontrastratio.php).


##### Text-align

Any long passage of text should have its alignment match its reading order. Which means, if the language is English, which is read left to right, then any long passage of text should be aligned left.  Right aligned or center aligned text can be very hard for dyslexics.

Obviously, a header or perhaps a menu might be exempt, because they are not typically long passages of text. So this guideline doesn't mean an end to good page layout and typography.


#### Summary
So now, we've seen how typography can affect the accessibility and approachability of your page. It is not so very difficult. Common sense and awareness are good companions and will serve you well.

If you are interested in accessibility, there is much more to learn. These simple guidelines merely scratch the surface.


### Knowledge checks


Here are some questions for a self check to make sure you understand everything. These questions are not graded.

1. Size me!

  Which CSS property lets you adjust the size of the text?

  Ans: font-size <br/>
  `font-size` is the CSS property that governs the text size.


2. Space control

  Which CSS property allows you to control the spacing between html items?

  Ans: `margin` or `margin:` or `margin-top` or `margin-top:` or `margin-left` or `margin-left:` or `margin-right` or `margin-right:` or `margin-bottom` or `margin-bottom:` <br/>
  The `margin` property governs basic spacing between items.


3. Font-size values

  Which of the following is __NOT__ an acceptable value for the `font-size` property?

  1. `medium`
  2. `x-small`
  3. `.4page`
  4. `1.2em`
  5. `.9rem`
  6. `larger`
  7. `14px`

  Ans: 3



### Activity - Units

With the HTML below, please size the text using different units:

+ Use `px` units to set the root size of the text for the document.
+ Use `rem` units to size the `h1` and `li` tags.
+ Change the text size of the root CSS rule. You should observe all the text of the document adjusting appropriately.
+ Change the `h1` so that it uses px units. As the root CSS rule is changed, the `h1` will no longer adjust with the rest of the document.

Please experiment by editing the following [Codepen](https://codepen.io/w3devcampus/pen/YVeQZN) [sample file](src/3.3.6-Units.html)



## 3.4 Lists and selectors

### Styling lists

The list markup tags (`<ul>`, `<ol>` and `<li>`) are some of the most frequently used specific purpose tags in HTML. There are a few CSS style properties that are available for lists.


#### list-style-type

`list-style-type` governs the little list marker that is usually positioned to the left of any list item.  For un-ordered lists (`<ul>`), there are several popular values: <span style="color: #ff6600;">disc, circle, square</span>, and <span style="color: #ff6600;">none</span>.

```css
li { list-style-type: disc; }
```

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<tbody>
  <tr style="background-color: lightgray; text-align: left; line-height: 1.2rem;"><th style="width: 10%;">html</th><th style="width: 5%;">default</th><th style="width: 5%;">disc</th><th style="width: 5%;">circle</th><th style="width: 5%;">square</th><th style="width: 5%;">none</th></tr>
  <tr>
    <td>
    <pre style="border: none;">&lt;ul&gt;
     &lt;li&gt;eggs&lt;/li&gt;
     &lt;li&gt;milk&lt;/li&gt;
     &lt;li&gt;bread&lt;/li&gt;
&lt;/ul&gt;</pre>
    </td>
    <td><ul><li>eggs</li><li>milk</li><li>bread</li></ul></td>
    <td><ul style="list-style-type: disc;"><li>eggs</li><li>milk</li><li>bread</li></ul></td>
    <td><ul style="list-style-type: circle;"><li>eggs</li><li>milk</li><li>bread</li></ul></td>
    <td><ul style="list-style-type: square;"><li>eggs</li><li>milk</li><li>bread</li></ul></td>
    <td><ul style="list-style-type: none;"><li>eggs</li><li>milk</li><li>bread</li></ul></td>
  </tr>
</tbody>
</table>

For ordered lists (`<ol>`) you can choose different ways of having the numbers shown: <span style="color: #ff6600;">decimal, decimal-leading-zero, lower-roman, upper-roman, lower-alpha, upper-alpha</span>, as well as several of the worlds languages: <span style="color: #ff6600;">armenian, georgian, simp-chinese-formal</span>, and many others.

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width="90%">
<tbody>
  <tr style="background-color: lightgray; text-align: left; line-height: 1.2rem;"><th style="width: 10%;">decimal</th><th style="width: 10%;">decimal-leading-zero</th><th style="width: 10%;">lower-roman</th><th style="width: 10%;">upper-alpha</th><th style="width: 10%;">simp-chinese-formal</th></tr>
  <tr>
    <td><ol style="list-style-type: decimal;"><li>eggs</li><li>milk</li><li>bread</li></ol></td>
    <td><ol style="list-style-type: decimal-leading-zero;"><li>eggs</li><li>milk</li><li>bread</li></ol></td>
    <td><ol style="list-style-type: lower-roman;"><li>eggs</li><li>milk</li><li>bread</li></ol></td>
    <td><ol style="list-style-type: upper-alpha;"><li>eggs</li><li>milk</li><li>bread</li></ol></td>
    <td><ol style="list-style-type: simp-chinese-formal;"><li>eggs</li><li>milk</li><li>bread</li></ol></td>
  </tr>
</tbody>
</table>


#### list-style-position

Besides choosing the type of marker applied to each list item, you may also want to govern how closely it is positioned to the list itself. The `list-style-position` property handles that.  The two values are <span style="color: #ff6600;">inside</span> and <span style="color: #ff6600;">outside</span>.  They govern whether the markers are positioned inside the box of the list, or outside. This is most evident if a border or background or similar is applied to the list. Below, we have put a blue border on the list. 

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width="50%">
<tbody>
  <tr style="background-color: lightgray; text-align: left; line-height: 1.2rem;"><th>outside</th><th>inside</th></tr>
  <tr>
    <td><ol style="border: 1px blue solid; list-style-position: outside;"><li>eggs</li><li>milk</li><li>bread</li></ol></td>
    <td><ol style="border: 1px blue solid; list-style-position: inside;"><li>eggs</li><li>milk</li><li>bread</li></ol></td>
  </tr>
</tbody>
</table>



#### list-style-image

The little markers on a list can also be customized to be an image of your choosing. This will require you to have a small image in a Web compatible format (PNG or JPEG recommended) and to know the path from the place where the CSS is being defined to the image.  Image pathnames were covered in Module 2, and we'll be discussing them again in the background-image section. 

```css
li { list-style-image: url("my_triangle.png"); }
```

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width="40%">
<tbody>
  <tr style="background-color: lightgray; text-align: left; line-height: 1.2rem;"><th>list-style-image</th></tr>
  <tr>
    <td>
      <ul><li style="list-style-image: url('https://prod-edxapp.edx-cdn.org/assets/courseware/v1/073e0b55b08d259174c48c569c6696d9/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/my_triangle.png');">eggs</li><li style="list-style-image: url('https://prod-edxapp.edx-cdn.org/assets/courseware/v1/073e0b55b08d259174c48c569c6696d9/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/my_triangle.png');">milk</li><li style="list-style-image: url('https://prod-edxapp.edx-cdn.org/assets/courseware/v1/073e0b55b08d259174c48c569c6696d9/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/my_triangle.png');">bread</li>
      </ul>
    </td>
  </tr>
</tbody>
</table>

Note that the browser will do little more than draw the image.  There is no guarantee to scale the image or assist with spacing or alignment.  Many users find `list-style-image` to be frustrating and instead use the `background-image` CSS property which has more options. There is a section dedicated to the `background-image` property.  


### Selectors

Earlier, we learned that a CSS rule is made up of two parts: the selector and the declaration. We've seen quite a few different declarations, but the only selector we've learned is the tag selector. There are other choices, and they can be composed together in interesting and useful ways. So let's learn some more CSS selectors.


#### Tag selector

We've already seen this one. A CSS selector that consists solely of a single tag (without punctuation or spacing) will be applied to any matching tag on the page.

```css
li { list-style-type: circle; }
```


#### id selector

You may remember the `id` attribute (short for "identifier"). This attribute can be applied to an HTML tag to uniquely identify the element. Recall that the value for any given `id` attribute can only appear once in a document. No two tags are allowed to have the same id. You may also recall that the id cannot contain spaces, nor most punctuation, nor begin with numbers.

In the HTML below, there are two paragraph tags. So, to style them individually, we can apply unique `id` attributes to the paragraphs (`id="p18"` and `id="p19"`). In the CSS, we will use the id selector.  The id selector is simply a hash sign (#) followed directly by the id.  

CSS:

```css
#p18 { color: blue; }
#p19 { color: green; }
```

HTML:

```html
<p id="p18">He is Ulysses, a man of great craft, son of Laertes. He was born in 
  rugged Ithaca, and excels in all manner of stratagems and subtle cunning.</p> 
<p id="p19">Madam, you have spoken truly.</p>
```

Result

<table style="border: 1px lightgray solid;" width="100%">
<tbody>
  <tr>
    <td>
      <p style="color: blue;">He is Ulysses, a man of great craft, son of Laertes. He was born in rugged Ithaca, and excels in all manner of stratagems and subtle cunning.</p>
      <p style="color: green;">Madam, you have spoken truly.</p>
    </td>
  </tr>
</tbody>
</table>


#### Class selector

The `class` attribute is similar to the id. However, whereas the `id` must be unique and singular, the values of the `class` attribute can be shared by multiple tags. And, multiple classes can be assigned to a tag by simply separating them with spaces.  

HTML

```html
<ul>
  <li class="bird flying">eagle</li>
  <li class="bird">ostrich</li>
  <li class="insect">ant</li>
  <li class="insect flying">moth</li>
</ul>
```

The class selector is simply a period (.) followed by the class name itself.

CSS

```css
.bird   { color: blue; }
.insect { color: green; }
.flying { text-decoration: underline; }
```

Result

<table>
<tbody>
  <tr>
    <td>
    <ul><li style="color: blue; text-decoration: underline;">eagle</li><li style="color: blue;">ostrich</li><li style="color: green;">ant</li><li style="color: green; text-decoration: underline;">moth</li></ul>
    </td>
  </tr>
</tbody>
</table>



### Combining selectors

Being able to define a CSS selector in terms of a tag, class or id is very powerful. But it's not practical to place classes on every tag in your document, much less to put unique ids throughout.  It's also inconvenient to constantly repeat CSS rules. But by combining composing selectors, all that can be avoided.  


#### Comma separated selectors

Let's say we want to make all our `<blockquote>` tags, `<q>` tags, and anything with "speech" in it's class string, to be red italic text.  How might we do that?  We could make three separate rule sets.  Or, better, we can separate our selectors with commas (,) before one rule set.  Like so:

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width="70%">
<tbody>
  <tr style="background-color: lightgray; text-align: left; line-height: 1.2rem;"><th style="width: 20%;">separate</th><th style="width: 20%;">joined</th></tr>
  <tr>
    <td><code><span style="color: #0000ff;">blockquote</span> {<br>&nbsp; color: <span style="color: #ff6600;">red</span>;<br>&nbsp; <span style="color: #333399;">font-style</span>: <span style="color: #ff6600;">italic</span>;<br> }<br><span style="color: #0000ff;">q</span> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{<br>&nbsp; <span style="color: #333399;">color</span>: <span style="color: #ff6600;">red</span>;<br>&nbsp; <span style="color: #333399;">font-style</span>: <span style="color: #ff6600;">italic</span>;<br> }<br><span style="color: #0000ff;">.speech</span> &nbsp; &nbsp;{<br>&nbsp; <span style="color: #333399;">color</span>: <span style="color: #ff6600;">red</span>;<br>&nbsp; <span style="color: #333399;">font-style</span>: <span style="color: #ff6600;">italic</span>;<br> }</code></td>
    <td><code><span style="color: #0000ff;">blockquote</span>, <br><span style="color: #0000ff;">q</span>, <br><span style="color: #0000ff;">.speech</span> {<br>&nbsp; &nbsp;<span style="color: #333399;">color</span>: <span style="color: #ff6600;">red</span>;<br>&nbsp; &nbsp;<span style="color: #333399;">font-style</span>: <span style="color: #ff6600;">italic</span>; &nbsp;&nbsp;<br>}</code></td>
  </tr>
</tbody>
</table>


The joined version on the right is much easier to read and maintain.  

If the "speech" items need to also be bold, that can simply be added by an additional rule:

```css
blockquote, 
q, 
.speech {
   color: red;
   font-style: italic;   
} 
.speech { font-weight: bold; }
```


#### Specialized selectors

If two selectors of different types (like tag and class) appear next to each other with no spacing separating them, then they form a specialized selector. To match, a candidate must match __both__ rules.  If a tag selector is used, it must appear first.  

This is most useful with class and tag selectors, like so:

```css
blockquote.speech { font-color: green; }
```

In the example above, the `blockquote.speech` selector is a blockquote tag selector combined with a .speech class selector.  So this rule will not necessarily apply to every `blockquote`, nor every element with the speech class. Instead, it will only apply to those blockquotes that also have the speech class.

It isn't unusual to see multiple classes joined this way as well:

```css
.insect.flying { text-decoration: underline; font-weight:bold; }
```

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width="70%">
<tbody>
  <tr style="background-color: lightgray; text-align: left; line-height: 1.2rem;"><th>html</th><th>css</th><th>result</th></tr>
  <tr>
    <td>
    <pre style="border: none;">       &lt;ul&gt;
          &lt;li class="bird flying"&gt;parrot&lt;/li&gt;
          &lt;li class="bird"&gt;ostrich&lt;/li&gt;
          &lt;li class="insect"&gt;ant&lt;/li&gt;
          &lt;li class="insect flying"&gt;wasp&lt;/li&gt;
          &lt;li class="insect flying"&gt;moth&lt;/li&gt;
          &lt;li class="flying"&gt;airplane&lt;/li&gt;
        &lt;/ul&gt;
       </pre>
    </td>
    <td>
    <pre style="border: none;"><span style="color: #0000ff;">    .insect.flying</span> {
          <span style="color: #333399;">text-decoration</span>: <span style="color: #ff6600;">underline</span>; 
          <span style="color: #333399;">font-weight</span>: <span style="color: #ff6600;">bold</span>; 
    }
     </pre>
    </td>
    <td>
    <ul>
      <li style="color: blue; text-decoration: underline;">parrot</li>
      <li style="color: blue;">ostrich</li>
      <li style="color: green;">ant</li>
      <li style="color: green; text-decoration: underline;">wasp</li>
      <li style="color: green; text-decoration: underline;">moth</li>
      <li style="text-decoration: underline;">airplane</li>
    </ul>
    </td>
  </tr>
</tbody>
</table>


#### Descendant selectors

In the following HTML, we see some paragraphs that have some links (`<a>`) inside. The link tags are inside the paragraphs, but not necessarily direct children.  

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;section</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"intro"</span><span class="tag">&gt;</span><span class="pln">Welcome to </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"#palaceland"</span><span class="tag">&gt;</span><span class="pln">PalaceLand</span><span class="tag">&lt;/a&gt;</span><span class="pln">, world renown </span><span class="tag">&lt;q&gt;</span><span class="pln">Land of endless palaces and </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"#delight"</span><span class="tag">&gt;</span><span class="pln">delights</span><span class="tag">&lt;/a&gt;&lt;/q&gt;</span><span class="pln">. As you make your way about, remember the words of our founder </span><span class="tag">&lt;blockquote&gt;</span><span class="pln">Shouldn't we have </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"#chairs"</span><span class="tag">&gt;</span><span class="pln">chairs</span><span class="tag">&lt;/a&gt;</span><span class="pln">? Never made much sense wandering room a room looking for a place to sit a spell. Folk that don't sit are not likely all right in the </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"#head"</span><span class="tag">&gt;</span><span class="pln">head</span><span class="tag">&lt;/a&gt;&lt;/blockquote&gt;&lt;/section&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;section</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"guideline"</span><span class="tag">&gt;</span><span class="pln">There are guidelines to follow while in </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"#palaceland"</span><span class="tag">&gt;</span><span class="pln">PalaceLand</span><span class="tag">&lt;/a&gt;</span><span class="pln">. They are outlined on the back of your </span><span class="tag">&lt;q&gt;</span><span class="pln">Daring Footman </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"#trademark"</span><span class="tag">&gt;</span><span class="pln">(tm)</span><span class="tag">&lt;/a&gt;&lt;/q&gt;</span><span class="pln"> card. But the spirit of the guidelines are best summed up by our founder </span><span class="tag">&lt;blockquote&gt;</span><span class="pln">Don't just </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"#standthere"</span><span class="tag">&gt;</span><span class="pln">stand there</span><span class="tag">&lt;/a&gt;</span><span class="pln"> with your mouth hanging open waiting for a pair of nesting birds.</span><span class="tag">&lt;/blockquote&gt;</span><span class="pln"> (and no </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"#camera_policy"</span><span class="tag">&gt;</span><span class="pln">flash photography</span><span class="tag">&lt;/a&gt;</span><span class="pln"> please.)</span><span class="tag">&lt;/section&gt;</span><span class="pln"> </span></li>
</ol></div>

What if we wanted all the links in the introductory section to be red, but all the link in the guideline section to be green?  That is what descendant selectors are for. Here is an example for the problem we are facing:

```css
#intro a { color: red; }
#guideline a { color: #00FF00; }
```

We merely separate the tag, identifier, or class selectors by a space.

So, in the first rule, we see that the selector will match to any `<a>` tag that is a descendant of `#intro`.  The `<a>` tag can appear directly within `#intro`, or be buried within its children.  Here is the result:

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<tbody>
  <tr>
    <td>
      <div id="intro">Welcome to <a href="#palaceland">PalaceLand</a>, world renown <q>Land of endless palaces and <a href="#delight">delights</a></q>. As you make your way about, remember the words of our founder
      <blockquote>Shouldn't we have <a href="#chairs">chairs</a>? Never made much sense wandering room a room looking for a place to sit a spell. Folk that don't sit are not likely all right in the <a href="#head">head</a></blockquote>
      </div>
      <div id="guideline">There are guidelines to follow while in <a href="#palaceland">PalaceLand</a>. They are outlined on the back of your <q>Daring Footman <a href="#trademark">(tm)</a></q> card. But the spirit of the guidelines are best summed up by our founder
      <blockquote>Don't just <a href="#standthere">stand there</a> with your mouth hanging open waiting for a pair of nesting birds.</blockquote>
      (and no <a href="#camera_policy">flash photography</a> please.)</div>
    </td>
  </tr>
</tbody>
</table>


But what if we want the links in the founder blockquote in the intro section to be bold?  Again, a descendant selector will work.  We add this:

```css
#intro blockquote a { font-weight: bold; } 
```

Any `<a>` tags anywhere inside a `<blockquote>` anywhere inside the #intro section will now be bold.


#### Direct descendant selectors ( > )

Sometimes you don't want to apply a style to any _possible_ child, but to only to the direct children.  This can be done with the > symbol.  Use it between selectors to limit the application to the direct children of the parent. For example, this rule, if applied to the HTML of the previous selector, would cause the links in the intro section to be larger, but not the links in any nested quotes or blockquotes. :

```css
#intro > a { font-size: large; }
```


#### Everything selector (*)

The asterisk (*) can be used to match any tag. By itself, this is only marginally useful. But combined with other selectors into a descendant selector, it can be pretty useful.

```css
body > * { margin-left: 10px; } /* all the _direct_ children of the body receive the margin */
p * { text-decoration: underline; } 
/* the text of the paragraph will be normal, but any children anywhere inside it will be underlined */
```


### Cascading: inheritance and precedence

#### Inheritance

__Now that we've covered several ways of defining CSS selectors, we need to understand what happens when multiple selectors resolve to the same element, and how an element can get inherit rules from its parent.__

Remember when we said _"For now don't worry about the 'Cascading' part..."_ at the beginning of this module?  Well, that was then, this is now. From this moment on, you will need to worry about cascading.

Most CSS rules once applied to an element are also applied to all the children of that element, and to their children, and theirs ad infinitum. There are exceptions, notably the layout properties (margin, padding, position, width, etc.) and the decorative properties (border, background, etc.) __do not__ cascade. This cascading of a CSS property from parent to child is also called "inheritance".

Generally, inheritance is a good thing. Do you want the whole page to use your corporate approved Web-font?  `body { font-family: "Soulless", serif; }` is all you need.  There is no need to apply the same `font-family` property to each and every tag used within the page.  Thank you, Cascading!

However, sometimes inheritance can be a bad thing.  An element may suddenly display in a way that you weren't expecting and you can't find any relevant CSS rule for that element. In this case, one likely culprit is a CSS rule that has been inherited from a parent. Thanks, Cascading!

Inheritance can be explicitly leveraged. Many CSS properties accept the value of <span style="color: #ff6600;">inherit</span>, which means to inherit the value from the parent. By smartly leveraging <span style="color: #ff6600;">inherit</span>, you can reduce repetition in your CSS rules and make your project easier to maintain.

In the sample below, we see a paragraph with children and grand-children. A CSS rule is applied to the paragraph that sets the font-family to be monospace, and the padding is set to 40 pixels.  Note that in the result, the font-family is applied to all the children, while the padding is only applied to the paragraph itself, none of its children inherit the padding.

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr style="background-color: lightgray; text-align: left; line-height: 1.2rem;"><th width="33%">HTML</th><th width="33%">CSS</th><th width="33%">Result</th></tr>
  <tr>
    <td>
      <pre style="border: none;">&lt;p&gt;This paragraph has children &lt;span&gt;spans&lt;/span&gt; and &lt;span&gt;q&lt;/span&gt;, which, in turn, have their own child &lt;span&gt;spans&lt;/span&gt;.<br/><br/>&lt;q&gt;With this structure, we can see how some CSS &lt;span&gt;rules&lt;/span&gt; are<br/>&lt;span&gt;applied across a &lt;q&gt;variety&lt;/q&gt;&lt;/span&gt; of scopes.&lt;/q&gt;<br/>&lt;/p&gt;<br/></pre>
    </td>
    <td>
      <pre style="border: none;">p {<br/>  /* inherited by children of p */<br/>  font-family: monospace;  <br/><br/>  /* not inherited */<br/>  padding: 40px;<br/>}</pre>
    </td>
    <td>
      <p style="padding: 40px;">This paragraph has children <span>spans</span> and <span>q</span>, which, in turn, have their own child <span>spans</span>. <q>With this structure, we can see how some CSS <span>rules</span> are <span>applied across a <q>variety</q></span> of scopes.</q></p>
    </td>
  </tr>
  <tr style="background-color: lightgray; text-align: left; line-height: 1.2rem;"><th>Discussion</th><th>CSS</th><th>Result</th></tr>
  <tr>
    <td>
      <p>To the right we add another CSS rule, this one instructing that the padding for spans and q elements should be inherited from their parent.</p>
      <p>Look at the result on the right, the padding is very evident.&nbsp;</p>
    </td>
    <td>
      <pre style="border: none;">span, q {<br/>  padding: inherit; <br/> }<br/></pre>
    </td>
    <td>
      <p class="p-appall">This paragraph has children <span>spans</span> and <span>q</span>, which, in turn, have their own child <span>spans</span>. <q>With this structure, we can see how some CSS <span>rules</span> are <span>applied across a <q>variety</q></span> of scopes.</q></p>
    </td>
  </tr>
</tbody>
</table>

This paragraph has children spans and q, which, in turn, have their own child spans. With this structure, we can see how some CSS rules are applied across a variety of scopes.

##### Which rules are inheritable?

There is no reliable rule for which CSS properties are inheritable by default and which are not. However, generally, the properties associated with positioning and layout are not inherited.  Likewise, the decorative properties (borders, background images, etc.) do not inherit.  Most properties that begin with `text-` or `font-` inherit.


#### Precedence

It is possible, and easy, to have several different CSS rules all applying to the same element.  This is often advantageous because most CSS properties are orthogonal to one another, meaning they do not interfere with each other. This gives us freedom to organize the CSS properties in rules in ways that make sense to us as developers, knowing that they can compose nicely. For example, a bit of text can be made italic by one rule, bold by another, and underlined by a third. We do not have to put all those properties into one place if that is not convenient for us.

However, what happens when there are different rules competing to set different values for the same property?  This is where CSS precedence comes into play. When rendering CSS, the browser has some guidelines it follows for resolving conflicting rules. Here is rough summary, in order:

__1 - Most specific rule__

A more _specific_ rule takes precedence over a less specific rule.  A rule that more tightly matches a particular element than a general rule will be applied. 

```css
span { color: blue; }
ul li span { color: red; }
```

In the example above, both rules are attempting to set a span color for a span inside a list item. However, the second rule will "win" when there is a conflict (like color in this case).

__2 - #id selector is the most specific__

Rules with an id selector (e.g. <code>#someid</code>) are considered more specific than rules without.

__3- .class selector is more specific than a tag selector__

Rules employing a class selector (e.g. <code>.someclass</code>) are considered more specific than rules without (but not as specific as an #id selector, which trumps everything).

__4- Rules that come later override those that come earlier__

This guideline is for two CSS rulesets with the same selector.  Where there are conflicts, the rules from the later one apply.  

```css
.hortense { color: red; text-decoration: underline; }
.hortense { color: blue; }
```

In the example above, an element with the <code>.hortense</code> class will be underlined and its color will be __blue__, because that rule came later than when it was set red.


##### No fear

These guidelines seem fairly straightforward, but situations can quickly get rather knotty.  For example, what color should we expect in this situation?

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr style="background-color: lightgray; text-align: left; line-height: 1.2rem;"><th>HTML</th><th>CSS</th></tr>
  <tr>
    <td>&lt;p class="forest"&gt;&lt;span class="tree"&gt;arbol&lt;/span&gt;&lt;/p&gt;</td>
    <td>
      <pre style="border: none;">  p.forest span       { color: green; }<br/>  p        span.tree  { color: blue;  }<br/></pre>
    </td>
  </tr>
</tbody>
</table>

What if the order of the CSS rules were reversed? Would it make a difference?

If this problem seems difficult to figure out, don't worry about it. In the next section, we will be looking at Chrome Developer Tools. You'll see how you can use the tools in the browser itself to inspect your elements and see exactly what CSS rules and properties are being inherited, applied and what is their precedence.  


#### !important

```css
p { color: orange !important; }
```

Because multiple CSS selectors can resolve to the same element, and because the rules that govern precedence are complex, you may from time to time encounter a situation where you need to apply a particular CSS property and you want it to take precedence over all others, no matter what.    !important will do that.  

The exclamation point is required, and the whole symbol ( `!important` ) goes after the value and before the semi-colon ( ; ).  

This may seem like an attractive option, but using it is not recommended. Once you start to use it, then you'll eventually run into a conflict with the various rules that are using `!important`, and from that conflict there is no escape.  If you are having problems with precedence the best advice is to fix them directly, rather than using `!important`.



### Knowledge checks


Here are some questions for a self check to make sure you understand everything. These questions are not graded.

1. My CSS declaration

  The list items (li) in a unordered list (ul) each have bullet points next to them by default. What is the CSS declaration you would use to remove them?
  
  Ans: `list-style-type:none` or `list-style-type:none;` or `list-style-type: none` or `list-style-type: none;`


2. List-style-position values

  Which of the following are acceptable values for the list-style-position property?

  1. within
  2. inside
  3. near
  4. outside
  5. baseline

  Ans: 24


3. id selection

  Given the HTML below, how would you select it by id?

  ```html
  <p id="dorothea">Perhaps we don't always discriminate between sense and nonsense.</p>
  ```

  Ans: `#dorothea`


4. class selection

  Given the HTML below, how would you select it by class?

  ```html
  <p id="dorothea" class="brooks" >Perhaps we don't always discriminate between sense and nonsense.</p> 
  ```

  Ans: `.brooks`<br/>
  While you have constructed a class selector using dot (.), that does not match any class held by the node in question. You have mixed the class selector dot with the id, which will not work


We'll use this block of HTML for the next few questions.

```html
<ul id="forest">
    <li class="evergreen"><a>pine</a></li>
    <li class="evergreen"><a>lodgepole</a></li>
    <li class="evergreen fruit"><a>holly</a></li>
    <li class="leaf fruit"><a>apple</a></li>
    <li class="leaf"><a>oak</a></li>
    <li class="leaf"><a>maple</a></li>
</ul>
```

5. What selector would you use...

  There may be other lists on the page, in addition to the one above. Given that, what selector would you use to select all the list items in the forest's unordered list?

  Ans: `#forest li` <br/>
  Hints: Just provide the selector itself; Try constructing a __descendent selector__ <br/>
  `#forest`: This selects the forest `ul`, but we want to select the `li` elements below it. <br/>
  `li`: `li` would certainly select every list item under the forest unordered list, but it would also select every other list item on the page. <br/>
  `ul`: This might select other unordered lists on the page. Additionally, it does not exactly select the list items (li) themselves.


6. Selecting the apple tree

  Assume that the evergreen, fruit and leaf classes are not used elsewhere on the page. What selector will select the apple tree, but none of the others?
  
  Ans: `li.leaf.fruit` <br/>
  Hint: No need to qualify by id; Try constructing a __specialized selector__; Make a specialized selector with two class names


7. CSS selector and hyperlinks

  ```html
  <p>The proud-mooded <a href="#wederchief">Wederchief</a> replied to his question,
  <q>Hardy 'neath helmet: <q><a href="#higelac">Higelac's</a> mates are we;
  <a href="beowulf">Beowulf</a> hight I. To the bairn of Healfdene,
  The famous folk-leader, I freely will tell
  To thy prince my commission, if pleasantly hearing
  He’ll grant we may greet him so gracious to all men
  </q>
  </p>
  ```

  In the HTML above, there are hyperlink tags both in a paragraph and within a nested quote. What CSS selector will select any hyperlink at the top of the paragraph, but not hyperlinks in the quotation?

  Ans: `p > a` <br/>
  Hint: We want to select the hyperlink with "Wederchief" but not the hyperlinks for "Higelac" or "Beowulf"; Try constructing a __direct descendent selector__; Use the caret (>) to make a direct descendent selector


8. Color of the rainbow

  Examine this HTML and CSS:

  ```html
  <p id="physics" class="rainbow">Rainbows result from refraction of sunlight in  falling 
  water droplets plus reflection of the light from the back of the droplet.</p>
  ```

  ```css
  #physics { color: red; }
  .rainbow { color: green; }
  ```

  With which color will the paragraph appear?

  1. black (no change)
  2. blue
  3. red
  4. green

  Ans: 3 <br/>
  the id selector (using #) takes precedence over other selectors, regardless of order


9. With which color will the paragraph appear?

  Examine this HTML and CSS:

  ```html
  <p id="physics" class="rainbow">Rainbows result from refraction of sunlight in falling water 
    droplets plus reflection of the light from the back of the droplet.</p>
  ```

  ```css
  p { color: blue; }
  html, body { color: black; }
  ```

  With which color will the paragraph appear?

  1. black
  2. blue
  3. red
  4. green

  Ans: 2 <br/>
  in this case the tag selector for the paragraph is more specific than the inheritable selector


### Activity - Lists

The HTML that follows is for a simple list.  Insert it into a properly formed HTML file and format it.  Try to ensure the following are done:

+ space the list items at least 20 pixels from the left edge of the page
+ space the list items at least 10 pixels from each other
+ center the header
+ keep the list at least 50 pixels from the header
+ the book titles in the list should not be displayed in a serif font
+ the header should use a different font than the list
+ the text of header should be dark red
+ break the CSS rules into two different .css files. One file should contain any spacing rules, the other any rules governing font faces or coloring.  Bind both into your HTML document
+ instead of numbers, have the list items indexed by the alphabet
+ change the `<ol>` tag to `<ul>` (and the closing `</ol>` to `</ul>`) and style the list items to have square bullet points
+ download this [simple triangle shape](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/073e0b55b08d259174c48c569c6696d9/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/my_triangle.png) <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/073e0b55b08d259174c48c569c6696d9/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/my_triangle.png" alt="Simple triangle shape" height=10> and style the list items to use it

Please work on the following CodePen and implement the instructions above - do not hesitate to tweak and test!

[Sample code](src/3.4.6-Lists.html)

[Sample Spacing code](src/3.4.6-spacing.css)

[Sample color code](src/3.4.6-color.css)



### Activity - CSS selectors

Using the HTML below (in this [CodePen](https://codepen.io/w3devcampus/pen/JNpJpX)), please style the two lists by following these instructions:

+ The female characters are in blue text, and the male characters are red
+ Dorothea Brooke and Sydney Carton are bold text
+ Joshua Rigg and Madame Defarge are italicized
+ The list for Middlemarch is enumerated with roman numerals
+ The list for A Tale of Two Cities is enumerated with alpha characters
+ The list items for Middlemarch are spaced out more
+ The list for Middlemarch has been moved rightward
+ Serif font is not used anywhere on the page

Can you achieve the same styling without adding any new tags (i.e., without adding `<i>` or `<b>` or `<span>`) ? Feel free to modify the HTML, but try not to add any new `id` attributes, if possible.

[Sample code](src/3.4.7-selector.html)


### Recipe project - Module3

We're going to make our Recipe Web page look a lot better using the CSS that you've been learning.  See what you can do with backgrounds, margins and size settings to get your Web page looking more like [this](src/3.4.8-ProjectSample.html)

If you'd like to see what we did for Module 2, you can find it [here](src/2.5.7-Recipe.html).

[Example code](src/3.4.8-Recipe.html)


<video src="https://edx-video.net/W3CHTM502016-V008900_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@ca1d1804e4a04db9bc74aad1f79a6fc8/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


## 3.5 Exercises - Module 3

### CSS rules (1-7)


Source code for the following question (1):

```html
<!DOCTYPE html>
<html>
  <head>
    <css>
       .swann-way { font-size: 2pm; }
       h { font-base: monospace; }
       h3.h { font-size: larger; }
       #subtitle { color: blue; }
    </css>
  </head>
  <body>
    <h1 id="swann-way" class="h">Swann's Way</h1>
    <h2 id="subtitle" class="h">Remembrance of Things Past, Volume One</h2>
    <author>By Marcel Proust</author>
    <h3 class="h">Overture</h3>
    <p>For a long time I used to go to bed early. Sometimes, when I had put out my
    candle, my eyes would close so quickly that I had not even time to say <q>I'm 
    going to sleep.</q></p>
   </body>
</html>
```

1. Error identification

  Examine the HTML and CSS above. It has several problems.

  The CSS rules in the code above are not correctly displaying. Please identify all the errors: (select all that apply - 5 correct answers!)

  1. The CSS selector `#subtitle` is incorrect. It should be `.subtitle`
  2. `<css>` is not a valid tag
  3. The CSS selector `.swann-way` is incorrect. It should be `#swann-way`
  4. No element has the class of subtitle. This prevents one of the CSS rules from working
  5. The CSS selector `h` is incorrect. It should be `.h`
  6. `pm` is not a valid unit
  7. `h3.h` is reversed, it should be `h.h3`.
  8. font-base is not a valid CSS property
  9. larger is not an acceptable value for font-size

  Note that this question is worth 5 points!

  Ans: 23568, x23468


2. External parent

  What tag will let you bind an external .css file to a parent .html file?

  Ans: `link` or `<link>` <br/>
  Explanation: `<link>` is the tag that will let you include an external style sheet.

  ```html
  <link href="my_stylesheet.css" rel="stylesheet">
  ```

3. CSS in HTML

  What tag will let you place CSS code directly into an HTML file?

  Ans: style or `<style>`<br/>
  Explanation: `<style>` or `style` <br/>
  The `<style>` tag will let you put CSS directly into an HTML document.

  ```html
  <style>
      p { color: blue; }
  </style>
  ```

4. Cramped lines

  You have a long paragraph of text. You have already adjusted the font-size and are happy with it. But the lines of text in the paragraph are simply too cramped and you want to space them out more.

  What CSS property should you use to make the text less cramped?

  Ans: line-height <br/>
  Explanation: While the `font-size` property will make the text larger, the line-height property is the one that makes the area given to each line of text larger or smaller, without changing the actual size of the individual characters themselves.


5. More space, please

  Your `<article>` contains several paragraphs of text (`<p>`). You want more space between the individual paragraphs.

  What CSS property should you use to put more space between the paragraphs?

  Ans: margin or margin-top or margin-bottom or margin: or margin-top: or margin-bottom <br/>
  margin or margin-top or margin-bottom or margin: or margin-top: or margin-bottom <br/>
  Explanation: Your "go to" property when needing to adjust positioning should always be margin. In this situation, simply adjusting the top or bottom margins ( margin-top margin-bottom) would suffice.


6. Valid CSS units

  Which of the following are valid CSS units? (select all that apply - 6 correct answers!)

  1. `vh`
  2. `px`
  3. `pix`
  4. `perc`
  5. `em`
  6. `rem`
  7. `sem`
  8. `%`
  9. `vw`

  Ans: 125689


Source code for the following question (7):

```html
<ul>
  <li>birds
    <ul>
      <li>flying
        <ul>
          <li>hawk</li>
          <li>sparrow</li>
        </ul>
      </li>
      <li>flightless
        <ul>
          <li>penguin</li>
          <li>ostrich</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>bugs
    [ ... MORE BUGS ... ]
  </li>
</ul>
```

7. Which is the cause of this problem?

  Your page contains a nested list, an excerpt of which is above.

  However, there is a problem. Each more deeply nested item is smaller than the parent. The most deeply nested items (like hawks, sparrows, penguins and ostrich) are so small as to be unreadable.

  Which is the most likely cause of this problem?

  1. `li { font-size: .5em; }`
  2. `ul > li { font-size: 14px; }`
  3. `li { font-size: .5rem; }`
  4. `ul li { font-size: 14px; }`
  5. `li { margin-top: 10%; }`

  Ans: 1 <br/>
  Explanation: The em unit is used to size text relative to the parent text. So in the case of nested lists, if the list items have font-size: .5em; then the outermost list items are half the font size of the main page. <br/>
  But the second level in are half the size of that, because they are half the size of their parent (which are already half sized). So that second level is a quarter size. <br/>
  And the third nested level is half again, so only 12% of the original page font size. <br/>
  And so on.


### CSS selectors (8-11)

Source code for the next four questions:

```html
<body>
  <h1>Birds and Not Birds</h1>
  <h2>A compendium of flying and not flying things</h2>
  <p>While walking through the woods with my daughter she asked me <q>Papa, what kind of bird is that?</q> and was pointing to an <a href="#ok">oesterkirche</a>. (A huge one!)</p>
  <p>I told her its name and explained that while an oesterkirche flies like a bird and eats bugs and worms (<sup><a href="#footnote">*</a></sup>) like a bird, it is not, in fact, a bird. This lead us to a discussion of other flying things that might or might not be birds, and birds that don't fly. Here is our list:</p>
   <ul>
     <li class="bird">penguin</li>
     <li class="bird flying">hawk</li>
     <li class="flying">oesterkirche</li>
     <li class="insect flying">butterfly</li>
     <li class="bird">ostrich</li>
     <li class="insect flying">wasp</li>
     <li class="bird flying">sparrow</li>
     <li class="insect">ant</li>
    </ul>
  
  <hr>
  <p id="footnote">(*) - Does anyone know exactly what oesterkirche eat? Don't they also eat fish?</p>
  <img id="ok" src="oesterkirche.jpg" alt="scary oesterkirche, don't get close!">
</body>
```

8. CSS selectors

  Which of the following assertions are true about the code above? (select all that apply - 2 correct answers!)

  1. `li { color: red; }` will make all the list items red
  2. `p > * { font-weight:bold; }` will make the three paragraphs, the quotation and the list bold faced
  3. `.insect.flying {list-style-type: square; }` would put a square marker to the left of the _wasp_ and _butterfly_ list items
  4. `.insect { font-style:italic; }` would italicize the ant list item and no others
  5. `p > a {color: orange; }` would make both links orange

  Ans: ac <br/>
  Explanation: The first rule will turn all `<li>` red. The second rule will only turn the HTML elements included in a paragraph: the element between `<q>` and `</q>` and the two links. The third rule will affect only list items with class "insect" and "flying" together: the wasp and butterfly items. The fourth rule will italicize all items with the "insect" class: three of them, not only the ant list item. The last rule will only turn orange the link that is directly in a paragraph: the first one, not the second one. Here is a [JsBin with the running code](http://jsbin.com/laleram/edit?html,css,output).


9. Headings

  Pretend you have a rule that needs to be applied to both headings. What selector would you use?

  Ans: `h1,h2` or `h2,h1` or `h1, h2` or `h2, h1`; x class; x comma separate selector <br/>
  Explanation: Use a comma (,) to apply the same rule set to a variety of selectors.

  ```css
  h1, h2 {
      color: blue;
  }
  ```


10. List items

  If you need to apply a rule to the hawk and the sparrow list items, what selector would you write?

  Ans: `.bird.flying` or `.flying.bird` or `li.bird.flying` or `li.flying.bird`
  Explanation: If you examine the code you'll see that the entries for hawk and sparrow both have the flying class as well as the bird class, and they are the only two that have both classes. So the solution is to make a selector that selects for both: `.flying.bird`

  ```css
  .flying.bird {
      color: red;
  }
  ```


11. Links

  There is a rule that must be applied to the link to the #footnote, and not the other link. Please provide a selector:

  Ans: `sup a` or `sup>a` or `sup` or `sup > a` or `sup> a` or `sup >a` or `p sup a` or `p sup>a` or `p sup > a` or `p > sup a` or `p > sup>a` or `p > sup > a` or `p>sup a` or `p>sup>a` or `p>sup > a` <br/>
  Explanation: If you examine the two links (`<a>`) in the code above, you'll notice that one of them is in the paragraph (`<p>`) while the one that links to the #footnote is nested in a `<sup>` block. <br/>
  So, a descendent selector can be used to uniquely select the `<a>` inside the `<sup>: sup a` or perhaps: `sup > a`

  ```css
   sup a { 
    color: green;
  }
  ```


### CSS properties (12-15)


12. Underline with CSS

  Which CSS property will let you apply an underline to the text of an element?

  Ans: `text-decoration` <br/>
  Explanation: The `text-decoration` property will let you apply an underline to an element.


13. Underline property values

  The property that applies an underline accepts which of the values below  (select all that apply - 3 correct answers!)

  1. underline
  2. italic
  3. overline
  4. line-through
  5. bold
  6. red

  Ans: 134 <br/>
  Explanation: The property that can apply an underline is text-decoration and three of its possible values appear above: `underline`, `overline`, and `line-through`


14. Which color?

  Examine the HTML and accompanying CSS below.

  ```html
  <p id="opening-paragraph" class="dorothea">Miss Brooke had that kind of beauty 
  which seems to be thrown into relief by poor dress.</p>
  ```

  ```css
  #opening-paragraph { color: blue; }
  .dorothea { color: red; }
  ```

  With which color will the paragraph appear on the page?

  1. green
  2. blue
  3. red
  4. black (the default)

  Ans: 2 <br/>
  Explanation: An id selector (#opening-paragraph) takes precedence over a class selector (.dorothea).


15. For which is CSS an acronym?

  For which is CSS an acronym?

  1. Canvas Styling System
  2. Cascading Style Sheets
  3. Control and Show Symbolic language
  4. Color Size Selectors

  Ans: 2




