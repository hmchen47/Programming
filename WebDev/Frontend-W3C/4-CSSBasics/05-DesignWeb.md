# Module 5: Designing your Web site for your audience

## 5.1 Introduction

### Welcome to Module 5

#### Video: welcome to Module 5

<video src="https://edx-video.net/W3CCSS0I2016-V005100_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@ff57fabe3b184e809f8cb9b31a2d3bb7/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


#### In this module, we'll...

+ Learn how to apply basic design principals based on the context of your HTML elements
+ Explore CSS and HTML's accessibility features and how you can design your page to accommodate a diverse audience
+ Introduce you to features to help internationalize your page and make it easier for those viewing it in different languages
+ Discuss the lessons learned from historical Web design trends and give you the new tech we use instead
+ Meet the newest fashions in Web design to help you give your Web pages a modern look and feel



### The importance of design

#### Video: the importance of design

<video src="https://edx-video.net/W3CCSS0I2016-V005200_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@05f1d31c3812439f84c6020adf4c1c8b/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


#### Web stats

Numerous studies have been done to determine exactly how important Web design is. Here are a few interesting stats to guide you:

+ 38% of people will stop engaging with a website if the content/layout is unattractive
+ 2 out of every 3 minutes spent on the Web are via a mobile device



### CSS best practices

