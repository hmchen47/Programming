# Cascading Style Sheet (CSS)


## Tools

+ [CSS Validator][000]

+ [CSS Zen Garden][003]

## [CSS design principles(CSS 2.2)][001]

+ Forward and backward compatibility.
+ Complementary to structured documents.
+ Vendor, platform, and device independence.
+ Maintainability.
+ Simplicity.
+ Network performance.
+ Flexibility
+ Richness
+ Alternative language binding.
+ Accessibility

## [Effective Use of Style Sheets][002]

+ Generalized Style
  + single style sheet for all of the pages on your site
  + linked style sheets
  + centralized design
  + active evangelism program
  + plenty of examples
  + page authors should be allowed to create additional embedded styles for their own pages
+ Implementation advice
  + continue to work when style sheets are disabled
  + Do not use more than two fonts
  + Do not use absolute font sizes
  + Do not use the !important attribute
  + use the same CLASS names for the same concept in all of the style sheets

## [CSS Best Practice][056]

+ [Executive summary][057]
  + Logical source order: accessibility, mobile optimization, device adaptability, and long-term maintainability.
  + Liquid layouts and relativity: Use smart relative sizing
  + Media queries: get font size adaptation free by using `em`s
  + Prevent zombie code: Delete it before it does, and ruins your layout
  + Test in multiple browsers: Your favorite browser is not always right.
  + Don't use proprietary features! Don't rely on the latest -WebKit- invention.
  + Turn off CSS: A well-coded page will be understandable without it.

+ [Foundations][058]
  + Indent your code for readability ease
  + Learn how to code CSS before relying on frameworks (such as Bootstrap, etc.)
  + Separate content and style
    + Use semantic markup, ie., "classes for meaning, not for show".
    + Use `<table>` for tabular data: don't use tables for layout
  + Linearized logical source order
    + The order of the HTML content should make sense even without the CSS.
      + for long-term site maintainability
      + for mobile
      + for accessibility
      + as a foundation for device adaptation (media queries)
  + Linguistic variations: set the language correctly for better typography

+ [Testing][059]
  + Test without CSS: turn off CSS, and if the page makes no sense, fix your markup.
  + Test in multiple environments:
    + Resize the window
    + Zoom the text
    + Try a mobile browser
    + Navigate by keyboard
  + Test in multiple browsers: remember that just testing in Chrome does not work for everyone! ;)

+ [Adaptability][060]
  + Media queries: set media query breakpoints in `em` or `ch`, not always in `px`.
  + Liquid layouts and relativity: what is your sizing based on?
    + Containing block size? → Use percents.
    + Viewport size? → Use viewport units: `vw`, `vh`, `vmin`, `vmax`
    + Font height? → Use `em` or `rem`.
    + Font pitch? → Use `em` or `ch`.
    + Content size? → Use auto or min-content/max-content.
    + Combination of the above? → Use the appropriate layout formulas: `flex`, `min-width`, `max-width`, etc.

+ [Defensive Coding][061]
  + `!important` means never override- to use with caution
  + Use !important to define overriding rules, not for fixups
  + Duplicate selectors if you need to increase specificity, or
  + Simplify selectors if you need to decrease specificity
  + Don't over-escalate: understand your code, and don't overkill.
  + Drop dead code: you tried something and it didn't work? Delete it right away!
  + Code to Standard
  + Don't rely on proprietary extensions
  + Don't use experimental features in production or commit to keeping up-to-date.
  + Provide fallbacks / use @supports.


## [CSS Syntax][004]

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/fa2e67e5afb94de3981b22805acd686c/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4098c09f586c9c45349fe25ca9e1742a14">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/39ef39b8e6685b816badb923520fa827/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-3-1_css_anatomy.PNG" style="margin: 0.1em;" alt="A CSS rule is broken into two parts: the selector and the property" title="css anatomy" width="250">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/989b2e8ecef6fec3fcc6fd02a5baed58/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-3-1_property_anatomy.PNG" style="margin: 0.1em;" alt="This is what tells the browser how to style the HTML tag that has been selected. This can be as many lines of code as you choose, each of which has two parts- the property and the value you want that property to be." title="property anatomy" width="250">
  </a></div>
</div>

