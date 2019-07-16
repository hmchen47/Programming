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
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ebbf5b8bead6014e108c5be1df38d824/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/boxmodel.jpg" style="margin: 0.1em;" alt="Illustration of CSS Box Model" title="Illustration of CSS Box Model" width=250>
  </a></div>
</div>


The margin, as we learned earlier, specifies the position of the element relative to whatever is adjacent to it, either to the right or left, or top or bottom.  The margin is always transparent, and each side can be set individually.  The unique thing about the margin is that the values for any of the sides can be negative, even if that means that it overlaps with another element on the page.  This can be useful when you want to control where an element is placed on a page.  In the following pictures, the black rectangles encompass the content:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/854f4a689894455ca4f375f15d0cbc42/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%407031c507bfe94604a6a98013af262725">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d96a4d58ef317a49b577ad255625f642/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P25.png" style="margin: 0.1em;" alt="0 margin" title="0 margin" width=150>
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/98a468c9a83a1abe03d657270e298813/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P26.png" style="margin: 0.1em;" alt="positive and negative margins" title="positive and negative margins" width=150>
  </a></div>
</div>


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
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/063b584da882baac3e39e088c4c9dc80/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/Screen_Shot_2016-03-08_at_8.19.27_PM.png" style="margin: 0.1em;" alt="image of a CSS Box Model" title="image of a CSS Box Model" width=250>
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
<h3 style="margin-left: -3rem; background: lightblue; z-index: -100;">What is my margin?</h3>
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
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f3cb82f487e8498fcf2a11aa344e5e61/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/box-model-0.png" style="margin: 0.1em;" alt="Box model showing an inspecting element of 500.00 x 332.812" title="Box model showing an inspecting element of 500.00 x 332.812" width=250>
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

As we learned in the last module, in order for the computer to decide which of several rules may apply to a given element in a particular context, there is a well defined "precedence" to define which rule should apply. Theoretically, we should be able to always figure out which rule applies by using the precedence rules, but in practice, it can be quite complicated, especially when conflicting rules are in different .css files.

Nevertheless, that can cause problems when you have different rules that could apply to the same element. Consider the [example](src/4.4.1-Precedence.html)

Looking at the style rules we see there are three different possibilities for the size and color of an `<h1>` element. In this case the application of the rules seems pretty intuitive. The outermost heading is neither in a Article or a Section, so it is blue and largest of the three. The one that's in the Article, but not in the section is black and of medium size.

Finally, the heading in the section is the smallest and shows up as grey.

Your intuition may be thinking along these lines - "section h1" is more specific than "article h1" or "h1", and therefore it takes precedence resulting in smaller gray text.  However, when you re-arrange the rules you get a different [result](src/4.4.1-PrecedenceH1.html).

What happened? To answer that question, we'll turn to the browser's debugger.



### Debugging CSS precedence

This lesson is using developers tools provided by the Chrome browser. In the right panel of the debugger there are several tabs, such as "Styles" and "Computed".  Both of these are helpful in sorting out where a particular style setting is coming from.  We saw in a previous section that we can add or change CSS settings in the "Styles" panel, however, there is much more information there.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/4bc228e91d0f414eb80c9bdcf3fdf356/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%401e671f9dbfc44419a801bb40d931d8f0">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/feea62b8dd00860ce4db9657d0f31dcd/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P1-2.png" style="margin: 0.1em;" alt="Styles in the debugger" title="Styles in the debugger" width=450>
  </a></div>
</div>


There is a sequence of the panels under "Style" that helps understand just where a particular CSS rule is coming from.  Starting at the top, we have rules that apply specifically to the currently active element.  In fact changes in this top panel are mirrored as settings in the style attribute of the element:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/4bc228e91d0f414eb80c9bdcf3fdf356/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%401e671f9dbfc44419a801bb40d931d8f0">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/08c82f54e296b1d5fea38cabfd707738/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P2-2.jpg" style="margin: 0.1em;" alt="Modifying style in the debugger" title="Modifying style in the debugger" width=450>
  </a></div>
</div>


Under that there are more panels which show where CSS properties for other elements come from.  Under the top panel, which corresponds to inline style settings, we find properties for this element that came from the rules with the selector "article h1".  This may seem odd at first because the h1 element that we're examining is inside a section, so you'd think that the "section h1" selector would take precedence.

If we keep going down, we find the overridden rule that applies to all h1 elements, and then there are the two grayed-out section with the label "user agent stylesheet".  These are basically the defaults, the values that the browser will use if nothing else is specified.  Any rule you provide should override the corresponding rule in the user agent stylesheet.

