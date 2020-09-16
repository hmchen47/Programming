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
  
  + [Layout without Floats Demo1](src/web02e-floatDemo.html)
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

  + [Layout with Floats Demo 2](src/web02e-floatDemo2.html)


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

  + [Three-column Layout with Floats Demo](src/web02e-floatDemo3.html)


### Clearing & Containing Floats





## Positioning with Inline-Block





## Creating Reusable Layouts





## Uniquely Positioning Elements




