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

The W3C CSS Working Group

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

Style tag in the XDK code editor

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

In the above, the selector is __p__.  When a selector appears unprefixed by any punctuation, then it is assumed to match to an HTML tag.  Thus, the __p__ selector will apply the CSS rule to all `<p>` tags in the document. 

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

<table  table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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




### Units




### Accessible typography




### Knowledge checks




### Activity - Units




## 3.4 Lists and selectors

### Styling lists




### Selectors




### Combining selectors




### Cascading: inheritance and precedence




### Knowledge checks




### Activity - Lists




### Activity - CSS selectors




### Recipe project - Module3




## 3.5 Exercises - Module 3

### CSS rules (1-7)




### CSS selectors (8-11)




### CSS properties (12-15)

