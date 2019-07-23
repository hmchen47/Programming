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


### Horizontal and vertical centering

#### Horizontal centering

Now that we've covered inline versus block display, we can intelligently discuss centering. Let's start with inline elements.


##### inline

How do you center an inline element?  As we recall, inline elements are positioned along the baseline, in the natural flow of the text or content. So for any individual inline element, there is _no CSS property_ you can apply directly to cause this element to center. You may apply some padding evenly or unevenly to position its content relative to its own box. But that's not centering the element itself.

To center an inline element, we use the `text-align` property of its parent.

```css
p { text-align: center; } /* the text and any inline children of this element will be centered */
```

If this isn't satisfactory, consider changing the element to be inline-block or block.


##### block

How do you center a block level element? First, you may recall that block level elements take the width of their parent by default. If the element is the same width as its parent, it is already centered.  So the first step is to limit the width of the element.  Setting the width property directly is not generally a good practice, but we'll just do that and discuss sizing at length later.

```css
div { width: 200px; }
```

Now that we've sized the element, how to center it?


##### margin magic

If set to auto, then the left and right margins will center the element.  This is the simplest and best way of centering a block level element.  So the full solution is to set the width and apply auto to the left and right margins (or to all margins).

```css
div { width: 200px; margin: auto; }
```

Horizontal centering - a better way
Do auto margins seem spooky to you?  There is a better way to achieve centering and its name is flexbox.  We'll read more about it later.


#### Vertical centering

##### inline

Inline elements respect the vertical-align property. This determines how the inline element is aligned relative to the baseline it is being laid upon. This may or may not solve your vertical centering conundrum.


##### block

There is no `margin:auto` approach to vertical centering. There are some complicated systems that folk have developed, but the shortest and best answer to vertical centering: use flexbox.



### Key concept: position property

#### The 'left', 'top', 'right', and 'bottom' properties

In CSS, there are four properties which can be used to adjust or set the position of an element. Those properties are: `left`, `top`, `right`, and `bottom`.

However, in one of the best jokes played by the authors of the CSS specification, using those properties by themselves will have _no effect_ on any element. Surprisingly, most developers struggling with CSS don't find this funny.

The reason these properties don't work by default is that they only work when applied to positioned elements. And positioned elements are those that have had their `position` property changed from the default.


#### The 'position' property

The CSS `position` property governs how an element is positioned on the page and how it responds to the position adjusting properties (`left`, `top`, `right`, and `bottom`).  Up to this point in this course, we have not used this property and so everything we've seen has been the default position, which is `position:static` for all elements.

As of today, the position property has four different values it can take: `static`, `relative`, `absolute`, and `fixed`. We will look at `static` and `fixed`.   The options `relative` and `absolute` are more complex, they'll be discussed in an optional advanced section for completeness, but we aren't going to worry much about them because flexbox reduces their use cases.


#### Static

```css
position: static; /* the default */
```

A position property of static is the default for all elements. It simply means that all elements follow the "flowing text"model of layout and the only properties influencing their position are margins, padding, and the display property that selects block level layout, inline or inline-block. Static elements ignore the positioning properties we read about earlier (`left`, `top`, `right`, and `bottom`).


#### Fixed

```css
position: fixed;
```

A fixed positioned element respects the positioning properties (`left`, `top`, `right`, and `bottom`).  A fixed positioned element is positioned against the _window_ rectangle (aka the viewport).  This means that fixed position elements will not scroll with the rest of the page.  Fixed position elements can easily "stick" to the side or bottom or top of the browser. To observe this better, see the Fixed position activity in the next section.

+ Fixed position elements are positioned against the viewport.
+ Best practice: use both a horizontal and a vertical positioning property on every fixed positioned element.
+ Fixed positioned elements do not contribute to size of the parent.
+ Fixed positioned block level elements do not get the width of their parent
+ Margins do not work the same.
+ Opposite properties can be used to size an element.


__Best practice: use both horizontal and vertical positioning property on every fixed element__

There is a very subtle extension to the previous interpretation problem: if an element is set to be `position:fixed`, but has no horizontal positioning property (that is, `left` or `right`), then it will be displayed in the flow exactly as it would have been.  Except, later, if `left:0px;` is added (for example), then the element may jump to the left edge of the browser window. The same applies vertically. This is a bewildering behavior, as most users do not expect there to be a difference between `left:0px` and no `left` property at all.

Therefore, for any fixed positioned element, the best practice is to ensure that one of the horizontal positioning properties (that is, `left` or `right`) and one of the vertical properties (top or bottom) are both set.


__Fixed positioned block level elements do not get the width of their parent__

Earlier we learned that the block level element automatically gets the width of its parent, that is, they extend to become full width. But this is only true for `static` and `relative` positioned elements. Elements that are `fixed` positioned (or `absolute`) do not exhibit this behavior. Their initial width is simply the width of their content. Though it can be changed.


##### Margins do not work the same

For `static` and `relative` positioned items, margins can be used to adjust an element position and keep neighboring siblings "away". That's our quick assumption about the margins. However, when an element is `fixed` positioned, a given margin might be able to move the element but will not move any siblings. Margins cannot be used to keep siblings "away", to fight crowding.

As a general rule, if a positioning property is being used (like `left`), then the matching margin (`margin-left`) can also be used to additionally adjust the position of the element. Otherwise, the margin will unlikely have any effect.


##### opposite properties can be used to size element

This is one of the nicer features. Working with preset dimension properties (`height` and `width`) can make your design brittle and reduce its adaptability. However, `fixed` positioned items can instead set the opposite positioning properties (like `left` and `right`) and leave the matching dimensional property (`width`) unspecified.  The element will grow or shrink based on the size of the browser window.  Note that this feature is only available to `fixed` (and `absolute`) elements.



### Knowledge checks


1. Inline display

  Which of the following tags default to inline display? (select all that apply - 5 correct answers!)

  1. p
  2. q
  3. blockquote
  4. span
  5. div
  6. h1
  7. a
  8. ul
  9. ol
  10. li
  11. i
  12. b
  
  Ans: 2 4 7 11 12


2. Inline element

  Which of the following statements are true about an inline element? (select all that apply -- 4 correct answers!)

  1. respect all margins.
  2. ignore top and bottom margins.
  3. respect width and height properties.
  4. are set along the text baseline next to their siblings.
  5. always receive a new line.
  6. padding makes the item larger.
  7. top and bottom padding do not contribute to any line-height calculations.

  Ans: 2467

  + inline elements support left and right margins, but not top and bottom
  + inline elements are sized by their content and padding, not by width and height properties
  + block level elements always receive a new line, not inline elements


3. Block lifting

  Which of the following statements are true about block level elements? (select all that apply -- 5 correct answers!)

  1. always receive a "new line" when placed.
  2. respects all margin properties.
  3. defaults to the full width of any parent.
  4. ignores the width property.
  5. ignores the height property.
  6. with absence of any height properties, is vertically sized to accomodate its children (though there are exceptions).
  7. ignores the vertical-align property.
  
  Ans: 12367

  + Block level elements respect the width property.
  + By default, block level elements are vertically sized to accommodate their children. The height property can override, and some children are exceptions.
  + Block level elements do not support the vertical-align property.
  + Absent any width property, a block level element will default to the full width of its parent.
  + Block level elements respect all margins (including top and bottom).
  + Block level elements always receive a new line when positioned.


4. My ways...

  Elements that are inline-block are inline elements that behave in some ways like block level elements. What ways are those? (select all that apply -- 3 correct answers!)

  1. get a "new line" when placed.
  2. respect all margin properties.
  3. default to full width of any parent.
  4. respect the width and height properties.
  5. top and bottom padding contributes to line-height calculation.
  
  Ans: 245

  + inline-block elements are set on the text baseline alongside any siblings, they do not receive a new line.
  + inline elements do not support top and bottom margins. But inline-block elements do support the top and bottom margins (as well as left and right).
  + inline-block elements are sized to their content, like inline elements. They do not take on the width of their parent.
  


5. Image behavior

  Which of the following best describes the default display behavior of the `<img>` element?

  1. inline-block
  2. inline
  3. block
  
  Ans: 1 <br/>
  If you look in the Element Inspector of your browser, it will most likely show you that an `<img>` element is display:inline. However, the element does not behave like an inline element. It supports height and width and all margins. `<img>` elements are inline-block elements.


6. Unset element

  What is the default position property that every element has if it is unset?

  1. static
  2. relative
  3. fixed
  4. absolute
  5. unanswered
  
  Ans: 1<br/>

  1. static position is the default that every element gets unless it has the position property explicitly set.
  2. Many designers wish that relative position were the default, but it is not. It must be specifically elected by explicitlyl setting the position property.
  3. fixed position must be specifically elected by setting the position property. It is not the default.
  4. absolute position must be specifically elected by setting the position property. It is not the default.



7. Static positioning

  Do the various positioning properties (like left, top, etc.) affect an item that is statically positioned?
  
  Ans: No <br/>
  static elements (the default) do not respect the positioning properties.


8. Viewport position

  If you want to position an element relative to the browser window (aka the viewport), what position value should you choose?

  1. static
  2. absolute
  3. fixed
  4. relative
  
  Ans: 3

  + Static elements are not considered positioned elements. They fall where they are supposed to (which depends upon whether they are display inline or block) and all positioning properties are ignored.
  + Fixed positioned elements have their positioning properties interpreted relative to the viewport, regardless of parents or how the document might have been scrolled.
  + This will position an element on its first positioned parent. Even if that parent were the top document, this might still not be the browser window / viewport, because the document can be scrolled.


