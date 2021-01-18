# Module 1: Introduction to JavaScript

## 1.2 JavaScript, HTML and CSS

### 1.2.1 HTML is for structure

#### The "Hyper Text" part: links!

A fundamental key to the World Wide Web is the concept of "hypertext".  Hypertext is built on the idea of linking information together, not unlike using footnotes, but far easier and more flexible. The idea is to "mark up" your document with links and define how to break it down into different segments (chapters, sections, paragraphs, tables, figures, etc.)

That's why, in 1989, Tim Berners-Lee began to create a definition of HTML: Hypertext Markup Language, to provide a simple, uniform way to incorporate hyperlinks into a text document.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y6osf6ba')"
    src    ="https://tinyurl.com/y3z2mp8m"
    alt    ="Illustration of hypertext documents"
    title  ="Illustration of hypertext documents"
  />
</figure>

He envisioned a technology that would facilitate thoroughly interconnected documents. He wanted authors to be able to connect an idea in one document to the source of the idea in another, or connect a statement with the data that backs up that statement. Traditionally this kind of thing was done with footnotes and bibliographies, which can be cumbersome. This information should be easily transferable from one place to another, so that in reading one document, it is easy to access everything related (linked) to it. Tim Berners-Lee imagined a "Web" of interconnected documents.

He used the metaphor of a Web to emphasize the importance of connections between documents. It was not just a long list of details, but rather a sea of information stretching out in all directions. This sea of information was navigated by a new tool called a "browser".

#### The "Markup" part : elements, tags and attributes!

So the "M" in HTML stands for "Markup", but what does Markup really mean?  Essentially it means to annotate a document with extra information: things like where different sections and paragraphs begin and end, which part is the title, which things should be emphasized and so on.

