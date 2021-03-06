# Week 1: HTML5 Basics


## 1.6 Exercises - Week 1


### 1.6.1 Intro exercises - Week 1

We hope that the first week of the course has been informative!  Now is your opportunity to show that you have learned the material by completing some exercises.

Please try to complete the following 34 assessments in a timely manner.

As stated in the grading policy page, they count towards 15% of your final grade.



### 1.6.2 Greater simplicity (1-2)

1. Towards more simplicity

  HTML5 has a relaxed syntax compared to previous versions. One of these statements is incorrect - which one?

  a. `<link rel='stylesheet' href=style.css>`<br/>
  b. `<textarea rows=20 cols="80">Hello...</textarea>`<br/>
  c. `<img src=myImage.jpg width=200 height=400>`<br/>
  d. `<img src=Michel Buffa.jpg ></img>`<br/>
  e. `<link rel=stylesheet href=style.css>`<br/>

  Ans: d <br/>
  Exmplanation: HTML5 quotes are optional if an attribute value does not contain any spaces. All answers are correct except answer 4, as Michel Buffa contains a space, so in that case the correct value should have been "Michel Buffa.jpg" or 'Michel Buffa.jpg'


2. Doctype definition

  With HTML5, please select how to declare the DOCTYPE of an element:

  a. You need to declare `<!DOCTYPE html>` in order to have a valid document<br/>
  b. No need to declare any DOCTYPE, the document will be valid anyway<br/>
  c. All HTML4.01 and XHTML DOCTYPE definitions can be used<br/>
  
  Ans: a <br/>
  Explanation: There is only one simplified way to declare the DOCTYPE. The DOCTYPE must be declared in order to have a valid document.


### 1.6.3 Sectioning elements (3-12)

3. Sectioning elements part 1

  Which of these elements is a sectioning element? (2 correct answers)

  a. p<br/>
  b. article<br/>
  c. br<br/>
  d. h1<br/>
  e. section<br/>

  Ans: be<br/>
  Explanation: Only `<section>` and `<article>` are sectioning elements.


4. Sectioning elements part 2

  Which of these elements are sectioning elements: (2 correct answers)

  a. aside<br/>
  b. div<br/>
  c. nav<br/>
  d. span<br/>
  e. h2<br/>

  Ans: ac<br/>
  Explanation: Only `<aside>` and `<nav>` are sectioning elements.


5. Sectioning root element

  The `<body>` element is called a "sectioning root". Best practice is to systematically add a heading in the body (a `<h1>`..`<h2>`)

  Ans: True<br/>
  Explanation: The `<body>` element is indeed a "sectioning root". Adding a heading in the body will make the document more accessible to people using screen readers.


6. Section in article?

  The blog example used several `<article>` elements in a `<section>`, could we have done the reverse: used sections in articles? (True/False)

  Ans: True<br/>
  Explanation: Indeed, a section may be cut into articles, and a long article may in turn be cut into sections.


7. To div or not to div...

  The `<div>` element has been removed from the HTML5 specification, as it has now been replaced by the new sectioning elements `<article>`, `<section>`, etc. (True/False)

  Ans: False<br/>
  Explanation: No, `<div>` is still there and can be used when there is no clear need to use a sectioning element. For example, to put part of the document into a container just to make styling its content easier.


8. Default content?

  All HTML content that is not inside one of the new elements presented in the course: header, footer, section, article, nav, aside, figure, figcaption, time, main, is considered implicitly as the "default content"? (True/False)

  Ans: True<br/>
  Explanation: The W3C HTML5 group decided that anything not embedded in one of the sectioning elements is "<span style="color: cyan;">default content</span>".


9. The `<main>` element

  Is it recommended to use `<main>` if you use other sectioning elements such as `<article>`, `<section>`, etc.? (False/True)

  Ans: True<br/>
  Explanation: If you use other sectioning elements, it is recommened to also add a `<main>` to your document. However, this element should only be used subject to the following constraints:
    + a) There must not be more than one `<main>` element in a document,
    + b) it must not be a descendant of an `<article>`, `<aside>`, `<footer>`, `<header>`, or `<nav>` element.


10. The `<nav>` element

  Should the `<nav>` element be used for major navigation blocks? (Yes/No)

  Ans: Yes<br/>
  Explanation: Yes, `<nav>` is designed to be used in all navigation blocks.


