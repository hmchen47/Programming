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



### Debugging with the box model



### Box model



### Knowledge checks



### Activity - Birds



### Activity - Rectangles



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





