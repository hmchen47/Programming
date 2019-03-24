# Module 3: Specific HTML element targeting with CSS selectors

## 3.1 Introduction

### Welcome to Module 3

#### Video: welcome to Module 3


<video src="https://edx-video.net/W3CCSS0I2016-V005900_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@4217fd0468774c3789c662106419427b/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


#### In this module, we'll learn:

+ How to use classes and IDs to independently target HTML elements of the same type
+ How to apply different style to the same element based on the way the user interacts with that element using pseudo-classes
+ How to scope style rules using contextual selectors and the HTML inheritance structure of your document
+ What the "Cascading" part of "Cascading Style Sheets" means


### The power of selectors

<video src="https://edx-video.net/W3CCSS0I2016-V003700_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@32b59e549e1347ac84255be40457e6db/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>

Code mentioned in above video

```css
p {
    color: white;
    background-color: midnightblue;
    font-size: large;
}
.middle {
    color: darkviolet;
    background-color: lightgray;
    padding-left: 120px;
    padding-right: 120px;
    font-size: large;
}
#bottom {
    background-color: transparent;
    color: black;
    font-family: 'Franklin Gothic Medium';
}
```

## 3.2 Using HTML classes and IDs

### Meet IDs and classes

#### Video: meet IDs and classes
 
<video src="https://edx-video.net/W3CCSS0I2016-V004600_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@d06bd738723849709edb85e879cd89e7/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>

#### Classes

Classes are an HTML attribute that specifies a name for a group of elements on the page. You can apply the class name to as many elements as you like, even if they are of different HTML tag types. You can use the class name with a period in front as the selector like so:

```css
<p class="className">The intro paragraph</p>
```

Class names must be single words, but you can include digits and dashes as long as the name begins with a letter. Note that names are case sensitive.

To apply a CSS rule to a class you use the class name preceeded by a period (".") like in the code below:

```css
.className {
    color: blue;
}
```

[Documentation](https://www.w3.org/TR/html52/dom.html#classes)

#### IDs

An ID is an HTML attribute that specifies a name or unique identifier for a particular HTML element. They are like classes with a very important distinction: the value of the ID attribute must be unique throughout the document. This lets you target a single HTML element for styling. You use the name with a hashtag in front as the selector like so:

`<p id="MyFirstId">` This is an extra special paragraph </p>
ID names have the same rules as class names: start with a letter, can include numbers and dashes, no spaces. The way to create a selector for an ID is also similar to how you create a selector for a class, except you replace the period with a hash symbol ("#") like in the code below:

```css
#MyFirstId {
    color: blue;
}
```

[Documentation](https://www.w3.org/TR/html52/dom.html#the-id-attribute)

#### Example

HTML code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Classes and IDs</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Title</h1>
    <p id="intro">
      Classes and IDs are "attribute selectors". This means that you can attach style to HTML elements based on that element's attributes. This empowers you to apply different style to items of the same HTML type.
    </p>
    <p class="odd">
      Classes are an HTML attribute that specifies a name for a group of elements on the page. You can apply the class name to as many elements as you like, even if they are of different HTML tag types. You can use the class name with a period in front as the selector like so:
    </p>
    <p class="even">
      Class names must be single words, but you can include digits and dashes as long as the name begins with a letter. Note that names are case sensitive. 
      To apply a CSS rule to a class you use the class name preceeded by a period (".") like in the code below:
    </p>
    <p class="odd">
      An ID is an HTML attribute that specifies a name or unique identifier for a particular HTML element. They are like classes with a very important distinction: the value of the ID attribute must be unique throughout the document. This lets you target a single HTML element for styling. You use the name with a hashtag in front as the selector like so:
    </p>
    <p class="even">
      ID names have the same rules as class names: start with a letter, can include numbers and dashes, no spaces. The way to create a selector for an ID is also similar to how you create a selector for a class, except you replace the period with a hash symbol ("#") like in the code below:
    </p>
  </body>
</html>
```

CSS code:

```css
#intro {
    color: green;
}
.odd {
    color: blue;
}
.even {
    color: red;
}
```

Output:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/46a1028808b949b9af0061a363d40b8a/ac74f8ec30b14ea58fe791c324062d2c/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40f60d634ed7f54bd8935f185e31f17dac">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/1a0cf9e0b83dc19c7e6fb78286ceb5bc/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/3-2_output.PNG" style="margin: 0.1em;" alt="Sample Classes and IDs output" title="Sample Classes and IDs output" width="350">
  </a></div>
</div>


### Activity 3.2




## 3.3 CSS pseudo-classes

### Meet CSS pseudo-classes




### Activity 3.3




## 3.4 Combining selectors

### Meet contextual selectors




### Activity 3.4.1




### Cascading styles




### Activity 3.4.2




## 3.5 Style studies

### Images




### Forms




## 3.6 Project 3 - My profile




## 3.7 Conclusion and exercises

### After this module you should be able to...




### Exercises (1-5)




### Exercises (6-10)




### Exercises (11-15)