11. `<nav>` in `<article>`?

  Is `<nav>` allowed inside an `<article>` or in a `<section>`? (Yes/No)

  Ans: Yes<br/>
  Explanation: `<nav>` can be used at <u>any location</u> that requires a navigation block. An article may have an internal navigation menu (next blog post/previous blog post, for example...).


12. Aside....

  Should `<aside>` elements be used for _important explanations for the understanding of the main document_? (Yes/No)

  Ans: <span style="color: cyan;">No</span>, xYes<br/>
  Explanation: No, the `<aside>` element is used to display content not necessary for understanding the main content. It is often used for adverts, tags, recommended navigation, etc.
  

### 1.6.4 Headers and footers (13-14)

13. Headers and footers

  We can have `<header>...</header>` and `<footer>...</footer>` ONLY at the beginning of the document, not in other sectioning elements like `</article>` or `</section>` (True/False)

  Ans: False<br/>
  Explanation: Headers and footers can be added in any sectioning element.


14. Header and headings

  What are the correct following statements about `<header>` and headings? (3 correct answers)

  a. We call "headings" the `<h1>`...`<h6>` elements.<br/>
  b. The `<header>` element is just a container that is useful to regroup one or more headings with other HTML content.<br/>
  c. `<header>` `<h1>` This HTML5 course is great!`</h1>` `</header>` will be rendered the same as `<h1>`This HTML5 course is great!`</h1>`<br/>
  d. `<header>`This HTML5 course is great!`</header>` will be rendered the same as `<h1>`This HTML5 course is great!`</h1>`<br/>
  
  Ans: abc<br/>
  Explanation: The `<header>` is just a container. Use it when you have more than just a simple heading.


### 1.6.5 Headings (15-18)

15. Headings and sectioning content

  What best practices have been presented in the course? (2 correct answers)

  a. Whenever possible, try not to use `<article>` or `<section>`. Instead, use a heading (`<h1>`...`<h6>`) to define an implicit "section of a document".<br/>
  b. `<h1>`...`<h6>` define a hierarchy that can be used to generate a table of contents.<br/>
  c. You should use at least one heading after each sectioning content or after the `<body>` of the document.<br/>
  d. It is necessary to use `<h1>` immediately after each sectioning content, as we did in the first version of the blog example presented in the course.<br/>

  Ans: bc<br/>
  Explanation: 
    + a) The first answer is false: it is good practice to explicitly define sections instead of relying on the fact that H1...H6 implicitly define a section in the document. 
    + b) The second answer is true: H1...H6 indeed define a hierarchy. 
    + c) The third answer is true: screen readers will read the headings aloud, making the document accessible to people with vision impairments. 
    + d) The fourth answer is false: having an H1 after each sectioning element is practical but not mandatory. It's not even recommended today since most screen readers/browsers do not yet implement the renumbering of the hierarchy levels when H1s are inside sections.


16. Displaying a table of contents

  Displaying the table of contents helps understanding the global structure of the document? (True/False)

  Ans: True<br/>
  Explanation: Looking at the table of contents helps to locate errors in the structure.



17. Tools for displaying the table of contents

  To see the table of contents of an HTML5 document: (3 correct answers)

  a. I can use a browser extension.<br/>
  b. I have to write some JavaScript code myself, and look at the Document Object Model structure of the document.<br/>
  c. I can use a piece of JavaScript code that implements the outline algorithm that computes the different hierarchy levels.<br/>
  d. There are online Web sites where you can copy and paste HTML code or the URL of a document, and that will display the table of contents.<br/>
  e. Displaying the table of contents is a feature implemented by default in nearly all major modern Web browsers; no need to do anything but to select this feature in one menu of the browser.<br/>

  Ans: acd<br/>
  Explanation: You do not need to write any code yourself, tools exist both as browser extensions or ready-to-go JavaScript code you can embed, as shown in the course. There are also Web sites with useful tools that display the table of contents of HTML code that you paste or from a URL. No browser today implements the table of contents rendering natively. Correct answers are 1, 3 and 4.


18. Displaying table of contents for debugging

  Does the table of contents help debugging accessibility of my document?

  a. No<br/>
  b. It shows missing headings as "Untitled" entries<br/>
  c. The table of contents does not display invalid sections<br/>

  Ans: b<br/>
  Explanation: Indeed, untitled entries in the table of contents show the lack of a heading in this particular section of the document. And it is good practice to have at least a heading after each section.


