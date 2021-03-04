# Module 5: Working with forms


## 5.3 [HTML5 tables, forms and input fields


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

+ Common styles for <`table>` element
  + rendering cell/row/table border, e.g., `tr, th, td { border: 1px solid; }`
  + adjusting spacing btw text and in cells and the cell borders, e.g., `td { padding: 10px; }`


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

+ examples: [table object](src/05c-example04.html)
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
    + `sectionRowINdex`: the position of a row in the `rows` collection of a `<tbody>`, `<thead>` or `<tfoot>`
  + most useful methods
    + `insertCell()`:
      + insert a cell into the current table `row`
      + no parameters: append a cell after the last cell of the row
      + index of the the cell as a unique parameter: insert the row and push other cells to the right
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





