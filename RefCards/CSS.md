# Cascading Style Sheet (CSS)


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


## Tools

+ [CSS Validator][000]

+ [CSS Zen Garden][003]


## [CSS Syntax][004]

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div>
  <a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/fa2e67e5afb94de3981b22805acd686c/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%4098c09f586c9c45349fe25ca9e1742a14">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/39ef39b8e6685b816badb923520fa827/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-3-1_css_anatomy.PNG" style="margin: 0.1em;" alt="A CSS rule is broken into two parts: the selector and the property" title="css anatomy" width="250">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/989b2e8ecef6fec3fcc6fd02a5baed58/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-3-1_property_anatomy.PNG" style="margin: 0.1em;" alt="This is what tells the browser how to style the HTML tag that has been selected. This can be as many lines of code as you choose, each of which has two parts- the property and the value you want that property to be." title="property anatomy" width="250">
  </a>
  <a href="https://www.w3schools.com/css/css_syntax.asp">
    <img src="https://www.w3schools.com/css/selector.gif" style="margin: 0.1em;" alt="The selector points to the HTML element you want to style. The declaration block contains one or more declarations separated by semicolons. Each declaration includes a CSS property name and a value, separated by a colon. A CSS declaration always ends with a semicolon, and declaration blocks are surrounded by curly braces." title="CSS rule-set consists of a selector and a declaration block" width="300">
  </a>
  </div>
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



## Measurement Units

| Unit | Specification | Link |
|------|---------------|------|
| `px` | pixel, a single dot on the screen | [Units][081] |
| `em` | vertical dimensions, height of capital letter in the _parent_ context | [Units][082] |
| `rem` | vertical dimensions, size relative to the _root_ | [Units][083] |
| `%` | relative to the _parent_ dimension | [Units][084] |
| `vh` | viewport height, percentage of the screen | [Units][085] |
| `vw` | viewport width, percentage of the screen | [Units][085] |



## Selectors

### [CSS Selector Reference](https://www.w3schools.com/cssref/css_selectors.asp)