9. Cornered

  Which of the following will result in its element being positioned in the lower right corner of the browser window?

  1. position:static; display:block; margin-left:90%; margin-right:0px; margin-top:90%; margin-bottom:0px;
  2. position:relative; bottom:0px; right:0px;
  3. position:fixed; bottom:0px; right:0px;
  4. position:absolute; top:90vh; left:90vw; width:10vh; height:10vw;
  
  Ans: 3 <br/>
  
  1. This might work if the parent element is the same size as the browser window and flush to the upper left corner. But even then the element will not be tied to the viewport.
  2. This would only work if the parent is the same size as the window and flush to the upper left corner, and even then the element is not tied to the viewport.
  3. A simple elegant solution. Works even if the item in question is inline.
  4. Nice job using the vh/vw units. However, while this might sometimes seem to position the element where you want, there are problems: the element is not truly tied to the viewport. The positioning is relative to the nearest positioned element ancestor. So this depends a lot on how the HTML is organized. Finally, the height and width properties will not work on inline elements.




### Absolute and relative position

#### Positioned elements

We read about the positioned elements in an earlier section. There are five positioning properties (`left`, `top`, `right`, `bottom`, and `z-index`) that can be used to influence the position of an element. But these properties, by default, will have no effect on any element.  This is because all elements are `position:static` by default, and static elements ignore those positioning properties.  Only positioned elements, which are elements where the position property is set to something besides static, respect the properties.

We saw `position:fixed`, which is fairly simple: the positioning properties cause the fixed elements to be positioned relative to the browser window; they don't even scroll with the content.  Besides `fixed` and `static`, the `position` property can also be set to `relative` and `absolute`. For these values, the positioning properties have different interpretations.   


#### relative

```css
position: relative;
```

The relative value is exactly like static in that the "flowing text" model of layout is setting the initial position for the element (including margins and display). However, unlike static, elements with relative position respect the positioning  properties (`left`, `top`, `right`, and `bottom`).  These properties will move the named edge of the element __from__ its initial position. So a value of `top: 20px;` will move the top edge of the element 20 pixels further down the page.  And similarly, a value of left: 20px; will move an element 20 pixels from its original left edge, which means move it 20 pixels to the right.

The `relative` position property has three primary gotchas of which you should be aware:

+ Items are moved independently of siblings.
+ Opposite positioning properties (like left and right) cannot be used simultaneously.
+ There are no automatic size adjustments.


##### Independence - margin-top vs top

IMPORTANT: The positioning properties (`left`, `top`, `right`, and `bottom`) adjust the placement of the element <strong><em>independently of its siblings</em></strong>.  What does this mean?   Let's imagine we have a list and we want to move one of the items a little further down the page. Should we use `margin-top` to move it? Or `position:relative` in conjunction with the top property?  The answer to this question depends on whether you want any of the other list items to move as well.  If you want the siblings to move down as well, then use `margin-top`.

Here is an example. Suppose we have two lists. We want the third item in the list to have a background color and to be moved down by 30 pixels. Compare what happens when we use  `margin-top` to move it, versus a positioning property (`top`). When we use `top`, the "Third" item appears overlapping the Fourth and Fifth items, as they did not move at all.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;" colspan="2">margin-top</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;" colspan="2">top</th></tr>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Result</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;">.third</span> {
  <span style="color: #333399;">margin-top</span>: <span style="color: #339966;">30px</span>;
  <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">lightblue</span>;
}</pre>
    </td>
    <td><ul><li>First</li><li>Second</li><li style="margin-top: 30px; background-color: lightblue;">Third</li><li>Fourth</li><li>Fifth</li></ul></td>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;">.third</span> {
  <span style="color: #333399;">position</span>: <span style="color: #ff6600;">relative</span>;
  <span style="color: #333399;">top</span>: <span style="color: #339966;">30px</span>;
  <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">lightblue</span>;
}</pre>
    </td>
    <td><ul><li>First</li><li>Second</li><li style="position: relative; top: 30px; background-color: lightblue;">Third</li><li>Fourth</li><li>Fifth</li></ul></td>
  </tr>
</tbody>
</table>


This is why, in our introduction to CSS, we said that margin should be your "go to" property when you want to adjust position. 


##### Cannot use opposite properties

When using `position:relative` if you use the `left` property you cannot also use the `right` property.  And, if you use the `top` property you cannot also use the `bottom` property. If both properties are applied, then the CSS precedence rules will determine the "winner", which is usually just the last one applied.

Again, this is unlike margins, where both `margin-right` and `margin-left` can be meaningfully used.


##### No automatic size adjustments

This follows from the previous limitation. You may recall that block level elements take the width of their parent (when no width is specified).  And when using left or right margins on a block level element that does not have an explicit width, the browser will smartly size the element down for you to make it fit.  But this size adjustment does not happen when you use `position:relative` and the `left` or `right` positional properties. This is easily illustrated with an example. Below is a block level paragraph with a border applied to it.  When a `margin-left` is applied to it, the paragraph is made smaller and no part goes outside its parent.  But when it is `position:relative` and moved with the `left` property, it can leave the bounds of its parent, or go offscreen.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;" colspan="2">margin-left</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;" colspan="2">left</th></tr>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Result</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;">p</span> {
  <span style="color: #333399;">margin-left</span>: <span style="color: #339966;">40px</span>;
}</pre>
    </td>
    <td>
      <p style="margin-left: 40px; font-family: monospace;font-size: 12px;line-height: 24px;border: 2px solid darkblue;">Dorothea was altogether captivated by the wide embrace of this conception.</p>
    </td>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;">p</span> {
  <span style="color: #333399;">position</span>: <span style="color: #ff6600;">relative</span>;
  <span style="color: #333399;">left</span>: <span style="color: #339966;">40px</span>;
}</pre>
    </td>
    <td>
      <p style="position: relative; left: 40px;    font-family: monospace; font-size: 12px; line-height: 24px; border: 2px solid darkblue;">Dorothea was altogether captivated by the wide embrace of this conception.</p>
    </td>
  </tr>
</tbody>
</table>

Admittedly, this is not necessarily a "limitation", for many layout situations preserving the size is exactly what is wanted. 


#### Absolute

```css
position: absolute;
```

Absolute positioning, as it is realized in the browsers via CSS, can be very powerful and that ease and power is very seductive to many CSS newbies. But there are some big trade-offs incurred that are often not appreciated. Many experienced professional CSS developers completely forswear absolute positioning - they will not use it under any circumstances. 

An element that is positioned absolutely is taken out of the normal text "flow" that governs elements positioned statically or relatively.  Instead, an absolutely positioned element is positioned by the `left`, `top`, `right`, and/or `bottom` properties. The size or position of siblings have no effect on an absolutely positioned element that has some positioning properties set (`left`, `top`, etc.)

Let's take a simple example.  Here we have a paragraph that contains some text and an inner `<q>`.  For a better illustration, the paragraph has its height set and a border applied.  The `<q>` is positioned absolutely.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">HTML</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Result</th></tr>
  <tr>
    <td>&lt;p&gt;She bethought herself now of the condemned criminal. &lt;q&gt;What news have you brought about the sheep-stealer, uncle?&lt;/q&gt;&lt;/p&gt;</td>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;">p</span> { 
  <span style="color: #333399;">height</span>: <span style="color: #339966;">200px</span>;
  <span style="color: #333399;">border</span>: <span style="color: #339966;">2px</span> <span style="color: #ff6600;">solid black</span>;  
 }
<span style="color: #0000ff;">q</span> { 
    <span style="color: #333399;">position</span>: <span style="color: #ff6600;">absolute</span>;
    <span style="color: #333399;">left</span>: <span style="color: #339966;">50px</span>;
    <span style="color: #333399;">top</span>: <span style="color: #339966;">50px</span>;
    <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">lightblue</span>;
    <span style="color: #333399;">padding</span>: <span style="color: #339966;">10px</span>;<br>    <span style="color: #333399;">display</span>: <span style="color: #ff6600;">block</span>; 
    <span style="color: #333399;">width</span>: <span style="color: #339966;">70px</span>;
 }
</pre>
    </td>
    <td>
      <p style="height: 200px; border: 2px solid black; position: relative;">She bethought herself now of the condemned criminal. <q style="position: absolute; display: block; left: 50px; top: 50px; background-color: lightblue; padding: 10px; width: 70px;">What news have you brought about the sheep-stealer, uncle?</q></p>
    </td>
  </tr>
</tbody>
</table>

So that seems fairly straightforward and useful. But there are some subtle caveats and trade-offs of which you must be wary:

+ Interpretation of positioning depends upon parent/grandparent elements being positioned elements.
+ Best practice: use both a horizontal and a vertical positioning property on every absolute element.
+ Absolutely positioned elements do not contribute to size of the parent.
+ Absolute positioned block level elements do not get the width of their parent.
+ Margins do not work the same.
+ Opposite properties can be used to size element.


__Interpretation of positioning properties (top, left, etc.) depends ON parent/grandparent being positioned elements (or not).__

_IMPORTANT_: For an absolutely positioned element, <strong><em>where</em></strong> the left, top, etc. are calculated <strong><em>from</em></strong> depends upon the `position` property of the parent and grandparents of the element in question. If the parent of the element is a positioned element (meaning its position is set to anything except `position:static`), then an absolutely positioned child  is positioned relative to that parents rectangle (or grandparent, or great-grandparent, etc).  But if none of the parents are positioned elements, the child is positioned relative to the bounds of the document.  

This means that how the position properties of an absolutely positioned element are interpreted depends upon the position property of its parent (and grandparents). For many developers, this is a spooky action at a distance. Changing the position property on an element may not affect that element at all, but can cause it children (or great great grandchildren) to suddenly jump to another part of the page.  

In the example below, someone who did not read the section in the module 3 about how to style list items has decided to use arbitrary numbers. There are four list items each containing child spans which are absolutely positioned. Two of the list items are position:relative, so the spans are positioned starting from their rectangle.  But two of the list items are `position:static` (the default), so the spans are moved up to the `<ul>` (which is also `position:relative`) where they overlap each other. (The red 1 is hidden behind the red 2). Borders have been added in the result below, so you can easily see the rectangle for `<li>` versus `<ul>`.


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
<tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">HTML</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none">&lt;ul&gt;
&lt;li&gt;First &lt;span&gt;1&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;Second &lt;span&gt;2&lt;/span&gt;&lt;/li&gt;
&lt;li class="rel"&gt;Third &lt;span&gt;3&lt;/span&gt;&lt;/li&gt;
&lt;li class="rel"&gt;Fourth &lt;span&gt;4&lt;/span&gt;&lt;/li&gt;
&lt;/ul&gt;</pre>
    </td>
    <td>
