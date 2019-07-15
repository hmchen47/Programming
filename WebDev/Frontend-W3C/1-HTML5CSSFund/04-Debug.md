# Module 4: Fixing and debugging


## 4.1 Introduction to Module 4

### Welcome to Module 4

<video src="https://edx-video.net/W3CHTM502016-V014400_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@a7f3d2b7cefc4e5690548f5cc63d09b0/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Module 4 - Content

4.1 __Introduction__: You will now begin learning how to fix your Web page when it's not doing what you hoped it would do.

4.2 __Tools__: Learn about tools and accessibility and how they relate to debugging.

4.3 __The Box Model__: Understanding the CSS Box Model and how to control the spacing of elements on the page.

4.4 __Precedence__: Which style controls what? — using the debugger in the browser to understand conflicting rules.

4.5 __Give Your Mind a Workout__: Lets see what you have learned about debugging your code.


## 4.2 Debugging tools and HTML5

### Tools

It's hard to overestimate the value of tools for programming languages. There are tools for creation, testing, debugging and even measuring the performance of a program. HTML pages are really programs, in specific programming languages, so you need tools for those as well.

One tool that you should, by now, be very familiar with, is the editor.  While traditional text editors allowed you to enter and edit text, modern editors can actually help you detect and avoid errors, visualize your program more clearly, and even stick in bits of text for you if it thinks it knows what you might need, e.g. close tags.

Some of the most ubiquitous tools are in the browser itself, which is handy because everyone seems to have one. You might have even seen this yourself if you've ever tried the "Show Source" button, but perhaps the most important tool that we have yet to explore is the debugger activated when you "Inspect Element".


#### Accessibility

