# Hypertext Markup Language (HTML)

## Tools

+ Web Editors
  + [Visual Studio Code][001]
  + [Codepen][000]

+ W3C validators
  + [W3C Validator][002]
  + [Unicorn][003] - W3C's unified validator
  + [Link Checker][004]
  + [Internationalization Checker][005]

+ W3C cheatsheet
  + [W3C cheatsheet][006]


## HTML Template

```html
<!DOCTYPE html> 
<!--It's a best practice to always declare DOCTYPE!-->
<html lang="en">
  <head>
    <title>Title for Tab in Browser</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/style.css"/>
    <style>
      /* code block for CSS & Comment Syntax */
    </style>
  </head>
  <body>
    <!-- CONTENTS HERE / COMMENT Syntax-->
  </body>
</html>
```

+ HTML element Syntax

```html
<tagname>
    My content
</tagname>
```

## Common HTML Tags

| Tag | Description |Attribute |  Link |
|-----|-------------|------|
| `<html>` | root element of a document  | `lang="en"` | [W3C][008], [Common Tags][009] |
| `<head>` | element containing all the metadata for the site | | [W3C][010], [Common Tags][011] |
| `<body>` | element containing all the visible content for the site like text, images, links etc. | | [W3C][012], [Common Tags][013] |
| `<p>` | paragraph, a block of text that is physically separated from adjacent blocks through blank lines | | [W3C][014], [Common Tags][015] |
| `<a>` | By surrounding text with an tag you turn it into a hyperlink. | `href="url"` | [W3C][016], [Common Tags][017] |
| `<img />` | insert an image based on the source | `src="url" alt="text"` | [W3C][018], [Common Tags][019] |
| `<ul>` | "unordered list" element, a collection of elements in which the order is meaningless | | [W3C][020], [Common Tags][021] |
| `<ol>` | "ordered list" element, displayed with a number preceding them | | [W3C][022], [Common Tags][023] |
| `<br />` | a self-closing tag that inserts a line break | | [W3C][024], [Common Tags][025] |
| `<header>` | sectioning element, containing all the introductory content on the page typically a title and tagline or navigational elements | | [W3C][026], [Common Tags][027] |
| `<section>` | sectioning element, a general-purpose grouping element | | [W3C][028], [Common Tags][029] |
| `<footer>` | sectioning element, organizing the final content on the page such as the credits or contact info | | [W3C][030], [Common Tags][031] |
| `<div>` | a generic element to hold content, used to collect together large portions of a site that contain multiple different types of content | | [W3C][032], [Common Tags][033] |










-------------------------------------------

<!--
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

[000]: http://www.codepen.io/
[001]: https://msdn.microsoft.com/en-us/library/02aa8baz(v=vs.80).aspx
[002]: https://validator.w3.org/
[003]: http://validator.w3.org/unicorn/
[004]: http://validator.w3.org/checklink
[005]: https://validator.w3.org/i18n-checker/
[006]: http://www.w3.org/2009/cheatsheet/
[007]: https://www.w3.org/TR/html52/
[008]: https://www.w3.org/TR/2016/WD-html52-20160818/semantics.html#the-html-element
[009]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#html
[000]: https://www.w3.org/TR/2016/WD-html52-20160818/document-metadata.html#the-head-element
[011]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#head
[012]: https://www.w3.org/TR/2016/WD-html52-20160818/sections.html#the-body-element
[013]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#body
[014]: https://www.w3.org/TR/2016/WD-html52-20160818/grouping-content.html#the-p-element
[015]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#p
[016]: https://www.w3.org/TR/2016/WD-html52-20160818/textlevel-semantics.html#elementdef-a
[017]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#a
[018]: https://www.w3.org/TR/2016/WD-html52-20160818/semantics-embedded-content.html#the-img-element
[019]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#img-
[020]: https://www.w3.org/TR/2016/WD-html52-20160818/grouping-content.html#the-ul-element
[021]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#ul-
[022]: https://www.w3.org/TR/2016/WD-html52-20160818/grouping-content.html#the-ol-element
[023]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#ol
[024]: https://www.w3.org/TR/2016/WD-html52-20160818/textlevel-semantics.html#the-br-element
[025]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#br-
[026]: https://www.w3.org/TR/2016/WD-html52-20160818/sections.html#the-header-element
[027]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#header
[028]: https://www.w3.org/TR/2016/WD-html52-20160818/sections.html#the-section-element
[029]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#section
[030]: https://www.w3.org/TR/2016/WD-html52-20160818/sections.html#the-footer-element
[031]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#footer
[032]: https://www.w3.org/TR/2016/WD-html52-20160818/grouping-content.html#the-div-element
[033]: ../WebDev/Frontend-W3C/4-CSSBasics/02-CSSRules.md#div