There are many ways to markup a document, but HTML borrows a technique from an ancestor language, SGML ([Standard Generalized Markup Language](https://en.wikipedia.org/wiki/Standard_Generalized_Markup_Language)), which uses angle brackets ("<" and ">") to separate the annotations from the regular text.  In HTML these annotations are called "tags".

For example, consider the following chunk of HTML code (note: you can edit the source code and see the resulting Web page updating in real time): [Local Example - tags](src/01b-example01.html)

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li style="margin-bottom: 0px;" value="1">&nbsp; &nbsp;&lt;body&gt;</li>
<li style="margin-bottom: 0px; font-family: 'Courier New'; list-style-type: none; background: #eeeeee;">&nbsp; &nbsp; &nbsp; &lt;h1&gt;A Tale of Two Cities&lt;/h1&gt;</li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: cyan;">&lt;p&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; It was the best of times, it was the worst of times, . . . .</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: cyan;">&lt;/p&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp; &nbsp; . . .</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: cyan;">&lt;p&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; . . . it is a far, far better rest</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; that I go to than I have ever known.</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: cyan;">&lt;/p&gt;</span></li>
<li style="margin-bottom: 0px;"><span style="color: cyan;">&nbsp;&nbsp; &lt;/body&gt;</span></li>
</ol></div><br/>

If you eliminated everything in between the angle brackets from the text, for most purposes it would still read the same:

<pre><code>A Tale of Two Cities</code><br>It was the best of times, it was the worst of times . . . .<br>  . . .<br>. . . it is a far, far better rest<br>    that I go to than I have ever known.</pre>

Once you know that everything in angle brackets is "meta-information", it gives you a lot of flexibility. You can put a lot of different things in between those brackets without any of it showing up (directly) in your finished document. And though you don't usually see directly what's in those angle brackets, they can often have a big effect on how your Web page looks, as well as how it responds and interacts with you.

Here is another, more generic example:

_Notes:_

+ Remember that the first line of your HTML5 page should start by `<!DOCTYPE html>`. CodePen does not force you to add a DOCTYPE on CodePen, but be assured that you have to specify the DOCTYPE in all your Web documents.
+ You can modify the source code in the [Demo File](src/01b-example02.html), and see the results in real time.

<br/>
<div><ol>
<li style="margin-bottom: 0px;" value="1"><span> </span><span>&lt;!DOCTYPE html&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span><span>&lt;html</span><span> </span><span>lang</span><span>=</span><span>"en"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&lt;head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; &nbsp; </span><span>&lt;title&gt;</span><span>Your first HTML page</span><span>&lt;/title&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; &nbsp; </span><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>/&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&lt;/head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&lt;body&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&lt;h1&gt;</span><span>My home page</span><span>&lt;/h1&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&lt;h2&gt;</span><span>Who am I?</span><span>&lt;/h2&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp; </span><span>&lt;p&gt;</span><span>Hi! Welcome to my Home Page! My name is Michel Buffa, I'm a professor at the University of Nice, in France, and I'm also the author of two MOOCS about HTML5 on W3Cx.</span><span>&lt;/p&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp; </span><span>&lt;p&gt;</span><span>I also play electric guitar and love coding WebAudio applications...</span><span>&lt;/p&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp; </span><span>&lt;img</span><span> </span><span>src</span><span>=</span><span>"https://pbs.twimg.com/profile_images/110455194/n666194627_2302_400x400.jpg"</span><span> </span><span>width</span><span>=</span><span>200</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp;&nbsp; </span><span>alt</span><span>=</span><span>"Michel Buffa plays rock and roll"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&lt;h2&gt;</span><span>My Hobbies</span><span>&lt;/h2&gt;</span></li>
<li style="margin-bottom: 0px;"><span> Music, Movies, Video Games, Travelling, Family, etc.</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&lt;/body&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&lt;/html&gt;</span></li>
</ol></div><br/>

#### Coding Tools

It's time to write your first HTML code :-)

You can use a source code editor like [Sublime Text](https://www.sublimetext.com/), [Atom](https://atom.io/), [Brackets](http://brackets.io/) or any lightweight text editor. You can also use more "professional" tools such as [Visual Studio Code](https://code.visualstudio.com/), [NetBeans](https://netbeans.org/), [Eclipse](https://eclipse.org/downloads/), [WebStorm](https://www.jetbrains.com/webstorm), etc.

To try out the simple examples from this course, I'd suggest using an online IDE such as [JSBin](https://jsbin.com/), [CodePen](https://codepen.io/), [Plunker](https://plnkr.co/), etc.

During the course, we will show you how to test out simple code snippets in online IDEs, but we will also teach you how to organize your code with folders and files.

The next video shows how you can use JsBin, CodePen, and SublimeText in order to test the HTML code provided earlier in this section.

#### Live coding video: using the course's tools

<a href="https://edx-video.net/W3CJSIXX2016-V000100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y44skxok)


#### HTML elements

If you are sitting at a coffee shop next to a table of Web developers, you will probably often hear these three words: "Elements", "Tags" and "Attributes".

"Elements" are the pieces themselves, i.e. a paragraph is an element, a header is an element, even the body is an element. Most elements can contain other elements, as the body element would contain header elements, paragraph elements, in fact pretty much all of the visible elements of the Document Object Model (that developers refer to as the "DOM").

As an example, let's look at a simplified version of the last HTML code we presented earlier: 

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;title&gt;</span><span class="pln">Your first HTML page</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">/&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;h1&gt;</span><span class="pln">My home page</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;p&gt;</span><span class="pln">Hi! Welcome to my Home Page! My name is Michel Buffa, I'm a professor at the University of Côte d'Azur, in France, and I'm also the author of three W3Cx MOOCS.</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br/>

Click the red circle next to HTML to unfold this HTML document structure (we can also say "see its DOM structure"): ([Demo File - DOM Structure](src/01b-example03.html))

Consider the figure above. It contains a single `html` element. It turns out this includes within it the entire content of your html file. If you click on the "html" red node, you'll find that it contains two components, a `head` and a `body`. Clicking on each of those will reveal their respective contents. This structure is what we computer scientists call a "tree". Any given element (except for the outermost "html" element) is wholly contained inside another element, referred to as the "parent" element. Not surprisingly, the elements contained within a given element are its "child" elements. And, yes, children of a common parent are often referred to as "siblings".

Thus in the example above, the top element is the `html` element, which contains just two elements, the `head` and `body`.  The `head` element contains a `title` element and the body contains an `h1` element and a `p` element.  In a more typical example, the body would contain many more children, but for our purpose this is enough. `p` is for "paragraph" (the text between `<p>` and `</p>` will be separated by some space before the next element is displayed in the final HTML page rendering), `h1` means "heading level 1", and will be rendered by default in bold with a bigger char size than any other text element, etc.

That may be a great picture, but how do we represent such a structure in a text file?  Well, that's where "tags" come in.

#### HTML tags

"Tags" are what we use to organize a text file (which is just a long string of characters) such that it represents a tree of elements that make up the html document. Tags are not the elements themselves, rather they're the bits of text you use to tell the computer where an element begins and ends. When you "mark up" a document, you generally don't want those extra notes that are not really part of the text to be presented to the reader.

HTML borrows a technique from another language, SGML, to provide an easy way for a computer to determine which parts are "MarkUp" and which parts are the content. By using "<" and ">" as a kind of parentheses, HTML can indicate the beginning and end of a tag, i.e. the presence of "<" tells the browser "this next bit is markup, pay attention".

Whatever that tag (or "open tag") does, it applies to the content following the tag. Unless you want that to be the entire rest of the document, you need to indicate when to stop using that tag and do something else, so "<" and ">" are used again. Since elements are typically nested within other elements, the browser needs to be able to distinguish between the end of the current tag and the beginning of a new tag (representing a nested element). This is done by adding a "/" right after the "<" to indicated that it's a "close tag". To indicate the beginning and end of a paragraph (indicated by the single letter "p") you end up with something like this:

<div><ol>
<li value="1"><span>&lt;p&gt;</span><span>This is my first paragraph!</span><span>&lt;/p&gt;</span></li>
</ol></div>

The browser sees the letters "`<p>`" and decides "A new paragraph is starting, I'd better start a new line and maybe indent it". Then when it sees "`</p>`" it knows that the paragraph it was working on is finished, so it should break the line there before going on to whatever is next.

For example, the "`<em>`" tag is used for element that needs Emphasis.  The  "<" and ">" indicate that this is a tag, and the "little bits of text" in between tell us what kind of tag it is.  To completely describe the element, it needs an open and close tag, and everything in between the tags is the contents of the element:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y6osf6ba')"
    src    ="https://tinyurl.com/yyo882n2"
    alt    ="Diagram of an element"
    title  ="Diagram of an element"
  />
</figure>

Most tags have open and close versions, but there are a few strange ones.  For more info, we strongly recommend that you follow the W3Cx [HTML5&CSS Fundamentals](https://www.edx.org/course/html5-and-css-fundamentals) course, but we generally refer to the strange ones as "self closing" tags.   Usually these tags represent an element that is completely described by its attributes, and thus there is no need for other content.  So if you see something like this:

<div><ol>
<li value="1"><span>&lt;img</span><span>&nbsp;src="https://goo.gl/pVxY0e" alt="Floating Flower"</span><span>/&gt;</span></li>
</ol></div>

... then you should know that the slash at the end of the open tag is sort of a shorthand for a close tag, so you won't see any other indication that this element is now complete. There are also a few tags that don't even use the "/" at the end, they just don't have any close tag at all.  This works because all of the information this tag needs is declared in an "attribute".

The `<img>` tag is one of them, the "/" at the end is optional and can be removed entirely, this will still be [valid HTML5](https://w3c.github.io/html/syntax.html#void-elements).

<div><ol>
<li value="1"><span>&lt;img</span><span>&nbsp;src="https://goo.gl/pVxY0e" alt="Floating Flower"</span><span>&gt;</span></li>
</ol></div>

These elements, without a "/" at the end, are called "void elements". They are : `area`, `base`, `br`, `col`, `embed`, `hr`, `img`, `input`, `link`, `menuitem`, `meta`, `param`, `source`, `track`, `wbr`.

#### HTML attributes

Most of what you can learn about HTML attributes is presented in [the three W3Cx MOOCs about HTML5](https://www.edx.org/school/w3cx) (fundamentals, coding essentials, and advanced techniques), but we can introduce the idea briefly in this JavaScript course. Basically, a given element on your Web page can be distinguished by any number of unique or common attributes. For example, we've already seen how an image can be inserted in your Web page, and in that example we used the `width` attribute of the `<img>` tag in order to constrain the `width` of the image:

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;img</span><span> </span><span>src</span><span>=</span><span>"https://pbs.twimg.com/profile_images/110455194/n666194627_2302_400x400.jpg"</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; &nbsp;width</span><span>=</span><span>200 alt="Michel Buffa plays rock&amp;roll"</span><span>&gt;</span></li>
</ol></div>

As you might guess, the `<img>` tag also has a height attribute, as well as others. Different HTML tags share some common attributes that we'll meet in the next section, which are particularly useful when coupled with CSS (id and class) for applying graphic styles (color, shadow, etc.), but  can also have specific attributes (for example: the src attribute can be found in the `<video>`, `<audio>`, `<img>` tags but not on a `<p>` or on an `<h1>` tag!)

Try changing the value of the width attribute in the example below, or add a height attribute, and see the result:

[Local Demo Exxample - Image](src/01b-example04.html)


#### Live coding video: creating a simple Web page using common tags and attributes

<a href="https://edx-video.net/W3CJSIXX2016-V000200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://courses.edx.org/courses/course-v1:W3Cx+JS.0x+2T2020/xblock/block-v1:W3Cx+JS.0x+2T2020+type@video+block@94922dbc74b14fe8b24c59c9986a3114/handler/transcript/download)


Note : there is a small error in the live coding video.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y6osf6ba')"
    src    ="https://tinyurl.com/y6ounvnr"
    alt    ="Error in HTML"
    title  ="Error in HTML"
  />
</figure>

This shows a `<h2>` heading and `<ol>` nested in a `<p>` paragraph, I did not notice that while shooting the video. The closing tag </p> should therefore be moved before `<h2>` starts, and not be placed after `<h2>` and `<ol>` as demonstrated on the video. 

Michel Buffa

#### Notes of 1.2.1 HTML is for structure

+ Hypertext
  + fundamental key to the WWW
  + idea:
    + linking information together: far easier and more flexible
    + "mark up" document w/ links
    + define how break document down into different segments (chapters, sections, paragraphs, tables, figures, etc.)
  + Tim Berners-Lee (1989): Hypertext Markup Language, to provide a simple, uniform way to incorporate hyperlinks into a text document
    + thoroughly interconnected documents
    + traditionally done with footnotes and bibliographies but cumbersome
    + information easily transferable from one place to another
    + easy to access everything related (linked) to it
    + imagined a "Web" of interconnected documents
  + browser: a tool to navigate the sea of information

+ Markup documents
  + annotating a document w/ extra info
  + components: elements, tags & attributes
  + many ways to makup a document
  + HTML utilizing SGML syntax
    + using angle brackets ("<" and ">") to separate the annotations from the regular text
    + these annotations called "tags"
  + meta-information: everything in angle brackets
  + putting things in btw those brackets w/o showing up (directly) in the finished document
  + tags:
    + big effect on how Web page looks
    + how document responds and interacts with users

+ Popular coding tools
  + source code editors
    + [Sublime Text](https://www.sublimetext.com/)
    + [Atom](https://atom.io/)
    + [Brackets](http://brackets.io/)
    + any lightweight text editor
  + professional tools
    + [Visual Studio Code](https://code.visualstudio.com/)
    + [NetBeans](https://netbeans.org/)
    + [Eclipse](https://eclipse.org/downloads/)
    + [WebStorm](https://www.jetbrains.com/webstorm)
    + etc.
  + online IDE
    + [JSBin](https://jsbin.com/)
    + [CodePen](https://codepen.io/)
    + [Plunker](https://plnkr.co/)
    + etc.

+ HTML elements
  + the pieces themselves
  + examples: a paragraph, a header, even the body
  + able to contain other elements
  + all of the visible elements of the Document Object Model (DOM)
    + tree diagram
    + any given element contained inside another elements, except for the outmost "html" element
    + child elements: elements contained within a given element
    + sibling: children of a common parent element

+ HTML Tags
  + used to organize a text file s.t. representing a tree of elements
  + not the element themselves
  + the bits of text to tell the computer where an element begins and ends
  + when marking up a document, none these extract notes displayed
  + SGML providing an easy to determine
    + which parts are "MakUp"
    + which pars are the contents
  + by using "<" and ">" to indicate the begining and end
  + adding "/" right after the "<" to indicate a close tag
  + example: `<p>This is my first paragraph!</p>`
    + `<p>`: a new paragraph starting and starting a new line
    + `</p>`: the paragraph working on finished and braking the line
  + illustration of a tag

    <figure style="margin: 0.5em; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
        onclick="window.open('https://tinyurl.com/y6osf6ba')"
        src    ="https://tinyurl.com/yyo882n2"
        alt    ="Diagram of an element"
        title  ="Diagram of an element"
      />
    </figure>

  + self-closing tags
    + most tags w/ open and close versions
    + some tags representing an element completely described by its attributes $\implies$ no need for content
    + using "/" before ">" to indicate the complete of the tag
    + example: `<img src="https://goo.gl/pVxY0e" alt="Floating Flower"/>`
  + void elements
    + elements w/o a "/" at the end
    + all info required declared in an "attribute"
    + example: `<img src="https://goo.gl/pVxY0e" alt="Floating Flower">`
    + including: `area`, `base`, `br`, `col`, `embed`, `hr`, `img`, `input`, `link`, `menuitem`, `meta`, `param`, `source`, `track`, `wbr`

+ HTML attributes
  + a given element dinguiashed by any number of unique or common attributes
  + example: `<img src="n666194627.jpg" width=200 alt="Michel Buffa plays rock&roll">`
    + `width` attribute: constraint the width of an image
  + different tags sharing some common attributes and w/ specific attributes
  + shared attributes useful when coupled w/ CSS (id & class)

#### Knowledge check 1.2.1 

1. HTML tags and HTML elements the same thing. True or false?

  Ans: False<br/>
  Explanation: No, tags are not the elements themselves. They are the bits of text you use to tell the computer where an element begins and ends; they are enclosed between the < and > characters.

#### Knowledge check 1.2.2

1. The HTML structure of a document is a tree. (Correct/Incorrect)

  Ans: Correct<br/>
  Explanation: The structure of an HTML document is a "tree". Any given element (except for the outermost "html" element) is wholly contained inside another element, referred to as the "parent" element.



### 1.2.2 CSS is for style

#### Live coding video: using CSS to style HTML elements

<a href="https://edx-video.net/W3CJSIXX2016-V000300_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y6z8xyhz) <br/>


CSS, or <b>C</b>ascading <b>S</b>tyle <b>S</b>heets, is a style sheet language used to describe the way an HTML or XML document should look to a user. CSS is where you specify the color, size, spacing, font and other visual aspects of the content that you create in your markup language document.

Usually, you see CSS used alongside HTML to describe the way a Web page looks and feels. You can have a Web page without CSS, but it would be very difficult to make it look the way you want with just HTML. This is why almost every Web page is a combination of HTML and CSS.

<p><b style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;"><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: 16pt; line-height: 22.8267px; font-family: inherit; vertical-align: baseline;">CSS</span></b><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 14pt; line-height: 19.9733px; font-family: inherit; vertical-align: baseline;">&nbsp;</span><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 12pt; line-height: 17.12px; font-family: inherit; vertical-align: baseline;">•</span><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 14pt; line-height: 19.9733px; font-family: inherit; vertical-align: baseline;">&nbsp;/</span><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 14pt; line-height: 19.9733px; font-family: inherit; vertical-align: baseline;"><span class="transcribed_word" style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;">si-ɛs-ɛs</span>/</span><span style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 12pt; line-height: 17.12px; font-family: inherit; vertical-align: baseline;">&nbsp;•&nbsp;</span><i style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;">noun&nbsp;</i></p>

<p class="MsoNormal" style="text-rendering: optimizeLegibility; margin-right: 0px; margin-left: 0.2in; padding: 0px; border: 0px; outline: 0px; font-variant-numeric: inherit; font-stretch: inherit; font-size: 16px; font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; vertical-align: baseline;">Stands&nbsp;for "<b style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;">C</b>ascading&nbsp;<b style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;">S</b>tyle&nbsp;<b style="text-rendering: optimizeLegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; vertical-align: baseline;">S</b>heets". A style sheet language for describing how to display an HTML document.</p>

#### An example

Let's take the (ridiculous) Michel Buffa home page again:

Notice the use of some HTML tags: h1, img, p, body etc.

Now, we can add some "CSS rules" to the HTML, and see that the appearance of the resulting HTML page rendering is rather different (click on the HMTL/CSS buttons to see alternatively the HTML or the CSS code, remember you can always make changes to the code: change the color in the CSS part, etc.): [Demo - CSS](src/01b-example05.html)

If you click on the CSS button on the top left of the previous codepen example, you see the CSS rules that have been applied to the HTML document. Let's look at the first one:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">h1 </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; color</span><span class="pun">:</span><span class="pln">red</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln">lightGreen</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; border</span><span class="pun">:</span><span class="lit">12px</span><span class="pln"> solid violet</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; padding</span><span class="pun">:</span><span class="pln"> </span><span class="lit">5px</span><span class="pun">; &nbsp;&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; border</span><span class="pun">-</span><span class="pln">radius</span><span class="pun">:</span><span class="pln"> </span><span class="lit">15px</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; text</span><span class="pun">-</span><span class="pln">align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br/>

This rule turns all the `h1s` in the document into red text, centered horizontally, on a light green background, with a violet border of 12 pixels (a solid border, not a dashed one), and this border has rounded corners made of arcs of a circle whose radius is 15 pixels.

The part before the opening brace (_line 1_) is the "CSS selector", it indicates the elements that have their properties changed according to what is inside the braces.

The part inside the braces is a set of properties and values that are useful for setting the look and feel of the selected elements.

Line 2 for example, says that all `h1s` is colored in `red`.


#### CSS rules are applied in sequence

After the previous rule is applied, then the second rule is taken into account, then the next, etc. In this way, you can see that all `h2s` is in brown (second rule).

The third rule uses what is called "a multiple selector":

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">p</span><span class="pun">,</span><span class="pln"> h1</span><span class="pun">,</span><span class="pln"> h2 </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;font</span><span class="pun">-</span><span class="pln">family</span><span class="pun">:</span><span class="pln"> cursive </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br/>

This one says that all `p`, `h1` and `h2` uses a cursive font character. The "," means "and also".

This is also how we indicate in the last rule that images and paragraphs should be moved to the right 50 pixels (property `margin-left: 50px`).

#### The id and class attributes

Basically, any given element on your Web page can be identified uniquely with an '`id`' attribute, or grouped with a class of other elements by setting the '`class`' attribute.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;p</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"paragraph-1"</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"regular-paragraphs"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Call me Ishmael . . .</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/p&gt;</span></li>
</ol></div><br/>

The paragraph above has a unique identifier: the id attribute whose value is "paragraph-1" and is part of a class of "regular-paragraphs". The letters inside the quotes have no meaning to the computer, they just need to be consistent. They are actually strings. 

Again, the fact that the computer does not care what we put in those strings (except for some restrictions) means we can use them to convey meaning to a human developer. I could just as easily have said id='x' and class='y', but anyone looking at that would have no hint what the significance of x and y are. Best practice is to name these things to increase clarity, consistency and brevity.

Let's look at a modified version of Michel Buffa's home page example: [Demo - Modified](src/01b-example06.html)

The last two rules first target the element whose id is 'hobbyTitle', in our case it's the second h2 element:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;h2</span><span class="pln"> </span><span style="color: #ff0000;"><strong><span class="atn">id</span><span class="pun">=</span><span class="atv">"hobbyTitle"</span></strong></span><span class="tag">&gt;</span><span class="pln">My Hobbies</span><span class="tag">&lt;/h2&gt;</span></li>
</ol></div><br/>

And here is the CSS rule:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com"><strong>#hobbyTitle</strong> {</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; font</span><span class="pun">-</span><span class="pln">family</span><span class="pun">:</span><span class="pln"> </span><span class="str">'caveat'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; font</span><span class="pun">-</span><span class="pln">size</span><span class="pun">:</span><span class="lit">40px</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; text</span><span class="pun">-</span><span class="pln">shadow</span><span class="pun">:</span><span class="pln"> </span><span class="lit">4px</span><span class="pln"> </span><span class="lit">4px</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> rgba</span><span class="pun">(</span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br/>

_Line 1_ uses the "#" character in the selector, meaning that we're going to select an element by its `id` attribute. In this case, the selector equal to `#hobbyTitle`, selects the element that has an attribute `id="hobbyTitle"`.

In that case, we use a funny char font called 'caveat' we took from the Google font service (see [fonts.google.com](https://fonts.google.com/)), and in order to be able to use it in a font-family CSS property, we included its definition using a `<link>` tag in the HTML part of the document:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;head&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;title&gt;</span><span class="pln">Your first HTML page</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp;</span>&lt;meta charset="utf-8"/&gt;</li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; <strong>&lt;link</strong></span><strong><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://fonts.googleapis.com/css?family=Caveat"</span><span class="pln"> </span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; rel</span><span class="pun">=</span><span class="atv">"stylesheet"</span><span class="tag">&gt;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
</ol></div><br/>

The last rule targets all elements that have an attribute `class="funny"`. Notice they can be different elements, we can have a p and an h3 element that have the `class="funny"` attribute:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pun">.</span><span class="pln">funny </span></strong><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; color</span><span class="pun">:</span><span class="pln">purple</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; font</span><span class="pun">-</span><span class="pln">family</span><span class="pun">:</span><span class="pln"> </span><span class="str">'caveat'</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; font</span><span class="pun">-</span><span class="pln">size</span><span class="pun">:</span><span class="lit">40px</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br/>

This rule changes the color, font family and size of two out of three paragraphs in the HTML element:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">p </span><span class="kwd">class</span><span class="pun">=</span><span class="str">"funny"</span><span class="pun">&gt;</span><span class="pln">I also play electric guitar </span><span class="kwd">and</span><span class="pln"> love coding </span><span class="typ">WebAudio</span><span class="pln"> applications</span><span class="pun">...&lt;/</span><span class="pln">p</span><span class="pun">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">&lt;</span><span class="pln">p </span><span class="kwd">class</span><span class="pun">=</span><span class="str">"funny"</span><span class="pun">&gt;</span><span class="typ">Music</span><span class="pun">,</span><span class="pln"> </span><span class="typ">Movies</span><span class="pun">,</span><span class="pln"> </span><span class="typ">Video</span><span class="pln"> </span><span class="typ">Games</span><span class="pun">,</span><span class="pln"> </span><span class="typ">Traveling</span><span class="pun">,</span><span class="pln"> </span><span class="typ">Family</span><span class="pun">,</span><span class="pln"> etc</span><span class="pun">.&lt;/</span><span class="pln">p</span><span class="pun">&gt;</span></li>
</ol></div><br/>

There are many, many, many different CSS properties in existence, and many different ways to select elements. We recommend that you follow the W3Cx [CSS Basics](https://www.edx.org/course/css-basics) and [HTML5&CSS Fundamentals](https://www.edx.org/course/html5-and-css-fundamentals) courses to learn more about CSS and about HTML5 basics.

#### Where can we put the CSS rules: in the HTML file? in another file? 

You can do both! 

You can embed the CSS rules between a `<style>...</style>` tag, located inside the `<head>...</head>` of the HTML documents, like in this example: [Demo - Inline Style](src/01b-example07.html)

This is OK if you do not have too many CSS rules. In general it's better to put the CSS rules in one or more separate .css files, like this (open [this example in Plunker](https://plnkr.co/edit/vedmaDmnfiJzoiLPrInG?p=preview))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y3k2wqtk')"
    src    ="https://tinyurl.com/y3f5ayyy"
    alt    ="Snapshot of a code editor showing a separate css file"
    title  ="Snapshot of a code editor showing a separate css file"
  />
</figure>

Note that when you use an online IDE, you usually type/paste the CSS rules in a "CSS tab" in the online editor, and it hides all the "plumbing" for you (except the more complete ones such as Plunker or AWS Cloud9 that enable you to manage files in the cloud).

#### Live coding video: mixing HTML and CSS

<a href="https://edx-video.net/W3CJSIXX2016-V000400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/yy27g4dp)

#### Notes for 1.2.2 CSS is for style

+ Cascade Style Sheet (CSS)
  + a style sheet language used to describe the way an HTML or XML document shown
  + able to specify the color, sizee, spacing, font and other visual aspect of the content
  + used along side HTML to desceibe the way a Web page looks and feels
  + w/o CSS: difficult to make document looks the way intended
  + almost every Web page combining HTML and CSS
  + example:

    ```css
    h1 {
      color:red;
      background-color:lightGreen;
      border:12px solid violet;
      padding: 5px;   
      border-radius: 15px;
      text-align: center;
    }
    ```

    + CSS selector
      + the part before the opening brace
      + indicating the elements w/ properties changed inside the brace
      + example: `h1`
    + property:
      + the part inside brace
      + used for setting the look and feel of the selected elements
      + a set of properties and values

+ CSS rules
  + rules applied in sequences
  + multiple selector
    + example

      ```css
      p, h1, h2 {
        font-family: cursive
      }
      ```

    + all `p`, `h1`, & `h2` using cursive font
    + ',' means "and also"

+ `id` and `class` attributes
  + `id` attribute: identifying any element in Web page uniquely
  + `class` attribute: grouping any elements w/ a class of other elements
  + example: `<p id="paragraph-1" class="regular-paragraphs">`
    + unique identifier w/ `id="paragraph-1"`
    + part of class `regular-paragraphs`
  + text within the quotes
    + w/o meaning to the computer
    + used to convey the meaning to a human developer
    + best pratice: named to increase clarity, consistency, and brevity
  + example: `<h2 id="hobbyTitle">My Hobbies</h2>`

    ```css
    #hobbyTitle {
      font-family: 'caveat';
      font-size:40px;
      text-shadow: 4px 4px 2px rgba(150, 150, 150, 1);
    }
    ```

  + `#` in selector: to select an element by its `id` attribute
  + `<link>` tag in HTML `<head>` element
    + including other CSS properties from remote/local CSS style sheet file
    + example: `<link href="https://fonts.googleapis.com/css?family=Caveat" rel="stylesheet">`





#### Knowledge check 1.2.3

<pre>.important {
  color:red;
}
</pre>

  In CSS, when we use a selector like .important, it means that:

  a. `.important` is not correct, there is no such selector in CSS<br/>
  b. We are going to select all HTML elements that have a `class="important"` attribute/value, and the CSS rule will be applied to all these elements<br/>
  c. We are going to select a single HTML element that has the `id="important"` attribute. Two HTML elements cannot have the same value for the `id` attribute (it must be unique and it acts as an identifier)

  Ans: <br/>
  Explanation: 






