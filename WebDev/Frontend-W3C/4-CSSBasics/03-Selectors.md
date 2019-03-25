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

#### Classes and IDs

Classes and IDs are "attribute selectors". This means that you can attach style to HTML elements based on that element's attributes. This empowers you to apply different style to items of the same HTML type.



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

An ID is an HTML attribute that specifies a name or unique identifier for a particular HTML element. They are like classes with a very important distinction: _the value of the ID attribute must be unique throughout the document_. This lets you target a single HTML element for styling. You use the name with a hashtag in front as the selector like so:

```html
<p id="MyFirstId"> This is an extra special paragraph </p>
```

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


### Activity - Add your own classes and ids

Here is some HTML and CSS. As you can see it's not too interesting, because not all of the styles are applied to the HTML.

```css
body {
   background-color: #00ccff;
   color: white;
   font-family: Helvetica, sans-serif;
   margin: 35px 25px 0px 25px;
}
p,h2 {
   padding: 10px;
}
.topSection{
   background-color: #3300cc;
   color: #cccccc;
}
.bottomSection {
   background-color: #cccccc;
   color: #3300cc;
}
#importantItem {
   text-decoration: underline;
   color: #99ff99;
}
#unimportantItem {
   color: gray;
}
```

```html
<!DOCTYPE html> 
  <!--It's a best practice to always declare DOCTYPE!-->
    <html lang="en">
        <head>
            <meta charset="utf-8">
        </head>
  <body>
    <h1>Welcome to my page</h1>
    <h2>Top Section</h2>
    <p>Classes and IDs are "attribute selectors". This means that you can attach style to HTML elements based on that element's attributes. This empowers you to apply different style to items of the same HTML type.Classes are an HTML attribute that specifies a name for a group of elements on the page. You can apply the class name to as many elements as you like, even if they are of different HTML tag types. You can use the class name with a period in front as the selector like so:</p>
    <ul>
      <li>Class names must be single words</li>
      <li>but you can include digits and dashes as long as the name begins with a letter</li>
      <li>To apply a CSS rule to a class you use the class name preceeded by a period (".")</li>
    </ul>
    <h2>Bottom Section</h2>
    <p>An ID is an HTML attribute that specifies a name or unique identifier for a particular HTML element. They are like classes with a very important distinction: the value of the ID attribute must be unique throughout the document. This lets you target a single HTML element for styling. You use the name with a hashtag in front as the selector like so. ID names have the same rules as class names: start with a letter, can include numbers and dashes, no spaces. The way to create a selector for an ID is also similar to how you create a selector for a class, except you replace the period with a hash symbol ("#") like in the code below.
    </p>
    <ul>
      <li>How to use classes and IDs to independently target HTML elements of the same type</li>
      <li>How to apply different style to the same element based on the way the user interacts with that element using pseudo-classes</li>
      <li>What the "Cascading" part of "Cascading Style Sheets" means</li>
      <li>How to scope style rules using contextual selectors and the HTML inheritance structure of your document</li>
    </ul>
  </body>
</html>
```

In this activity, your job is to add the HTML id and class attributes to the correct elements so that you get a final result that looks like this:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/46a1028808b949b9af0061a363d40b8a/ac74f8ec30b14ea58fe791c324062d2c/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40f60d634ed7f54bd8935f185e31f17dac">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/2d0d454c1dd43e5cc10ca355082a61bc/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/3-2-2_activity.PNG" style="margin: 0.1em;" alt="Activity: Apply Classes and IDs final image" title="Apply Classes and IDs final image" width="350">
  </a></div>
</div>




## 3.3 CSS pseudo-classes

### Meet CSS pseudo-classes

<video src="https://edx-video.net/W3CCSS0I2016-V004700_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@66314acf9cd1453f9f035925a73fa363/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>

### CSS pseudo-classes

