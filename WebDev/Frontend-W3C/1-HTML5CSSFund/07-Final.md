# Module 7: Final exam

## Final exam (1-7)


1. HTML and CSS

  Which of the following are true of HTML and CSS? (select all that apply -- 3 correct answers!)

  1. HTML and CSS are separate languages
  2. CSS is a subset of HTML
  3. HTML is used to specify the content of a document while CSS handles its appearance
  4. It is possible to put CSS inside an HTML document

  Ans: 134<br/>
  Explanation: If CSS were a subset, it would be HTML5 with fewer features, rather it is a different language, with different syntax. CSS code can be included in an HTML file using the 'style' tag.


2. Identification

  Which of the following are correct well-formed snippets of HTML? (select all that apply -- 2 correct answers!)

  1. `<p>We stood, muted.</p>.`
  2. `<span>More light and light- more dark and dark our woes!</em>`
  3. -
    ```html
    <ol reversed>
      <li>day</li>
      <li>night</li>
    </ol>
    ```
  4. `<a href="#foot>*</a>`
  5. `<q>Good night, <b>good <i>night!</b> parting</i> is such sweet sorrow</q>`

  Ans: 13 <br/>
  Explanation: A close tag should match the last unmatched open tag preceding it. Quotation marks must also match, either single or double.


3. The `<ol>` tag

  Many tags are abbreviations. For example, in the tag `<p>`, the p stands for paragraph.

  `<ol>` stands for:
  
  Ans: ordered list or order list or orderlist or orderedlist<br/>
  Explanation: An 'ordered list' will number the elements of the list in order.


4. The `<ul>` tag

  `<ul>` stands for:
  
  Ans: unordered list or unorder list or unorderlist or unorderedlist <br/>
  Explanation: A list without any labeled order (e.g. bullets instead of numbers) is an 'Unordered List'.


5. The `<li>` tag

  `<li>` stands for:
  
  Ans: list item or listitem<br/>
  Explanation: A list is composed of various items, hence 'List Items'.



6. The `b` tag

  `<b>` stands for:
  
  Ans: bold<br/>
  Explanation: The 'b' comes from 'bold', which was it's original meaning. In HTML5, however, it is intended for 'a span of text to which attention is being drawn' for any number of reasons, not necessarily because it is important.


7. The `<q>` tag

  Many tags are abbreviations. For example, in the tag `<p>`, the p stands for paragraph.

  Please enter the full name for the tag.

  `<q>` stands for:
  
  Ans: quote or quotation<br/>
  Explanation: "Q is for 'quote' or 'quotation', an inline element for short quotes.



## Final exam (8-16)


8. Image

  The `<img>` element supports several attributes, but two of them are always required.

  Which two attributes are always required for an img element? (select all that apply -- 2 correct answers!)

  1. src
  2. title
  3. alt
  4. width
  5. height

  Ans: 13<br/>
  Explanation: Any image tag needs the image, indicated by the 'src' attribute, and alternate text for screen readers, defined by the 'alt' attribute.


9. Image size

  Imagine you have a PNG file that's 400 pixels wide and 300 pixels tall. We include it onto the Web page and attempt to resize it with the following:

  ```html
  <img src="image.png" alt="kitten!" width="200">
  ```

  How tall will the image be when it appears in the browser?

  1. 100 pixels
  2. 150 pixels (aspect ratio preserved)
  3. 200 pixels (same as the adjusted width)
  4. 300 pixels (the original height)

  Ans: 2<br/>
  Explanation: If only one dimension is set on an `<img>` then the browser will automatically adjust its other dimension such that the original aspect ratio is preserved and the image is not "warped".


10. Identification

  Which of the following demonstrate correct syntax for applying an attribute to a tag? (select all that apply -- 2 correct answers!)

  1. `<img src="flower.png" alt = lovely daffodils>`
  2. `<ol reversed>`
  3. `<p id="opening">`
  4. `</p id="opening">`
  5. `<a href="http://wikipedia.org>`

  Ans: 23<br/>
  Explanation: The 'alt' attribute takes a single string, but without quotes the space is seen as a separator. Also, Quotation marks must match, for ever open there is a close. Closing tags do not have attributes.
  