+ Selector:
  + tell the browser what HTML tags this rule applies to
  + types: tag, class & id
  + attribute selectors: Classes and IDs
  + multiple HTML elements with similar style: `p, ul, ol {color: blue; }`

+ Property:
  + tell the browser how to style the HTML tag that has been selected
  + as many lines of code as you choose
  + each of which has two parts- the property and the value you want that property to be
  + with its own collection of possible values
  + [complete list of latest CSS properties][005] at the W3C


## Selectors

| Selector | Description | Declaration | Usage | Link |
|----------|-------------|-------------|-------|------|
| `.class` | an HTML attribute that specifies a name for a group of elements on the page | `.className { color: blue; }` | `<p class="className">paragraph</p>` | [W3C][023], [Selectors][024] |
| `#id` | an HTML attribute that specifies a name or unique identifier for a particular HTML element | `#MyFirstId { color: blue; }` | `<p id="MyFirstId"> special paragraph </p>` | [W3C][025], [Selectors][026] |
| `element` | select all elements | `p { color: blue;}` | `<p>Paragraph</p>` | [W3C][027] |
| `element1, element2` | select all element1 & element2 | `p, div { color: blue; }` | `<div> division </div>`, `<p> paragraph </p>` | [W3C][027] |
| `element1 element2` | select all element2 inside element 1 | `div p { color: blue;}` | `<div> <p> text </p> </div>`, `<div> <article> <p> text </p> </article> </div>` | [W3C][027] [Selector][034] |
| `element1>element2` | select all element2 where the parent is element1 | `div>p {color: blue;}` | `<div> <img /> <p> text </p> </div>` | [W3C][027] |
| `element1+element2` | select all element2placed immediately after element1 | `div+p { color: blue;}` | `<div> <p> text </p> </div>`  | [W3C][027] |
| `e:state` | pseudo-classes, applied to an existing selector based on their state | `a:active {color: blue;}` | `<a href="url">` | [W3C][027] |
| `e:link`, `e:visited` | User agents commonly display unvisited links differently from previously visited ones | `a:link { color: blue; }`, `a:visited {color: orange}` | [W3C][028] [Selector][029] |
| `e:hover` | applies while the user designates an element (with some pointing device), but does not activate it | `li.hover { background-color: green; }` | `<li> text </li>` | [W3C][030], [W3C][031], [Selector][032] |
| `e.active` | applies while an element is being activated by the user | `li.active {background-color: orange;}` | `<li> text </li>` | [W3C][031], [Selector][033] |
| `e.focus` | applies while an element has the focus (accepts keyboard events or other forms of text input) | `li.focus { background-color: blue;}` | `<li> text </li>` | [W3C][031], [Selector][033] |


## Tree Presentation - Inheritance

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/0e1bd16d542e4a1085cb8d9b305f8e59/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40833b012fc6dd41f68fa5fd6e3b93e8a8">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c3441bd3d744e14d5d1c0c663d7ad1dc/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-4-2_inheritance_tree.PNG" style="margin: 0.1em;" alt="ags that contain other tags are parents, and the tags inside of them are their children in the following tree representation." title="HTML inheritance structure" width="250">
  </a></div>
</div>

+ CSS property values set on one element will be transferred down the tree to that element's children.
+ Not every property is inherited, but many are.

## [Selector's specificity][036]

+ Calculate specificity
  + count the number of ID selectors in the selector (= a)
  + count the number of class selectors, attributes selectors, and pseudo-classes in the selector (= b)
  + count the number of type selectors and pseudo-elements in the selector (= c)
  + ignore the universal selector (`*`)

+ Example

  ```
  *               /* a=0 b=0 c=0 -> specificity =   0 */
  LI              /* a=0 b=0 c=1 -> specificity =   1 */
  UL LI           /* a=0 b=0 c=2 -> specificity =   2 */
  UL OL+LI        /* a=0 b=0 c=3 -> specificity =   3 */
  H1 + *[REL=up]  /* a=0 b=1 c=1 -> specificity =  11 */
  UL OL LI.red    /* a=0 b=1 c=3 -> specificity =  13 */
  LI.red.level    /* a=0 b=2 c=1 -> specificity =  21 */
  #x34y           /* a=1 b=0 c=0 -> specificity = 100 */
  #s12:not(FOO)   /* a=1 b=0 c=1 -> specificity = 101 */
  ```

