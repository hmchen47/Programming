# Cascading Style Sheet (CSS)


## General Information

### CSS design principles(CSS 2.2)

+ [CSS design principles (CSS2.2)](https://www.w3.org/TR/CSS22/intro.html#design-principles)
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


### Effective Use of Style Sheets

+ [Generalized Style](https://www.nngroup.com/articles/effective-use-of-style-sheets/)
  + single style sheet for all of the pages on your site
  + linked style sheets
  + centralized design
  + active evangelism program
  + plenty of examples
  + page authors should be allowed to create additional embedded styles for their own pages

+ [Implementation advice](https://www.nngroup.com/articles/effective-use-of-style-sheets/)
  + continue to work when style sheets are disabled
  + Do not use more than two fonts
  + Do not use absolute font sizes
  + Do not use the !important attribute
  + use the same CLASS names for the same concept in all of the style sheets


### CSS Best Practice

+ [Executive summary](/WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#executive-summary)
  + Logical source order: accessibility, mobile optimization, device adaptability, and long-term maintainability.
  + Liquid layouts and relativity: Use smart relative sizing
  + Media queries: get font size adaptation free by using `em`s
  + Prevent zombie code: Delete it before it does, and ruins your layout
  + Test in multiple browsers: Your favorite browser is not always right.
  + Don't use proprietary features! Don't rely on the latest -WebKit- invention.
  + Turn off CSS: A well-coded page will be understandable without it.

+ [Foundations](/WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#foundations)
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

+ [Testing]/WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#testing
  + Test without CSS: turn off CSS, and if the page makes no sense, fix your markup.
  + Test in multiple environments:
    + Resize the window
    + Zoom the text
    + Try a mobile browser
    + Navigate by keyboard
  + Test in multiple browsers: remember that just testing in Chrome does not work for everyone! ;)

+ [Adaptability](/WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#adaptability)
  + Media queries: set media query breakpoints in `em` or `ch`, not always in `px`.
  + Liquid layouts and relativity: what is your sizing based on?
    + Containing block size? → Use percents.
    + Viewport size? → Use viewport units: `vw`, `vh`, `vmin`, `vmax`
    + Font height? → Use `em` or `rem`.
    + Font pitch? → Use `em` or `ch`.
    + Content size? → Use auto or min-content/max-content.
    + Combination of the above? → Use the appropriate layout formulas: `flex`, `min-width`, `max-width`, etc.

+ [Defensive Coding](/WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#defensive-coding)
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


### Tools

+ [CSS Validator](https://jigsaw.w3.org/css-validator/)

+ [CSS Zen Garden](http://www.csszengarden.com/)

+ [WC3 complete list of CSS properties](https://www.w3.org/Style/CSS/all-properties.en.html)

+ [Web Accessibility Evaluations Tools List](https://www.w3.org/WAI/ER/tools/)


### Usage

+ &lt;style&gt;: to place CSS directly into an HTML document within &lt;head&gt; and &lt;/head&gt;

  ```html
  <head>
    <meta charset="UTF-8">
    <title>Style and link tags</title>
    <style>
      /* CSS will go in this area */
    </style>
  </head>
  ```

+ &lt;link&gt;:
  + the better practice
  + easily be re-used between your different `.html` pages
  + put your CSS into a separate file
  + must appear in the `<head>` section
  + usually kept in a directory named css

  ```html
  <head>
    <meta charset="UTF-8">
    <title>Style and link tags</title>
    <link rel="stylesheet" href="css/my_styles.css">
  </head>
  ```


### CSS Syntax

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div>
  <a href="https://tinyurl.com/yc944w7n">
    <img src="https://tinyurl.com/y4o4ah8y" style="margin: 0.1em;" alt="A CSS rule is broken into two parts: the selector and the property" title="css anatomy" width="250">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/989b2e8ecef6fec3fcc6fd02a5baed58/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-3-1_property_anatomy.PNG" style="margin: 0.1em;" alt="This is what tells the browser how to style the HTML tag that has been selected. This can be as many lines of code as you choose, each of which has two parts- the property and the value you want that property to be." title="property anatomy" width="250">
  </a>
  <a href="https://www.w3schools.com/css/css_syntax.asp">
    <img src="https://www.w3schools.com/css/selector.gif" style="margin: 0.1em;" alt="The selector points to the HTML element you want to style. The declaration block contains one or more declarations separated by semicolons. Each declaration includes a CSS property name and a value, separated by a colon. A CSS declaration always ends with a semicolon, and declaration blocks are surrounded by curly braces." title="CSS rule-set consists of a selector and a declaration block" width="300">
  </a>
  </div>
</div>


+ [Selector](../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#constructing-your-css-rules)
  + tell the browser what HTML tags this rule applies to
  + types: tag, class & id
  + attribute selectors: Classes and IDs
  + multiple HTML elements with similar style: `p, ul, ol {color: blue; }`

+ [Property](../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#constructing-your-css-rules)
  + tell the browser how to style the HTML tag that has been selected
  + as many lines of code as you choose
  + each of which has two parts- the property and the value you want that property to be
  + with its own collection of possible values
  + [complete list of latest CSS properties](https://www.w3.org/Style/CSS/all-properties#list) at the W3C


### Comment

+ Comments
  + begin with `/*` and must end with `*/`
  + able to span several lines
  + not nested

  ```css
  p {
    font-size: 8px; /* client insists small text makes them more 'professional'. */

    /* none of the stuff below is working. I don't know why.
    margin-top: 5%;
    margin-bottom:6%;
    */
  }
  ```

### Debugging

+ [Programming languages](../WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#debugging)
  + Javascript: procedure programming
  + HTML and CSS: declarative

+ Every browser is a bit different, but most of them have ways to examine the various elements and their properties.

+ [Box Model](../WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#debugging-with-the-box-model)

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/37f15009345846f391d7ac4d5bf06520/854f4a689894455ca4f375f15d0cbc42/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%407031c507bfe94604a6a98013af262725">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/063b584da882baac3e39e088c4c9dc80/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/Screen_Shot_2016-03-08_at_8.19.27_PM.png" style="margin: 0.1em;" alt="image of a CSS Box Model" title="image of a CSS Box Model" width=250>
    </a></div>
  </div>

  + the centered blue box corresponds to the size of the inspected element: width is 536 pixels and height is 118 pixels
  + padding is only defined by padding-left which value is 40 pixels
  + there is a border of 5 pixels on each side
  + margin-left and margin-right are undefined (default value is 0 pixel)
  + margin-top and margin-bottom are equal to 16 pixels

+ [CSS Precedence](../WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#4-4-debugging-css-precedence)
  + "Styles" and "Computed" are helpful in sorting out where a particular style setting is coming from
  + a sequence of the panels under "Style" that helps understand just where a particular CSS rule is coming from
  + from top, rules applied specifically to the currently active element
  + overridden rule shown as striked out ones
  + default ruke: grayed out tules

+ [Image Size](../WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#debugging-image-size)
  + Any style setting for the img width will take precedence over the attribute setting.
  + special case the smaller pictures and use a larger width by default

+ [Computed tab](../WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#computed-tab)
  + The styles panel doesn't tell us a lot about the actually font-size in absolute terms. 
  + The "Computed" tab contains the values of all the CSS properties that apply to the current element.
  + click on the triangle to expand the details on font-size, which makes a little more clear what's going on
  + the em unit is relative measurement, depending on the current font-size


### Accessibility

+ [WAI resources](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#wai-resources)

### Internationalization

+ [Internationalization and CSS](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#internationalization-and-css-use-cases)

+ [Internationalization Resoources](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#internationalization-resources)


## CSS Values and Units

### CSS Value Types & Functions

+ [Textual data types](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Textual_data_types)
  + [&lt;custome-ident&gt](https://developer.mozilla.org/en-US/docs/Web/CSS/custom-ident)
    + an arbitrary user-defined string used as an identifier
    + case-sensitive
    + characters: alphabetical character (-Z, a-z); decimal digit (0-9); hyphen (-); underscore (_); escape character (\); Unicode character (\ + 1-6 hexadecimal digits)
  + Pre-defined keywords as an &lt;ident&gt;
    + text values defined by the specification for that property
    + e.g., float: `left | right | none | inline-start | inline-end`
    + CSS-wide property values: `initial`, `inherit`, and `unset`
      + initial: the value specified as the property’s initial value
      + inherit: the computed value of the property on the element’s parent
      + unset: either inherit or initial, depending on whether the property is inherited or not
  + [&lt;string&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/string)
    + a sequence of characters
    + composed of any number of Unicode characters surrounded by either double (") or single (') quotes
    + Unicode points in hexadecimal: `\22` = double quote; `\27` = single quote; `\A9` = copyright symbol
  + [&lt;url&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/url)
    + a pointer to a resource
    + specified using the url() functional notation
    + e.g., `url("http://mysite.example.com/mycursor.png")`, `url('http://mysite.example.com/mycursor.png')` or `url(http://mysite.example.com/mycursor.png)`

+ [Numeric data types](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Numeric_data_types)
  + [&lt;integer&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/integer)
    + a special type of &lt;number&gt; that represents a whole number, whether positive or negative
    + consists of one or several decimal digits, 0 through 9 inclusive, optionally preceded by a single + or - sign
    + no unit associated with integers
  + [&lt;number&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/number)
    + a number, being either an integer or a number with a fractional component
    + maybe preceded by a + or - symbol
  + [&lt;dimension&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/dimension)
    + a &lt;number&gt; with a unit attached to it
    + [&lt;length&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/length):Distance units
    + [&lt;angle&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/angle): an angle value expressed in degrees, gradians, radians, or turns
    + [&lt;time&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/time): a time value expressed in seconds or milliseconds
    + [&lt;frequency&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/frequency): a frequency dimension, such as the pitch of a speaking voice
    + [&lt;resolution&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/resolution): used for describing resolutions in media queries, denote the pixel density of an output device
  + [&lt;Percentag&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Percentages)
    + a fraction of some other value
    + used to define a size as relative to an element's parent object
    + consist of a &lt;number&gt; followed by the percentage sign (%)
    + may be preceded by a single + or - sign, although negative values are not valid for all properties

+ [Mixing percentages and dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Mixing_percentages_and_dimensions)
  + [&lt;frequency-percentage&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/frequency-percentage): a value that can be either a &lt;frequency&gt; or a &lt;percentage&gt; 
  + [&lt;angle-percentage&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/angle-percentage): a value that can be either a &lt;angle&gt; or a &lt;percentage&gt;
  + [&lt;time-percentage&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/time-percentage): a value that can be either a &lt;time&gt; or a &lt;percentage&gt;

+ [Special data types](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Special_data_types_(defined_in_other_specs))
  + [&lt;color&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/color)
    + specify the color of an element feature
    + a color in the sRGB color space
    + may include an alpha-channel transparency value
    + ways to define:
      + keyword (e.g., blue or transparent)
      + RGB cubic-coordinate system (via the #-hexadecimal or the rgb() and rgba() functional notations)
      + HSL cylindrical-coordinate system (via the hsl() and hsla() functional notations)
    + [Color Name & sRGB Values](HTML-Color.md)
  + [&lt;image&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/image)
    + two-dimensional image
    + two kinds of images
      + plain images, referenced with a &lt;url&gt;
      + dynamically-generated images, generated with &lt;gradient&gt; or element()
    + handle the following kinds of images
      + Images with intrinsic dimensions (a natural size), e.g., JPEG, PNG
      + Images with multiple intrinsic dimensions, existing in multiple versions inside a single file, like some .ico formats
      + Images with no intrinsic dimensions but with an intrinsic aspect ratio between its width and height, e.g., SVG
      + Images with neither intrinsic dimensions, nor an intrinsic aspect ratio, e.g., CSS gradient
  + [&lt;position&gt;](https://developer.mozilla.org/en-US/docs/Web/CSS/position_value)
    + a two-dimensional coordinate used to set a location relative to an element box
    + used in the `background-position` property
    + specified with one or two keywords, with optional offsets
    + keyword values: `center`, `top`, `right`, `bottom`, and `left`

    <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
      <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position_value" ismap target="_blank">
        <img src="https://mdn.mozillademos.org/files/12215/position_type.png" style="margin: 0.1em;" alt="Syntax of position property" title="Syntax of position property" width=350>
      </a>
    </div>


+ [Functional notation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Functional_notation)
  + [calc() CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/calc)
    + perform calculations when specifying CSS property values
    + used anywhere a &lt;length&gt;, &lt;frequency&gt;, &lt;angle&gt;, &lt;time&gt;, &lt;percentage&gt;, &lt;number&gt;, or &lt;integer&gt;
    + function takes a single expression as its parameter, with the expression's result used as the value
    + operators used: +, -, * , /
    + e.g., `width: calc(100% - 80px);`
    + [overuse makes page slow](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#calc-)
    + used for sizing flexbox items nor always as desired, in particular along the cross axis
  + [min()](https://developer.mozilla.org/en-US/docs/Web/CSS/min):
    + set the smallest (most negative) value from a list of comma-separated expressions as the value of a CSS property value
    + used anywhere a &lt;length&gt;, &lt;frequency&gt;, &lt;angle&gt;, &lt;time&gt;, &lt;percentage&gt;,&lt;number&gt;, or &lt;integer&gt;
    + e.g., `width: min(10vw, 4em, 80px);`
  + [max()](https://developer.mozilla.org/en-US/docs/Web/CSS/max)
    + set the largest (most positive) value from a list of comma-separated expressions as the value of a CSS property value
    + used anywhere a &lt;length&gt;, &lt;frequency&gt;, &lt;angle&gt;, &lt;time&gt;, &lt;percentage&gt;,&lt;number&gt;, or &lt;integer&gt;
    + e.g., `width: max(10vw, 4em, 80px);`
  + [clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp)
    + clamp a value between an upper and lower bound
    + enable selecting a middle value within a range of values between a defined minimum and maximum
    + three parameters: a minimum value, a preferred value, and a maximum allowed value
    + used anywhere a &lt;length&gt;, &lt;frequency&gt;, &lt;angle&gt;, &lt;time&gt;, &lt;percentage&gt;, &lt;number&gt;, or &lt;integer&gt;
    + e.g., `width: clamp(10px, 4em, 80px);`
  + toggle(): ?
  + [attr()](https://developer.mozilla.org/en-US/docs/Web/CSS/attr)
    + used to retrieve the value of an attribute of the selected element and use it in the stylesheet
    + used on pseudo-elements, in which case the value of the attribute on the pseudo-element's originating element is returned
    + e.g., Simple usage: `attr(data-count);`, With type: `attr(src url);`, With fallback: `attr(data-count number, 0);`



### Relative Length

<br/>
<table  table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=60%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Dimensions">Relative Length Units</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 5%;">Unit</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 40%;">Related to</th>
  </tr>
  </thead>
  <tbody>
    <tr><td><code>em</code></td><td>Font size of the element.</td></tr>
  <tr><td><code>ex</code></td><td>x-height of the element's font.</td></tr>
  <tr><td><code>cap</code></td><td>Cap height (the nominal height of capital letters) of the element's font.</td></tr>
  <tr><td><code>ch</code></td><td>Average character advance of a narrow glyph in the element’s font, as represented by the “0” (ZERO, U+0030) glyph.</td></tr>
  <tr><td><code>ic</code></td><td>Average character advance of a full width glyph in the element’s font, as represented by the “水” (CJK water ideograph, U+6C34) glyph.</td></tr>
  <tr><td><code>rem</code></td><td>Font size of the root element.</td></tr>
  <tr><td><code>lh</code></td><td>Line height of the element.</td></tr>
  <tr><td><code>rlh</code></td><td>Line height of the root element.</td></tr>
  <tr><td><code>vw</code></td><td>1% of viewport's width.</td></tr>
  <tr><td><code>vh</code></td><td>1% of viewport's height.</td></tr>
  <tr><td><code>vi</code></td><td>1% of viewport's size in the root element's inline axis.</td></tr>
  <tr><td><code>vb</code></td><td>1% of viewport's size in the root element's block axis.</td></tr>
  <tr><td><code>vmin</code></td><td>1% of viewport's smaller dimension.</td></tr>
  <tr><td><code>vmax</code></td><td>1% of viewport's larger dimension.</td></tr>
 </tbody>
</table><br/>


### Absolute Length

<table  table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=60%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Dimensions">Absolute Length Units</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 5%;">Unit</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">Name</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 10%;">Equivalent to</th>
  </tr>
  </thead>
 <tbody>
  <tr> <td><code>cm</code></td> <td>Centimeters</td> <td>1cm = 96px/2.54</td></tr>
  <tr> <td><code>mm</code></td> <td>Millimeters</td> <td>1mm = 1/10th of 1cm</td></tr>
  <tr> <td><code>Q</code></td> <td>Quarter-millimeters</td> <td>1Q = 1/40th of 1cm</td></tr>
  <tr> <td><code>in</code></td> <td>Inches</td> <td>1in = 2.54cm = 96px</td></tr>
  <tr> <td><code>pc</code></td> <td>Picas</td> <td>1pc = 1/16th of 1in</td></tr>
  <tr> <td><code>pt</code></td> <td>Points</td> <td>1pt = 1/72th of 1in</td></tr>
  <tr><td><code>px</code></td><td>Pixels</td><td>1px = 1/96th of 1in</td></tr>
 </tbody>
</table><br/>



## Selectors

### Definition of Selectors

+ CSS rule is made up of two parts: the selector and the declaration

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="http://gottheknack.com/a_htmlCss/weeks/week8/cssRuleStructure/cssRuleStructure.html">
      <img src="http://gottheknack.com/a_htmlCss/weeks/week8/cssRuleStructure/images/ruleParts.gif" style="margin: 0.1em;" alt="text" title="caption" width=350>
    </a></div>
  </div>

+ Selectors
  + tag selecctor
    + consist solely of a single tag (without punctuation or spacing) will be applied to any matching tag on the page
    + e.g., `li { list-style-type: circle; }`
  + id selector
    + applied to an HTML tag to uniquely identify the element
    + the value for any given id attribute can only appear once in a document
    + no spaces, nor most punctuation, nor begin with numbers
    + e.g., declartion: `#p19 { color: green; }`; use: `<p id="p19">Madam, you have spoken truly.</p>`
  + Class selector
    + similar to the id, but shared by multiple tags
    + assigned to a tag by simply separating them with spaces
    + simply a period (.) followed by the class name itself
    + e.g., declaration: `.insect { color: green; }` & `.flying { text-decoration: underline; }`; use: `<li class="insect flying">moth</li>`

+ Combining selectors
  + comma separated selectors: `blockquote, q, .speech {color: red; font-style: italic;}`
  + specialized selectors: 
    + two selectors of different types (like tag and class) appear next to each other with no spacing separating them
    + e.g., `blockquote.speech {font-color: green;}` -> only apply to those blockquotes that also have the speech class
  + descant selectors:
    + separate the tag, identifier, or class selectors by a space
    + e.g., `#intro a { color: red; }` -> the selector will match to any &lt;a&gt; tag that is a descendant of #intro
  + direct descendant selectors ( &gt; )
    + only to the direct children
    + Use it between selectors to limit the application to the direct children of the parent.
    + e.g., `#intro > a { font-size: large; }`
  + everything selector ( * )
    + used to match any tag
    + e.g., `body > * { margin-left: 10px; } /* all the _direct_ children of the body receive the margin */`

+ [!important](../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#-important)
  + take precedence over all others
  + not recommended
  + fix conflict directly, rather than using !important
  + e.g., `p { color: orange !important; }`


### List of CSS Selectors

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em; color: darkblue; font-weight: bold;"><a href="https://www.w3schools.com/cssref/css_selectors.asp">CSS Selectors</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%">Selector</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%">Example</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%">Example description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td><strong>.<i>class</i></strong></td><td>.intro</td><td>Selects all elements with class="intro"</td>
  </tr>
  <tr>
    <td><strong>#<i>id</i></strong></td><td>#firstname</td><td>Selects the element with id="firstname"</td>
  </tr>  
  <tr>
    <td><strong>*</strong></td><td>*</td><td>Selects all elements</td>
  </tr>
  <tr>
    <td><strong><i>element</i></strong></td><td>p</td><td>Selects all &lt;p&gt; elements</td>
  </tr>
  <tr>
    <td><strong><i>element,element</i></strong></td><td>div, p</td><td>Selects all &lt;div&gt; elements and all &lt;p&gt; elements</td>
  </tr>
  <tr>
    <td><strong><i>element</i> <i>element</i></strong></td><td>div p</td><td>Selects all &lt;p&gt; elements inside &lt;div&gt; elements</td>
  </tr>
  <tr>
    <td><strong><i>element</i>&gt;<i>element</i></strong></td><td>div &gt; p</td><td>Selects all &lt;p&gt; elements where the parent is a &lt;div&gt; element</td>
  </tr>
  <tr>
    <td><strong><i>element</i>+<i>element</i></strong></td><td>div + p</td><td>Selects all &lt;p&gt; elements that are placed immediately after &lt;div&gt; elements</td>
  </tr>
  <tr>
    <td><strong><i>element1</i>~<i>element2</i></strong></td><td>p ~ ul</td><td>Selects every &lt;ul&gt; element that are preceded by a &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><strong>[<i>attribute</i>]</strong></td><td>[target]</td><td>Selects all elements with a target attribute</td>
  </tr>
  <tr>
    <td><strong>[<i>attribute</i>=<i>value</i>]</strong></td><td>[target=_blank]</td><td>Selects all elements with target="_blank"</td>
  </tr>
  <tr>
    <td><strong>[<i>attribute</i>~=<i>value</i>]</strong></td><td>[title~=flower]</td><td>Selects all elements with a title attribute containing the word "flower"</td>
  </tr>
  <tr>
    <td><strong>[<i>attribute</i>|=<i>value</i>]</strong></td><td>[lang|=en]</td><td>Selects all elements with a lang attribute value starting with "en"</td>
  </tr>
  <tr>
    <td><strong>[<i>attribute</i>^=<i>value</i>]</strong></td><td>a[href^="https"]</td><td>Selects every &lt;a&gt; element whose href attribute value begins with "https"</td>
  </tr>
  <tr>  
    <td><strong>[<i>attribute</i>&#x24;=<i>value</i>]</strong></td><td>a[href$=".pdf"]</td><td>Selects every &lt;a&gt; element whose href attribute value ends with ".pdf"</td>
  </tr>
  <tr>
    <td><strong>[<i>attribute</i>*=<i>value</i>]</strong></td><td>a[href*="w3schools"]</td><td>Selects every &lt;a&gt; element whose href attribute value contains the substring "w3schools"</td>
  </tr>
  <tr>
    <td><strong>:active</strong></td><td>a:active</td><td>Selects the active link</td>
  </tr>
  <tr>
    <td><strong>::after</strong></td><td>p::after</td><td>Insert something after the content of each &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><strong>::before</strong></td><td>p::before</td><td>Insert something before&nbsp;the content of each &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><strong>:checked</strong></td><td>input:checked</td><td>Selects every checked &lt;input&gt; element</td>
  <tr>
  <tr>
    <td><strong>:default</strong></td><td>input:default</td><td>Selects the default &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><strong>:disabled</strong></td><td>input:disabled</td><td>Selects every disabled &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><strong>:empty</strong></td><td>p:empty</td><td>Selects every &lt;p&gt; element that has no children (including text nodes)</td>
  </tr>
  <tr>
    <td><strong>:enabled</strong></td><td>input:enabled</td><td>Selects every enabled &lt;input&gt; element</td>
  </tr>
  <tr>
    <td><strong>:first-child</strong></td><td>p:first-child</td><td>Selects every &lt;p&gt; element that is the first child of its parent</td>
  </tr>
  <tr>
    <td><strong>::first-letter</strong></td><td>p::first-letter</td><td>Selects the first letter of every &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><strong>::first-line</strong></td><td>p::first-line</td><td>Selects the first line of every &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><strong>:first-of-type</strong></td><td>p:first-of-type</td><td>Selects every &lt;p&gt; element that is the first &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><strong>:focus</strong></td><td>input:focus</td><td>Selects the input element which has focus</td>
  </tr>
  <tr>
    <td><strong>:hover</strong></td><td>a:hover</td><td>Selects links on mouse over</td>
  </tr>
  <tr>
    <td><strong>:in-range</strong></td><td>input:in-range</td><td>Selects input elements with a value within a specified range</td>
  </tr>
  <tr>
    <td><strong>:indeterminate</strong></td><td>input:indeterminate</td><td>Selects input elements that are in an indeterminate state</td>
  </tr>
  <tr>
    <td><strong>:invalid</strong></td><td>input:invalid</td><td>Selects all input elements with an invalid value</td>
  </tr>
  <tr>
    <td><strong>:lang(<i>language</i>)</strong></td><td>p:lang(it)</td><td>Selects every &lt;p&gt; element with a lang attribute equal to "it" (Italian)</td>
  </tr>
  <tr>
    <td><strong>:last-child</strong></td><td>p:last-child</td><td>Selects every &lt;p&gt; element that is the last child of its parent</td>
  </tr>
  <tr>
    <td><strong>:last-of-type</strong></td><td>p:last-of-type</td><td>Selects every &lt;p&gt; element that is the last &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><strong>:link</strong></td><td>a:link</td><td>Selects all unvisited links</td>
  </tr>
  <tr>
    <td><strong>:not(<i>selector</i>)</strong></td><td>:not(p)</td><td>Selects every element that is not a &lt;p&gt; element</td>
  </tr>
  <tr>
    <td><strong>:nth-child(<i>n</i>)</strong></td><td>p:nth-child(2)</td><td>Selects every &lt;p&gt; element that is the second child of its parent</td>
  </tr>
  <tr>
    <td><strong>:nth-last-child(<i>n</i>)</strong></td><td>p:nth-last-child(2)</td><td>Selects every &lt;p&gt; element that is the second child of its parent, counting from the last child</td>
  </tr>
  <tr>
    <td><strong>:nth-last-of-type(<i>n</i>)</strong></td><td>p:nth-last-of-type(2)</td><td>Selects every &lt;p&gt; element that is the second &lt;p&gt; element of its parent, counting from the last child</td>
  </tr>
  <tr>
    <td><strong>:nth-of-type(<i>n</i>)</strong></td><td>p:nth-of-type(2)</td><td>Selects every &lt;p&gt; element that is the second &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><strong>:only-of-type</strong></td><td>p:only-of-type</td><td>Selects every &lt;p&gt; element that is the only &lt;p&gt; element of its parent</td>
  </tr>
  <tr>
    <td><strong>:only-child</strong></td><td>p:only-child</td><td>Selects every &lt;p&gt; element that is the only child of its parent</td>
  </tr>
  <tr>
    <td><strong>:optional</strong></td><td>input:optional</td><td>Selects input elements with no "required" attribute</td>
  </tr>
  <tr>
    <td><strong>:out-of-range</strong></td><td>input:out-of-range</td><td>Selects input elements with a value outside a specified range</td>
  </tr>
  <tr>
    <td><strong>::placeholder</strong></td><td>input::placeholder</td><td>Selects input elements with placeholder text</td>
  </tr>
  <tr>
    <td><strong>:read-only</strong></td><td>input:read-only</td><td>Selects input elements with the "readonly" attribute specified</td>
  </tr>
  <tr>
    <td><strong>:read-write</strong></td><td>input:read-write</td><td>Selects input elements with the "readonly" attribute NOT specified</td>
  </tr>
  <tr>
    <td><strong>:required</strong></td><td>input:required</td><td>Selects input elements with the "required" attribute specified</td>
  </tr>
  <tr>
    <td><strong>:root</strong></td><td>:root</td><td>Selects the document's root element</td>
  </tr>
  <tr>
    <td><strong>::selection</strong></td><td>::selection</td><td>Selects the portion of an element that is selected by a user</td>
  </tr>
  <tr>
    <td><strong>:target</strong></td><td>#news:target </td><td>Selects the current active #news element (clicked on a URL containing that anchor name)</td>
  </tr>
  <tr>
    <td><strong>:valid</strong></td><td>input:valid</td><td>Selects all input elements with a valid value</td>
  </tr>
  <tr>
    <td><strong>:visited</strong></td><td>a:visited</td><td>Selects all visited links</td>
  </tr>
</tbody></table>

<br/>


### Commonly Used Selectors

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em; color: darkblue; font-weight: bold;"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#selectors">CSS Selectors</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Selector</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">HTML</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">CSS</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>tag</td>
    <td>&lt;li&gt;</td>
    <td>li {list-style_type: circle;}</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#tag-selector">Selector</a></td>
  </tr>
  <tr>
    <td>id</td>
    <td>&lt;p id="p18"&gt; Ulysses &lt;/p&gt;</td>
    <td>#p18 {color: blue;}</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#id-selector">Selector</a></td>
  </tr>
  <tr>
    <td>class</td>
    <td>&lt;li class="bird flying"&gt;eagle&lt;/li&gt;</td>
    <td>.bird   { color: blue; } <br/>.flying { text-decoration: underline; }</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#class-selector">Selector</a></td>
  </tr>
  <tr>
    <td>Comma separated</td>
    <td>,</td>
    <td>blockquote, <br/> q, <br/> .speech { <br/> &nbsp;&nbsp;&nbsp;&nbsp; color: red; <br/>&nbsp;&nbsp;&nbsp;&nbsp; font-style: italic; <br/> } <br/> .speech { font-weight: bold; }</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#comma-separated-selectors">Selector</a></td>
  </tr>
  <tr>
    <td>Specialized</td>
    <td>&lt;li class="insect flying"&gt;wasp&lt;/li&gt;</td>
    <td>.insect.flying { <br/> &nbsp;&nbsp;&nbsp;&nbsp; text-decoration: underline; <br/> &nbsp;&nbsp;&nbsp;&nbsp; font-weight: bold; <br/>   }</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#specialized-selectors">Selector</a></td>
  </tr>
  <tr>
    <td>Descendant</td>
    <td>&lt;section id="intro"&gt; Welcome to &lt;a href="#palaceland"&gt; PalaceLand &lt;/a&gt;</td>
    <td>#intro a { color: red; }</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#descendant-selectors">Selector</a></td>
  </tr>
  <tr>
    <td>Direct descendant</td>
    <td>&lt;section id="intro"&gt; Welcome to &lt;a href="#palaceland"&gt; PalaceLand &lt;/a&gt;</td>
    <td>#intro > a { font-size: large; }</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03.CSS.md#direct-descendant-selectors---">Selector</a></td>
  </tr>
  </tbody>
</table>



### Styling with Pseudo Class


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Class</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>tr:nth-child(even)<br/>tr:nth-child(odd)<br/>tr:nth-cjild(An+B)</td>
    <td><ul><li>alternating colors for table rows making it easier to differentiate data between rows</li><li> specified with a single argument, which represents the pattern for matching elements</li><li>Examples:<ul><li><strong>tr:nth-child(odd)</strong> = <strong>tr:nth-child(2n+1)</strong></li><li><strong>tr:nth-child(even)</strong> = <strong>tr:nth-child(2n)</strong></li><li><strong>:nth-child(7)</strong>: the seventh element</li><li><strong>:nth-child(5n)</strong>: elements 5 [=5×1], 10 [=5×2], 15 [=5×3], etc.</li><li><strong>:nth-child(3n+4)</strong>: elements 4 [=(3×0)+4], 7 [=(3×1)+4], 10 [=(3×2)+4], 13 [=(3×3)+4], etc.</li><li><strong>:nth-child(-n+3)</strong>: the first three elements. [=-0+3, -1+3, -2+3]</li></ul></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#-nth-child">Zebra</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-child">MDN</a></td>
  </tr>
  <tr>
    <td>tr:hover</td>
    <td><ul><li>interact with an element with a pointing device</li><li>generally triggered when the user hovers over an element with the cursor (mouse pointer)</li><li>overridden by any subsequent link-related pseudo-class (:link, :visited, or :active) that has at least equal specificity</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#-hover-active">Hover</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:hover">MDN</a></td>
  </tr>
  <tr>
    <td>tr:visted</td>
    <td><ul><li>usually put on a selector that resolves to an &lt;a&gt; tag</li><li>represent links that the user has already visited</li><li>overridden by any subsequent link-related pseudo-class (:link, :hover, or :active) that has at least equal specificity</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#-visited">Visted</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:visited">MDN</a></td>
  </tr>
  <tr>
    <td>tr:active</td>
    <td><ul><li>an element (such as a button) that is being activated by the user</li><li>typically starts when the user presses down the primary mouse button</li></<li>commonly used on &lt;a&gt; and &lt;button&gt; elements</li><li>overridden by any subsequent link-related pseudo-class</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#-hover-active">Active</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:active">MDN</a></td>
  </tr>
  </tbody>
</table>

### Tree Presentation - Inheritance

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/0e1bd16d542e4a1085cb8d9b305f8e59/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40833b012fc6dd41f68fa5fd6e3b93e8a8">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c3441bd3d744e14d5d1c0c663d7ad1dc/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-4-2_inheritance_tree.PNG" style="margin: 0.1em;" alt="ags that contain other tags are parents, and the tags inside of them are their children in the following tree representation." title="HTML inheritance structure" width="250">
  </a></div>
</div>

+ [Inheritance](../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#inheritance): the cascading of a CSS property from parent to child

+ CSS property values set on one element will be transferred down the tree to that element's children.

+ Not every property is inherited, but many are, e.g., the layout properties (margin, padding, position, width, etc.) and the decorative properties (border, background, etc.)

+ Inheritance can be explicitly leveraged.

+ Reducing repetition in CSS rules and make project easier to maintain by smartly leveraging

+ No reliable rule for which CSS properties are inheritable by default and which are not

+ Generally, the properties associated with positioning and layout are not inherited. Likewise, the decorative properties (borders, background images, etc.) do not inherit.

+ Most properties that begin with text- or font- inherit.


### CSS Precedence

+ [Precedence](../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#precedence)
  + most CSS properties are orthogonal to one another
  + organize the CSS properties in rules in ways that make sense to developers
  
+ [Guidelines](../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#precedence) to resolve conflicting rules
  1. Most specific rule
    + A more specific rule takes precedence over a less specific rule.
    + A rule that more tightly matches a particular element than a general rule will be applied.
    + e.g., `ul li span {color: red;}` > `span {color: blue;}`
  2. #id selector is the most specific
    + an id selector (e.g. #someid) considered more specific than rules without
  3. .class selector is more specific than a tag selector
    + a class selector (e.g. .someclass) are considered more specific than rules without except for the id selector
  4. Rules that come later override those that come earlier
    + guideline for two CSS rulesets with the same selector


+ [Rules](https://stackoverflow.com/questions/25105736/what-is-the-order-of-precedence-for-css):

  1. __inline > style/css file__: inline css ( html style attribute ) overrides css rules in style tag and css file
  2. __specific > less-specific__: a more specific selector takes precedence over a less specific one
  3. __later > earlier__: rules that appear later in the code override earlier rules if both have the same specificity.
  4. __`!important`__ highest: A css rule with `!important` always takes precedence.


+ Four categories which define the [specificity level](https://www.w3schools.com/css/css_specificity.asp) of a selector:

  1. __Inline styles__ - An inline style is attached directly to the element to be styled. Example: `<h1 style="color: #ffffff;">`.
  2. __IDs__ - An ID is a unique identifier for the page elements, such as `#navbar`.
  3. __Classes, attributes and pseudo-classes__ - This category includes `.classes`, `[attributes]` and pseudo-classes such as `:hover`, `:focus` etc.
  4. __Elements__ and __pseudo-elements__ - This category includes element names and pseudo-elements, such as `h1`, `div`, `:before` and `:after`.

+ [selector's specificity calculation](https://www.w3.org/TR/selectors-3/#specificity):

  + count the number of ID selectors in the selector (= a)
  + count the number of class selectors, attributes selectors, and pseudo-classes in the selector (= b)
  + count the number of type selectors and pseudo-elements in the selector (= c)
  + ignore the universal selector

    + Examples:
      <pre style="border: none; font-family: 'Courier New'; font-weight: bold;">
        *               /* a=0 b=0 c=0 -> specificity =   0 */
        LI              /* a=0 b=0 c=1 -> specificity =   1 */
        UL LI           /* a=0 b=0 c=2 -> specificity =   2 */
        UL OL+LI        /* a=0 b=0 c=3 -> specificity =   3 */
        H1 + *[REL=up]  /* a=0 b=1 c=1 -> specificity =  11 */
        UL OL LI.red    /* a=0 b=1 c=3 -> specificity =  13 */
        LI.red.level    /* a=0 b=2 c=1 -> specificity =  21 */
        #x34y           /* a=1 b=0 c=0 -> specificity = 100 */
        #s12:not(FOO)   /* a=1 b=0 c=1 -> specificity = 101 */
      </pre>



## Font Property

### List of Font Properties

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.w3.org/Style/Examples/007/fonts">Font properties</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Property</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Value</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>font-family</td>
    <td>font face, a collection of Web safe fonts that generally each browser has agreed to support</td>
    <td>Verdana, New Time Roman, serif, sans-serif, monospace, cursive, fantasy, etc.</td>
    <td><a href="https://www.w3.org/TR/css-fonts/#font-family-prop">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#font-family">Font</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#font-family">Common</a></td>
  </tr>
  <tr>
    <td>font-size</td>
    <td>overall scale of the text</td>
    <td>em, %, px, vh</td>
    <td><a href="https://www.w3.org/TR/css-fonts/#font-size-prop">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#font-size">Font</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#font-size">Common</a></td>
  </tr>
  <tr>
    <td>font-weight</td>
    <td>thickness of the letters</td>
    <td>&lt;number&gt;, 100~900, bold=700, normal = 400, bolder, lighter, normal</td>
    <td><a href="https://www.w3.org/TR/css-fonts/#font-weight-prop">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#font-weight">Font</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#font-weight-bold">Common</a></td>
  </tr>
  <tr>
    <td>font-style</td>
    <td>adjust the angle of the letters in relation to the horizontal plane</td>
    <td>italic, normal, oblique &lt;angle&gt;</td>
    <td><a href="https://www.w3.org/TR/CSS2/box.html#propdef-padding-top">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#padding">Font</a></td>
  </tr>
  <tr>
    <td>text_decoration</td>
    <td>add a line across text</td>
    <td>underline</td>
    <td><a href="https://www.w3.org/TR/css3-background/#borders">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#border">Font</a></td>
  </tr>
  <tr>
    <td>color</td>
    <td>text color</td>
    <td>blue, lightblue, darkblue, red, etc.</td>
    <td><a href="HTML-color.md">Color</a></td>
  </tr>
  <tr>
    <td>line-height</td>
    <td>height of the space; the one that makes the area given to each line of text larger or smaller, without changing the actual size of the individual characters themselves</td>
    <td>&lt;number&gt;</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#line-height">Common</a></td>
  </tr>
  <tr>
    <td>text-align</td>
    <td>alignment</td>
    <td>left, center, right, justify, justify-all</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#text-align">Common</a></td>
  </tr>
  <tr>
    <td>text-decoration</td>
    <td>the decoration added to text</td>
    <td>underline, overline, line-through, none</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#text-decoration-underline">Common</a></td>
  </tbody>
</table>


### Typography

+ [Typography](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
  + sans-serif: the letters do not have added flourishes; most popular; `Helvetica`, `Verdana`, `Arial`, `Tahoma`
  + serif - the small flourish lines at the edges of letters and symbols; `Times New Roman`, `Book Antiqua`, `Georgia`
  + monospace - all letters have the same fixed width; `Courier New`
  + cursive - mimic human handwriting often by joining letters or having an italic slant; `Comic Sans MS`
  + fantasy - the most diverse category of fonts including all of those that are particularly decorative




## Color Properties

### Format of Color

+ [Named colors](../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#named-colors): the most common English names for colors; e.g., `color: transparent;`

+ [rgb/rgba](../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#rgb-rgba):
  + rgb(): 
    + any color on a computer is exactly specified by mixing three components together: red, green, and blue
    + the amount of each component falls within a range between 0 and 255
    + syntax: `rgb( red, green, blue);`
    + e.g., `p { color: rgb(10, 200, 255); }`
  + rgba(): 
    + used for semi-transparent colors
    + the fourth value: the "alpha channel", the opacity
    + alpha: a number between 0 and 1
    + e.g., `b { color: rgba(10, 200, 255, 0.5); }`

+ [Hex code](../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#hex-code)
  + providing an hexadecimal (hex) code w.r.t. [0, 255]
  + start with the pound sign (#) and is followed by three pairs of hex number, ranging 00 to FF
  + e.g., `p { color: #3A2BFF; }`

+ A `<color>` is either a keyword or a numerical RGB specification.

+ Complementary and Triadic colour schemes

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://www.w3.org/wiki/Colour_theory">
      <img src="https://www.w3.org/wiki/images/4/49/50000000.jpg" style="margin: 0.1em;" alt="the complementary scheme, where you match up colours that lie directly opposite each other on the colour wheel." title="Complementary colour schemes" width="450">
      <img src="https://www.w3.org/wiki/images/e/e5/80000001.jpg" style="margin: 0.1em;" alt="A triadic colour scheme is created when you pick one colour and then pick two other colours that lie equidistant from each other around the circle." title="Triadic colour schemes" width="300">
    </a></div>
  </div>


### List of Color Properties

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.w3.org/TR/css3-color/#foreground">Foreground</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Property</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>color</td>
    <td>the foreground color of an element's text content</td>
    <td><a href="https://www.w3.org/TR/css3-color/#foreground">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#color">Color18</a></td>
  </tr>
  <tr>
    <td>background-color</td>
    <td>background color of an element</td>
    <td><a href="https://www.w3.org/TR/css3-background/#the-background-color">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#background-color">BGColor18</a></td>
  </tr>
  </tbody>
</table>


### Important References

+ Color
  + [Color names and sRGB values](HTML-Color.md)
  + [Tanaguru Contrast-Finder](http://contrast-finder.tanaguru.com/)


## Item List Properties

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=100%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Lists_and_Counters">List Properties</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Property</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Value</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>list-style</td>
    <td>a shorthand to set list style properties list-style-type, list-style-image, and list-style-position</td>
    <td>list-style-type<br/>list-style-image<br/>list-style-position</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style">MDN</a></td>
  </tr>
  <tr>
    <td>list-style-type</td>
    <td><ul><li>sets the marker (such as a disc, character, or custom counter style) of a list item element</li><li>color of the marker the same as the computed color of the element it applies to</li><li>applied to any element whose display value is set to list-item</li></ul></td>
    <td><ul><li>&lt;custom-ident&gt;: an identifier matching the value of a @counter-style or one of the predefined styles</li><li>symbols(): defines an anonymous style of the list<ul><li>ul: disc, circle, square, none </li><li>ol: decimal, decimal-leading-zero, lower-roman, upper-roman, lower-alpha, upper-alpha, armenian, georgian, simp-chinese-formal, etc.</li></ul></li><li>&lt;string&gt;: used as the item's marker</li><li>none</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#list-style-type">List</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type">MDN</a></td>
  </tr>
  <tr>
    <td>list-style-position</td>
    <td>how closely it is positioned to the list itself</td>
    <td>inside<br/>outside</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#list-style-position">List</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-position">MDN</a></td>
  </tr>
  <tr>
    <td>list-style-image</td>
    <td>customized little markers on a list</td>
    <td>&lt;url&gt<br/>none</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#list-style-image">List</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-image">MDN</a></td>
  </tr>
  </tbody>
</table>


## Image Related Properties

<table  table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/image">Image Properties</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 15%;">Kind of Object (CSS Property)</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 40%;">Default object size</th>
  </tr>
  </thead>
 <tbody>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-image" title="The background-image CSS property sets one or more background images on an element."><code>background-image</code></a></td> <td>The size of the element's background positioning area</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-image" title="The list-style-image CSS property sets an image to be used as the list item marker."><code>list-style-image</code></a></td> <td>The size of a <code>1em</code> character</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-image-source" title="The border-image-source CSS property sets the source image used to create an element's border image."><code>border-image-source</code></a></td> <td>The size of the element's border image area</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/cursor" title="The cursor CSS property sets the type of cursor, if any, to show when the mouse pointer is over an element."><code>cursor</code></a></td> <td>The browser-defined size matching the usual cursor size on the client's system</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/mask-image" title="The mask-image CSS property sets the image that is used as mask layer for an element."><code>mask-image</code></a></td> <td>?</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/shape-outside" title="The shape-outside CSS property defines a shape—which may be non-rectangular—around which adjacent inline content should wrap."><code>shape-outside</code></a></td> <td>?</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/mask-border-source" title="The mask-border-source CSS property sets the source image used to create an element's mask border."><code>mask-border-source</code></a></td> <td>?</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/symbols" title="The symbols() CSS function lets you define counter styles inline, directly as the value of a property such as list-style. Unlike @counter-style, symbols() is anonymous (i.e., it can only be used once). Although less powerful, it is shorter and easier to write than @counter-style."><code>symbols</code></a> for @counter-style</td> <td>At risk feature. If supported, the browser-defined size matching the usual cursor size on the client's system</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/content" title="The content CSS property replaces an element with a generated value. Objects inserted using the content property are anonymous replaced elements."><code>content</code></a> for a pseudo-element (<a href="/en-US/docs/Web/CSS/::after" title="In CSS, ::after creates a pseudo-element that is the last child of the selected element. It is often used to add cosmetic content to an element with the content property."><code>::after</code></a>/<a href="/en-US/docs/Web/CSS/::before" title="In CSS, ::before creates a pseudo-element that is the first child of the selected element. It is often used to add cosmetic content to an element with the content property."><code>::before</code></a>)</td> <td>A 300px × 150px rectangle</td></tr>
 </tbody>
</table>


## Background Properties


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.w3.org/TR/CSS22/colors.html#background-properties">List of Background properties</a> (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Backgrounds_and_Borders">MDN</a>)</caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:15%;">Property</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:15%;">Value</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>  
    <td>background</td>
    <td>&lt;attachment&gt;<br/>&lt;box&gt;<br/>&lt;background-color&gt;<br/>&lt;bg-image&gt;<br/>&lt;position&gt;<br/>&lt;repeat-style&gt;<br/>&lt;bg-size&gt;</td>
    <td>a shorthand that sets the following properties in a single declaration: background-clip, background-color, background-image, background-origin, background-position, background-repeat, background-size, and background-attachment</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background">MDN</a></td>
  </tr>
  <tr>  
    <td>background-color</td>
    <td>&lt;color&gt;<br/>transparent<br/>inherit</td>
    <td>set the background color of an element, either a &lt;color&gt;> value or the keyword 'transparent', to make the underlying colors shine through</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#background-color">Color</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-color">MDN</a></td>
  </tr>
  <tr>  
    <td>background-image</td>
    <td>&lt;uri&gt;<br/>none<br/>inherit</td>
    <td>set the background image of an element</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#background-image">Image</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-image">MDN</a></td>
  </tr>
  <tr>  
    <td>background-repeat</td>
    <td>repeat<br/>repeat-x<br/>repeat-y<br/>no-repeat<br/>inherit</td>
    <td>specify whether the image is repeated (tiled), and how</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#background-repeat">Repeat</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-repeat">MDN</a></td>
  </tr>
  <tr>  
    <td>background-attachment</td>
    <td>scroll<br/>fixed<br/>inherit</td>
    <td>specifies whether it is fixed with regard to the viewport ('fixed') or scrolls along with the containing block ('scroll')</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-attachment">MDN</a></td>
  </tr>
  <tr>  
    <td>background-size</td>
    <td>[&lt;length&gt; &ltlength&gt]<br/>[&lt;length&gt;  auto]<br/>[&lt;percentag&gt; auto]</td>
    <td>size a background image to fit its element<br/>auto preserves aspect ratio, no distorting</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#background-size">Size</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-size">MDN</a></td>
  </tr>
  <tr>  
    <td>background-position</td>
    <td><strong>1-value syntax</strong>: <br/>&nbsp;&nbsp;&nbsp;&nbsp;center<br/>&nbsp;&nbsp;&nbsp;&nbsp;top<br/>&nbsp;&nbsp;&nbsp;&nbsp;left<br/>&nbsp;&nbsp;&nbsp;&nbsp;bottom<br/>&nbsp;&nbsp;&nbsp;&nbsp;right<br/>&nbsp;&nbsp;&nbsp;&nbsp;&lt;length-percentage&gt; <br/><strong>2-value syntax</strong>: <br/>&nbsp;&nbsp;&nbsp;&nbsp;top<br/>&nbsp;&nbsp;&nbsp;&nbsp;right<br/>&nbsp;&nbsp;&nbsp;&nbsp;bottom<br/>&nbsp;&nbsp;&nbsp;&nbsp;left<br/>&nbsp;&nbsp;&nbsp;&nbsp;&lt;length-percentage&gt;</td>
    <td>specifies background image's initial position<br/>1 value: the 2nd value = center<br/>2 calues: (horizontal, vertical) position</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#background-position">Position</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-position">MDN</a></td>
  </tr>
  </tbody>
</table>



## Alignment Property

### Characteristics of Alignment

+ [Horizontal centering](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#horizontal-centering)
  + inline elements
    + positioned along the baseline
    + no CSS property directly applied to cause this element to center
    + using `text-align` to centerize an inline element
  + block level elements
    + take the width of their parent by defaut
    + NOT recommended: limiting the width of the element
    + RECOMMENDED: `margin: auto;`: center the element

+ [Vertical centering](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#vertical-centering)
  + Inline elements:
    + respect the vertical-align property
    + aligned relative to the baseline
  + Block level elements
    + no margin:auto approach
    + flexbox: the best practice to centerize vertically


### List of Alignment Properties

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Property</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Value</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>  
    <td>text-align</td>
    <td>set the content's alignment horizontally</td>
    <td>left, right, center, justify</td>
    <td><a href="https://www.w3.org/TR/CSS22/text.html#alignment-prop">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#text-align">Alignment</a></td>
  </tr>
  <tr>
    <td>line-height</td>
    <td>HTML element block grows and the text will vertically center within it</td>
    <td>em, rem, %, px</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#line-height">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#line-height">Alignment</a></td>
  </tr>
  </tbody>
</table>


## Box Model

### Box Model and Characteristics

+ [CSS Box Model](../WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#css-box-model)
  + All elements in an html document end up being treated as rectangles somewhere in the window.
  + 3 important spacing features
    + Padding: just outside the content
    + Border: go around the content and the padding
    + Margin: specifies the position of the element relative to whatever is adjacent to it, either to the right or left, or top or bottom
  + Padding separates the contents from the border.
  + The border property has a lot more options than the padding or margin
    + visible
    + size, shape, color and style
    + completely or partially transparent border
    + color of the border to the color of the background
  + Default border properties
    + border-width (the size of your imaginary pen)
    + border-style (dashed, dotted, solid, etc.)
    + border-color (the color of your pen)
  + Negative margin: overlap with another element on the page


<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.w3.org/TR/CSS22/box.html">
    <img src="https://www.w3.org/TR/CSS22/images/boxdim.png" style="margin: 0.1em;" alt="Each box has a content area (e.g., text, an image, etc.) and optional surrounding padding, border, and margin areas; the size of each area is specified by properties defined below. The following diagram shows how these areas relate and the terminology used to refer to pieces of margin, border, and padding. The margin, border, and padding can be broken down into top, right, bottom, and left segments (e.g., in the diagram, 'LM' for left margin, 'RP' for right padding, 'TB' for top border, etc.)." title="The four areas of the generic CSS box: content, padding, border, and margin" width="300">
  </a>
  <a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/b51f656fe5bd47a7b2f24fe7617b7870/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40021c5be913ac42348edca84f9a89bf46">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f6f6c946356774ddb886956cd94df4c9/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/margin__padding__border.png" style="margin: 0.1em;" alt="Diagram presenting the relationship of margin, padding and border" title="Box Model" width="300">
  </a></div>
</div>


+ [MDN Box Model](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model)
  + CSS determines the size, position, and properties (color, background, border size, etc.) of these boxes.
  + composed of four parts (or areas), defined by their respective edges: the content edge, padding edge, border edge, and margin edge.
  + content area:
    + bounded by the content edge, contains the "real" content of the element, such as text, an image, or a video player
    + dimensions: the content width (or content-box width) and the content height (or content-box height)
    + box-sizing property: explicitly defined with the width, min-width, max-width, height, min-height, and max-height properties
  + padding area
    + bounded by the padding edge, extends the content area to include the element's padding
    + dimensions: the padding-box width and the padding-box height
    + determined by the padding-top, padding-right, padding-bottom, padding-left, and shorthand padding properties
  + border area
    + bounded by the border edge, extends the padding area to include the element's borders
    + dimensions: the border-box width and the border-box height
    + thickness of the borders: the border-width and shorthand border properties
    + box-sizing property: set to border-box
    + explicitly defined with the width, min-width, max-width, height, min-height, and max-height properties
    + a background (background-color or background-image) set on a box, it extends to the outer edge of the border
  + margin area
    + bounded by the margin edge, extends the border area to include an empty area used to separate the element from its neighbors
    + dimensions: the margin-box width and the margin-box height
    + determined by the margin-top, margin-right, margin-bottom, margin-left, and shorthand margin properties
    + margin collapsing: not clearly defined since margins are shared between boxes

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model" ismap target="_blank">
    <img src="https://mdn.mozillademos.org/files/8685/boxmodel-(3).png" style="margin: 0.1em;" alt="MDN Box Model" title="MDN Box Model" width=350>
  </a>
</div>

+ [Border style](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#border-style)

  <table style="border-collapse: separate; border-spacing: 4px;" width=90%>
  <tbody>
    <tr>
      <td style="width: 10%; padding: 0.5em; text-align: center;  border-style: solid;">solid</td>
      <td style="width: 10%; padding: 0.5em; text-align: center;  border-style: dotted;">dotted</td>
      <td style="width: 10%; padding: 0.5em; text-align: center;  border-style: dashed;">dashed</td>
      <td style="width: 10%; padding: 0.5em; text-align: center;  border-style: double;">double</td>
      <td style="width: 10%; padding: 0.5em; text-align: center;  border-style: groove;">groove</td>
      <td style="width: 10%; padding: 0.5em; text-align: center;  border-style: ridge;">ridge</td>
      <td style="width: 10%; padding: 0.5em; text-align: center;  border-style: inset;">inset</td>
      <td style="width: 10%; padding: 0.5em; text-align: center;  border-style: outset;">outset</td>
    </tr>
  </tbody>
  </table>

+ [Element Size Control](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#managing-element-size)
  + control an element's size for the purpose of controlling how a border or background extends relative to the item itself
  + not recommended: width, height, left and top CSS properties
  + best practice: padding properties
  + Margins make space between elements and padding makes an element larger.


### Box Sizing

<table table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing">Values of box-sizing property</a></caption>
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 30%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Example</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
  <tr>
    <td>content-box</td>
    <td><ul> <li>the default CSS box-sizing behavior</li> <li>including width and height, but not padding, border, or margin</li><li> the dimensions of the element: width = width of the content; height = height of the content</li></ul></td>
    <td><div>box-sizing: content-box;<br/>width: 100%</div><br/><div>box-sizing: content-box;<br/>width: 100%;<br/>border: solid #5B6DCD 10px;</div></td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#the-box-model-and-box-sizing">Box-sizing</a></td>
  </tr>
  <tr>
    <td>border-box</td>
    <td><ul><li>telling the browser to account for any border and padding in the values specified for an element's width and height</li><li>including width and height, padding & border, but not margin</li><li> the dimensions of the element: width = border + padding + width of the content, height = border + padding + height of the content</li></ul></td>
    <td><div>box-sizing: content-box;<br/>width: 100%</div><div>box-sizing: content-box;<br/>width: 100%;<br/>border: solid #5B6DCD 10px;</div></td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#the-box-model-and-box-sizing">Box-sizing</a></td>
  </tr>
  </tbody>
</table>


### Box Model Properties

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Box_model#Box_properties">Box Properties</a></caption>
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 20%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>width</td>
    <td>set an element's width; override by 'min-width' and 'max-width'</td>
    <td><ul><li>&lt;length&gt;</li> <li>&lt;percentag&gt;</li> <li>auto: browser caclulate</li><ul></td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/width">MDN</a>, <a href="#element-width-and-height">Element</a>, </td>
  </tr>
  <tr>
    <td>height</td>
    <td>specify the height of an elementh; override by 'min-height' and 'max-height'</td>
    <td><ul><li>&lt;length&gt;</li> <li>&lt;percentag&gt;</li> <li>auto: browser caclulate</li><ul></td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/height">MDN</a>, <a href="#element-width-and-height">Element</a>, </td>
  </tr>
  <tr>
    <td>padding</td>
    <td>padding for all sides of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a>, </td>
  </tr>
  <tr>
    <td>padding-top</td>
    <td>padding for top side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-right</td>
    <td>padding for right side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-bottom</td>
    <td>padding for bottom side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding-left</td>
    <td>padding for left side of an element</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border</td>
    <td>the style, width, and color of an element's border</td>
    <td>border-width, border-style (required), border-color</td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#border-abbreviations">Border</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-style</td>
    <td>what kind of border to display</td>
    <td>dotted, dashed, solid, double, groove, ridge, inset, outset, none, hidden <br/><br/>Examples: <br/><ul><li>border-style: dotted solid double dashed;</li>  <li>border-style: dotted solid double;</li> <li>border-style: dotted solid;</li> <li>border-style: dotted;</li></ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#border-style">Border</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-width</td>
    <td>the width of the four borders</td>
    <td>px, pt, cm, em, thin, medium, thick</td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-color</td>
    <td>the color of the four borders</td>
    <td>name, Hex, RGB, transparent</td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-radius</td>
    <td>round the corners of an element's outer border edge</td>
    <td>&lt;length&gt; <br/>&lt;percentage&gt; </td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#border-radius">Border</a>, <a href="https://www.w3schools.com/cssref/css3_pr_border-radius.asp">W3S</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius">MDN</a></td>
  </tr>
  <tr>
    <td>box-shadow</td>
    <td>add shadow effects around an element's frame<br/><br/>Example: <br/>box-shadow: &lt;x-offset&gt; &lt;y-offset&gt; &lt;blur&gt; &lt;color&gt;;</td>
    <td>none: no shadow<br/>[&lt;offset-x&gt; &lt;offset-y&gt;](required): set the shadow offset<br/>&lt;blur-radius&gt;: the larger this value, the bigger the blur<br/>&lt;spread-radius&gt;: cause the shadow to expand and grow bigger (positive) or shrink (negative)<br/>&lt;color&gt;: keywords or notations</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#box-shadow">Border</a>, <a href="https://www.w3schools.com/cssref/css3_pr_box-shadow.asp">W3S</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow">MDN</a></td>
  </tr>
  <tr>
    <td>text-shadow</td>
    <td>add shadows to text<br/><br/>Example: <br/>box-shadow: &lt;x-offset&gt; &lt;y-offset&gt; &lt;blur&gt; &lt;color&gt;;</td>
    <td>[&lt;offset-x&gt; &lt;offset-y&gt;](required): set the shadow offset<br/>&lt;blur-radius&gt;: the larger this value, the bigger the blur<br/>&lt;color&gt;: keywords or notations</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#text-shadow">Border</a>, <a href="https://www.w3schools.com/cssref/css3_pr_text-shadow.asp">W3S</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow">MDN</a></td>
  </tr>
  <tr>
    <td>margin</td>
    <td>space around elements, outside of any defined borders</td>
    <td>#px, auto <br/><br/> Example: <br/><ul><li>margin: top right bottom left;</li>  <li>margin: top right bottom</li> <li>margin: top right</li></ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#margin">Common</a></td>
  </tr>
  <tr>
    <td>margin-top</td>
    <td>space on top of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-right</td>
    <td>space on right of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-bottom</td>
    <td>space on bottom of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  <tr>
    <td>margin-left</td>
    <td>space on left of elements, outside of any defined borders</td>
    <td><ul><li>length (`px`, `em`, `cm`, etc.)</li> <li>% (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../1-HTML5CSSFund/04-Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a></td>
  </tr>
  </tbody>
</table>




## Sizing and Dimensions


### Characteristics of Size & Dimensions

+ [Sizing & Dimensions](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#sizing-and-dimensions)
  + The default sizing behavior depends upon the display property for an element.
  + Images: preserrve the original aspecct ratio if only one simension set
  + Variability: one of the most powerful and useful aspects of these elements
  + Sizing properties: width, min-width, max-width, height, min-height, max-height
    + remove that variability from the element
  + Avoid using explicit dimension properties like width and height
  + using the min- or max- variants if required

+ [Inline elements](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#inline-2)
  + the size of their content plus any padding
  + ignore any explicit sizing properties (width, height, etc.) unless position:absolute or position:fixed
  + using inline-block instead if explicitly indicated

+ [Inline-block elements](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#inline-block-1)
  + take the size of their content, plus padding
  + respect any explicit sizing properties
  + sized (height and width) to their content

+ [Block level elements](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#block-2)
  + take the width of their parent and the height of their content if no sizing properties used
  + respect any explicit sizing properties


### Global Sizing

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Property</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Value</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:11%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>width</td>
    <td>element width</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, auto, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#the-width-property">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#width-and-height">Layout</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/width">MDN</a></td>
  </tr>
  <tr>
    <td>height</td>
    <td>element height</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, auto, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#the-height-property">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#width-and-height">Layout</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/height">MDN</a></td>
  </tr>
  <tr>
    <td>min-width</td>
    <td>minimum width of the element</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#min-max-widths">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#min-width-max-width-min-height-max-height">Layout</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/min-width">MDN</a></td>
  </tr>
  <tr>
    <td>min-width</td>
    <td>maximum width of the element</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, none, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#min-max-widths">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#min-width-max-width-min-height-max-height">Layout</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/max-width">MDN</a></td>
  </tr>
  <tr>
    <td>min-height</td>
    <td>minimum height of the element</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#min-max-heights">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#min-width-max-width-min-height-max-height">Layout</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/min-height">MDN</a></td>
  </tr>
  <tr>
    <td>max-height</td>
    <td>maximum height of the element</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, none, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#min-max-heights">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#min-width-max-width-min-height-max-height">Layout</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/max-height">MDN</a></td>
  </tr>
  </tbody>
</table>



### Characteristics of Overflow

+ [Overflow](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#cropping-and-scrolling-overflow)
  + dimensions overdetermined by the sizing properties
  + with common text, normally only occurs in the vertical direction
  + overflow horizontally when containing images, extremely long words, or has adjusted CSS white spacing properties
  + able to assign different policies for horizontal versus vertical overflow


### List of Overflow Properties

<table table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#cropping-and-scrolling-overflow">Overflow Properties</a></caption>
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
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow">Overflow</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#cropping-and-scrolling-overflow">Layout</a>, <a href="..file:///home/hmchen/Projects/Programming/WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#overflow">Table</a></td>
  </tr>
  <tr>
    <td>overflow-x</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows a block-level element's left and right edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-x">Overflow-X</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#cropping-and-scrolling-overflow">Layout</a></td>
  </tr>
  <tr>
    <td>overflow-y</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows an inline element's top and bottom edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-y">Overflow-Y</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#cropping-and-scrolling-overflow">Layout</a></td>
  </tr>
  <tr>
    <td>overflow-block</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows a block-level element's block start and block end edge</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-block">Overflow-Block</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#cropping-and-scrolling-overflow">Layout</a></td>
  </tr>
  <tr>
    <td>overflow-inline</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows an inline element's start and end edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-inline">Overflow-Inline</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#cropping-and-scrolling-overflow">Layout</a></td>
  </tr>
  </tbody>
</table>


### Values of Overflow Propery

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=70%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#cropping-and-scrolling-overflow">Values of Overflow Property</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Values</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>visible</td>
    <td><ul><li>not clipped</li><li>may be rendered outside the padding box</li></ul></td>
  </tr>
  <tr>
    <td>hidden</td>
    <td><ul><li>clipped to fit the padding box</li><li>no scrollbars</li><li>no scrolling</li><li>scrolled programmatically (e.g., by setting the value of a property such as offsetLeft)</li></ul></td>
  </tr>
  <tr>
    <td>clip</td>
    <td><ul><li>clipped to the element's padding box</li><li>forbids all scrolling, including programmatic scrolling</li><li>not start a new formatting context</li><li>not a scroll container</li><li>not supported for all browsers yet</li></ul></td>
  </tr>
  <tr>
    <td>scroll</td>
    <td><ul><li>clipped if necessary to fit the padding box</li><li>always displaying scrollbars whether or not any content is actually clipped</li><li>preventing scrollbars from appearing or disappearing as content changes</li></ul></td>
  </tr>
  <tr>
    <td>auto</td>
    <td><ul><li>depend on the user agent</li><li>fit inside the padding box as visible, but but still establishes a new block formatting context</li><li>Desktop browsers provide scrollbars if content overflows.</li></ul></td>
  </tr>
  </tbody>
</table>



## Floating Property

### List of Flowing Properties

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Property</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Value</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>float</td>
    <td>liberates an element from its automatic position and lifts it up to "float" on top of other elements in the direction specified</td>
    <td>left, right, none, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visuren.html#float-position">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#the-float-property">Float52</a></td>
  </tr>
  <tr>
    <td>clear</td>
    <td>indicate which sides of an element's box(es) may not be adjacent to an earlier floating box</td>
    <td>none, left, right, both, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visuren.html#propdef-clear">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#the-clear-property">Color18</a></td>
  </tr>
  </tbody>
</table>


### CSS Website Layout - Example

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.w3schools.com/css/css_website_layout.asp">
    <img src="css-layout.png" style="margin: 0.1em;" alt="There are tons of different layout designs to choose from. However, the structure above, is one of the most common, and we will take a closer look at it in this tutorial." title="A website is often divided into headers, menus, content and a footer" width="400">
  </a></div>
</div>




## Table Properties

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://www.tallcomponents.com/tallpdf/help/guide/tables?build=net40">
    <img src="https://www.tallcomponents.com/tallpdf5/content/guide/tallpdf/media/table-border-padding-and-margin.png" style="margin: 0.1em;" alt="The extra space outside a border is set by a left, right, top and bottom margin. The extra space inside a border is set by a left, right, top and bottom padding. These attributes are part of the table, row or cell. The following figure makes this clear." title="Padding, Margins and Border Width" width="400">
  </a></div>
  <div><a href="http://learningspot.altervista.org/html-table-tag-attributes/">
    <img src="http://learningspot.altervista.org/wp-content/uploads/2017/07/HTML_cellpadding_cellspacing.png" style="margin: 0.1em;" alt="The size indicated in cellpadding and cellspacing, once set, affects all sides of the cell." title="Table cell padding and spacing" width="345">
  </a></div>
</div>
<br/>


<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Applied To</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 25%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr> 
    <td>border</td>
    <td> &lt;table&gt;, &lt;th&gt;, &lt;td&gt;</td>
    <td>sets border-width, border-style and border-color in order</td>
    <td> <ul><li> &lt;width, style, color&gt; <ul><li>width = pixel </li> <li>style = none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset </li>    <li>color = color name or color values, transparent</li> </ul></li> <li><a href="https://www.w3schools.com/cssref/pr_border-width.asp">border-width</a>: medium, thin, thick, length, initial, inherit, pixel, (left-pixel, right-pixel)</li> <li><a href="https://www.w3schools.com/cssref/pr_border-style.asp">border-style</a> (required): none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset, initial, inherit</li> <li><a href="https://www.w3schools.com/cssref/pr_border-color.asp">border-color</a>: <i>color value</i>, transparent</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#border">Table</a>, <a href="https://www.w3schools.com/cssref/pr_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-top, border-left, broder-bottom, border-right</td>
    <td>&lt;th&gt;, &lt;td&gt;</td>
    <td>set borders to individual sides</td>
    <td> <ul> &lt;width, style, color&gt; <ul><li>width = pixel </li> <li>style = none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset </li> <li>color = color name or color values, transparent</li> </ul></td>
    <td><a href="../WebDev/Frontend-W<td3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#side-borders"></a>, <a href="https://www.w3schools.com/cssref/pr_border-top.asp">Top</a>, <a href="https://www.w3schools.com/cssref/pr_border-right.asp">Right</a>, <a href="https://www.w3schools.com/cssref/pr_border-bottom.asp">Bottom</a>, <a href="https://www.w3schools.com/cssref/pr_border-left.asp">Left</a></td>
  </tr>
  <tr>
    <td>border-collapse</td>
    <td> &lt;table&gt;, &lt;th&gt;, &lt;td&gt;</td>
    <td>to collapse border or not</td>
    <td><ul><li><strong>separate</strong>: each cell will display its own borders; default value</li> <li><strong>collapse</strong>: border are collapsed into a single border (border-spacing and empty-cells properties have no effect)</li><li>initial: sets to default value (separate)</li><li>inherit: inherited from its parent element</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#border-collapse">Collapse</a>, <a href="https://www.w3schools.com/cssref/pr_border-collapse.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-spacing</td>
    <td> &lt;table&gt;, &lt;th&gt;, &lt;td&gt;</td>
    <td>space between content in cell and border</td>
    <td><strong>&lt; length, length&gt; </strong>: specifyingthe distance between the borders of adjacent cells in px, cm, etc. Negative values are not allowed.<ul><li>one value: define both the horizontal and vertical spacing between cells</li> <li>two values: the first sets the horizontal spacing and the second sets the vertical spacing</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#border-spacing">Spacing</a>, <a href="https://www.w3schools.com/cssref/pr_border-spacing.asp">W3S</a></td>
  </tr>
  <tr>
    <td>width; height</td>
    <td> &lt;td&gt;</td>
    <td>set the width and height for the rows and columns for your table based on the content in your cells | units of length like pixels, percentage; auto: the browser will calculate and select a width for the specified element (default value)</td>
    <td><ul><li> auto</li> <li><i>length</i> (px, em, cm, etc.)</li> <li><i>%</i> (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#table-width-and-height">Size</a>, <a href="https://www.w3schools.com/cssref/pr_dim_height.asp">height</a>, <a href="https://www.w3schools.com/cssref/pr_dim_width.asp">width</a></td>
  </tr>
  <tr>
    <td>text-align</td>
    <td> &lt;th&gt;, &lt;td&gt;</td>
    <td>align the text of and cells left, right or center</td>
    <td><ul><li> left</li> <li>right</li> <li>center</li> <li>Default: &lt;th&gt; = center, &lt;td&gt; = left</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#text-align">Size</a>, <a href="https://www.w3schools.com/cssref/pr_text_text-align.asp">W3S</a></td>
  </tr>
  <tr>
    <td>vertical-align</td>
    <td> &lt;th&gt;, &lt;td&gt;</td>
    <td>align the text of and cells top, bottom or middle</td>
    <td><ul><li> top</li> <li>bottom</li> <li>middle</li> <li>Default: middle</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#vertical-align">Size</a>, <a href="https://www.w3schools.com/cssref/pr_pos_vertical-align.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding</td>
    <td> &lt;th&gt;, &lt;td&gt;</td>
    <td>provide some space between border and content in cell</td>
    <td><ul><li><i>length</i> (px, em, cm, etc.)</li> <li><i>%</i> (% of the width of the containing element)</li> <li><strong>&lt;length1, length2&gt;</strong>: <br/>top = bottom = length1; right = left = length2</li> <li><strong>&lt;length1, length2, length3&gt;</strong>: <br/>top = length1; right = left = length2; bottom = length3</li> <li><strong>&lt;length1, length2, length3. length4&gt;</strong>: <br/>top = length1; right = length2; bottom = length3; left = length4</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#padding">Padding</a>, <a href="https://www.w3schools.com/cssref/pr_text_text-align.asp">W3S</a></td>
  </tr>
  </tbody>
</table>



## Display Property

+ Display property
  + different default values for different tags
  + Some tags start with display:block, and others are display:inline.

+ [Baseline](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#baseline)
  + a key concept to understanding how the browser makes its layout decisions
    <a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/306cfa0313a449a29b2dbcb0b2afcb86/1fe35eaba7534b5d86b69fa0e09494a3/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%4065eedf84e09a4619a4152d1cdcadc73a" ismap target="_blank" style="padding-left: 0.5em;">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/03a5c30240869b1400f96ca51fc2eb19/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/baseline2.png" style="margin: 0.1em;" alt="baseline" title="baseline" width=70></a>
  + the blue line indicating the baseline
  + determine how and where the characters are positioned
  + govern the placement of all inline elements

+ Normal Flow / Flow Layout
  + the way that Block and Inline elements are displayed on a page before any changes are made to their layout
  + essentially a set of things that are all working together and know about each other in your layout

+ [Block-level vs. inline](/WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#display-block-versus-inline)
  + Content model:
    + block-level element may contain inline elements and other block-level elements
    + block elements create "larger" structures than inline elements
  + Default formating:
    + block-level elements begin on new lines
    + in-line elements can start anywhere in a line
+ [Block Level](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#block-level)
  + appear __below__ and to the __left__ of their block level neighbors
  + expand to fill the __width of the parent container__ by default
  + respect all __margin__ properties
  + has its __width__ property set
  + takes on the __height__ of all its children
  + ignores the __vertical-align__ property

+ [Inline Elements](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#inline-elements)
  + appear to the right of their preceding __inline neighbor__
  + the __width__ of the content of the element, plus any padding, by default
  + ignore __top and bottom__ margin settings
  + ignore __width and height__ properties
  + subject to __vertical-align__ property as well as CSS __white-space__ settings
  + padding, but not padding-top or padding-bottom
  + cleave to the baseline

+ [Inline-Block Elements](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#inline-block)
  + cleave to the text baseline
  + adjust to the room if top or bottom margins or paddings used
  + respect margin-top and margin-bottom
  + the height of th eline including the vertical padding for inline-block elements
  + inline-block elements respect width and height properties


### Display Type of Elements

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#display-block-versus-inline">Categories of Elements</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="50%"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements#Elements"> Block-level Element </a></td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="50%"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements#Elements">Inline Element</a></td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td valign="top" style="line-height:1.5em;"><strong>&lt;address&gt;</strong>: Contact information<br/><strong>&lt;article&gt;</strong>: Article content<br/><strong>&lt;aside&gt;</strong>: Aside content<br/><strong>&lt;blockquote&gt;</strong>: Long ("block") quotation<br/><strong>&lt;details&gt;</strong>: Disclosure widget<br/><strong>&lt;dialog&gt;</strong>: Dialog box<br/><strong>&lt;dd&gt;</strong>: Describes a term in a description list<br/><strong>&lt;div&gt;</strong>: Document division<br/><strong>&lt;dl&gt;</strong>: Description list<br/><strong>&lt;dt&gt;</strong>: Description list term<br/><strong>&lt;fieldset&gt;</strong>: Field set label<br/><strong>&lt;figcaption&gt;</strong>: Figure caption<br/><strong>&lt;figure&gt;</strong>: Groups media content with a caption (see &lt;figcaption&gt;)<br/><strong>&lt;footer&gt;</strong>: Section or page footer<br/><strong>&lt;form&gt;</strong>: Input form<br/><strong>&lt;h1&gt;</strong>, <strong>&lt;h2&gt;</strong>, <strong>&lt;h3&gt;</strong>, <strong>&lt;h4&gt;</strong>, <strong>&lt;h5&gt;</strong>, <strong>&lt;h6&gt;</strong>: Heading levels 1-6<br/><strong>&lt;header&gt;</strong>: Section or page header<br/><strong>&lt;hgroup&gt;</strong>: Groups header information<br/><strong>&lt;hr&gt;</strong>: Horizontal rule (dividing line)<br/><strong>&lt;li&gt;</strong>: List item<br/><strong>&lt;main&gt;</strong>: Contains the central content unique to this document<br/><strong>&lt;nav&gt;</strong>: Contains navigation links<br/><strong>&lt;ol&gt;</strong>: Ordered list<br/><strong>&lt;p&gt;</strong>: Paragraph<br/><strong>&lt;pre&gt;</strong>: Preformatted text<br/><strong>&lt;section&gt;</strong>: Section of a web page<br/><strong>&lt;table&gt;</strong>: Table<br/><strong>&lt;ul&gt;</strong>: Unordered list</td>
    <td style="line-height:1.5em;"><strong>&lt;a&gt;</strong>: create a hyperlink<br/> <strong>&lt;abbr&gt;</strong> &amp; <strong>&lt;acronym&gt;</strong>: an abbreviation or acronym<br/> <strong>&lt;audio&gt;</strong>: embed sound content in documents<br/> <strong>&lt;b&gt;</strong>: HTML Bring Attention To element; draw the reader's attention to the element's contents<br/><strong>&lt;bdi&gt;</strong>: Bidirectional Isolate element; tell the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text<br/><strong>&lt;bdo&gt;</strong>: Bidirectional Text Override element; override the current directionality of text<br/><strong>&lt;big&gt;</strong>: render the enclosed text at a font size one level larger than the surrounding text<br/><strong>&lt;br&gt;</strong>: produce a line break in text (carriage-return)<br/><strong>&lt;button&gt;</strong>: represent a clickable button<br/><strong>&lt;canvas&gt;</strong>: either the canvas scripting API or the WebGL API to draw graphics and animations<br/><strong>&lt;cite&gt;</strong>: Citation element; used to describe a reference to a cited creative work, and must include the title of that work<br/><strong>&lt;code&gt;</strong>: display its contents styled in a fashion intended to indicate that the text is a short fragment of computer code<br/><strong>&lt;data&gt;</strong>: link a given content with a machine-readable translation<br/><strong>&lt;datalist&gt;</strong>: contain a set of &lt;option&gt; elements that represent the values available for other controls<br/><strong>&lt;del&gt;</strong>: represent a range of text that has been deleted from a document<br/><strong>&lt;dfn&gt;</strong>: Definition element; used to indicate the term being defined within the context of a definition phrase or sentence<br/><strong>&lt;em&gt;</strong>: used to indicate the term being defined within the context of a definition phrase or sentence<br/><strong>&lt;embed&gt;</strong>: embed external content at the specified point in the document<br/><strong>&lt;i&gt;</strong>: represent a range of text that is set off from the normal text for some reason<br/><strong>&lt;iframe&gt;</strong>: Inline Frame element; represent a nested browsing context, embedding another HTML page into the current one<br/><strong>&lt;img&gt;</strong>: embed an image into the document<br/><strong>&lt;input&gt;</strong>: used to create interactive controls for web-based forms<br/><strong>&lt;ins&gt;</strong>: represent a range of text that has been added to a document<br/><strong>&lt;kbd&gt;</strong>: Keyboard Input element; represent a span of inline text denoting textual user input<br/><strong>&lt;label&gt;</strong>: represent a caption for an item in a user interface<br/><strong>&lt;map&gt;</strong>: used with &lt;area&gt; element to define an image map (a clickable link area)<br/><strong>&lt;mark&gt;</strong>: Mark Text element; represent text which is marked or highlighted for reference or notation purposes<br/><strong>&lt;meter&gt;</strong>: represent either a scalar value within a known range or a fractional value<br/><strong>&lt;noscript&gt;</strong>: define a section of HTML to be inserted<br/><strong>&lt;object&gt;</strong>: represent an external resource<br/><strong>&lt;output&gt;</strong>: a container element into which a site or app can inject the results of a calculation or the outcome of a user action<br/><strong>&lt;picture&gt;</strong>: contain zero or more &lt;source&gt; elements and one &lt;img&gt; element to provide versions of an image for different display/device scenarios<br/><strong>&lt;progress&gt;</strong>: display an indicator showing the completion progress of a task<br/><strong>&lt;q&gt;</strong>: the enclosed text is a short inline quotation<br/><strong>&lt;ruby&gt;</strong>: represent a ruby, showing pronunciation of East Asian characters, annotation<br/><strong>&lt;s&gt;</strong>: render text with a strikethrough<br/><strong>&lt;samp&gt;</strong>: Sample Element; used to enclose inline text<br/><strong>&lt;script&gt;</strong>: used to embed or reference executable code<br/><strong>&lt;select&gt;</strong>: represent a control that provides a menu of options<br/><strong>&lt;slot&gt;</strong>: a placeholder inside a web component<br/><strong>&lt;small&gt;</strong>: make the text font size one size smaller down to the browser's minimum font size<br/><strong>&lt;span&gt;</strong>: a generic inline container for phrasing content<br/><strong>&lt;strong&gt;</strong>: indicate that its contents have strong importance, seriousness, or urgency<br/><strong>&lt;sub&gt;</strong>: specify inline text displayed as subscript<br/><strong>&lt;sup&gt;</strong>: specify inline text displayed as superscript<br/><strong>&lt;svg&gt;</strong>: <br/><strong>&lt;template&gt;</strong>: a mechanism for holding HTML that is not to be rendered immediately<br/><strong>&lt;textarea&gt;</strong>: represent a multi-line plain-text editing control<br/><strong>&lt;time&gt;</strong>: represent a specific period in time<br/><strong>&lt;u&gt;</strong>: Unarticulated Annotation Element; a simple solid underline<br/><strong>&lt;tt&gt;</strong>: Teletype Text element; obsolete HTML Teletype Text element<br/><strong>&lt;var&gt;</strong>: Variable element; the name of a variable in a mathematical expression or a programming contex<br/><strong>&lt;video&gt;</strong>: embed a media player<br/><strong>&lt;wbr&gt;</strong>: represent a word break opportunity</td>
  </tr>
  </tbody>
</table>


### Values of Display Property


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display#Syntax">Display Properties</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Category</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Value</th>
  </thead>
  <tbody>
  <tr>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display-outside">&lt;display-outside&gt;</a></td>
    <td>specify the element’s outer display type, which is essentially its role in flow layout</td>
    <td>display: block;<br/>display: inline;<br/>display: run-in;</td>
  </tr>
  <tr>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display-inside">&lt;display-inside&gt;</a></td>
    <td>pecify the element’s inner display type, which defines the type of formatting context that its contents are laid out in (assuming it is a non-replaced element)</td>
    <td>display: flow;<br/>display: flow-root;<br/>display: table;<br/>display: flex;<br/>display: grid;<br/>display: ruby;</td>
  </tr>
  <tr>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display-outside">&lt;display-outside&gt;</a> + <br/><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display-inside">&lt;display-inside&gt;</a></td>
    <td>specify the element’s outer display type, which is essentially its role in flow layout</td>
    <td>display: block flow;<br/>display: inline table;<br/>display: flex run-in;</td>
  </tr>
  <tr>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display-listitem">&lt;display-listitem&gt;</a></td>
    <td>generate a block box for the content and a separate list-item inline box</td>
    <td>display: list-item;<br/>display: list-item block;<br/>display: list-item inline;<br/>display: list-item flow;<br/>display: list-item flow-root;<br/>display: list-item block flow;<br/>display: list-item block flow-root;<br/>display: flow list-item block;</td>
  </tr>
  <tr>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display-internal">&lt;display-internal&gt;</a></td>
    <td>some layout models such as table and ruby have a complex internal structure, with several different roles that their children and descendants can fill</td>
    <td>display: table-row-group;<br/>display: table-header-group;<br/>display: table-footer-group;<br/>display: table-row;<br/>display: table-cell;<br/>display: table-column-group;<br/>display: table-column;<br/>display: table-caption;<br/>display: ruby-base;<br/>display: ruby-text;<br/>display: ruby-base-container;<br/>display: ruby-text-container;</td>
  </tr>
  <tr>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display-box">&lt;display-box&gt;</a></td>
    <td>define whether an element generates display boxes at all</td>
    <td>display: contents;<br/>display: none;</td>
  </tr>
  <tr>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display-legacy">&lt;display-legacy&gt;</a></td>
    <td>used a single-keyword syntax for the display property, requiring separate keywords for block-level and inline-level variants of the same layout mode</td>
    <td>display: inline-block;<br/>display: inline-table;<br/>display: inline-flex;<br/>display: inline-grid;</td>
  </tr>
  </tbody>
</table>



### Display Characteristics

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="5%">Property</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#block-level">Block Level</a></td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#inline-elements">Inline Element</a></td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#inline-block">Inline-Block</a></td>
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
    <td><ul> <li> expand to fill the width of the parent container by default </li> <li> make width narrower and wrap, but not crop </li> <li>take the width of their parent</li> <li> centering - <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#block">"margin: auto;" </li> </ul></td>
    <td><ul> <li>width of the content of the element, plus any padding</li> <li> no width properties </li> <li> subject to CSS white-space settings </li> <li> centering - <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#inline">"text-align: center;"</a> </li> </ul></td>
    <td><ul> <li> adjusted to make room respect to width properties </li> </ul></td>
  </tr>
  <tr>
    <td>Height</td>
    <td><ul> <li>take on the height of all its children</li> <li> no vertical-align property</li> <li>take the height of their content </li> <li>centering - <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#inline-1">"vertical-align: center;" </a></li> </ul></td>
    <td><ul> <li>no height properties</li> <li> subject to vertical-align property </li> <li>line-height property</li> <li>centering - <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#inline-1">flexbox</a> </li></ul></td>
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


## Positioned Properties

### List of Positioned Properties

<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning">CSS Positioned Layout</a></caption>
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Property</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 20%">Possible Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>left, top, right, bottom</td>
    <td><ul> <li>adjust or set the position of an element</li> <li>determine the final location of positioned elements</li></ul></td>
    <td>&lt;length&gt;, &lt;percentage&gt;, auto</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/left">Left</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/top">Top</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/bottom">Bottom</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/right">Right</a>, <a href="https://www.w3.org/TR/CSS22/visuren.html#position-props">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#the-position-property"> Positioning </a> </td>
  </tr>
  <tr>
    <td>z-index</td>
    <td><ul><li>control overlapping - whether or not an element is in front of or behind other sibling positioned elements</li><li>apply to positioned elements, except for static</li><li>used to figure out which sibling is higher than another</li><li>The higher the number, the more "topmost" or "overlapping" the element will be.</li><li>relative between siblings, not any arbitrary elements</li></ul></td>
    <td>auto, &lt;integer&gt;</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#-z-index-">Z-Index</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/z-index">MDN</a></td>
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
    <td>static, relative, absolute, sticky, fixed</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">Position</a>, <a href="https://www.w3.org/TR/CSS22/visuren.html#choose-position">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#the-position-property">Positioning</a>, <a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#the-position-property">Concept</a></td>
  </tr>
  </tbody>
</table>


### Characteristics of Position Property

+ [Types of positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/position#Types_of_positioning)
  + __positioned element__: an element whose computed position value is either relative, absolute, fixed, or sticky
  + relatively positioned element
    + an element whose computed position value is relative
    + top and bottom properties: the vertical offset from its normal position
    + left and right properties: the horizontal offset
  + absolutely positioned element
    + an element whose computed position value is absolute or fixed
    + top, right, bottom, and left properties: offsets from the edges of the element's containing block
    + margins added to the offset
  + stickily positioned element
    + an element whose computed position value is sticky
    + treated as relatively positioned until its containing block crosses a specified threshold within its flow root

+ [Margin with psitioned values](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#margins-do-not-work-the-same)
  + static / relative:
    + used to adjust an element position
    + keeping neighboring siblings "away"
  + fixed
    + able to move the element
    + not move any siblings
  + general rule: if a positioning property is being used (like left), then the matching margin (margin-left) can also be used to additionally adjust the position of the element

+ [Opposite properties](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#opposite-properties-can-be-used-to-size-element)
  + preset dimensional properties (height and width): make design brittle and reduce its adaptability
  + fixed/absolute positioned + positioned properties (left, right):
    + leave the matching dimensional property (width) unspecified
    + grow or shrink based on the size of the browser window

+ [positioning properties](/WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#positioned-elements)
  + left, top, right, bottom, and z-index
  + used to influence the position of an element
  + Positioned values
    + static: no effect on any element (default positioned value)
    + fixed: positioned relative to the browser window
    + relative: as static, the "flowing text" model of layout is setting the initial position for the element (including margins and display)

+ [Relative position property](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#relative)
  + Items are moved independently of siblings.
    + positioning properties adjust the placement of the element independently of its siblings
    + `margin-top` instead of `top` to move the sibilings downward
  + Opposite positioning properties (like left and right) cannot be used simultaneously.
    + not using left and right properties simultaneously
    + not using top and bottom properties simultaneously
    + the CSS precedence rules determining the "winner" id both used (last order)
  + There are no automatic size adjustments.
    + block level elements take the width of their parent (when no width is specified)
    + using left or right margins on block level element, the browser adjust the width to fit
    + using relative & positioning properties: no adjustment applied

+ [Absolute position property](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#absolute)
  + ease and power is very seductive to many CSS newbies
  + not use it under any circumstances
  + taken out of the normal text "flow" that governs elements positioned statically or relatively
  + positioned by the left, top, right, and/or bottom properties
  + The size or position of siblings have no effect on an absolutely positioned element that has some positioning properties set (left, top, etc.).
  + caveats and trade-offs
    + Interpretation of positioning depends upon parent/grandparent elements being positioned elements.
    + Best practice: use both a horizontal and a vertical positioning property on every absolute element.
    + Absolutely positioned elements do not contribute to size of the parent.
    + Absolute positioned block level elements do not get the width of their parent.
    + Margins do not work the same.
    + Opposite properties can be used to size element.


<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">Position property</a></caption>
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 40%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Link</th>
  </tr></thead>
  <tbody>
  <tr>
    <td>static</td>
    <td><ul> <li>follow the "flowing text" model of layout </li> <li>influenced by margins, padding</li> <li>block level layout, inline or inline-block</li> <li>default value</li><li>margins used to adjust an element position and keep neighboring siblings "away"</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#static">Static</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html">Positioning</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">MDN</a></td>
  </tr>
  <tr>
    <td>fixed</td>
    <td><ul><li>respect the positioning properties (left, top, right, and bottom)</li><li>not scroll with the rest of the page</li><li>positioned against the window rectangle (aka the viewport)</li><li>not contribute to size of the parent</li><li>not get the width of their parent</li><li>determined by the values of top, right, bottom, and left</li><li>Best practice: use both a horizontal and a vertical positioning property on every fixed positioned element</li><li>margin able to move the element but not move any siblings</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#fixed">Fixed</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html">Positioning</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">MDN</a></td>
  </tr>
  <tr>
    <td>relative</td>
    <td><ul><li>exactly like static in that the "flowing text" model of layout is setting the initial position for the element (including margins and display) but move the named edge of the element from its initial position</li><li>positioned according to the normal flow of the document is positioned relative to its normal position, and then offset relative to itself based on the values of top, right, bottom, and left</li><li>margins used to adjust an element position and keep neighboring siblings "away"</li><li>Items are moved independently of siblings.</li><li>Opposite positioning properties (like left and right) cannot be used simultaneously.</li><li>no automatic size adjustments</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#relative">Relative</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html">Positioning</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">MDN</a></td>
  </tr>
  <tr>
    <td>absolute</td>
    <td><ul><li>RECOMMENDED: not use it under any circumstances</li><li>taken out of the normal text "flow" that governs elements positioned statically or relatively </li> <li>positioned by the left, top, right, and/or bottom properties </li> <li>relative to the closest positioned ancestor, if there is any; otherwise, it is placed relative to the initial containing block and its final position is determined by the values of top, right, bottom, and left</li></ul></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#absolute">Absolute</a>, <a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html">Positioning</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">MDN</a></td>
  </tr>
  <tr>
    <td>sticky</td>
    <td><ul><li>positioned corresponding to the normal flow of the document, and then offset relative to its closest ascending block-level, including table-related elements, according to the values of top, right, bottom, and left</td>
    <td><a href="https://www.htmlgoodies.com/html5/css/positioning-html-elements-using-css.html">Positioning</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">MDN</a></td>
  </tr>
  </tbody>
</table>





## The Flexible Box Layout

### Basic Concepts of flexbox

+ [Flexbox](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flexbox)
  + performing layout tasks like columnar layout or anything responsive requires coordinating multiple elements
  + flex container:
    + CSS properties that are applied to a parent element
    + handle laying out of its children
    + making the best use of the screen size available to children
    + still following the general guidelines laid down
  + flex items: CSS properties that are applied to the direct children of that parent

+ [minimum scenario for using flexbox](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#the-minimum)
  1. flex container: `display:flex;`
  2. flex items: `flex:1;`
  3. flex container (better): `flex-flow: row wrap;`

+ [Layout and Axes](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox#The_two_axes_of_flexbox)
  + __flex container__: set parent element w/ `display: flex`
  + __flex items__: the items being laid out as flexible boxes inside the flex container
  + __main axis__:
    + the axis running in the direction the flex items are being laid out in
    + __main start__ and __main end__: the start and end of main axis
  + __cross axis__:
    + the axis running perpendicular to the direction the flex items are being laid out in
    + __cross start__ and __cross end__:  start and end of cross axis

+ [Combinations of flex-flow and the Start and End Points](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#start-and-end)
  + Illustration of flexbox axes and start & end points for `flex-flow: row wrap;` setting
    <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
      <a href="https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox" ismap target="_blank">
        <img src="https://developer.mozilla.org/files/3739/flex_terms.png" style="margin: 0.1em;" alt="flexbox axes and points with flex-flow: row wrap;" title="Illustration of flexbox axes and points with flex-flow: row wrap;" width=450>
      </a>
    </div>

  + `Flex-flow` combinations
    + row wrap (above diagram)
    + row wrap-reverse
    + row-reverse wrap
    + row-reverse wrap-reverse
    + column wrap
    + column wrap-reverse
    + column-reverse wrap
    + column-reverse wrap-reverse
  + main axis for sizing, cross axis for alignment
  + properties control the main axis: 
    + how a flexbox container spaces out and positions flex items
    + list of properties: `flex`, `flex-grow`, `flex-shrink`, `flex-basis`, `justify-content`
  + properties control alignment: 
    + govern how a flex item might be aligned or positioned along the cross axis
    + list of properties: `align-content`, `align-items`, `align-self`
  + flexbox items incluence their sizes and position on main axis but only position on the across axis (except for coarse stretch option)
  + `flex-start` and `flex-end`:
    + refer to the "main start" and "main end" sides with justify-content property
    + refer to the "cross start" and "cross end" sides with flexbox align properties

+ [main axis defined by __flex-direction__](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox#The_main_axis)
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
  + ways to create a flex container all of the contained flex items
    + Items display in a row (the `flex-direction` property's default is `row`).
    + The items start from the start edge of the main axis.
    + The items do not stretch on the main dimension, but can shrink.
    + The items will stretch to fill the size of the cross axis.
    + The `flex-basis` property is set to `auto`.
    + The `flex-wrap `property is set to `nowrap`.
  + changing `flex-direction`:
    + change the direction that flex items display
    + values: row, row-reverse, column, column-reverse

+ [Multi-line flex containers with flex-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox#The_flex_container)
  + While flexbox is a one dimensional model, it is possible to cause our flex items to wrap onto multiple lines.
  + To cause wrapping behaviour add the property `flex-wrap` with a value of `wrap`.
  + guide to wrap flex items: [Mastering Wrapping of Flex Items](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Mastering_Wrapping_of_Flex_Items)

+ [Aligning Items in a Flex Container](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Aligning_Items_in_a_Flex_Container)
  + use the `align-items` property to align items on the cross axis
  + use `justify-content` to align the item on the main axis
  + Properties
    + `justify-content`: control alignment of all items on the main axis
    + `align-items`: control alignment of all items on the cross axis
    + `align-self`: control alignment of an individual flex item on the cross axis
    + `align-content`: control space between flex lines on the cross axis 

+ [flex-flow](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-flow)
  + lay out children both horizontally and vertically at the same time
  + an abbreviation that replaces two other flexbox container properties: `flex-direction` and `flex-wrap`
  + Syntax: `flex-flow: <flex-direction> <flex-wrap>;`

+ [Flex items](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flex-items)
  + the direct children of a flex container
  + exception: items with `position-fixed` or `position-absolute`
  + empty flex items are automatically removed from the flex container
  + interrelatted properties: `flex-grow`, `flex-shrin`k, and `flex-basis`
  + abbreviation: `flex: <flex-grow> <flex-shrink> <flex-basis>;`

+ [Utilizing flex-grow](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Controlling_Ratios_of_Flex_Items_Along_the_Main_Ax#Combining_flex-grow_and_flex-basis)
  + `flex: 1 1 auto;`:
    + auto sized as items without width settings
    + retain the max-content size of the items (the size of each item)
    + lay out the items with some free space (aggregated size smaller than teh container))
    + remant space evenly distributed for the items
    + items' final size not the same
  + `flex: 1 1 0`
    + basis = 0: all the space is up for grabs
    + grow factor (1): each get an equal amount of space distributed
    + items: equal width

+ [Utilizing flex-shrink](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Controlling_Ratios_of_Flex_Items_Along_the_Main_Ax#Combining_flex-shrink_and_flex-basis)
  + use as the total size of the items larger than the the flex container
  + min-content size: the size that items become if they take advantage of any soft wrapping opportunities available to them (according to the content of the item)
  + set the min-content floor of the items (never smaller than min-content)
  + tend to give you reasonable results

+ [Algorithm to decide flex item calculation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Controlling_Ratios_of_Flex_Items_Along_the_Main_Ax#Combining_flex-shrink_and_flex-basis)
  + What sets the base size of the item?
    1. `flex-basis: auto` & width set: based on the given width
    2. `flex-basis: auto` or `flex-basis: content`: based on the item's size
    3. `flex-basis` > 0: the size of the item
    4. `flex-basis` = 0: item size not considered for space-sharing calculation
  + Are there available aspace?
    1. total item size < container size: positive free space & `flex-grow` involved
    2. total item size > container size: negative free space & `flex-shrink` involved

+ [Best Practice](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flexbox-advice-and-best-practices)
  + the minimum use
  + Use variable dimensions on flex items instead of explicit ones
  + Do not overconstrain your flex items. Let the browser work for you.
  + Using flexbox instead of inline-block
  + Using flexbox for centering
  + AVOID `margin: auto` on flex items
  + keep simple

+ [Typical use cases of Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Typical_Use_Cases_of_Flexbox)
  + Navigation
    + space distributed outside the items
    + space distributed within the items
  + Spalit navigation
  + Center item
  + Car layout pushing footer down
  + Media objects
    + flippin the media object
  + Form controls

+ [Order](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#order)
  + determine the order in which the item appears in the flexbox
  + present the information in the flexbox layout independent of its order in the HTML itself
  + Syntax: `order: <integer>`


### Flexbox Property


<table table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em; margin-bottom: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout#CSS_Properties">Flexbox CSS Properties</a></caption>
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
    <td>&lt;flex-grow&gt;, &lt;flex-shrink&gt;, &lt;flex-basis&gt;, init, auto, none</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex">MDN</a>, <a href="../Programming/WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flex-property">Flex</a></td>
  </tr>
  <tr>
    <td>flex-grow</td>
    <td><ul><li>set how much of the remaining space, related to its siblings, in the flex container should be assigned to that item (the flex grow factor)</li><li>remaining space: the size of the flex container minus the size of all flex items together</li><li>sibling items: <ul><li>all items with the same share of remaining space with the same grow factor</li><li>distributed according tot he ratio defined by the different flex grow factors</li><li>e.g., item with 2 will be twice larger than the the items with 1</li><li>space proportional to the aggregated values with the assigned space</li><li>flex-grow=0: prevent the flex item from growing, as the original item space</li></ul><li>determine how much the flex item will grow relative to the rest of the flex items in the flex container when the positive free space is distributed</li></ul></td>
    <td>&lt;number&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flex-grow">Grow</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Controlling_Ratios_of_Flex_Items_Along_the_Main_Ax#The_flex-grow_property">Example</a></td>
  </tr>
  <tr>
    <td>flex-shrink</td>
    <td><ul><li>set the flex shrink factor of a flex item</li><li>the opposite of flex-grow</li><li>compared to its sibling flex-shrink values</li><li>only occur in the situation where the flex-container might need some space from its children</li></ul></td>
    <td>&lt;number&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flex-shrink">Shrink</a></td>
  </tr>
  <tr>
    <td>flex-basis</td>
    <td><ul><li>set the initial main size of a flex item</li><li>used instead of the sizing properties on a flex item</li><li>gorvern the withd with firection as row or row-reverse</li><li>govern the height with direction as column or column-reverse</li><li>specify the initial size of the flex item before any space distribution happens</li><li>innitial value: auto</li><li></li></ul></td>
    <td>&lt;'width'&gt; (auto, &lt;length&gt;, &lt;percentag&gt;), content (fill, max-xontent, min-content, fit-content)</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flex-basis">Basis</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Controlling_Ratios_of_Flex_Items_Along_the_Main_Ax#The_flex-basis_property">Example</a></td>
  </tr>
  <tr>
    <td>flex-flow</td>
    <td>a shorthand property for <strong>flex-direction</strong> and <strong>flex-wrap</strong> properties</td>
    <td>nowrap, wrap, wrap-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-flow">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flex-flow">Flow</a></td>
  </tr>
  <tr>
    <td>flex-direction</td>
    <td>>set how flex items placed in the flex container defining the main axis and the direction (normal or reversed)</td>
    <td>row, row-reverse, column, column-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flex-flow">Direction</a></td>
  </tr>
  <tr>
    <td>flex-wrap</td>
    <td>set whether flex items are forced onto one line or can wrap onto multiple lines</td>
    <td>nowrap, wrap, wrap-reverse</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flex-flow">Wrap</a></td>
  </tr>
  </tr>
  <tr>
    <td>flex-basis</td>
    <td><ul><li>set the initial main size of a flex item</li><li>content: automatic sizing, based on the flex item’s content</li></ul></td>
    <td>&lt;width&gt;, content</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#flex-container">Lecture</a></td>
  </tr>
  </tbody>
</table>


### Alignment Properties


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="top" width=100%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout#Alignment_Properties">Alignment Properties</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Property</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:50%;">Value</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td valign="top">justify-content</td>
    <td valign="top"><ul><li>define how the browser distributes space between and around content items along the <span style="color: #ff6000; font-weight: bold;">main-axis</span> of a flex container, and the inline axis of a grid container</li><li>alignment done after the lengths and auto margins applied</li><li>flex-direction = row-reverse: reverse the appearances of flex-start and flex-end</li><li>flex-direction = column: <ul><li>no extra vertical space to distribute with block level element</li><li>flex-start, flex-end, center, space-between & space-around options are identical</li><li>exception:  larger flex contailer height defined</li></ul></li></ul></td>
    <td rowspan="2"><ul><li><span style="color: #ff6000; font-weight: bold;">start</span>: packed flush to each other toward the start edge of the alignment container</li><li><span style="color: #ff6000; font-weight: bold;">end</span>: packed flush to each other toward the end edge of the alignment container</li><li><span style="color: #ff6000; font-weight: bold;">flex-start</span>: <ul><li>packed flush to each other toward the edge of the alignment container depending on the flex container's main-start side</li><li>only applies to flex layout items</li><li>items not children of a flex container act as start</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">flex-end</span>: <ul><li>packed flush to each other toward the edge of the alignment container depending on the flex container's main-end side</li><li>only applies to flex layout items</li><li>items not children of a flex container act as end</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">center</span>: packed flush to each other toward the center of the alignment container</li><li><span style="color: #ff6000; font-weight: bold;">left</span> (justify only): <ul><li>packed flush to each other toward the left edge of the alignment container</li><li>if not parallel with the inline axis, behave like start</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">right</span> (justify only): <ul><li>packed flush to each other toward the right edge of the alignment container</li><li>if not parallel with the inline axis, behave like start</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">normal</span>: <ul><li>packed in their default position as if no justify-content value was set</li><li>behave as stretch in grid and flex containers</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">baseline, first baseline, last baselinbe</span> (justify only): <ul><li>align the alignment baseline of the box’s first or last baseline set with the corresponding baseline in the shared first or last baseline set of all the boxes in its baseline-sharing group</li><li>fallback alignment for first baseline is start, the one for last baseline is end</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">space-between</span>: <ul><li>evenly distributed within the alignment container along the main axis</li><li>same spacing between each pair of adjacent items</li><li>first item is flush with the main-start edge; the last item is flush with the main-end edge</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">space-around</span>: <ul><li>evenly distributed within the alignment container along the main axis</li><li>same spacing between each pair of adjacent items</li><li>empty space before the first and after the last item equals half of the space between each pair of adjacent items</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">space-evenly</span>: <ul><li>evenly distributed within the alignment container along the main axis</li><li>same spacing between each pair of adjacent items, the main-start edge and the first item, and the main-end edge and the last item</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">stretch</span>: <ul><li>total size of items < size of alignment container: auto-sized items have their size increased equally (not proportionally), while still respecting the constraints imposed by max-height/max-width (or equivalent functionality)</li><li>combined size exactly fills the alignment container along the main axis</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">safe</span>: if the item overflows the alignment container causing data loss, then behave as start</li><li><span style="color: #ff6000; font-weight: bold;">unsafe</span>: regardless of the relative sizes of the item and alignment container, and regardless of whether overflow which causes data loss, floow the gieven align value</li><br/><li><span style="color: #ff6000; font-weight: bold;">baseline, first baseline, last baselinbe</span> (align only): <br/><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Typography_Line_Terms.svg/410px-Typography_Line_Terms.svg.png" style="margin: 0.5em; margin-left: 4em;" alt="vertical baseline" title="vertical baseline" width=350><br/><ul><li>specify participation in first- or last-baseline alignment: align the alignment baseline of the box’s first or last baseline set with the corresponding baseline in the shared first or last baseline set of all the boxes in its baseline-sharing group</li><li>fallback alignment for first baseline is start, the one for last baseline is end</li></ul></li></ul></td>
    <td valign="top"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#justify-content">Justify</a></td>
  </tr>
  <tr>
    <td valign="top">align-content</td>
    <td valign="top"><ul><li>set the distribution of space between and around content items along a flexbox's <span style="color: #ff6000; font-weight: bold;">cross-axis</span> or a grid's <span style="color: #ff6000; font-weight: bold;">block axis</span></li><li>no effect on single line flex containers, i.e., ones with flex-wrap: nowrap;</li></ul></td>
    <td valign="top"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/align-content">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#align-content">Align</a></td>
  </tr>
  <tr>
    <td valign="top">justify-self</td>
    <td valign="top"><ul><li>set the way a box is justified inside its alignment container along the appropriate axis</li><li>layout mode effects: <ul><li>block-level layouts: align an item inside its containing block on the inline axis</li><li>absolutely-positioned elements: align an item inside its containing block on the inline axis, accounting for the offset values of top, left, bottom, and right</li><li>table cell layouts: ignored</li><li>flexbox layouts: ignored</li><li>grid layouts: align an item inside its grid area on the inline axis</li></ul></li><li>forms: <ul><li>basic keywords: normal, auto, or stretch</li><li>baseline alignment: baseline, first baseline, or last baseline</li><li>positional alignment: <ul><li>center, start, end, flex-start, flex-end, self-start, self-end, left, or right</li><li>(optional) safe or unsafe</li></ul></li></ul></ul></td>
    <td valign="top" rowspan="2"><ul><li><span style="color: #ff6000; font-weight: bold;">auto</span>: compute to the parent's align-items value</li><li><span style="color: #ff6000; font-weight: bold;">normal</span>: <ul><li>absolutely-positioned layouts: behave like start on replaced absolutely-positioned boxes, and as stretch on all other absolutely-positioned boxes</li><li>static position of absolutely-positioned layouts: behave as stretch</li><li>flex items: behave as stretch</li><li>grid items: behave similar to stretch, except for boxes with an aspect ratio or an intrinsic sizes where it behaves like start</li><li>NOT apply to block-level boxes, and to table cells</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">start</span> (justify only): packed flush to each other toward the start edge of the alignment container in the appropriate axis</li><li><span style="color: #ff6000; font-weight: bold;">end</span> (justify only): packed flush to each other toward the end edge of the alignment container in the appropriate axis</li><li><span style="color: #ff6000; font-weight: bold;">self-start</span>: flush with the edge of the alignment container corresponding to the item's start side</li><li><span style="color: #ff6000; font-weight: bold;">self-end</span>: flush with the edge of the alignment container corresponding to the item's end side</li><li><span style="color: #ff6000; font-weight: bold;">flex-start</span>: cross-start margin edge of the flex item flushed with the cross-start edge of the line</li><li><span style="color: #ff6000; font-weight: bold;">flex-end</span>: cross-end margin edge of the flex item is flushed with the cross-end edge of the line</li><li><span style="color: #ff6000; font-weight: bold;">center</span>: <ul><li>margin box centered within the line on the cross-axis</li><li>cross-size of the item > the flex container: overflow equally in both directions</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">baseline, first baseline, last baseline</span>: <ul><li>specify participation in first- or last-baseline alignment: aligns the alignment baseline of the box’s first or last baseline set with the corresponding baseline in the shared first or last baseline set of all the boxes in its baseline-sharing group</li><li>fallback alignment: first baseline is start, last baseline is end</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">stretch</span>: <ul><li>total size of items < size of alignment container: auto-sized items have their size increased equally (not proportionally), while still respecting the constraints imposed by max-height/max-width (or equivalent functionality)</li><li>combined size exactly fills the alignment container along the main axis</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">safe</span>: if the item overflows the alignment container causing data loss, then behave as start</li><li><span style="color: #ff6000; font-weight: bold;">unsafe</span>: regardless of the relative sizes of the item and alignment container, and regardless of whether overflow which causes data loss, floow the gieven align value</li></ul></td>
    <td valign="top"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/justify-self">MDN</a></td>
  </tr>
  <tr>
    <td valign="top">align-self</td>
    <td valign="top"><ul><li>override a grid or flex item's align-items value</li><li>Flexbox: align the item on the cross axis</li><li>Grid: align the item inside the grid area</li><li>NOT apply to block-level boxes, or to table cells</li><li>ignore if a flexbox item's cross-axis margin is auto</li></ul></td>
    <td valign="top"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/align-self">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#align-self">Self</a></td>
  </tr>
  <tr>
    <td valign="top">justify-items</td>
    <td valign="top"><ul><li>define the default justify-self for all items of the box, giving them all a default way of justifying each box along the appropriate axis</li><li>layout mode effects: <ul><li>block-level layouts: align an item inside its containing block on the inline axis</li><li>absolutely-positioned elements: align an item inside its containing block on the inline axis, accounting for the offset values of top, left, bottom, and right</li><li>table cell layouts: ignored</li><li>flexbox layouts: ignored</li><li>grid layouts: align an item inside its grid area on the inline axis</li></ul></li><li>forms: <ul><li>basic keywords: normal, auto, or stretch</li><li>baseline alignment: baseline, first baseline, or last baseline</li><li>positional alignment: <ul><li>center, start, end, flex-start, flex-end, self-start, self-end, left, or right</li><li>(optional) safe or unsafe</li><li>legacy alignment: legacy, followed by left or right</li></ul></li></ul></td>
    <td valign="top" rowspan="2"><ul><li><span style="color: #ff6000; font-weight: bold;">auto</span> (justify only): compute to the parent's align-items value</li><li><span style="color: #ff6000; font-weight: bold;">normal</span>: <ul><li>absolutely-positioned layouts: behave like start on replaced absolutely-positioned boxes, and as stretch on all other absolutely-positioned boxes</li><li>static position of absolutely-positioned layouts: behave as stretch</li><li>flex items: behave as stretch</li><li>grid items: behave similar to stretch, except for boxes with an aspect ratio or an intrinsic sizes where it behaves like start</li><li>NOT apply to block-level boxes, and to table cells</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">start</span> (justify only): packed flush to each other toward the start edge of the alignment container in the appropriate axis</li><li><span style="color: #ff6000; font-weight: bold;">end</span> (justify only): packed flush to each other toward the end edge of the alignment container in the appropriate axis</li><li><span style="color: #ff6000; font-weight: bold;">self-start</span>: flush with the edge of the alignment container corresponding to the item's start side</li><li><span style="color: #ff6000; font-weight: bold;">self-end</span>: flush with the edge of the alignment container corresponding to the item's end side</li><li><span style="color: #ff6000; font-weight: bold;">flex-start</span>: cross-start margin edge of the flex item flushed with the cross-start edge of the line</li><li><span style="color: #ff6000; font-weight: bold;">flex-end</span>: cross-end margin edge of the flex item is flushed with the cross-end edge of the line</li><li><span style="color: #ff6000; font-weight: bold;">center</span>: <ul><li>margin box centered within the line on the cross-axis</li><li>cross-size of the item > the flex container: overflow equally in both directions</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">left</span> (justify only): <ul><li>packed flush to each other toward the left edge of the alignment container</li><li>if not parallel with the inline axis, behave like start</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">right</span> (justify only): <ul><li>packed flush to each other toward the right edge of the alignment container</li><li>if not parallel with the inline axis, behave like start</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">baseline, first baseline, last baseline</span>: <ul><li>specify participation in first- or last-baseline alignment: aligns the alignment baseline of the box’s first or last baseline set with the corresponding baseline in the shared first or last baseline set of all the boxes in its baseline-sharing group</li><li>fallback alignment: first baseline is start, last baseline is end</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">stretch</span>: <ul><li>total size of items < size of alignment container: auto-sized items have their size increased equally (not proportionally), while still respecting the constraints imposed by max-height/max-width (or equivalent functionality)</li><li>combined size exactly fills the alignment container along the main axis</li></ul></li><li><span style="color: #ff6000; font-weight: bold;">safe</span>: if the item overflows the alignment container causing data loss, then behave as start</li><li><span style="color: #ff6000; font-weight: bold;">unsafe</span>: regardless of the relative sizes of the item and alignment container, and regardless of whether overflow which causes data loss, floow the gieven align value</li><li><span style="color: #ff6000; font-weight: bold;">legacy</span> (justify only): <ul><li>inherited by the box descendants</li><li>if descendant with 'justify-self: auto' value, not considered by the descend</li><li>only descend with only the left, right, or center associated to it</li></ul></li></ul></td>
    <td valign="top"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/justify-items">MDN</a></td>
  </tr>
  <tr>
    <td valign="top">align-items</td>
    <td valign="top"><ul><li>set the align-self value on all direct children as a group</li><li>flexbox: control the alignment of items on the Cross Axis</li><li>Grid Layout: controls the alignment of items on the Block Axis within their grid area</li></ul></td>
    <td valign="top"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/align-items">MDN</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#align-items">Items</a></td>
  </tr>
  <tr>
    <td  valign="top">place-content</td>
    <td  valign="top"><ul><li>a shorthand for align-content and justify-content</li><li>used in any layout method which utilizes both of these alignment values</li></ul></td>
    <td  valign="top">start<br/>flex-start<br/>flex-end<br/>center<br/>left<br/>right<br/>space-between<br/>baseline<br/>first baseline, last baseline, space-around<br/>space evenly<br/>stretch</td>
    <td  valign="top"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/place-content">MDN</a></td>
  </tr>
  <tr>
    <td  valign="top">place-self</td>
    <td  valign="top"><ul><li>a shorthand for align-self and justify-self</li><li>1st value for align-self; 2nd vlue for justify-self</li></ul></td>
    <td  valign="top">auto<br/>normal<br/>self-start<br/>self-end<br/>flex-start<br/>flex-end<br/>baseline, first baseline, last baseline<br/>stretch</td>
    <td  valign="top"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/place-self">MDN</a></td>
  </tr>
  <tr>
    <td  valign="top">place-items</td>
    <td  valign="top"><ul><li>a shorthand for align-items and justify-items</li><li>1st value for align-items; 2nd vlue for justify-items</li></ul></td>
    <td  valign="top">auto<br/>normal<br/>start<br/>end<br/>flex-start<br/>flex-end<br/>self-start<br/>self-end<br/>center<br/>left<br/>right<br/>baseline, first baseline, last baeline<br/>stretch</td>
    <td  valign="top"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/place-items">MDN</a></td>
  </tr>
  </tbody>
</table>


## CSS Grid Layout

### Concepts of CSS Grid

+ [CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
  + dividing a page into major regions or defining the relationship in terms of size, position, and layer, between parts of a control built from HTML primitives
  + enables an author to align elements into columns and rows
  + able to be used to lay out major page areas or small user interface elements
  + a grid-based layout system, with rows and columns, making it easier to design web pages without having to use floats and positioning
  + Display property: `display: grid;` or `display: inline-grid;`

+ [Grid features](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#What_is_a_grid)
  + fixed an flexible track sizes
    + fixed track sizes: specify pixel which fits to the layout desired
    + flexible sizes: percentages or `fr` unit
  + item placement
    + place items into a precise location on the grid using line numbers, names or by targeting an area of the grid
    + contain an algorithm to control the placement of items not given an explicit position on the grid
  + creation of additional tracks to hold content
    + define an explicit grid with grid layout
    + flexible enough to add additional rows and columns when needed
  + alignment control: control how the items align
  + control of overlapping content
    + more than one item able to be placed into a grid cell or area
    + control with `z-index` property

+ [The Grid container](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#The_Grid_container)
  + Declare: `display: grid;` or `display: inline-grid;`
  + grid items: all direct children

+ [Grid Tracks](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#Grid_Tracks)
  + the space between any two lines on the grid
  + define rows and columns (explicit): `grid-template-columns` and `grid-template-rows`
  + defined using any length unit
  + `fr` unit: a fraction of the available space in the grid container
    + `grid-template-columns: 1fr 1fr 1fr;`: equally divided into three columns
    + `grid-template-columns: 2fr 1fr 1fr;`: divided into 4 portiona while the first column occupies 2 portions
    + `grid-template-columns: 500px 1fr 1fr;`: first column with 500px while the last two columns evenly share the remaint
  + `repeat()` notation
    + repeat all or a section of the track listing
    + e..g., `grid-template-columns: repeat(3, 1fr);`; `grid-template-columns: 20px repeat(6, 1fr) 20px;`; `grid-template-columns: repeat(5, 1fr 2fr);`
  + implicit grid
    + rows creat on its own
    + defined with `grid-auto-rows` and `grid-auto-columns`
  + track sizing
    + minimum size given by explicit grid or automatically created rows or columns
    + `minmax()` notation
      + given the minmun and maximum values
      + e.g., `grid-auto-rows: minmax(100px, auto);`

+ [Grid lines](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#Grid_lines)
  + define a grid defined the grid tracks, not the actual lines
  + numbering the lines to use when positioning items
  + numbered according to the writing mode of the document: left-to-right language or right-to-left language
  + Positioning items against lines
    + properties: `grid-column-start`, `grid-column-end`, `grid-row-start` and `grid-row-end`
    + e.g., `grid-column-start: 1; grid-column-end: 4; grid-row-start: 1; grid-row-end: 3;`

+ [Grid Cells](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#Grid_cells): the smallest unit on a grid, like a table cell

+ [Grid areas](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#Grid_areas): 
  + rectangular are to place items which can span one or more cells both by row or by column
  + L-shaped area not allowed

+ [Gutters or alleys](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#Gutters)
  + space between grid cells
  + created using the `column-gap` and `row-gap` properties, or the shorthand `gap`
  + e.g., `row-gap: 1em;`

+ [Nesting grids](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#Nesting_grids)
  + A grid item as a grid container
  + defined as a grid container 
  + `grid-gap` not inherited
  + subgrid
    + creating nested grids that use the track definition of the parent grid
    + e.g., `grid-template-columns: subgrid;`

+ [Layering items](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#Layering_items_with_z-index)
  + grid items can occupy the same cell
  + later items cover the previous ones
  + `z-index`: controlling the order

+ [CSS Grid](../WebDev/Frontend-W3C/1-HTML5CSSFund/06-Layout.md#css-grid)
  + Grid arranges in two dimensions, while Flexbox lays out in one. 
  + a CSS module that defines a two-dimensional grid-based layout system, optimized for user interface design
  + children of an element (the ‘grid container’) can be positioned into arbitrary slots in a predefined flexible or fixed-size layout grid
  + split the box that makes up an element into many individual ‘slots’, arranged in a matrix, and separated from each other by (invisible) horizontal and vertical lines

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <a href="https://webkit.org/blog/7434/css-grid-layout-a-new-layout-module-for-the-web/" ismap target="_blank">
      <img src="https://webkit.org/wp-content/uploads/grid-concepts.svg" style="margin: 0.1em;" alt="concepts of CSS Grid layout" title="Definitions of CSS Grid Layout" width=350>
    </a>
  </div>


### List of CSS Grid Properties


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout#CSS_properties">Grid Properties</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Property</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Value</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>grid-template-columns</td>
    <td>defines the line names and track sizing functions of the grid columns</td>
    <td rowspan="2">none<br/>&lt;length&gt;<br/>&lt;percentage&gt;<br/>&lt;flex&gt;<br/>max-content<br/>min-content<br/>minmax(min, max)<br/>auto<br/>fit-content(args)<br/>repeat(args)</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-columns">MDN</a></td>
  </tr>
  <tr>
    <td>grid-template-rows</td>
    <td>define the line names and track sizing functions of the grid rows</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-rows">MDN</a></td>
  </tr>
  <tr>
    <td>grid-template-areas</td>
    <td>specify named grid areas</td>
    <td>none<br/>&lt;string&gt;+</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas">MDN</a></td>
  </tr>
  <tr>
    <td>grid-template</td>
    <td>a shorthand property for defining grid columns, rows, and areas</td>
    <td>none<br/>&lt;'grid-template-rows'&gt; / &lt;'grid-template-columns'&gt;<br/>[ &lt;line-names&gt;? &lt;string&gt; &lt;track-size&gt;? &lt;line-names&gt;? ]+ [ / &lt;explicit-track-list&gt; ]?</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template">MDN</a></td>
  </tr>
  <tr>
    <td>grid-auto-columns</td>
    <td>specify the size of an implicitly-created grid column track</td>
    <td rowspan="2">&lt;length&gt;<br/>&lt;percentage&gt;<br/>&lt;flex&gt;<br/>max-content<br/>min-content<br/>minmax(min, max)<br/>fit-content(args)<br/>auto</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-columns">MDN</a></td>
  </tr>
  <tr>
    <td>grid-auto-rows</td>
    <td>specify the size of an implicitly-created grid row track</td>
    <td><a href="">MDN</a></td>
  </tr>
  <tr>
    <td>grid-auto-flow</td>
    <td><ul><li>control how the auto-placement algorithm works</li><li>specifying exactly how auto-placed items get flowed into the grid</li></ul></td>
    <td>roe<br/>column<br/>dense</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-flow">MDN</a></td>
  </tr>
  <tr>
    <td>grid</td>
    <td>a shorthand property that sets all of the explicit grid properties ('grid-template-rows', 'grid-template-columns', and 'grid-template-areas'), and all the implicit grid properties ('grid-auto-rows', 'grid-auto-columns', and 'grid-auto-flow'), in a single declaration</td>
    <td>&lt;'grid-template'&gt;<br/>&lt;'grid-template-rows'&gt; / [ auto-flow && dense? ] &lt;'grid-auto-columns'&gt;?<br/>[ auto-flow && dense? ] &lt;'grid-auto-rows'&gt;? / &lt;'grid-template-columns'&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid">MDN</a></td>
  </tr>
  <tr>
    <td>grid-row-start</td>
    <td>specify a grid item’s start position within the grid row by contributing a line, a span, or nothing (automatic) to its grid placement, thereby specifying the inline-start edge of its grid area</td>
    <td rowspan="3">auto<br/>&lt;custom-ident&gt;<br/>&lt;integer&gt; && &lt;custom-ident&gt;?<br/>span && [ &lt;integer&gt; || &lt;custom-ident&gt; ]</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-start">MDN</a></td>
  </tr>
  <tr>
    <td>grid-row-end</td>
    <td>specify a grid item’s end position within the grid row by contributing a line, a span, or nothing (automatic) to its grid placement, thereby specifying the inline-end edge of its grid area</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-end">MDN</a></td>
  </tr>
  <tr>
    <td>grid-row</td>
    <td>a shorthand property for 'grid-row-start' and 'grid-row-end specifying' a grid item’s size and location within the grid row by contributing a line, a span, or nothing (automatic) to its grid placement, thereby specifying the 'inline-start' and 'inline-end edge' of its grid area</td>
    <td><a href="">MDN</a></td>
  </tr>
  <tr>
    <td>grid-column-start</td>
    <td><ul><li>specify a grid item’s start position within the grid column by contributing a line, a span, or nothing (automatic) to its grid placement</li><li>define the block-start edge of the grid area</li></ul></td>
    <td rowspan="3">auto<br/>&lt;custom-ident&gt;<br/>&lt;integer&gt; && &lt;custom-ident&gt;?<br/>span && [ &lt;integer&gt; || &lt;custom-ident&gt; ]</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column-start">MDN</a></td>
  </tr>
  <tr>
    <td>grid-column-end</td>
    <td>specify a grid item’s end position within the grid column by contributing a line, a span, or nothing (automatic) to its grid placement, thereby specifying the block-end edge of its grid area</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column-end">MDN</a></td>
  </tr>
  <tr>
    <td>grid-column</td>
    <td>a shorthand property for grid-column-start and grid-column-end specifying a grid item's size and location within the grid column by contributing a line, a span, or nothing (automatic) to its grid placement, thereby specifying the inline-start and inline-end edge of its grid area</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column">MDN</a></td>
  </tr>
  <tr>
    <td>grid-area</td>
    <td>a shorthand property for grid-row-start, grid-column-start, grid-row-end and grid-column-end, specifying a grid item’s size and location within the grid by contributing a line, a span, or nothing (automatic) to its grid placement, thereby specifying the edges of its grid area</td>
    <td>auto<br/>&lt;custom-ident&gt;<br/>&lt;integer&gt; && &lt;custom-ident&gt;?<br/>span && [ &lt;integer&gt; || &lt;custom-ident&gt; ]</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/grid-area">MDN</a></td>
  </tr>
  <tr>
    <td>row-gap</td>
    <td>set the size of the gap (gutter) between an element's grid rows</td>
    <td>&lt;length-percentage&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/row-gap">MDN</a></td>
  </tr>
  <tr>
    <td>column-gap</td>
    <td>set the size of the gap (gutter) between an element's columns</td>
    <td>normal<br/>&lt;length&gt;<br/>&lt;percentage&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/column-gap">MDN</a></td>
  </tr>
  <tr>
    <td>gap</td>
    <td>a shorthand for 'row-gap' and 'column-gap'</td>
    <td>&lt;length&gt;<br/>&lt;percentage&gt;</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/gap">MDN</a></td>
  </tr>
  </tbody>
</table>


