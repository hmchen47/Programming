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




## Final exam (36-43)




## Final exam (44-52)



