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
  + multiple HTML elements with similar style: `p, ul, ol {color: blue; }`

+ Property:
  + tell the browser how to style the HTML tag that has been selected
  + as many lines of code as you choose
  + each of which has two parts- the property and the value you want that property to be
  + with its own collection of possible values
  + [complete list of latest CSS properties][005] at the W3C


## Tree Presentation - Inheritance

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+CSS.0x+3T2018/courseware/bb30325abfbf47b583784acd793db6dc/0e1bd16d542e4a1085cb8d9b305f8e59/1?activate_block_id=block-v1%3AW3Cx%2BCSS.0x%2B3T2018%2Btype%40vertical%2Bblock%40833b012fc6dd41f68fa5fd6e3b93e8a8">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c3441bd3d744e14d5d1c0c663d7ad1dc/asset-v1:W3Cx+CSS.0x+3T2018+type@asset+block/2-4-2_inheritance_tree.PNG" style="margin: 0.1em;" alt="ags that contain other tags are parents, and the tags inside of them are their children in the following tree representation." title="HTML inheritance structure" width="250">
  </a></div>
</div>

+ CSS property values set on one element will be transferred down the tree to that element's children. 
+ Not every property is inherited, but many are.

## Color Properties

| Property | Description | Link |
|----------|-------------|------|
| `color` | the foreground color of an element's text content | [W3C][006], [Color][007] |
| `background-color` | background color of an element | [W3C][008], [Color][009] |

### HTML Color Names and Values

+ A `<color>` is either a keyword or a numerical RGB specification.


