# Learn CSS Layout

[original](https://learnlayout.com/)


- No layout: one big column of element

- The `display` property
  - the most important property for controlling layout
  - every element w/ default display
  - most default values: **block** and **inline**
  - `block` values
    - `div`: the standard block-level element
    - starting on a *new-line* ans stretching out to the left and right as far as it could
    - example elements: `p`, `form`, `header`, `footer`, `section`, etc.
  - `inline` values
    - `span`: the standard inline element
    - wraping some text *inside* a paragraph `<span>like this</span>` w/o disrupting the flow of  the paragraph
    - most common element: `a`
  - `none` value
    - commonly used w/ JavaScript to hide and show element w/o really deleting and recreating them
    - rendering the page as though the element does not exist
    - `visibility: hidden`: hiding the element, but the element will still take up the space it would  if it was fully visible
    - always able to override default


- Centralizing elements
  - syntax: `margin: 0 auto;`

    ```css
    #main {
      margin: 0 auto;
    }
    ```

  - width of a block-level element preventing from stretching out to the edges of its container to the left and right
  - setting left and right margins to `auto` to horizontally center the element within its container
  - element taking up the width specified, then, evenly splitting the remaining space b/w two margins
  - issue: screen narrower than the width <br>
    sol: browser creating horizontal scrollbar on the page


- The `max-width` property
  - improving the browser's handling of small window
  - making a site usable on mobile
  - example: `<div id="main"> text insert here</div>

    ```css
    #main {
      max-width: 600px;
      margin: 0 auto; 
    }
    ```



