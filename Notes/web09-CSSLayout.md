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
      <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
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
    - positioned relative to the *viewport*
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
    - like fixed except relative to the *nearest positioned ancestor* instead of relative to the viewport
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
        <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
          onclick= "window.open('https://learnlayout.com/position.html')"
          src    = "img/web09-position_absolute.png"
          alt    = "Snapshot of 'absolute' position example"
          title  = "Snapshot of 'absolute' position example"
        />
      </figure>


- Position example
  - stretching to the width of the window

  ```css
  .container {
    position: relative;
  }
  nav {
    position: absolute;
    left: 0px;
    width: 200px;
  }
  section {
    /* position is static by default */
    margin-left: 200px;
  }
  footer {
    position: fixed;
    bottom: 0;
    left: 0;
    height: 70px;
    background-color: white;
    width: 100%;
  }
  body {
    margin-bottom: 120px;
  }
  ```

  <figure style="display: table; margin: auto; text-align: center;"">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open('https://learnlayout.com/position-example.html')"
      src    = "img/web09-position_exp.png"
      alt    = "Snapshot of various positioning example"
      title  = "Snapshot of various positioning example"
    />
  </figure>


- The `float` property
  - intended for wrapping text around images
  - example

    ```css
    img {
      float: right;
      margin: 0 0 1em 1em;
    }
    ```

    <figure style="display: table; margin: auto; text-align: center;"">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
        onclick= "window.open('https://learnlayout.com/float.html')"
        src    = "img/web09-float.png"
        alt    = "Snapshot of various positioning example"
        title  = "Snapshot of various positioning example"
      />
    </figure>


- The `clear` property
  - important for controlling the behavior of floats
  - example w/o `clear` (left diagram)

    ```html
    <div class="box">...</div>
    <section>...</section>
    ```

    ```css
    .box {
      float: left;
      width: 200px;
      height: 100px;
      margin: 1em;
    }
    ```

  - example w/ `clear` (right diagram)

    ```css
    .box {
      float: left;
      width: 200px;
      height: 100px;
      margin: 1em;
    }
    .after-box {
      clear: left;
    }
    ```

  <div style="display: flex; justify-content: center;">
    <figure style="display: table; float: left; margin-right: 0.25em; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 400px;"
        onclick= "window.open('https://en.wikipedia.org/wiki/CSS_box_model')"
        src    = "img/web09-clear0.png"
        alt    = "Snapshot of float example w/o clear property"
        title  = "Snapshot of float example w/o clear property"
      />
      <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
        float example w/o clear property
      </figcaption>
    </figure>
    <figure style="display: table; float: right; margin-left: 0.25em; align-items: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 400px;"
        onclick= "window.open('https://learnlayout.com/box-model.html')"
        src    = "img/web09-clear1.png"
        alt    = "Snapshot of float example w/ clear property"
        title  = "Snapshot of float example w/ clear property"
      />
      <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
        float example w/ clear property
      </figcaption>
    </figure>
  </div>


- The `clearfix` hack
  - weird, bad thing happened w/ `float`
  - way to fixed: `clearfix`
  - example

    ```css
    /* simple float - left diagram*/
    img {
      float: right;
    }

    /* clear float after use - right diagram */
    .clearfix {
      overflow: auto;
    }
    ```

    <div style="display: flex; justify-content: center;">
      <figure style="display: table; float: left; margin-right: 0.25em; align-item: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; height: 150px;"
          onclick= "window.open('https://learnlayout.com/clearfix.html')"
          src    = "img/web09-clearfix0.png"
          alt    = "Simple float produces weird, bad layout"
          title  = "Simple float produces weird, bad layout"
        />
        <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
          Simple float produces weird, bad layout
        </figcaption>
      </figure>
      <figure style="display: table; float: right; margin-left: 0.25em; align-item: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; height: 150px;"
          onclick= "window.open('https://learnlayout.com/clearfix.html')"
          src    = "img/web09-clearfix1.png"
          alt    = "Eliminate weird layout w/ clearfix"
          title  = "Eliminate weird layout w/ clearfix"
        />
        <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
          Eliminate weird layout w/ clearfix
        </figcaption>
      </figure>
    </div>


