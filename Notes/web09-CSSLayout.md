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


- The box model
  - element's border and padding stretching out the element beyond the specified width
  - example: 

    ```css
    .simple {
      width: 500px;
      margin: 20px auto;
    }

    .fancy {
      width: 500px;
      margin: 20px auto;
      padding: 50px;
      border-width: 10px;
    }
    ```

    <div style="display: flex; justify-content: center;">
      <figure style="display: table; float: left; margin-right: 0.25em; align-items: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; height: 300px;"
          onclick= "window.open('https://en.wikipedia.org/wiki/CSS_box_model')"
          src    = "https://upload.wikimedia.org/wikipedia/commons/7/7a/Boxmodell-detail.png"
          alt    = "The CSS box model"
          title  = "The CSS box model"
        />
      </figure>
      <figure style="display: table; float: right; margin-left: 0.25em; align-items: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; height: 150px;"
          onclick= "window.open('https://learnlayout.com/box-model.html')"
          src    = "img/web09-boxmodel.png"
          alt    = "Screenshot of two containers for the box model"
          title  = "Screenshot of two containers for the box model"
        />
      </figure>
    </div>

