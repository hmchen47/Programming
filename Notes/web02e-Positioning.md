# Positioning Content

Author: Shay Howe

[Origin](https://learn.shayhowe.com/html-css/positioning-content/)


## Positioning with Floats

+ the `float` property
  + take an element, remove it from the normal flow of a page, and position it to the left or right of its parent element
  + other elements on the page flowing around the floated element
  + e.g., `<img>` element floated to the side of a few paragraphs of text
  + used on multiple elements at the same time
    + provide the ability to create a layout by floating elements directly next to or opposite each other
    + seen in multiple-column layouts
  + most popular values: `left` and `right`

    ```css
    img {
      float: left;
    }
    ```

### Floats in Practice

+ Plain page w/ straight flow
  + a common page layout with a header at the top, two columns in the center, and a footer at the bottom
  + page marked up using the `<header>`, `<section>`, `<aside>`, and `<footer>` elements
  
    ```html
    <header>...</header>
    <section>...</section>
    <aside>...</aside>
    <footer>...</footer>
    ```
  
  + [Layout without Floats Demo1](src/web02e-floatDemo01.html)
  + the `<section>` and `<aside>` elements
    + block-level elements
    + stacked on top of one another by default
  + floating the `<section>` to the left and the `<aside>` to the right

    ```css
    section {
      float: left;
    }
    aside {
      float: right;
    }
    ```

  + an element floated: float all the way to the edge of its parent element
  + floated element w/o parent element: float all the way to the edge of the page
  + floating an element
    + taking it out of the normal flow of the HTML document
    + the width of the element to default to the width of the content within it $\to$ variable size
    + issue: columns for a reusable layout
    + solution: adding a fixed `width` property value to each column
    + issue: floated elements touching one another
    + solution: using the `margin` property to create space between elements

    ```css
    section {
      float: left;
      margin: 0 1.5%;
      width: 63%;
    }
    aside {
      float: right;
      margin: 0 1.5%;
      width: 30%;
    }
    ```

  + [Layout with Floats Demo 2](src/web02e-floatDemo02.html)


+ Possibly Changing display value
  + floated element removed from the normal flow of a page
  + possibly changing an element’s default display value
  + floated element relies on an element w `display: block;`
  + alter an element’s default display value if not `display: block;`
  + example
    + `<span>` element w/ `display: inline;` and ignore `width` and `height`
    + once floated, `width` and `height` accepted

+ Float more than 2 columns
  + example: 3 columns

    ```html
    <header>...</header>
    <section>...</section>
    <section>...</section>
    <section>...</section>
    <footer>...</footer>
    ```

  + float all three `<section>` elements to the left
  + adjust the width of the `<section>` elements to account for the additional columns and to get them to sit one next to the other

    ```css
    section {
      float: left;
      margin: 0 1.5%;
      width: 30%;
    }
    ```

  + [Three-column Layout with Floats Demo](src/web02e-floatDemo03.html)


### Clearing & Containing Floats

+ The `float` property
  + originally designed to allow content to wrap around images
  + never actually intended to be used for layout and positioning purposes
  + pitfalls
    + not render on an element that it is sitting next to or a parent element of a floated element
    + often margin and padding property values not interpreted correctly
    + sometimes unwanted content wrapping around a floated element
  + example: 2 columns
    + before set a width property value, the content within the `<footer>` element would have wrapped in between the two floated elements above it, filling in any available space
    + [Layout without Cleared or Contained Floats Demo](src/web02e-floatDemo04.html)
  + To prevent content from wrapping around floated elements
    + clear those floats and return the page to its normal flow
    + contain those floats and return the page to its normal flow

+ Clearing floats
  + accomplished using the `clear` property
  + values for `clear` property: `left`, `right`, and `both`
  + examples

    ```css
    div {
      clear: left;    /* left floats */
    }
    footer {
      clear: both;    /* clear all floats */
    }
    ```

  + [Layout with Cleared Floats Demo](src/web02e-floatDemo05.html)

+ Containing Floats
  + known as a "clearfix" or "cf" class in many websites
  + ensure that all of our styles rendered properly
  + reside within a parent element
  + parent element acting as a container, leaving the flow of the document completely normal outside of it
  + example:

    ```css
    .group:before,
    .group:after {
      content: "";
      display: table;
    }
    .group:after {
      clear: both;
    }
    .group {
      clear: both;
      *zoom: 1;
    }
    ```
  
  + CSS:
    + clearing any floated elements within the element with the class of group
    + returning the flow of the document back to normal
  + the `:before` and `:after` pseudo-elements
    + dynamically generated elements above and below the element with the class of group
    + displayed as table-level elements, much like block-level elements
    + The dynamically generated element after the element with the class of group is clearing the floats within the element with the class of group, much like the clear from before.
    + the element with the class of group itself also clears any floats that may appear above it, in case a left or right float may exist
  + example

    ```html
    <header>...</header>
    <div class="group">
      <section>...</section>
      <aside>...</aside>
    </div>
    <footer>...</footer>
    ```

    ```css
    .group:before,
    .group:after {
      content: "";
      display: table;
    }
    .group:after {
      clear: both;
    }
    .group {
      clear: both;
      *zoom: 1;
    }
    section {
      float: left;
      margin: 0 1.5%;
      width: 63%;
    }
    aside {
      float: right;
      margin: 0 1.5%;
      width: 30%;
    }
    ```
  
  + [Layout with Contained Floats Demo](src/web02e-floatDemo06.html)
  + the flow of a page is reset by either clearing or containing the floats as necessary


### In Practice - Example: Styles Conference Website - Layout

1. following previous Styles Conference Website

  + provide a way to contain those floats by adding the clearfix to our CSS
  + add the clearfix under the class name group

  ```css
  /*
    ========================================
    Clearfix
    ========================================
  */
  .group:before,
  .group:after {
    content: "";
    display: table;
  }
  .group:after {
    clear: both;
  }
  .group {
    clear: both;
    *zoom: 1;
  }
  ```

2. contain floats

  + float the primary `<h1>` within the `<header>` element to the left
  + allow all of the other content in the header to wrap to the right of it
  + add a class of logo to the `<h1>` element
  + add a new section of styles for the primary header

  ```html
  <h1 class="logo">
    <a href="index.html">Styles Conference</a>
  </h1>
  ```

  ```css
  /*
    ========================================
    Primary header
    ========================================
  */

  .logo {
    float: left;
  }
  ```

3. add a little more detail to logo

  + placing a `<br>` element, or line break, between the word “Styles” and the word “Conference” to force the text of our logo to sit on two lines
  + add a border to the top of our logo and some vertical `padding` to give the logo breathing room

  ```html
  <h1 class="logo">
    <a href="index.html">Styles <br> Conference</a>
  </h1>
  ```

  ```css
  .logo {
    border-top: 4px solid #648880;
    padding: 40px 0 22px 0;
    float: left;
  }
  ```

4. contain the floated `<h1>` element

  ```html
  <header class="container group">
    ...
  </header>
  ```

5. processing `<footer>` element

  + float copyright to the left within the `<small>` element
  + other elements wrap around it to the right
  + apply a class to the parent of the floated element and use a unique CSS selector to select the element and then float it
  + adding the class of `primary-footer` to the `<footer>` element

  ```html
  <footer class="primary-footer container group">
    ...
  </footer>
  ```

6. `primary-footer` class

  + use that class to prequalify the `<small>` element with CSS
  + select and `float` the `<small>` element to the `left`
  + create a new section within our `main.css` file for these primary footer styles

  ```css
  /*
    ========================================
    Primary footer
    ========================================
  */

  .primary-footer small {
    float: left;
  }
  ```

7. put some padding on the top and bottom of the <footer> element

  ```css
    .primary-footer {
    padding-bottom: 44px;
    padding-top: 44px;
  }
  ```

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y6396y5a')"
    src    ="https://tinyurl.com/y6396y5a"
    alt    ="Styles Conference website"
  />
  <figcaption> With a few floats, the &lt;header&gt; and &lt;footer&gt; elements <br/>on our Styles Conference home page are coming together </figcaption>
</figure>



## Positioning with Inline-Block

+ the `display` property
  + position content in conjunction with the `inline-block` value
  + `inline-block` method
    + primarily helpful for laying out pages or for placing elements next to one another within a line
    + displaying elements within a line while allowing them to accept all box model properties
    + including `height`, `width`, `padding`, `border`, and `margin`
  

### Inline-Block in Practice

+ Example: 3 columns

    ```html
    <header>...</header>
    <section>...</section>
    <section>...</section>
    <section>...</section>
    <footer>...</footer>
    ```

  + change `<section>` display values to `inline-block`, leaving the `margin` and `width` properties from before alone

  ```css
  section {
    display: inline-block;
    margin: 0 1.5%;
    width: 30%;
  }
  ```

  + the last `<section>` element pushed to a new row
    + `inline-block` elements displayed on the same line as one another
    + including a single space between them
    + the size of each single space added to the `width` and horizontal `margin` values of all the elements in the row
    + total width becomes too great, pushing the last `<section>` element to a new row
  + [Inline-Block Elements with White Space Demo](src/web02e-floatDemo07.html)
  + solution: displaying all of the `<section>` elements on the same row, the white space between each `<section>` element must be removed


### Removing Spaces Between Inline-Block Elements

+ ways to eliminate the space
  + no space btw two sections
    + put each new `<section>` element’s opening tag on the same line as the previous `<section>` element’s closing tag

    ```html
    <header>...</header>
    <section>
      ...
    </section><section>
      ...
    </section><section>
      ...
    </section>
    <footer>...</footer>
    ```

    + [Inline-Block Elements without White Space Demo](src/web02e-floatDemo08.html)
  + HTML comment
    + open an HTML comment directly after an `inline-block` element’s closing tag
    + close the HTML comment immediately before the next `inline-block` element’s opening tag

    ```html
    <header>...</header>
    <section>
      ...
    </section><!--
    --><section>
      ...
    </section><!--
    --><section>
      ...
    </section>
    <footer>...</footer>
    ```


## Creating Reusable Layouts

+ Reusable layouts best practice
  + high on the list of reusable code
  + recommendations
    + use inline-block elements to create the grid — or layout — of a page
    + then use floats when content to wrap around a given element
  + inline-block elements easier to work with
  + new CSS specifications in the works — specifically `flex-` and `grid-` based properties


### In Practice - Example: Styles Conference Website - Reusable Layout

1. create a three-column reusable layout using inline-block elements

  + three columns of equal width
  + two columns with the total width split between them, two-thirds in one and one-third in the other
  + create classes that define the width of these columns
    + `col-1-3`: for one-third
    + `col-2-3`: for two-thirds

  ```css
  .col-1-3 {
    width: 33.33%;
  }
  .col-2-3 {
    width: 66.66%;
  }
  ```

2. both of the columns to be displayed as `inline-block` elements

  ```css
  .col-1-3,
  .col-2-3 {
    display: inline-block;
    vertical-align: top;
  }
  ```

  + comma at the end of the first selector signifies that another selector is to follow
  + 2nd selector followed by the opening curly bracket, `{`, which signifies that style declarations are to follow
  + comma-separating the selectors: bind the same styles to multiple selectors at one time

3. put some space in between each of the columns
  
  + putting horizontal padding on each of the columns
  + issue: width of the space between them will be double that of the space from the outside columns to the edge of the row
  + solution: place all of columns within a grid and add the same padding from our columns to that grid

  ```css
  .grid,
  .col-1-3,
  .col-2-3 {
    padding-left: 15px;
    padding-right: 15px;
  }
  ```

4. setting up horizontal `padding`

  + `container` class: center all of our content on a page within a 960-pixel-wide element
  + put an element with the class of `grid` inside an element with the class of container
    + horizontal paddings add to one another
    + columns not appear proportionate to the width of the rest of the page
  + share some of the styles from the `container` rule set with the `grid` rule set

  ```css
  .container,
  .grid {
    margin: 0 auto;
    width: 960px;
  }
  .container {
    padding-left: 30px;
    padding-right: 30px;
  }
  ```

  + any element with the class of `container` or grid w/ be `960` pixels wide and centered on the page

5. work on HTML and observe how these classes perform

  + aligning home page into three columns
  + originally wrapped in a `<section>` element with the class of `container`
  + change class from `container` to `grid`

  ```html
  <section class="grid">
    ...
  </section>
  ```

6. add a class of `col-1-3` to each of the `<section>` elements within the `<section>` element with the class of `grid`

  ```html
  <section class="grid">

    <section class="col-1-3">
      ...
    </section>

    <section class="col-1-3">
      ...
    </section>

    <section class="col-1-3">
      ...
    </section>

  </section>
  ```

7. remove the empty white space between columns

  ```html
  01 <section class="grid">

  03  <!-- Speakers -->

  05  <section class="col-1-3">
      ...
  07  </section><!--
    
  09  Schedule
    
  11   --><section class="col-1-3">
      ...
  13  </section><!--
    
    Venue
    
  17  --><section class="col-1-3">
      ...
  19  </section>

  21 </section>
  ```

  + line 03: leave a comment identifying the “Speakers” section to follow
  + line 07: open a comment immediately after the closing `</section>` tag
  + line 09: identify the “Schedule” section to come
  + line 11: close the comment at the beginning, before the opening `<section>` tag

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/ybkg4vrk')"
    src    ="https://tinyurl.com/yyd7s3z2"
    alt    ="Styles Conference website"
  />
  <figcaption> Our Styles Conference home page now includes a three-column layout </figcaption>
</figure>


### Demo & Source Code

+ [View the Styles Conference Website](https://learn.shayhowe.com/practice/positioning-content/index.html)

+ [Download the Source Code](https://tinyurl.com/y4yxrs93)

+ [Local Demo: Styles Conference Website](src/positioning-content/index.html)



## Uniquely Positioning Elements

+ The `position` property
  + floats or inline-block elements not for precisely position
    + floats: remove an element from the flow of a page, often produce unwanted results as surrounding elements flow around the floated element
    + inline-block elements: fairly awkward to get into the proper position unless creating columns
  + `position` property
    + identify how an element positioned on a page and whether or not within the normal flow of a document
    + used in conjunction with the box offset properties
    + subproperties: `top`, `right`, `bottom`, and `left`
    + identify exactly where an element positioned by moving elements in a number of different directions
    + default: every element has a position value of `static`
      + exist in the normal flow of a document
      + not accept any box offset properties
    + most commonly overwritten with a `relative` or `absolute` value


### Relative Positioning

+ The `relative` value 
  + value of the `position` property
  + allow elements to appear within the normal flow a page, leaving space for an element as intended while not allowing other elements to flow around it
  + allow an element’s display position to be modified with the box offset properties

  ```html
  <div>...</div>
  <div class="offset">...</div>
  <div>...</div>
  ```

  ```css
  div {
    height: 100px;
    width: 100px;
  }
  .offset {
    left: 20px;
    position: relative;
    top: 20px;
  }
  ```

  + [Relative Positioning Demo](src/web02e-floatDemo09.html)
  + `offset` class
    + `position` property: `relative`
    + `left` & `right` properties: box offset to reposition the element
  + the box offset properties identify where an element moved from given its original position
  + `left: 20px;`: push the element towards the right, from the left, 20 pixels
  + `top: 20px;`: push an element towards the bottom, from the top, 20 pixels
  + the element overlaps the element when using the box offset properties




