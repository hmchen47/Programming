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
  







