# Module 4: Layout and positioning

## 4.1 Introduction

### Welcome to Module 4

<video src="https://edx-video.net/W3CCSS0I2016-V005000_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@a9612f0ade0e4846a6fce8679b0f0873/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


### In this module, you will learn

+ How to use padding and margin to position elements relative to each other and the window
+ How to use alignment to control how your content sits within its HTML element
+ How to use the float property to let multiple HTML elements share horizontal space
+ How to use relative positioning to design your page so that it maintains its layout regardless of screen size


### Meet the box model

<video src="https://edx-video.net/W3CCSS0I2016-V004900_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@d7de8c9c374b442c8dca24cbb32d0766/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


### The Box Model

The Box Model is how Web browsers see individual HTML elements. Each element is comprised of 4 areas: the __element__, the __padding__, the __border__ and the __margin__.

We discussed how to adjust the white space of these areas in Module 2.5, but in this module we will be discussing these areas as a method to position elements on a page.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/2fb0b177f7594d2aa29f0ffa9e3b8b0a/cc87ccb0d8f243f98b2f17c1955c0298/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%408347080b2233486082d5154ee2e14ad6">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e0c6338dd98e9176bf12088bb686892f/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/4-1_box_model.PNG" style="margin: 0.1em;" alt="anatomy of the box model" title="anatomy of the box model" width="400">
  </a></div>
</div>


+ __element__ - This is always contained within a square, even if it is a text block with jagged edges or a transparent image that isn't rectangular. Web browsers will impose a rectangle around the smallest area the HTML element's content actually occupies. Until now we've allowed the Web browser to determine the size of the element based solely on the content, but later in this section we'll learn how to adjust this sizing.
+ __padding__ - This is the white space just outside the element's content. You can set each of the four sides independently, and you can set the value to 0. If you set the element's background color, that color will apply to the padding as well.
+ __border__ - This is the area just outside the padding. Most HTML element's border default width is 0 and thus invisible. You can set each of the four sides independently. You can set a color, a pattern, even an image. This is a great way to add horizontal or vertical lines to an element on your page.
+ __margin__ - This is the space surrounding an element, outside the border. Margins are the part of HTML elements that interact with one another. When two margins interact the larger of the two wins meaning the smaller margin "collapses", thus the actual space between two elements is the larger of the two, not the sum of the margins.

[Example HTML](src/4.1-Box.html)
[Example CSS](src/css/4.1-Box.css)

#### External resource:

Box model definition in the [W3C's CSS2.1 specification](https://www.w3.org/TR/CSS2/box.html)



## 4.2 The basics of layout

### The alignment property

One of the simplest ways to align content is to use the direct text-align property. This can help you set the alignment of text or inline content within the context of their containing HTML element.

__text-align__

[Documentation](https://www.w3.org/TR/CSS22/text.html#alignment-prop)

```css
h1 {
   text-align: center;
}
```

If you have used a text editor before, like Microsoft Word, you've probably used the different text-align properties: left (default for English), right, center and justify. Text-align in CSS works the same way. Left, center and right specify how the lines of text within the text block are arranged. Justify sets the left and right edges of the text flush with the container's edges, which stretches the white space between words so that the overall block fits in a perfect rectangle.

See below for examples of what each of these values will do to your text:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/2fb0b177f7594d2aa29f0ffa9e3b8b0a/8677e13b3db74668975ed449d681277e/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40830982357f6646b796b37c238897fb9e">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8fa61e99d7f19f1e10862952f41a5128/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/4-2-3_text_align.PNG" style="margin: 0.1em;" alt="Example of each text-align value options" title="Example of each text-align value options" width="350">
  </a></div>
</div>


Note that this property can only apply to block elements like paragraphs, divs and headers.

__line-height__

[Documentation](https://www.w3.org/TR/CSS22/visudet.html#line-height)

```css
h1 {
   line-height: 1.2;
}
```

You may have noticed that the text-align property sets the content's alignment horizontally, but it leaves its vertical alignment unchanged. Text lives within a specified vertical space, in which the text is drawn by default in the middle of that vertical space. If you change the height of the containing HTML block, the text will remain at the top of the block. However, if you instead use the "line-height" property, then the block will grow and the text will vertically center within it.


... and the resulting output:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/2fb0b177f7594d2aa29f0ffa9e3b8b0a/8677e13b3db74668975ed449d681277e/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40830982357f6646b796b37c238897fb9e">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3de7c0b54bd64eeffcf209a9928a95f0/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/4-2-3_alignment-1.PNG" style="margin: 0.1em;" alt="output from alignment example code" title="output from alignment example code" width="450">
  </a></div>
</div>


INTERNATIONAL CONSIDERATIONS
Please do not use text-align indiscriminately. If there's a possibility that your site will need to be translated into a language that uses the Arabic, Hebrew, or Thaana scripts (which read from right to left), it creates difficulties to have to change all the  right values to left and vice versa.

Most, but not yet all, major browsers support the values start and end. The start value aligns text with the side of the line where you start reading, whether that's on the left for English or the right for Urdu. They also make more sense for use with vertical text, such as for Japanese and Mongolian. Once these values are widely supported by browsers, they will often be a better choice than right and left, since there's no need to change the values for pages as the language changes.

Also, note that CSS will in the future provide better support for justification in languages where words are not separated by spaces, such as Chinese and Thai, or languages where words are separated by special marks, such as in Amharic. For more information about different approaches to justification, see this article.

Once you finish this course, look out for these and other international features of CSS as you explore its features further.


### Element width and height



### Padding and margin



### Activity



## 4.3 Floating elements

### Meet the float property



### Activity



## 4.4 Relative positioning

### Meet relative positioning



### Activity



## 4.5 Style studies

### Menus



### Footers



## 4.6 Project 4 - My resume

### When to use what?



### Module 4 project



## 4.7 Conclusion and exercises

### After Module 4, you should be able to...



### Exercises (1-5)



### Exercises (6-10)



### Exercises (11-14)