## Color Properties

| Property | Description | Link |
|----------|-------------|------|
| `color` | the foreground color of an element's text content | [W3C][006], [Color][007] |
| `background-color` | background color of an element | [W3C][008], [Color][009] |

### HTML Color Names and Values

+ A `<color>` is either a keyword or a numerical RGB specification.
+ [Color names and sRGB values](HTML-Color.md)

+ Complementary and Triadic colour schemes

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://www.w3.org/wiki/Colour_theory">
      <img src="https://www.w3.org/wiki/images/4/49/50000000.jpg" style="margin: 0.1em;" alt="the complementary scheme, where you match up colours that lie directly opposite each other on the colour wheel." title="Complementary colour schemes" width="450">
      <img src="https://www.w3.org/wiki/images/e/e5/80000001.jpg" style="margin: 0.1em;" alt="A triadic colour scheme is created when you pick one colour and then pick two other colours that lie equidistant from each other around the circle." title="Triadic colour schemes" width="300">
    </a></div>
  </div>


## [Font Property][010]

| Property | Description | Value | Link |
|----------|-------------|------|-------|
| `font-family` | font face, a collection of Web safe fonts that generally each browser has agreed to support | `Verdana`, `New Time Roman` | [W3C][011], [Fonts][012] |
| `font-size` | overall scale of the text | `em`, `%`, `px` | [W3C][013], [Fonts][014] |
| `font-weight` | thickness of the letters | 100~900, `bold`=700, `normal` = 400, `bolder`, `lighter` | [W3C][015], [Fonts][016] |
| `font-style` | adjust the angle of the letters in relation to the horizontal plane | `italic`, `normal`, `oblique <angle>` | [W3C][017], [Fonts][018] |
| `text_decoration` | add a line across text | `underline` | [W3C][019], [Fonts][020] |


### [Typography][066]

+ sans-serif: the letters do not have added flourishes; most popular; `Helvetica`, `Verdana`, `Arial`, `Tahoma`
+ serif - the small flourish lines at the edges of letters and symbols; `Times New Roman`, `Book Antiqua`, `Georgia`
+ monospace - all letters have the same fixed width; `Courier New`
+ cursive - mimic human handwriting often by joining letters or having an italic slant; `Comic Sans MS`
+ fantasy - the most diverse category of fonts including all of those that are particularly decorative



## Spacing Property

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/b51f656fe5bd47a7b2f24fe7617b7870/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40021c5be913ac42348edca84f9a89bf46">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f6f6c946356774ddb886956cd94df4c9/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/margin__padding__border.png" style="margin: 0.1em;" alt="Diagram presenting the relationship of margin, padding and border" title="Box Model" width="300">
  </a></div>
</div>

| Property | Description | Value | Link |
|----------|-------------|------|-------|
| `padding`, `padding-top`, `padding-right`, `padding-bottom`, `padding-left` | the white space that sits closest to an HTML element | `px`, `em` | [W3C][021], [Space][022] |
| `border`, `border-top`, `border-right`, `border-bottom`, `border-left` | the area outside the padding of an HTML element | `1px black solid` | [W3C][023], [Space][024] |
| `margin`, `margin-top`, `margin-right`, `margin-bottom`, `margin-left` | the white space that sits outside the border | `auto`, `em`, `px` | [W3C][025], [Space][026] |


## Image Property

See [Image Attributes][]


## Alignment Property

| Property | Description | Value | Link |
|----------|-------------|------|-------|
| `text-align` | set the content's alignment horizontally | `left`, `right`, `center`, `justify` | [W3C][038], [Alignment][039] |
| `line-height` | HTML element block grows and the text will vertically center within it | [W3C][040], [Alignment][041] |


## Element width and height

| Property | Description | Value | Link |
|----------|-------------|------|-------|
| `width` | element width | `<length>`, `<percentage>`, `auto`, `inherit`  | [W3C][043] [Element][047] |
| `height` | element height | `<length>`, `<percentage>`, `auto`, `inherit` | [W3C][044] [Element][047] |
| `min-width` | minimum width of the element | `<length>`, `<percentage>`, `inherit` | [W3C][045] [Element][048] |
| `min-width` | maximum width of the element |`<length>`, `<percentage>`, `none`, `inherit` | [W3C][045] [Element][048] |
| `min-height` | minimum height of the element |`<length>`, `<percentage>`, `inherit` | [W3C][046] [Element][048] |
| `max-width` | maximum height of the element |`<length>`, `<percentage>`, `none`, `inherit` | [W3C][046] [Element][048] |


