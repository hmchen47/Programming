# Cascading Style Sheet (CSS)


## General Information

### [CSS design principles(CSS 2.2)][001]

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


### [Effective Use of Style Sheets][002]

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


### [CSS Best Practice][056]

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


### Tools

+ [CSS Validator][000]

+ [CSS Zen Garden][003]

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


### [CSS Syntax][004]

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


### Comment

+ Comments
  + begin with /* and must end with */
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



### CSS Values and Units

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
  + [&lt;color&gt;]()
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



<!-- A version based on W3C Specification

+ [Integers and real numbers](https://www.w3.org/TR/CSS22/syndata.html#numbers)
  + Real numbers and Integers: decimal notation only
  + &lt;integer&gt; : one or more digits "0" to "9"
  + &lt;number&gt; : either an &lt;integer&gt; or zero or more digits followed by a dot (.) followed by one or more digits
  + preceded by a "-" or "+" to indicate the sign
  + '-0' = 0: not a negative number

+ [Lrngths](https://www.w3.org/TR/CSS22/syndata.html#length-units)
  + refer to distance measurements
  + &gt;length&lt; : a &lt;number&gt; (with or without a decimal point) immediately followed by a unit identifier (e.g., px, em, etc.)
  + negative length values
    + allowed for some properties
    + converted to the nearest value if not supported
  + Relative length units
    + specify a length relative to another length property
    + more easily scale from one output environment to another
    + <span style="font-weight: bold; color: #ff6000;">em</span>: the 'font-size' of the relevant font
      + equal to the computed value of the 'font-size' property of the element on which it is used
      + EXCEPTIOn: when the value of the 'font-size' property itself refers to the font size of the parent element
      + used for vertical or horizontal measurement
    + <span style="font-weight: bold; color: #ff6000;">ex</span> : the 'x-height' of the relevant font
      + defined by the element's first available font
      + often equal to the height of the lowercase "x"
      + EXCEPTIOn: when the value of the 'font-size' property itself refers to the 'ex' of the parent element
  + Absolute length units
    + <span style="font-weight: bold; color: #ff6000;">in</span>: inches — 1in is equal to 2.54cm.
    + <span style="font-weight: bold; color: #ff6000;">cm</span>: centimeters
    + <span style="font-weight: bold; color: #ff6000;">mm</span>: millimeters
    + <span style="font-weight: bold; color: #ff6000;">pt</span>: points — the points used by CSS are equal to 1/72nd of 1in.
    + <span style="font-weight: bold; color: #ff6000;">pc</span>: picas — 1pc is equal to 12pt.
    + <span style="font-weight: bold; color: #ff6000;">px</span>: pixel units — 1px is equal to 0.75pt.


+ [Percentages](https://www.w3.org/TR/CSS22/syndata.html#percentage-units)
  + a &lt;number&gt; immediately followed by '%'
  + always relative to another value
  + be that of another property for the same element, a property for an ancestor element, or a value of the formatting context
  + set for a property of the root element: percentage times the initial value of that property

+ [URLs and URIs](https://www.w3.org/TR/CSS22/syndata.html#uri)
  + Uniform Resource Identifiers
  + used to designate URIs in property values

+ [Counters](https://www.w3.org/TR/CSS22/syndata.html#counter)
  + denoted by case-sensitive identifiers
  + 'counter(&lt;identifier&gt;)' or 'counter(&lt;identifier&gt;, &lt;'list-style-type'&gt;)': the value of a counter
  + 'counters(&lt;identifier&gt;, &lt;string&gt;)' or 'counters(&lt;identifier&gt;, &lt;string&gt;, &lt;'list-style-type'&gt;)': a sequence of nested counters of the same name
  + optional white space separating the tokens

+ [Colors](https://www.w3.org/TR/CSS22/syndata.html#color-units)
  + A &lt;color&gt; is either a keyword or a numerical RGB specification.
  + color keywords: aqua, black, blue, fuchsia, gray, green, lime, maroon, navy, olive, orange, purple, red, silver, teal, white, and yellow
  + The RGB color model
    + used in numerical color specifications
    + hexadecimal notation: a '#' immediately followed by either three or six hexadecimal characters; e.g., #f60 (#rgb) or  #ff66000 (#rrggbb)
    + functional notation: 'rgb(x, y, z)', where x, y, x in [0, 255] or [0, 100%]; e.g, rgb(255,0,0) or rgb(100%, 0%, 0%)

    <div style="width: 25em; height: 20em; margin: 1em auto; font-family: Verdana,sans-serif; font-size: 12px;" id="TanteksColorDiagram20020613">
    <div style="height: 5em;">
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: maroon; color:white"><span style="font-weight: bold;">maroon</span> #800000
    </span><span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: red"><span style="font-weight: bold;">red</span> #ff0000
    </span><span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: orange"><span style="font-weight: bold;">orange</span> #ffA500
    </span><span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: yellow"><span style="font-weight: bold;">yellow</span> #ffff00
    </span><span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: olive;color:white"><span style="font-weight: bold;">olive</span> #808000</span>
    </div>
    <div style="height: 5em;">
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: purple;color:white"><span style="font-weight: bold;">purple</span> #800080</span>
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: fuchsia"><span style="font-weight: bold;">fuchsia</span> #ff00ff</span>
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: white"><span style="font-weight: bold;">white</span> #ffffff</span>
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: lime"><span style="font-weight: bold;">lime</span> #00ff00</span>
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: green;color:white"><span style="font-weight: bold;">green</span> #008000</span>
    </div>
    <div style="height: 5em; padding:0 2.5em">
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: navy;color:white"><span style="font-weight: bold;">navy</span> #000080</span>
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: blue"><span style="font-weight: bold;">blue</span> #0000ff</span>
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: aqua"><span style="font-weight: bold;">aqua</span> #00ffff</span>
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background: teal;color:white"><span style="font-weight: bold;">teal</span> #008080</span>
    </div>
    <div style="height: 5em; padding:0 5em">
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background:black;color:white"><span style="font-weight: bold;">black</span> #000000</span>
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background:silver"><span style="font-weight: bold;">silver</span> #c0c0c0</span>
    <span style="float: left; width: 5em; height: 3em; text-align: center; padding: 1.2em 0 .8em; background:gray;color:white"><span style="font-weight: bold;">gray</span> #808080</span>
    </div>
    </div>

+ [Strings](https://www.w3.org/TR/CSS22/syndata.html#strings)
  + either be written with double quotes or with single quotes
  + double quotes cannot occur inside double quotes, unless escaped (e.g., as '\"' or as '\22')
  + e.g., "this is a 'string'" = "this is a \"string\"" = 'this is a "string"' = 'this is a \'string\''


<table  table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=70%>
  <caption style="font-size: 1.5em;"><a href="url">Measurement Units</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 5%;">Unit</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 20%;">Specification</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 5%">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td><code>px</code></a></td>
    <td>pixel, a single dot on the screen</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#px">Unit</a></td>
  </tr>
  <tr>
    <td><code>em</code></a></td>
    <td>vertical dimensions, height of capital letter in the _parent_ context</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#em">Unit</a></td>
  </tr>
  <tr>
    <td><code>rem</code></a></td>
    <td>vertical dimensions, size relative to the <em>root</em></td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#rem">Unit</a></td>
  </tr>
  <tr>
    <td><code>%</code></a></td>
    <td>relative to the <em>parent</em> dimension</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#-">Unit</a></td>
  </tr>
  <tr>
    <td><code>vh</code></a></td>
    <td>viewport height, percentage of the screen</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#vh-vw">Unit</a></td>
  </tr>
  <tr>
    <td><code>vw</code></a></td>
    <td>viewport width, percentage of the screen</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#vh-vw">Unit</a></td>
  </tr>
  </tbody>
</table>

-->

#### Relative Length

<br/>
<table  table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=60%>
  <caption style="font-size: 1.5em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Dimensions">Relative Length Units</a></caption>
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


#### Absolute Length

<table  table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=60%>
  <caption style="font-size: 1.5em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Dimensions">Absolute Length Units</a></caption>
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



#### Image Related Properties

<table  table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=90%>
  <caption style="font-size: 1.5em;"><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units#Dimensions">Relative Length Units</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 15%;">Kind of Object (CSS Property)</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 40%;">Default object size</th>
  </tr>
  </thead>
 <tbody>
  <tr><td><a href="/en-US/docs/Web/CSS/background-image" title="The background-image CSS property sets one or more background images on an element."><code>background-image</code></a></td> <td>The size of the element's background positioning area</td></tr>
  <tr><td><a href="/en-US/docs/Web/CSS/list-style-image" title="The list-style-image CSS property sets an image to be used as the list item marker."><code>list-style-image</code></a></td> <td>The size of a <code>1em</code> character</td></tr>
  <tr><td><a href="/en-US/docs/Web/CSS/border-image-source" title="The border-image-source CSS property sets the source image used to create an element's border image."><code>border-image-source</code></a></td> <td>The size of the element's border image area</td></tr>
  <tr><td><a href="/en-US/docs/Web/CSS/cursor" title="The cursor CSS property sets the type of cursor, if any, to show when the mouse pointer is over an element."><code>cursor</code></a></td> <td>The browser-defined size matching the usual cursor size on the client's system</td></tr>
  <tr><td><a href="/en-US/docs/Web/CSS/mask-image" title="The mask-image CSS property sets the image that is used as mask layer for an element."><code>mask-image</code></a></td> <td>?</td></tr>
  <tr><td><a href="/en-US/docs/Web/CSS/shape-outside" title="The shape-outside CSS property defines a shape—which may be non-rectangular—around which adjacent inline content should wrap."><code>shape-outside</code></a></td> <td>?</td></tr>
  <tr><td><a href="/en-US/docs/Web/CSS/mask-border-source" title="The mask-border-source CSS property sets the source image used to create an element's mask border."><code>mask-border-source</code></a></td> <td>?</td></tr>
  <tr><td><a href="/en-US/docs/Web/CSS/symbols" title="The symbols() CSS function lets you define counter styles inline, directly as the value of a property such as list-style. Unlike @counter-style, symbols() is anonymous (i.e., it can only be used once). Although less powerful, it is shorter and easier to write than @counter-style."><code>symbols</code></a> for @counter-style</td> <td>At risk feature. If supported, the browser-defined size matching the usual cursor size on the client's system</td></tr>
  <tr><td><a href="/en-US/docs/Web/CSS/content" title="The content CSS property replaces an element with a generated value. Objects inserted using the content property are anonymous replaced elements."><code>content</code></a> for a pseudo-element (<a href="/en-US/docs/Web/CSS/::after" title="In CSS, ::after creates a pseudo-element that is the last child of the selected element. It is often used to add cosmetic content to an element with the content property."><code>::after</code></a>/<a href="/en-US/docs/Web/CSS/::before" title="In CSS, ::before creates a pseudo-element that is the first child of the selected element. It is often used to add cosmetic content to an element with the content property."><code>::before</code></a>)</td> <td>A 300px × 150px rectangle</td></tr>
 </tbody>
</table>



### Accessibility

+ [Accessibility](../WebDev/Frontend-W3C/1-HTML5CSSFund/04-Debug.md#accessibility): designing Web page with various disabilities in mind

+ Guidelines
  + not too small on font size
  + not too tight on line height
  + good color contrast for foregrounbd and background
  + not irregularly space text or make it jump around


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


### CSS Selector Reference

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="0" align="center" width=90%>
  <caption style="font-size: 1.5em; color: darkblue; font-weight: bold;"><a href="https://www.w3schools.com/cssref/css_selectors.asp">CSS Selectors</a></caption>
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


### Typical Selectors

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
  <caption style="font-size: 1.5em; color: darkblue; font-weight: bold;"><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#selectors">CSS Selectors</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Selector</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">HTML</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">CSS</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>tag</td>
    <td>&lt;li&gt;</td>
    <td>li {list-style_type: circle;}</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#tag-selector">Selector</a></td>
  </tr>
  <tr>
    <td>id</td>
    <td>&lt;p id="p18"&gt; Ulysses &lt;/p&gt;</td>
    <td>#p18 {color: blue;}</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#id-selector">Selector</a></td>
  </tr>
  <tr>
    <td>class</td>
    <td>&lt;li class="bird flying"&gt;eagle&lt;/li&gt;</td>
    <td>.bird   { color: blue; } <br/>.flying { text-decoration: underline; }</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#class-selector">Selector</a></td>
  </tr>
  <tr>
    <td>Comma separated</td>
    <td>,</td>
    <td>blockquote, <br/> q, <br/> .speech { <br/> &nbsp;&nbsp;&nbsp;&nbsp; color: red; <br/>&nbsp;&nbsp;&nbsp;&nbsp; font-style: italic; <br/> } <br/> .speech { font-weight: bold; }</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#comma-separated-selectors">Selector</a></td>
  </tr>
  <tr>
    <td>Specialized</td>
    <td>&gt;li class="insect flying"&lt;wasp&lt;/li&gt;</td>
    <td>.insect.flying { <br/> &nbsp;&nbsp;&nbsp;&nbsp; text-decoration: underline; <br/> &nbsp;&nbsp;&nbsp;&nbsp; font-weight: bold; <br/>   }</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#specialized-selectors">Selector</a></td>
  </tr>
  <tr>
    <td>Descendant</td>
    <td>&lt;section id="intro"&gt;Welcome to &lt;a href="#palaceland"&gt;PalaceLand&lt;/a&gt;</td>
    <td>#intro a { color: red; }</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#descendant-selectors">Selector</a></td>
  </tr>
  <tr>
    <td>Direct descendant</td>
    <td>&lt;section id="intro"&gt;Welcome to &lt;a href="#palaceland"&gt;PalaceLand&lt;/a&gt;</td>
    <td>#intro > a { font-size: large; }</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#direct-descendant-selectors---">Selector</a></td>
  </tr>
  </tbody>
</table>



### Styling with Pseudo Class

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Class</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Properties/Values</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>tr:nth-child(even), tr:nth-child(odd)</td>
    <td>alternating colors for table rows making it easier to differentiate data between rows</td>
    <td>background-color: color;</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#-nth-child">Zebra</a></td>
  </tr>
  <tr>
    <td>tr.hover</td>
    <td>mouse over rows in your table to highlight them in the color specified</td>
    <td>background-color: black;</td>
    <td><a href="..WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#-hover-active">Hover</a></td>
  </tr>
  <tr>
    <td>tr.visted</td>
    <td>usually put on a selector that resolves to an &lt;a&gt; tag</td>
    <td>None</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#-visited">Visted</a></td>
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

### List of Color properties

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
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



## Font Property

### List of Font Properties

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
  <caption style="font-size: 1.5em;"><a href="https://www.w3.org/Style/Examples/007/fonts">Font properties</a></caption>
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
    <td>height of the space</td>
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


### [Typography][066]

+ sans-serif: the letters do not have added flourishes; most popular; `Helvetica`, `Verdana`, `Arial`, `Tahoma`
+ serif - the small flourish lines at the edges of letters and symbols; `Times New Roman`, `Book Antiqua`, `Georgia`
+ monospace - all letters have the same fixed width; `Courier New`
+ cursive - mimic human handwriting often by joining letters or having an italic slant; `Comic Sans MS`
+ fantasy - the most diverse category of fonts including all of those that are particularly decorative


## List Property

### List of List Styling

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
    <td>list-style-type</td>
    <td>list marker, usually positioned to the left of any list item</td>
    <td>ul: disc, circle, square, none; <br/>ol: decimal, decimal-leading-zero, lower-roman, upper-roman, lower-alpha, upper-alpha, armenian, georgian, simp-chinese-formal, etc.</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#list-style-type">List</a></td>
  </tr>
  <tr>
    <td>list-style-position</td>
    <td>how closely it is positioned to the list itself</td>
    <td>inside, outside</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#list-style-position">List</a></td>
  </tr>
  <tr>
    <td>list-style-image</td>
    <td>customized little markers on a list</td>
    <td>url("path/fig.png")</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#list-style-image">List</a></td>
  </tr>
  </tbody>
</table>



## Background Image Properties


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em;"><a href="https://www.w3.org/TR/CSS22/colors.html#background-properties">List of Background properties</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Property</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Value</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Link</th>
  </tr>
  </thead>
  <tbody>
  <tr>  
    <td>background-color</td>
    <td>&lt;color&gt;<br/>transparent<br/>inherit</td>
    <td>set the background color of an element, either a &lt;color&gt;> value or the keyword 'transparent', to make the underlying colors shine through</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#background-color">Color</a></td>
  </tr>
  <tr>  
    <td>background-image</td>
    <td>&lt;uri&gt;<br/>none<br/>inherit</td>
    <td>set the background image of an element</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#background-image">Image</a></td>
  </tr>
  <tr>  
    <td>background-repeat</td>
    <td>repeat<br/>repeat-x<br/>repeat-y<br/>no-repeat<br/>inherit</td>
    <td>specify whether the image is repeated (tiled), and how</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#background-repeat">Repeat</a></td>
  </tr>
  <tr>  
    <td>background-attachment</td>
    <td>scroll<br/>fixed<br/>inherit</td>
    <td>specifies whether it is fixed with regard to the viewport ('fixed') or scrolls along with the containing block ('scroll')</td>
    <td><a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#text-align">Alignment</a></td>
  </tr>
  <tr>  
    <td>background-size</td>
    <td>[&lt;length&gt; &ltlength&gt]<br/>[&lt;length&gt;  auto]<br/>[&lt;percentag&gt; auto]</td>
    <td>size a background image to fit its element</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#background-size">Size</a></td>
  </tr>
  <tr>  
    <td>background-position</td>
    <td>[[ &lt;percentage&gt; | &lt;length&gt; | left | center | right ] [ &lt;percentage&gt; | &lt;length&gt; | top | center | bottom ]? ] <br/> [ [ left | center | right ] || [ top | center | bottom ] ]<br/>inherit</td>
    <td>specifies background image's initial position</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#background-position">Position</a></td>
  </tr>
  </tbody>
</table>





## Alignment Property

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


## Element width and height

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
    <td>width</td>
    <td>element width</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, auto, inherit</td>
    <td><a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#width-and-height">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#width-and-height">Element18</a></td>
  </tr>
  <tr>
    <td>height</td>
    <td>element height</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, auto, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#the-height-property">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#width-and-height">Element18</a></td>
  </tr>
  <tr>
    <td>min-width</td>
    <td>minimum width of the element</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#min-max-widths">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#min-width-max-width-min-height-max-height">Element18</a></td>
  </tr>
  <tr>
    <td>min-width</td>
    <td>maximum width of the element</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, none, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#min-max-widths">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#min-width-max-width-min-height-max-height">Element18</a></td>
  </tr>
  <tr>
    <td>min-height</td>
    <td>minimum height of the element</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#min-max-heights">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#min-width-max-width-min-height-max-height">Element18</a></td>
  </tr>
  <tr>
    <td>max-height</td>
    <td>maximum height of the element</td>
    <td>&lt;length&gt;, &lt;percentage&gt;, none, inherit</td>
    <td><a href="https://www.w3.org/TR/CSS22/visudet.html#min-max-heights">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#min-width-max-width-min-height-max-height">Element18</a></td>
  </tr>
  </tbody>
</table>


## Floating Property

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
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#border">Table</a>, <a href="https://www.w3schools.com/cssref/pr_border.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-top, border-left, broder-bottom, border-right</td>
    <td>&lt;th&gt;, &lt;td&gt;</td>
    <td>set borders to individual sides</td>
    <td> <ul> &lt;width, style, color&gt; <ul><li>width = pixel </li> <li>style = none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset </li> <li>color = color name or color values, transparent</li> </ul></td>
    <td><a href="../WebDev/Frontend-W<td3C/1.HTML5CSS/05.HTMLCSS.md#side-borders"></a>, <a href="https://www.w3schools.com/cssref/pr_border-top.asp">Top</a>, <a href="https://www.w3schools.com/cssref/pr_border-right.asp">Right</a>, <a href="https://www.w3schools.com/cssref/pr_border-bottom.asp">Bottom</a>, <a href="https://www.w3schools.com/cssref/pr_border-left.asp">Left</a></td>
  </tr>
  <tr>
    <td>border-collapse</td>
    <td> &lt;table&gt;, &lt;th&gt;, &lt;td&gt;</td>
    <td>to collapse border or not</td>
    <td><ul><li><strong>separate</strong>: each cell will display its own borders; default value</li> <li><strong>collapse</strong>: border are collapsed into a single border (border-spacing and empty-cells properties have no effect)</li><li>initial: sets to default value (separate)</li><li>inherit: inherited from its parent element</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#border-collapse">Collapse</a>, <a href="https://www.w3schools.com/cssref/pr_border-collapse.asp">W3S</a></td>
  </tr>
  <tr>
    <td>border-spacing</td>
    <td> &lt;table&gt;, &lt;th&gt;, &lt;td&gt;</td>
    <td>space between content in cell and border</td>
    <td><strong>&lt; length, length&gt; </strong>: specifyingthe distance between the borders of adjacent cells in px, cm, etc. Negative values are not allowed.<ul><li>one value: define both the horizontal and vertical spacing between cells</li> <li>two values: the first sets the horizontal spacing and the second sets the vertical spacing</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#border-spacing">Spacing</a>, <a href="https://www.w3schools.com/cssref/pr_border-spacing.asp">W3S</a></td>
  </tr>
  <tr>
    <td>width; height</td>
    <td> &lt;td&gt;</td>
    <td>set the width and height for the rows and columns for your table based on the content in your cells | units of length like pixels, percentage; auto: the browser will calculate and select a width for the specified element (default value)</td>
    <td><ul><li> auto</li> <li><i>length</i> (px, em, cm, etc.)</li> <li><i>%</i> (% of the width of the containing element)</li> <li>inherit (inherited from the parent element)</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#table-width-and-height">Size</a>, <a href="https://www.w3schools.com/cssref/pr_dim_height.asp">height</a>, <a href="https://www.w3schools.com/cssref/pr_dim_width.asp">width</a></td>
  </tr>
  <tr>
    <td>text-align</td>
    <td> &lt;th&gt;, &lt;td&gt;</td>
    <td>align the text of and cells left, right or center</td>
    <td><ul><li> left</li> <li>right</li> <li>center</li> <li>Default: &lt;th&gt; = center, &lt;td&gt; = left</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#text-align">Size</a>, <a href="https://www.w3schools.com/cssref/pr_text_text-align.asp">W3S</a></td>
  </tr>
  <tr>
    <td>vertical-align</td>
    <td> &lt;th&gt;, &lt;td&gt;</td>
    <td>align the text of and cells top, bottom or middle</td>
    <td><ul><li> top</li> <li>bottom</li> <li>middle</li> <li>Default: middle</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#vertical-align">Size</a>, <a href="https://www.w3schools.com/cssref/pr_pos_vertical-align.asp">W3S</a></td>
  </tr>
  <tr>
    <td>padding</td>
    <td> &lt;th&gt;, &lt;td&gt;</td>
    <td>provide some space between border and content in cell</td>
    <td><ul><li><i>length</i> (px, em, cm, etc.)</li> <li><i>%</i> (% of the width of the containing element)</li> <li><strong>&lt;length1, length2&gt;</strong>: <br/>top = bottom = length1; right = left = length2</li> <li><strong>&lt;length1, length2, length3&gt;</strong>: <br/>top = length1; right = left = length2; bottom = length3</li> <li><strong>&lt;length1, length2, length3. length4&gt;</strong>: <br/>top = length1; right = length2; bottom = length3; left = length4</li><ul></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#padding">Padding</a>, <a href="https://www.w3schools.com/cssref/pr_text_text-align.asp">W3S</a></td>
  </tr>
  </tbody>
</table>



## Box Model

### Model and Characteristics

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


### Model Properties

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 70vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
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
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="">Space</a>, <a href="https://www.w3schools.com/css/css_padding.asp">W3S</a>, </td>
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
    <td><a href="../1.HTML5CSS/04.Debug.md#43-debugging-and-the-css-box-model">Box</a>, <a href="https://www.w3schools.com/css/css_margin.asp">W3S</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/03-CSS.md#margin">Common</a></td>
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

+  [Display Elements](../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#display-property)


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

### Position Property

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
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#the-left-top-right-and-bottom-properties">Position</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/left">Left</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/top">Top</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/bottom">Bottom</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/right">Right</a>, <a href="https://www.w3.org/TR/CSS22/visuren.html#position-props">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#the-position-property"> Positioning </a> </td>
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
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">Position</a>, <a href="https://www.w3.org/TR/CSS22/visuren.html#choose-position">W3C</a>, <a href="../WebDev/Frontend-W3C/4-CSSBasics/04-Layout.md#the-position-property"> Positioning </a></td>
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
    <td>max-height</td>
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
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow">Overflow</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Layout</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#overflow">Table</a></td>
  </tr>
  <tr>
    <td>overflow-block</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows a block-level element's block start and block end edge</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-block">Overflow-Block</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Layout</a></td>
  </tr>
  <tr>
    <td>overflow-inline</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows an inline element's start and end edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-inline">Overflow-Inline</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Layout</a></td>
  </tr>
  <tr>
    <td>overflow-x</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows a block-level element's left and right edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-x">Overflow-X</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Layout</a></td>
  </tr>
  <tr>
    <td>overflow-y</td>
    <td><ul><li>specified with a single keyword</li><li>sets what shows when content overflows an inline element's top and bottom edges</li></ul></td>
    <td>visible, hidden, auto, scroll</td>
    <td><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-y">Overflow-Y</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/06-Layout.md#cropping-and-scrolling-overflow">Layout</a></td>
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
[094]: ..WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#-hover-active
[095]: ../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#-nth-child
[096]: ../WebDev/Frontend-W3C/1.HTML5CSS/05.HTMLCSS.md#-visited
