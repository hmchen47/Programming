# Module 2: Attributes, images and links


## 2.1 Introduction to Module 2

### Welcome to Module 2

<video src="https://edx-video.net/W3CHTM502016-V014600_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@7f247e6d116540ba8b4c263a05631dea/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Meaningful Web pages

Tags and elements are building blocks of HTML5. However, they can be made so much more exciting with attributes. Let's take a simple element like list. You know how to add one to your page but can you change the order of your list? Or change it to an alphabetically ordered list instead of a numerical list? Can you display your list in reverse order? Yes, you can do all this and more using attributes.

Apart from exploring attributes for elements, we will continue to add life to our Web page by adding images and hyperlinks and learning about how to use and place them properly in your Web page.

In this module, we will also look at creating meaningful Web pages. Imagine you are the Web page designer of an online magazine. You want to have a central article, some aside commentary, captions, a summary of your article, addresses and citations. You also want to provide more detailed information such as, 'This sentence is really important and you need to convey that to the reader'.

If we just use `<p>` tags and header tags, `<h1>` to `<h6>`, visually it might look like what you want, but only a human will be able to read and understand the page. To a browser, there is very little information except that there is text and headings in your page. How can a search engine know what is important? Does a visually impaired person have to listen to the entire page or can just jump to the article?

It is very important to style your Web pages for search engines to improve your SEO rankings and for visually impaired people who access your Web page using assistive technology like screen readers. Semantic markup enables all of this and more.  


### Module 2 - Content

2.1 __Introduction__: Check out this video explaining what you'll be learning about in Module 2 - and wrap your mind around the concept of "semantic markup".

2.2 __Attributes__: Here you will build on to what you have already learned about attributes.

2.3 __Semantic meaning__: Explaining the difference between 'semantic' and 'style'.

2.4 __Images__: Learn how, when, and where to best utilize images in your Web pages.

2.5 __Hyperlinks__: They are the connections that allow the world to jump from place to place on the Web. Explore the secrets of this powerful mechanism!

2.6 __Exercises__ - Module 2: Lets check what you've learned during Module 2.


## 2.2 Attributes

### Introduction to attributes

We learned a little bit about what attributes are in the previous module. Let's look into it in more depth, by using examples.

Here is an ordered list:

```html
<ol>
  <li>Lights</li>
  <li>Camera</li>
  <li>Action</li>
</ol>
```

Output:

<ol>
  <li>Lights</li>
  <li>Camera</li>
  <li>Action</li>
</ol>

If i want an ordered list to start with the number 5 instead of 1 (as it does by default), let's code like this:

```html
<ol start="5">
  <li>Lights</li>
  <li>Camera</li>
  <li>Action</li>
</ol>
```

Output:

<ol start="5">
  <li>Lights</li>
  <li>Camera</li>
  <li>Action</li>
</ol>

Here, using the `start` attribute, we made our list start with 5 instead of 1.

Like `start`, we have many useful attributes we will see in this section that can affect your element. Attributes are a significant part of HTML. Tags and attributes make up the language. 


#### Syntax

Attributes are used in tags to further define the tag:

+ It is used inside the opening tag it is applied to and should be added after a space from the tag name: `<ol start="5">`. The start attribute is used inside the `<ol>` tag. 
+ `start="5"`<br/>Attribute name, equal sign, opening quote, attribute value, closing quote
+ Attributes are a name-value pair:` start="5"`<br/>name: start>br>value: any positive integer
+ The only exception to the name-value pair is if the attribute is a 'boolean attribute'. These attributes have only two types of values - true or false. But instead of writing "true" or "false" for its value, you add the attribute name to indicate true and omit it to indicate false. An example is the 'reversed' attribute in an ordered list `<ol>`. Adding this attribute is an indication that the list order should be reversed (in descending order).

  ```html
  <ol reversed></ol>
  ```

+ A tag can have multiple attributes:
  ```html
  <ol start="5"></ol>
  <ol id="cinema" class="attribute-list" start="5"></ol>
  <ol start="5" class="attribute-list"></ol>
  ```


#### Example 1: the 'id' attribute

Imagine you have two paragraphs in your HTML page:

```html
<p>I am paragraph 1 and I want to be in red</p>
<p>I am paragraph 2 and I want to be in blue</p>
```