## Floating Property

| Property | Description | Value | Link |
|----------|-------------|------|-------|
| `float` | liberates an element from its automatic position and lifts it up to "float" on top of other elements in the direction specified | `left`, `right`, `none`, `inherit` | [W3C][050], [Float][050] |
| `clear` | indicate which sides of an element's box(es) may not be adjacent to an earlier floating box | `none`, `left`, `right`, `both`, `inherit` | [W3C][051], [Float][052] |


## Position Property

| Property | Description | Value | Link |
|----------|-------------|------|-------|
| `position` | set the algorithm for how the Web browser will compute the way the HTML elements are placed on the pag | `static`, `relative`, `absolute`, `fixed`, `inherit` | [W3C][053], [Position][054] |
| `top` | specify how far an absolutely positioned box's top margin edge is offset below the top edge of the box's containing block | `<length>`, `<percentage>`, `auto`, `inherit` | [W3C][055], [Position][054] |
| `right` | specify how far a box's right margin edge is offset to the left of the right edge of the box's containing block | `<length>`, `<percentage>`, `auto`, `inherit` | [W3C][055], [Position][054] |
| `bottom` | specify how far a box's bottom margin edge is offset above the bottom of the box's containing block | `<length>`, `<percentage>`, `auto`, `inherit` | [W3C][055], [Position][054] |
| `left` | specify how far a box's left margin edge is offset to the right of the left edge of the box's containing block | `<length>`, `<percentage>`, `auto`, `inherit` | [W3C][055], [Position][054] |






-------------------------------------------
<!--
[062]: https://github.com/hmchen47/Programming/blob/css/WebDev/Frontend-W3C/4-CSSBasics/05-DesignWeb.md#typography
[063]: 
[064]: 
[065]: 
[066]: 
[067]: 
[068]: 
[069]: 
[070]: 
[071]: 
[072]: 
[073]: 
[074]: 
[075]: 
[076]: 
[077]: 
[078]: 
[079]: 
[080]: 
[081]: 
[082]: 
[083]: 
[084]: 
[085]: 
[086]: 
[087]: 
[088]: 
[089]: 
[090]: 
[091]: 
[092]: 
[093]: 
[094]: 
[095]: 
[096]: 
[097]: 
[098]: 
[099]: 
[100]: 
[101]: 
[102]: 
[103]: 
[104]: 
[105]: 
[106]: 
[107]: 
[108]: 
[109]: 
[100]: 
[111]: 
[112]: 
[113]: 
[114]: 
[115]: 
[116]: 
[117]: 
[118]: 
[119]: 
[120]: 
[121]: 
[122]: 
[123]: 
[124]: 
[125]: 
[126]: 
[127]: 
[128]: 
[129]: 
[130]: 
[131]: 
[132]: 
[133]: 
[134]: 
[135]: 
[136]: 
[137]: 
[138]: 
[139]: 
[140]: 
[141]: 
[142]: 
[143]: 
[144]: 
[145]: 
[146]: 
[147]: 
[148]: 
[149]: 
[150]: 
[151]: 
[152]: 
[153]: 
[154]: 
[155]: 
[156]: 
[157]: 
[158]: 
[159]: 
[160]: 
[161]: 
[162]: 
[163]: 
[164]: 
[165]: 
[166]: 
[167]: 
[168]: 
[169]: 
[170]: 
[171]: 
[172]: 
[173]: 
[174]: 
[175]: 
[176]: 
[177]: 
[178]: 
[179]: 
[180]: 
[181]: 
[182]: 
[183]: 
[184]: 
[185]: 
[186]: 
[187]: 
[188]: 
[189]: 
[190]: 
[191]: 
[192]: 
[193]: 
[194]: 
[195]: 
[196]: 
[197]: 
[198]: 
[199]: 
-->