<table style="display: table; border-collapse: separate;border-spacing: 2px; border-color: grey; text-align: center;font-family: Helvetica, Verdana, sans-serif;">
   <caption style="font-size: 1.2em;"><b><a href="https://www.w3.org/TR/css-color-3/#svg-color">Color names and <span class="index-inst" id="srgbval">sRGB</span>
    values</a></b><br>
   <tbody>
    <tr>
     <th style="background:black; min-width: 10vw;">Named
     </th><th style="background:black; min-width: 10vw;">Numeric
     </th><th style="background:black; min-width: 15vw;">Color name
     </th><th style="background:black; min-width: 15vw;">Hex rgb
     </th><th style="background:black; min-width: 15vw;">Decimal
    </th></tr><tr>
     <td style="background:aliceblue"> </td><td style="background:#f0f8ff"> </td><td><dfn style="font-weight:bolder;">aliceblue</dfn> </td><td style="text-transform: uppercase;">#f0f8ff </td><td style="text-transform: uppercase;">240,248,255
    </td></tr><tr>
     <td style="background:antiquewhite"> </td><td style="background:#faebd7"> </td><td><dfn style="font-weight:bolder;">antiquewhite</dfn> </td><td style="text-transform: uppercase;">#faebd7 </td><td style="text-transform: uppercase;">250,235,215
    </td></tr><tr>
     <td style="background:aqua"> </td><td style="background:#00ffff"> </td><td><dfn style="font-weight:bolder;">aqua</dfn> </td><td style="text-transform: uppercase;">#00ffff </td><td style="text-transform: uppercase;">0,255,255
    </td></tr><tr>
     <td style="background:aquamarine"> </td><td style="background:#7fffd4"> </td><td><dfn style="font-weight:bolder;">aquamarine</dfn> </td><td style="text-transform: uppercase;">#7fffd4 </td><td style="text-transform: uppercase;">127,255,212
    </td></tr><tr>
     <td style="background:azure"> </td><td style="background:#f0ffff"> </td><td><dfn style="font-weight:bolder;">azure</dfn> </td><td style="text-transform: uppercase;">#f0ffff </td><td style="text-transform: uppercase;">240,255,255
    </td></tr><tr>
     <td style="background:beige"> </td><td style="background:#f5f5dc"> </td><td><dfn style="font-weight:bolder;">beige</dfn> </td><td style="text-transform: uppercase;">#f5f5dc </td><td style="text-transform: uppercase;">245,245,220
    </td></tr><tr>
     <td style="background:bisque"> </td><td style="background:#ffe4c4"> </td><td><dfn style="font-weight:bolder;">bisque</dfn> </td><td style="text-transform: uppercase;">#ffe4c4 </td><td style="text-transform: uppercase;">255,228,196
    </td></tr><tr>
     <td style="background:black"> </td><td style="background:#000000"> </td><td><dfn style="font-weight:bolder;">black</dfn> </td><td style="text-transform: uppercase;">#000000 </td><td style="text-transform: uppercase;">0,0,0
    </td></tr><tr>
     <td style="background:blanchedalmond"> </td><td style="background:#ffebcd"> </td><td><dfn style="font-weight:bolder;">blanchedalmond</dfn> </td><td style="text-transform: uppercase;">#ffebcd </td><td style="text-transform: uppercase;">255,235,205
    </td></tr><tr>
     <td style="background:blue"> </td><td style="background:#0000ff"> </td><td><dfn style="font-weight:bolder;">blue</dfn> </td><td style="text-transform: uppercase;">#0000ff </td><td style="text-transform: uppercase;">0,0,255
    </td></tr><tr>
     <td style="background:blueviolet"> </td><td style="background:#8a2be2"> </td><td><dfn style="font-weight:bolder;">blueviolet</dfn> </td><td style="text-transform: uppercase;">#8a2be2 </td><td style="text-transform: uppercase;">138,43,226
    </td></tr><tr>
     <td style="background:brown"> </td><td style="background:#a52a2a"> </td><td><dfn style="font-weight:bolder;">brown</dfn> </td><td style="text-transform: uppercase;">#a52a2a </td><td style="text-transform: uppercase;">165,42,42
    </td></tr><tr>
     <td style="background:burlywood"> </td><td style="background:#deb887"> </td><td><dfn style="font-weight:bolder;">burlywood</dfn> </td><td style="text-transform: uppercase;">#deb887 </td><td style="text-transform: uppercase;">222,184,135
    </td></tr><tr>
     <td style="background:cadetblue"> </td><td style="background:#5f9ea0"> </td><td><dfn style="font-weight:bolder;">cadetblue</dfn> </td><td style="text-transform: uppercase;">#5f9ea0 </td><td style="text-transform: uppercase;">95,158,160
    </td></tr><tr>
     <td style="background:chartreuse"> </td><td style="background:#7fff00"> </td><td><dfn style="font-weight:bolder;">chartreuse</dfn> </td><td style="text-transform: uppercase;">#7fff00 </td><td style="text-transform: uppercase;">127,255,0
    </td></tr><tr>
     <td style="background:chocolate"> </td><td style="background:#d2691e"> </td><td><dfn style="font-weight:bolder;">chocolate</dfn> </td><td style="text-transform: uppercase;">#d2691e </td><td style="text-transform: uppercase;">210,105,30
    </td></tr><tr>
     <td style="background:coral"> </td><td style="background:#ff7f50"> </td><td><dfn style="font-weight:bolder;">coral</dfn> </td><td style="text-transform: uppercase;">#ff7f50 </td><td style="text-transform: uppercase;">255,127,80
    </td></tr><tr>
     <td style="background:cornflowerblue"> </td><td style="background:#6495ed"> </td><td><dfn style="font-weight:bolder;">cornflowerblue</dfn> </td><td style="text-transform: uppercase;">#6495ed </td><td style="text-transform: uppercase;">100,149,237
    </td></tr><tr>
     <td style="background:cornsilk"> </td><td style="background:#fff8dc"> </td><td><dfn style="font-weight:bolder;">cornsilk</dfn> </td><td style="text-transform: uppercase;">#fff8dc </td><td style="text-transform: uppercase;">255,248,220
    </td></tr><tr>
     <td style="background:crimson"> </td><td style="background:#dc143c"> </td><td><dfn style="font-weight:bolder;">crimson</dfn> </td><td style="text-transform: uppercase;">#dc143c </td><td style="text-transform: uppercase;">220,20,60
    </td></tr><tr>
     <td style="background:cyan"> </td><td style="background:#00ffff"> </td><td><dfn style="font-weight:bolder;">cyan</dfn> </td><td style="text-transform: uppercase;">#00ffff </td><td style="text-transform: uppercase;">0,255,255
    </td></tr><tr>
     <td style="background:darkblue"> </td><td style="background:#00008b"> </td><td><dfn style="font-weight:bolder;">darkblue</dfn> </td><td style="text-transform: uppercase;">#00008b </td><td style="text-transform: uppercase;">0,0,139
    </td></tr><tr>
     <td style="background:darkcyan"> </td><td style="background:#008b8b"> </td><td><dfn style="font-weight:bolder;">darkcyan</dfn> </td><td style="text-transform: uppercase;">#008b8b </td><td style="text-transform: uppercase;">0,139,139
    </td></tr><tr>
     <td style="background:darkgoldenrod"> </td><td style="background:#b8860b"> </td><td><dfn style="font-weight:bolder;">darkgoldenrod</dfn> </td><td style="text-transform: uppercase;">#b8860b </td><td style="text-transform: uppercase;">184,134,11
    </td></tr><tr>
     <td style="background:darkgray"> </td><td style="background:#a9a9a9"> </td><td><dfn style="font-weight:bolder;">darkgray</dfn> </td><td style="text-transform: uppercase;">#a9a9a9 </td><td style="text-transform: uppercase;">169,169,169
    </td></tr><tr>
     <td style="background:darkgreen"> </td><td style="background:#006400"> </td><td><dfn style="font-weight:bolder;">darkgreen</dfn> </td><td style="text-transform: uppercase;">#006400 </td><td style="text-transform: uppercase;">0,100,0
    </td></tr><tr>
     <td style="background:darkgrey"> </td><td style="background:#a9a9a9"> </td><td><dfn style="font-weight:bolder;">darkgrey</dfn> </td><td style="text-transform: uppercase;">#a9a9a9 </td><td style="text-transform: uppercase;">169,169,169
    </td></tr><tr>
     <td style="background:darkkhaki"> </td><td style="background:#bdb76b"> </td><td><dfn style="font-weight:bolder;">darkkhaki</dfn> </td><td style="text-transform: uppercase;">#bdb76b </td><td style="text-transform: uppercase;">189,183,107
    </td></tr><tr>
     <td style="background:darkmagenta"> </td><td style="background:#8b008b"> </td><td><dfn style="font-weight:bolder;">darkmagenta</dfn> </td><td style="text-transform: uppercase;">#8b008b </td><td style="text-transform: uppercase;">139,0,139
    </td></tr><tr>
     <td style="background:darkolivegreen"> </td><td style="background:#556b2f"> </td><td><dfn style="font-weight:bolder;">darkolivegreen</dfn> </td><td style="text-transform: uppercase;">#556b2f </td><td style="text-transform: uppercase;">85,107,47
    </td></tr><tr>
     <td style="background:darkorange"> </td><td style="background:#ff8c00"> </td><td><dfn style="font-weight:bolder;">darkorange</dfn> </td><td style="text-transform: uppercase;">#ff8c00 </td><td style="text-transform: uppercase;">255,140,0
    </td></tr><tr>
     <td style="background:darkorchid"> </td><td style="background:#9932cc"> </td><td><dfn style="font-weight:bolder;">darkorchid</dfn> </td><td style="text-transform: uppercase;">#9932cc </td><td style="text-transform: uppercase;">153,50,204
    </td></tr><tr>
     <td style="background:darkred"> </td><td style="background:#8b0000"> </td><td><dfn style="font-weight:bolder;">darkred</dfn> </td><td style="text-transform: uppercase;">#8b0000 </td><td style="text-transform: uppercase;">139,0,0
    </td></tr><tr>
     <td style="background:darksalmon"> </td><td style="background:#e9967a"> </td><td><dfn style="font-weight:bolder;">darksalmon</dfn> </td><td style="text-transform: uppercase;">#e9967a </td><td style="text-transform: uppercase;">233,150,122
    </td></tr><tr>
     <td style="background:darkseagreen"> </td><td style="background:#8fbc8f"> </td><td><dfn style="font-weight:bolder;">darkseagreen</dfn> </td><td style="text-transform: uppercase;">#8fbc8f </td><td style="text-transform: uppercase;">143,188,143
    </td></tr><tr>
     <td style="background:darkslateblue"> </td><td style="background:#483d8b"> </td><td><dfn style="font-weight:bolder;">darkslateblue</dfn> </td><td style="text-transform: uppercase;">#483d8b </td><td style="text-transform: uppercase;">72,61,139
    </td></tr><tr>
     <td style="background:darkslategray"> </td><td style="background:#2f4f4f"> </td><td><dfn style="font-weight:bolder;">darkslategray</dfn> </td><td style="text-transform: uppercase;">#2f4f4f </td><td style="text-transform: uppercase;">47,79,79
    </td></tr><tr>
     <td style="background:darkslategrey"> </td><td style="background:#2f4f4f"> </td><td><dfn style="font-weight:bolder;">darkslategrey</dfn> </td><td style="text-transform: uppercase;">#2f4f4f </td><td style="text-transform: uppercase;">47,79,79
    </td></tr><tr>
     <td style="background:darkturquoise"> </td><td style="background:#00ced1"> </td><td><dfn style="font-weight:bolder;">darkturquoise</dfn> </td><td style="text-transform: uppercase;">#00ced1 </td><td style="text-transform: uppercase;">0,206,209
    </td></tr><tr>
     <td style="background:darkviolet"> </td><td style="background:#9400d3"> </td><td><dfn style="font-weight:bolder;">darkviolet</dfn> </td><td style="text-transform: uppercase;">#9400d3 </td><td style="text-transform: uppercase;">148,0,211
    </td></tr><tr>
     <td style="background:deeppink"> </td><td style="background:#ff1493"> </td><td><dfn style="font-weight:bolder;">deeppink</dfn> </td><td style="text-transform: uppercase;">#ff1493 </td><td style="text-transform: uppercase;">255,20,147
    </td></tr><tr>
     <td style="background:deepskyblue"> </td><td style="background:#00bfff"> </td><td><dfn style="font-weight:bolder;">deepskyblue</dfn> </td><td style="text-transform: uppercase;">#00bfff </td><td style="text-transform: uppercase;">0,191,255
    </td></tr><tr>
     <td style="background:dimgray"> </td><td style="background:#696969"> </td><td><dfn style="font-weight:bolder;">dimgray</dfn> </td><td style="text-transform: uppercase;">#696969 </td><td style="text-transform: uppercase;">105,105,105
    </td></tr><tr>
     <td style="background:dimgrey"> </td><td style="background:#696969"> </td><td><dfn style="font-weight:bolder;">dimgrey</dfn> </td><td style="text-transform: uppercase;">#696969 </td><td style="text-transform: uppercase;">105,105,105
    </td></tr><tr>
     <td style="background:dodgerblue"> </td><td style="background:#1e90ff"> </td><td><dfn style="font-weight:bolder;">dodgerblue</dfn> </td><td style="text-transform: uppercase;">#1e90ff </td><td style="text-transform: uppercase;">30,144,255
    </td></tr><tr>
     <td style="background:firebrick"> </td><td style="background:#b22222"> </td><td><dfn style="font-weight:bolder;">firebrick</dfn> </td><td style="text-transform: uppercase;">#b22222 </td><td style="text-transform: uppercase;">178,34,34
    </td></tr><tr>
     <td style="background:floralwhite"> </td><td style="background:#fffaf0"> </td><td><dfn style="font-weight:bolder;">floralwhite</dfn> </td><td style="text-transform: uppercase;">#fffaf0 </td><td style="text-transform: uppercase;">255,250,240
    </td></tr><tr>
     <td style="background:forestgreen"> </td><td style="background:#228b22"> </td><td><dfn style="font-weight:bolder;">forestgreen</dfn> </td><td style="text-transform: uppercase;">#228b22 </td><td style="text-transform: uppercase;">34,139,34
    </td></tr><tr>
     <td style="background:fuchsia"> </td><td style="background:#ff00ff"> </td><td><dfn style="font-weight:bolder;">fuchsia</dfn> </td><td style="text-transform: uppercase;">#ff00ff </td><td style="text-transform: uppercase;">255,0,255
    </td></tr><tr>
     <td style="background:gainsboro"> </td><td style="background:#dcdcdc"> </td><td><dfn style="font-weight:bolder;">gainsboro</dfn> </td><td style="text-transform: uppercase;">#dcdcdc </td><td style="text-transform: uppercase;">220,220,220
    </td></tr><tr>
     <td style="background:ghostwhite"> </td><td style="background:#f8f8ff"> </td><td><dfn style="font-weight:bolder;">ghostwhite</dfn> </td><td style="text-transform: uppercase;">#f8f8ff </td><td style="text-transform: uppercase;">248,248,255
    </td></tr><tr>
     <td style="background:gold"> </td><td style="background:#ffd700"> </td><td><dfn style="font-weight:bolder;">gold</dfn> </td><td style="text-transform: uppercase;">#ffd700 </td><td style="text-transform: uppercase;">255,215,0
    </td></tr><tr>
     <td style="background:goldenrod"> </td><td style="background:#daa520"> </td><td><dfn style="font-weight:bolder;">goldenrod</dfn> </td><td style="text-transform: uppercase;">#daa520 </td><td style="text-transform: uppercase;">218,165,32
    </td></tr><tr>
     <td style="background:gray"> </td><td style="background:#808080"> </td><td><dfn style="font-weight:bolder;">gray</dfn> </td><td style="text-transform: uppercase;">#808080 </td><td style="text-transform: uppercase;">128,128,128
    </td></tr><tr>
     <td style="background:green"> </td><td style="background:#008000"> </td><td><dfn style="font-weight:bolder;">green</dfn> </td><td style="text-transform: uppercase;">#008000 </td><td style="text-transform: uppercase;">0,128,0
    </td></tr><tr>
     <td style="background:greenyellow"> </td><td style="background:#adff2f"> </td><td><dfn style="font-weight:bolder;">greenyellow</dfn> </td><td style="text-transform: uppercase;">#adff2f </td><td style="text-transform: uppercase;">173,255,47
    </td></tr><tr>
     <td style="background:grey"> </td><td style="background:#808080"> </td><td><dfn style="font-weight:bolder;">grey</dfn> </td><td style="text-transform: uppercase;">#808080 </td><td style="text-transform: uppercase;">128,128,128
    </td></tr><tr>
     <td style="background:honeydew"> </td><td style="background:#f0fff0"> </td><td><dfn style="font-weight:bolder;">honeydew</dfn> </td><td style="text-transform: uppercase;">#f0fff0 </td><td style="text-transform: uppercase;">240,255,240
    </td></tr><tr>
     <td style="background:hotpink"> </td><td style="background:#ff69b4"> </td><td><dfn style="font-weight:bolder;">hotpink</dfn> </td><td style="text-transform: uppercase;">#ff69b4 </td><td style="text-transform: uppercase;">255,105,180
    </td></tr><tr>
     <td style="background:indianred"> </td><td style="background:#cd5c5c"> </td><td><dfn style="font-weight:bolder;">indianred</dfn> </td><td style="text-transform: uppercase;">#cd5c5c </td><td style="text-transform: uppercase;">205,92,92
    </td></tr><tr>
     <td style="background:indigo"> </td><td style="background:#4b0082"> </td><td><dfn style="font-weight:bolder;">indigo</dfn> </td><td style="text-transform: uppercase;">#4b0082 </td><td style="text-transform: uppercase;">75,0,130
    </td></tr><tr>
     <td style="background:ivory"> </td><td style="background:#fffff0"> </td><td><dfn style="font-weight:bolder;">ivory</dfn> </td><td style="text-transform: uppercase;">#fffff0 </td><td style="text-transform: uppercase;">255,255,240
    </td></tr><tr>
     <td style="background:khaki"> </td><td style="background:#f0e68c"> </td><td><dfn style="font-weight:bolder;">khaki</dfn> </td><td style="text-transform: uppercase;">#f0e68c </td><td style="text-transform: uppercase;">240,230,140
    </td></tr><tr>
     <td style="background:lavender"> </td><td style="background:#e6e6fa"> </td><td><dfn style="font-weight:bolder;">lavender</dfn> </td><td style="text-transform: uppercase;">#e6e6fa </td><td style="text-transform: uppercase;">230,230,250
    </td></tr><tr>
     <td style="background:lavenderblush"> </td><td style="background:#fff0f5"> </td><td><dfn style="font-weight:bolder;">lavenderblush</dfn> </td><td style="text-transform: uppercase;">#fff0f5 </td><td style="text-transform: uppercase;">255,240,245
    </td></tr><tr>
     <td style="background:lawngreen"> </td><td style="background:#7cfc00"> </td><td><dfn style="font-weight:bolder;">lawngreen</dfn> </td><td style="text-transform: uppercase;">#7cfc00 </td><td style="text-transform: uppercase;">124,252,0
    </td></tr><tr>
     <td style="background:lemonchiffon"> </td><td style="background:#fffacd"> </td><td><dfn style="font-weight:bolder;">lemonchiffon</dfn> </td><td style="text-transform: uppercase;">#fffacd </td><td style="text-transform: uppercase;">255,250,205
    </td></tr><tr>
     <td style="background:lightblue"> </td><td style="background:#add8e6"> </td><td><dfn style="font-weight:bolder;">lightblue</dfn> </td><td style="text-transform: uppercase;">#add8e6 </td><td style="text-transform: uppercase;">173,216,230
    </td></tr><tr>
     <td style="background:lightcoral"> </td><td style="background:#f08080"> </td><td><dfn style="font-weight:bolder;">lightcoral</dfn> </td><td style="text-transform: uppercase;">#f08080 </td><td style="text-transform: uppercase;">240,128,128
    </td></tr><tr>
     <td style="background:lightcyan"> </td><td style="background:#e0ffff"> </td><td><dfn style="font-weight:bolder;">lightcyan</dfn> </td><td style="text-transform: uppercase;">#e0ffff </td><td style="text-transform: uppercase;">224,255,255
    </td></tr><tr>
     <td style="background:lightgoldenrodyellow"> </td><td style="background:#fafad2"> </td><td><dfn style="font-weight:bolder;">lightgoldenrodyellow</dfn> </td><td style="text-transform: uppercase;">#fafad2 </td><td style="text-transform: uppercase;">250,250,210
    </td></tr><tr>
     <td style="background:lightgray"> </td><td style="background:#d3d3d3"> </td><td><dfn style="font-weight:bolder;">lightgray</dfn> </td><td style="text-transform: uppercase;">#d3d3d3 </td><td style="text-transform: uppercase;">211,211,211
    </td></tr><tr>
     <td style="background:lightgreen"> </td><td style="background:#90ee90"> </td><td><dfn style="font-weight:bolder;">lightgreen</dfn> </td><td style="text-transform: uppercase;">#90ee90 </td><td style="text-transform: uppercase;">144,238,144
    </td></tr><tr>
     <td style="background:lightgrey"> </td><td style="background:#d3d3d3"> </td><td><dfn style="font-weight:bolder;">lightgrey</dfn> </td><td style="text-transform: uppercase;">#d3d3d3 </td><td style="text-transform: uppercase;">211,211,211
    </td></tr><tr>
     <td style="background:lightpink"> </td><td style="background:#ffb6c1"> </td><td><dfn style="font-weight:bolder;">lightpink</dfn> </td><td style="text-transform: uppercase;">#ffb6c1 </td><td style="text-transform: uppercase;">255,182,193
    </td></tr><tr>
     <td style="background:lightsalmon"> </td><td style="background:#ffa07a"> </td><td><dfn style="font-weight:bolder;">lightsalmon</dfn> </td><td style="text-transform: uppercase;">#ffa07a </td><td style="text-transform: uppercase;">255,160,122
    </td></tr><tr>
     <td style="background:lightseagreen"> </td><td style="background:#20b2aa"> </td><td><dfn style="font-weight:bolder;">lightseagreen</dfn> </td><td style="text-transform: uppercase;">#20b2aa </td><td style="text-transform: uppercase;">32,178,170
    </td></tr><tr>
     <td style="background:lightskyblue"> </td><td style="background:#87cefa"> </td><td><dfn style="font-weight:bolder;">lightskyblue</dfn> </td><td style="text-transform: uppercase;">#87cefa </td><td style="text-transform: uppercase;">135,206,250
    </td></tr><tr>
     <td style="background:lightslategray"> </td><td style="background:#778899"> </td><td><dfn style="font-weight:bolder;">lightslategray</dfn> </td><td style="text-transform: uppercase;">#778899 </td><td style="text-transform: uppercase;">119,136,153
    </td></tr><tr>
     <td style="background:lightslategrey"> </td><td style="background:#778899"> </td><td><dfn style="font-weight:bolder;">lightslategrey</dfn> </td><td style="text-transform: uppercase;">#778899 </td><td style="text-transform: uppercase;">119,136,153
    </td></tr><tr>
     <td style="background:lightsteelblue"> </td><td style="background:#b0c4de"> </td><td><dfn style="font-weight:bolder;">lightsteelblue</dfn> </td><td style="text-transform: uppercase;">#b0c4de </td><td style="text-transform: uppercase;">176,196,222
    </td></tr><tr>
     <td style="background:lightyellow"> </td><td style="background:#ffffe0"> </td><td><dfn style="font-weight:bolder;">lightyellow</dfn> </td><td style="text-transform: uppercase;">#ffffe0 </td><td style="text-transform: uppercase;">255,255,224
    </td></tr><tr>
     <td style="background:lime"> </td><td style="background:#00ff00"> </td><td><dfn style="font-weight:bolder;">lime</dfn> </td><td style="text-transform: uppercase;">#00ff00 </td><td style="text-transform: uppercase;">0,255,0
    </td></tr><tr>
     <td style="background:limegreen"> </td><td style="background:#32cd32"> </td><td><dfn style="font-weight:bolder;">limegreen</dfn> </td><td style="text-transform: uppercase;">#32cd32 </td><td style="text-transform: uppercase;">50,205,50
    </td></tr><tr>
     <td style="background:linen"> </td><td style="background:#faf0e6"> </td><td><dfn style="font-weight:bolder;">linen</dfn> </td><td style="text-transform: uppercase;">#faf0e6 </td><td style="text-transform: uppercase;">250,240,230
    </td></tr><tr>
     <td style="background:magenta"> </td><td style="background:#ff00ff"> </td><td><dfn style="font-weight:bolder;">magenta</dfn> </td><td style="text-transform: uppercase;">#ff00ff </td><td style="text-transform: uppercase;">255,0,255
    </td></tr><tr>
     <td style="background:maroon"> </td><td style="background:#800000"> </td><td><dfn style="font-weight:bolder;">maroon</dfn> </td><td style="text-transform: uppercase;">#800000 </td><td style="text-transform: uppercase;">128,0,0
    </td></tr><tr>
     <td style="background:mediumaquamarine"> </td><td style="background:#66cdaa"> </td><td><dfn style="font-weight:bolder;">mediumaquamarine</dfn> </td><td style="text-transform: uppercase;">#66cdaa </td><td style="text-transform: uppercase;">102,205,170
    </td></tr><tr>
     <td style="background:mediumblue"> </td><td style="background:#0000cd"> </td><td><dfn style="font-weight:bolder;">mediumblue</dfn> </td><td style="text-transform: uppercase;">#0000cd </td><td style="text-transform: uppercase;">0,0,205
    </td></tr><tr>
     <td style="background:mediumorchid"> </td><td style="background:#ba55d3"> </td><td><dfn style="font-weight:bolder;">mediumorchid</dfn> </td><td style="text-transform: uppercase;">#ba55d3 </td><td style="text-transform: uppercase;">186,85,211
    </td></tr><tr>
     <td style="background:mediumpurple"> </td><td style="background:#9370db"> </td><td><dfn style="font-weight:bolder;">mediumpurple</dfn> </td><td style="text-transform: uppercase;">#9370db </td><td style="text-transform: uppercase;">147,112,219
    </td></tr><tr>
     <td style="background:mediumseagreen"> </td><td style="background:#3cb371"> </td><td><dfn style="font-weight:bolder;">mediumseagreen</dfn> </td><td style="text-transform: uppercase;">#3cb371 </td><td style="text-transform: uppercase;">60,179,113
    </td></tr><tr>
     <td style="background:mediumslateblue"> </td><td style="background:#7b68ee"> </td><td><dfn style="font-weight:bolder;">mediumslateblue</dfn> </td><td style="text-transform: uppercase;">#7b68ee </td><td style="text-transform: uppercase;">123,104,238
    </td></tr><tr>
     <td style="background:mediumspringgreen"> </td><td style="background:#00fa9a"> </td><td><dfn style="font-weight:bolder;">mediumspringgreen</dfn> </td><td style="text-transform: uppercase;">#00fa9a </td><td style="text-transform: uppercase;">0,250,154
    </td></tr><tr>
     <td style="background:mediumturquoise"> </td><td style="background:#48d1cc"> </td><td><dfn style="font-weight:bolder;">mediumturquoise</dfn> </td><td style="text-transform: uppercase;">#48d1cc </td><td style="text-transform: uppercase;">72,209,204
    </td></tr><tr>
     <td style="background:mediumvioletred"> </td><td style="background:#c71585"> </td><td><dfn style="font-weight:bolder;">mediumvioletred</dfn> </td><td style="text-transform: uppercase;">#c71585 </td><td style="text-transform: uppercase;">199,21,133
    </td></tr><tr>
     <td style="background:midnightblue"> </td><td style="background:#191970"> </td><td><dfn style="font-weight:bolder;">midnightblue</dfn> </td><td style="text-transform: uppercase;">#191970 </td><td style="text-transform: uppercase;">25,25,112
    </td></tr><tr>
     <td style="background:mintcream"> </td><td style="background:#f5fffa"> </td><td><dfn style="font-weight:bolder;">mintcream</dfn> </td><td style="text-transform: uppercase;">#f5fffa </td><td style="text-transform: uppercase;">245,255,250
    </td></tr><tr>
     <td style="background:mistyrose"> </td><td style="background:#ffe4e1"> </td><td><dfn style="font-weight:bolder;">mistyrose</dfn> </td><td style="text-transform: uppercase;">#ffe4e1 </td><td style="text-transform: uppercase;">255,228,225
    </td></tr><tr>
     <td style="background:moccasin"> </td><td style="background:#ffe4b5"> </td><td><dfn style="font-weight:bolder;">moccasin</dfn> </td><td style="text-transform: uppercase;">#ffe4b5 </td><td style="text-transform: uppercase;">255,228,181
    </td></tr><tr>
     <td style="background:navajowhite"> </td><td style="background:#ffdead"> </td><td><dfn style="font-weight:bolder;">navajowhite</dfn> </td><td style="text-transform: uppercase;">#ffdead </td><td style="text-transform: uppercase;">255,222,173
    </td></tr><tr>
     <td style="background:navy"> </td><td style="background:#000080"> </td><td><dfn style="font-weight:bolder;">navy</dfn> </td><td style="text-transform: uppercase;">#000080 </td><td style="text-transform: uppercase;">0,0,128
    </td></tr><tr>
     <td style="background:oldlace"> </td><td style="background:#fdf5e6"> </td><td><dfn style="font-weight:bolder;">oldlace</dfn> </td><td style="text-transform: uppercase;">#fdf5e6 </td><td style="text-transform: uppercase;">253,245,230
    </td></tr><tr>
     <td style="background:olive"> </td><td style="background:#808000"> </td><td><dfn style="font-weight:bolder;">olive</dfn> </td><td style="text-transform: uppercase;">#808000 </td><td style="text-transform: uppercase;">128,128,0
    </td></tr><tr>
     <td style="background:olivedrab"> </td><td style="background:#6b8e23"> </td><td><dfn style="font-weight:bolder;">olivedrab</dfn> </td><td style="text-transform: uppercase;">#6b8e23 </td><td style="text-transform: uppercase;">107,142,35
    </td></tr><tr>
     <td style="background:orange"> </td><td style="background:#ffa500"> </td><td><dfn style="font-weight:bolder;">orange</dfn> </td><td style="text-transform: uppercase;">#ffa500 </td><td style="text-transform: uppercase;">255,165,0
    </td></tr><tr>
     <td style="background:orangered"> </td><td style="background:#ff4500"> </td><td><dfn style="font-weight:bolder;">orangered</dfn> </td><td style="text-transform: uppercase;">#ff4500 </td><td style="text-transform: uppercase;">255,69,0
    </td></tr><tr>
     <td style="background:orchid"> </td><td style="background:#da70d6"> </td><td><dfn style="font-weight:bolder;">orchid</dfn> </td><td style="text-transform: uppercase;">#da70d6 </td><td style="text-transform: uppercase;">218,112,214
    </td></tr><tr>
     <td style="background:palegoldenrod"> </td><td style="background:#eee8aa"> </td><td><dfn style="font-weight:bolder;">palegoldenrod</dfn> </td><td style="text-transform: uppercase;">#eee8aa </td><td style="text-transform: uppercase;">238,232,170
    </td></tr><tr>
     <td style="background:palegreen"> </td><td style="background:#98fb98"> </td><td><dfn style="font-weight:bolder;">palegreen</dfn> </td><td style="text-transform: uppercase;">#98fb98 </td><td style="text-transform: uppercase;">152,251,152
    </td></tr><tr>
     <td style="background:paleturquoise"> </td><td style="background:#afeeee"> </td><td><dfn style="font-weight:bolder;">paleturquoise</dfn> </td><td style="text-transform: uppercase;">#afeeee </td><td style="text-transform: uppercase;">175,238,238
    </td></tr><tr>
     <td style="background:palevioletred"> </td><td style="background:#db7093"> </td><td><dfn style="font-weight:bolder;">palevioletred</dfn> </td><td style="text-transform: uppercase;">#db7093 </td><td style="text-transform: uppercase;">219,112,147
    </td></tr><tr>
     <td style="background:papayawhip"> </td><td style="background:#ffefd5"> </td><td><dfn style="font-weight:bolder;">papayawhip</dfn> </td><td style="text-transform: uppercase;">#ffefd5 </td><td style="text-transform: uppercase;">255,239,213
    </td></tr><tr>
     <td style="background:peachpuff"> </td><td style="background:#ffdab9"> </td><td><dfn style="font-weight:bolder;">peachpuff</dfn> </td><td style="text-transform: uppercase;">#ffdab9 </td><td style="text-transform: uppercase;">255,218,185
    </td></tr><tr>
     <td style="background:peru"> </td><td style="background:#cd853f"> </td><td><dfn style="font-weight:bolder;">peru</dfn> </td><td style="text-transform: uppercase;">#cd853f </td><td style="text-transform: uppercase;">205,133,63
    </td></tr><tr>
     <td style="background:pink"> </td><td style="background:#ffc0cb"> </td><td><dfn style="font-weight:bolder;">pink</dfn> </td><td style="text-transform: uppercase;">#ffc0cb </td><td style="text-transform: uppercase;">255,192,203
    </td></tr><tr>
     <td style="background:plum"> </td><td style="background:#dda0dd"> </td><td><dfn style="font-weight:bolder;">plum</dfn> </td><td style="text-transform: uppercase;">#dda0dd </td><td style="text-transform: uppercase;">221,160,221
    </td></tr><tr>
     <td style="background:powderblue"> </td><td style="background:#b0e0e6"> </td><td><dfn style="font-weight:bolder;">powderblue</dfn> </td><td style="text-transform: uppercase;">#b0e0e6 </td><td style="text-transform: uppercase;">176,224,230
    </td></tr><tr>
     <td style="background:purple"> </td><td style="background:#800080"> </td><td><dfn style="font-weight:bolder;">purple</dfn> </td><td style="text-transform: uppercase;">#800080 </td><td style="text-transform: uppercase;">128,0,128
    </td></tr><tr>
     <td style="background:red"> </td><td style="background:#ff0000"> </td><td><dfn style="font-weight:bolder;">red</dfn> </td><td style="text-transform: uppercase;">#ff0000 </td><td style="text-transform: uppercase;">255,0,0
    </td></tr><tr>
     <td style="background:rosybrown"> </td><td style="background:#bc8f8f"> </td><td><dfn style="font-weight:bolder;">rosybrown</dfn> </td><td style="text-transform: uppercase;">#bc8f8f </td><td style="text-transform: uppercase;">188,143,143
    </td></tr><tr>
     <td style="background:royalblue"> </td><td style="background:#4169e1"> </td><td><dfn style="font-weight:bolder;">royalblue</dfn> </td><td style="text-transform: uppercase;">#4169e1 </td><td style="text-transform: uppercase;">65,105,225
    </td></tr><tr>
     <td style="background:saddlebrown"> </td><td style="background:#8b4513"> </td><td><dfn style="font-weight:bolder;">saddlebrown</dfn> </td><td style="text-transform: uppercase;">#8b4513 </td><td style="text-transform: uppercase;">139,69,19
    </td></tr><tr>
     <td style="background:salmon"> </td><td style="background:#fa8072"> </td><td><dfn style="font-weight:bolder;">salmon</dfn> </td><td style="text-transform: uppercase;">#fa8072 </td><td style="text-transform: uppercase;">250,128,114
    </td></tr><tr>
     <td style="background:sandybrown"> </td><td style="background:#f4a460"> </td><td><dfn style="font-weight:bolder;">sandybrown</dfn> </td><td style="text-transform: uppercase;">#f4a460 </td><td style="text-transform: uppercase;">244,164,96
    </td></tr><tr>
     <td style="background:seagreen"> </td><td style="background:#2e8b57"> </td><td><dfn style="font-weight:bolder;">seagreen</dfn> </td><td style="text-transform: uppercase;">#2e8b57 </td><td style="text-transform: uppercase;">46,139,87
    </td></tr><tr>
     <td style="background:seashell"> </td><td style="background:#fff5ee"> </td><td><dfn style="font-weight:bolder;">seashell</dfn> </td><td style="text-transform: uppercase;">#fff5ee </td><td style="text-transform: uppercase;">255,245,238
    </td></tr><tr>
     <td style="background:sienna"> </td><td style="background:#a0522d"> </td><td><dfn style="font-weight:bolder;">sienna</dfn> </td><td style="text-transform: uppercase;">#a0522d </td><td style="text-transform: uppercase;">160,82,45
    </td></tr><tr>
     <td style="background:silver"> </td><td style="background:#c0c0c0"> </td><td><dfn style="font-weight:bolder;">silver</dfn> </td><td style="text-transform: uppercase;">#c0c0c0 </td><td style="text-transform: uppercase;">192,192,192
    </td></tr><tr>
     <td style="background:skyblue"> </td><td style="background:#87ceeb"> </td><td><dfn style="font-weight:bolder;">skyblue</dfn> </td><td style="text-transform: uppercase;">#87cee </td><td style="text-transform: uppercase;">135,206,235
    </td></tr><tr>
     <td style="background:slateblue"> </td><td style="background:#6a5acd"> </td><td><dfn style="font-weight:bolder;">slateblue</dfn> </td><td style="text-transform: uppercase;">#6a5acd </td><td style="text-transform: uppercase;">106,90,205
    </td></tr><tr>
     <td style="background:slategray"> </td><td style="background:#708090"> </td><td><dfn style="font-weight:bolder;">slategray</dfn> </td><td style="text-transform: uppercase;">#708090 </td><td style="text-transform: uppercase;">112,128,144
    </td></tr><tr>
     <td style="background:slategrey"> </td><td style="background:#708090"> </td><td><dfn style="font-weight:bolder;">slategrey</dfn> </td><td style="text-transform: uppercase;">#708090 </td><td style="text-transform: uppercase;">112,128,144
    </td></tr><tr>
     <td style="background:snow"> </td><td style="background:#fffafa"> </td><td><dfn style="font-weight:bolder;">snow</dfn> </td><td style="text-transform: uppercase;">#fffafa </td><td style="text-transform: uppercase;">255,250,250
    </td></tr><tr>
     <td style="background:springgreen"> </td><td style="background:#00ff7f"> </td><td><dfn style="font-weight:bolder;">springgreen</dfn> </td><td style="text-transform: uppercase;">#00ff7f </td><td style="text-transform: uppercase;">0,255,127
    </td></tr><tr>
     <td style="background:steelblue"> </td><td style="background:#4682b4"> </td><td><dfn style="font-weight:bolder;">steelblue</dfn> </td><td style="text-transform: uppercase;">#4682b4 </td><td style="text-transform: uppercase;">70,130,180
    </td></tr><tr>
     <td style="background:tan"> </td><td style="background:#d2b48c"> </td><td><dfn style="font-weight:bolder;">tan</dfn> </td><td style="text-transform: uppercase;">#d2b48c </td><td style="text-transform: uppercase;">210,180,140
    </td></tr><tr>
     <td style="background:teal"> </td><td style="background:#008080"> </td><td><dfn style="font-weight:bolder;">teal</dfn> </td><td style="text-transform: uppercase;">#008080 </td><td style="text-transform: uppercase;">0,128,128
    </td></tr><tr>
     <td style="background:thistle"> </td><td style="background:#d8bfd8"> </td><td><dfn style="font-weight:bolder;">thistle</dfn> </td><td style="text-transform: uppercase;">#d8bfd8 </td><td style="text-transform: uppercase;">216,191,216
    </td></tr><tr>
     <td style="background:tomato"> </td><td style="background:#ff6347"> </td><td><dfn style="font-weight:bolder;">tomato</dfn> </td><td style="text-transform: uppercase;">#ff6347 </td><td style="text-transform: uppercase;">255,99,71
    </td></tr><tr>
     <td style="background:turquoise"> </td><td style="background:#40e0d0"> </td><td><dfn style="font-weight:bolder;">turquoise</dfn> </td><td style="text-transform: uppercase;">#40e0d0 </td><td style="text-transform: uppercase;">64,224,208
    </td></tr><tr>
     <td style="background:violet"> </td><td style="background:#ee82ee"> </td><td><dfn style="font-weight:bolder;">violet</dfn> </td><td style="text-transform: uppercase;">#ee82ee </td><td style="text-transform: uppercase;">238,130,238
    </td></tr><tr>
     <td style="background:wheat"> </td><td style="background:#f5deb3"> </td><td><dfn style="font-weight:bolder;">wheat</dfn> </td><td style="text-transform: uppercase;">#f5deb3 </td><td style="text-transform: uppercase;">245,222,179
    </td></tr><tr>
     <td style="background:white"> </td><td style="background:#ffffff"> </td><td><dfn style="font-weight:bolder;">white</dfn> </td><td style="text-transform: uppercase;">#ffffff </td><td style="text-transform: uppercase;">255,255,255
    </td></tr><tr>
     <td style="background:whitesmoke"> </td><td style="background:#f5f5f5"> </td><td><dfn style="font-weight:bolder;">whitesmoke</dfn> </td><td style="text-transform: uppercase;">#f5f5f5 </td><td style="text-transform: uppercase;">245,245,245
    </td></tr><tr>
     <td style="background:yellow"> </td><td style="background:#ffff00"> </td><td><dfn style="font-weight:bolder;">yellow</dfn> </td><td style="text-transform: uppercase;">#ffff00 </td><td style="text-transform: uppercase;">255,255,0
    </td></tr><tr>
     <td style="background:yellowgreen"> </td><td style="background:#9acd32"> </td><td><dfn style="font-weight:bolder;">yellowgreen</dfn> </td><td style="text-transform: uppercase;">#9acd32 </td><td style="text-transform: uppercase;">154,205,50
  </td></tr></tbody></table>