11. Attributes

  Can an attribute be applied multiple times to the same element?
  
  Ans: No <br/>
  Explication: Any given attribute may only be applied once to an element.


12. Attributes and classes

  Which of the following demonstrates the __correct__ way to apply multiple classes to a single element?

  1. No element can have multiple classes
  2. `<li class="bird flightless">penguin</li>`
  3. `<li class="bird" class="flightless">penguin</li>`

  Ans: 2<br/>
  Explication: A 'class' attribute can take multiple classes as a string of space separated classnames, but it can only be specified once in the tag.


13. Attributes and identifiers

  Which of the following demonstrates the __correct__ way to apply multiple identifiers to a single element?

  1. No element can have multiple ids
  2. `<p id="first-paragraph dorothea">Ms. Brooke</p>`
  3. `<p id="first-paragraph" id="dorothea">Ms. Brooke</p>`

  Ans: 1<br/>
  Explication: Because identifiers are unique ways of referencing an element, the id can only be used once and each element can have only one id.


14. Hyperlinks

  Examine this snippet of HTML:

  `<a href="#footnote">Footnote</a>`
  
  Which of the following statements are true about the snippet above?

  1. The hyperlink will open a new window
  2. The hyperlink will take the user to another page, footnote.html
  3. The hyperlink will take the user to some other element on the page that has id="footnote"
  4. It is not a valid hyperlink

  Ans: 3<br/>
  Explanation: '#idName' is the format for referring to an id, both in this case and in CSS. This allows linking to a particular point in a page, not just the top.


15. The `<details>` tag

  The `<details>` tag is used in conjunction with which other tag?

  1. `<mark>`
  2. `<information>`
  3. `<summary>`
  4. `<li>`

  Ans: 3<br/>
  Explanation: The `<details>` tag is used in conjunction with the `<summary>` tag.

  ```html
  <details>
    <summary>Mary Ann Evans greatest author ever</summary>
    <p>Middlemarch is the greatest book ever. Middlemarch was written by George Eliot. George Eliot
      was the pen name of Mary Ann Evans.  Ergo, Mary Ann Evans is the greatest author ever.</p>
  </details>
  ```


16. More details...

  What do the `<details>` tag and the answer to the previous question do when used together?

  1. They do nothing special
  2. Define a hyperlink that will jump between the two sections
  3. Show a disclosure triangle that can be "opened" to see the other contents of the `<details>`
  4. Display a caption that accompanies an image

  Ans: 3 <br/>
  Explanation: Normally a summary is shown unless details are requested, by clicking on the disclosure icon.



## Final exam (17-24)


17. Basic CSS properties - size

  What is the CSS property that adjusts the size of text?
  
  Ans: font-size<br/>
  Explanation: The font-size property will adjust the text size of an element.


18. Basic CSS properties - color

  What CSS property lets us change the text color?
  
  Ans: color<br/>
  Explication: The color property will change the text color of an element.


19. Basic CSS properties - space

  What CSS property puts spacing between elements?
  
  Ans: margin or margin-top or margin-bottom or margin-left or margin-right<br/>
  Explanation: The margin property is used to put space between elements.



20. CSS selectors - article

  `article { line-height: 16px; }`

  In the CSS above, the CSS selector used is an example of which type?

  1. pseudo selector
  2. class selector
  3. tag selector
  4. id selector
  
  Ans: 3<br/>
  Explanation: Tag selector meaning that the selector uses a tag.


21. CSS selectors - first paragraph

  `#first-paragraph { line-height: 16px; }`

  In the CSS above, the CSS selector used is an example of which type?

  1. pseudo selector
  2. id selector
  3. tag selector
  4. class selector

  Ans: 2<br/>
  Explanation #idName indicates an element with the id idName.


22. CSS selectors

  `.dorothea { line-height: 16px; }`

  In the CSS above, the CSS selector used is an example of which type?

  1. pseudo selector
  2. class selector
  3. tag selector
  4. id selector
  
  Ans: 2<br/>
  Explanation: .className indicates an element with the class className.