Your task is to make the text color of the first paragraph <span style="color: red;">red</span> and the other <span style="color: blue;">blue</span>. How do we do that? You add styling to your HTML document through CSS. CSS is a style sheet language where you add any presentation related information for your HTML document. You will learn about this in the next chapter. In this case, you will have to write code in your style sheet to inform that it needs to change the text colors respectively. 

But to identify each paragraph, we need to give them each a name first so we can instruct our style sheet to make X red and Y blue. This unique name we give each element is called an 'ID'. This is very similar to your school or corporate ID that is unique to you. No one else in your company will have the same ID as you. id is an attribute. It should be unique to the element because we know that two people having the same ID will just cause a lot of confusion. 

```html
<p id="para1">I am paragraph 1 and I want to be in red</p>
<p id="para2">I am paragraph 2 and I want to be in blue</p>
```

Here, we can style `para1` and `para2` separately using CSS. The id attribute helps us do this by letting us give each paragraph an ID.


#### Example 2: the 'class' attribute

A similar attribute is `class`. `class` like `id` is a very useful attribute and one you will be using very frequently. Let's assume you are an author of a book. You like poems and you want to include at least 20 of them in your new book. You add IDs for them: 'poem1', 'poem2', 'poem3'.

You want your poems to look different from your other text. Grey text color, italic and bold. Like this:

<p style="text-rendering: optimizeLegibility; margin-right: 0px; margin-left: 0px; padding: 0px 0px 0px 30px; border: 0px; outline: 0px; font-stretch: inherit; font-size: 16px; font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; vertical-align: baseline;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline; color: #808080;"><em style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;"><strong style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;">To move, to breathe, to fly, to float,</strong></em></span><br style="text-rendering: optimizeLegibility; line-height: 24px; color: #111111; font-family: Verdana, Helvetica, Arial, sans-serif; font-size: 15px; background-color: #fef3ea;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline; color: #808080;"><em style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;"><strong style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;">To gain all while you give,</strong></em></span><br style="text-rendering: optimizeLegibility; line-height: 24px; color: #111111; font-family: Verdana, Helvetica, Arial, sans-serif; font-size: 15px; background-color: #fef3ea;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline; color: #808080;"><em style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;"><strong style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;">To roam the roads of lands remote,</strong></em></span><br style="text-rendering: optimizeLegibility; line-height: 24px; color: #111111; font-family: Verdana, Helvetica, Arial, sans-serif; font-size: 15px; background-color: #fef3ea;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline; color: #808080;"><em style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;"><strong style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;">To travel is to live.</strong></em></span></p>

So all poems have the same requirements.

If you use id attribute, you can instruct the stylesheet to style each poem in a particular way. It will look something like (we will learn how to write proper styles in the next chapter, so for now we will just phrase it in English) -

<p style="padding-left: 30px;">'Make poem1's&nbsp;text color grey, italic and bold'<br> 'Make poem2's&nbsp;text color grey, italic and bold'<br>'Make poem3's&nbsp;text color grey, italic and bold'</p>

Can you imagine how repetitive your style sheet will look if you have to instruct it to do the same thing 20 times for different poem IDs? HTML makes it easier. We use the class attribute. Let's name this class of poems 'poetry'. 

<p id="poem1" class="poetry">To move, to breathe, to fly, to float...</p>
<p id="poem2" class="poetry">Roses are red, violets are blue...</p>
So now, all you have to do in your style sheet, is to instruct it to make all elements belonging to the 'poetry' class grey, italic and bold. 

#### Knowledge check 2.2.1

```html
<ol id="student-male" class="primary" start="10"></ol>
<ol start="10" class="primary" id="student-male"></ol>
```

True or False? Both tags will give the same output. The order in which the attributes are specified in the opening tag does not matter.

  Ans: True, xFalse<br/>
  Explication: As long as they are specified in the start tag, their order does not matter. Most are a name-value pair but for some like 'reversed' (boolean attribute), just their presence can affect the element.



### Global & non-global attributes

You have seen a few examples of attributes now: `start`, `id` and `class`. All HTML elements have attributes.

There are two kind of attributes:

+ Global
+ Non-global


#### Global attributes

