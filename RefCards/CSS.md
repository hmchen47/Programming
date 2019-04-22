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





-------------------------------------------
<!--
[042]: 
[043]: 
[044]: 
[045]: 
[046]: 
[047]: 
[048]: 
[049]: 
[050]: 
[051]: 
[052]: 
[053]: 
[054]: 
[055]: 
[056]: 
[057]: 
[058]: 
[059]: 
[060]: 
[061]: 
[062]: 
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