23. CSS comments

  Which of the following demonstrate correctly how to include a comment into CSS?

  1. `;; Put your CSS below`
  1. `/* Put your CSS below */`
  1. `// Put your CSS below`
  1. `<!-- Put your CSS below -->`

  Ans: 2<br/>
  Explication
  + CSS only supports one notation for comments, and that is the /* ... */ notation.
  + In HTML, comments are denoted with `<!-- ... -->`
  + And in Javascript, both /* ... */ and // .... can denote comments.


24. Inherit

  What does the `inherit` value mean?

  1. Override any other competing CSS rules and apply this value no matter what.
  2. The value of the CSS property in question being applied to this child element should be gotten from its parent element.
  3. For the property in question, use the same value as in the preceding CSS rule, ie from earlier in the CSS file.
  4. Just use the default value for the CSS property in question.

  Ans: 2 <br/>
  Explication: The inherit value means that the value for a given property should be inherited from the parent element.




## Final exam (25-35)


25. Invisible border

  True or False? An invisible border is the same as no border:
  
  Ans: False<br/>
  Explication; A transparent border would be invisible, but could still have width and thus affect the layout of the page.


26. Three blocks - negative margin

  The next 3 questions (26, 27 and 28) refer to this image:

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+2T2018/courseware/306cfa0313a449a29b2dbcb0b2afcb86/6be610c329d743c88824c48667c0d0ae/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B2T2018%2Btype%40vertical%2Bblock%40885d1392a8cb4d70a79fda91b960a2f4">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/2c88627f0e19f0341e97ccb8775e40c1/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/quiz-2.png" style="margin: 0.1em;" alt="The image is composed of 3 boxes horizontally disposed. The first box is light green with a blue border and is identified by the words 'Block 1'. On its right, there are 2 other boxes. First, 'Block 2' is light-blue with a red border and, second, 'Block 3' is light-pink with a thick green border. 'Block3' is overlapping 'Block 2' on the left." title="Diagram for Q26~28" width="250">
    </a></div>
  </div>

  Which of the boxes above has a negative margin-left?

  1. None - negative margins aren't allowed
  2. Block 2
  3. Block 3
  4. Block 1

  Ans: 2<br/>
  Explanation: Setting a negative margin-left will pull a box to the left. Since Block 3 is overlapping the box to the left, it must be Block 3.


27. Three blocks - negative padding

  Which of the boxes above has negative padding?

  1. None - negative padding isn't allowed
  2. Block 2
  3. Block 3
  4. Block 1
  
  Ans: 1 <br/>
  Explication: The smallest padding allowed is 0, which is no padding. It can't be negative.


28. Three blocks - border

  Which of the boxes has the smallest border?

  1. All the borders are the same width
  2. Block 1
  3. Block 3
  4. Block 2
  
  Ans: 2 <br/>
  Explication: Block 1, though larger than the other blocks, has the thinnest/smallest border.


29. Debugging the box model

  Use this image for the next 4 problems (29, 30, 31 and 32):

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+2T2018/courseware/306cfa0313a449a29b2dbcb0b2afcb86/6be610c329d743c88824c48667c0d0ae/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B2T2018%2Btype%40vertical%2Bblock%40885d1392a8cb4d70a79fda91b960a2f4">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6380d1a9d7502285764f236822d04974/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/quiz-3.png" style="margin: 0.1em;" alt="box model" title="Diagram for Q29~32" width="250">
    </a></div>
  </div>

  True or False? Padding, border and margin are all equal to each other
  
  Ans: False<br/>
  Explanation: According to the box diagram above, all three have different values.


30. Debugging the box model - padding

  True or False? Padding on all 4 sides is equal.
  
  Ans: True<br/>
  Explication: According to the box diagram, padding is 32 pixels on all four sides.


31. Debugging the box model - margin

  True or False? There are no negative margins

  Ans: True<br/>



32. Debugging the box model - height

  Assuming the border and background are visible, what is the height of the visible part of this element on the screen?

  1. 126.219px
  2. 89.219px
  3. 94px
  4. 57px
  
  Ans: 3