Global attributes can be applied to __all tags__. They are common attributes. Examples of global attributes are id and class. There are many more global attributes. Here is a [list of all the global attributes](https://www.w3.org/wiki/HTML/Attributes/_Global) and the values they accept. 

So attributes like `id` and `class` can be applied to any HTML tag.
<pre style="padding-left: 30px;"><span style="line-height: 25.6px;">&lt;p id="para1" class="poetry" lang="en"&gt;The global attribute lang takes language codes for values. The code for English is 'en'.&lt;/p&gt;<br><br>&lt;html lang="fr"&gt;&lt;/html&gt; </span>- The language attribute tells the browser that the contents of this document will be in french.</pre>


#### Non-global attributes

Non-global attributes are attributes applied to a specific instance of a tag. It can be applied to one or more tags. For example, `start` is an attribute for the `<ol>` tag and it cannot be applied on the `<p>` or `<h1>` tags, it is specific to only ordered lists `<ol>`. Another attribute specific to the `<ol>` tag is reversed, which we learned in the last unit as an example of a boolean attribute. The non-global attribute width can be applied to several tags such as `<img>`, `<input>` and `<video>`.

Without the boolean attribute `reversed`:

```html
<ol>
   <li>HTML5</li>
   <li>CSS</li>
   <li>JavaScript</li>
</ol>
```

With the boolean attribute reversed:

```html
<ol reversed>
   <li>HTML5</li>
   <li>CSS</li>
   <li>JavaScript</li>
</ol>
```

[Example Code](src/2.2.2-Attributes.html)

Ordered lists have their own specific attributes and all global attributes can also be applied to them.


#### More examples

The image `<img>` and hyperlink `<a>` elements, which we will be learning about shortly, have many non-global attributes of their own.

<strong>&lt;img&gt;</strong>  :  `src`, `alt`, etc.

<strong>&lt;a&gt;</strong>  : `href`, `target`, `download`, etc.

Other than the common global attributes, if you wish to learn about the supported non-global attributes for any element, you can visit the [W3C HTML5 recommendation](https://www.w3.org/TR/html5/dom.html#global-attributes) or the [HTML attribute reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes) available at the Mozilla Developer Network (MDN).

__Important__: Throughout the course, using the MDN attribute reference, you are encouraged to explore non-global attributes for the elements you learn about or would like to use in your Web pages. In the MDN attribute reference list, you can click on the element's hyperlinked name to be navigated to its page that lists supported attributes for that element.

__Try this__: Navigate to the [HTML attribute reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes) at Mozilla Developer Network and find out which element(s) the attributes muted and readonly can be applied to. 

__Try this__: Navigate to the [HTML attribute reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes) at Mozilla Developer Network and find out the non-global attributes that can be applied to the `<li>` tag. If you click on the `<li>` element, it will take you to the list tag's page that specifies applicable attributes.


### Global attributes: examples

#### Global attribute: 'id'

Like we saw in the previous unit, here is a [list of all the global attributes](https://www.w3.org/TR/html5/dom.html#global-attributes) and the values they accept. To understand attributes, we considered an example of usage `id` and `class`. We are going to look at it in depth here and discuss another global attribute `title`.

The id attribute gives your element a unique identifier. In your HTML document, that ID value can only be used in one element. 

Naming rules for `id` attribute:

+ Must be of at least one character
+ Should not contain any spaces
+ Values are case-sensitive. This means 'QuestioN' and 'question' are NOT the same. That does not mean you can use two different IDs that only differ by case, i.e. "myid" and "MyId". They are different and so legal but extremely confusing!

```html
<p id="question-about-html">How many times can a particular 'id' value be used in a HTML document?</p>
<p id="html-answer">Once</p>
```

`id` is primarily used for:

1. Styling your element. You can specify the style you want for the element in your style sheet by referencing the 'id'.

  Using CSS, you can specify code that will give different styles to "question-about-html" (eg: black text, center-aligned) and "html-answer"  (eg: green text)

2. Specifying a link target. We will be learning about hyperlinks later in this section. You can link to a section of your HTML page using the 'id' of the section. You should reference the 'id' value with a number sign preceding it - '#id-value'

  ```html
  <a href="#introduction">1.1 Introduction</a> 
    <!-- This is a hyperlink element which we will learn about later in this week -->
  <p id="introduction">This paragraph is the Introduction to the Web page</p>
  ```

3. In JavaScript, 'id' can be used to manipulate an html element. Using the 'id' of the element, you can write JavaScript code to make it perform an action, i.e. change the text within paragraph tags.


#### Global attribute: 'class'

The class attribute, while similar to id, groups a set of elements in the same class. It's name-value pair is class="classname". Unlike id, which is unique to the element,  the same class name can be assigned to more than one element.

For example:

```html
<p class="question">What is your name?</p>
<p class="question">Do you like HTML5?</p>
```

Both paragraphs above are grouped under the class named 'question'. An element can have one or more class names. If we also want the second question to be under the 'html' class because it is a html related question, you can add two class names by separating them by space:

```html
<p class="question html">Do you like HTML5?</p>
```

Naming rules for `class` attribute:

+ Must begin with a letter (a-z or A-Z)
+ First letter can be followed by a letter, digit, hyphen or underscore
+ Values are case-sensitive

class is primarily used for:

1. Styling your elements. You can specify the style you want for all the elements that belong to the class in your stylesheet. 

  ```html
  <p class="question">Who are you?</p>
  <p class="answer">I am the author</p>
  <p class="question html">Do you like HTML5?</p>
  <p class="answer">Yes</p>
  ```

  In your CSS, you can include code to style your classes like this:

  + 'question' class: text color is black and text is bold
  + 'answer' class: text color is green
  + 'html' class: text color is red

  The code above will look like this:

  <p style="padding-left: 60px;"><strong><span style="line-height: 25.6px;">Who are you?</span></strong></p>

  <p style="padding-left: 60px;"><span style="line-height: 25.6px; color: #339966;">I am the author</span></p>

  <p style="padding-left: 60px;"><span style="color: #ef0000;"><strong>Do you like HTML5?</strong></span></p>

  <p style="padding-left: 60px;"><span style="color: #339966;">Yes</span></p>

  The 'Do you like HTML5?' question has styles for both classes 'question' and 'html' applied to it.

2. In JavaScript, `class` can also be used to manipulate html elements of the same class. 


#### Global attribute: 'lang'

The lang attribute indicates the language of the text in the element to which it is attached.  Identifying the language of content is increasingly important, as browsers adapt styling and other aspects of the user's experience according to the language of the content. 

For example, if you create a page in Japanese, the browser will automatically apply a font that produces Japanese shapes for the characters, rather than Chinese shapes – but only if you have told it that your content is in Japanese. Various presentational aspects also require a knowledge of the language of the content: for example, CSS will style content differently for line-breaking, hyphenation, and text-transforms depending on the declared language. Other features, such as spell-checking and voice-browsers for visually-challenged people, also work differently according to which language the content is in.  For more details see [Why use the language attribute?](https://www.w3.org/International/questions/qa-lang-why)

The value of a lang attribute must be a language tag that is composed of one or more subtags defined in the [IANA Language Subtag Registry](http://www.iana.org/assignments/language-subtag-registry). Multiple subtags are separated by hyphens.  (Do n__ot use the ISO lists of languages and countries! Those lists are already subsets of the IANA registry.) You may find it easier to look up subtags using the unofficial [Language Subtag Lookup](https://r12a.github.io/app-subtags/) tool.

You should __always declare the language of your page in the `<html>` tag__.  You can also declare the language of content within the page by attaching a lang attribute to an element that surrounds it.

For example:

```html
<html lang="en-GB">...</html>
<p>In French you'd say <span lang="fr">On voit souvent des chats sur le Web.</span></p>
```

The first example above shows how you can qualify the language (English) with a region subtag (GB) to specify British English.  This distinction can be useful for spellchecking your source. You can also add other subtags, such as scripts and variant labels to further refine the language. However, the golden rule is to always keep the lang value as short as possible, and only use additional subtags when you have a good reason (ie. use just ja for Japanese, not ja-JP). For more information, see the article [Declaring language in HTML](https://www.w3.org/International/questions/qa-html-language-declarations).

The second example shows how you could specify a change of language within the document.  This would help a voice browser pronounce the French word 'chats' correctly, meaning 'cats' and not 'chats' in English.


#### Global attribute: 'title'

Try this: Place your cursor on the word and then on the picture below. Don't click on it, just rest your cursor there. 

Example image of a girl with a beautiful smile to illustrate title attribute

Did you see the two secret messages? A message that appears when you point your cursor at something is called a tooltip. Be it a paragraph, header, image or any element, the title attribute is used to provide additional information about it. It is very useful to elaborate abbreviations or add some context. For images, you must use an alt attribute as there is no guarantee that the title attribute is presented to assistive technology users. The title can be of any text value. 

```html
<abbr title="National Aeronautics and Space Administration">NASA</abbr>
```

#### Knowledge check 2.2.3

```html
<p id="greeting" class="hello world">This is me greeting the world</p>
```

Which of the following is the correct behavior with respect to the code above?

1. Both the classname and paragraph text cannot contain "world"
2. Two different classes "hello" and "world" will be applied to the paragraph
3. The code is invalid because space is not allowed in class attribute's value
4. One class "hello world" will be applied to the paragraph

  Ans: 2 <br/>
  Explanation: If there is a space between classes, they will be treated as two different classes - "hello" and "world". In this case, both classes will be applied to the paragraph.
  

### Global attributes

References for video below:

+ [W3C Cheatsheet](https://www.w3.org/2009/cheatsheet/)
+ [MDN Attribute Reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)

<video src="https://edx-video.net/W3CHTM50/W3CHTM502016-V005600_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width="180">
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@17f73d8ba52c4569967a94db806240a0/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Activities - Attributes

Please find below suggested activities to help you practice:

1. Find the list of supported attributes for the `<area>` tag. (Hint: use the [W3C cheatsheet](https://www.w3.org/2009/cheatsheet/) or [MDN attribute reference list](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes))

  Attributes: alt, coords, ping, referrerpolicy, rel, shape, target

2. Create two paragraphs with the same `id` and run your code in a CodePen. What happens? We know the value of the `id` attribute must be unique, so why does it behave the way it does? Run your code through the [W3C Markup Validator](https://validator.w3.org/#validate_by_input). Does it throw an error?

  [Example code](src/2.2.5-AttributesID.html)

  ```txt
  Error: Duplicate ID idtest.
  </p>↩↩  <p id="idtest">Method
  ```

3. Does an attribute called `src` exist? What is the purpose of this attribute and what are the elements it can be applied to? (Hint: refer to the [W3C HTML5 specification](https://www.w3.org/TR/html5/index.html#contents), [W3C cheatsheet](https://www.w3.org/2009/cheatsheet/) or [MDN attribute reference list](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes))

  + src: The URL of the embeddable content; Valid non-empty URL potentially surrounded by spaces
  + Elements: audio, embed, iframe, img, input, script, source, track, video

4. Create an ordered list starting with the number 11. Then, reverse the list. Give it the following title (when you hover your mouse, it should display the title as a tooltip): 'Activity List'.

  [Example Code](src/2.2.5-ArttributesList.html)

Note: If you wish to share your HTML code in the discussions, you can paste your code directly in a discussion forum post (highlight code and Ctrl+K/use the code widget) or use one of the following online code editors:

+ JS Bin: http://jsbin.com (JS Bin tutorial)
+ CodePen: http://codepen.io (CodePen tutorial)

These are HTML, CSS, and JavaScript code editors that preview/showcase your code bits in your browser. It helps with cross-device testing, realtime remote pair programming.



## 2.3 Semantic meaning

### Separating content & style



### Introduction to semantic elements



### New HTML5 semantic elements



### Differentiating semantic elements



### &lt;article&gt; and &lt;section&gt; elements



### &lt;div&gt; and &lt;span&gt; elements



### Activities - Semantic meaning



## 2.4 Images

### Introduction to images



### Attribute: alt



### Attributes: title, height & width



### Decorative images



### Using &lt;img&gt; tags



### Activities - Images



## 2.5 Hyperlinks

### Introduction to hyperlinks



### Attributes: href and target



### Attributes: media and download



### Use of hyperlink attributes



### Activities - Hyperlinks



### Recipe project - Module 2



## 2.6 Exercises - Module 2


### Attributes (1-9)



### Semantic elements (10-16)



### Images (17-24)



### Hyperlinks (25-28)