<pre  style="border: none; box-shadow: none"><span style="color: #0000ff;">ul</span>   { <span style="color: #333399;">position</span>: <span style="color: #ff6600;">relative</span>;  }
 
<span style="color: #0000ff;">.rel</span> { <span style="color: #333399;">position: <span style="color: #ff6600;">relative</span></span>; }
 
 <span style="color: #0000ff;">span</span> {
   <span style="color: #333399;">position</span>: <span style="color: #ff6600;">absolute</span>;
   <span style="color: #333399;">left</span>: <span style="color: #339966;">0px</span>;
   <span style="color: #333399;">top</span>: <span style="color: #339966;">0px</span>;
 }</pre>
    </td>
    <td><ul style="position: relative; border: 1px solid dimgray; line-height: 1.4em;"><li style="border: 1px dashed gray; padding-left: 10px; list-style-type: none; line-height: 1.4em; margin-bottom: 0.70788em;">First <span style="position: absolute; left: 0px; top: 0px; font-size: 1.1em; color: red; font-weight: bold; background-color: lightblue; margin-bottom: 0.70788em;">1</span></li><li style="border: 1px dashed gray; padding-left: 10px; list-style-type: none; line-height: 1.4em; margin-bottom: 0.70788em;">Second <span style="position: absolute; left: 0px; top: 0px; font-size: 1.1em; color: red; font-weight: bold; background-color: lightblue;">2</span></li><li style="position: relative; border: 1px dashed gray; padding-left: 10px; list-style-type: none; line-height: 1.4em; margin-bottom: 0.70788em;">Third <span style="position: absolute; left: 0px; top: 0px; font-size: 1.1em; color: red; font-weight: bold; background-color: lightblue;">3</span></li><li style="position: relative; border: 1px dashed gray; padding-left: 10px; list-style-type: none; line-height: 1.4em; margin-bottom: 0.70788em;">Fourth <span style="position: absolute; left: 0px; top: 0px; font-size: 1.1em; color: red; font-weight: bold; background-color: lightblue;">4</span></li></ul></td>
  </tr>
</tbody>
</table>


__Best practice: use both horizontal and vertical positioning property on every absolute element__

There is a very subtle extension to the previous interpretation problem: if an element is set to be `position:absolute` but has no horizontal positioning property (that is, `left` or `right`), then it will be displayed in the flow exactly as it would have been.  Except, later, if `left:0px;` were added (for example), then the element may jump to the left edge of the first parent/grandparent that is a positioned element. The same applies vertically. This is a bewildering behavior, as most users do not expect there to be a difference between `left:0px` and no `left` property at all.

Therefore, for any absolutely positioned element, the best practice is to ensure that one of the horizontal positioning properties (that is, `left` or `right`) and one of the vertical properties (`top` or `bottom`) are set.


__Absolutely positioned elements do not contribute to size of parent__

Whether you realize it or not, one of the most useful default behaviors is that the height of a parent element is automatically extended to include all its children, its content. Designers working in CSS unconsciously lean on this fact as they plan layouts and adjust element positions. But this is __not__ true for children that are positioned absolutely.  Absolutely positioned children do not contribute to the size of the parent element. A parent element that contains only absolutely positioned children will have a height of 0, has no "measurable" content and will behave as if it is empty.

A consequence of this is that as a design starts to use absolute positioning, it may also have to start explicitly setting the dimensions of containers, which makes the overall design brittle and less adaptable.

In the example below, there are two lists (`<ul>`) each with a fat border. The list on the left is normal - its children contribute to making the `<ul>` taller and the fat border extends around, enclosing everything correctly. But the list items (`<li>`) on the right are positioned absolutely.  So those list items on the right do not contribute to the height of the parent. As a result, it ends up with a height of 0, as if it were empty. The fat border just becomes a fat flat line, and the list items themselves are not enclosed. 

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">default</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">absolute</th></tr>
  <tr>
    <td><ul style="border: 4px outset gray; padding: 0 0 0 1em; margin: 1em 0; color: #313131; padding-left: 1em; list-style: disc outside none;"><li style="background-color: lightblue; margin-bottom: 0.70788em;">First</li><li style="background-color: lightblue; margin-bottom: 0.70788em;">Second</li><li style="background-color: lightblue; margin-bottom: 0.70788em;">Third</li></ul></td>
    <td><ul style="padding-left: 1em; list-style: disc outside none; padding: 0 0 0 1em; margin: 1em 0; color: #313131; border: 4px outset gray; line-height: 1.4em;     position: relative;"><li style="margin-bottom: 0.70788em; line-height: 1.4em; background-color: lightblue; position: absolute; top: 0px;">First</li><li style="margin-bottom: 0.70788em; line-height: 1.4em; background-color: lightblue; position: absolute; top: 20px;">Second</li><li style="margin-bottom: 0.70788em; line-height: 1.4em; background-color: lightblue; position: absolute; top: 40px;">Third</li></ul></td>
  </tr>
</tbody>
</table>


__Absolute positioned block level elements do not get the width of their parent__

Earlier we learned that block level elements automatically get the width of their parent, that is, they extend to become full width. But this is only true for static and relative positioned elements. Elements that are absolute positioned (or fixed) do not exhibit this behavior. If you look at the table above, from the previous point, the individual list items have a light blue background color. All the list items are block level elements, and the ones on the left, which are `position:static`, extend their rectangle rightward to fill the entire line. But the right column of absolutely positioned items does not. Their initial size is simply the size of their content.


__Margins do not work the same__

For static and relative positioned items, margins can be used to adjust an element position and keep neighboring siblings "away". We make this quick assumption about margins.  But when an element is absolutely positioned, a given margin might be able to move the element but will not move any siblings. Margins cannot be used to keep siblings "away", to fight crowding.

 As a general rule, if a positioning property is being used (like `left`), then the matching margin (`margin-left`) can also be used to additionally adjust the position of the element. Otherwise, the margin will unlikely have any effect.


__Opposite properties can be used to size element__

This is one of the nicer features. Working with preset dimension properties (`height` and `width`) can make your design brittle and reduce its adaptability. However, absolutely positioned items can instead set the opposite positioning properties (like `left` and `right`) and leave the matching dimensional property (width) unspecified.  The element will grow or shrink based on the size of the ancestor it is positioning against.  Note that this feature is only available to absolute and fixed positioned elements.




### 'z-index'

In the previous sections, we named four positioning properties: `left`, `top`, `right`, and `bottom`.   With these properties, we can govern the placement of positioned elements in both the x and y axis.  But there is a fifth positioning property: `z-index`.

```css
z-index: 3;
```

Like the other positioning properties, `z-index` only applies to positioned elements (elements that have their position property set to relative, absolute,or fixed, but not static).  With the z-index you can control overlapping - whether or not an element is in front of or behind other sibling positioned elements.  The z-index can be an integer 0 or higher. The higher the number, the more "topmost" or "overlapping" the element will be.  

In the sample below, we have two lists with relatively positioned list items and background colors. We are forcing them to overlap by making them position relative and using negative margins (`margin-bottom:-20px;`). The list on the left has no z-index values set, so the later elements overlap the earlier ones.  But on the right, we govern the overlapping with the z-index property.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Result</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Result</th></tr>
  <tr>
    <td><pre style="border: none; box-shadow: none">/* no z-index set */</pre></td>
    <td>
      <ul style="padding: 0 0 0 1em; margin: 1em 0; color: #313131; padding-left: 1em;">
        <li style="background-color: lightblue; position: relative; padding: 10px; margin: 0px 0px -20px 0px !important; border: 1px dotted gray; list-style-type: none;">First</li>
        <li style="position: relative; padding: 10px; margin: 0px 0px -20px 0px !important; border: 1px dotted gray; list-style-type: none; background-color: lightgreen;">Second</li>
        <li style="position: relative; padding: 10px; margin: 0px 0px -20px 0px !important; border: 1px dotted gray; list-style-type: none; background-color: pink;">Third</li>
        <li style="position: relative; padding: 10px; margin: 0px 0px -20px 0px !important; border: 1px dotted gray; list-style-type: none; background-color: plum;">Fourth</li>
      </ul>
    </td>
    <td>
<pre style="border: none; box-shadow: none">.first { z-index: 4; }
.second { z-index: 3; }
.third { z-index: 2; }
.fourth { z-index: 1; }</pre>
    </td>
    <td>
      <ul style="padding-left: 1em; list-style: disc outside none; padding: 0 0 0 1em; margin: 1em 0; color: #313131;">
        <li style="z-index: 4; position: relative; padding: 10px; margin: 0px 0px -20px 0px !important; border: 1px dotted gray; list-style-type: none; background-color: lightblue;">First</li>
        <li style="z-index: 3; position: relative; padding: 10px; margin: 0px 0px -20px 0px !important; border: 1px dotted gray; list-style-type: none; background-color: lightgreen;">Second</li>
        <li style="z-index: 2; position: relative; padding: 10px; margin: 0px 0px -20px 0px !important; border: 1px dotted gray; list-style-type: none; background-color: pink;">Third</li>
        <li style="z-index: 1; position: relative; padding: 10px; margin: 0px 0px -20px 0px !important; border: 1px dotted gray; list-style-type: none; background-color: plum;">Fourth</li>
      </ul>
    </td>
  </tr>
</tbody>
</table>

+ z-index has no effect on position:static (the default) elements.
+ If z-index is not set, siblings that appear later in the HTML document overlap (are "higher than") earlier siblings.
+ z-index is relative between siblings, not any arbitrary elements.


#### Siblings and nesting

It is entirely possible that one element with z-index:100 could appear __below__ another element with z-index:1;  

This can happen because the z-index is used to figure out which sibling is higher than another. But if two elements are not siblings, then the z-index of their respective sibling ancestors will need to be calculated to figure out which is higher.

