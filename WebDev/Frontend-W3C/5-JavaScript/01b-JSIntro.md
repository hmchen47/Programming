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

For example, consider the following chunk of HTML code (note: you can edit the source code and see the resulting Web page updating in real time): [Local Example - tags](src/01b-example1.html)

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
+ You can modify the source code in the [Demo File](src/01b-example2.html), and see the results in real time.

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

Click the red circle next to HTML to unfold this HTML document structure (we can also say "see its DOM structure"): ([Demo File - DOM Structure](src/01b-example3.html))

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

[Local Demo Exxample - Image](src/01b-example4.html)


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


#### Knowledge check 1.2.1 

1. HTML tags and HTML elements the same thing. True or false?

  Ans: 

#### Knowledge check 1.2.2

1. The HTML structure of a document is a tree. (Correct/Incorrect)

  Ans: 


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





