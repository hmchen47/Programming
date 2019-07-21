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


##### Best practice: use both horizontal and vertical positioning property on every fixed element

There is a very subtle extension to the previous interpretation problem: if an element is set to be `position:fixed`, but has no horizontal positioning property (that is, `left` or `right`), then it will be displayed in the flow exactly as it would have been.  Except, later, if `left:0px;` is added (for example), then the element may jump to the left edge of the browser window. The same applies vertically. This is a bewildering behavior, as most users do not expect there to be a difference between `left:0px` and no `left` property at all.

Therefore, for any fixed positioned element, the best practice is to ensure that one of the horizontal positioning properties (that is, `left` or `right`) and one of the vertical properties (top or bottom) are both set.


##### Fixed positioned block level elements do not get the width of their parent

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


##### Interpretation of positioning properties (top, left, etc.) depends ON parent/grandparent being positioned elements (or not).

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


###### Best practice: use both horizontal and vertical positioning property on every absolute element

There is a very subtle extension to the previous interpretation problem: if an element is set to be `position:absolute` but has no horizontal positioning property (that is, `left` or `right`), then it will be displayed in the flow exactly as it would have been.  Except, later, if `left:0px;` were added (for example), then the element may jump to the left edge of the first parent/grandparent that is a positioned element. The same applies vertically. This is a bewildering behavior, as most users do not expect there to be a difference between `left:0px` and no `left` property at all.

Therefore, for any absolutely positioned element, the best practice is to ensure that one of the horizontal positioning properties (that is, `left` or `right`) and one of the vertical properties (`top` or `bottom`) are set.


##### Absolutely positioned elements do not contribute to size of parent

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

##### Absolute positioned block level elements do not get the width of their parent

Earlier we learned that block level elements automatically get the width of their parent, that is, they extend to become full width. But this is only true for static and relative positioned elements. Elements that are absolute positioned (or fixed) do not exhibit this behavior. If you look at the table above, from the previous point, the individual list items have a light blue background color. All the list items are block level elements, and the ones on the left, which are `position:static`, extend their rectangle rightward to fill the entire line. But the right column of absolutely positioned items does not. Their initial size is simply the size of their content.


##### Margins do not work the same

For static and relative positioned items, margins can be used to adjust an element position and keep neighboring siblings "away". We make this quick assumption about margins.  But when an element is absolutely positioned, a given margin might be able to move the element but will not move any siblings. Margins cannot be used to keep siblings "away", to fight crowding.

 As a general rule, if a positioning property is being used (like `left`), then the matching margin (`margin-left`) can also be used to additionally adjust the position of the element. Otherwise, the margin will unlikely have any effect.


##### Opposite properties can be used to size element

This is one of the nicer features. Working with preset dimension properties (`height` and `width`) can make your design brittle and reduce its adaptability. However, absolutely positioned items can instead set the opposite positioning properties (like `left` and `right`) and leave the matching dimensional property (width) unspecified.  The element will grow or shrink based on the size of the ancestor it is positioning against.  Note that this feature is only available to absolute and fixed positioned elements.




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