Below is a simple example: there are two overlapping sibling divs, "Albert" and "Betty". Albert has a red border and is  z-index:1.  Betty has a blue border, and is z-index:2.  Therefore, Betty and her child Bernice are _higher_ than Albert and his child Alan. Albert's child Alan has a z-index of 100, which is the highest z-index of any of them, but because Alan's parent Albert is lower than Betty, Alan remains behind. Alan's high z-index is only relevant to his siblings, not to cousins further out in the document.

<table>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">HTML</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none">&lt;div class="albert"&gt;
&lt;div class="alan"&gt;Alan&lt;/div&gt;
&lt;/div&gt;
&lt;div class="betty"&gt;
&lt;div class="bernice"&gt;Bernice&lt;/div&gt;
&lt;/div&gt;
</pre>
    </td>
    <td>
<pre style="border: none; box-shadow: none"><span style="color: #0000ff;">.albert</span> { <span style="color: #333399;">z-index</span>: <span style="color: #339966;">1</span>; }
<span style="color: #0000ff;">.betty</span>  { <span style="color: #333399;">z-index</span>: <span style="color: #339966;">2</span>; }

<span style="color: #0000ff;">.alan</span> { <span style="color: #333399;">z-index</span>: <span style="color: #339966;">100</span>; }
<span style="color: #0000ff;">.bernice</span> { <span style="color: #333399;">z-index</span>:<span style="color: #339966;">0</span>; }
</pre>
    </td>
    <td>
      <div style="position: relative; width: 210px; height: 210px; margin: 0px;">
        <div style="border: 2px solid red; position: absolute; left: 00px; top: 10px; width: 200px; height: 200px; z-index: 1;">
          <div style="z-index: 100; position: relative; height: 95px; background-color: pink; margin: 0px 0px 10px 0px;">&nbsp;&nbsp;Alan</div>
        </div>
        <div style="border: 2px solid blue; position: absolute; left: 10px; top: 00px; width: 200px; height: 200px; z-index: 2;">
          <div style="z-index: 0; display: inline-block !important; position: relative; width: 90px; height: 200px; background-color: lightblue; margin: 0px 0px 0px 110px;">&nbsp;&nbsp;Bernice</div>
        </div>
      </div>
    </td>
  </tr>
</tbody>
</table>


#### Knowledge checks

1. Will the z-index property work...

  Will the z-index property work on an item with `position:relative;`?

  Ans: Yes <br/>
  the z-index property will apply to all positioned elements. So every position option except position:static.
  

2. On an item with 'position:static;' ...

  Will the z-index property work on an item with `position:static;`?

  Ans: No <br/>
  z-index will not work on a position:static element.




### Activity - Block vs. inline

We've provided you with a starter project file. The [code](src/6.2.7-BlockInline.html) is included below in this CodePen.

This simple file has two block level elements (the paragraphs) and two spans, which are inline. Additionally, there are several classes defined for you. 

Try the following:

+ Notice immediately each paragraph gets its own line.
+ Notice the inline span that follows the paragraph (`</p>`) starts on its own line. However, the second inline span directly follows its predecessor - it does not get a new line, it continues on the same line.
+ Try applying the `brect` and `prect` classes to the elements. (via `class="brect"` ). When applied to the paragraphs, you can see that the classes make the width of the paragraph stretch to the edge of the window. It is the same as its parent width.  Note that its height is no more than its content.  But the background colors and borders are tight to the spans.
+ Try applying the `w` class to each of the elements. This class sets the `width` property. It works on both paragraphs, but it has no effect on the two spans.
+ Try applying the `h` class to each element. This class sets the `height` property. Again, the paragraphs are affected, but the spans are not.
+ Apply the pad class to each element. This class sets the `padding` property. The paragraphs are clearly padded. The spans are also padded, but the extra padding does not space them out. So if the background colors are still being applied, the padded background of one inline element may overlap the other.  Can you think of a solution that would prevent the overlap?
+ Apply the `marg-vert` class to each element. This class sets the top and bottom margins. Note that it works on the block level paragraphs well enough, but has no effect on the inline spans.
+ Apply the `marg-horiz` class to each element. This class sets the left and right margins.  It works on everything.

Play some more with the elements, trying to appreciate how block and inline elements differ.

+ Try changing the HTML so that the inline elements are inside the block level ones.  
+ Put a `margin:0` on the body.
+ Have fun!

NOTE: Please do not upload HTML code to the discussion forum.


### Activity - Cornerpiece

For this activity, use this [CodePen](http://codepen.io/w3devcampus/pen/aWaORJ).

[Sample code](src/6.2.8-ConerPiece.html)

The project file consists of a very long bit of prose and at the end has a single <img> tag.  

+ Get the cornerpiece `<img>` element to appear in the lower right of the viewport.  It should not scroll with the rest of the document.
+ That cornerpiece likely obscures any text that it overlaps. Try to get the document text to be on top of the cornerpiece. You will have to adjust the HTML to achieve this. 
+ That cornerpiece is definitely a decorative graphic. Remove the `<img>` tag and use decorative CSS. Again, you will have to change the HTML to achieve this.

NOTE: Please do not upload HTML code to the discussion forum.



## 6.3 CSS Flexbox

### Sizing and dimensions

We have already touched on the size properties in the various discussions about display and positioning. But here we'll cover them properly and add a few more.


#### Default behavior

The default sizing behavior depends upon the display property for an element.  


##### inline

Inline elements take the size of their content plus any padding. Additionally, inline elements __ignore__ any explicit sizing properties (`width`, `height`, etc.) unless they are also `position:absolute` or `position:fixed`.  This leads to a lot of confusion when newbies are working with inline elements. If you have an inline element whose size you want to indicate explicitly, you should probably change it to inline-block.


##### inline-block

Inline-block elements also take the size of their content, plus padding. However, they respect any explicit sizing properties.  This is handy.


##### block

By default when no sizing properties are used, block level elements take the width of their parent and the height of their content. Block level elements respect any explicit sizing properties.

The "width of parent" aspect of block level elements occasionally surprises developers who might not expect that each animal in a modest list of pets extends all the way to the right edge of the browser.

These display states are covered in the display section.


##### images - aspect ratio preserving

Images have an interesting behavior in that if only one dimension is set, the other is automatically calculated so that the original aspect ratio of the image is preserved.  This is true for both decorative CSS images and `<img>` tags.


#### sizing properties

There are six sizing properties. They are 

+ width
+ min-width
+ max-width
+ height
+ min-height
+ max-height

The width and height properties are a simple way to explicitly set the width or height of an element. It is set directly, and the element maintains that dimension (unless it is inline and ignores these properties). And certainly, when dealing with images, there is little reason to pursue anything but the most straightforward approach. 

However, if you look again at the descriptions for inline-block and block level elements above, you will notice that inline-block elements are sized (height and width) to their content.  And block level elements take the width of their parent and the _height of their content_. So these elements are fundamentally __variably__ sized, and this variability is one of the most powerful and useful aspects of these elements.

However, when we use an explicit width or height property, we remove that variability from the element. This makes it less powerful and less useful.

The `min-width` and `min-height` properties allow us to set a minimum boundary for that variability, but otherwise the variable sizing of the element is unimpeded. So if we have `min-width:300px;` that means the element will be 300 pixels or possibly wider.

Likewise the `max-width` and `max-height` properties allow us to set a maximum boundary for the variability.

As we move into flexbox based layouts, variability in our design will become very important.  


#### Best practice

Unless you have good cause, try to avoid using explicit dimension properties like width and height.  If you must control the dimensions, consider using the min- or max- variants.


#### Cropping and scrolling: overflow

If the element's dimensions are overdetermined by the sizing properties, then its content may not fit. In the example below, the width and height of the paragraph have been set too small for its content.  As a result, the content overflows the rectangle of the paragraph. We've made this easier to see by adding a border and background color to the paragraph.  

This default behavior, that content that doesn't fit is shown anyway, can be surprising if you weren't expecting it. 

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=60%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;">p {
  width:  250px;
  height: 200px;
  border: 1px solid black;
  background-color: lightblue;
 }
 </pre>
    </td>
    <td>
      <p style="width: 250px; height: 200px; border: 1px solid black; background-color: lightblue; font-size: 9px;">For a long time I used to go to bed early. Sometimes, when I had put out my candle, my eyes would close so quickly that I had not even time to say "I'm going to sleep." And half an hour later the thought that it was time to go to sleep would awaken me; I would try to put away the book which, I imagined, was still in my hands, and to blow out the light; I had been thinking all the time, while I was asleep, of what I had just been reading, but my thoughts had run into a channel of their own, until I myself seemed actually to have become the subject of my book: a church, a quartet, the rivalry between François I and Charles V. This impression would persist for some moments after I was awake; it did not disturb my mind, but it lay like scales upon my eyes and prevented them from registering the fact that the candle was no longer burning. Then it would begin to seem unintelligible, as the thoughts of a former existence must be to a reincarnate spirit; the subject of my book would separate itself from me, leaving me free to choose whether I would form part of it or no; and at the same time my sight would return and I would be astonished to find myself in a state of darkness, pleasant and restful enough for the eyes, and even more, perhaps, for my mind, to which it appeared incomprehensible, without a cause, a matter dark indeed.</p>
      <p></p>
    </td>
  </tr>
</tbody>
</table>


##### overflow

The overflow properties govern this situation.  There are three related properties: overflow, overflow-x, and overflow-y.

```css
p { overflow: auto; }
```

With common text, overflowing normally only occurs in the vertical direction (like in the example above). But if your element contains images, extremely long words, or has adjusted CSS white spacing properties, then content can overflow horizontally as well.  The overflow property applies a common policy to both situations, and the overflow-x and overflow-y properties let you assign different policies for horizontal versus vertical overflow. 

There are five possible values: `unset`, `auto`, `visible`, `hidden`, and `scroll`. In the example below, the paragraphs are limited to a height of 100 pixels.