While it's important that your page looks and acts the way you intend, there are other considerations as well. One important aspect is "[accessibility](https://www.w3.org/WAI/intro/accessibility.php)". When talking about Web pages, accessibility means designing your page with various disabilities in mind. For example, for someone with impaired vision, you'd want to make sure that your page is zoomable, or make sure that it makes it easy for screen-readers. Just as wheelchair ramps are a benefit for many users (ask anyone who's had to drag a stroller up the stairs), making your Web site accessible can be a benefit for many users.

Fortunately, there are a number of tools available to help evaluate the accessibility of your site.  You can evaluate the overall accessibility of your page, see how it looks to a screenreader and even figure out how well your background a foreground colors interact.  For a good list of such tools, check out [Web Accessibility Evaluations Tools List](https://www.w3.org/WAI/ER/tools/).


#### Debugging

When you're using a traditional programming language, like JavaScript, debugging is primarily concerned with values of variables, what path is being taken through the code, and whether the program crashes, usually resulting in everything after the crash not happening at all. JavaScript is what you could call a "Procedural" language, in that things follow a procedure in order described by the program. Just think of how you might direct a small child, "Go into the bathroom, stand in front of the sink, pick up your toothbrush, then put toothpaste on it and put the toothbrush in your mouth, but don't swallow the toothpaste etc, etc." It can be a bit tedious, but then you've got a better chance that the end result will be accomplished.

HTML and CSS are not procedural languages, they are "Declarative". You declare what you want, and the computer makes it happen. You say "this is the header, here's a paragraph, I want this to be large, that to be red, on your mark, get set GO!". You don't proscribe exactly how it's done, just what you want the result to be. Now you're dealing with something more like a teenager - "I want to see this room sparkle! And I should be able to bounce quarters on that bed!". Less tedious, just sometimes it's a bit tricky to get exactly what you're hoping for.

In either case, you might need some help. With a small child, you might rely on an older sibling reporting exactly what happened, so you can correct any unexpected variations that might occur. For teenagers you can usually listen at some distance and figure out what's happening (or not happening).

Since we are focusing on HTML and CSS, let's consider what sort of info may be helpful. There are several things that can go wrong with our programs. Some text might be missing. Some things will be in the wrong place. Some things might be too close together, while others are too far apart. You thought you had everything right, but it doesn't look quite right. How to figure out where the problem is? That's where Development tools come in.

Every browser is a bit different, but most of them have ways to examine the various elements and their properties. It probably began as a way to see what's going on with particular elements of the HTML page, at least or so it seems as "Inspect Element" seems to be common to most browsers, including Microsoft Edge and Firefox.  Note that if all browsers are likely to have similar capabilities, the user interface may be a bit different.  Feel free to use whichever "Developers Tools" you prefer.



### Identifying HTML5 elements

Remember that elements are the intangible parts of your Web page, which are described by the text in tags and are rendered on the screen of whatever device you're looking at your Web page with. The two things (the text code and the pixels on the screen) correspond to each other, but it's not always obvious which bit of the screen corresponds to which bit of text.

There are two opposite directions in which you might need to figure out in these two different things that both correspond to an element. You might have some HTML5 code that you've written and want to find out where on the Web page that code shows up. The other direction can be needed as well, i.e. given a particular part of the page, what part of your code produced it?

When you hover over an element in the DOM Explorer window in your browser developer tools, the corresponding element on the displayed page is highlighted:

It is also possible to go the other direction, i.e. click on a point on the displayed page and it will highlight the code in the source that corresponds to that element. This is helpful when you want to figure out where something came from and what might be affecting it's styling (size, color, font, any number of other characteristics).  To do that in your browser developer tools, use the DOM explorer pane and the "select element" option, you can also right click on the section on your page you want to inspect and select "Inspect element" which will bring up the developers tools and highlights the HTML element or code for that section on the page.

Check the video below to see how to do that with Microsoft Edge developer tools:

<video src="https://edx-video.net/W3CHTM502016-V013600_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@13f49d5521214d95bf39ba2cce51d40b/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Modifying HTML5 elements

Another handy feature of the developer tools is the ability to make temporary modifications to your code to try out different things and see what works the way you want it to.  When you have a visible element selected in the DOM explorer tab, you can make style changes in the "Styles" panel, or use the "Computed" panel to see the values for each property and how they were determined.

It's possible to change things a few different ways.  If you double click on an element in your HTML5 source code, you can change the source code.  For example you could click on an attribute to modify it or it's value, or you can change the type of the tag or even the contents of an element.

You can use this same approach to add a "style" attribute to a particular element, which should override any other settings, there is also an easier way to do that.  In the panel just to the right of the elements panel is the another panel with tabs including "Styles" and "Computed" and a few others.  Most of the time we'll want the "Styles" tab activated.  Once you do that, you can modify CSS properties of the current element by adding them to the "element.style" box at the top of the "Styles" panel.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/9567029b13454d0181141361837b2b96/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%4023e86990270640c284ab3748e3dc43a2">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/fb3a3f5292f058e8ad1d5ee2bfef9114/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/changestylevalue.png" style="margin: 0.1em;" alt="Screenshot of MS Edge showing modifying in the developers tools" title="Screenshot of MS Edge showing modifying in the developers tools" width=350>
  </a></div>
</div>

Just click in between the two curly braces on the "Inline style" rule at the top of the Styles panel.  After clicking you should see a little text entry box with which you can type property value pairs that will then effect the currently active element.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/9567029b13454d0181141361837b2b96/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%4023e86990270640c284ab3748e3dc43a2">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3b490286433826da4adeedc091090036/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/MSEdgeeditstyle.PNG" style="margin: 0.1em;" alt="Screenshot of MSEdge developer tools showing changing text color in developers tools" title="Screenshot of MSEdge developer tools showing changing text color in developers tools" width=350>
  </a></div>
</div>


It's important to know that any changes you make in the developer tools will have no effect on the original Web page. They only affect that particular instance of that page during that debugging session. If you navigate to another page and come back, you'll need to make the same changes again if you want to get back to where you were. It's not that easy to break the Web!


#### Live coding video: modifying elements

<video src="https://edx-video.net/W3CHTM502016-V009000_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@9b135f759c7b48cca1709d71291d0ed7/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Knowledge checks

Here are some questions for a self check to make sure you understand everything. These questions are not graded.

Use this screenshot for the questions below:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+2T2018/courseware/37f15009345846f391d7ac4d5bf06520/9567029b13454d0181141361837b2b96/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B2T2018%2Btype%40vertical%2Bblock%4023e86990270640c284ab3748e3dc43a2">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/4e013ef8d1453b878dd25544a4b2ff0f/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/week-4-kc-1take22.png" style="margin: 0.1em;" alt="screenshot of a web page" title="Screenshot of developer tools showing example" width=100%>
  </a></div>
</div>

1. 'id' of the element

    Given the picture above: one element on the right screen is highlighted and another has been modified...

    What is the id of the element that has been modified? (without any quotes)

    Ans: cumulus <br/>
    Explanation: The cumulus element has been selected, though the mouse is hovering over a different element which is highlighted on the page.


2. Width in pixels?

    Given the picture above:

    What is the width, in pixels, of the highlighted element? (write just the number of pixels, not the units)

    Ans: 144 <br/>
    Explanation: Like an x-y graph, x is horizontal and comes before y which is vertical, thus the pixels are written as width x height.


3. text-decoration property?

    Given the picture above:

    For the modified element, what value does the text-decoration property have? (no quotes)

    Ans: underline <br/>
    Explanation: The text decoration used on this element comes from the file 'third.css' from a rule on li elements.



### Activity - Debugger

Using your favorite browser, navigate to [Wikipedia.org](https://www.wikipedia.org/). Using the developers tools, change the title and header of the page to "My Wikipedia" and change the background to light green.

(Hint: use "Inspect" or "Inspect Element").

In another browser window, open up [Wikipedia.org](https://www.wikipedia.org/). Does it look like the one you've modified? Why or why not? Did you just break Wikipedia for the rest of the world?

Ans: the change on `<title>` only display on the browser tab not the contents. Meanwhile there is not header in text but in image.  We cannot change anything on image.  The question supposed is designed for old version of the page. When add background color to `<body>`, the page background color changed to the specified color.


## 4.3 Debugging and the CSS box model

### CSS box model

Before we get too far into debugging, it's helpful to understand a couple of things about CSS more deeply.

The placement of elements on a Web page can be fairly complicated. One of the most basic features that influence where things go on a Web page is the CSS Box Model. The Box Model governs 3 important spacing features of CSS.  We learned about margins previously as the space between elements.  There are two other similar notions, padding and borders.

Perhaps the best way to understand is with a picture.  All elements in an html document end up being treated as rectangles somewhere in the window. The content of each rectangle corresponds to the innermost rectangle in the image below.  Just outside the content is the padding.  This is kind of like an internal margin, meaning that it separates the contents from the border.  The border essentially traces the sides of the padding rectangle.

It's important to note that the border goes around the content and the padding.  There are sometimes visible things associated with an element that are not technically part of the content of the element.  One such example is the list item:

<ul>
<li style="border: 2px solid blue;">I'm in a blue box</li>
</ul>

The box does not include the bullets because it is outside of the content.  Sometimes when you see that it might be a bit confusing, especially because it also affects padding (which is inside the border).

<ul>
<li style="border: 2px solid blue; padding-left: 1rem;">padding-left: 1rem;</li>
</ul>

There is a list-style option , list-style-position, which can be used to include the bullet as part of the content:

<ul>
<li style="border: 2px solid blue; list-style-position: inside; padding-left: 1rem;">list-style-position: inside; padding-left: 1rem;</li>
</ul>

Now the bullet is inside the border, and padding affects the bullet as well as the text.

The border property has a lot more options than the padding or margin. Imagine using a pen to draw the edges of a rectangle.  You can choose how thick the pen is, and whether you draw a solid or dotted line. You can even choose how you go around the corners, whether it's a sharp turn or a more gradual circular shape.  All of these characteristics can be controlled by CSS properties, like border-width, border-style and border-radius.

While all of these border properties have default values, there are three that you'll see most often when specifying a border: border-width (the size of your imaginary pen), border-style (dashed, dotted,  solid, etc.) and border-color (the color of your pen).  In fact these are so commonly specified that there is a shorthand syntax to set all three in one line:

<p style="border: 5px solid blue;">&nbsp; &nbsp; border: 5px solid blue;</p>

There are many other shortcuts to learn, but this one is fairly common.  To draw a border you need to know the width, style and color.  There are defaults for these values, so you technically don't need to specify all of them, but it is the minimal info needed and is quite common.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/854f4a689894455ca4f375f15d0cbc42/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%407031c507bfe94604a6a98013af262725">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ebbf5b8bead6014e108c5be1df38d824/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/boxmodel.jpg" style="margin: 0.1em;" alt="text" title="caption" width=250>
  </a></div>
</div>
Illustration of CSS Box Model

The margin, as we learned earlier, specifies the position of the element relative to whatever is adjacent to it, either to the right or left, or top or bottom.  The margin is always transparent, and each side can be set individually.  The unique thing about the margin is that the values for any of the sides can be negative, even if that means that it overlaps with another element on the page.  This can be useful when you want to control where an element is placed on a page.  In the following pictures, the black rectangles encompass the content:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/854f4a689894455ca4f375f15d0cbc42/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%407031c507bfe94604a6a98013af262725">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d96a4d58ef317a49b577ad255625f642/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P25.png" style="margin: 0.1em;" alt="text" title="caption" width=150>
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/98a468c9a83a1abe03d657270e298813/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P26.png" style="margin: 0.1em;" alt="text" title="caption" width=150>
  </a></div>
</div>
0 margin positive and negative margins

On the left, we see three blocks with no margins between them. On the right are the same 3 blocks, but now block 2 has a positive margin-left, creating space between blocks 1 and 2.  Block 3 has a negative margin-left, causing its left side to overlap with block 2.

The border may be easier to comprehend because it is often visible, though it doesn't have to be.  Unlike the margin (or the padding), there are many more options controlling the size, shape, color and style of the border. You can even create a completely or partially transparent border, or you can match the color of the border to the color of the background, essentially rendering it invisible.  It's still there, though, taking up some space on the page and influencing the placement of elements displayed in the browser.  The width of the border controls it's size (thickness), so it only makes sense to accept numbers greater than or equal to 0.  What the browser does if the border-width is less than 0 is undefined and shouldn't be relied on.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/854f4a689894455ca4f375f15d0cbc42/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%407031c507bfe94604a6a98013af262725">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/4f1cd62aac6e1517eeb8f79fd616cdfb/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P27.png" style="margin: 0.1em;" alt="Various Borders" title="Various Borders" width=250>
  </a></div>
</div>


Here blocks 1, 2 and 3 all have borders with different widths, but the margins are zero.  There is no overlap, the borders are up against each other regardless of their width.  The contents have different positions, influenced by the width of the border.  If we were to make the borders invisible (fully transparent), the positioning of the contents would be the same.

Inside the border is the padding.  This controls the amount of space between the elements content and the border box (whether it's visible or not).  If you have no padding, then the contents of the element (maybe text or image) would be right up against the border, which could be awkward if you have a visible border.

Like the margin and the border, all four sides can be independently set.  The background of the padded area matches the background of element, so the effective visible size of the element includes the padding.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/854f4a689894455ca4f375f15d0cbc42/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%407031c507bfe94604a6a98013af262725">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7e12176ec28a70a8a12e6e74cf76e095/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P28.png" style="margin: 0.1em;" alt="Padding demo" title="Padding demo" width=250>
  </a></div>
</div>


Here we've got a thin border directly around the content to delineate where the content ends and the padding begins.  Again, the contents are affected by the width of the padding, but now the background of the padding is the same as the background of the content.  This makes it look more like the contents have been expanded.  If we add a thin border to these, we see that the padding is reflected by empty space between the contents and the border:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/854f4a689894455ca4f375f15d0cbc42/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%407031c507bfe94604a6a98013af262725">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/fb8053eecf3d50dcc758f8bbd60e304f/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P29.png" style="margin: 0.1em;" alt="Padding with borders" title="Padding with borders" width=250>
  </a></div>
</div>


All of these can have a width of 0, which is equivalent to not having them, thus 'margin: 0;'  is the same as 'margin: none;'.  Each can be controlled individually with relative or absolute lengths.  While the padding and borders require non-negative widths, margins can be either positive or negative.

Using these three settings in combination provides quite a bit of flexibility in terms of spacing and drawing of borders.  If you have padding and a visible border, you can control how close the border comes to the contents.  By setting the margin you can control how close the border comes to surrounding elements.  You can even give your border rounded corners using the border-radius setting:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/854f4a689894455ca4f375f15d0cbc42/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%407031c507bfe94604a6a98013af262725">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e4d431fbcb77fea2e180465a12551c68/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P30.png" style="margin: 0.1em;" alt="Rounded borders" title="Rounded borders" width=250>
  </a></div>
</div>



### Debugging with the box model

In any browser's debugger, you will see a box model diagram. It looks like this:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/854f4a689894455ca4f375f15d0cbc42/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%407031c507bfe94604a6a98013af262725">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/063b584da882baac3e39e088c4c9dc80/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/Screen_Shot_2016-03-08_at_8.19.27_PM.png" style="margin: 0.1em;" alt="image of a CSS Box Model" title="image of a CSS Box Model" width=350>
  </a></div>
</div>


This is an example of a diagram of the box model information for a selected element.  
The innermost box gives the dimensions of the element, outside of that is the padding, then the border around which is the margin.  On each side of each corresponding rectangle is the width in pixels of that side, with "-" when it is 0 (essentially non-existent).  Also, when you hover over one of the rectangles, that portion of element is highlighted on the rendered page, so you can see exactly where the margin, the border, the padding and the element are.

So, in the example above:

+ the centered blue box corresponds to the size of the inspected element: width is 536 pixels and height is 118 pixels
+ padding is only defined by padding-left which value is 40 pixels
+ there is a border of 5 pixels on each side
+ margin-left and margin-right are undefined (default value is 0 pixel)
+ margin-top and margin-bottom are equal to 16 pixels



### Box model

<video src="https://edx-video.net/W3CHTM502016-V009100_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@0baf12106ba64b5ba01835a9d26c7732/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Knowledge checks

<div>
<h3 style="margin-left: -5rem; background: lightblue; z-index: -100;">What is my margin?</h3>
</div>

1. Likely setting?

  The blue banner above should say "What is my margin?", though some of it may be obscured.

  Assuming the margin-right, margin-top and margin-bottom are 0, what is the likely setting for margin-left? (choose the best answer)

  1. 5%
  2. 5rem
  3. -5rem
  4. 0
  
  Ans: 3 <br/>
  Explanation: Since the box is further to the left than it should be (likely overlapping another element) margin-left must be negative, and there's only one answer for which that's true.


2. Which of these would you set?

  If you wanted to move the banner to the right instead of the left, which of these would you set? (choose the best answer)

  1. margin-bottom:
  2. margin-left:
  3. margin-top:
  4. margin-right:

  Ans: 2 <br/>
  Explanation: Changing the right margin essentially changes the width of the element, but changing the left margin changes where it starts. To 'move' the element either left or right, you need to set the left margin.




### Activity - Birds

Let's see what we can do to improve the look of the following [Web page](src/4.3.5-BirdsOrigin.html) (this [CodePen](https://codepen.io/w3devcampus/pen/ybvXqd)) showing various sea birds common to the San Francisco Bay Area.

First, the pictures and names are a little cramped, it would be good to have some space there. It would also be helpful to have some vertical space between the pictures. Finally, it would look nicer with some sort of frame around the pictures. We'll start by examining the box model measurements of the images in the browser's debugger.

In the case of our birds page, when we select one of the images: the box model diagram shows us that margin, padding and border are all 0:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/854f4a689894455ca4f375f15d0cbc42/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%407031c507bfe94604a6a98013af262725">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f3cb82f487e8498fcf2a11aa344e5e61/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/box-model-0.png" style="margin: 0.1em;" alt="Box model showing an inspecting element of 500.00 x 332.812" title="Box model showing an inspecting element of 500.00 x 332.812" width=350>
  </a></div>
</div>


Improvement steps:
1. First, we'll add some space between the names and pictures of each bird.  For that we'll want to use a margin, particularly on the left:

  ```css
  img {margin-left: 1rem;}
  ```

2. To increase the vertical space, we can add a margin on the top of each img:

  ```css
  margin-top: 3rem;
  ```

3. The placement of the words at the very bottom of each picture is a bit awkward as well.  We can improve that by moving each image down using a negative bottom margin:

  ```css
  margin-bottom: -1rem;
  ```

4. Next, we can add a frame around it.  Using a border, provide a simple frame around each picture:

  ```css
  border: 5px solid navy;
  ```

4. Finally, to make the border a little more "frame" like, we can add some padding to separate the border from the image itself:

  ```css
  padding: 5px;
  ```

Though not perfect, the Web page looks a bit better now, with more space and a frame around each picture! See the [resulting](src/4.3.5-BirdsResult.html) CodePen.



### Activity - Rectangles

Create a simple Web page with some rectangles distinguished by their background color so you can see them.  You can create the rectangles using spans and/or divs, and explicitly setting the width and height.  They need to have some content or else they'll be of size 0, so you need to put some text or at least an &nbsp; inside, but then you should be able to adjust the height and width using CSS.

In your browser's debugger, try modifying the padding, border and margin settings using the arrow keys to modify numerical values so you can see how the changing number affects the element. Be sure to try border-radius and see if you can create a circle or oval.  Be sure to try out some other border attributes like style and color.  If you're feeling brave, you could even try [border-gradient](https://css-tricks.com/examples/GradientBorder/).

For example, these lines of codes draw 2 rectangles:

```html
<!DOCTYPE html>
  <html lang="en">
 
    <head>
      <meta charset="UTF-8">
      <title>Activity - Rectangles</title>
      <style>
        #first{
          background-color: blue;
          width: 250px;
          height: 100px;
         }
        #second{
         border: 5px solid red;
         width: 50px;
         height: 200px;
         }
      </style>
   </head>
 
   <body>
      <div id="first"></div>
      <div id="second"></div>
   </body>
</html>
```

... and the associated [CodePen](https://codepen.io/w3devcampus/pen/qPNYbJ) gives the resulting displayed image:

[Sample Result code](src/src/4.3.6-Rectangles.html)



## 4.4 Debugging CSS precedence

### CSS precedence



### Debugging CSS precedence



### Cloud images



### Shrinking text



### Recipe project - Module 4



### Recipe Project - Module 4



## 4.5 Exercises - Module 4

### CSS box model (1-14)



### CSS precedence (15-17)



### Debugging (18-25)