You will find below an excerpt of CSS best practices (see the [full slide set](http://fantasai.inkedblade.net/style/talks/best-practices/#title)) that were written by Elika J. Etemad (also known as [fantasai](http://fantasai.inkedblade.net/)). Elika is an expert on the [W3C CSS Working Group](http://www.w3.org/Style/CSS/) (since 2004!) and a longtime contributor to the Mozilla Project. In addition to editing many of the CSS3 specifications, she’s worked on layout engine testing and development for Gecko and managing the CSS test suites at W3C.

#### Executive summary

+ __Logical source order__: The order of the HTML content should make sense even without the CSS: for accessibility, mobile optimization, device adaptability, and long-term maintainability.
+ __Liquid layouts and relativity__: Use smart relative sizing: to optimize layouts while minimizing media query code forks.
+ __Media queries__: Adapt to screen size changes; get font size adaptation free by using `em`s.
+ __Prevent zombie code__: Dead code may come alive as CSS changes. Delete it before it does, and ruins your layout.
+ __Test in multiple browsers__: Your favorite browser is not always right.
+ __Don't use proprietary features!__ Keep the Web open to everyone! Don't rely on the latest -WebKit- invention.
+ __Turn off CSS__: A well-coded page will be understandable without it.


#### Foundations

+ Indent your code for readability ease
+ Learn how to code CSS before relying on frameworks (such as Bootstrap, etc.)
+ __Separate content and style__
  + Use semantic markup, ie., "classes for meaning, not for show".  
    The following article is helpful to understand this concept: [Meaningful CSS: Style Like You Mean It](http://alistapart.com/article/meaningful-css-style-like-you-mean-it) (Tim Baxter, May 2016 - A list apart). It is also fully described in the [HTML5&CSS Fundamentals course](https://www.edx.org/course/html5-css-fundamentals-w3cx-html5-0x).
  + Use `<table>` for tabular data: don't use tables for layout, but if your content is tabular like a catalog, a calendar, or a price list, then the table element is the correct markup.
+ __Linearized logical source order__
  + The order of the HTML content should make sense even without the CSS.  
    Benefits are numerous as it _works best_:
    + for long-term site maintainability
    + for mobile
    + for accessibility
    + as a foundation for device adaptation (media queries)
+ __Linguistic variations__: set the language correctly for better typography (see the section entitled "[why Internationalization is important](https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+1T2017/courseware/12e8f1585d88470e95f54cf0ff6a1a00/ce75a56f15a940fe8b10d4e1650d85c0/3)")


#### Testing

+ __Test without CSS__: turn off CSS, and if the page makes no sense, fix your markup.
+ __Test in multiple environments__:
  + Resize the window
  + Zoom the text
  + Try a mobile browser
  + Navigate by keyboard
+ __Test in multiple browsers__: remember that just testing in Chrome does not work for everyone!  ;)


#### Adaptability

+ __Media queries__: set media query breakpoints in `em` or `ch`, not always in `px`.
+ __Liquid layouts and relativity__: what is your sizing based on?
  + Containing block size? → Use percents.
  + Viewport size? → Use viewport units: `vw`, `vh`, `vmin`, `vmax`
  + Font height? → Use `em` or `rem`.
  + Font pitch? → Use `em` or `ch`.
  + Content size? → Use `auto` or `min-content`/`max-content`.
  + Combination of the above? → Use the appropriate layout formulas: `flex`, `min-width`, `max-width`, etc.

Absolute units are usually the wrong answer.


#### Defensive Coding

+ `!important` means never override- to use with caution
+ Use `!important` to define overriding rules, not for fixups
+ Duplicate selectors if you need to increase specificity, or
+ Simplify selectors if you need to decrease specificity
+ __Don't over-escalate__: understand your code, and don't overkill.  
  For example, avoid:
  + `z-index: 9999999999999999999999999999999999999;`
  + `position: absolute; left: -10000000000px`
+ __Drop dead code__: you tried something and it didn't work? Delete it right away!
+ Code to Standard
+ Don't rely on proprietary extensions
+ Don't use experimental features in production or commit to keeping up-to-date.
+ Provide fallbacks / use @supports.



### The W3C CSS WG

The W3C CSS Working Group
The CSS Working Group (Cascading Style Sheets Working Group or CSS WG) is a working group created by the W3C in 1997 to tackle issues that had not been addressed with CSS level 1. The number of members reaches 125 in April 2017!

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/6c9058a29dc5493fbb43332c6bc3b550/2?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40video%2Bblock%4005f1d31c3812439f84c6020adf4c1c8b">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/399b45274a039620a540a7faca602183/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/CSSWG-TPAC16.jpg" style="margin: 0.1em;" alt="The CSS WG meeting in Lisbon, November 2016. The working group is co-chaired by Rossen Atanassov and Alan Stearns. (Photo credit: Marie-Claire Forgue)" title="Photo of the CSS Working Group members at TPAC 2016" width="350">
  </a></div>
</div>


The CSS WG members are working on a [whole range of specifications](https://www.w3.org/Style/CSS/current-work), but their core document is [CSS snapshot 2018](https://www.w3.org/TR/css-2018/). This document collects together into one definition all the specs that together form the current state of Cascading Style Sheets (CSS) as of 2018. The primary audience is CSS implementers, not CSS authors, as this definition includes modules by specification stability, not Web browser adoption rate.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/6c9058a29dc5493fbb43332c6bc3b550/2?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40video%2Bblock%4005f1d31c3812439f84c6020adf4c1c8b">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/1d59dc5bc30f26cb9e6cab6afe0d6516/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/CSS-WG-TPAC2018.jpg" style="margin: 0.1em;" alt="he CSS WG meeting in Lyon, France, October 2018. The working group is co-chaired by Rossen Atanassov and Alan Stearns." title="Photo of the CSS Working Group members at TPAC 2018" width="350">
  </a></div>
</div>


## 5.2 The basics of design

### Applying basic design principals

Often it's hard to pull apart the pieces of a design that are "good" or "bad", most of that is subjective. Instead, it's better to think of individual pieces of a design as "effective" or "ineffective" according to the demographic and the task they are trying to achieve. 

Web sites can become pretty complicated if you add many design elements, and it can be intimidating to figure out how to get started when thinking about how to present your Web page. One of the best ways to get started is to think about each of the individual HTML elements we've learned how to style so far, and how to style according to your specific goals. 

In this module, we'll discuss how to style the three most fundamental design aspects of a Web page: typography, color, and white space.


### Typography

A good rule of thumb when designing your Web site is to use no more than two different typefaces per page. Typically this means that you select 1 bold typeface for titles or other eye-catching pieces of text, and a neutral typeface for large blocks or the body text of your page. 

There is no official taxonomy of fonts, and not all browsers support all fonts, so it can be difficult to get your font looking exactly the way you want on all platforms. While you're starting out, it's best to stick to the most popular and commonly used fonts. [Here is a good list](https://www.w3.org/Style/Examples/007/fonts.en.html) of fonts for English pages and the appropriate fall-backs to get you started. On the Web, you can find other lists of available system fonts for non-Latin scripts, such as [this one](https://r12a.github.io/scripts/fontlist/).

As you get more comfortable, you can branch out to more exotic fonts. Remember that, when you are building your font-family set, you will want to always include a Web safe font alternative for an exotic font in case the user's device doesn't support it. 

```css
body {
   font-family: "Segoe UI", Helvetica, sans-serif;
}
```

When choosing your font, probably the biggest choice you'll make is what category of font to use. There are 5 basic categories of font: 

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/b1db41b5f1914fb5bfa55c3d502e756f/?child=first">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f5e20435f76b92b0a061c54c18a06264/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/5-2-2_font_categories.PNG" style="margin: 0.1em;" alt="Examples of 5 different font categories" title="Examples of 5 different font categories" width="450">
  </a></div>
</div>


+ __sans-serif__ - These are the most popular fonts for Web pages. This means the letters do not have added flourishes, so the typefaces are simpler. Their simplicity makes them easier to display on computer screens as their resolution is much lower than a printed document. It is often suggested you choose a sans-serif font for large blocks of digital text.  <br/>
  Examples: <span style="font-family: Helvetica;">Helvetica<span/>, <span style="font-family: Verdana;">Verdana<span/>, <span style="font-family: Arial;">Arial<span/>, <span style="font-family: Tahoma;">Tahoma<span/>
+ __serif__ - These fonts are the second most popular typefaces. "Serif" refers to the small flourish lines at the edges of letters and symbols. "Serifs" make each character more distinct, making text easier to read in print. This is why these fonts might remind you of a text from a typewriter, or of the fonts you see in printed books, newspapers or magazines. These typefaces can often be used effectively for titles or emphasis.  <br/>
  Examples: <span style="font-family: Times New Roman;">Times New Roman<span/>, <span style="font-family: Book Antiqua;">Book Antiqua<span/>, <span style="font-family: Georgia;">Georgia<span/>
+ __monospace__ - These fonts guarantee that all letters have the same fixed width. This is similar to a manual typewriter, or how computer code appears in editors. These fonts were designed for the ease of the technology, not humans, so they should be used sparingly. The most effective time to use these is when showing snippets of code.  <br/>
  Example: <span style="font-family: Courier New;">Courier New<span/>
+ __cursive__ - These fonts mimic human handwriting often by joining letters or having an italic slant. For some languages, these fonts are extra effective such as Arabic. Other than for specific languages, these fonts in English can be rather complex so they are best use extremely sparingly.  <br/>
  Example: <span style="font-family: Comic Sans MS;">Comic Sans MS<span/>
+ __fantasy__ - This is the most diverse category of fonts and includes all of those that are particularly decorative. These can make really great top headers as they can give your Web page a very distinct visual identity. Rarely will you want to use these for anything other than titles. It is also good to note that few of these are widely supported, so to use these you'll probably want to download them from a font service to make them available for your user.  <br/>
  Example: <span style="font-family: Impact;">Impact<span/>

#### External resource

+ Here is the W3C documentation for all of CSS's font properties: [CSS Fonts Module Level 3](https://www.w3.org/TR/css-fonts-3/).
+ Difference between type family, font face, typeface, font in the context of typography
  + __Type Family__ - The design of all the characters comprised of a family and all its encompassing faces. `Helvetica` is a type family. Helvetica Condensed is a type family, Myriad Pro is a type family, etc.
  + __Typeface__ - the specific weight or instance of a particular family. I.E. `Bold`, `italic`, `oblique` are all typefaces. Typeface is generally referred to by family + face. For example Helvetica Bold Italic would be referred to as the typeface where `Helvetica` is the Family and `Bold Italic` is the face.
  + __Font__ - Refers to the computer software file which contains information regarding _the display and output of a typeface_. You choose a font from the typeface menu. Fonts only exist on a computer. In the world today many use the word "Font" incorrectly -- "oh, I like that font." is wrong. It should be "Oh, I like that typeface." However, "Which font did you pick for that Photoshop design?" would be correct. Whereas, "What font is used in this logo?" is incorrect (should be typeface).
  + __Font Face__ - (somewhat interchangeable with typeface) the face of the type family. For example `Bold` or `Italic` are a face where as `Helvetica` would be the family. Referencing "font", font face specifically refers to the software used to render a particular face of a family - You may have `Helvetica bold` as a font face, but not `Helvetica italic`.



### Color

One of the most important design decisions you can make is your Web site's color palette. You should choose a palette before you begin designing to keep a cohesive visual identity. A common mistake it to use too many colors on a page. As you are starting out, it is best to limit yourself to just a few colors per page.

For a consistent look and feel your users will recognize, you will want to limit yourself to around __4 colors__ for all non-graphic content like text, backgrounds, borders, etc. There are different color palette tools on the Web you can play around with, but one of the best ways is to find a site you like the look and feel of and see if you can identify what color palette they are using.

When getting into design, it's a good idea to brush up on the basics of color theory, but just in case here's a short refresher. This is the color wheel:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/b1db41b5f1914fb5bfa55c3d502e756f/3?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40402411814eeb443188ebe6ea6c857534">
    <img src="https://www.w3.org/wiki/images/d/d2/10000000.jpg" style="margin: 0.1em;" alt="A color circle, based on red, yellow and blue, is traditional in the field of art. Sir Isaac Newton developed the first circular diagram of colors in 1666. Since then, scientists and artists have studied and designed numerous variations of this concept. Differences of opinion about the validity of one format over another continue to provoke debate. In reality, any color circle or color wheel which presents a logically arranged sequence of pure hues has merit." title="Color Wheel" width="250">
  </a></div>
</div>


#### Colors make other colors

+ The historical color wheel is organized around the three _primary_ colors: red, yellow and blue.
+ The _secondary_ colors are the combinations of these primary colors: orange, green and purple.
+ You can follow this pattern of varying the amount of each primary color to create infinite intermediary colors.
+ However, as you've seen for the Web, we define all colors as combinations of [Red, Green and Blue](https://en.wikipedia.org/wiki/RGB_color_space) (green, not yellow). The short answer for this is because that is how the human eye perceives color, something that was unknown when the historical color wheel was made.


#### Build a palette based on the color wheel

+ Colors that are across the wheel are called "complementary", blue and orange, red and green, etc.
+ Colors that are next to one another are considered  "analogous" like navy, blue and teal or lime, green and hunter.
+ When picking a color palette, you should generally pick between one that is comprised mostly of analogous colors, or mostly of complementary colors. Thankfully, there are lots of wonderful tools to help you do this! One we suggest is http://www.paletton.com/, where you can choose a starting color. It will generate for you a set of other colors that according to color theory will look pleasing together.

In your 4 colors, you'll want to keep a consistent tone so that your colors look good together. You'll want at least 1 very light color and 1 dark color. Avoid having all dark colors or all light, as often having contrast is important for readability. Also keep in mind not all users have full-color vision, so try to avoid too many similar colors. We will discuss how to choose inclusive colors in more detail in a later section.

#### External resource

+ Here is a good article that goes into detail about [color theory](https://www.w3.org/wiki/Colour_theory).


### White space

It can be difficult to strike a good balance of white space. The most common mistake beginner Web designers make is to not leave enough white space or empty space between HTML elements. 

You will want to make liberal use of paddings and margins to make sure that your site has plenty of empty space. Empty space makes it easier for a user's eyes to move around your page. You will want to ensure there is space between your HTML elements as well as between your elements and the edge of the page. 

Good balance between content and white space prevents your user from becoming fatigued while looking at your site. For example, when lines of text are very long, it is difficult to read without losing track of where you are. It is also fatiguing when the lines of text are too short because the user has to read vertically too much. There is considerable research on the topic, but a good rule of thumb is to limit __lines of text to 50-75 characters wide__. 


### Activity 5.2 - Breaking design guidelines

For this activity, you'll need to find a Web site that violates one of the following design guidelines:
1. Uses more than 2 different font-faces within a single page
2. Uses more than 4 different colors within the same page
3. Displays text wider than 50-75 characters across

Example:

+ [LingsCars](https://www.lingscars.com/): violate 1, 2, & 3
+ http://www.arngren.net/: looks like old way advertisement, violates 2, though the text not wider than 50~70 but the pcitures crowded the whole page, only one font-family: "New Time Roman"
+ [World's Worst Website Ever](http://www.arngren.net/): violate 1, 2


Once you have found a site, please share it in the discussion and answer the following questions:
1. Which of the 3 design guidelines are violated? More than 1 guideline?
2. Do you think that violation is a problem in this design?
3. How you you improve the design overall? 


## 5.3 Designing for your audience

### Intro to Web accessibility

#### What is Web accessibility?

> The power of the Web is in its universality.<br/>
> Access by everyone regardless of disability is an essential aspect.<br/>
> __Tim Berners-Lee, W3C Director and inventor of the World Wide Web__

The Web has become an essential aspect of our daily lives, and everyone should have access to this technology. Web accessibility focuses on ensuring equivalent access for people with disabilities. It is increasingly important to many organizations and governments from around the world, and has many business benefits. Access to information, including on the Web, is also recognized by the UN Convention on the Rights of Persons with Disabilities (CRPD).

##### Who is impacted?

Web accessibility addresses all disabilities, including hearing, learning and cognitive, neurological, physical, speech, and visual disabilities. Some examples of Web accessibility features include:

+ Captions on audio and multimedia content for people who are hard of hearing;
+ Clear and consistent layout for people with learning and cognitive disabilities;
+ Keyboard support for people with physical disabilities and do not use a mouse;
+ Text alternatives for people with visual disabilities and using screen readers;

__Web accessibility benefits people with and without disabilities__

Web accessibility features also benefit many more users, such as:

+ People with temporary situational limitations, such as a broken arm;
+ People using mobile devices, televisions, and other access channels;
+ People using older computers, with low bandwidth, and other limitations;
+ People who are new to computers, to the Web, or to your own website;
+ People who are not fluent in the language of your particular website;

The Web is an increasingly important resource in many aspects of life: education, employment, government, commerce, health care, recreation, and more. When Web pages, Web technologies, Web tools, or Web applications are badly designed, they can create barriers that exclude people from using the Web. More information is available in the [W3C Accessibility](https://www.w3.org/standards/webdesign/accessibility) overview.

#### First steps in Web accessibility

There are many simple Web accessibility improvements that you can implement and check right away, even when you are new to this topic. Two example excerpts are provided below on this page but you can find more tips and information from W3C/WAI:

+ [Tips for Getting Started with Web Accessibility](https://www.w3.org/standards/webdesign/accessibility)
+ [Easy Checks - A First Review of Web Accessibility](https://www.w3.org/WAI/eval/preliminary)


##### Example 1: page title

Good page titles are particularly important for orientation - to help people know where they are and move between pages open in their browser. The first thing screen readers say when the user goes to a different Web page is the page title. In the Web page markup, they are the `<title>` within the `<head>`.

__Check #1: There is a title that adequately and briefly describes the content of a page, and that it distinguishes the page from other Web pages.__

Example:

```html
<head>
...
   <title>Web Accessibility Initiative (WAI) - home page</title>
...
</head>
```

##### Example 2: image text alternatives ("ALT TEXT")

Text alternatives ("alt text") are a primary way of making visual information accessible, because they can be rendered through any sensory modality (for example, visual, auditory or tactile) to match the needs of the user. Providing text alternatives allows the information to be rendered in a variety of ways by a variety of user agents. For example, a person who cannot see a picture can have the text alternative read aloud using synthesized speech.

__Check #2: Every image has alt with appropriate alternative text.__

Example: See the W3C logo below. It contains a link that points to the W3C Web site. The text alternative is going to be a brief description of the link target.

```html
<a href="http://w3.org">
   <img src="images/w3c_home.png" width="72" height="48" alt="W3C Web site">
</a>
```

### Inclusive design

As you are designing your site, it is critical that you keep in mind the range of users who might be viewing your page. There are some simple design choices you can make to ensure that your web page is as inclusive as possible.

Typically a good approach is to keep your designs on the simpler side. Not only is this in line with current trends, but when there are fewer elements and styles, it is easier for everyone to consume the information you are trying to convey.


#### color-blind

When a user is color-blind, it typically means there is a category of colors that are difficult for them to distinguish between. So, by picking diverse colors that contrast well, you can ensure that these users can still read your page. To do this:

1. Pick a base color (example: blue).
2. Choose one or two shades of the same color (example: pastel blue, navy blue) as supplementary colors. Make sure these colors contrast with the base color, meaning that if one was placed on top of the other, it is still legible. Also, if you are choosing multiple supplementary colors, try to pick one from the yellows group (warmer colors) and one from the blues group (cooler colors). This way, a color-blind user is likely to only have difficulty seeing one of these, not both.
3. Select an accent color that is a totally different color from the previously chosen colors.

Even with a carefully chosen palette, it might still be difficult for a user to distinguish between colors. In addition to using color to indicate something, you'll also want to use shape. For example, if you have two buttons, one that is green for "agree" and one that is red for "disagree", it can be almost impossible for some users to decide which to click! In this case, you'll want to make sure they are both clearly labeled, or the shapes of the buttons are distinctly different.

Thankfully, The Paciello Group has created a tool you can download to check if your chosen colors provide enough contrast for color blind users. You can find out more about this free tool [here](https://www.paciellogroup.com/resources/contrastanalyser/)


#### low-vision

It is extremely common (as many as 20% of users over 45) for a user to have difficulty reading small text. These users often will have their Web browser set to magnify text to a size that is more comfortable for them, which can make all your carefully designed layouts look very different. These users will typically do one of two things:

+ _zoom in on the entire page_: you can test to see what this experience will be like with your own Web browser, typically with the "ctrl+" shortcut.
+ _use a text-only zoom_: to see what it looks like, you might want to test your layout with larger fonts, like 24pt or 32pt, to make sure your layout can grow to accommodate the overflow text. Also, note that long lines of text (over 50 characters wide) can be especially difficult to scroll through to read.

In general, you will want to make sure your font size is at least 1em. By using em you can let the text size grow based on the user's browser settings. 


#### External resources

+ [Tips on designing for Web accessibility](https://www.w3.org/WAI/gettingstarted/tips/designing) - on W3C's WAI Web site
+ [Color contrast](https://www.w3.org/WAI/eval/preliminary.html#contrast)


### What is internationalization?

Access to the Web for all has been a fundamental concern and goal of the W3C since the beginning. It is easy to overlook the needs of people from cultures different to your own, or who use different languages or writing systems, but you have to ensure that any content or application that you design or develop is ready to support the international features that they will need.

'Internationalization' is sometimes abbreviated to 'i18n' in English, because there are 18 characters between the 'i' and the 'n'.

The [W3C Internationalization Activity](http://www.w3.org/International/) works with W3C working groups and liaises with other organizations to make it possible to use Web technologies with different languages, scripts, and cultures.

People who use non-Latin writing systems or use the Latin script for certain languages, often have specific typographic needs that differ from text in, say, English. As you learn more about CSS, you will find that it provides many features to support those needs.

Whereas HTML markup provides structure for the content of your page, CSS bring the expressive power to make the page look the way a person from particular culture would expect.


#### Examples

Here are some examples of things that can be done with CSS.

+ It is already possible to make text run vertically in CSS for languages such as Chinese, Japanese, Korean and Mongolian. For more information see [Styling vertical Chinese, Japanese, Korean and Mongolian text](https://www.w3.org/International/articles/vertical-text/).

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/ce75a56f15a940fe8b10d4e1650d85c0/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4076912636762f48e2a0b99c10ebdda976">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ad92ee0958556281802909063f7ce69d/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/mongolian.png" style="margin: 0.1em;" alt="Vertically set Mongolian text." title="Vertically set Mongolian text." width="150">
    </a></div>
  </div>

+ You can also style counters for lists or chapter headings and such like according to local preferences. Here we see lists using Georgian and Japanese labels.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/ce75a56f15a940fe8b10d4e1650d85c0/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4076912636762f48e2a0b99c10ebdda976">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/47ca8caaf9c052289979a322e53b1cef/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/counterstyles1.png" style="margin: 0.1em;" alt="Georgian counter styles. Japanese counter styles." title="Georgian counter styles. Japanese counter styles." width="100">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/1418f5744104758c3429bdcbe7b02512/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/counterstyles2.png" style="margin: 0.1em;" alt="Georgian counter styles. Japanese counter styles." title="Georgian counter styles. Japanese counter styles." width="100">
  </a></div>
</div>

+ When you want to justify text so that the lines are straight on both sides of your column, different strategies are used for different scripts. Most Western typography puts an emphasis on adjusting inter-word spaces, but Chinese doesn't use spaces between words, so you generally do inter-character spacing. In text written using the arabic script it is common to stretch the baseline that joins letters, or use other techniques to balance the line.

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/ce75a56f15a940fe8b10d4e1650d85c0/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4076912636762f48e2a0b99c10ebdda976">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5dc2f0add20107a9d1fa253ea7ee9620/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/justified_arabic.png" style="margin: 0.1em;" alt="Arabic justification." title="Arabic justification." width="250">
    </a></div>
  </div>
  
  Some scripts allow words to be hyphenated in order to improve the visual effect of a paragraph, but note that the way in which words are hyphenated depends on the language. (And in arabic script, the CSS specification requires that both parts of the word retain their joining line during hyphenation.)

+ Text decoration and text style features can vary in applicability from script to script. For example, Japanese characters are fairly complicated so, rather than italicise their text for emphasis, which can make it harder to read at small sizes, they have a tradition of placing special marks alongside the emphasised text (see the middle line of the Japanese example below). Also, it may be important to avoid underlines running over descenders in some scripts, since it can obscure important marks attached to a base character, so CSS allows you to skip 'ink' as shown in the Burmese example below.

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/ce75a56f15a940fe8b10d4e1650d85c0/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4076912636762f48e2a0b99c10ebdda976">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/827e123772afe0c16b042dbedeb3d207/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/boten.png" style="margin: 0.1em;" alt="Emphasis in Japanese. Skipping descenders in Burmese." title="Emphasis in Japanese. Skipping descenders in Burmese." width="75">
    </a></div>
  </div>

These are just a few examples. There are many more.


#### CSS & Language

__An important point to bear in mind is that for many of these features to work as expected, you need to declare the language of the content.__ For example:

+ Hyphenation won't work unless the content is labelled for language. This is because the way that hyphenation works, and the dictionaries it uses, are language-specific.
+ If you want to convert Turkish or Azeri text to uppercase or vice versa, you will get incorrect results unless the browser knows that the text is in that language, because they have a dotted i and a non-dotted ı which do case conversion differently from European languages.
+ If text wraps to a new line, by default it does so differently dependent on whether you are dealing with Chinese or Japanese.
+ And we could continue...

Therefore, you should always ensure that the correct language is specified in the `lang` attribute on the `html` tag, to indicate the default language of the page. And if you have passages in another language inside the page, you should put a `lang` attribute on markup that surrounds them, too.


#### Localization

In addition, CSS provides tremendous help if you have to translate content from one language to another. Being able to change a single line in a style sheet to apply a change to all the pages being translated, rather than having to edit every page, saves a massive amount of time. However, this works best when you keep the distinction between semantics (markup) and presentation (styling) clear.

Don't use CSS to apply direction for bidirectional or right-to-left scripts, such as content in Arabic, Hebrew, Persian, Urdu, Divehi, etc. [Use HTML markup instead](https://www.w3.org/International/questions/qa-bidi-css-markup).


### Internationalization quick tips

1. __Language__: Always declare the default language of your page using the lang attribute on the html tag, and indicate internal language changes.
2. __Localizable styling__: Use CSS styling for the presentational aspects of your page. So that it's easy to adapt content to suit the typographic needs of the audience, keep a clear separation between styling and semantic content, and don't use 'presentational' markup.
3. __Use international features__: Use the international features provided by CSS to make your pages look natural to your audience. The more you use such features, and the more you request them, the better browsers will support them.
4. __Check your colors and styles__: Be sensitive to local preferences of your audience for things such as color, but also use of white space, two-dimensional vs. uni-directional display of information, etc.
5. __Use start and end__: Using these values, where possible, rather than left and right makes it easier to convert content between languages that use right-to-left and lef-to-right scripts.


### Activity 5.3 - Accessibility guidelines

For this section, your task is to go out and find a Web page that has one of the following issues:

1. A page that does not have a title set in its header
2. A page that has images without alt-text
3. A page with a color scheme makes it difficult for color-blind users to use
4. A page with a layout that breaks on text-only zoom

Once you've found an example of any of the above, post it on the discussion below, and answer the following questions:

1. Which of the above 4 accessibility guidelines does this page break? More than one?
2. Because of this violation what part of the Web page becomes inaccessible and to which group of users?

Examples: 

+ [Most Famous Videos of the Last Century](https://www.scaruffi.com/politics/videos.html): violate 1

## 5.4 Historical Web design trends

### The history of Web design

<video src="https://edx-video.net/W3CCSS0I2016-V005500_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@07690fa73ca040fe9d662289d7ea0249/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Moving pieces

As Web design tools became more sophisticated, the Web seemed to fill up with lots of fancy features that ultimately were just distracting. Especially in an era before mobile phones, certain items were used to add emphasis and style, but now are considered dated and would be a huge issue for mobile Web browsers.

Here is a list of style elements that should be avoided:

+ __marquee and rotating text__ - instead, use the different aspects of font to emphasize text like: size, color, weight or typography.
+ __cursors with animation__ - a very exciting feature at the time, now would be considered very dated, especially since mobile Web browsers don't even show a cursor. If you are going to adjust the cursor's appearance, do so using the [CSS cursor property](https://www.w3.org/wiki/CSS/Properties/cursor) and limit your usage to help your users understand when an item is interactive.
+ __lots of GIFs__ - GIFs are still very in style, especially with the popularity of services like giphy.com. Be aware however that GIFs draw a LOT of attention, so try to only use them when necessary. 
+ __videos that play automatically__ - these days, you'll find this tactic used almost exclusively by advertisements, so it is a good idea to avoid it if you don't want your user to dismiss your content. 
+ __background music__ - sometimes still used to set a tone for your site, but often is considered disruptive by users. If you absolutely must have background music, make sure to give your user a way to turn it off that is easily accessible.


### Rigid layouts

Now, when we design sites, we are always talking about "different screen sizes", "different devices", etc. This is because there is such a huge array of ways that users will access a Web site. Historically, this was not the case, and it was a safe assumption that your user would access your site using a device and screen that were very similar to the ones you used to make it. As our devices evolved, so did our CSS layout tools so we could move away from these old trends.


#### frames

Used as a crutch for Web site navigation, this was a site within a site that followed your user around as they navigated. It was often used in placement of a menu bar. This feature was removed in HTML5.

Instead, focus on making a user's flow through your site intuitive by building a visually distinct and consistent form of navigation. 


#### HTML Tables for Layout

Tables organize data into structured rectangular sections, so it was an easy way to organize your site in a grid-like layout. HTML tables came with lots of problems. They overloaded HTML trees with lots of unnecessary tags that all come with their own set style that had to be adjusted, and they were extremely limited in how much you could actually adjust them. They also can pose problems with accessibility, it was easy for your content to be displayed in the wrong order.

Initially, we replaced HTML tables with `<div>` tags, a multi-purpose tag that was much more flexible than a table row or column, but while divs were flexible they weren't very descriptive. With HTML5, we gained more content descriptive tags like `<header>`, `<footer>`, `<section>` and `<article>` that have the same flexibility of div but that better describe your content.



### Heavy content

These days, it is extremely likely that many of your users will view your page on a mobile device, typically using cell data as their connection. Cell networks are much more limited than the hard wired connections that were once the only gateway to the Internet.

Back when this was the case, Web designers employed a number of techniques that were very "heavy" (often Adobe Flash) or required a lot of data to download. Now, we have to always be aware of how heavy our page load is, so we don't exclude users on cellular data networks from accessing our site.


#### Adobe Flash

This is a way for designers to add interactivity and sophisticated animations to sites. However, Flash is not supported on mobile phones and so the use of flash to animate pages has fallen out of style. Also, with CSS3, we now have a host of animations that come standard with CSS so there is less need for an external, heavy technology to make dynamic pages.

Animations are beyond the scope of this class, however be aware that there are two ways to do animations: using [CSS animations](https://www.w3.org/TR/css3-animations/) or [CSS transitions](https://www.w3.org/TR/css3-transitions/).



### Activity 5.4 - Retro design styles

For this activity, please find a retro styled Web site that uses one of the following outdated design elements. You might want to use the Internet Archive to find some older Web pages where these elements were more prevalent.

1. overly animated text
2. animated cursors
3. Frames
4. HTML table layouts

Once you've found an example page, post it in the discussion and answer the following questions:

1. Which historic design element does this page use? More than one?
2. What new technology would you use to modernize this element?


Examples:

+ [Neo-Surrealism Art](https://web.archive.org/web/20060410143214/http://www.neosurrealismart.com/): violated 2, 4
+ [Moving Letters](https://tobiasahlin.com/moving-letters/): violated 1 (bit it's ok on this webpage)
+ [16 Frames](https://www.w3.org/TR/html401/present/frames.html): violate 3 (bot the webpage itself but the contents described)


#### Resources

+ [Framing](https://en.wikipedia.org/wiki/Framing_(World_Wide_Web))
  + In the context of a web browser, a __frame__ is a part of a web page or browser window which displays content independent of its container, with the ability to load content independently.
  + In HTML, a __frameset__ is a group of named frames to which web pages and media can be directed; an iframe provides for a frame to be placed inside the body of a document.
  + Frames were used to display and navigate early web apps, such as web chat sites and online magazines.
  + Since the early 2000s, the use of framesets has increasingly been considered obsolete due to usability and accessibility concerns, and the feature has been removed from the HTML5 standard.
  + The practice of framing HTML content led to numerous criticisms, most centering on usability and accessibility concerns.



## 5.5 Current Web design trends

### The current state of Web design

<video src="https://edx-video.net/W3CCSS0I2016-V005600_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@6d511486ee544712b50e9f0cd5a43153/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Minimalism

This Web design trend is part fashion, part function. Since we always keep mobile devices in mind when designing, the "rich design" styles of the past (drop shadows, gradients, lots of images, colors, and fonts) have been replaced with the current trend "flat design".

Flat design emphasizes:

+ _simple elements_ - grid layouts, limited number of elements
+ _flat colors_ - no drop shadows, no attempt to make 2D elements look 3D
+ _clean typography_ - sans-serif fonts, large sized and lower case 

Benefits of flat design:

+ _low load times_ - better for mobile network connections
+ _responsiveness_ - when there are a small number of elements, it is easier to manage their relationships so that the overall layout can grow and shrink to accommodate different screen sizes
+ _intuitive experience_ - research has shown that the cleaner a site, the easier it is for a user to find the information they are looking for


### Long scrolling

In the past, Web sites were comprised of many separate pages that you would navigate to, leaving behind the page you came from. These days, you'll often find pages that are comprised of a single long scrolling page with links that just jump to different portions of the page. The reason for this is less about fashion and more about technological developments. Especially on touch devices, scrolling is a more natural human way to interact with a page.

This can be accomplished with something called "internal links". This is where you load the entire page as one long site and the links at the top simple jump to different locations within the site. To do this, you need to give the section you want to jump to an id, and then you use the `id` selector as the `href` setting on the anchor tag. 

[HTML Example](src/5.5-LongScroll.html)

There are other methods that are more advanced that save you from loading the entire page. One technique under development to make scrolling easier and more accurate is a module called "[CSS Scroll Snap](https://www.w3.org/TR/css-scroll-snap-1/)".


### New layout techniques (OPTIONAL)

Web layout is always constrained by the limitations of CSS, but future trends will be able to make use of new tools, such as CSS Flexbox (officially: CSS Flexible Box Layout) and CSS Grid.

Since the summer of 2017, the major browsers support this module of CSS, which provides the beginnings of something professional designers have long been waiting for: [a design grid](https://en.wikipedia.org/wiki/Grid_(graphic_design)).

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/f88fb97e1bfb40f88c89f55ed6bfab31/4?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40b4c314ed834d44beab8fcbab663089ab">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a3394a993e85bcc83720b18cba696330/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/CSSBasics-Flex-Grid-smal.png" style="margin: 0.1em;" alt="CSS flexbox and grid layout differences" title="CSS flexbox and grid layout differences" width="250">
  </a></div>
</div>

It's been a few years now that the CSS Flexbox module gives advanced control over alignment and spacing of elements on a line or in a stack. The Grid module now allows alignment in two dimensions: to elements on the same line and to elements in the same column.

Grid doesn't replace Flexbox. There is some flexibility when placing elements in one line that you lose when you add a second dimension. At the same time there are layouts that were difficult or impossible even with Flexbox and are now easy with Grid.

The Grid module is only a first step. Level 1 has a number of limitations (just like Flexbox), due to do issues around complexity and performance. For example, you can currently only align elements that have the same parent. That said, for laying out graphical user interfaces (GUIs), Flexbox and Grid work very well.

We briefly present them below, and give a few resources at the bottom of the page so that you can explore more. Note: _this lecture is optional and there will be no questions related to it in the final exam_.


#### CSS Flexbox

Since its introduction in 2012, CSS Flexbox has become widely used and [browser support](http://caniuse.com/#feat=flexbox) is really good. Flexbox made a lot of complex layout tasks easier, like equidistant spacing between elements, top-to-bottom layouts or the [holy grail](https://en.wikipedia.org/wiki/Holy_Grail_(web_design)). Find out about Flexbox and how to use it in the last section of the [W3C HTML5 and CSS Fundamentals course](https://www.edx.org/course/html5-and-css-fundamentals)!

Despite the similarities in concept and syntax, Flexbox and Grid are not competing layout techniques. Grid arranges in two dimensions, while Flexbox lays out in one. There is synergy when using the two together.


#### CSS Grid

CSS Grid is a CSS module that defines a two-dimensional grid-based layout system, optimized for user interface design. In the grid layout model, the children of an element (the ‘grid container’) can be positioned into arbitrary slots in a predefined flexible or fixed-size layout grid.

If that sounds a bit too abstract, here is another way of looking at it. The idea behind the Grid module is that you split the [box](https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/jump_to_id/61920cda43ca49cca2fcf26e763bbe16) that makes up an element into many individual ‘slots’, arranged in a matrix, and separated from each other by (invisible) horizontal and vertical lines. You do that with a property called 'grid', which contains the desired number of rows and columns and/or their sizes. Each child element goes into a slot, so that they end up aligned as in a table. But you have full control over which slot they go into, you can change their order, they can span more than one row or column, and you can leave some slots empty.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/12e8f1585d88470e95f54cf0ff6a1a00/f88fb97e1bfb40f88c89f55ed6bfab31/4?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40b4c314ed834d44beab8fcbab663089ab">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/68610fc2b976618d03192de396b29649/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/grid.png" style="margin: 0.1em; background-color: white;" alt="CSS Grid is a CSS module that defines a two-dimensional grid-based layout system, optimized for user interface design" title="Diagram for CSS Grid" width="350">
  </a></div>
</div>

The Grid module provides several different ways to define such a grid and to place the child elements. Too many, in fact, to present here.

Because they can refer to a previously defined grid of horizontal and vertical lines, the properties from the CSS Grid module provide more control over the alignment of elements than most other properties in CSS, such as the table-related properties or the 'float' and 'clear' properties, while also allowing elements to be displayed out of order. As such they are especially appreciated for (Web) applications with user interfaces that are made with HTML and CSS. The Grid module is not yet the '[design grid](https://en.wikipedia.org/wiki/Grid_(graphic_design))' that typographers want for the layout of magazines and books, but it is a first step. (E.g., one obvious thing to do, applying grid properties to an HTML table, doesn't work, because the properties do not handle nested elements yet.) Even though this is only level 1 of the module, it is well worth trying out.

The properties from the Grid module have only been available in major browsers since mid 2017 (see the [status of browser support](http://caniuse.com/#feat=css-grid)). But the ideas behind the Grid module aren't new. From the start of CSS, there have been proposals to use CSS properties to define a template or matrix to guide the layout of elements, e.g.: [Frame-based layout](http://www.w3.org/TR/WD-layout), [Advanced Layout](http://www.w3.org/TR/2005/WD-css3-layout-20051215/) (later called [Template Layout](http://www.w3.org/TR/css-template-3/)), [Grid Style Sheets](https://github.com/gss) and [Constraint CSS](https://constraints.cs.washington.edu/web/ccss-uwtr.pdf). But only recently has technology become good enough to support some (not all!) of those ideas.


#### A few resources

If you look at the CSS Grid module, you may notice that it has rather a large number of properties: 18. That is because it tries to allow different manners of writing style sheets. There are many shorthand properties and many alternative ways to define the same grid. In practice, most style sheet writers will select a set of just three or four properties that suits their way of working.

When considering the CSS Grid module, also look at the CSS Flexible Box module. It only provides for alignment of elements in a single row or column, but has some features that Grid doesn't have (and it has been around longer and works in older browsers). On the other hand, even for a single row or column, the Grid properties may turn out easier in some cases.


##### CSS Layout

+ [CSS Layout News](http://csslayout.news/) - A weekly collection of tutorials, news and information on all things CSS Layout, by Rachel Andrew.


##### CSS grid resources

+ [A complete guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) (CSS Tricks)
+ [CSS Grid](https://www.w3.org/TR/css-grid-1/), the W3C specification
+ [Grid by example](https://gridbyexample.com/): this site is a collection of examples, video and other information to help you learn CSS Grid Layout.


##### CSS flexbox resources

+ [A complete guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) (CSS Tricks)
+ [CSS Flexible Box Layout](http://www.w3.org/TR/css-flexbox/), the W3C specification
+ [Flexbox froggy](http://flexboxfroggy.com/) (game to practice CSS flexbox code)


### CSS Grid layout (OPTIONAL)

#### CSS Grid Layout: from an idea to a reality

Have a look at how CSS Grid Layout went from an idea to a reality. The video below has been shot in August 2017 by the Microsoft team. It features some of the [CSS Working Group participants](https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2017/courseware/12e8f1585d88470e95f54cf0ff6a1a00/6c9058a29dc5493fbb43332c6bc3b550/4?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2017%2Btype%40vertical%2Bblock%40beac75cf51c34b51a0ac0f6e5fad70cc):

> Rossen Atanassov (Microsoft) ; Tab Atkins Jr. (Google) ; Sergio Villar Senin (Igalia) ; Bo Cupp (Microsof) ; Elika Etemad, aka fantasai (W3C Invited Expert to the CSS WG) ; Greg Whitworth (Microsoft) ; Dr. Bert Bos (W3C & Co-Creator of CSS) ; Rachel Andrew (W3C Invited Expert to the CSS WG).

#### Video: creating CSS Grid

<video src="https://youtu.be/z-TXKGF9B-0" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@76f3139130a94dfb97d486b6f767f356/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Activity 5.5 - Best design

For this activity, go out and find what you think is the best-designed Web page! Post a link to it in the discussion along with the answers to the following questions:

1. Why do you like the design of this Web page?
2. What is one aspect of this Web page you would like to use in your own design?
3. Is this Web page accessible?


## 5.6 Project 5 - Apply good design

Now that we've discussed so many design guidelines, it's your turn to try some out. Take your resume you created in Module 4 and make sure that it conforms to all the following rules:

+ 4 total colors that are color-blind inclusive
+ 2 total typefaces that can grow if a user is employing a text-zoom
+ each element has a good amount of white space around it
+ no line of text is longer than 75 characters wide

Be creative and do not hesitate to share your results in the discussion forum below!