### 1.6.6 Other elements and attributes (19-26)

19. Which element?

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick="window.open('https://tinyurl.com/y3yws87p')"
      src    ="https://tinyurl.com/y39xph3f"
      alt    ="example of summary details, the question asks which HTML element is used to display the short text that is displayed when summary/details is unfolded"
      title  ="example of summary details, the question asks which HTML element is used to display the short text that is displayed when summary/details is unfolded"
    />
  </figure>

  What element is used for the part with a green background? Just type the name of the element without "<" and ">" characters. For example type P, not `<P>` if the answer is the `<P>` element.

  Ans: summary or Summary or SUMMARY<br/>
  Explanation: The part at the top is the `<summary>`


20. CSS Styling?

  Can we easily style `<summary>` and `<details>`?

  a. Yes, CSS rules can be used like color, background-color etc, and some browsers propose non standard pseudo-classes for the icon, depending on the state of the summary element (folded / unfolded)<br/>
  b. Yes but we can only style them using proprietary browser-dependent pseudo classes<br/>
  c. No, there is no support for styling these elements<br/>

  Ans: a<br/>
  Explanation: The right answer is the last one: we can use regular CSS properties; some of them will work like color, margin, padding, etc, and browser-dependent pseudo classes can be used for customizing dedicated properties like the small icon.


21. Correct schema

  What is the correct schema from schema.org for describing a person's address?

  a. https://schema.org/LocalAddress<br/>
  b. https://schema.org/PostalAddress<br/>
  c. https://schema.org/SurfaceAddress<br/>
  d. https://schema.org/Address<br/>

  Ans: b<br/>
  Explanation: The right schema is https://schema.org/PostalAddress.


22. Duration value?

  <pre>&lt;h2&gt;Recipe:&lt;/h2&gt;
  &lt;ul&gt;
    &lt;li&gt; Preparation time: &lt;time datetime="<b>AAAA</b>"&gt;30 minutes&lt;/time&gt; &lt;/li&gt;
  &lt;/ul&gt;
  </pre>

  What textual value should be entered in place of the AAAA string in the above example?

  Ans: PT30M or PT30m or 30M or 30m<br/>
  Explanation: A duration value in minutes is of the form PT30M where "P" means "Period", "T" means "Time" and "M" means Minutes


23. Date?

  `Michel was born <time datetime="?">April 16, 1965</time>.`

  What value should you put instead of the ? string (answer is 10 characters)?

  Ans: 1965-04-16<br/>
  Explanation: The right syntax is YEAR-MONTH-DAY, so the right answer is 1965-04-16.


24. Highlighting text?

  Which HTML5 element has been designed to highlight text?

  a. `<ht>`<br/>
  b. No element is particularly dedicated, I can use use CSS to change the background of a part of text, for example by surrounding it with `<span style="background-color:yellow">`...`<span>`<br/>
  c. `<mark>`<br/>
  d. `<bold>`<br/>
  e. `<highlight>`<br/>

  Ans: c<br/>
  Explanation: The `<mark>` element has been designed to highlight text. By default is makes the text background yellow, but as it affects also the DOM it adds also semantics to the document (and can be searched from the JavaScript DOM API).


25. Missing attribute...

  <pre>&lt;a href="http://users.polytech.unice.fr/~buffa/normal.gif"
    <b>AAA</b>="MichelBuffa.jpg"&gt;
      download a picture of Michel Buffa as a file named MichelBuffa.jpg
  &lt;/a&gt;
  </pre>

  What would you put instead of AAA in the above code?

  Ans: download or Download or DOWNLOAD<br/>
  Explanation: The `download` attribute of the A element has been designed to download a linked file with another name than its remote filename.


26. Michel Ham or Michel Jambon?

  Which attribute and value pair can be used to avoid translating parts of text when used with translation services such as Google or Microsoft translate?

  a. translate=no<br/>
  b. Only service dependent attributes can be used. You have to read the documentation of translate.google.com and microsofttranslator.com services.<br/>
  c. translate=yes<br/>
  d. ignoretranslation=true<br/>
  e. notranslate=true<br/>

  Ans: a<br/>
  Explanation: The right answer is the second one, example `<span translate="no" class="author">Michel Ham</span>`.


#### Microdata (27-34)