1. `unset` is both the default value when overflow has not been set and a value that can be explicitly set. 
2. The interpretation for the `auto` value may vary from browser to browser. Typically, if a scroll bar is needed, it is shown, but if it is not needed, no scroll bar is shown.  In the example below, no horizontal scroll bar is needed, so none is shown. If there was less content in the paragraph, then no scroll bar would be shown at all.
3. When the value is `scroll`, then the scroll bars are always shown, whether they are needed or not.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=100%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">unset</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">auto</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">visible</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">hidden</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">scroll</th></tr>
  <tr class="tighten">
    <td>
      <p style="height: 120px; overflow: unset;">For a long time I used to go to bed early. Sometimes, when I had put out my candle, my eyes would close so quickly that I had not even time to say "I'm going to sleep."</p>
    </td>
    <td>
      <p style="height: 120px; overflow: auto;">For a long time I used to go to bed early. Sometimes, when I had put out my candle, my eyes would close so quickly that I had not even time to say "I'm going to sleep."</p>
    </td>
    <td>
      <p style="height: 120px; overflow: visible;">For a long time I used to go to bed early. Sometimes, when I had put out my candle, my eyes would close so quickly that I had not even time to say "I'm going to sleep."</p>
    </td>
    <td>
      <p style="height: 120px; overflow: hidden;">For a long time I used to go to bed early. Sometimes, when I had put out my candle, my eyes would close so quickly that I had not even time to say "I'm going to sleep."</p>
    </td>
    <td>
      <p style="height: 120px; overflow: scroll;">For a long time I used to go to bed early. Sometimes, when I had put out my candle, my eyes would close so quickly that I had not even time to say "I'm going to sleep."</p>
    </td>
  </tr>
</tbody>
</table>


#### The box model and box-sizing

So, if we say that some block level element is supposed to have a height and width of 100 pixels, does that include the border or the padding?  This is an excellent question, worthy of some experimentation. The reader is encouraged to explore this.

The answer is that the default behavior of the browser is that the sizing properties govern the size of the content area and any padding or borders are "extra".  But, if this is not the desired behavior, you can change it. 

Every element has several "boxes" it manages: its own content, padding, border, and margins.  In CSS parlance, this question is about the "Box Model" of the element.  Here is an illustration of how the different boxes are organized (innermost to outermost).

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/306cfa0313a449a29b2dbcb0b2afcb86/432fe5c1283c420ea9df95e888578cac/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%40f59373dbfbc04cfbb386dc810e886e0e" ismap target="_blank">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ebbf5b8bead6014e108c5be1df38d824/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/boxmodel.jpg" style="margin: 0.1em;" alt="Flexbox diagram" title="Flexbox diagram" width=350>
  </a>
</div>


##### box-sizing

```css
p { box-sizing: border-box; }
```

The `box-sizing` property determines how the sizing properties are applied.  It has two values: `content-box` and `border-box`.  

The `content-box` value is default and simply means that the height or width properties affect the content box of the element and any padding or border is "additional".  

When `border-box` is used, the sizing properties are used to set the "whole" size of the element, and the content size is likely to be less.


#### This is making my head hurt! How important is this?

Another good question. If you are manipulating items with JavaScript, then it may be important. If you are using any of the "older" methods for CSS layout (like floats, tables, etc.), then managing the box model is of paramount importance.

However, if you are using the flexbox layout (which we begin in the next section), then the box-model is not that important. The rule of thumb is that the more you are directly managing the size of items, the more likely you will need to change the `box-sizing` property to be `border-box`.


### Flexbox

Up to this point, we have covered quite a few different CSS layout concepts. Inline vs. block level display, different position values, various positioning properties, six different sizing properties, plus countless details and interactions.  So by this time, we should know enough to make a two-column page design, right?  Sadly, we cannot.  The intrepid among us might be able to cobble something together by creatively using inline-block, or maybe absolute or fixed positioning, but ultimately, any design built with just the topics we've covered so far will likely be brittle or unwieldy. Why is that?

All the layout properties we've looked at have all applied to an _individual_ element.  But performing layout tasks like columnar layout or anything responsive requires coordinating _multiple_ elements.  This is where the flexbox comes in.  When working with flexbox layout, there are some CSS properties that are applied to a parent element (also known as the flex container) and other CSS properties that are applied to the direct children of that parent (also known as the flex items).  The flex container will handle laying out of its children. And, best of all, the flex container will lay out its children smartly, making the best use of the screen size available to it, while still following the general guidelines you laid down for it.   As a general rule, layout with flexbox is pretty easy and the results are great.  So let's get started.


#### The minimum

The minimum scenario for using flexbox is to make use of two CSS rules, and better results are achieved with a third.

1. display:flex; on the flex container
2. flex:1; on the flex items (the children of the flex container)
3. (better)   flex-flow: row wrap; on the flex container.

Here is a series of screen captures showing these minimum options applied to a parent `<div>` and four identical paragraphs at various browser sizes, with no other properties applied except some small margin and padding on the paragraph, and a background color and a border radius to help visualize.

<p style="border: 2px solid dimgray;"><img style="margin: 5px; vertical-align: top;" alt="Flexbox image with four columns wide" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/12adc51449bbe643629a3a37c8464cae/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/four_across_wide_30.png" type="saveimage" target="[object Object]" width="251" height="94"><img class="three" alt="Flexbox image with three columns and one beneath" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/bd6de0e3780ce3303f225bfaedf61d23/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/three_and_one_30.png" type="saveimage" target="[object Object]" width="157" height="148"><img style="margin: 5px; vertical-align: top;"  alt="Flexbox image with two lines of two" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/741852181e2467cb6c6cdd5a067e9ee9/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/two_and_two_30.png" type="saveimage" target="[object Object]" width="122" height="152"><img style="margin: 5px; vertical-align: top;"  alt="Flexbox image with one column and four lines" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/4e8158ad51651509b53f35439557859e/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/one_30.png" type="saveimage" target="[object Object]" width="87" height="206"></p>

Flexbox image with four columns wideFlexbox image with three columns and one beneathFlexbox image with two lines of twoFlexbox image with one column and four lines


#### flex container

```css
div  { display: flex; }
span { display: inline-flex; }
```

To designate an element as a flex container, we simply set the `display` property to be `flex` or `inline-flex`. A flex element will itself be a block level element, and an inline-flex element will itself be an inline element. However, in both cases the element is now a flex container and will be handling the layout of its children.


##### flex-flow

```css
.fc {
  display: flex;  /* this is now a flex container */
  flex-flow: row wrap; 
 }
```

Flexbox containers can lay out their children both horizontally, as in a row, and vertically, as in a column, and both at the same time.  This means that a single flex container not only can help you lay out a three column design, but also handle the header and footer above and below. (Did we mention that flexbox rocks?)

But the flexbox container does need a starting rule to follow. Do you want it to primarily line things up horizontally like a row? Or vertically like a column? And will you be wanting that row or column to wrap? The `flex-flow` property lets you specify both of those things.

Strictly speaking, the `flex-flow` property is actually an abbreviation that replaces two other flexbox container properties: `flex-direction` and `flex-wrap`.  But the row wrap value is so useful that it will likely be the standard.

```css
flex-flow: <flex-direction> <flex-wrap>;
```

The possible values for the flex-direction are: `row`, `row-reverse`, `column`, and `column-reverse`.

The values for the flex-wrap part are: `wrap`, `wrap-reverse`, and `nowrap`.

There are more properties that we can apply to a flex container and we'll look at them in the upcoming sections. But these two will take care of most of what you might want.


##### flex items

The direct children of a flex container are automatically converted into flex items, with the exception of children that are position-fixed or position-absolute, which are taken out of the "flow" of the flex container.  So there is no property needed to designate a child as a flex item, as it happens automatically. 

One other automatic behavior to be aware of is that empty flex items are automatically removed from the flex container. Keep that in mind if you were planning on using an empty `<div></div>` construct as a placeholder for a CSS background image.

There is an array of flex item properties that can be applied to the children of a flex container, but there are three that we are not supposed to use in isolation. These three are: flex-grow, flex-shrink, and flex-basis.These three properties interrelate, so rather than using them in isolation the CSS3 specification encourages us to use the flex property, which can act as an abbreviation for all the three.


##### flex property

Earlier, we saw that `display:flex;` can be used to designate a parent element as a flex container. In that case, the symbol "flex" is used as a value of the `display` property.

But `flex` is also the name of  a property. It is a property that is applied to flex items, the children of a flex container.  

```css
span { flex: <flex-grow> <flex-shrink> <flex-basis>; }
```

The flex property provides a convenient way to abbreviate the three interrelated properties of `flex-grow`, `flex-shrink`, and `flex-basis`.  The flex property also gives a flex item nice defaults for the optional properties. Therefore, `flex:1;` is __better__ than `flex-grow:1;`.


##### flex-grow

```css
p { flex: 1; /* rather than use flex-grow, use flex: <flex-grow>; */ }
```

The `flex-grow` property is set simply to a positive number. In isolation that number means nothing. However, when the flex container is laying out its children, for any row (or column) it is processing it may end up with a little extra space. The `flex-grow` property determines how much extra space this flex item should get relative to its siblings.  If one sibling has a `flex-grow` value of 2 and another  - `flex-grow` value of 1, the former will receive twice as much of the extra space that is divided among the children.

A larger `flex-grow` value does not necessarily mean that an element is larger than its siblings that have smaller `flex-grow` values. The content of each sibling is first accounted for by the flex container when creating any row or column and only after that has been settled is any extra space distributed among the children.

Setting the `flex-grow` to 0 will prevent the flex item from growing. But remember, that will cause the item to shed its "flexible size" super-power.


##### flex-shrink

```css
p { flex: 1 1; /* rather than use flex-shrink directly, use flex: <flex-grow> <flex-shrink> */ }
```

The `flex-shrink` is the opposite of `flex-grow`. When laying out any row or column, if the flex container needs to take away some space from the children, then those with the highest `flex-shrink` values contribute more of the needed space.  Again, the `flex-shrink` value is just a number and it only has meaning when compared to its sibling `flex-shrink` values. And, again, this only occurs in the situation where the flex-container might need some space from its children.