33. Inspector

  Use this image for the 3 following questions (33, 34 and 35):

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+2T2018/courseware/306cfa0313a449a29b2dbcb0b2afcb86/6be610c329d743c88824c48667c0d0ae/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B2T2018%2Btype%40vertical%2Bblock%40885d1392a8cb4d70a79fda91b960a2f4">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ae95260728fe37cc40491e2da960fcd3/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/quiz-4.png" style="margin: 0.1em;" alt="This image shows the style debugger tool with the following parameters: element.style has a 30px padding-right. The li element has a display attribute equals to list-item.There are 2 style attributes that are inherited from the ul element: list-style-type equals to none and font-size equals to 16px. The list-style-type of the ul element of the user agent stylesheet is striked out. The font-size attribute inherited from the body element is striked out." title="Diagram for Q33~35" width="250">
    </a></div>
  </div>

  Name one property that has been overridden by a more specific rule
  
  Ans: font-size or list-style-type or padding-right


34. Inspector - best practice

  Does this code use the best practice of putting CSS Style rules into a separate .css file?
  
  Ans: No


35. Inspector - numbering

  Assuming the element is part of a list, are the list items automatically numbered?

  Ans: No (xYes)<br/>
  Explanation: First, it's an unordered list, second the list-style-type is "none", so there are no bullets or numbers on.




## Final exam (36-43)


36. HTML entities

  The HTML entity `&lt;` will result in which character appearing on the page?

  1. `#`
  2. `<`
  3. `&`
  4. `>`
  
  Ans: 2<br/>
  Explanation: lt, as in the mathematical symbol 'Less Than'


37. HTML entities - &

  What HTML entity will result in an ampersand (&) ?
  
  Ans: `&amp;`<br/>
  Explanation: `&amp;` results in an ampersand being displayed.


38. Table identification - green border

  The next 3 questions (38, 39 and 40) refer to this image:

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+2T2018/courseware/306cfa0313a449a29b2dbcb0b2afcb86/6be610c329d743c88824c48667c0d0ae/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B2T2018%2Btype%40vertical%2Bblock%40885d1392a8cb4d70a79fda91b960a2f4">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/946a724ff9ef1473ae29609b28b38f91/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/table_identification.png" style="margin: 0.1em;" alt="The image shows a table composed of 2 columns and 6 rows. The header of the 1st column has a green border. The 4th row has a red border and the last cell -- 2nd column and 6th row -- has a blue border" title="Diagram for Q38~40" width="250">
    </a></div>
  </div>

  Which tag was used to define the area with the green border?

  1. `<td>`
  2. `<tr>`
  3. `<th>`
  4. `<table>`
  
  Ans: 3 <br/>
  Explanation: 'th' as in 'Table Heading'


39. Table identification - red border

  Which tag was used to define the area with the red border?

  1. `<td>`
  2. `<tr>`
  3. `<th>`
  4. `<table>`
  
  Ans: 2<br/>
  Explication: 'tr' as in 'Table Row'


40. Table identification - blue border

  Which tag was used to define the area with the blue border?

  1. `<td>`
  2. `<tr>`
  3. `<th>`
  4. `<table>`
  
  Ans: 1<br/>
  Explication: 'td' as in 'Table Data'


41. Inline element position

  Which of the following CSS properties could affect the position of an inline element?

  1. Neither margin-top nor padding-top nor border-top
  2. padding-top
  3. border-top
  4. margin-top
  
  Ans: 1<br/>
  Explication: For an inline element, margin, padding and border can affect the width of space taken up by the element. Height is not affected, e.g. margin-right and margin-left affect the width, but margin-top and margin-bottom are ignored.


42. Borders and decorations

  Which CSS property will let you put a border around an element?
  
  Ans: border<br/>
  Explication: The border property will apply a border to an element. The more specific variants are border-style border-width and border-color. Additionally, the border-radius property can be used for rounded corners.


43. Decorative images

  Which CSS property will let you apply an image into the background of an element?

  Ans: background-image<br/>
  Explanation: Unsurprisingly, an image in the background is specified by 'background-image'.




## Final exam (44-52)


Source code for the following question (44):