[000]: https://jigsaw.w3.org/css-validator/
[001]: https://www.w3.org/TR/CSS22/intro.html#design-principles
[002]: https://www.nngroup.com/articles/effective-use-of-style-sheets/
[003]: http://www.csszengarden.com/
[004]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#constructing-your-css-rules
[005]: https://www.w3.org/Style/CSS/all-properties#list
[006]: https://www.w3.org/TR/css3-color/#foreground
[007]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#color
[008]: https://www.w3.org/TR/css3-background/#the-background-color
[009]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#background-color
[010]: https://www.w3.org/Style/Examples/007/fonts
[011]: https://www.w3.org/TR/css-fonts/#font-family-prop
[012]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#font-family
[013]: https://www.w3.org/TR/css-fonts/#font-size-prop
[014]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#font-size
[015]: https://www.w3.org/TR/css-fonts/#font-weight-prop
[016]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#font-weight
[017]: https://www.w3.org/TR/CSS2/box.html#propdef-padding-top
[018]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#padding
[019]: https://www.w3.org/TR/css3-background/#borders
[020]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#border
[021]: https://www.w3.org/TR/CSS2/box.html#propdef-margin
[022]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#margin
[023]: https://www.w3.org/TR/html52/dom.html#classes
[024]: ../WebDev/Frontend-W3C/4-CSSBasics/03-Selectors.md#classes
[025]: https://www.w3.org/TR/html52/dom.html#the-id-attribute
[026]: ../WebDev/Frontend-W3C/4-CSSBasics/03-Selectors.md#ids
[027]: https://www.w3schools.com/cssref/css_selectors.asp
[028]: https://www.w3.org/TR/CSS22/selector.html#link-pseudo-elements
[029]: ../WebDev/Frontend-W3C/4-CSSBasics/03-Selectors.md#link-and-visited
[030]: ../WebDev/Frontend-W3C/4-CSSBasics/03-Selectors.md#hover
[031]: https://www.w3.org/TR/CSS22/selector.html#dynamic-pseudo-classes
[032]: ../WebDev/Frontend-W3C/4-CSSBasics/03-Selectors.md#hover
[033]: ../WebDev/Frontend-W3C/4-CSSBasics/03-Selectors.md#focus
[034]: ../WebDev/Frontend-W3C/4-CSSBasics/03-Selectors.md#active
[035]: ../WebDev/Frontend-W3C/4-CSSBasics/03-Selectors.md#contextual-selectors
[036]: https://www.w3.org/TR/selectors-3/#specificity
[037]: ./HTML.md#image-element
[038]: https://www.w3.org/TR/CSS22/text.html#alignment-prop
[039]: ../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#text-align
[040]: https://www.w3.org/TR/CSS22/visudet.html#line-height
[041]: ../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#line-height
[042]: https://www.w3.org/TR/CSS22/visudet.html#the-width-property
[043]: ../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#width-and-height
[044]: https://www.w3.org/TR/CSS22/visudet.html#the-height-property
[045]: https://www.w3.org/TR/CSS22/visudet.html#min-max-widths
[046]: https://www.w3.org/TR/CSS22/visudet.html#min-max-heights
[047]: ../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#width-and-height
[048]: ../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#min-width-max-width-min-height-max-height
[049]: https://www.w3.org/TR/CSS22/visuren.html#float-position
[050]: ../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#the-float-property
[051]: https://www.w3.org/TR/CSS22/visuren.html#propdef-clear
[052]: ../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#the-clear-property
[053]: https://www.w3.org/TR/CSS22/visuren.html#choose-position
[054]: ../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#the-position-property
[055]: https://www.w3.org/TR/CSS22/visuren.html#position-props
[056]: ../WebDev/Frontend-W3C/4-CSSBasics/05-DesignWeb.md#css-best-practices
[057]: ../WebDev/Frontend-W3C/4-CSSBasics/05-DesignWeb.md#executive-summary
[058]: ../WebDev/Frontend-W3C/4-CSSBasics/05-DesignWeb.md#foundations
[059]: ../WebDev/Frontend-W3C/4-CSSBasics/05-DesignWeb.md#testing
[060]: ../WebDev/Frontend-W3C/4-CSSBasics/05-DesignWeb.md#adaptability
[061]: ../WebDev/Frontend-W3C/4-CSSBasics/05-DesignWeb.md#defensive-coding