Note: Like `flex-grow`, setting the `flex-shrink` to 0 will prevent the flex item from shrinking. However, this may not be as desirable as it first seems. Remember the box model from the previous section? If an item `flex-shrink` value is 0, then its border or padding may end up off-screen or pushed out of the parent, because there is a difference between "fitting" and "fitting nicely", and without the ability to be shrunk an item might fit but not "fit nicely". If you must set `flex-shrink` to 0, then it is recommended that you also set the `box-sizing` to `border-box`.


##### flex-basis

```css
p { flex: 1 1 87px;  /* use flex: <flex-grow> <flex-shrink> <flex-basis> */}
```

The `flex-basis` can be used instead of the sizing properties on a flex item. If the `flex-direction` of the parent flex container is `row` or `row-reverse`, then the `flex-basis` will govern the width of the flex item. If the `flex-direction` is `column` or `column-reverse`, it governs the height.

The `flex-basis` provides the starting dimension (width or height) for the flex-item. It may be grown or shrunk from that. If you do not want it to change at all, then set the `flex-grow` and `flex-shrink` to 0, and the `box-sizing` to `border-box`.  However, this is not advisable. Read the `flex-shrink` discussion above.  


### Flexbox advice and best practices

Here are some quick tips to help you get the most out of flexbox.


__Remember the minimum__

If you have a parent element that contains some child elements, then putting `display:flex;` on the parent is all that is needed to get started. The parent itself behaves like a normal block level element, it is the flex container, and all of its children are flex items.

It's not a bad idea to specify the `flex-flow` for the flex container (`flex-flow: row wrap;`), but it isn't required.

It's generally a good idea to also initialize the `flex` property on the flex items (e.g. `flex:1`), but again, this isn't required.


__Use variable dimensions on flex items instead of explicit ones__

This advice may not apply to images and may not be appropriate for every flex item. However, for most flex items, try to avoid using explicit `width` and `height` properties. Instead, use the `flex-basis` to set a desired dimension (e.g. `flex: 1 1 200px;`).  Or consider using `min-width` (or `max-width`) and `min-height` (or `max-height`).

Doing so will make your flex items a bit more malleable. In CSS professional parlance, this is called being "responsive".


__Do not overconstrain your flex items. Let the browser work for you.__

This is a follow-on to the previous piece of advice. With flexbox you give the browser some general guidelines and allow it to figure it out. ("_Hey, put these in a row, I guess they can wrap. This item should be 80 pixels wide generally, and this item should always be at least 200 pixels wide, and this item should be first._").  If you overly constrain the flexbox container by disallowing growing, shrinking, and setting explicit dimensions, then the results may be not optimal. Don't micromanage, let the flexbox do its job.

Remember also, that if you overdetermine the dimensions for an element, then you may also have to start managing its `overflow` setting and its box model. Who needs more worry?  Underconstraining is the path to happiness.


__Thinking of using inline-block? Consider flexbox instead.__

If you are considering changing the display of several elements to be `inline-block`, that may indicate that you should be using flexbox instead. Perhaps their parent should be set to be a flex container and they should be flex items.  


__Centering? Maybe flexbox__

If you need to center some content horizontally, then the previous section on centering may help. It discusses the various options for inline or block level elements.  However, a flex container and a flex child is also a possible approach. The flex container property `justify-content:center;` might help. See the optional section on that.   Both approaches (flexbox and "traditional") have their advantages in various situations.  Use your judgement.

If you need to center something vertically, unless it is an inline element or the content of a table cell, the best answer is almost certainly flexbox. See the `align-content` and `justify-content` properties in the advanced optional flexbox material.


__AVOID margin: auto on flex items__