<table  style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%">Selector</th>    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%">Example</th>    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;">Example description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="sel_class.asp">.<i>class</i></a></td>    <td>.intro</td>    <td>Selects all elements with class="intro"</td>
  </tr>
  <tr>
    <td><a href="sel_id.asp">#<i>id</i></a></td>    <td>#firstname</td>    <td>Selects the element with id="firstname"</td>
  </tr>  <tr>
    <td><a href="sel_all.asp">*</a></td>    <td>*</td>    <td>Selects all elements</td>
  </tr>
  <tr>
    <td><i><a href="sel_element.asp">element</a></i></td>    <td>p</td>    <td>Selects all &lt;p&gt; elements</td>
  </tr>
  <tr>
    <td><i><a href="sel_element_comma.asp">element,element</a></i></td>    <td>div, p</td>    <td>Selects all &lt;div&gt; elements and all &lt;p&gt; elements</td>
  </tr>
  <tr>
    <td><a href="sel_element_element.asp"><i>element</i> <i>element</i></a></td>    <td>div p</td>    <td>Selects all &lt;p&gt; elements inside &lt;div&gt; elements</td>
  </tr>
  <tr>
    <td><a href="sel_element_gt.asp"><i>element</i>&gt;<i>element</i></a></td>    <td>div &gt; p</td>    <td>Selects all &lt;p&gt; elements where the parent is a &lt;div&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_element_pluss.asp"><i>element</i>+<i>element</i></a></td>    <td>div + p</td>    <td>Selects all &lt;p&gt; elements that are placed immediately after &lt;div&gt; elements</td>
  </tr>
  <tr>
    <td><a href="sel_gen_sibling.asp"><i>element1</i>~<i>element2</i></a></td>    <td>p ~ ul</td>    <td>Selects every &lt;ul&gt; element that are preceded by a &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_attribute.asp">[<i>attribute</i>]</a></td>    <td>[target]</td>    <td>Selects all elements with a target attribute</td>
  </tr>
  <tr>
    <td><a href="sel_attribute_value.asp">[<i>attribute</i>=<i>value</i>]</a></td>    <td>[target=_blank]</td>    <td>Selects all elements with target="_blank"</td>
  </tr>
  <tr>
    <td><a href="sel_attribute_value_contains.&#x24;asp">[<i>attribute</i>~=<i>value</i>]</a></td>    <td>[title~=flower]</td>    <td>Selects all elements with a title attribute containing the word "flower"</td>
  </tr>
  <tr>
    <td><a href="sel_attribute_value_lang.asp">[<i>attribute</i>|=<i>value</i>]</a></td>    <td>[lang|=en]</td>    <td>Selects all elements with a lang attribute value starting with "en"</td>
  </tr>
  <tr>
    <td><a href="sel_attr_begin.asp">[<i>attribute</i>^=<i>value</i>]</a></td>    <td>a[href^="https"]</td>    <td>Selects every &lt;a&gt; element whose href attribute value begins with "https"</td>
  </tr>
  <tr>
    <td><a href="sel_attr_end.asp">[<i>attribute</i>&#x24;=<i>value</i>]</a></td>    <td>a[href$=".pdf"]</td>    <td>Selects every &lt;a&gt; element whose href attribute value ends with ".pdf"</td>
  </tr>
  <tr>
    <td><a href="sel_attr_contain.asp">[<i>attribute</i>*=<i>value</i>]</a></td>    <td>a[href*="w3schools"]</td>    <td>Selects every &lt;a&gt; element whose href attribute value contains the substring "w3schools"</td>
  </tr>
  <tr>
    <td><a href="sel_active.asp">:active</a></td>    <td>a:active</td>    <td>Selects the active link</td>
  </tr>
  <tr>
    <td><a href="sel_after.asp">::after</a></td>    <td>p::after</td>    <td>Insert something after the content of each &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_before.asp">::before</a></td>    <td>p::before</td>    <td>Insert something before&nbsp;the content of each &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_checked.asp">:checked</a></td>    <td>input:checked</td>    <td>Selects every checked &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_default.asp">:default</a></td>    <td>input:default</td>    <td>Selects the default &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_disabled.asp">:disabled</a></td>    <td>input:disabled</td>    <td>Selects every disabled &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_empty.asp">:empty</a></td>    <td>p:empty</td>    <td>Selects every &lt;p&gt; element that has no children (including text nodes)</td>
  </tr>
  <tr>
    <td><a href="sel_enabled.asp">:enabled</a></td>    <td>input:enabled</td>    <td>Selects every enabled &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_firstchild.asp">:first-child</a></td>    <td>p:first-child</td>    <td>Selects every &lt;p&gt; element that is the first child of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_firstletter.asp">::first-letter</a></td>    <td>p::first-letter</td>    <td>Selects the first letter of every &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_firstline.asp">::first-line</a></td>    <td>p::first-line</td>    <td>Selects the first line of every &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_first-of-type.asp">:first-of-type</a></td>    <td>p:first-of-type</td>    <td>Selects every &lt;p&gt; element that is the first &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_focus.asp">:focus</a></td>    <td>input:focus</td>    <td>Selects the input element which has focus</td>
  </tr>
  <tr>
    <td><a href="sel_hover.asp">:hover</a></td>    <td>a:hover</td>    <td>Selects links on mouse over</td>
  </tr>
  <tr>
    <td><a href="sel_in-range.asp">:in-range</a></td>    <td>input:in-range</td>    <td>Selects input elements with a value within a specified range</td>
  </tr>
  <tr>
    <td><a href="sel_indeterminate.asp">:indeterminate</a></td>    <td>input:indeterminate</td>    <td>Selects input elements that are in an indeterminate state</td>
  </tr>
  <tr>
    <td><a href="sel_invalid.asp">:invalid</a></td>    <td>input:invalid</td>    <td>Selects all input elements with an invalid value</td>
  </tr>
  <tr>
    <td><a href="sel_lang.asp">:lang(<i>language</i>)</a></td>    <td>p:lang(it)</td>    <td>Selects every &lt;p&gt; element with a lang attribute equal to "it" (Italian)</td>
  </tr>
  <tr>
    <td><a href="sel_last-child.asp">:last-child</a></td>    <td>p:last-child</td>    <td>Selects every &lt;p&gt; element that is the last child of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_last-of-type.asp">:last-of-type</a></td>    <td>p:last-of-type</td>    <td>Selects every &lt;p&gt; element that is the last &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_link.asp">:link</a></td>    <td>a:link</td>    <td>Selects all unvisited links</td>
  </tr>
  <tr>
    <td><a href="sel_not.asp">:not(<i>selector</i>)</a></td>    <td>:not(p)</td>    <td>Selects every element that is not a &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><a href="sel_nth-child.asp">:nth-child(<i>n</i>)</a></td>    <td>p:nth-child(2)</td>    <td>Selects every &lt;p&gt; element that is the second child of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_nth-last-child.asp">:nth-last-child(<i>n</i>)</a></td>    <td>p:nth-last-child(2)</td>    <td>Selects every &lt;p&gt; element that is the second child of its parent, counting from the last child</td>
  </tr>
  <tr>
    <td><a href="sel_nth-last-of-type.asp">:nth-last-of-type(<i>n</i>)</a></td>    <td>p:nth-last-of-type(2)</td>    <td>Selects every &lt;p&gt; element that is the second &lt;p&gt; element of its parent, counting from the last child</td>
  </tr>
  <tr>
    <td><a href="sel_nth-of-type.asp">:nth-of-type(<i>n</i>)</a></td>    <td>p:nth-of-type(2)</td>    <td>Selects every &lt;p&gt; element that is the second &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_only-of-type.asp">:only-of-type</a></td>    <td>p:only-of-type</td>    <td>Selects every &lt;p&gt; element that is the only &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_only-child.asp">:only-child</a></td>    <td>p:only-child</td>    <td>Selects every &lt;p&gt; element that is the only child of its parent</td>
  </tr>
  <tr>
    <td><a href="sel_optional.asp">:optional</a></td>    <td>input:optional</td>    <td>Selects input elements with no "required" attribute</td>
  </tr>
  <tr>
    <td><a href="sel_out-of-range.asp">:out-of-range</a></td>    <td>input:out-of-range</td>    <td>Selects input elements with a value outside a specified range</td>
  </tr>
  <tr>
    <td><a href="sel_placeholder.asp">::placeholder</a></td>    <td>input::placeholder</td>    <td>Selects input elements with placeholder text</td>
  </tr>
  <tr>
    <td><a href="sel_read-only.asp">:read-only</a></td>    <td>input:read-only</td>    <td>Selects input elements with the "readonly" attribute specified</td>
  </tr>
  <tr>
    <td><a href="sel_read-write.asp">:read-write</a></td>    <td>input:read-write</td>    <td>Selects input elements with the "readonly" attribute NOT specified</td>
  </tr>
  <tr>
    <td><a href="sel_required.asp">:required</a></td>    <td>input:required</td>    <td>Selects input elements with the "required" attribute specified</td>
  </tr>
  <tr>
    <td><a href="sel_root.asp">:root</a></td>    <td>:root</td>    <td>Selects the document's root element</td>
  </tr>
  <tr>
    <td><a href="sel_selection.asp">::selection</a></td>    <td>::selection</td>    <td>Selects the portion of an element that is selected by a user</td>
  </tr>
  <tr>
    <td><a href="sel_target.asp">:target</a></td>    <td>#news:target </td>    <td>Selects the current active #news element (clicked on a URL containing that anchor name)</td>
  </tr>
  <tr>
    <td><a href="sel_valid.asp">:valid</a></td>    <td>input:valid</td>    <td>Selects all input elements with a valid value</td>
  </tr>
  <tr>
    <td><a href="sel_visited.asp">:visited</a></td>    <td>a:visited</td>    <td>Selects all visited links</td>
  </tr>
</tbody></table>

<br/>


### [Selector in Lecture][086]

| Selector | HTML | CSS | Link |
|----------|------|-----|------|
| tag | `<li>` | `li {list-style_type: circle;}` | [Selector][087] |
| id | `<p id="p18"> Ulysses </p>` | `#p18 {color: blue;}` | [Selector][088] |
| class | `<li class="bird flying">eagle</li>` | `.bird   { color: blue; }` <br/> `.flying { text-decoration: underline; }` | [Selector][089] |
| Comma separated | `,` | `blockquote,` <br/> `q,` <br/> `.speech {` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `color: red;` <br/>&nbsp;&nbsp;&nbsp;&nbsp; `font-style: italic;` <br/> `}` <br/> `.speech { font-weight: bold; }` | [Selector][090] |
| Specialized | `<li class="insect flying">wasp</li>` | `.insect.flying {` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `text-decoration: underline;` <br/> &nbsp;&nbsp;&nbsp;&nbsp; `font-weight: bold;` <br/>   `}` | [Selector][091] |
| Descendant  | `<section id="intro">Welcome to <a href="#palaceland">PalaceLand</a>` | `#intro a { color: red; }` | [Selector][092] |
| Direct descendant | `<section id="intro">Welcome to <a href="#palaceland">PalaceLand</a>` | `#intro > a { font-size: large; }` | [Selector][093] |



### Tree Presentation - Inheritance

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/0e1bd16d542e4a1085cb8d9b305f8e59/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40833b012fc6dd41f68fa5fd6e3b93e8a8">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c3441bd3d744e14d5d1c0c663d7ad1dc/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-4-2_inheritance_tree.PNG" style="margin: 0.1em;" alt="ags that contain other tags are parents, and the tags inside of them are their children in the following tree representation." title="HTML inheritance structure" width="250">
  </a></div>
</div>

+ CSS property values set on one element will be transferred down the tree to that element's children.
+ Not every property is inherited, but many are.



### CSS Precedence

Rules:

1. __inline > style/css file__: inline css ( html style attribute ) overrides css rules in style tag and css file
2. __specific > less-specific__: a more specific selector takes precedence over a less specific one
3. __later > earlier__: rules that appear later in the code override earlier rules if both have the same specificity.
4. __`!important`__ highest: A css rule with `!important` always takes precedence.


Four categories which define the [specificity level](https://www.w3schools.com/css/css_specificity.asp) of a selector:

1. __Inline styles__ - An inline style is attached directly to the element to be styled. Example: `<h1 style="color: #ffffff;">`.
2. __IDs__ - An ID is a unique identifier for the page elements, such as `#navbar`.
3. __Classes, attributes and pseudo-classes__ - This category includes `.classes`, `[attributes]` and pseudo-classes such as `:hover`, `:focus` etc.
4. __Elements__ and __pseudo-elements__ - This category includes element names and pseudo-elements, such as `h1`, `div`, `:before` and `:after`.

[selector's specificity calculation](https://www.w3.org/TR/selectors-3/#specificity):

+ count the number of ID selectors in the selector (= a)
+ count the number of class selectors, attributes selectors, and pseudo-classes in the selector (= b)
+ count the number of type selectors and pseudo-elements in the selector (= c)
+ ignore the universal selector

  Examples:

  ```ssh
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



## [Properties][071]

| Property | Description | Value Options | Link |
|----------|-------------|---------------|------|
| `color` | text color | `blue`, `lightblue`, `darkblue`, `red`, etc. | |
| `font-size` | size the text of a tag | `px`, `em`, `%`, `vh` | [Common Prty][072] |
| `line-height` | height of the space | `<number>` | [Common Prty][073] |
| `text-align` | alignment | `left`, `center`, `right`, `justify`, `justify-all` | [Common Prty][074] |
| `text-decoration` | the decoration added to text | `underline`, `overline`, `line-through`, `none` | [Common Prty][075] |
| `font-weight` | text bolder (or less bold) | `normal`, `bold`, `bolder`, `lighter`, `<number>` | [Common Prty][076] |
| `font-family` | font for an element | `serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`, etc. | [Common Prty][077] |
| `list-style-type` | list marker, usually positioned to the left of any list item | ul: `disc`, `circle`, `square`, `none`; <br/>ol: `decimal`, `decimal-leading-zero`, `lower-roman`, `upper-roman`, `lower-alpha`, `upper-alpha`, `armenian`, `georgian`, `simp-chinese-formal`, etc. | [List][078] |
| `list-style-position` | how closely it is positioned to the list itself | `inside`, `outside` | [List][079] |
| `list-style-image` | customized little markers on a list | `url("path/fig.png")` | [List][080] |



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



### CSS Website Layout - Example

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.w3schools.com/css/css_website_layout.asp">
    <img src="css-layout.png" style="margin: 0.1em;" alt="There are tons of different layout designs to choose from. However, the structure above, is one of the most common, and we will take a closer look at it in this tutorial." title="A website is often divided into headers, menus, content and a footer" width="400">
  </a></div>
</div>



### Table Properties

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.tallcomponents.com/tallpdf/help/guide/tables?build=net40">
    <img src="https://www.tallcomponents.com/tallpdf5/content/guide/tallpdf/media/table-border-padding-and-margin.png" style="margin: 0.1em;" alt="The extra space outside a border is set by a left, right, top and bottom margin. The extra space inside a border is set by a left, right, top and bottom padding. These attributes are part of the table, row or cell. The following figure makes this clear." title="Padding, Margins and Border Width" width="400">
  </a></div>
  <div><a href="http://learningspot.altervista.org/html-table-tag-attributes/">
    <img src="http://learningspot.altervista.org/wp-content/uploads/2017/07/HTML_cellpadding_cellspacing.png" style="margin: 0.1em;" alt="The size indicated in cellpadding and cellspacing, once set, affects all sides of the cell." title="Table cell padding and spacing" width="345">
  </a></div>
</div>

#### Table Properties

| Property | Applied To | Description | Possible Value | Link |
|----------|------------|-------------|----------------|------|
| `border` | `<table>`, `<th>` `<td>` | sets border-width, border-style and border-color in order | `<width, style, color>`: width = pixel, style = none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset; color = color name or color values, transparent | [Border][062] |
| `border-collapse` | `<table>`, `<th>`, `<td>` | to collapse border or not | separate - default value <br/> collapse - border are collapsed into a single border <br/> initial - sets to default value (separate) | [Collapse][063] |
| `width`; `height` | `<td>` | set the width and height for the rows and columns for your table based on the content in your cells | units of length like pixels, percentage; auto: the browser will calculate and select a width for the specified element (default value) | [Size][064] |
| `text-align` | `<th>`, `<td>` | align the text of and cells left, right or center |  left, right or center; Default: `<th>` - center, `<td>` - left | [Horizontal][065] |
| `vertical-align` | `<th>`, `<td>` | align the text of and cells top, bottom or middle | top, bottom or middle; default: middle | [Vertical][066] |
| `padding` | `<th>`, `<td>` | provide some space between border and content in cell | units of length like px, cm, % - relative to parent container's width | [Padding][067] | 
|border-spacing | `<table>`, `<td>`, `<th>` | space between content in cell and border | units of length like px, cm, % - relative to parent container's width | [Space][068] |
| `border-top`, `border-right`, `border-bottom`, `border-left` | `<th>`, `<td>` | set borders to individual sides | `<width, style, color>` | [Side][069] |


#### Styling with Pseudo Class

| Class | Description | Possible Property/Values | Link |
|-------|-------------|-------------------|------|
| `tr:nth-child(even)`, `tr:nth-child(odd)` | alternating colors for table rows making it easier to differentiate data between rows | `background-color: color;` | [Zebra][083] |
| `tr.hover` | mouse over rows in your table to highlight them in the color specified | `background-color: black;` | [Hover][084] |




### Box Model

<a href="https://www.w3.org/TR/CSS22/box.html"> 
    <img src="https://www.w3.org/TR/CSS22/images/boxdim.png" alt="Each box has a content area (e.g., text, an image, etc.) and optional surrounding padding, border, and margin areas; the size of each area is specified by properties defined below. The following diagram shows how these areas relate and the terminology used to refer to pieces of margin, border, and padding. The margin, border, and padding can be broken down into top, right, bottom, and left segments (e.g., in the diagram, 'LM' for left margin, 'RP' for right padding, 'TB' for top border, etc.)." title="The four areas of the generic CSS box: content, padding, border, and margin." width="350" style="display: block; margin: auto; background-color: white"> <br/>
</a>


<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 20%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>padding</td>
    <td>padding for all sides of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-top</td>
    <td>padding for top side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-right</td>
    <td>padding for right side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-bottom</td>
    <td>padding for bottom side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-left</td>
    <td>padding for left side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border</td>
    <td>the style, width, and color of an element's border</td>
    <td>border-width, border-style (required), border-color</td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-style</td>
    <td>what kind of border to display</td>
    <td>dotted, dashed, solid, double, groove, ridge, inset, outset, none, hidden <br/><br/>Examples: <br/><ul><li>border-style: dotted solid double dashed;</li>  <li>border-style: dotted solid double;</li>, <li>border-style: dotted solid;</li>,  <li>border-style: dotted;</li></ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-width</td>
    <td>the width of the four borders</td>
    <td>px, pt, cm, em, thin, medium, thick</td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-color</td>
    <td>the color of the four borders</td>
    <td>name, Hex, RGB, transparent</td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin</td>
    <td>space around elements, outside of any defined borders</td>
    <td>#px, auto <br/><br/> Example: <br/><ul><li>margin: top right bottom left;</li>  <li>margin: top right bottom</li> <li>margin: top right</li></ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-top</td>
    <td>space on top of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-right</td>
    <td>space on right of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-bottom</td>
    <td>space on bottom of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-left</td>
    <td>space on left of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  </tbody>
</table>



## Display: Block and Inline Elements

### [Display Elements](../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#display-property):


## Display Flow Layout

+ Normal Flow / Flow Layout
  + the way that Block and Inline elements are displayed on a page before any changes are made to their layout
  + essentially a set of things that are all working together and know about each other in your layout

+ Block-level vs. inline
  + Content model:
    + block-level element may contain inline elements and other block-level elements
    + block elements create "larger" structures than inline elements
  + Default formating:
    + block-level elements begin on new lines
    + in-line elements can start anywhere in a line

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements#Elements"> Block-level Element </a></td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements#Elements">Inline Element</a></td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>&lt;address&gt;: Contact information<br/>&lt;article&gt;: Article content<br/>&lt;aside&gt;: Aside content<br/>&lt;blockquote&gt;: Long ("block") quotation<br/>&lt;details&gt;: Disclosure widget<br/>&lt;dialog&gt;: Dialog box<br/>&lt;dd&gt;: Describes a term in a description list<br/>&lt;div&gt;: Document division<br/>&lt;dl&gt;: Description list<br/>&lt;dt&gt;: Description list term<br/>&lt;fieldset&gt;: Field set label<br/>&lt;figcaption&gt;: Figure caption<br/>&lt;figure&gt;: Groups media content with a caption (see &lt;figcaption&gt;)<br/>&lt;footer&gt;: Section or page footer<br/>&lt;form&gt;: Input form<br/>&lt;h1&gt;, &lt;h2&gt;, &lt;h3&gt;, &lt;h4&gt;, &lt;h5&gt;, &lt;h6&gt;: Heading levels 1-6<br/>&lt;header&gt;: Section or page header; &lt;hgroup&gt;: Groups header information<br/>&lt;hr&gt;: Horizontal rule (dividing line)<br/>&lt;li&gt;: List item<br/>&lt;main&gt;: Contains the central content unique to this document<br/>&lt;nav&gt;: Contains navigation links<br/>&lt;ol&gt;: Ordered list<br/>&lt;p&gt;: Paragraph<br/>&lt;pre&gt;: Preformatted text<br/>&lt;section&gt;: Section of a web page<br/>&lt;table&gt;: Table<br/>&lt;ul&gt;: Unordered list</td>
    <td>&lt;a&gt;, &lt;abbr&gt;, &lt;acronym&gt;, &lt;audio&gt;, &lt;b&gt;<br/>&lt;bdi&gt;, &lt;bdo&gt;, &lt;big&gt;, &lt;br&gt;, &lt;button&gt;<br/>&lt;canvas&gt;, &lt;cite&gt;, &lt;code&gt;, &lt;data&gt;, &lt;datalist&gt;<br/>&lt;del&gt;, &lt;dfn&gt;, &lt;em&gt;, &lt;embed&gt;, &lt;i&gt;<br/>&lt;iframe&gt;, &lt;img&gt;, &lt;input&gt;, &lt;ins&gt;, &lt;kbd&gt;<br/>&lt;label&gt;, &lt;map&gt;, &lt;mark&gt;, &lt;meter&gt;, &lt;noscript&gt;<br/>&lt;object&gt;, &lt;output&gt;, &lt;picture&gt;, &lt;progress&gt;, &lt;q&gt;<br/>&lt;ruby&gt;, &lt;s&gt;, &lt;samp&gt;, &lt;script&gt;, &lt;select&gt;<br/>&lt;slot&gt;, &lt;small&gt;, &lt;span&gt;, &lt;strong&gt;, &lt;sub&gt;<br/>&lt;sup&gt;, &lt;svg&gt;, &lt;template&gt;, &lt;textarea&gt;, &lt;time&gt;<br/>&lt;u&gt;, &lt;tt&gt;, &lt;var&gt;, &lt;video&gt;, &lt;wbr&gt;</td>
  </tr>
  </tbody>
</table>


### [Display Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/display#Syntax)

```css
/* <display-outside> values */
display: block;
display: inline;
display: run-in;

/* <display-inside> values */
display: flow;
display: flow-root;
display: table;
display: flex;
display: grid;
display: ruby;

/* <display-outside> plus <display-inside> values */
display: block flow;
display: inline table;
display: flex run-in;

/* <display-listitem> values */
display: list-item;
display: list-item block;
display: list-item inline;
display: list-item flow;
display: list-item flow-root;
display: list-item block flow;
display: list-item block flow-root;
display: flow list-item block;

/* <display-internal> values */
display: table-row-group;
display: table-header-group;
display: table-footer-group;
display: table-row;
display: table-cell;
display: table-column-group;
display: table-column;
display: table-caption;
display: ruby-base;
display: ruby-text;
display: ruby-base-container;
display: ruby-text-container;

/* <display-box> values */
display: contents;
display: none;

/* <display-legacy> values */
display: inline-block;
display: inline-table;
display: inline-flex;
display: inline-grid;
```

+ Categories
  1. `<display-outside>`: specify the element’s outer display type, which is essentially its role in flow layout
  2. `<display-inside>`: specify the element’s inner display type, which defines the type of formatting context that its contents are laid out in (assuming it is a non-replaced element)
  3. `<display-listitem>`: generate a block box for the content and a separate list-item inline box
  4. `<display-internal>`: Some layout models such as table and ruby have a complex internal structure, with several different roles that their children and descendants can fill
  5. `<display-box>`: define whether an element generates display boxes at all
  6. `<display-legacy>`: used a single-keyword syntax for the display property, requiring separate keywords for block-level and inline-level variants of the same layout mode.


### Display Characteristics

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Property</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%"><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#block-level">Block Level</a></td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%"><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#inline-elements">Inline Element</a></td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%"><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#nline-block">Inline-Block</a></td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>Position</td>
    <td><ul> <li> below and left of their block level neighbors </li> </ul></td>
    <td><ul> <li> right of their preceding inline elements </li> <li> cleave to the baseline where they are being placed </li></ul></td>
    <td><ul> <li> cleave to the text baseline </li> </ul></td>
  </tr>
  <tr>
    <td>Width</td>
    <td><ul> <li> expand to fill the width of the parent container by default </li> <li> make width narrower and wrap, but not crop </li> <li>take the width of their parent</li> <li> centering - <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#block">"margin: auto;" </li> </ul></td>
    <td><ul> <li>width of the content of the element, plus any padding</li> <li> no width properties </li> <li> subject to CSS white-space settings </li> <li> centering - <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#inline">"text-align: center;"</a> </li> </ul></td>
    <td><ul> <li> adjusted to make room respect to width properties </li> </ul></td>
  </tr>
  <tr>
    <td>Height</td>
    <td><ul> <li>take on the height of all its children</li> <li> no vertical-align property</li> <li>take the height of their content </li> <li>centering - <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#inline-1">"vertical-align: center;" </a></li> </ul></td>
    <td><ul> <li>no height properties</li> <li> subject to vertical-align property </li> <li>line-height property</li> <li>centering - <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#inline-1">flexbox</a> </li></ul></td>
    <td><ul> <li> adjusted to make room respect to height properties </li> </ul></td>
  </tr>
  <tr>
    <td>Margin</td>
    <td><ul> <li> respect all margin properties</li> </ul></td>
    <td><ul> <li>no top and bottom margin</li> </ul></td>
    <td><ul> <li> adjusted to make room respect to margin-top and margin-bottom </li> </ul></td>
  </tr>
  <tr>
    <td>Padding</td>
    <td><ul> <li>all padding properties</li> </ul></td>
    <td><ul> <li>padding properties, but any padding-top or padding-bottom</li> <li> keep neighbors away horizontally </li></ul></td>
    <td><ul> <li> vertical padding contribute to the calculation of the height of the line it falls on </li> </ul></td>
  </tr>
  </tbody>
</table>


## Positioned Property

<table table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>left, top, right, bottom</td>
    <td><ul> <li>adjust or set the position of an element</li> <li>determine the final location of positioned elements</li></ul></td>
    <td>length-value, percentage, auto</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-left-top-right-and-bottom-properties">Position</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/left">Left</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/top">Top</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/bottom">Bottom</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/right">Right</a></td>
  </tr>
  <tr>
    <td>z-index</td>
    <td><ul> <li>control overlapping - whether or not an element is in front of or behind other sibling positioned elements</li> <li>The higher the number, the more "topmost" or "overlapping" the element will be.</li></ul></td>
    <td>auto, integer</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#-z-index-">Z-Index</a></td>
  </tr>
  <tr>
    <td>float</td>
    <td><ul> <li>place an element on the left or right side of its container, allowing text and inline elements to wrap around it</li> <li>removed from the normal flow of the page, though still remaining a part of the flow</li></ul></td>
    <td>none, left, right, inline-start, inline-end</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/float">Float</a></td>
  </tr>
  <tr>
    <td>clear</td>
    <td><ul> <li>applied to floating and non-floating elements</li></ul></td>
    <td>none, left, right, both, inline-start, inline-end</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/clear">Clear</a></td>
  </tr>
  <tr>
    <td>position</td>
    <td><ul> <li>applied to floating and non-floating elements</li></ul></td>
    <td>none, left, right, both, inline-start, inline-end</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">Position</a></td>
  </tr>
  </tbody>
</table>


### Position Characteristics

<table table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>static</td>
    <td><ul> <li>follow the "flowing text" model of layout </li> <li>influenced by margins, padding</li> <li>block level layout, inline or inline-block</li> <li>default value</li> </ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#static">Static</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html"> Positioning </a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"> MDN </a></td>
  </tr>
  <tr>
    <td>fixed</td>
    <td><ul><li>positioned against the window rectangle (aka the viewport) </li> <li>Best practice: use both a horizontal and a vertical positioning property on every fixed positioned element</li> <li> etermined by the values of top, right, bottom, and left</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#fixed">Fixed</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html"> Positioning </a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"> MDN </a></td>
  </tr>
  <tr>
    <td>relative</td>
    <td><ul><li>exactly like static in that the "flowing text" model of layout is setting the initial position for the element (including margins and display) but move the named edge of the element from its initial position </li> <li>positioned according to the normal flow of the document is positioned relative to its normal position, and then offset relative to itself based on the values of top, right, bottom, and left</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#relative">Relative</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html"> Positioning </a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"> MDN </a></td>
  </tr>
  <tr>
    <td>absolute</td>
    <td><ul><li>taken out of the normal text "flow" that governs elements positioned statically or relatively </li> <li>positioned by the left, top, right, and/or bottom properties </li> <li>relative to the closest positioned ancestor, if there is any; otherwise, it is placed relative to the initial containing block and its final position is determined by the values of top, right, bottom, and left</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#absolute">Absolute</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html"> Positioning </a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"> MDN </a></td>
  </tr>
  <tr>
    <td>sticky</td>
    <td><ul><li>positioned corresponding to the normal flow of the document, and then offset relative to its closest ascending block-level, including table-related elements, according to the values of top, right, bottom, and left</td>
    <td><a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html"> Positioning </a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position"> MDN </a></td>
  </tr>
  </tbody>
</table>


## Sizing Properties

### Global Sizing

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 20%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>height</td>
    <td>Sets the height of an element</td>
  </tr>
  <tr>
    <td>max-height</td>box-sizing
    <td>Sets the maximubox-sizingent</td>
  </tr>
  <tr>
    <td>max-width</td>
    <td>Sets the maximum width of an element</td>
  </tr>
  <tr>
    <td>min-height</td>
    <td>Sets the minimum height of an element</td>
  </tr>
  <tr>
    <td>min-width</td>
    <td>Sets the minimum width of an element</td>
  </tr>
  <tr>
    <td>width</td>
    <td>Sets the width of an element</td>
  </tr>
  </tbody>
</table>


### Box Sizing


<table table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Example</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>content-box</td>
    <td><ul> <li>the default CSS box-sizing behavior</li> <li>including width and height, but not padding, border, or margin</li><li> the dimensions of the element: width = width of the content; height = height of the content</li></ul></td>
    <td><div>box-sizing: content-box;<br/>width: 100%</div><br/><div>box-sizing: content-box;<br/>width: 100%;<br/>border: solid #5B6DCD 10px;</div></td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing">MDN</a>, <a href="/WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-box-model-and-box-sizing">Box-sizing</a></td>
  </tr>
  <tr>
    <td>border-box</td>
    <td><ul><li>telling the browser to account for any border and padding in the values specified for an element's width and height</li><li>including width and height, padding & border, but not margin</li><li> the dimensions of the element: width = border + padding + width of the content, height = border + padding + height of the content</li></ul></td>
    <td><div>box-sizing: content-box;<br/>width: 100%</div><div>box-sizing: content-box;<br/>width: 100%;<br/>border: solid #5B6DCD 10px;</div></td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing">MDN</a>, <a href="/WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-box-model-and-box-sizing">Box-sizing</a></td>
  </tr>
  </tbody>
</table>



## Cropping and scrolling

<table table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>overflow</td>
    <td><ul> <li>specified as one or two keywords chosen from the list of values below</li> <li>two keywords: (overflow-x, overflow-y)</li><li>create a new block formatting context except visible </li><li>if a float intersected with the scrolling element it would forcibly rewrap the content after each scroll step, leading to a slow scrolling experience</li><li>the block-level container must have either a set height (height or max-height) or white-space set to nowrap</li></ul></td>
    <td>visible, hidden, auto, scroll, clip, hidden visible</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow">Overflow</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Lecture</a></td>
  </tr>
  <tr>
    <td>overflow-block</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows a block-level element's block start and block end edge</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-block">Overflow-Block</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Lecture</a></td>
  </tr>
  <tr>
    <td>overflow-inline</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows an inline element's start and end edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-inline">Overflow-Inline</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Lecture</a></td>
  </tr>
  <tr>
    <td>overflow-x</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows a block-level element's left and right edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-x">Overflow-X</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Lecture</a></td>
  </tr>
  <tr>
    <td>overflow-y</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows an inline element's top and bottom edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-y">Overflow-Y</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Lecture</a></td>
  </tr>
  </tbody>
</table>


## The Flexible Box Layout

### Basic Concepts of flexbox

+ Layout and Axes
  + __main axis__:
    + the axis running in the direction the flex items are being laid out in
    + __main start__ and __main end__: the start and end of main axis
  + __cross axis__:
    + the axis running perpendicular to the direction the flex items are being laid out in
    + __cross start__ and __cross end__:  start and end of cross axis
  + __flex container__: set parent element w/ `display: fex`
  + __flex items__: the items being laid out as flexible boxes inside the flex container

+ main axis defined by __flex-direction__
  + row: along the row in the inline direction from left to right
  + row-reverse: along the row in the inline direction from right to left
  + column: from the top of the page to the bottom
  + column-reverse: from the bottom of the page to the top

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox">
      <img src="https://mdn.mozillademos.org/files/15614/Basics1.png" style="margin: 0.1em;" alt="row or row-reverse: main axis will run along the row in the inline direction" title="Inline directon: row or row-reverse" width="250">
      <img src="https://mdn.mozillademos.org/files/15615/Basics2.png" style="margin: 0.1em;" alt="column or column-reverse: main axis will run from the top of the page to the bottom — in the block direction" title="Block direction: column or column-reverse" width="250">
      <img src="https://mdn.mozillademos.org/files/15616/Basics3.png" style="margin: 0.1em;" alt=" flex-direction (main axis) is set to row or row-reverse the cross axis runs down the columns" title="The cross axis runs perpendicular to the main axis" width="250">
      <img src="https://mdn.mozillademos.org/files/15617/Basics4.png" style="margin: 0.1em;" alt="main axis is column or column-reverse then the cross axis runs along the rows" title="main axis is column or column-reverse then the cross axis runs along the rows" width="250">
    </a></div>
  </div>

+ [The flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox#The_flex_container)
  + An area of a document laid out using flexbox
  + set the value of the area's container's display property to `flex` or `inline-flex`
  + flex items: the direct children of that container
  + ways to create a flex container all of the contained flex items
    + Items display in a row (the `flex-direction` property's default is `row`).
    + The items start from the start edge of the main axis.
    + The items do not stretch on the main dimension, but can shrink.
    + The items will stretch to fill the size of the cross axis.
    + The `flex-basis` property is set to `auto`.
    + The `flex-wrap `property is set to `nowrap`.

+ [Multi-line flex containers with flex-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox#The_flex_container)
  + While flexbox is a one dimensional model, it is possible to cause our flex items to wrap onto multiple lines.
  + To cause wrapping behaviour add the property `flex-wrap` with a value of `wrap`.
  + guide to wrap flex items: [Mastering Wrapping of Flex Items](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Mastering_Wrapping_of_Flex_Items)



### Flexbox Property


<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>flex</td>
    <td>specified using one, two, or three values:<ul> <li><strong>One-value syntax:</strong><ul><li>&lt;number&gt;: interpreted as &lt;flex-grow&gt;</li><li>value for width: interpreted as &lt;flex-basis&gt;</li><li>keywords: none, auto, or initial</li></ul></li> <li><strong>Two-value syntax</strong>: the first value, &lt;number&gt;, interpreted as &lt;flex-grow&gt;. The second value must be one of: <ul><li>&lt;number&gt;: interpreted as &lt;flex-shrink&gt;</li><li>value for width: interpreted as &lt;flex-basis&gt;</li></ul></li><li><strong>Three-value syntax</strong> (order): <ol><li>&lt;number&gt; for &lt;flex-grow&gt;</li><li>&lt;number&gt; for &lt;flex-shrink&gt;</li><li>value for width: interpreted as &lt;flex-basis&gt;</li></ol></li></ul></td>
    <td>init, auto, none, &lt;flex-grow&gt;, &lt;flex-shrink&gt;, &lt;flex-basis&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-minimum">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-direction</td>
    <td>set how flex items placed in the flex container defining the main axis and the direction (normal or reversed)</td>
    <td>row, row-reverse, column, column-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-wrap</td>
    <td>set whether flex items are forced onto one line or can wrap onto multiple lines</td>
    <td>nowrap, wrap, wrap-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-flow</td>
    <td>a shorthand property for <strong>flex-direction</strong> and <strong>flex-wrap</strong> properties</td>
    <td>nowrap, wrap, wrap-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-flow">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-basis</td>
    <td><ul><li>set the initial main size of a flex item</li><li>content: automatic sizing, based on the flex item’s content</li></ul></td>
    <td>&lt;width&gt;, content</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-grow</td>
    <td><ul><li>set how much of the remaining space in the flex container should be assigned to that item (the flex grow factor)</li><li>remaining space: the size of the flex container minus the size of all flex items together</li><li>sibling items: <ul><li>all items with the same share of remaining space with the same grow factor</li><li>distributed according tot he ratio defined by the different flex grow factors</li></ul></ul></td>
    <td>&lt;number&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-shrink</td>
    <td>set the flex shrink factor of a flex item</td>
    <td>&lt;number&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  </tbody>
</table>


## The Flexible Box Layout

### Basic Concepts of flexbox

+ Layout and Axes
  + __main axis__:
    + the axis running in the direction the flex items are being laid out in
    + __main start__ and __main end__: the start and end of main axis
  + __cross axis__:
    + the axis running perpendicular to the direction the flex items are being laid out in
    + __cross start__ and __cross end__:  start and end of cross axis
  + __flex container__: set parent element w/ `display: fex`
  + __flex items__: the items being laid out as flexible boxes inside the flex container

+ main axis defined by __flex-direction__
  + row: along the row in the inline direction from left to right
  + row-reverse: along the row in the inline direction from right to left
  + column: from the top of the page to the bottom
  + column-reverse: from the bottom of the page to the top

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox">
      <img src="https://mdn.mozillademos.org/files/15614/Basics1.png" style="margin: 0.1em;" alt="row or row-reverse: main axis will run along the row in the inline direction" title="Inline directon: row or row-reverse" width="250">
      <img src="https://mdn.mozillademos.org/files/15615/Basics2.png" style="margin: 0.1em;" alt="column or column-reverse: main axis will run from the top of the page to the bottom — in the block direction" title="Block direction: column or column-reverse" width="250">
      <img src="https://mdn.mozillademos.org/files/15616/Basics3.png" style="margin: 0.1em;" alt=" flex-direction (main axis) is set to row or row-reverse the cross axis runs down the columns" title="The cross axis runs perpendicular to the main axis" width="250">
      <img src="https://mdn.mozillademos.org/files/15617/Basics4.png" style="margin: 0.1em;" alt="main axis is column or column-reverse then the cross axis runs along the rows" title="main axis is column or column-reverse then the cross axis runs along the rows" width="250">
    </a></div>
  </div>

+ [The flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox#The_flex_container)
  + An area of a document laid out using flexbox
  + set the value of the area's container's display property to `flex` or `inline-flex`
  + flex items: the direct children of that container
  + ways to create a flex container all of the contained flex items
    + Items display in a row (the `flex-direction` property's default is `row`).
    + The items start from the start edge of the main axis.
    + The items do not stretch on the main dimension, but can shrink.
    + The items will stretch to fill the size of the cross axis.
    + The `flex-basis` property is set to `auto`.
    + The `flex-wrap `property is set to `nowrap`.

+ [Multi-line flex containers with flex-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox#The_flex_container)
  + While flexbox is a one dimensional model, it is possible to cause our flex items to wrap onto multiple lines.
  + To cause wrapping behaviour add the property `flex-wrap` with a value of `wrap`.
  + guide to wrap flex items: [Mastering Wrapping of Flex Items](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Mastering_Wrapping_of_Flex_Items)



### Flexbox Property


<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>flex</td>
    <td>specified using one, two, or three values:<ul> <li><strong>One-value syntax:</strong><ul><li>&lt;number&gt;: interpreted as &lt;flex-grow&gt;</li><li>value for width: interpreted as &lt;flex-basis&gt;</li><li>keywords: none, auto, or initial</li></ul></li> <li><strong>Two-value syntax</strong>: the first value, &lt;number&gt;, interpreted as &lt;flex-grow&gt;. The second value must be one of: <ul><li>&lt;number&gt;: interpreted as &lt;flex-shrink&gt;</li><li>value for width: interpreted as &lt;flex-basis&gt;</li></ul></li><li><strong>Three-value syntax</strong> (order): <ol><li>&lt;number&gt; for &lt;flex-grow&gt;</li><li>&lt;number&gt; for &lt;flex-shrink&gt;</li><li>value for width: interpreted as &lt;flex-basis&gt;</li></ol></li></ul></td>
    <td>init, auto, none, &lt;flex-grow&gt;, &lt;flex-shrink&gt;, &lt;flex-basis&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-minimum">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-direction</td>
    <td>set how flex items placed in the flex container defining the main axis and the direction (normal or reversed)</td>
    <td>row, row-reverse, column, column-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-wrap</td>
    <td>set whether flex items are forced onto one line or can wrap onto multiple lines</td>
    <td>nowrap, wrap, wrap-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-flow</td>
    <td>a shorthand property for <strong>flex-direction</strong> and <strong>flex-wrap</strong> properties</td>
    <td>nowrap, wrap, wrap-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-flow">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-basis</td>
    <td><ul><li>set the initial main size of a flex item</li><li>content: automatic sizing, based on the flex item’s content</li></ul></td>
    <td>&lt;width&gt;, content</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-grow</td>
    <td><ul><li>set how much of the remaining space in the flex container should be assigned to that item (the flex grow factor)</li><li>remaining space: the size of the flex container minus the size of all flex items together</li><li>sibling items: <ul><li>all items with the same share of remaining space with the same grow factor</li><li>distributed according tot he ratio defined by the different flex grow factors</li></ul></ul></td>
    <td>&lt;number&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  <tr>
    <td>flex-shrink</td>
    <td>set the flex shrink factor of a flex item</td>
    <td>&lt;number&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink">MDN</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  </tbody>
</table>







-------------------------------------------
<!--
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
[062]: https://developer.mozilla.org/en-US/docs/Web/CSS/top
[063]: https://developer.mozilla.org/en-US/docs/Web/CSS/right
[064]: https://developer.mozilla.org/en-US/docs/Web/CSS/bottom
[065]: https://developer.mozilla.org/en-US/docs/Web/CSS/float
[066]: https://developer.mozilla.org/en-US/docs/Web/CSS/position
[067]: https://developer.mozilla.org/en-US/docs/Web/CSS/clear
[068]: https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements#Elements
[069]: https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements#Elements
[070]: https://github.com/hmchen47/Programming/blob/css/WebDev/Frontend-W3C/4-CSSBasics/05-DesignWeb.md#typography
[071]: https://www.w3.org/Style/CSS/all-properties.en.html#list
[072]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#font-size
[073]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#line-height
[074]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#text-align
[075]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#text-decoration-underline
[076]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#font-weight-bold
[077]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#font-family
[078]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#list-style-type
[079]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#list-style-position
[080]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#list-style-image
[081]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#px
[082]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#em
[083]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#rem
[084]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#
[085]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#vh--vw
[086]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#selectors
[087]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#tag-selector
[088]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#id-selector
[089]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#class-selector
[090]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#comma-separated-selectors
[091]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#specialized-selectors
[092]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#descendant-selectors
[093]: ../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#direct-descendant-selectors---