```html
<!DOCTYPE html>
<html>
<head>
  <title>Confessions</title>
  <style>
    q {
      margin-top: 20px;
      margin-left: 20px;
    }
    .stammer {
      left: 50px;
      top: 50px;
    }
  </style>
</head>
<body>
  <p>I stared into the fridge disbelieving my eyes.
    <q>I ate the last piece of cake,</q> she said, her head poking around the door.
  </p>
  <p class="stammer"><q>But whose head is this?</q> I stammered.</p>
  <p><q>Oh that? - I think it belongs to my ex.</q> she stepped from behind the door, a knife in her hand.
  <q> Sorry about the cake. You aren't mad, are you?</q> her lashes raised up and I fell into her sumptuous 
  eyes, for not the first time. Those eyes!</p>
</body>
</html>
```

44. Error identification

  Examine the CSS and HTML above.

  The CSS above is not working as intended. Identify all the problems: (select all that apply -- 2 correct answers!)

  1. `<q>` is an inline element. As such, the margin-left will have no effect upon it.
  2. `<q>` is an inline element. As such, the margin-top will have no effect upon it.
  3. `<p>` is an inline element. As such, the left and top properties will have no effect upon it.
  4. `<p>` is position:static by default. As such, it is not a positioned element and the left and top properties will have no effect upon it.
  
  Ans: 24 <br/>
  Explanation
  + 'q' is an inline element and thus top-margin and bottom-margin have no effect.
  + 'Static position' elements are not affected by top or left (or bottom or right) settings.


45. Positioned element

  What does it mean to be a positioned element?

  1. Positioned elements are "smart" elements and fix all problems
  2. Unlike non-positioned elements, a positioned element can have its position adjusted/set by the positioning properties (top, left, bottom, right, and z-index )
  3. Positioned elements ignore font- and text- properties
  4. Unlike non-positioned elements, a positioned element can have its position adjusted by the margin property (and margin-top, margin-left, margin-bottom, and margin-right )
  
  Ans: 2 <br/>
  Explanation: Positioned elements, where position value is either absolute, fixed, or relative, can be "positioned" with attributes like 'top' and 'left'.


46. Sizing - block width

  Which describes the default width of a block level element?

  1. Sized to width of parent
  2. Sized to width of content, plus padding
  
  Ans: 1 (x2) <br/>
  Explanation: Block level elements normally appear on their own line (horizontal space) within the parent, e.g. a paragraph that is the direct child of the body would take up the entire width of the body.


47. Sizing - inline width

  Which describes the default width of an inline element?

  1. Sized to width of content, plus padding
  2. Sized to width of parent
  
  Ans: 1<br/>
  Explanation: Because inline elements typically occur on the same line with other elements, their width is determined by the contents plus any horizontal (left or right) padding.


48. Sizing - block height

  Which describes the default height of a block level element?

  1. Sized to height of content
  2. Sized to height of parent
  
  Ans: 1 (x2) <br/>
  Explanation: Height includes the height of the content plus the top and bottom padding.


49. Sizing - inline height

  Which describes the height of an inline level element?

  1. Sized to height of content, plus padding
  2. Sized to height of parent
  
  Ans: 1 <br/>
  Explanation: While the padding top or bottom won't change the positioning of an element, it does affect the height, as can be seen by setting a background-color or border on the element.


50. Flexbox

  How cool is flexbox?

  1. Pretty Cool
  2. Cool
  3. Very Cool
  4. Awesome

  Ans: 1/2/3/4<br/>
  Explanation: It's really cool :-)


51. Flexbox container

  How do you designate an element as a flexbox container? (select all that apply - 2 correct answers!)

  1. `display:flex`
  2. `flex:1`
  3. `display:inline-flex`
  4. `display:block; flex:1`
  
  Ans: 13 <br/>
  Explanation: display: flex will make an element a 'flex container', influencing the layout of its child elements.


52. 'flex-basis'

  What does the flex-basis property do?
  
  1. tells the parent flexbox container the ideal starting size (main-axis size) for the flexbox item
  2. sets the maximum amount of space that can be given to or taken from the flexbox item
  3. sets the cross axis size for the flexbox item
  
  Ans: 1 <br/>
  Explanation: Starting with the basis, its size may flex in our out depending on layout considerations and other flex elements.