`margin:auto` prevents align-self from working (a very handy flexbox property covered in the Optional section). There are effective ways of using auto margins though, just do so [with care](https://medium.com/@samserif/flexbox-s-best-kept-secret-bd3d892826b6#.wzrvpxpqv)


__Try to keep your flexbox usage simple__

You can see [here](http://caniuse.com/#search=flexbox) that flexbox is widely supported across all the modern browsers. However, Internet Explorer had bugs in its support (but they are fixed in Edge). And the flexbox standard has had some changes since it was first proposed. For this reason, try to keep your usage of flexbox close to what is covered in this course material, and, as with all CSS, be sure to always test in as many browsers as possible.


__External resources__

+ [Flexbox documentation](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox) on MDN (available in many languages!)
+ [What Happens When You Create A Flexbox Flex Container?](https://www.smashingmagazine.com/2018/08/flexbox-display-flex-container/) (by Rachel Andrew - 2 August 2018)



### Knowledge checks (1-8)

1. Compatibility of combinations

  Which of the following combinations are NOT compatible? Which of the following will not work?

  1. display:inline; min-width:200px;
  2. display:inline-block; max-width:100px;
  3. display:block; width:200px;

  Ans: 1<br/>
  Inline elements do not respond to the sizing properties.


2. Default sizing

  Which of the following statements correctly describe the default sizing of a block level element? How does a block level element behave when no sizing properties are applied?

  1. horizontally sizes to its own content, takes the height of its parent
  2. vertically sizes to own content, takes the width of parent
  3. sized horizontally and vertically to its content
  4. takes height and width of parent

  Ans: 2<br/>
  A block level element defaults to the width of its parent but vertically is sized by its content.


3. Flexbox container

  How do you designate an element as a flexbox container? (select all that apply -- 2 correct answers!)

  1. display:flex
  2. flex:1
  3. display:inline-flex
  4. display:block; flex:1

  Ans: 13<br/>
  The flex property is applied to flexbox children, not the flexbox container.


4. What is needed to designate its children?

  If a parent has been designated as a flexbox container, then what is needed to designate its children as a flexbox items?

  1. display:flex
  2. nothing. All direct children of a flexbox container are automatically made into flexbox items.
  3. position:static
  4. flex:1

  Ans: 2<br/>
  It is recommended that every flexbox item have its flex property initialized, but this is not strictly required.


5. Flexbox layout

  Examine this image of a flexbox layout:

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/306cfa0313a449a29b2dbcb0b2afcb86/432fe5c1283c420ea9df95e888578cac/3?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%409aed5d083fa44945885e2945292e3aee" ismap target="_blank">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/bd6de0e3780ce3303f225bfaedf61d23/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/three_and_one_30.png" style="margin: 0.1em;" alt="image shows a browser window with three flexbox items of the same size layouted as 3 columns, and one flewbox item below that is as wide as the sum of the 3 items above" title="image shows a browser window with three flexbox items of the same size layouted as 3 columns, and one flewbox item below that is as wide as the sum of the 3 items above" width=150>
    </a>
  </div>

  Which of the following is true?

  1. the flexbox container has flex-flow:row wrap;
  2. the last flexbox item has clear:both
  3. the flexbox container has flex-flow:row;
  4. the flexbox container has flex-flow: column;
  
  Ans: 1<br/>
  The flex-flow specifies both a row flex-direction and wrapping


6. Flexbox container with three children

  There is a flexbox container with three children with identical content.

  The flexbox container has `flex-flow:row;`

  The first child has `flex:1` applied to it, the second `flex:2`, and the third `flex:3`.

  `flex:1` is the same as which of the following?

  1. flex-basis:1px;
  2. flex-grow:1
  3. flex-shrink:1

  Ans: 1


7. Which of the following are possible...

  There is a flexbox container with three children with _identical content_.

  The flexbox container has `flex-flow:row;`

  The first child has `flex:1` applied to it, the second `flex:2`, and the third `flex:3`.

  When examined in the browser, which of the following are possible? (select all that apply - 2 correct answers!)

  1. all three elements are the same width.
  2. the first item is wider than the others.
  3. the first item is the narrowest and the third item the widest.
  4. the first item is much narrower, and the second and third items are the same width.

  Ans: 13<br/>
  + if there is extra space to be applied to the various children, then no two of them will be the same width.
  + flex:1 determines the relative growth of an item, with a smaller number meaning less relative growth than a larger number.


8. Full flex property

  Which of the following is the correct description of the full flex property?

  1. `flex: <flex-grow> <flex-basis> <flex-shrink>`
  2. `flex: <flex-grow> <flex-shrink> <flex-basis>`
  3. `flex: <flex-shrink> <flex-grow>`
  4. `flex: <flex-grow> <flex-start> <flex-end>`
  
  Ans: 2



### Knowledge checks (9-13)

#### Units

Recall from Week 3 the different units that are available in CSS for specifying dimensions:

  + px
  + em
  + rem
  + %
  + vh / vw

These are all convenient for sizing text and images and videos as might befit the need.  However, when pursuing page layout we often want to mix units. Examine this simple situation:

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">HTML</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">CSS</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;">&lt;body&gt;
  &lt;header&gt;Header&lt;/header&gt;
  &lt;main&gt;Content Goes Here&lt;/main&gt;
&lt;/body&gt;
  </pre>
    </td>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;">body</span>{
  <span style="color: #333399;">margin</span>: <span style="color: #339966;">0px</span>; 
  }
<span style="color: #0000ff;">header</span> {
  <span style="color: #333399;">height</span>: <span style="color: #339966;">100px</span>;
  <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">lightblue</span>;
  }
<span style="color: #0000ff;">main</span> {
  <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">whitesmoke</span>;
  <span style="color: #333399;">overflow-y</span>: <span style="color: #ff6600;">scroll</span>;
  }
  </pre>
    </td>
  </tr>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;" colspan="2">Result</th></tr>
  <tr>
    <td colspan="2"><img alt="image shows a browser window with a large header. In the main element, it is written &quot;Content Goes Here&quot;. The content is not extending down (i.e., there is a little scrolling bar)" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ae8c8eaae966eba6c448fcf4a210fb37/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/unhappy.png" type="saveimage" target="[object Object]" width="404" align="middle"></td>
  </tr>
</tbody>
</table>

Because `<header>` and `<main>` are both block level elements, they extend full width.  Great.  And the `height` of the header has been set to `100px`.  But the main does not yet have a height set, so it takes the height of its content. However, for this design, we want it to scroll its content, and we want it to extend to the bottom of the browser window.  The scrolling is easily accomplished with the `overflow-y:scroll;` declaration.

So what should the height of the `<main>` section be to make it extend down?  


#### calc()

The ideal height for the main section is that of the viewport minus the height of the header.  You may remember that the vh unit is a percentage of the viewport.  So `100vh` is one hundred percent of the viewport.  And we can see that the height of the header in the CSS above is `100px`.

Wherever a CSS dimension unit is accepted we can also provide the `calc()` expression. This expression lets us mix units of different types. It looks like this:

```css
main { height: calc(100vh - 100px); }
```

And if we try adding that to the CSS above, we get the result we wanted:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/306cfa0313a449a29b2dbcb0b2afcb86/432fe5c1283c420ea9df95e888578cac/3?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%409aed5d083fa44945885e2945292e3aee" ismap target="_blank">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b96b9edc87d4895b8a307caf8e85a27e/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/happy.png" style="margin: 0.1em;" alt="image shows a browser window with a large header. In the main element, it is written "Content Goes Here". The main is extending to bottom (i.e., there is a big scrolling bar)" title="image shows a browser window with a large header. In the main element, it is written "Content Goes Here". The main is extending to bottom (i.e., there is a big scrolling bar)" width=250>
  </a>
</div>

You can download the final result here.

So that's `calc()`, another weapon in your ever strengthening CSS arsenal.


__Notes__
+ The parentheses for `calc()` are required.   
+ The standard arithmetic operations are supported, addition, subtraction, multiplication, and division:  +  -  *  / 
+ Overuse of `calc()` can make your page slow. 
+ Using `calc()` for sizing flexbox items (the items inside a flexbox container) may not always work as desired. In particular, `calc()` along the cross axis may not work in every situation.


__Exploration Activity__
Go back to the original situation posed above.  Can you think of any other solutions that will end up with the desired result that don't use calc() and do not use flexbox?  We have already discussed quite a few layout concepts. Might some be leveraged to otherwise solve this problem?

<hr/>

9. calc() declarations

  Which of the 'calc()' declarations are correct? (select all that apply -- 3 correct answers!)

  1. calc 100vh - 80px;
  2. calc(100vh - 80px);
  3. calc(80px + 120px);
  4. calc(75vw * 2);
  
  Ans: 234

<hr/>


Examine the following HTML code FOR questions 10 through 13:

```html
<body>
  <header>Header</header>
  <article>Article</article>
  <footer>Footer</footer>
</body>
```

##### Situation

For this design, you are asked to make the header and footer each have a height of 80px. The content of the article may vary in height. It could be a long series of paragraphs, or it could be just a sentence.

What is the CSS that will size the article height such that it will keep the footer at the bottom of the viewport if the article content is small? However, if the content is long, it will let the article just size to the content (meaning the footer may be offscreen until the user scrolls the entire page down).  

<hr/>

The next four questions are about the CSS needed to size the article as described.

10. Which property for the height of the article

  Examine the code and situation above. Think about the CSS required to acheive it.

  ```css
  article { property:value; }
  ```

  What property should be set to control the overall height of the article as described?

  1. min-height
  2. max-height
  3. height

  Ans: 1 <br/>
  + Setting the height of the article could help fix the footer to the bottom, but if the content of the article is long, it will overflow.
  + Setting the minimum height for the article can help keep it sized so that the footer, which follows it, stays at the bottom of the browser window.


11. Desired value

  Examine the code and situation above. In Question 10, you selected the property that should be used to control the height of the article. But what should its value be set to?

  Which of these sentences describes the desired value most accurately?

  1. the maximum height of the article should be no more than twice the viewport height.
  2. at minimum, the height of the article should be the height of the viewport minus the combined heights of the header and footer.
  3. the minimum height of the article should be the height of the viewport plus the height of the header and the footer
  4. the height of the article should be the same as the height of the viewport

  Ans: 2 <br>
  + (1) There is no reason to set an upper bound on the article height.
  + (3) Adding all three heights together is not the size we want.
  + (4) For this, we do not want to set the height of the article, but its min-height. And setting it to be the same as the viewport will fail to take into consideration the heights of the footer and header


12. Height of the viewport

  Which of these unit declarations represents the height of the viewport?

  1. 100vw
  2. 100vh
  3. 720px
  4. 100%

  Ans: 2 <br/>
  + vw is the viewport _width_, not its height
  + 100vh means one hundred percent of the viewport height.
  + There is no guarantee that the browser window will be any given pixel size.
  + 100% means the height of the parent. In our context, that is the height of the body, which would be limited to the height of its content. This is not the same as the height of the viewport, as the content of the document could be shorter or taller than the viewport.


13. What value should be set...

  Examine the code and situation above. In question 10, you selected the property we need to control the height of the article as described. In question 11, you selected a description of its value. In question 12, you selected the declaration that represents the overall height of the viewport. Lastly, observe that the height of the footer and header are each 80 pixels. So, finally, what value should be set for the property?

  ```css
  article { property:value; }
  ```

  What value should be set for the property?

  Ans: calc(100vh - 160px)



### Activity - Basic flexbox

There are several more flexbox related properties that we will learn. However, there is a lot already that can be accomplished with only display:flex, flex-flow, and flex. So let's explore.

You can edit in this [CodePen](http://codepen.io/w3devcampus/pen/mmGeda).

[Sample Code](src/6.3.6-Flexbox.html)

The resulting layout should look like this:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/306cfa0313a449a29b2dbcb0b2afcb86/432fe5c1283c420ea9df95e888578cac/3?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%409aed5d083fa44945885e2945292e3aee" ismap target="_blank">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/07b4af5c81f90dafe6e40a9036ef9ae9/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/resultflexbox.PNG" style="margin: 0.1em;" alt="Result of 6.3.6 Activity - Basic flexbox" title="Result of 6.3.6 Activity - Basic flexbox" width=350>
  </a>
</div>


### Basic flexbox

<video src="https://edx-video.net/W3CHTM502016-V015900_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@3a74f3304450402b9944caf0d9202ea9/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Activity - Holy grail with flexbox

Among CSS aficionados, the "holy grail" was considered to be a simple page layout of a header, footer, and three columns specified with CSS and without any hacks or complications.  In other words, CSS as a language would not be considered ready for performing layout until such a task could be accomplished.

With flexbox this goal is finally achievable. And it doesn't require much flexbox knowledge. We've already covered everything we need. So let's see how to do it.


#### Semantic sections

You may recall from week 2 several semantic tags for denoting the different parts of a page:

+ header
+ footer
+ aside
+ article
+ main
+ section
+ nav

Several of those tags like `<header>`, `<footer>`, and `<aside>` have tantalizingly promising names that suggest they provide some sort of layout assistance.  However, the HTML5 newcomer may be disappointed to discover that those tags are just basic block level elements, functioning no different than `<p>` or `<div>`.   Flexbox comes to the rescue and helps those tags realize their potential.


__Step 1 - choose tags__

Let us imagine that we are working on a three-column page with header and footer. So the `<header>` and `<footer>` tags are obvious choices.  Let's pick 3 others. We'll start with something like this:

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">HTML</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;">&lt;body&gt;
  &lt;header&gt;the header&lt;/header&gt;
  &lt;aside&gt;first column&lt;/aside&gt;
  &lt;main&gt;the main content should be here&lt;/main&gt;
  &lt;section&gt;this is the third column&lt;/section&gt;
  &lt;footer&gt;the footer&lt;/footer&gt;
&lt;/body&gt;</pre>
    </td>
  </tr>
</tbody>
</table>

NOTE:  A better practice is to use longer text content for the dummy text.  This will help us verify sizing and scrolling, etc. Instead of simple text like "first column", insert a long paragraph of text.


__Step 2 - surround with flexbox container__

Our five tags will be the flexbox items. They need to be nested in a flexbox container. So we'll surround them with a simple div, since the flexbox container serves no semantic purpose - it is only used to achieve a layout goal, and we'll apply a class to the div so we can easily apply the CSS we want.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">HTML</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;">&lt;body&gt;
  &lt;div class="fc"&gt;
    &lt;header&gt;the header&lt;/header&gt;
    &lt;aside&gt;first column&lt;/aside&gt;
    &lt;main&gt;the main content should be here&lt;/main&gt;
    &lt;section&gt;this is the third column&lt;/section&gt;
    &lt;footer&gt;the footer&lt;/footer&gt;
  &lt;/div&gt;
&lt;/body&gt;</pre>
    </td>
  </tr>
</tbody>
</table>


__Step 3 - add visualization CSS__

This can be removed later, but when working with layout it is often handy to temporarily apply a border or background color to our main elements to be able to see them fully.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;">body</span> { margin:0px; }

<span style="color: #0000ff;">.fc</span> &gt; * {
  <span style="color: #333399;">margin</span>: <span style="color: #339966;">10px</span>;
  <span style="color: #333399;">padding</span>: <span style="color: #339966;">20px</span>; 
  <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">lightgray</span>;
  <span style="color: #333399;">border-radius</span>: <span style="color: #339966;">10px</span>;
}</pre>
    </td>
    <td style="text-align: center;"><img alt="initial layout" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b3f9514fae73a184a82908fde05f97b0/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/holy_grail_initial_300.png" type="saveimage" preventdefault="function (){r.isDefaultPrevented=n}" stoppropagation="function (){r.isPropagationStopped=n}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" isdefaultprevented="function t(){return!1}" ispropagationstopped="function t(){return!1}" isimmediatepropagationstopped="function t(){return!1}" target="[object Object]" width="300" height="245"></td>
  </tr>
</tbody>
</table>


__Step 4 - add flexbox CSS__

We need to set the div to be a flex-container and set its flex-flow as well as initialize the flex property on all the flex items.  We saw this earlier and it is very simple. The sections will line up across as a row if your browser is wide enough.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;">.fc</span> { 
  <span style="color: #333399;">display</span>: <span style="color: #ff6600;">flex</span>;
  <span style="color: #333399;">flex-flow</span>: <span style="color: #ff6600;">row wrap</span>;
}
<span style="color: #0000ff;">.fc</span> &gt; * { 
  <span style="color: #333399;">flex</span>: <span style="color: #339966;">1</span>; 
}</pre>
    </td>
    <td style="text-align: center;"><img alt="first flex properties applied" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b719bc73c1ac80e6a7ac5d77ef5070dc/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/holy_grail_flex_300.png" type="saveimage" preventdefault="function (){r.isDefaultPrevented=n}" stoppropagation="function (){r.isPropagationStopped=n}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" isdefaultprevented="function t(){return!1}" ispropagationstopped="function t(){return!1}" isimmediatepropagationstopped="function t(){return!1}" target="[object Object]" width="300" height="176"></td>
  </tr>
</tbody>
</table>


__Step 5 - set header and footer widths__

We want to get the header and the footer into the correct position. To do that, we simply need to make them full width. There are two possible approaches to accomplishing this:

+ explicitly set one or more of the width properties (width, min-width, max-width) to the desired value
+ set the flex-basis  

Either approach will work, though if you go with the first approach you might also need to set the box-sizing property to be border-box.   We'll use the flex-basis, since that is simpler and participatory.

Since this is the layout for the entire page, we'll use the vw units to set the width to be 100 percent of the viewport width. 

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #0000ff;">.fc header</span>,
<span style="color: #0000ff;">.fc footer</span> { 
  <span style="color: #333399;">flex</span>: <span style="color: #339966;">0 1 100vw</span>;
}</pre>
    </td>
    <td style="text-align: center;"><img alt="header and footer full width" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/defe36ced89e46f7af23614781aa6a91/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/holy_grail_header_300.png" type="saveimage" preventdefault="function (){r.isDefaultPrevented=n}" stoppropagation="function (){r.isPropagationStopped=n}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" isdefaultprevented="function t(){return!1}" ispropagationstopped="function t(){return!1}" isimmediatepropagationstopped="function t(){return!1}" target="[object Object]" width="300" height="193"></td>
  </tr>
</tbody>
</table>


__Step 6 - increase flexbox container height__

You may notice that if there is little content of the sections, then the footer is not at the bottom of the viewport.  For many designs and situations, that is not a problem. However, for many designs, we want the footer to be either at the bottom of the viewport, or at the bottom of the page content, whichever is lower.  Meaning, that if the content of the page exceeds the viewport height, we should have to scroll down to see the bottom of the content, and then the footer would immediately follow. 

So how can we get that footer down there when there isn't enough content?  Think for a minute about this before continuing to read.

...[thinking]...

Have you figured it out? The solution is simple: just make the minimum height of the flex container be the viewport height.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #808080;">/* ensure flex-container is always at least as tall as the viewport. 
   Keeps footer from coming up*/</span>
<span style="color: #0000ff;">.fc</span> { <span style="color: #333399;">min-height</span>: <span style="color: #339966;">100vh</span>; }
</pre>
    </td>
    <td style="text-align: center;"><img alt="completed layout" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/14ed0170294836374ebc6bd9c86b4078/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/holy_grail_complete_300.png" type="saveimage" preventdefault="function (){r.isDefaultPrevented=n}" stoppropagation="function (){r.isPropagationStopped=n}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" isdefaultprevented="function t(){return!1}" ispropagationstopped="function t(){return!1}" isimmediatepropagationstopped="function t(){return!1}" target="[object Object]" width="300" height="180"></td>
  </tr>
</tbody>
</table>


__Congratulations__ - we are done!  So simple.  Go and try increasing the content of one of the middle sections by adding several paragraphs of text. Check that the behavior of the footer is correct.  

For reference, here is the final CSS, with comments. This does not include the visualization CSS for the background colors and rounded corners.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">CSS</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #808080;">/* initialize flexbox container and flexbox items */</span>
<span style="color: #0000ff;">.fc</span> { 
  <span style="color: #333399;">display</span>: <span style="color: #ff6600;">flex</span>;
  <span style="color: #333399;">flex-flow</span>: <span style="color: #ff6600;">row wrap</span>;
}
<span style="color: #0000ff;">.fc</span> &gt; * { 
  <span style="color: #333399;">flex</span>: <span style="color: #339966;">1</span>; 
}

<span style="color: #808080;">/* header and footer should be full width */</span>
<span style="color: #0000ff;">.fc header</span>,
<span style="color: #0000ff;">.fc footer</span> {
  <span style="color: #333399;">flex</span>:<span style="color: #339966;"> 0 1 100vw</span>; 
}

<span style="color: #808080;">/* ensure flex-container is always at least as tall as the viewport. 
   Keeps footer from coming up*/</span>
<span style="color: #0000ff;">.fc</span> { <span style="color: #333399;">min-height</span>: <span style="color: #339966;">100vh</span>; }</pre>
    </td>
  </tr>
</tbody>
</table>


__Hey - the header and footer height changes__

That is a great observation!  The flexbox container will manage the header and footer height as a function of managing its vertical space.   If you don't want the footer or header to be vertically resized, then the solution is to simply set their height. However, if you do this, you may notice that the flexbox container still gives their row extra height which they simply don't use. So the resulting layout is not optimal.

BUT, reflect for a moment: if the header and the footer are full width and they are fixed height, what is the flexbox container doing for them? Are they participating in the layout of their siblings in any way? They are not. If the header and footer are set to a constant height and the width of the viewport, they don't need any help from the flexbox container.  So, in this case, the solution is to remove them from the flexbox.


__Step 7 - (optional) remove header and footer from flexbox container__

The HTML change is trivial, and for the CSS we simply set header and footer width and height as desired (and we will likely want to set their box-sizing as well).

The only trick is that we must also adjust the height of the flexbox container. It is no longer the full height of the viewport. Instead, it is the full height of the viewport minus the combined height of the header and footer.  For that, we'll use calc() 


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">Result</th></tr>
  <tr>
    <td>
<pre style="border: none; box-shadow: none;">&lt;body&gt;
  &lt;header&gt;the header&lt;/header&gt;
  &lt;div class="fc"&gt;
    &lt;aside&gt;first column&lt;/aside&gt;
    &lt;main&gt;the main content should be here&lt;/main&gt;
    &lt;section&gt;this is the third column&lt;/section&gt;
  &lt;/div&gt;
  &lt;footer&gt;the footer&lt;/footer&gt;
&lt;/body&gt;</pre>
    </td>
    <td>
<pre style="border: none; box-shadow: none;"><span style="color: #808080;">/* ensure flex-container is always at least as tall as the viewport, 
   minus the height of the header and footer combined. 
*/</span>
<span style="color: #0000ff;">.fc</span> { <span style="color: #333399;">min-height</span>: <span style="color: #ff6600;">calc</span>(<span style="color: #339966;">100vh - 200px</span>); } 

<span style="color: #808080;">/* size header and footer to be full width and 100px tall each */</span>
<span style="color: #0000ff;">header</span>,
<span style="color: #0000ff;">footer</span> {
  <span style="color: #333399;">box-sizing</span>: <span style="color: #ff6600;">border-box</span>;
  <span style="color: #333399;">width</span>: <span style="color: #339966;">100vw</span>;
  <span style="color: #333399;">height</span>: <span style="color: #339966;">100px</span>;
}</pre>
    </td>
  </tr>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;" colspan="2">Result</th></tr>
  <tr>
    <td style="text-align: center;" colspan="2"><img alt="optional fixed header/footer height" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/dc93deee2b71d70002d941161aa25cfe/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/holy_grail_optional_400.png" type="saveimage" preventdefault="function (){r.isDefaultPrevented=n}" stoppropagation="function (){r.isPropagationStopped=n}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" isdefaultprevented="function t(){return!1}" ispropagationstopped="function t(){return!1}" isimmediatepropagationstopped="function t(){return!1}" target="[object Object]" width="400" height="340"></td>
  </tr>
</tbody>
</table>


#### Try it!

You are encouraged to follow these steps yourself. It is very satisfying seeing everything come together step by step.  But the two completed versions are available for direct download.

+ Holy grail variable height header and footer: [Sample Code](src/6.3.8-Variable.html)
+ Holy grail fixed height header and footer: [Sample code](src/6.3.8-Fixed.html)


#### Amendment

At the beginning of this section, the "holy grail" of layout was described as a three-column layout with header and footer. However, that representation wasn't quite complete. The holy grail is all that plus being responsive, meaning that on small devices the three columns should collapse to one.

How might you do this?  Experiment and see if you can figure it out.  (Answer below).

Here is a possible approach to make the columns more responsive.  

```css
.fc > * { min-width: 200px; }
```

Do you see why this works?



### Activity - Flex columns

Using the previous activity as a starting place, try setting the flex-flow of the flex container to `flex-flow: column wrap;`

Try to lay out something like this, where the header is a narrow column on the left and the footer is a narrow column on the right.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/306cfa0313a449a29b2dbcb0b2afcb86/432fe5c1283c420ea9df95e888578cac/3?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%409aed5d083fa44945885e2945292e3aee" ismap target="_blank">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/33fc647c20a8c85cc02c715d8268d72a/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/flex_column_400.png" style="margin: 0.1em;" alt="text" title="caption" width=250>
  </a>
</div>
 brower window showing 5 flebox items: 2 are vertical and surround 3 horizontal ones

Some notes:

+ Don't use the optional approach from the previous section. 
+ The default block level behavior of taking the width of the parent will work a bit against you. 
+ You will have to explicitly set width properties (width, min-width, and/or max-width) on all the children and the flexbox container.
+ Best results are achieved by sizing the flexbox container in both dimensions.
+ The margins between flexbox items are 10px per column. So you may need to account for that when performing dimension calculations to avoid a scroll bar appearing.  
+ Putting box-sizing: border-box on the flex items may help as well.

[Sample Code](src/6.3.9-Flex.html)


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





