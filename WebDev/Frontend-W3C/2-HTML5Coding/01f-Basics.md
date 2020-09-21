# Week 1: HTML5 Basics


## 1.6 Exercises - Week 1


### 1.6.1 Intro exercises - Week 1

We hope that the first week of the course has been informative!  Now is your opportunity to show that you have learned the material by completing some exercises.

Please try to complete the following 34 assessments in a timely manner.

As stated in the grading policy page, they count towards 15% of your final grade.


### 1.6.2 Quiz

#### Greater simplicity (1-2)

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


#### Sectioning elements (3-12)

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
  Explanation: If you use other sectioning elements, it is recommened to also add a<main> to your document. However, this element should only be used subject to the following constraints:
    + a) There must not be more than one `<main>` element in a document,
    + b) it must not be a descendant of an `<article>`, `<aside>`, `<footer>`, `<header>`, or `<nav>` element.


10. The `<nav>` element

  Should the `<nav>` element be used for major navigation blocks?

  Ans: True<br/>
  Explanation: Yes, `<nav>` is designed to be used in all navigation blocks.


11. `<nav>` in `<article>`?

  Is `<nav>` allowed inside an `<article>` or in a `<section>`? (Yes/No)

  Ans: True<br/>
  Explanation: `<nav>` can be used at any location that requires a navigation block. An article may have an internal navigation menu (next blog post/previous blog post, for example...).


12. Aside....

  Should `<aside>` elements be used for _important explanations for the understanding of the main document_? (Yes/No)

  Ans: <span style="color: cyan;">No</span>, xYes<br/>
  Explanation: No, the `<aside>` element is used to display content not necessary for understanding the main content. It is often used for adverts, tags, recommended navigation, etc.
  

#### Headers and footers (13-14)

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


#### Headings (15-18)

15. Headings and sectioning content

  What best practices have been presented in the course? (2 correct answers)

  a. Whenever possible, try not to use `<article>` or `<section>`. Instead, use a heading (`<h1>`...`<h6>`) to define an implicit "section of a document".
  b. `<h1>`...`<h6>` define a hierarchy that can be used to generate a table of contents.
  c. You should use at least one heading after each sectioning content or after the `<body>` of the document.
  d. It is necessary to use `<h1>` immediately after each sectioning content, as we did in the first version of the blog example presented in the course.

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
  a. I have to write some JavaScript code myself, and look at the Document Object Model structure of the document.<br/>
  a. I can use a piece of JavaScript code that implements the outline algorithm that computes the different hierarchy levels.<br/>
  a. There are online Web sites where you can copy and paste HTML code or the URL of a document, and that will display the table of contents.<br/>
  a. Displaying the table of contents is a feature implemented by default in nearly all major modern Web browsers; no need to do anything but to select this feature in one menu of the browser.<br/>

  Ans: acd<br/>
  Explanation: You do not need to write any code yourself, tools exist both as browser extensions or ready-to-go JavaScript code you can embed, as shown in the course. There are also Web sites with useful tools that display the table of contents of HTML code that you paste or from a URL. No browser today implements the table of contents rendering natively. Correct answers are 1, 3 and 4.


18. Displaying table of contents for debugging

  Does the table of contents help debugging accessibility of my document?

  a. No<br/>
  b. It shows missing headings as "Untitled" entries<br/>
  c. The table of contents does not display invalid sections<br/>

  Ans: c<br/>
  Explanation: Indeed, untitled entries in the table of contents show the lack of a heading in this particular section of the document. And it is good practice to have at least a heading after each section.


  



