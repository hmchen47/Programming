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




### Global attributes



### Activities - Attributes



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


