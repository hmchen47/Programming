# Module 6: Basics of page layout


## 6.1 Introduction to Module 6


### Welcome to Module 6

<video src="https://edx-video.net/W3CHTM502016-V014900_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@458b8e52b262434bb94d0dd1823a0972/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Module 6 - Content

6.1 __Introduction__: Understanding what "layout" means to your Web programming.

6.2 __Concepts__: Get an understanding of "display" versus "position" & "block" versus "inline". 
Note: Positioning and z-index are OPTIONAL material.

6.3 __Flexbox__: There is more to understand about positioning and sizing.
Note: Calc is OPTIONAL.

6.4 __More flexbox__: Main axis & cross axis, justification, alignment and order — more flexbox concepts.
Note: This ENTIRE section is OPTIONAL.

6.5 __Recipe project__: Let's get "responsive" — how to make your Web page look good on differently sized devices.

6.6 __Where to from here?__: Considering what you now know — what do you want to learn next?


### History of layout

Before we get started working on the topic of layout directly, it is useful to understand a bit of HTML and CSS history.  

In the not-so-distant-past, most HTML documents were long-form prose interspersed with lists and sometimes tables of information. HTML was used to present technical documentation, corporate communication, instructions and manuals, lists of files, and occasionally emails or notices. The "layout" needs were minimal to non-existent.

Over time, however, users began to prettify their documents by adjusting font sizes and font faces. And this was primarily done in HTML itself, which caused problems. Thus the first impetus for CSS was to separate any style information from the HTML document itself. However, the use cases those times were all still primarily text-based.  The goals of CSS were modeled after the "master sheets" of some word processors. 

Before the first specification for CSS had been agreed upon, Web developers began a transition to creating different types of documents. These documents were more like fancy magazine pages - images, not text, were the centerpiece. Decorative graphics abounded, advertisements showed up. And even as CSS2 and later CSS3 were being written, Web development changed again - Web pages became more interactive, the term "Web application" was coined. Many Web sites bore far more similarity to the control panel of a microwave than to a magazine article, much less the page of a book.  And finally along came smart phones and a whole new "mobile Web" focus for Web sites, Web pages, and Web applications. 

During its short lifetime, CSS has often played "catch up" especially with respect to layout.  Here is a short list of techniques and CSS properties used historically for layout:

+ tables and "slicing"
+ absolute positioning
+ floats and clear
+ css columns
+ css tables
+ flexbox

Except for some basic required concepts, we are going to skip all of this and go straight to flexbox. After many stumbles, flexbox finally brings sanity to the much needed world of layout in CSS.


## 6.2 Concepts


### Text baseline and the display property

#### Why won't this work?

When newbie developers are groping around CSS blindly, they often stumble upon a variety of CSS properties that could be used to alter the positioning or size of an element such as `left`, `top`, and `margin`. However, when using the properties, these developers get confused because the properties fail to behave consistently. Sometimes the properties work, sometimes they don't, sometimes they do the _opposite_ of what they are doing in a different rule.  We have not covered properties like `left` and `top` yet, but we have introduced `margin` and the intrepid readers may have already discovered in their exercises that `margin` can have some unexpected behavior. Why is that?

The answer has to do with the two CSS properties: `display` and `position`. The `display` property, in particular, has different default values for different tags. Some tags start with `display:block`, and others are `display:inline`. They behave very differently.  These two properties (`display` and `position`) often change how an element responds to certain other layout properties.  And when this is not understood, then it may seem random to a developer struggling to get stuff to work.

So, let's start with understanding a very important difference between block and inline display. And that begins with the baseline.


#### Baseline

The text "baseline" is a key concept to understanding how the browser makes its layout decisions.  

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/306cfa0313a449a29b2dbcb0b2afcb86/1fe35eaba7534b5d86b69fa0e09494a3/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%4065eedf84e09a4619a4152d1cdcadc73a" ismap target="_blank">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/03a5c30240869b1400f96ca51fc2eb19/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/baseline2.png" style="margin: 0.1em;" alt="baseline" title="baseline" width=100>
  </a>
</div>

In the image above, we see two text characters placed next to each other, the blue line indicating the baseline. The baseline determines how and where the characters are positioned. Note that the tail of the "g" hangs below the baseline.  

The baseline is never drawn by the browser, it is not exposed directly to you as a developer, and CSS only may have some properties related to it. However, the baseline governs the placement of all inline elements.


#### display: block versus inline

As the browser is rendering your page, every time it encounters the next tag it has a simple question: "Do I give this element its own line?"   For example, every <p> tag gets a new line, but `<a>` tags do not.

This is the key distinction between the "block" level elements (like the `<p>` tag) and the "inline" elements (like the `<a>` tag).   Here is a quick table of the default values for some of the tags we've already learned.


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=50%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Block</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Inline</th></tr>
  <tr>
  <td>
  <ul><li>p</li><li>h1</li><li>div</li><li>blockquote</li><li>ul</li><li>ol</li><li>li</li></ul>
  </td>
  <td>
    <ul><li>a</li><li>span</li><li>q</li><li>i</li><li>b</li></ul>
  </td>
  </tr>
</tbody>
</table>

Here are some differences between the block - level and inline elements.


##### Block Level

The block level:

+ appears below and to the left of their block level neighbors (like a carriage return on a typewriter going to the next new line)
+ __will expand to fill the width of the parent container by default__
+ respects all margin properties
+ can have its width property set, which will make it narrower and cause its children to wrap, but not crop. (We'll cover this later)
+ takes on the height of all its children (pending certain exceptions) as long as its own height is unset. (We will cover setting the height later)
+ ignores the vertical-align property


##### Inline Elements

Inline elements:

+ simply appear to the right of their preceding inline neighbor. They do not drop to the next line unless they must "wrap".
+ __by default, the width is simply the width of the content of the element, plus any padding__
+ __ignore top and bottom margin settings__
+ __ignore `width` and `height` properties__
+ are subject to `vertical-align` property as well as CSS `white-space` settings
+ support `padding`, but any `padding-top` or `padding-bottom` does __not__ contribute to the calculation of the height of the text line it sits upon
+ cleave to the baseline where they are being placed

The last bullet about inline elements is one of the most important to understand. Inline elements cleave to _the baseline_.  This is very important to understand why inline elements are positioned vertically the way they are. It also contributes to why they ignore top and bottom margins. Note that making an inline element "bigger" with padding will certainly keep its neighbors away horizontally. But if there is a neighboring text line above or below, it can only be kept at bay with the `line-height` property, not margins or padding.

Below we see a span that has padding, margin-top, and background-color applied, but no extra room is being made for it above or below, so its background is overlapping the lines above and below.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=60%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;"> span</span> {
  <span style="color: #333399;">margin-top</span>: <span style="color: #339966;">15px</span>; <span style="color: #808080;">/* ignored */</span>
  <span style="color: #333399;">padding</span>:<span style="color: #339966;">15px</span>;
  <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">lightblue</span>; 
  }
</pre>
    </td>
    <td style="width: 300px; font-size: 14px; line-height: 22px;">
      <p>Nothing could hinder it but her love of extremes, and her insistence on regulating life <span style="margin-top: 15px; padding: 15px; background-color: lightblue;">according</span> to notions which might cause a wary man to hesitate before he made her an offer, or even might lead her at last to refuse all offers.</p>
    </td>
  </tr>
</tbody>
</table>


So here we prevent the overlap by setting the line-height of the span. However, this solution should not be considered optimal.  Better is to change the span to be display:inline-block, which is discussed below.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=60%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;"> span</span> {
  <span style="color: #333399;">margin-top</span>: <span style="color: #339966;">15px</span>; <span style="color: #808080;">/* still ignored */</span>
  <span style="color: #333399;">padding</span>:<span style="color: #339966;">15px</span>;
  <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">lightblue</span>; 
  <span style="color: #333399;">line-height</span>: <span style="color: #339966;">42px</span>; <span style="color: #808080;">/* fix */</span>
  }
</pre>
    </td>
    <td>
      <p>Nothing could hinder it but her love of extremes, and her insistence on regulating life <span style="margin-top: 15px; line-height: 42px; padding: 15px; background-color: lightblue;">according</span> to notions which might cause a wary man to hesitate before he made her an offer, or even might lead her at last to refuse all offers.</p>
    </td>
  </tr>
</tbody>
</table>


##### inline-block

The astute reader may have spotted an obvious omission from the table of block and inline elements above: `<img>`. Is `<img>` a block level element or inline?  If you venture to experiment you may conclude "both", and you will be right.

For historic reasons, the `<img>` tag defaults to `display:inline` in most browsers. If you inspect using the browsers inspector, that's what you will see. However, it does not follow the same rules as other inline elements. In fact, regardless of what the inspector says, images are special cased and are inline-block.

Inline-block elements still cleave to the text baseline of the line they are on. If top or bottom margins or paddings are used, then the entire line is adjusted to make room. (So the line-height does not need to be used.)

+ `inline-block` elements respect `margin-top` and `margin-bottom`
+ the vertical padding for inline-block elements contributes to the calculation of the height of the line it falls on
+ inline-block elements respect `width` and `height` properties

In some browsers, some of the form elements default to inline-block (like `<button>`, `<select>`, and `<input>`)

Here is the overlapping background style presented again, but this time instead of using `line-height` to solve the problem, we simply make the span element `display:inline-block`.  Note that the margin-top is also respected.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=60%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;"> span</span> {
  <span style="color: #333399;">margin-top</span>: <span style="color: #339966;">15px</span>; <span style="color: #808080;">/* no longer ignored */</span>
  <span style="color: #333399;">padding</span>:<span style="color: #339966;">15px</span>;
  <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">lightblue</span>; 
  <span style="color: #333399;">display</span>:<span style="color: #ff6600;">inline-block</span>; <span style="color: #808080;">/* fix */</span>
  }
</pre>
    </td>
    <td class="inline-block-result">
      <p>Nothing could hinder it but her love of extremes, and her insistence on regulating life <span style="margin-top: 15px; display: inline-block; padding: 15px; background-color: lightblue;">according</span> to notions which might cause a wary man to hesitate before he made her an offer, or even might lead her at last to refuse all offers.</p>
    </td>
  </tr>
</tbody>
</table>


#### display property

At long last we arrive at the `display` property. We have now seen three of its possible values: `block`, `inline`, and `inline-block`.  There are others (like `none` and `flex`) and we will cover them later.  

```css
.name { display: inline-block; }
```

A key to not getting confounded by the display property is to have a grasp on which elements default to which display value and appreciating the differences between block, inline, and inline-block display.


### Horizontal centering




### Key concept: position property




### Knowledge checks




### Positioning




### 'z-index'




### Activity - Block vs. inline




### Activity - Cornerpiece




## 6.3 CSS Flexbox


### Sizing and dimensions




### Flexbox




### Flexbox advice and best practices




### Knowledge checks 




### Activity - Basic flexbox




### Basic flexbox




### Activity - Holy grail with flexbox




### Activity - Flex columns




## 6.4 More flexbox


### Main and cross axes




### Justification and alignment




### Order




## 6.5 New layout technique: CSS Grid


### CSS Grid




### New layout techniques




## 6.6 Recipe project


### Recipe project - Module 6




## 6.7 Where to from here?


### Where to from here?




### WAI resources




### Internationalization and CSS: use cases




### Internationalization resources