Back to our quandary, why does "article h1" take precedence over "section h1"?  Let's take a look at the first version we tried, before rearranging, which did what we wanted:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/4bc228e91d0f414eb80c9bdcf3fdf356/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%401e671f9dbfc44419a801bb40d931d8f0">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0ae9484396dfbafe5d2bb259b2dcac44/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P3-2.png" style="margin: 0.1em;" alt="Working version in debugger" title="Working version in debugger" width=450>
  </a></div>
</div>


Here we see just the opposite of what we saw before, now "section h1" takes precedence over "article h1".  What's going on?

Our intuition in this case is deceiving us.  We think of section as being more specific than article, but that's just because we've organized it that way.  In fact, we could decide that a section consists of multiple articles, then we'd want the opposite behavior.

As far as precedence calculations are concerned, though, the computer sees "tag-type tag-type", which is more specific than just one "tag-type", but no more specific than any other "tag-type tag-type" combination.  Since "article h1" and "section h1" are of equal precedence, the tie is broken by whichever rule came last.  When we rearrange the rules, we change which of the two comes last, thus causing the change in the section headers.

We could fix it by just making sure things are in the right order (which is important) but a more robust solution might be to make use of the fact that the way we're using `<section>` in fact is more specific than `<article>`.  We can make this explicit by changing the selector to "article section h1", so that now the smaller, lighter color will be used only on a section that is inside an article, which is really what we want:




### Cloud images

We're working on a Web page about clouds in the CodePen below, and we have some beautiful pictures we'd like to use: one for the top of the page, and others as examples of different types of clouds.  We include the pictures but the result is unwieldy.