+ Complementary and Triadic colour schemes

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://www.w3.org/wiki/Colour_theory">
      <img src="https://www.w3.org/wiki/images/4/49/50000000.jpg" style="margin: 0.1em;" alt="the complementary scheme, where you match up colours that lie directly opposite each other on the colour wheel." title="Complementary colour schemes" width="450">
      <img src="https://www.w3.org/wiki/images/e/e5/80000001.jpg" style="margin: 0.1em;" alt="A triadic colour scheme is created when you pick one colour and then pick two other colours that lie equidistant from each other around the circle." title="Triadic colour schemes" width="300">
    </a></div>
  </div>


## Font Property







-------------------------------------------
<!--
[010]: 
[011]: 
[012]: 
[013]: 
[014]: 
[015]: 
[016]: 
[017]: 
[018]: 
[019]: 
[020]: 
[021]: 
[022]: 
[023]: 
[024]: 
[025]: 
[026]: 
[027]: 
[028]: 
[029]: 
[030]: 
[031]: 
[032]: 
[033]: 
[034]: 
[035]: 
[036]: 
[037]: 
[038]: 
[039]: 
[040]: 
[041]: 
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
[007]: https://github.com/hmchen47/Programming/blob/css/WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#color
[008]: https://www.w3.org/TR/css3-background/#the-background-color
[009]: https://github.com/hmchen47/Programming/blob/css/WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#background-color
