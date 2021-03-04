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