[Sample Code](https://codepen.io/w3devcampus/pen/ybqbwJ)

When you see the pictures, the text is so small it's unreadable.  Clearly we have a solution for this.  We can just specify the width of <img> elements.  We can use the debugger to try different sizes, modifying it in the "Styles" panel and we decide on this:

```css
img {
   width: 10rem;
}
```

Giving a much [more reasonable page](src/4.4.3-Cloud2.html).

So far so good, but we want our top image to be a bit bigger without changing the other images.  Recall  that an <img> tag includes a width attribute, so we can special case this image accordingly in the HTML code:

```css
<img alt="Clouds" width=500 src="images/clouds.jpg">
```

We look at our page again, and it hasn't changed!  Time to try the debugger again.


#### Debugging image size

We open up the debugger and choose the `<img>` tag corresponding to our first picture, then we see this in the Styles section:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/4bc228e91d0f414eb80c9bdcf3fdf356/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%401e671f9dbfc44419a801bb40d931d8f0">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0ee32d3cac4d313f1c9e641721d3f26a/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/clouds-1.png" style="margin: 0.1em;" alt="Img width precedence in debugger" title="Img width precedence in debugger" width=250>
  </a></div>
</div>


The specialized width setting that we added as an img attribute isn't quite the same as setting the style.  Any style setting for the img width will take precedence over the attribute setting, so our img settings intended for the other images will change that one too.  You could fix this by adding an inline "style" setting, but that's generally discouraged.  It's better to sit back and think for a moment.  The images below are in a list, and we want smaller pictures there so we can scan the list easily.  The banner picture at the top should be big for more visual impact.  One reasonable way to address this would be to special case the smaller pictures, and use a larger width by default.  This would recognize that we really want small images when they are list elements, otherwise they should be bigger.  So we can change our code like this:

```css
img {
   width: 25rem;
}
li img {
   width: 10rem;
}
```

That looks better: [Result Code](src/4.4.3-Cloud3.html)



### Shrinking text

For this section you can play with the [CodePen](http://codepen.io/w3devcampus/pen/wdxegK) below. The main content is an outline for an essay and it should look something like [this](src/4.4.4-Shrink.html).

As with the cloud pictures, we want the listed items a bit smaller than the regular text, so we add this styling:

```css
section {
  font-size: 24px;
}
section h1 {
  font-size: 28px;
}
li {
  font-size: 0.5em;
}
```

The outermost level is fine, the next level is almost readable but the innermost level is ridiculously small.  Let's check what's wrong in the debugger.


#### Computed tab

Looking into the style settings in the chrome browser debugger, at first glance we don't see anything unusual.  The font-size is .5em as expected.  One odd thing is that below the user agent stylesheet panels is the over-ridden font-size setting identical to the current one, i.e. .5em on `<li>` elements.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/4bc228e91d0f414eb80c9bdcf3fdf356/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%401e671f9dbfc44419a801bb40d931d8f0">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/957741ff82f21e9c2fd51da53e4e1aef/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P21.png" style="margin: 0.1em;" alt="Debugging font-size" title="Debugging font-size" width=450>
  </a></div>
</div>


The styles panel doesn't tell us a lot about the actually font-size in absolute terms.  To determine that we can use the "Computed" tab. 

The "Computed" tab contains the values of all the CSS properties that apply to the current element.  There are a lot of them, and they're listed in alphabetical order.  Since the computer considers the character '-' as coming before 'a' in the alphabet, the first thing you'll see is a long list of properties starting with '-webkit'.  We're going to scroll down past those to "font-size" which reveals this:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/4bc228e91d0f414eb80c9bdcf3fdf356/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%401e671f9dbfc44419a801bb40d931d8f0">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a9e8e8f2500f14bd7d7232bb7f1aa78e/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P22.png" style="margin: 0.1em;" alt="Debugging font-size" title="Debugging font-size" width=250>
  </a></div>
</div>


This tells us that the font-size on the innermost list item is only 3px.  No wonder it's unreadable!

When we click on the triangle we can expand the details on font-size, which makes a little more clear what's going on.  We see that the font-size on the body is 24px, but there are several repetitions of the li .5em.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/4bc228e91d0f414eb80c9bdcf3fdf356/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%401e671f9dbfc44419a801bb40d931d8f0">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/88e9ed6b414690f10dd08d5d21819359/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/P39.png" style="margin: 0.1em;" alt="Computed tab for font-size" title="Computed tab for font-size" width=250>
  </a></div>
</div>


If we look at the next outer list item, we see that the font-size is 6px, and the one outside of that is 12px.  This doubling makes it clear what's happening.  Each nested `<li>` element has a font-size 1/2 the size of its parent, because the em unit is relative measurement, depending on the current font-size.

Now that we know what's happening, we can fix it in a few different ways.  We could use an absolute unit like px or pt, but a better solution would be rem.  This would make the size relative to the html font-size (the default font-size for the page), not to it's surroundings.



### Recipe project - Module 4

We are now going to do some more "beautifying" of our Web page using what we've learned in the debugger and the CSS box model to figure out where and what we need to change to tighten things up a bit and add a little more flair.

Try to make changes to get something like [this](src/4.4.5-Project.html).

Use the debugger to experiment with settings of margins, padding and borders, to figure out what needs to change to eliminate some of the gaps between elements and the side of the window and frame the images.

If you'd like to see what we did for the module 3, you can find it [here](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7c96010a1f16e016801677c17f103d1a/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/recipe-project-week-3v.zip) or in the CodePen below.

[Response Code](src/4.4.5-Recipe.html)



### Recipe Project - Module 4

<video src="https://edx-video.net/W3CHTM502016-V010900_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@5eda5d2e0eba4c9884c6b470c6155975/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


## 4.5 Exercises - Module 4

### CSS box model (1-14)


1. Rounded corners

  What CSS property would you set to create rounded corners on a border?

  Ans: border-radius or border-radius: <br/>
  Explication: By default border-radius is 0, making the border a sharp rectangle. Values greater than 0 provide rounded borders. The higher the number, the more rounded the corners are..


2. Too close for comfort

  If an image is too close to the text next to it, what property is best to fix the problem?

  Ans: margin or margin: or margin-left or margin-right or margin-top or margin-bottom or margin-left: or margin-right: or margin-top: or margin-bottom: <br/>
  Explication: Margin controls spacing between elements. If your image element has a border, only margin will separate that border from whatever is next to it.


3. Move it!

  If you wanted to move an element up 10px (relative to the top of the page) by adjusting the margin, which side of the margin would you set?

  Ans: margin-top or margin-top: or top <br/>
  Explication: To move it up without moving it left or right, we need to isolate its top margin, and the property for that is margin-top.


4. Border shorthand

  ```css
  border: 1px solid red;
  ```

  True or False? The code above is a shorthand way to set border-width, border-style and border-color.

  Ans: True <br/>
  Explication: This shorthand is often used because it contains the minimal information needed to create a border.


5. Interchangeable?

  True or False? Margin and padding are interchangeable.

  Ans: False <br/>
  Explication: Margin governs the spacing relative to other elements outside the border while padding is about the spacing of the contents relative to the inside of the border.


6. Margin color

  True or False? 'margin-color' is the correct property to set to change the color of the margin.

  Ans: False <br/>
  Explication: Margins are always transparent and there is no 'margin-color' property.


7. Margin values

  Which of the following are valid margin values? (select all that apply - 3 correct answers!)

  1. 3px;
  2. -3em;
  3. 3rem;
  4. 3ft

  Ans: 123 <br/>
  Explanation: Feet (ft) is not a valid unit in CSS.


8. Left move

  Which of the following would move an element 12 pixels to the left?

  1. margin-left: -12px;
  2. margin-left: 12px;
  3. margin-right: -12px;
  4. margin-right: 12px;

  Ans: 1<br/>
  Explication: Assuming that you're working with a left-to-right language, language, changing the left margin will adjust the placement of the element, while changing the right margin will affect what comes after that element.


9. It doesn't move!

  Suppose you're debugging an element on your page. You notice that if you increase padding-left, your content will move to the right, but if you increase padding-right, it doesn't move. Why?

  1. The text is right aligned (text-align: right) so space added to the right affects the contents
  2. The text is left aligned (text-align: left) so space added to the left affects the contents
  3. The text is right aligned (text-align: right) so space added to the left affects the contents

  Ans: 2<br/>


#### Reference image 1A

Use this image for the following 3 questions (10, 11 and 12):

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+2T2018/courseware/37f15009345846f391d7ac4d5bf06520/32042e5f81d146bca42c442bae4bbb97/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B2T2018%2Btype%40vertical%2Bblock%407f4f510d425e4a08a781f9911be2c29b">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5bf305f7bed5052a9f6bb0b905b21b7c/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/quiz-1a.png" style="margin: 0.1em;" alt="This is the picture of a debugger panel highlighting the style of ul. It also shows the box model with the following parameters: margin-top and margin-bottom are 16px large ; there are no borders, the padding-left is 40px. The size of the inspected element is 100 x 180 pixels." title="Fig. 1A" width="400">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0ef9039eacfcff0986158741b9105d38/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/quiz-1b.png" style="margin: 0.1em;" alt="This is the resulting image of the example showing 3 images of the same size in a bulleted list (ul). The image in the first bullet is inspected and it displays the following info.: img 100px x 56px" title="Fig. 1B" width="150">
  </a></div>
</div>

10. Which CSS rule?

  In reference image 1A above, assuming the original image files are all different sizes, can you guess which CSS rule is used?

  1. body {width: 100px}
  2. img {width: 100px}
  3. ul {width: 100px}
  4. li {width: 100px}

  Ans: 2 <br/>
  Explication: We can see from the second image that all the image widths are 100px, while setting the others would not restrict the image size.


11. Padding-left

  What is the padding-left on the ul element?

  1. 40px
  2. 40pt
  3. Cannot tell from the info provided
  4. 16px

  Ans: 1 <br/>
  Explanation: From the highlighting in the left panel, ul is currently selected. <br/>
  From the box model diagram, we see that the padding-left is 40. The units in that diagram are in px, not pt.


12. Height of each element

  In reference image 1A, assuming there is no padding, margin or border on the li elements, what is the height of each element?

  1. 180px
  2. 60px
  3. 56px

  Ans: 2 <br/>
  Explanation: From the box-model diagram, the contents of the ul element has a height of 180px. Since there are 3 li elements with no spacing around them, they must be 60px.



#### Code for the following 2 questions (13 and 14)

Reference code 1B

Around the second list item below, 'Oranges', there are: a 2px border, paddings of 0 or 20px, and margins of 0, 20 or -20px.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+2T2018/courseware/37f15009345846f391d7ac4d5bf06520/32042e5f81d146bca42c442bae4bbb97/2?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B2T2018%2Btype%40vertical%2Bblock%400d180ba4472d4efbb4ee4205b1e39c35">
    <img src="img/m04-01.png" style="margin: 0.1em;" alt="Reference code 1B" title="Fig. 1B" width="700">
  </a></div>
</div>

13. Margin settings (choose the best answer)

  Looking at padding and the margin, which settings for the margins of list item 2, Oranges, are consistent with reference code's result 1B above?

  1. margin-left: 0; margin-right: 0; margin-top: -20px; margin-bottom: 0;
  2. margin-left: 0; margin-right: 0; margin-top: 0; margin-bottom: -20px;
  3. margin-left: 0; margin-right: 0; margin-top: 20px; margin-bottom: 0;
  4. margin-left: -20px; margin-right: 0; margin-top: 0; margin-bottom: -20px;

  Ans: 2 <br/>
  border: 2px solid red; padding: 20px; padding-left: 0; padding-top: 0; margin: 0; margin-bottom: -20px; <br/>
  Explanation: While you can't tell what the top and right margins are, you know the bottom must be negative and the left 0, and there's only one answer in which that is true. <br/>
  The bottom of the rectangle has been pushed down so margin-bottom must be negative, i.e. pulling away from it's normal placement. When you account for the 2px border, the left side lines up with the other elements, so its margin must be 0.


14. Padding settings (choose the best answer)

  Looking at padding and the margin, which padding settings for list item 2, Oranges, are consistent with reference code's result 1B above?

  1. padding-left: 20px; padding-right: 20px; padding-top: 0; padding-bottom: 20px;
  2. padding-left: 0; padding-right: 20px; padding-top: 0; padding-bottom: 20px;
  3. padding-left: 0; padding-right: 0; padding-top: 20px; padding-bottom: 20px;
  4. padding-left: 20px; padding-right: 0; padding-top: 0; padding-bottom: 20px;

  Ans: 2 <br/>
  border: 2px solid red; padding: 20px; padding-left: 0; padding-top: 0; margin: 0; margin-bottom: -20px; <br/>
  Explanation: We know the left and top must be 0 because those borders are right up against the content and there is only one choice in which that is true.




### CSS precedence (15-17)


15. What color?

  ```css
  html, body { color: blue;  }
  p          { color: black; }
  #first     { color: green; }
  ```

  ```html
  <p id="first" style="color: red">What color am I?</p>
  ```

  Given the code above, what would be the color of the text in the paragraph?

  1. red
  2. black
  3. green
  4. blue

  Ans: 1 <br/>
  Explanation: The more specific the rule, the higher the priority, so the inline style elements has the highest priority, making it red.


16. So tall

  Given the following CSS rules: (Enter number of pixels, but don't write any units, just the number)

  ```css
  box-sizing: content-box; 
  border: 3px solid black; 
  padding: 5px; 
  padding-top: 10px; 
  height: 100px; 
  background: red;
  ```

  When it is rendered in the browser, how tall will the red part be?

  Ans: 115 <br/>
  Explanation: The content and the padding will have a red background. Since 'height' is the height of the content without padding, border or margin, when you add in the vertical padding, 10 for top and 5 for bottom, you get 115 pixels.


17. Padding values

  Which of the following are valid padding values? (Select all that apply - 3 correct answers!)

  1. 3px;
  2. -3em;
  3. 3in;
  4. 3mm;

  Ans: 134 <br/>
  Explanation: While it is possible to have negative margins, it is not possible to have negative padding.



### Debugging (18-25)


18. Finding CSS rules

  True or False? While it’s possible to examine html elements in the debugger, it is impossible to see CSS Rules.

  Ans: False <br/>
  Explication: You can definitely see CSS rules, either by looking at the source or by using the right pane (the one with tabs like 'Rules', or 'Styles' or 'Computed')


19. CSS properties

  True or False? You can use the debugger (or inspector) to see the computed CSS properties, and you can also see rules that have been overridden by more specific rules.

  Ans: True <br/>
  Explication: The debugger has a "Computed" tab which shows the computed value of each property, and under the "Styles" or "Rules" tab, overridden rules are listed with strike-through lines through them.


20. Debugger

  Which of the following can be modified in the debugger? (Select all that apply, there are 4 correct answers!)

  1. the color of text on your Web page
  2. background image of your Web page
  3. background of your desktop on the machine you're using
  4. text content of an element
  5. class and id attributes

  Ans: 1245


21. Multiple elements selection

  True or False? Using the settings in the right pane, it is possible to select multiple different, unrelated elements and change them all at once.

  Ans: False <br/>
  Explanation: While you cannot select an arbitrary set of elements, you can modify settings of groups of elements indicated by tag or class.


22. Color settings

  True or False? When in the debugger, if you change color settings for a Web site you are visiting, other people will see the changes, allowing you to effectively hack any Web site.

  Ans: False <br/>
  Explication: While you can make changes that will be visible in your debug session, they won't be reflected elsewhere, even in other browser windows on the same machine.


23. Named colors

  True or False? Using the debugger, I can find all the named colors that start with 'c'.

  Ans: True <br/>
  Explication: Thanks to completion of property names and values, if you modify a color, typing 'c' will show all of the color choices that start with 'c'.


24. CSS changes

  True or False? I can use the debugger to make CSS changes, but I can't otherwise affect HTML elements.

  Ans: False <br/>
  Explication: Making changes in the larger left pane allows me to edit attributes, reorder elements, add or delete elements or make arbitrary changes to the HTML code.


25. Inline style settings

  True or False? It is possible to override style settings associated with a specific tag type and 'id', like 'article#first', using the 'styles' tab in the rightpanel.

  Ans: True <br/>
  Explication: Modifications in the top box of the Styles pane are equivalent to (and mirrored by) inline style settings, which take precedence over other CSS settings.