- Float layout example
  - using `float` property than `position` property

  ```css
  nav {
    float: left;
    width: 200px;
  }
  section {
    margin-left: 200px;
  }
  ```

  <figure style="display: table; margin: auto; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open('https://learnlayout.com/float-layout.html')"
      src    = "img/web09-floatexp.png"
      alt    = "The same layout using float property"
      title  = "The same layout using float property"
    />
    <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
      The same layout using <code>float</code> property, not <code>position</code> property, to make things easier
    </figcaption>
  </figure>


- The percent width
  - percent: measurement unit relative to the containing block
  - great for image (left diagram)

    ```css
    article img {
      float: right;
      width: 50%;
    }
    ```

  - percent width layout (right diagram)
    - the `nav` content starting to wrap in a displeasing way when the windoe is too narrow

    ```css
    nav {
      float: left;
      width: 25%;
    }
    section {
      margin-left: 25%;
    }
    ```

    <div style="display: flex; justify-content: center;">
      <figure style="display: table; float: left; margin-right: 0.25em; align-item: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; height: 150px;"
          onclick= "window.open('https://learnlayout.com/percent.html')"
          src    = "img/web09-percent1.png"
          alt    = "Limiting image width w/ percentage of the container"
          title  = "Limiting image width w/ percentage of the container"
        />
        <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
          Limiting image width w/ percentage of the container 
        </figcaption>
      </figure>
      <figure style="display: table; float: right; margin-left: 0.25em; align-item: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; height: 150px;"
          onclick= "window.open('https://learnlayout.com/percent.html')"
          src    = "img/web09-percent2.png"
          alt    = "Flexible nav bar width w/ percent width of the page layout"
          title  = "Flexible nav bar width w/ percent width of the page layout"
        />
        <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
          Flexible nav bar width w/ percent width of the page layout
        </figcaption>
      </figure>
    </div>


- Media queries
  - **responsive design:**
    - the strategy of make a site that 'responds' to the browser and device
    - being shown on the browser and device by looking awesome no matter of what
  - the most powerful tool for responsive design
  - using percent width and displaying in one column when the browser too small to fit in the sidebar
  - references
    - [media queries examples](https://mediaqueri.es/)
    - [MDN web doc - Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries)
    - [An Introduction to Meta Viewport and @viewport](https://dev.opera.com/articles/an-introduction-to-meta-viewport-and-viewport/)
  - example

    ```css
    @media (min-width:600px) {
      nav {
        float: left;
        width: 25%;
      }
      section {
        margin-left: 25%;
      }
    }
    @media (max-width:599px) {
      nav li {
        display: inline;
      }
    }
    ```

    <figure style="display: table; margin: auto; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
        onclick= "window.open('https://learnlayout.com/media-queries.html')"
        src    = "img/web09-mediaquery.png"
        alt    = "One column layout instead of two columns when the window narrower than the nav bar size"
        title  = "One column layout instead of two columns when the window narrower than the nav bar size"
      />
      <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
        One column layout instead of two columns when the window narrower than the nav bar size
      </figcaption>
    </figure>


- The `inline-block` attribute
  - using `float` to create a grid of boxes that fills the browser width and wraps nicely
  - `inline-block` attribute making it easier
  - similar to `inline` element but w/ width and height
  - extra work required to support IE6 & IE7
  - the hard way w/ `float` property (left diagram)

    ```css
    .box {
      float: left;
      width: 200px;
      height: 100px;
      margin: 1em;
    }
    .after-box {
      clear: left;
    }
    ```

  - the easy way w/ `inline-block` attribute (right diagram)

    ```css
    .box2 {
      display: inline-block;
      width: 200px;
      height: 100px;
      margin: 1em;
    }
    ```

  <div style="display: flex; justify-content: center;">
    <figure style="display: table; float: left; margin-right: 0.25em; align-item: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; height: 250px;"
        onclick= "window.open('https://learnlayout.com/inline-block.html')"
        src    = "img/web09-inlineblock0.png"
        alt    = "Grid boxes using float property"
        title  = "Grid boxes using float property"
      />
      <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
        Grid boxes using float property
      </figcaption>
    </figure>
    <figure style="display: table; float: right; margin-left: 0.25em; align-item: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; height: 250px;"
        onclick= "window.open('https://learnlayout.com/inline-block.html')"
        src    = "img/web09-inlineblock1.png"
        alt    = "Grid boxes using inline-block attribute"
        title  = "Grid boxes using inline-block attribute"
      />
      <figcaption style="display: table-caption; caption-side: bottom; text-align: center;">
        Grid boxes using inline-block attribute
      </figcaption>
    </figure>
  </div>




