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




### CSS rules




## 3.3 CSS properties

### Common CSS properties




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

