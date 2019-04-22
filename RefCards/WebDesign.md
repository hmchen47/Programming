# Web Design Guideline


## [Accessibility: WCAG2 at a Glance][000]

+ Perceivable

  + Provide __text alternatives__ for non-text content.
  + Provide __captions and alternatives__ for audio and video content.
  + Make content __adaptable__; and make it available to assistive technologies.
  + Use __sufficient contrast__ to make things easy to see and hear.

+ Operable

  + Make all functionality __keyboard accessible__.
  + Give users __enough time__ to read and use content.
  + Do not use content that causes __seizures__.
  + Help users __navigate and find__ content.

+ Understandable

  + Make text __readable and understandable__.
  + Make content appear and operate in __predictable__ ways.
  + Help users __avoid and correct mistakes__.

+ Robust

  + Maximize __compatibility__ with current and future technologies.


## [English Typography][002]

Use the proper English characters instead of their misused equivalents.

+ Quotes
  + `“` (`&#8220;`) opening quote (instead of `"`)
  + `”` (`&#8221;`) closing quote (instead of `"`)
+ Apostrophe
  + `’` (`&#8217;`) apostrophe (instead of `'`)
+ Dashes and Hyphens
  + `–` (`&#8211;` or `&ndash;`) en dash, used for ranges, e.g. “13–15 November” (instead of `-`)
  + `—` (`&#8212;` or `&mdash;`) em dash, used for change of thought, e.g. “Star Wars is—as everyone knows—amazing.” (instead of `-`, or `--`)
+ Ellipsis
  + `…` (`&#8230;` or `&hellip;`) horizontal ellipsis, used to indicate an omission or a pause (instead of `...`)


## [Internationalization Quicktips][001]

+ Use Unicode wherever possible for content, databases, etc. Always declare the encoding of content.
+ Use characters rather than escapes (e.g. `&#xE1`; `&#225`; or `&aacute;`) whenever you can.
+ Declare the language of documents and indicate internal language changes.
+ Use style sheets for presentational information. Restrict markup to semantics.
+ Check for translatability and inappropriate cultural bias in images, animations & examples.
+ Use an appropriate encoding on both form and server. Support local formats of names/addresses, times/dates, etc.
+ Use simple, concise text. Use care when composing sentences from multiple strings.
+ On each page include clearly visible navigation to localized pages or sites, using the target language.
+ For XHTML, add dir="rtl" to the html tag for right-to-left text. Only re-use it to change the base direction.
+ Validate! Use techniques, tutorials, and articles at http://www.w3.org/International/


















---------------------------------------------

<!--
[003]: 
[004]: 
[005]: 
[006]: 
[007]: 
[008]: 
[009]: 
[000]: 
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

[000]: https://www.w3.org/2009/cheatsheet/#wcag2
[001]: https://www.w3.org/2009/cheatsheet/#i18n
[002]: https://www.w3.org/2009/cheatsheet/#typo