Pseudo-classes are a way to select HTML elements based on their state as opposed to their HTML structure. You can [read more about pseudo-classes here](https://www.w3.org/TR/CSS22/selector.html#pseudo-elements).

Pseudo-classes must always be applied to an existing selector. Their "flag character" is the colon (":"), as you can see used in the below examples. Here are some of the most popular pseudo-classes.


#### `:link` and `:visited`

```css
a:visited {
   color: gray;
   font-style: italic;
}
```

These pseudo classes are the ones you are probably most familiar with. Even on this page you've probably noticed that links have different style than paragraph text. The `<a>` tag by default sets the text color to blue with an underline, but have you ever seen a purple link? This is the "visited" pseudo-class that applies a different style to links that the user has already clicked. The opposite of visited is "link" which is a link a user has not yet clicked. These two states are mutually exclusive, meaning a link cannot be both at the same time.

[Documentation](https://www.w3.org/TR/CSS22/selector.html#link-pseudo-elements)


#### `:hover`

```css
li:hover {
   background-color: yellow;
}
```

The hover pseudo-class is applied when the user points at an object but doesn't activate it, most commonly when they let their mouse cursor lay on top of an element without clicking. Some form factors don't support this, such as touch devices or pen surfaces. This is a really good way to encourage a user to click a link and you will often see it used in navigation bars. 


#### `:focus`

```css
input:focus {
   background-color: blue;
}
```

The focus pseudo class is when a user has chosen to begin interacting with an element, often when the click into a form input such that the input is then ready to accept keyboard input.


#### `:active`

```css
p:active {
   color: red;
}
```

The active pseudo-class applies when an element is activated. This happens in the time between when the user clicks their mouse and they release it.

[Documentation](https://www.w3.org/TR/CSS22/selector.html#dynamic-pseudo-classes)


#### [Comparisons of `:active` and `:focus`](https://stackoverflow.com/questions/1677990/what-is-the-difference-between-focus-and-active)

`:focus` and `:active` are two different states.

+ `:focus` represents the state when the element is currently selected to receive input and
+ `:active` represents the state when the element is currently being activated by the user.

For example let's say we have a `<button>`. The `<button>` will not have any state to begin with. It just exists. If we use `Tab` to give "focus" to the `<button>`, it now enters its `:focus` state. If you then click (or press `space`), you then make the button enter its (`:active`) state.

On that note, when you click on an element, you give it focus, which also cultivates the illusion that `:focus` and `:active` are the same. They are not the same. When clicked the button is in `:focus:active` state.




[Example](src/3.3-PseudoClass.html)


### Activity - - Applying pseudo classes

Now it's your turn to try out some pseudo classes. Here is a Web page.

See the Pen [Practice with Pseudoclasses](https://codepen.io/techie4good/pen/rraNJr/)

```css
body {
   background-color: #006666;
   color: white;
}
h1 {
   text-decoration: underline;
}
input {
   border: 3px white solid;
}
input {
   border: 3px yellow solid;
}
input {
   background-color: yellow;
   border: 3px yellow solid;
}
button {
   background-color: white;
   color: #006666;
   border: 3px white solid;
}
button {
   background-color: #006666;
   color: white;
}
button {
   background-color: #33cc99;
}
li {
   background-color: white;
   color: #006666;
}
li {
   background-color: #33cc99;
   color: white;
}
a {
   color: white;
}
a {
   color: #33cc99;
}
```

If you look at the CSS for this page you'll notice there are multiple CSS rules with the same selectors. That is because some of these rules need to have pseudo classes applied.

Please add pseudo-classes to the existing rules so that:

+ The title is underlined when the user hovers their mouse over the text
+ The input box gets a yellow border when the user hovers their mouse over the box
+ The input box has a yellow background when the user clicks inside the box
+ When the user hovers over the button it gets a background color of #006666 (dark green) and a text color of white
+ When the user clicks the button it gets a background color of #33cc99 (light green)
+ The background color of the list elements turns white and the text turns #006666 (dark green) when the user hover overs them
+ When clicked, the list elements get a background color of #33cc99 (light green) while the text stays white
+ The links at the bottom of the page start out as white in color and then when they are clicked they turn #33cc99 (light green)
+ The resulting output should look like this when the user has not interacted with the page in any way:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/46a1028808b949b9af0061a363d40b8a/2069ed7e6d9c4e35a70c056994d2413e/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4040486880ddf54d08922814a53f31f69b">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/17c251eec9c7e28a5214a2888df27bef/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/3-3_activity.PNG" style="margin: 0.1em;" alt="Activity: Pseudo Class final image no interaction" title="Pseudo Class final image no interaction" width="350">
  </a></div>
</div>



## 3.4 Combining selectors

### Meet contextual selectors

<video src="https://edx-video.net/W3CCSS0I2016-V004800_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/xblock/block-v1:W3Cx+CSS.0x+3T2018+type@video+block@8d5b18b8cd6d43dbb7b4ff7f4708d3d0/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>
<br/>

### Contextual selectors

When you use two selectors separated by a space on a rule, you scope the rule to the elements that correspond to the selector on the right that are INSIDE the elements that correspond to the selector on the left. Let's say we have the following HTML:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <img src="images/pic1.jpg" alt="pic 1" />
        <p>
            This is my paragraph full of useful information
            <img src="images/pic2.jpg" alt="pic 2" />
            Since there is text around these images they should be styled a little differently.
            <img src="images/pic3.jpg" alt="pic 3" />
        </p>
        <img src="images/pic4.jpg" alt="pic 4" />
    </body>
</html>
```

If we applied the following CSS rule then the images INSIDE the paragraph would be set to a width of 100px, but that rule would not apply to the images outside the paragraph.

```css
p img {
    width: 100px;
}
```

Below is a diagram of the given HTML with the two imgs that will styled by the above rule are indicated by the red arrows.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/46a1028808b949b9af0061a363d40b8a/8c35f24ecbd746c1a0106f1c4ce9e1b0/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40096e999e5b21437b8b86bc0e4f12b730">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8a65bf214939ba9bec2a0b48674f222b/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/3-3-1_combinging_selectors.PNG" style="margin: 0.1em;" alt="Diagram pointing out which img tags will be styled" title="Diagram pointing out which img tags will be styled" width="350">
  </a></div>
</div>

As your Web pages get more complex, contextual selectors become more important, because it won't scale to apply classes and IDs to each individual item. Contextual selection becomes especially useful when you structure your HTML with section tags like header, section, article and footer. 

Pay attention to the styles of the paragraphs and lists in the following example:

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/46a1028808b949b9af0061a363d40b8a/8c35f24ecbd746c1a0106f1c4ce9e1b0/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40096e999e5b21437b8b86bc0e4f12b730">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c5e971447c473f55ca8f0b39e3ab624b/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/3-4_contextual_selectors.PNG" style="margin: 0.1em;" alt="Contextual selector example output" title="Contextual selector example output" width="350">
  </a></div>
</div>


### Activity 




### Cascading styles




### Activity 




## 3.5 Style studies

### Images




### Forms




## 3.6 Project 3 - My profile




## 3.7 Conclusion and exercises

### After this module you should be able to...




### Exercises (1-5)




### Exercises (6-10)




### Exercises (11-15)



