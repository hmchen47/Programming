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
        <img style="margin: 0.1em; padding-top: 0.5em; height: 200px;"
          onclick= "window.open('https://learnlayout.com/box-model.html')"
          src    = "img/web09-boxmodel.png"
          alt    = "Screenshot of two containers for the box model"
          title  = "Screenshot of two containers for the box model"
        />
      </figure>
    </div>


- The `box-sizing` property
  - original box model behavior considered unintuitive
  - `box-sizing: border-box;`: the padding and border of the element including in the width and height of aan element
  - example

    ```css
    .simple {
      width: 500px;
      margin: 20px auto;
      -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
              box-sizing: border-box;
    }

    .fancy {
      width: 500px;
      margin: 20px auto;
      padding: 50px;
      border: solid blue 10px;
      -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
              box-sizing: border-box;
    }
    ```

    <figure style="display: table; margin: auto; text-align: center;"">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
        onclick= "window.open('https://learnlayout.com/box-sizing.html')"
        src    = "img/web09-boxsizing.png"
        alt    = "Snapshot of box-siging example"
        title  = "Snapshot of box-siging example"
      />
    </figure>

  - enabling all elements w/ the same box size

    ```css
    * {
      -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
              box-sizing: border-box;
    }
    ```

  - new property:
    - using the `-webkit-` and `-moz-` prefixes for now
    - checking [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing#browser_compatibility)


- The `position` property
  - a bunch of possible values but no sense
  - `static`
    - default value
    - *not positioning* in any specific way
    - positioned: element w/ `position` set to anything else
  - `relative`
    - behaving the same as static unless you add some extra properties
    - adjusted away from its normal position: the `top`, `right`, `bottom`, and `left` properties

    <figure style="display: table; margin: auto; text-align: center;"">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
        onclick= "window.open('https://learnlayout.com/position.html')"
        src    = "img/web09-position_static.png"
        alt    = "Snapshot of static position example"
        title  = "Snapshot of static position example"
      />
    </figure>

  - `fixed`
    - positioned relative to the *viewpoint*
    - stayed in the same place even if the page is scrolled
    - properties: `top`, `right`, `bottom`, and `left`
    - fixed element in the lower-right corner of the page

      ```css
      .fixed {
        position: fixed;
        bottom: 0;
        right: 0;
        width: 200px;
        background-color: white;
      }
      ```

    - not leaving a gap in the page where it normally have been located
  - `absolute`
    - the trickiest position value
    - like fixed except relative to the *nearest positioned ancestor* instead of relative to the viewpoint
    - no positioned ancestor $\implies$ using document body and still moving along w/ page scrolling
    - example 

      ```css
      .relative {
        position: relative;
        width: 600px;
        height: 400px;
      }
      .absolute {
        position: absolute;
        top: 120px;
        right: 0;
        width: 300px;
        height: 200px;
      }
      ```

      <figure style="display: table; margin: auto; text-align: center;"">
        <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
          onclick= "window.open('https://learnlayout.com/position.html')"
          src    = "img/web09-position_absolute.png"
          alt    = "Snapshot of 'absolute' position example"
          title  = "Snapshot of 'absolute' position example"
        />
      </figure>





