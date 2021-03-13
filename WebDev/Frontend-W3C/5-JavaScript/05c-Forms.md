# Module 5: Working with forms


## 5.3 HTML5 tables, forms and input fields


#### 5.3.1 The HTML table basics

The `<table>` element helps with rendering tables in an HTML document.  

Each table row is defined with the `<tr>` tag (<b>T</b>able <b>R</b>ow). A table header is defined with the `<th>` tag (<b>T</b>able <b>H</b>eader). By default, table headings are bold and centered. A table data/cell is defined with the `<td>` tag (<b>T</b>able Data). In each cell, you can have other HTML elements/tags. You can have only "column table headers" (the first row of the table will be in bold), or you can also have "row headers" (first cell of each row).

__Best practice for making the table accessible:__ always add a `<caption>` tag inside the `<table>` tag. Data tables very often have brief descriptive text before or after the table that indicates the content of that table. This text should be associated to its respective table using the `<caption>` element. The `<caption>` element must be the first thing after the opening `<table>` tag.

__Second best practice for accessibility:__ use a scope attribute with all `<th scope = "row or column">` for identifying whether a table header is a column header or a row header. We invite you to read [these guidelines](https://www.w3.org/WAI/tutorials/tables/) for making accessible tables.

Typical example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;table&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; <strong>&lt;caption&gt;</strong></span><strong><span class="pln">A typical HTML table</span><span class="tag">&lt;/caption&gt;</span></strong><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;tr&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;th</span><span class="pln"> </span><strong><span class="atn">scope</span><span class="pun">=</span><span class="atv">"col"</span></strong><span class="tag">&gt;</span><span class="pln">Given Name</span><span class="tag">&lt;/th&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;th</span><span class="pln"> </span><strong><span class="atn">scope</span><span class="pun">=</span><span class="atv">"col"</span></strong><span class="tag">&gt;</span><span class="pln">Family Name</span><span class="tag">&lt;/th&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;th</span><span class="pln"> </span><strong><span class="atn">scope</span><span class="pun">=</span><span class="atv">"col"</span></strong><span class="tag">&gt;</span><span class="pln">Age</span><span class="tag">&lt;/th&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;/tr&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;tr&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;td&gt;</span><span class="pln">Michel</span><span class="tag">&lt;/td&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;td&gt;</span><span class="pln">Buffa</span><span class="tag">&lt;/td&gt;</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;td&gt;</span><span class="pln">52</span><span class="tag">&lt;/td&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;/tr&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;tr&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;td&gt;</span><span class="pln">Dark</span><span class="tag">&lt;/td&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;td&gt;</span><span class="pln">Vador</span><span class="tag">&lt;/td&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;td&gt;</span><span class="pln">Unknown</span><span class="tag">&lt;/td&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;/tr&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;tr&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;td&gt;</span><span class="pln">Luke</span><span class="tag">&lt;/td&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;td&gt;</span><span class="pln">Skywalker</span><span class="tag">&lt;/td&gt;</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;td&gt;</span><span class="pln">Unknown</span><span class="tag">&lt;/td&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;/tr&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/table&gt;</span></li>
</ol></div>

Most of the time, we add some CSS rules for rendering cell/row/table borders and for adjusting spacing between the text in the cells and the cell borders. Let's look at some examples.

#### Examples

__Example #1: HTML table with a very light CSS styling__

[CodePen Demo](https://codepen.io/w3devcampus/pen/vmNQNQ)

[Local Demo](src/05c-example01.html)

This is a static table. You can look at the CSS code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">table </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; width</span><span class="pun">:</span><span class="lit">100</span><span class="pun">%;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; border</span><span class="pun">:</span><span class="lit">1px</span><span class="pln"> solid</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">tr</span><span class="pun">,</span><span class="pln"> th</span><span class="pun">,</span><span class="pln"> td </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; border</span><span class="pun">:</span><span class="lit">1px</span><span class="pln"> solid</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; font</span><span class="pun">-</span><span class="pln">family</span><span class="pun">:</span><span class="pln">courier</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">td </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; text</span><span class="pun">-</span><span class="pln">align</span><span class="pun">:</span><span class="pln">center</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; padding</span><span class="pun">:</span><span class="lit">10px</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Explanations:

+ _Line 1_: this rule says that the table will occupy the width of the window and will have a black, continuous border that is one pixel wide.
+ _Line 7_: this rule says that table rows, table cells and table headers will also have a border and will use the font family Courier.
+ _Line 12_: this says that all cells will have the text horizontally centered and an internal margin (called padding) of 10px in each direction (top, bottom, left, right).

__Example #2: with more CSS styling (flat design)__

[CodePen Demo](https://codepen.io/w3devcampus/pen/MmKYNx)

[Local Demo](src/05c-example02.html)

__Example #3: with colored lines, header, footer, legend__

Look at the CSS - it's the only part that changed:

[CodePen Demo](https://codepen.io/w3devcampus/pen/gWPppo)

[Local Demo](src/05c-example02.html)


#### Notes for 5.3.1 The HTML table basics

+ The `<table>` and related elements
  + `<table>` element: rendering tables in an HTML document
  + `<tr>` element: table row
  + `<th>` element: table header, defaults as bold and centered
  + `<td>` element: a table data/cell
  + best practice for accessibility
    + always add a `<caption>` tag inside the `<table>` tag
    + use a `scope` attribute w/ all `<th scope="row or column">` for identifying whether a table header is a column header or a row header

+ Common styles for `<table>` element
  + rendering cell/row/table border, e.g., `tr, th, td { border: 1px solid; }`
  + adjusting spacing btw text in cells and the cell borders, e.g., `td { padding: 10px; }`


### 5.3.2 The HTML table JavaScript API


#### Live coding video: HTML table JavaScript API

<a href="https://edx-video.net/W3CJSIXX2016-V005400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/b785tczx)

__Source code from the above video__

[CodePen Demo](https://codepen.io/w3devcampus/pen/LLLrao?editors=0010)

[Local Demo](src/05c-example04.html)

There is a JavaScript API associated with the HTML table elements that makes dynamic table management possible, enabling you to add or delete a row, add or delete a cell, modify the content of the cells, etc.

We've already seen some examples in the course, but we have not completely covered the table JavaScript API.


#### The table object (`<table>`)

When you look for a table using the DOM API or the selector API, or when you create a table using the DOM API, you get a Table object:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> table </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"myTable"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> table </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myTable"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> table </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">"table"</span><span class="pun">);</span><span class="pln"> </span><span class="com">// creates a new table</span></li>
</ol></div>

Like all objects, an instance of Table will have properties and methods:

<table style="table-layout: auto; border: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif;" cellspacing="0" cellpadding="5" border="0" align="center">
  <tbody>
  <tr>
  <td style="padding: 5px; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray; text-align: center;" colspan="2">Most useful properties</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><strong><span style="font-family: 'courier new', courier;">rows</span></strong></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Returns a collection of all <strong><span style="font-family: 'courier new', courier;">&lt;tr&gt;</span></strong> elements in a table</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><strong><span style="font-family: 'courier new', courier;">caption</span></strong></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Returns the <strong><span style="font-family: 'courier new', courier;">&lt;caption&gt;</span></strong> element of a table</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><strong><span style="font-family: 'courier new', courier;">tFoot</span></strong></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Returns a reference to the <span style="font-family: 'courier new', courier;"><strong>&lt;tfoot&gt;</strong></span> element of a table</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><strong><span style="font-family: 'courier new', courier;">tHead</span></strong></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Returns a reference to the <span style="font-family: 'courier new', courier;"><strong>&lt;thead&gt;</strong></span> element of a table</td>
  </tr>
  </tbody>
</table>

<table style="table-layout: auto; border: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif;" cellspacing="0" cellpadding="5" border="0" align="center">
  <tbody>
  <tr>
  <td style="padding: 5px; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray; text-align: center;" colspan="2">Most useful methods</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>insertRow()</strong></span></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Creates an empty <span style="font-family: 'courier new', courier;"><strong>&lt;tr&gt;</strong></span> element and adds it to the table. Example:&nbsp;<span style="font-family: 'courier new', courier;"><strong>var row = table.insertRow();</strong></span> inserts a new row at the end of the table. <strong><span style="font-family: 'courier new', courier;">var row = table.insertRow(0);</span></strong> inserts at index = 0, <span style="font-family: 'courier new', courier;"><strong>var row = table.insertRow(10);</strong></span> inserts at index = 10, and pushes all the rows after this index.<br style="color: #424242; font-family: 'Open Sans', sans-serif;"><br></td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>deleteRow()</strong></span></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Removes a row (<span style="font-family: 'courier new', courier;"><strong>&lt;tr&gt;</strong></span>) from the table. Example <strong><span style="font-family: 'courier new', courier;">table.deleteRow(0)</span></strong>; deletes the row at index 0.</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><strong><span style="font-family: 'courier new', courier;">createCaption()</span></strong></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Creates an empty <span style="font-family: 'courier new', courier;"><strong>&lt;caption&gt;</strong></span> element and adds it to the table</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>deleteCaption()</strong></span></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Removes the first <span style="font-family: 'courier new', courier;"><strong>&lt;caption&gt;</strong></span> element from the table</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>createTHead()</strong></span></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Creates an empty <span style="font-family: 'courier new', courier;"><strong>&lt;thead&gt;</strong></span> element and adds it to the table</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>deleteTHead()</strong></span></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Removes the <span style="font-family: 'courier new', courier;"><strong>&lt;thead&gt;</strong></span> element from the table</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>createTFoot()</strong></span></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Creates an empty <span style="font-family: 'courier new', courier;"><strong>&lt;tfoot&gt;</strong></span> element and adds it to the table</td>
  </tr>
  <tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>deleteTFoot()</strong></span></td>
  <td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Removes the <span style="font-family: 'courier new', courier;"><strong>&lt;tfoot&gt;</strong></span> element from the table</td>
  </tr>
  </tbody>
</table>

Example that adds a new row or removes a row to/from a table using the insertRow()/deleteRow() methods:

[CodePen Demo](https://codepen.io/w3devcampus/pen/aWdOgw)

[Local Demo](src/05c-example05.html)

Notice the use of row.innerHTML= here to add some cells to the row. We will soon see another method for doing this.


#### The tableRow object (`<tr>`)

When you look for a row using the DOM API or the selector API, or when you create a row using the DOM API, you get a Row object:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="kwd">var</span><span class="pln">&nbsp;row1&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"row1"</span><span class="pun">);</span></li>
<li class="L1"><span class="pln">&nbsp;</span></li>
<li class="L2"><span class="kwd">var</span><span class="pln">&nbsp;row1&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#row1"</span><span class="pun">);</span></li>
<li class="L3"><span class="pln">&nbsp;</span></li>
<li class="L4"><span class="kwd">var</span><span class="pln">&nbsp;newRow&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">"row"</span><span class="pun">);</span><span class="pln">&nbsp;</span><span class="com">// creates a new&nbsp;row</span></li>
</ol></div>

You can also access a row from the rows property of a table:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> t </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">"table"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> r1 </span><span class="pun">=</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">insertRow</span><span class="pun">(</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> r1</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"&lt;td&gt;Hello&lt;/td&gt;"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">"&lt;td&gt;Hello&lt;/td&gt;"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> r2 </span><span class="pun">=</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">insertRow</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> r2</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"&lt;td&gt;Hello 2&lt;/td&gt;"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">"&lt;td&gt;Hello 2&lt;/td&gt;"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><strong><span class="kwd">var</span><span class="pln"> row1 </span><span class="pun">=</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">rows</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> row1</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="str">&lt;tr&gt;</span><span class="pun">&lt;</span><span class="pln">td</span><span class="pun">&gt;</span><span class="typ">Hello</span><span class="pun">&lt;</span><span class="str">/td&gt;&lt;/</span><span class="pln">tr</span><span class="pun">&gt;</span></li>
</ol></div>

Like all objects, a `tableRow` object has properties and methods. Here are the most useful ones:

<table style="table-layout: auto; border: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif;" cellspacing="0" cellpadding="5" border="0" align="center">
<tbody>
<tr>
<td style="padding: 5px; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray; text-align: center;" colspan="2">Most useful&nbsp;properties</td>
</tr>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><strong><span style="font-family: 'courier new', courier;">cells</span></strong></td>
<td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Returns a collection of all &lt;<strong><span style="font-family: 'courier new', courier;">td&gt;</span></strong> or <span style="font-family: 'courier new', courier;"><strong>&lt;th&gt;</strong></span> elements in a table row</td>
</tr>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>rowIndex</strong></span></td>
<td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Returns the position of a row in the <strong><span style="font-family: 'courier new', courier;">rows</span></strong> collection of a table</td>
</tr>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>sectionRowIndex</strong></span></td>
<td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Returns the position of a row in the <strong><span style="font-family: 'courier new', courier;">rows</span></strong> collection of a <span style="font-family: 'courier new', courier;"><strong>&lt;tbody&gt;</strong></span>, <span style="font-family: 'courier new', courier;"><strong>&lt;thead&gt;</strong></span>, or <span style="font-family: 'courier new', courier;"><strong>&lt;tfoot&gt;</strong></span></td>
</tr>
</tbody>
</table>


<table style="border: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif;" width="640" cellspacing="0" cellpadding="5" border="0" align="center">
<tbody>
<tr>
<td style="padding: 5px; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray; text-align: center;" colspan="2">Most useful methods</td>
</tr>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>insertCell()</strong></span></td>
<td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Inserts a cell into the current table row. Without parameters, appends a cell after the last cell of the row. You can pass the index of the cell as a unique parameter, in which case other cells are "pushed" to the right. The value of 0 results in the new cell&nbsp;being inserted at the first position. The value of -1 can also be used, which results in the new cell&nbsp;being inserted&nbsp;in the last position.</td>
</tr>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'courier new', courier;"><strong>deleteCell()</strong></span></td>
<td style="background-color: white; border: 2px solid LightSlateGray;" valign="top">Deletes a cell from the current table row. There is&nbsp;one parameter for this method: the index of the cell to remove. The value of 0 results in the deletion of the first cell. The value of -1 can also be used, which results in the deletion of the last cell.</td>
</tr>
</tbody>
</table>

Below are new versions of the previous examples, but instead of using the `innerHTML` of the `TableRow` object, we use the `insertCell()` method.

[CodePen Demo](https://codepen.io/w3devcampus/pen/OmMmGr)

[Local Demo](src/05c-example06.html)

Notice how we've created the new row cells:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> insertRow</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> table </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myTable"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // without parameters, insert at the end,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // otherwise parameter = index where the row will be inserted</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> row </span><span class="pun">=</span><span class="pln"> table</span><span class="pun">.</span><span class="pln">insertRow</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; <strong>var</strong></span><strong><span class="pln"> cell1 </span><span class="pun">=</span><span class="pln"> row</span><span class="pun">.</span><span class="pln">insertCell</span><span class="pun">();</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; cell1</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"New cell1"</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; <strong>var</strong></span><strong><span class="pln"> cell2 </span><span class="pun">=</span><span class="pln"> row</span><span class="pun">.</span><span class="pln">insertCell</span><span class="pun">();</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; cell2</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"New cell2"</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> cell3 </span><span class="pun">=</span><span class="pln"> row</span><span class="pun">.</span><span class="pln">insertCell</span><span class="pun">();</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; cell3</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"New cell3"</span><span class="pun">;&nbsp;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

So should we use `insertCell()` or just `row.innerHTML="<td>...</td>"`?

It's up to you: depending on the HTML that you plan to insert into each cell, one version may be more readable than the other.


#### Notes for 5.3.2 The HTML table JavaScript API

+ The table object
  + make dynamic table management possible
  + enable to add or delete a row, a cell, and modify the contents of the cells, etc.
  + most useful properties
    + `rows`: a collection of all `<tr>` elements in a table
    + `caption`: the `<caption>` element of a table
    + `tFoot`: a reference to the `<tfoot>` element of a table
    + `tHead`: a reference to the `<thead>` element of a table
  + most useful methods
    + `insertRow()`:
      + create an empty `<tr>` element and add it to the table
      + insert a new row at the end of the table: `var row = table.insertRow();`
      + insert at the index = `idx` and push down all the rows after: `var row = table.insertRow(idx);`
    + `deleteRow()`: remove a row `<tr>` from the table, e.g., `table.deleteRow(0);` delete the row at index 0
    + `createCaption()`: create an empty `<caption>` element and add it to the table
    + `deleteCaption()`: remove the first `<caption>` element from the table
    + `createTHead()`: create an empty `<thead>` element and add it to the table
    + `deleteTHead()`: remove the `<thead>` element from the table
    + `createTFoot()`: create an empty `<tfoot>` element and add it to the table
    + `deleteTFoot()`: remove the `<tfoot>` element from the table

+ Examples: [table object](src/05c-example04.html)
  + access table: `var table = document.getElementById("myTable);` and `var table = document.querySelector("#myTable");`
  + create a new table: `var table = document.createElement("table");`
  + insert last row: `function insertRow() { var table = document.querySelector("#myTable"); var row = table.insertRow(); row.innerHTML = "<td>New</td><td>New</td><td>New</td>"; }`
  + delete the first row: `function deleteRow() { var table = document.querySelector("#myTable"); table.deleteRow(1); // o is the header }`

+ The tableRow object (`<tr>`)
  + access a row using the DOM API or the selector API
  + create a row using the DOM API to get a Row object
  + most useful properties
    + `cells`: a collection of all `<td>` ot `<th>` elements in a table row
    + `rowIndex`: the position of a row in the `rows` collection of a table
    + `sectionRowIndex`: the position of a row in the `rows` collection of a `<tbody>`, `<thead>` or `<tfoot>`
  + most useful methods
    + `insertCell()`:
      + insert a cell into the current table `row`
      + no parameters: append a cell after the last cell of the row
      + index of the cell as a unique parameter: insert the row and push other cells to the right
      + `index = 0`: insert at the first position
      + `index = -1`: insert at the last position
    + `deleteCell()`:
      + delete a cell from the current table row
      + unique parametre: the index of the cell to remove
      + `index = 0`: delete the first cell
      + `index = -1`: delete the last cell

+ Example: [tableRow object](src/05c-example05.html)
  + access row: `var row1 = document.getElementById("row1"); var row = document.querySelector("#row1");`
  + create a new row: `var newRow = document.createElement("row");`
  + create a table: `var t = document.createElement("table");`
  + insert 1st row and add cells: `var r1 = t.insertRow(0); r1.innerHTML = "<td>Hello</td>`
  + append a row w/ cell: `var r2 = t.insertRow(); r2.innerHTML = "<td>Hello 2</td>`
  + access 1st row of the table: `var row1 = t.rows[0]; row1; // <tr><td>Hello</td></tr>`

+ Example: [create new row cells](src/05c-example06.html) `function insertRow() {...}`
  + access table: `var table = document.querySelector("#myTable");`
  + append a new row: `var row = table.insertRow();`
  + insert cells: `var cell1 = row.insertCell(); cell1.innerHTML = "New cell1"; var cell2 = row.insertCell(); cell2.innerHTML = "New cell2"; var cell3 = row.insertCell(); cell3.innerHTML = "New cell3";` 


### 5.3.3 HTML forms: best practices

#### Creating accessible forms

Forms are commonly used to enable user interaction within Web sites and Web applications, for example, for login, registering, commenting, and purchasing.

Since HTML5 provides functionalities to assist with accessibility, developers should make a concerted effort to mark up Web based forms. The following two guidelines are to give you a good start to make your forms accessible:

1. For every form field, ensure that a descriptive __label__ is provided and use the `<label>` element to identify each form control.
1. For larger or complex forms, use the `<fieldset>` and `<legend>` elements to respectively __group and associate__ related form controls.

Further reading:

The WAI Web site hosts a [Forms tutorial](https://www.w3.org/WAI/tutorials/forms/) where you will find more guidelines to help make your forms truly accessible: Form Instructions, Validating Input, User Notifications, Multi-Page Forms, and Custom Controls.


#### Why is this important?

Forms can be visually and cognitively complex and difficult to use. Accessible forms are easier to use for everyone, including people with disabilities.

+ __People with cognitive disabilities__ can more easily understand the form and how to complete it, as making forms accessible improves the layout structure, instructions, and feedback.
+ __People using speech input__ can use the labels via voice commands to activate controls and move the focus to the fields that they need to complete.
+ __People with limited dexterity__ benefit from large clickable areas that include the labels, especially for smaller controls, such as radio buttons and checkboxes.
+ __People using screen readers__ can identify and understand form controls more easily because they are associated with labels, field sets, and other structural elements.


#### Labeling controls

__Labels need to describe the purpose of the form control__

Form fields and other form controls usually have visible labels, such as "E-mail Address:" as the label for a text field (see figure below).

<p><img class="imgbreathe" src="https://www.w3.org/WAI/images/easychecks/form-label-text.png" type="saveimage" target="[object Object]" alt="Visual of a text input field preceded by the mention &quot;E-mail address:&quot;" width="242" height="29"></p>

When these labels are marked up correctly, people can interact with them using only the keyboard, using voice input, and using screen readers. Also, the label itself becomes clickable, which enables a person who has difficulty clicking on small radio buttons or checkboxes to click anywhere on the label text.


#### Associating labels explicitly

Whenever possible, use the `label` element to explicitly associate text with form elements. The `for` attribute of the label must exactly match the `id` of the form control.

Example #1 (click on the label, not on the input field to see the effect):

<div class="box-content"><form action="#" method="post">
<p class="exampleHTML"><label class="label" for="first_name">First name: </label> <input name="firstname" id="first_name" type="text"></p>
</form></div>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"first_name"</span><span class="tag">&gt;</span><span class="pln">Your First Name</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"first_name"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"fname"</span><span class="tag">/&gt;</span></li>
</ol></div>

Alternative example #1:

Note that you can also include the `<input>` element inside the `<label>...</label>` element, and also add a `<span lang="en">` for example, to indicate the language used in the label. Sometimes, [nesting labels and inputs can also make CSS styling easier and produce better results with screen readers](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/How_to_structure_an_HTML_form).

Source code (with `<input>` inside the `<label>`):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"first_name"</span><span class="tag">&gt;&lt;</span></strong><span class="pln"><strong>span lang=en"&gt;</strong>Your First Name</span><strong><span class="tag">&lt;/span&gt;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"first_name"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"fname"</span><span class="tag">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="tag">&lt;/label&gt;</span></strong></li>
</ol></div>

Example #2 (click on the label "Subscribe to newsletter" to see the effect):

<div class="box-content"><form action="#" method="post">
<p class="exampleHTML"><label class="label" for="firstname">First name: </label> <input name="firstname" id="firstname" type="text"><br><label class="label" for="subscribe">Subscribe to newsletter</label> <input name="subscribe" id="subscribe" type="checkbox"></p>
</form></div>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"firstname"</span><span class="tag">&gt;</span><span class="pln">First name:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"firstname"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"firstname"</span><span class="tag">&gt;&lt;br&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;label</span><span class="pln">&nbsp;</span><span class="atn">for</span><span class="pun">=</span><span class="atv">"subscribe"</span><span class="tag">&gt;</span><span class="pln">Subscribe to newsletter</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"checkbox"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"subscribe"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"subscribe"</span><span class="tag">&gt;</span></li>
</ol></div>


#### Labeling buttons

The label of a `<button>` element is set inside the element and can include markup. This allows advanced accessibility hints to be included, such as marking up language change.

Example: `<button>Mon <span lang="fr">bouton</span></button>`, for a button with a label in French.

When using the `<input>` element to create buttons, the label is set in the `value` attribute of the element.

Example: `<input type="submit" value="Please submit">`, will be rendered as a button.

Source code for an example of "Submit" and "Cancel" buttons:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"submit"</span><span class="tag">&gt;</span><span class="pln">Submit</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"button"</span><span class="tag">&gt;</span><span class="pln">Cancel</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"submit"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"Submit"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"button"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"Cancel"</span><span class="tag">&gt;</span></li>
</ol></div>

These will produce the same results:

<p class="exampleHTML">Lines 1 and 2 render as:<br><button type="submit">Submit</button> <button type="button">Cancel</button><br><br>While lines 3 and 4 render as:<br> <input value="Submit" type="submit"> <input value="Cancel" type="button"></p>

#### Labeling text areas

<p><label class="label" for="address">Enter your address:</label><br> <textarea name="addresstext" id="address" rows="5" cols="25"></textarea></p>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"address"</span><span class="tag">&gt;</span><span class="pln">Enter your address:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;br&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;textarea</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"address"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"addresstext"</span><span class="tag">&gt;&lt;/textarea&gt;</span></li>
</ol></div>


#### Grouping controls

Groupings of form controls, typically groups of related checkboxes and radio buttons, sometimes require a higher level description. Grouping related form controls makes forms more understandable for all users, as related controls are easier to identify.

__Associating related controls with `fieldset`__

Grouping needs to be carried out visually and in the code, for example, by using the `<fieldset>` and `<legend>` elements to associate related form controls. The `<fieldset>` identifies the entire grouping and `<legend>` identifies the grouping's descriptive text.

__Example #1: Radio buttons__

In the example below, there are three radio buttons that allow the user to choose an output format. Radio button groups should always be grouped using `<fieldset>`.

<form><fieldset><legend>Output format</legend> <input name="format" id="txt" value="txt" type="radio"> <label class="label" for="txt">Text file<br></label><br> <input name="format" id="csv" value="csv" type="radio"> <label class="label" for="csv">CSV file<br></label><br> <input name="format" id="html" value="HTML" type="radio"> <label class="label" for="html">HTML file</label></fieldset></form>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;fieldset&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;legend&gt;</span><span class="pln">Output format</span><span class="tag">&lt;/legend&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &lt;div&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"radio"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"format"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"txt"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"txt"</span><span class="pln"> </span><span class="atn">checked</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"txt"</span><span class="tag">&gt;</span><span class="pln">Text file</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &lt;/div&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;div&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"radio"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"format"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"csv"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"csv"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"csv"</span><span class="tag">&gt;</span><span class="pln">CSV file</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;/div&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> […]</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/fieldset&gt;</span></li>
</ol></div>

__Example #2: Checkboxes__

In the example below, there are three checkboxes that are all part of an opt-in function for receiving different types of information.

<form action="#" method="post"><fieldset><legend>I want to receive</legend>
<div><input name="newsletter" id="check_1" type="checkbox"> <label class="label" for="check_1">The weekly newsletter</label></div>
<div><input name="company_offers" id="check_2" type="checkbox"> <label class="label" for="check_2">Offers from the company</label></div>
<div><input name="assoc_offers" id="check_3" type="checkbox"> <label class="label" for="check_3">Offers from associated companies</label></div>
</fieldset></form>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;fieldset&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;legend&gt;</span><span class="pln">I want to receive</span><span class="tag">&lt;/legend&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;div&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"checkbox"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"newsletter"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"check_1"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"check_1"</span><span class="tag">&gt;</span><span class="pln">The weekly newsletter</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;/div&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;[…]</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/fieldset&gt;</span></li>
</ol></div>


#### [Advanced] Associating related controls with WAI-ARIA

WAI-ARIA provides a grouping role that functions in a similar way to `fieldset` and `legend`. For example, a div element can have `role=group` to indicate that the contained elements are members of a group.

WAI-ARIA roles are very important in the accessibility world, and we invite you to see an example provided in the [associated WAI tutorial](https://www.w3.org/WAI/tutorials/forms/grouping/). Find also another [WAI-ARIA documentation on MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA).


#### Notes for 5.3.3 HTML forms: best practices

+ Accessible forms
  + commonly used to enable user interaction within Web sites and Web applications
  + guidelines
    + descriptive label: ensure provided and use the `<label>` element to identify each from the control
    + complex forms: use the `<fieldset>` and `<legend>` elements to respectively group and associate related form controls
  + reference: [Web Accessibility Tutorials in WIA](https://www.w3.org/WAI/tutorials/forms/)
    + for instructions
    + validating input
    + user notifications
    + multi-page forms
    + custom controls

+ Label in accessible forms
  + describe the purpose of the form control `Form` field
  + label controls
    + marked up correctly: interact using only keyboard, voice input, and screen readers
    + clickable: enable a person who has difficulty clicking on small radio buttons or checkboxes to click anywhere on the the label text
  + associating labels explicitly
    + explicitly associating text w/ form elements
    + `for` attribute of the label exactly match the `id` of the form control, e.g. <br>`<label for="first_name">Your First Name</label>  <input id="first_name" type="text" name="fname"/>`
    + including the `<input>` element inside the `<label>...</label>` and add a `<span lang="en">` to indicate the language used in label, e.g., <br>`<label for="first_name"><span lang="en">Your First Name</span> <input id="first_name" type="text" name="fname"/> </label>`
  + labeling buttons
    + set inside the `<button>` element
    + allow advanced accessibility hints
    + `<input>` element to create button: set label in the `value` attribute of the element
    + examples:
      + a button w/ a label in French: `<button>Mon <span lang="fr">button</span></button>`
      + a button w/ `<button>` element: `<button type="submit">Submit</button>` and `<button type="button">Cancel</button>`
      + a button w/ `<input>` element: `<input type="submit" value="Submit">` and `<input type="button" value="Cancel">`
  + labeling text areas: `<label for="address">Enter your address:</label> <br> <textarea id="address" name="addresstext"></textarea>`

+ Grouping controls of accessible forms
  + typically groups of related checkbox and radio buttons
  + usually requiring a higher level description
  + grouping related forms: easier to understandable for all users
  + associating related controls w/ `fieldset`
    + grouping carried out visually and in the code
    + using `<fieldset>` and `<legend>` elements to associate related form controls
    + `<fieldset>`: identify the entire grouping
    + `<legend>`: identify the group's descriptive text
  + [Grouping Controls](https://www.w3.org/WAI/tutorials/forms/grouping/)
    + approach 1: associating related controls w/ `fieldset`
    + approach 2: associating related controls w/ WAI-ARIA, `aria-labelledby` attribute
  
+ Examples: radio buttons
  + radio buttons allowing the user to choose an output form
  + radio button group: `<fieldset>...<fieldset>`
  + description of group: `<legend>Output format</legend>`
  + radio button and label: `<div><input type="radio" name="format" id="txt" checked> <label for="txt">Text file</label></div>`

+ Example: checkboxes
  + checkboxes are all part of an opt-in function for receiving different types of info
  + checkbox group: `<fieldset>...</fieldset>`
  + description of group: `<legend>I want to receive</legdend>`
  + checkbox and label: `<div> <input type="checkbox" name="newsletter" id="check_1"><label for="check_1">The weekly newsletter</label>`


### 5.3.4 HTML forms and JavaScript


#### Live coding video: HTML Forms Best Practices

<a href="https://edx-video.net/W3CJSIXX2016-V004900_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/rkufhjv4)

__Source code from the example shown in the above video__

[CodePen Demo](https://codepen.io/w3devcampus/pen/ZyJXBe)

[Local Demo](src/05c-example07.html)

We highly recommend that you follow the W3Cx [HTML5 Coding essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) course that has an entire module dedicated to HTML5 forms. 

Forms are a way to get user input which is either sent to a remote server, or processed locally, or both.

This section of the course only covers local processing and the client-side part, with a focus on JavaScript processing.

Typical example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/ZKQJBR)

[Local Demo](src/05c-example08.html)


#### HTML form input can be sent to a server without JavaScript

If a form's content is sent to a remote server, on the server side, you may have PHP, Java, C#, Ruby, Python, etc. components. There are several ways to collect server-side data from a form in a Web page: REST Web services, servlets, Microsoft ASP pages, etc. 

On the client side, the forms indicate to which server and how the data should be sent,  using the `action` and `method` attributes respectively. A `<button type="submit">` or an `<input type=submit>` field is used to submit the form content.

For example: `<form action="myServerCode.php" method="POST">...</form>`. Here, we set the URL of the server side code (`myServerCode.php`), and the HTTP method that will be used by the browser for sending the form content (`POST`).

Example of HTML5 form that will not be sent if invalid input fields are present. Notice that the JavaScript part is only used for giving feedback while entering the password. No JavaScript is used for sending the form data, or for complex, global validation:

[CodePen Demo](https://codepen.io/w3devcampus/pen/pPgWoq)

[Local Demo](src/05c-example09.html)


#### HTML form input can be sent using Ajax / JavaScript

Another approach is to use JavaScript for sending the form content with Ajax. This will be covered in the JavaScript advanced course, to be be available on W3Cx.

__JavaScript can be used for validating user input "on the fly"__

While one is typing or selecting a color, or moving a slider, JavaScript event listeners can be used to track the user's interactions in real time, and perform some validation steps along with giving visual feedback.

We've already seen how we can track the keys typed in an input field in real time:

[CodePen Demo](https://codepen.io/w3devcampus/pen/XMQpRa)

[Local Demo](src/05c-example10.html)

__JavaScript can be used for a more global validation before sending a form to a remote server__

Example: checking that a password entered twice is identical in two different input fields, that some values are coherent (e.g. a birthday cannot be in the future), etc.


[CodePen Demo](https://codepen.io/w3devcampus/pen/gWPxvL)

[Local Demo](src/05c-example11.html)


__JavaScript can be used to make a WebApp that uses form data locally, perhaps with some client-side persistence API__

For example, a contact manager that will work offline, saving data locally, in a database inside the browser. Data will be displayed in a dynamic HTML table, without the need for a remote database.

This is the small project we will build together at the end of the course. :-)


#### Notes for 5.3.4 HTML forms and JavaScript

+ HTML input submit w/o JavaScript
  + several ways to collect server-side data from a form in Web page: REST Web service, servlets, MS ASP pages, etc.
  + client-side forms indicate to which server and how the data sent by `action` and `method` attributes, respectively
  + `<button type="submit">` and `<input type=submit>` used to submit the form content
  + example: `<form action="myServerCode.php" method="POST">...</form>`
    + `myServerCode.php`: set the URL of the server side code
    + `POST`: the HTTP method used by the browser for sending the form content

+ Example: [HTML5 input forms and submit](src/05c-example09.html)

+ HTML input submit w/ Ajax/JavaScript
  + JS used for validating user input "on the fly"
  + event listeners used for tracking user's interactions in real time, including typing or selecting a color, moving a slide, etc.
  + perform validation steps along w/ visual feedback
  + used for more global validation before sending a form to a remote server, e.g., checking password by entering twice in two different fields
  + used to make a WebApp using form data locally, perhaps w/ some client-side persistence API, e.g. data displayed in a dynamic HTML table w/o remote database but saving data locally

+ Example: [validate input on the fly](src/05c-example10.html)
  + register even listener: `<label> <span>Name (required):</span> <input type="text"  name="nom"  maxlength="32"  required onkeyup = "validateName(event)"> </label>`
  + container to display key stroke: `<span id="keyTyped"></span>`
  + validate input name: `function validateName(evt) {...}`
    + declare variables: `var key = evt.key;`
    + access display container: `var output = document.querySelector('#keyTyped');`
    + display key typed: `output.innerHTML = "Valid key: " + key;`
    + validation function here

+ Example: [password consistence check](src/05c-example11.html)
  + submit form: `<form class="myForm" onsubmit="return submitForm();">`
  + two input fields: `<label for="password1" >Password:</label> <input type="password" id="password1" oninput="checkPasswords()" required> <br> <label for="password2">Repeat password:</label> <input type="password" id="password2" oninput="checkPasswords()" required>`
  + password consistence check: `function checkPasswords() {...}`
    + access two password fields: `var password1 = document.querySelector('#password1'); var password2 = document.querySelector('#password2');`
    + password consistent check: `if (password1.value !== password2.value) {...}`
    + invalid: `password2.setCustomValidity('Passwords are different');`
    + valid: `password2.setCustomValidity('');`
  + submit form check: `function submitForm() {...}`
    + append a display info: `document.body.append("We can submit, the form is valid!");`
    + validation varied w/ the requirements


### 5.3.5 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics

+ HTML5 tables are some of the most complicated elements, and there are lots of tricks to make them nice and reactive using CSS3 styles. Please share in the forum some of the best looking tables you find.
+ There exist external JavaScript libraries for making "datatables", i.e., HTML tables especially made for displaying structured data. Do you know some of them and can you share your experiences and examples that use them in the forum? What do you think of them?

#### Optional projects

+ Add a search input field + a search button to the dynamic table example. Add some more data in the table. Implement a search feature: when you search for "Ian Solo", for example, highlight the table row that contains it. If not found, display a message in the page, next to the search form.
+ Please make a big table (with a few hundred rows containing structured data). _Tip_: use loops and random values. For example, use an array of names, an array of cities, an array of zip codes; use `Math.random()` and `Math.round()` to generate random indexes. Then pick data from the arrays, build an object with random names, cities, zip codes, etc. and add it as a row in the table.
+ Ah, but this table looks too long now!!! Try to paginate it by using a previous and a next page button. You will display the table with 15 rows per page, not more!