27. Microdata

  Which of the following statements are true for microdata? (3 correct answers)

  a. They are mandatory in order to be indexed by search engines.<br/>
  b. They are meant to be processed by machines, not read by humans.<br/>
  c. A page with proper microdata will be better indexed and may appear in search results with an enhanced presentation.<br/>
  d. They have been created by Google and Microsoft.<br/>
  e. There are many vocabularies (schemas) of microdata for describing Persons, Movies, Organizations, etc.<br/>

  Ans: bce<br>
  Explanation: Microdata are meant to be processed by machines, in particular by search engines and Web crawlers. Web sites with good microdata will be better indexed and have a higher rank. Some microdata values will appear in search results too, with an enhanced presentation (this depends on the search engine, you need to read their documentation related to SEO - Search Engine Optimization). And there are many vocabularies available, new ones being published every month. You can even define your own vocabulary.


28. Find the site!
  
  What is the name of the Web site that describes a lot of microdata schemas, and has been created at the initiative of Google, Microsoft, Yahoo and Yandex?

  a. schema.org<br/>
  b. schemas.org<br/>
  c. schemas.com<br/>
  d. microdata.org<br/>
  e. search.org<br/>

  Ans: a


29. Find the attribute part 1

  `<section ... AAA ...>`

  What is the attribute name to specify that the section above is a container for microdata; what would you use instead of AAA?

  Ans: itemscope or itemScope or ItemScope<br>
  Explanation: The correct answer is `itemscope` like in `<section itemscope ... >`


30. Find the attribute part 2

  `<section ... AAA="http://schema.org/Person">`

  What is the attribute name to specify a microdata schema, that replaces AAA in the example above?

  Ans: itemtype or itemType or ItemType<br>
  Explanation: The correct answer is `itemtype` like in `<section ... itemtype="http://schema.org/Person">`


31. What is my job?

  <pre>&lt;div itemscope itemtype="http://schema.org/Person"&gt;
      My name is &lt;span itemprop="name"&gt;Michel Buffa&lt;/span&gt;,
      And I'm a &lt;span itemprop="<b>AAA</b>"&gt;professor/researcher&lt;/span&gt;
      at the University of Nice, in France.
  &lt;/div&gt;
  </pre>

  What property name would you put instead of AAA?

  Ans: jobTitle or jobtitle or JobTitle<br>
  Explanation: The `jobTitle` property is the correct one for describing a person's job.

32. Nested microdata

  Is it possible to nest microdata items inside one another? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, you can for example nest the address of a person inside a container that describes this person.


33. Multiple properties with the same name

  Is it possible to have in a container that describes, for example, a person, several microdata properties that have the same name, but with different values? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, we can have multiple properties with the same name, for example, a person can have multiple urls for multiple home pages, that will be describe with the `url` property of the schema Person.


34. Harrison Ford produced Star Wars?

  <pre class="prettyprint  linenums:1">&lt;div itemtype="http://schema.org/Movie"&gt;

    Title: &lt;span itemprop="name"&gt;Star Wars&lt;/span&gt;
    Rating: &lt;span itemprop="contentRating"&gt;Select Rating&lt;/span&gt;
    Genre: &lt;span itemprop="genre"&gt;Space Opera&lt;/span&gt;
    Director:&lt;span itemprop="director"&gt;Georges Lucas&lt;/span&gt;
    &lt;div itemprop="actors" itemscope itemtype="https://schema.org/People"&gt;
      Actor: &lt;span itemprop="name"&gt;Mark Hamill&lt;/span&gt;
      Actor: &lt;span itemprop="name"&gt;Carrie Fisher&lt;/span&gt;
    &lt;/div&gt;
    Production Company:&lt;span itemprop="productionCompany"&gt;Harrison Ford&lt;/span&gt;

    &lt;/div&gt;</pre>

  Is the document above correct with respect to microdata? Check for the proper use of itemscope, itemtype and itemprop.

  a. No<br/>
  b. Yes, but Harrison Ford is not the guy who produced Star Wars!<br/>

  Ans: <span style="color: cyan;">No</span>, xYes<br>
  Explanation: The document is incorrect, an itemscope attribute is missing in the main `<div>` at the top of the hierarchy. We would need `<div itemscope itemtype="http://schema.org/Movie">`; and indeed Harrison Ford has never produced Star Wars!<br/>Also, we invented the http://schema.org/People vocabulary, and also invented the "actors" property. This does not make the document incorrect. You can create your own vocabularies and use them, same with properties. In terms of syntax, it's correct.
  



