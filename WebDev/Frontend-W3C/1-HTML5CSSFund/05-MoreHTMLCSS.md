# Module 5: More HTML and CSS

## 5.1 Introduction to Module 5

### Welcome to Module 5

<video src="https://edx-video.net/W3CHTM502016-V014700_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@e99b0a405ab44b288b5156ea813060a6/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### Module 5 - Content

5.1 __Introduction__: You will be combining HTML and CSS to create more complex pages.

5.2 __Tables__: Tables can be a great way of organizing your content — learn when to use tables, and when to avoid them.

5.3 __Multimedia__: Learn the best methods for including audio and video in your page.

5.4 __Embedding content__: Learn about iframes and some advanced image tag attributes, ismap and usemap. Note: This section is optional material included for the curious. It will not appear on any graded question.

5.5 __CSS tricks__: Here, we will introduce some next level methods for making awesome Web pages.

5.5 __Recipe project__: Separate your CSS and HTML into their own files for cleaner, easier coding.

5.6 __Exercises - Module 5__: Test your knowledge of this module's material.


### A world of possibilities

In Module 1, we learned the basics of HTML5. It's a fairly simple format, just a tree full of elements, which are described by tags, attributes, and the content inside the tags; the rest is details.

Once you know the list of all the possible tags, the list of available attributes, and a few special cases like the Document Type Declaration (DTD), self-closing tags, and meta tags, then you will have the foundation to code in HTML5.

Putting this all together to form a coherent Web page with the addition of CSS presents a world of possibilities. In this module, we'll delve into some of those interesting possibilities. 


## 5.2 Tables

### Introduction to tables

Using tables to organize information goes back a ways.  A long ways. Three or four thousand years ago, Sumerians were using [tables to calculate compound interest](http://www.storyofmathematics.com/sumerian.html).  Even so, tables are not obsolete, in fact HTML5 includes extensive facilities for describing/building tables. 

Tables are used to arrange data in tabular format - rows and columns of cells. You can put a variety of data like text, images, forms, links and even other tables in your table.

You may hear experienced Web developers decrying the use of tables, giving the impression that tables should be avoided at all costs.  It might seem off-putting at first, but they're not really talking about using tables for tabular information.  In earlier days, when layout options were limited, many developers resorted to tables as a means of layout.  There's really no need to do that anymore, there are plenty of layout capabilities in CSS3.  You really don't want to use tables that way, but there absolutely nothing wrong with using them for their intended purpose - making tables.


#### Separating content and style

Look at [this site](http://create.adobe.com/) that is laid out with CSS. You might be tempted to do this via tables instead. Or you might want to just make your whole Web page into one big table: site header in a table row, left navigation bar on the second row, left column, etc.

Bad idea! Here's why:

+ They are semantically incorrect for layout because they represent presentation and not content.
+ It puts presentation data in your content making your HTML larger. The user must download this unnecessary presentation data for every page they visit.
+ Accessibility: tables are not very screen reader friendly. Using tables for layout will clutter your HTML making it harder for assistive technology to parse your Web page.
+ Redesigns are harder when your HTML is cluttered with presentational code that should go into CSS. To change the layout of the page, you shouldn't be editing your content. Instead, you should just have to make CSS related changes.
+ Using CSS (one or two external stylesheets for your whole Web site) is easier to maintain consistency among pages.

Tables were not intended as a layout tool, so it is best to stick to them only for tabular data.


#### Table elements

Here is a list of all the  table elements we will be learning in this section:

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1px solid black" align="center" width=50%>
  <tbody>
    <tr>
      <td style="text-align: center; background-color: #3d64ff; color: #ffffff;">Type</td>
      <td style="text-align: center; background-color: #3d64ff; color: #ffffff;">Element</td>
    </tr>
    <tr>
      <td></td>
      <td>&lt;table&gt;</td>
    </tr>
    <tr>
      <td></td>
      <td>&lt;caption&gt;</td>
    </tr>
    <tr>
      <td>Row groups</td>
      <td>&lt;thead&gt;, &lt;tfoot&gt;, &lt;tbody&gt;</td>
    </tr>
    <tr>
      <td>Column groups</td>
      <td>&lt;colgroup&gt;, &lt;col&gt;</td>
    </tr>
    <tr>
      <td>Table row</td>
      <td>&lt;tr&gt;</td>
    </tr>
    <tr>
      <td>Table cells</td>
      <td>&lt;th&gt;, &lt;td&gt;</td>
    </tr>
  </tbody>
</table>

We will use these elements to build our table as we go.

#### The 'table' tag

This tag defines a table in HTML5.

Attribute:

border - has two values, 0 and 1. It is used to specify a border around table cells. 0 - no border, 1 - add border. 0 also suggests that it is a layout table.
Other attributes have been deprecated as the same can be achieved through CSS.

```css
<table border=1></table>
```

The code above will not provide any major visual change to your website yet because we don't have any cells defined.

Note: Though there is an attribute for border, the table elements should be styled using CSS. You can use the CSS border property to do that instead. 

#### 'caption' tag

It is used to give a title to the table and should be used as the first child element of `<table>`. It can be used to provide more context to the table if its content is ambiguous. As a summary of the table content, a caption can also be helpful for people who have difficulty understanding the content or use assistive technology.

```html
<table border=1>
  <caption>
    <p>Table 1.0</p>
    <p>Student's final exam results 2016</p>
  </caption>
</table>
```

[Sample Code](src/5.2.1-Table.html)


### The tr, th, td, colgroup, col tags

Let's now create the most basic table with a few cells.

#### 'tr' tag

Creates a table row.

#### 'th' tag

There are two types of cells in a table - header and standard. <th> creates table header cells. The content of table header cells is bold and centered by default.

```thml
<table border=1>
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
</table>
```

[Sample Code](src/5.2.2-th.html)


<table style="font-family: arial,helvetica,sans-serif;" auto="" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Attributes for &lt;th&gt;</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Purpose</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Usage</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Output</td>
  </tr>
  <tr>
    <td>colspan</td>
    <td>
      <p>Specifies the number of cells you want that column to span (cover)</p>
      <p>Possible values: positive integer number</p>
    </td>
    <td>&lt;th colspan="2"&gt;</td>
    <td><a href="https://codepen.io/w3devcampus/pen/xXERVo" target="_blank">View example</a></td>
  </tr>
  <tr>
    <td>rowspan</td>
    <td>
      <p>Specifies the number of cells you want the row to span (cover)</p>
      <p>Possible values: positive integer number</p>
    </td>
    <td>&lt;th rowspan="2"&gt;</td>
    <td><a href="https://codepen.io/w3devcampus/pen/WZGojz" target="_blank">View example</a></td>
  </tr>
  <tr>
    <td>scope</td>
    <td>
      <p>Specifies if a header cell is the header for a row, column, rowgroup or colgroup</p>
      <p>Possible values: row, col, rowgroup, colgroup, auto</p>
    </td>
    <td>&lt;th scope="row"&gt;</td>
    <td><a href="https://codepen.io/w3devcampus/pen/YrGpEG" target="_blank">View example</a></td>
  </tr>
</tbody>
</table>


#### 'td' tag

Creates table data (standard) cells. Content of table data cells is regular and left-aligned by default.

With these tags we can create a simple table.

```html
<table border=1>
  <tr>
    <th scope="col">Name</th>
    <th scope="col">Age</th>
  </tr>
  <tr>
    <td>Alexa</td>
    <td>23</td>
  </tr>
  <tr>
    <td>James</td>
    <td>35</td>
  </tr>
</table>
```

[Sample Code](src/5.2.2-td.html)

<table style="font-family: arial,helvetica,sans-serif;" auto="" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Attributes for &lt;td&gt;</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Purpose</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="20%">Usage</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Output</td>
  </tr>
  <tr>
    <td>colspan</td>
    <td>
      <p>Specifies the number of cells you want that column to span (cover)</p>
      <p>Possible values: positive integer number</p>
    </td>
    <td>&lt;td colspan="2"&gt;</td>
    <td><a href="https://codepen.io/w3devcampus/pen/zEKoRg" target="_blank">View example</a></td>
  </tr>
  <tr>
    <td>rowspan</td>
    <td>
      <p>Specifies the number of cells you want the row to span (cover)</p>
      <p>Possible values: positive integer number</p>
    </td>
    <td>&lt;td rowspan="2"&gt;</td>
    <td><a href="https://codepen.io/w3devcampus/pen/PJGbeJ" target="_blank">View example</a></td>
  </tr>
  <tr>
    <td>headers</td>
    <td>Value is the 'id' of the &lt;th&gt; tag it corresponds to if any</td>
    <td>&lt;tr&gt;<br>&nbsp; &lt;th id="header-id"&gt;<br>&lt;/tr&gt;<br>&lt;tr&gt;<br>&nbsp; &lt;td headers="header-id"&gt;<br>&nbsp; &lt;td headers="header-id"&gt;<br>&lt;/tr&gt;</td>
    <td><a href="https://codepen.io/w3devcampus/pen/KXgNxr" target="_blank">View example</a></td>
  </tr>
</tbody>
</table>


#### The 'colgroup' and 'col' tags

##### 'colgroup' tag

This tag allows you to group columns in a table. Grouping columns is useful if you want to specify properties for a group of columns like applying styles to the whole column instead of repeating it for each cell.

Attribute:

+ `span` - takes a positive integer value. It specifies the number of columns you want your colgroup to span (cover). The colgroup element shares its attributes like style and width with all the columns it spans.  Essentially it allows a single cell to stretch to cover multiple columns on a particular row.


##### 'col' tag

Used within `<colgroup>`, the `<col>` tag specifies the column property for each column within a colgroup. The only element a `<colgroup>` can contain is `<col>`.

Attribute:

+ `span` - takes a positive integer value. It specifies the number of columns you want the col element to span (cover). 
Consider the table above we created using `<tr>`, `<th>` and `<td>`. Let's say I want the 'name' column to be in green and the 'age' column to be orange. You need to use the `<colgroup>` and `<col>` tags to achieve styling effects specific to a column.

```html
<body>
  <table border=1>
    <colgroup>
      <col span="1" style="background-color:green">
      <col span="1" style="background-color:orange">
    </colgroup>
    <tr>
      <th>Name</th>
      <th>Age</th>
    </tr>
    <tr>
      <td>Alexa</td>
      <td>23</td>
    </tr>
    <tr>
      <td>James</td>
      <td>35</td>
    </tr>
  </table>
</body>
```

[Sample Code](src/5.2.2-tdColor.html)

#### Knowledge check 5.2.1

Which of the following tags will you use to add cells to the table header?

  1. < head >
  2. < td >
  3. < th >
  4. < tr >

  Ans: 3<br/>
  Explanation: th is for table header. th cell's content is bolded and centered by default.


### The thead, tbody and tfoot tags

Similar to an HTML document, a table in HTML can be split into header, body and footer. We use these three tags - `<thead>`, `<tbody>` and `<tfoot>` - to specify parts of a table.

It is very useful to define parts of a table as header, body and footer because once browsers are able to identify which cells are header and footer, the body can be allowed to scroll independently of header and footer catering to a good table viewing experience in small screens. This is one such example. Apart from this, these elements can also be used to style header, body and footer rows individually using CSS.


#### 'thead' tag

Just like how we use `<colgroup>` to group columns, `<thead>` is used to group the header content in a HTML table. 

As we learned in the previous unit, header cells are specified using `<th>` as a child of `<tr>`. Rows specified within `<thead>` indicate that they are header rows. See the code below:

```html
<thead style="color:white">
  <tr>
    <th scope="col">Name</th>
    <th scope="col">Age</th>
  </tr>
</thead>
```


#### 'tbody' tag

Following `<thead>`, subsequent rows are considered body rows in a table. Regular cells are specified using `<td>` as a child of `<tr>`:

```html
<tbody>
  <tr>
    <td>Alexa</td>
    <td>23</td>
  </tr>
  <tr>
    <td>James</td>
    <td>35</td>
  </tr>
  <tr>
    <td>Trisha</td>
    <td>23</td>
  </tr>
</tbody>
```


#### 'tfoot' tag

The footer is the last to be specified and rows within `<tfoot>` are considered footer rows at the end of a table:

```html
<tfoot>
  <tr>
    <td>3 Unique Name</td>
    <td>2 Unique Ages</td>
  </tr>
</tfoot>
```

Putting it all together:

```html
<table border=1>
  <colgroup>
    <col span="1" style="background-color:green">
    <col span="1" style="background-color:orange">
  </colgroup>
  <thead style="color:white">
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alexa</td>
      <td>23</td>
    </tr>
    <tr>
      <td>James</td>
      <td>35</td>
    </tr>
    <tr>
      <td>Trisha</td>
      <td>23</td>
    </tr>
  </tbody>
  <tfoot style="font-style: italic;">
    <tr>
      <td>3 Unique Names</td>
      <td>2 Unique Ages</td>
    </tr>
  </tfoot>
</table>
```

[Sample Code](src/5.2.3-tbody.html)


#### Knowledge check 5.2.3

True or False? By specifying the header, body and footer for the table, you can scroll these sections independent of each other.

  Ans: True, xFalse<br/>
  Explication: This is typically done when you want to display a large table in a small space. The body can be allowed to scroll independently of header and footer catering to a good table viewing experience in small screens. You can achieve this using pure CSS or JavaScript.


### Styling your table

We now know how to put a basic table together. However, the tables we have looked at so far could really use some work in terms of how they look.

Here, we will look at some useful CSS elements to style your table. All examples below are using CodePen. Each CodePen has three tabs - Result, HTML and CSS. Make sure to view each tab to get the HTML and CSS code for examples. You are also welcome to modify the code for each example by clicking on 'Edit on CodePen' on the top right corner of the CodePen (click on "RUN" when you completed your changes).


#### border

Though `border` is a valid attribute of the table element, it is best specified in CSS. It is a shorthand property meaning you can set several CSS properties simultaneously.

The CSS `border` property sets `border-width`, `border-style` and `border-color` in order:

```css
table { border: 1px solid black; }
```

<table style="font-family: arial,helvetica,sans-serif;" cellspacing="0" cellpadding="5" border="1" align="center" width=90%">
<tbody>
  <tr>
    <td style="text-align: center; background-color: #0021fd; color: #ffffff; width: 10%">Property Value</td>
    <td style="text-align: center; background-color: #0021fd; color: #ffffff; width: 40%">Possible values</td>
  </tr>
  <tr>
    <td>border-width</td>
    <td>thin, medium, thick, in pixels</td>
  </tr>
  <tr>
    <td>border-style</td>
    <td>none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset</td>
  </tr>
  <tr>
    <td>border-color</td>
    <td>color name or color values, transparent</td>
  </tr>
  <tr>
    <td>initial</td>
    <td>sets the property to the default value. Defaults for width, style and color are 'medium none current-color-of-element'</td>
  </tr>
  <tr>
    <td>inherit</td>
    <td>inherits property from parent element</td>
  </tr>
</tbody>
</table>

To give a border to `<table>`, `<th>` and `<td>`:

```css
table, th, td { border: 1px solid black; }
```

[Sample Code](5.2.4-Table1.html)


#### border-collapse

We gave a border to the table, table-header and table-data above. This creates two borders creating a double line. In order to collapse them all into a single border, we use the `border-collapse` CSS property:

```css
table { border-collapse: collapse; }
```

Possible values of this property are:

+ `separate` - default value where borders are detached like in the example above
+ `collapse` - border are collapsed into a single border
+ `initial` - sets to default value (separate)

[Sample Code](src/5.2.4-Table2.html)


#### Table width and height

Browsers automatically set the width and height for the rows and columns for your table based on the content in your cells. Cells with most content usually set the height and width of all cells adjacent to themselves.

With CSS, you can also explicitly set the dimensions of your cells. Width and height can be specified in:

+ units of length like pixels, percentage - relative to the table width, etc
+ auto: the browser will calculate and select a width for the specified element (default value)

It also supports initial (sets property to default value) and inherit (from parent element).

`width`/`height` of `<td>` of one cell will not only affect that cell but the whole column/row. If two cells in one column/row have different widths/heights specified, the larger value is set.

[Sample Code](src/5.2.4-Table3.html)


#### text-align

This property is used to align the text of `<th>` and `<td>` cells left, right or center (week 3 recap).

Default:

+ `<th>` - center
+ `<td>` - left


```css
td { text-align: right;}
```


#### vertical-align

This property is used to align the text of `<th>` and `<td>` cells top, bottom or middle.

Default:

+ `<th>` - middle
+ `<td>` - middle

```css
th { vertical-align: top; }
```


#### padding

Right now our table looks quite cramped. We use the `padding` property on `<th>` and `<td>` to provide some space between border and content in cell. It takes its value in units of length like px, cm, % - relative to parent container's width, etc.

```css
th, td { padding: 15px; }
```

This will add 15px space around the content on all sides.

You can also apply different padding styles for four individual sides by using:

+ padding-top: th, td { padding-top: 15px; }
+ padding-right: th, td { padding-right: 25px; }
+ padding-bottom: th, td { padding-bottom: 35px; }
+ padding-left: th, td { padding-left: 45px; }

Alternatively, `padding` can also be provided as a shorthand property where you can specify all four sides in one go:

```css
th, td { padding: 20px 30px 40px 50px; }
```

It is specified in the order: top, right, bottom and left padding.

[Sample Code](src/5.2.4-Table4.html)


#### border-spacing

`border-spacing` specifies the distance between two cell borders in pixels. This is different from padding which is space between content in cell and border. It takes its value in units of length like px, cm, % - relative to parent container's width, etc. 

It has the inherit property whose default value is 0.

It takes two values for horizontal and vertical spacing. If only one value is provided, it is used for both horizontal and vertical spacing: 

```css
table { border-spacing: 25px 50px; }
table, td, th (border-spacing: 25px; }
```

Some things to keep in mind:

+ If you try to provide spacing for only `<th>` and `<td>`, make sure there is space from the table border or you will not see a difference. 
+ You have to set - `table { border-collapse: separate; }` for it to take effect.

[Sample Code](src/5.2.4-Table5.html)


#### Side-borders

The first property `border` will set a border to all four sides. You can also set borders to individual sides - top, right, bottom, left:

```css
th, td { border-right: 1px solid black; }
```

[Sample Code](src/5.2.4-Table6.html)


#### zebra table

A zebra table has alternating colors for table rows making it easier to differentiate data between rows. You can specify which rows you want to differentiate using a different color. Typically, you apply this property to a set of even or odd table rows to created a striped effect. You can set odd or even rows a particular color and leave the other rows white (default color).

```css
tr:nth-child(even) { background-color: grey; }
tr:nth-child(odd) { background-color: #ccff99; }
```

The 'nth-child' selector matches every element that is the nth child of the table or any parent element. Therefore,

```css
tr:nth-child(3n) { background-color: grey; }
```

solidm grey.
solid
solidl)
solid

#### hover to highlight

Using the hover property on your `<tr>`, you can mouse over rows in your table to highlight them in the color you specify. This is useful to help users differentiate data between rows.

```css
tr:hover {background-color: #ccff99; }
```

Hover over these tables: [Sample Code](src/5.2.4-Table8.html)


#### overflow

With padding, additional columns and rows, your table can easily grow rather big overflowing out of the `<div>` you had planned for your table in your Web page. You can use the CSS overflow property to resolve this. It has four values other than initial (sets the default value) and inherit (from parent element).

+ visible - Content that has overflowed is visible outside the parent element. Eg: Text in a box overflows outside box and is visible.
+ hidden - Content that has overflowed is hidden. This makes the overflowed content inaccessible.
+ scroll - Content that has overflowed is hidden but a scroll bar is added to make it accessible.
+ auto - Content that has overflowed is hidden but a scroll bar is automatically added to view hidden content.

To address left and right edges of content, you can use overflow-x and to address top and bottom edges of content, you can use overflow-y.

[Sample Code](src/5.2.4-Table9.html)


#### In summary: a fancy table

As a conclusion to this tables section, here is a complete table design: [Sample Code](src/5.2.4-Table0.html)

Note: This table contains multi-line headers. You can find more information on the right way to design tables of different header types on this W3C [Tables Concepts](https://www.w3.org/WAI/tutorials/tables/) page.



#### Knowledge check 5.2.3

Source code for the following knowledge check:

```css
<style>
 table, th, td { border: 1px solid black; border-spacing: 50px; }
 table { border-collapse: collapse; }
</style>
```
```html
<table>
 <tr><th>Names</th><th>Age</th></tr>
 <tr><td>Michael</td><td>21</td></tr>
</table>
```

Try the code above in an HTML editor and view the output. The border spacing property is supposed to create a space between two border cells. There should be a 50px space between table border and cell borders and between cell borders. In this example, that is not the case. Why?

  1. table border is not set
  2. border-collapse should be set to separate
  3. border-spacing should not be specified in pixels
  4. There is a syntax error in the code above

  Ans: 2<br/>
  Explanation: For border spacing to take effect, border-collapse must be set to 'separate'. Setting border-collapse to 'collapse' will merge cell and table borders into one so as to avoid double borders. Revisit the Border Spacing section in the 'Styling your table' unit.



### Create a table

<video src="https://edx-video.net/W3CHTM502016-V012700_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@48db9bb03e1d4ea29ed567c0a3b1a68e/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>


[Sample Code][src/5.2.5-Table.html]
<br/>



### Activities - Tables

1. Create a simple 3x3 table with the first row containing header cells. You may choose not to add any styling including border. 
2. Create the following table with same cell content:

  <table style="font-family: arial,helvetica,sans-serif;" align="center" border="1" cellpadding="5" cellspacing="0">
  <tbody>
    <tr style="font-weight: bold;">
      <td style="text-align: center;">Attribute</td>
      <td style="text-align: center;">Description</td>
      <td style="text-align: center;">Usage</td>
    </tr>
    <tr>
      <td>src</td>
      <td>Used to specify the URL of the image</td>
      <td>src=“images/test.png"</td>
    </tr>
    <tr>
      <td>alt</td>
      <td>Used to specify replacement text for the image</td>
      <td>alt=“Test image for HTML5 course”</td>
    </tr>
  </tbody>
  </table>

  [Sample Code](src/5.2.6-Tables.html)

3. Create the following table structure using HTML and CSS following the style as closely as possible noting table border, colors, etc. Insert dummy text values for table.

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/5854bfc005394517ae62fc55fd58242e/83268eeaa4bf474e9aca8dcfb3f02da1/4?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%40e121ad32033442f9a8580c8f3f1edbb5">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/29bf635c377d4a265529ec8ecc838ec7/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/table-activity-2.PNG" style="margin: 0.1em;" alt="Tables activity example 2" title="Tables activity example 2" width=350>
    </a></div>
  </div>

  [Sample Code](src/5.2.6-Tables3.html)

4. Create the following table structure using HTML and CSS following the style as closely as possible noting table border, colors, etc. Make the table cover the entire width of the screen. Insert dummy text values for the table.

  <div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
    <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/5854bfc005394517ae62fc55fd58242e/83268eeaa4bf474e9aca8dcfb3f02da1/4?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%40e121ad32033442f9a8580c8f3f1edbb5">
      <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/df7e23ac8107fee9c284e3d9f5976ea2/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/table-activity-1.PNG" style="margin: 0.1em;" alt="Tables activity example" title="Tables activity example" width=350>
    </a></div>
  </div>

  [Sample Code](src/5.2.6-Tables4.html)

5. Find a table used in a real Web page whose table body can be scrolled.

  Ans: [Table scroll](https://mdbootstrap.com/docs/jquery/tables/scroll/)


6. Create a simple hover to highlight table that makes the background color of a row 'yellow' when you hover over a table row.

  [Sample Code](src/5.2.6-Tables6.html)

__Note__: If you wish to share your HTML code in the discussions, you can paste your code directly in a discussion forum post (highlight code and Ctrl+K/use the code widget) or use one of the following online code editors:

+ JS Bin: http://jsbin.com ([JS Bin tutorial](http://code.tutsplus.com/tutorials/javascript-tools-of-the-trade-jsbin--net-36843))
+ CodePen: http://codepen.io ([CodePen tutorial](https://css-tricks.com/video-screencasts/112-using-codepen/))

These are HTML, CSS, and JavaScript code editors that preview/showcase your code bits in your browser. It helps with cross-device testing, realtime remote pair programming.


## 5.3 Multimedia

### Audio element

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/5854bfc005394517ae62fc55fd58242e/5224d810e43e41ceabf2598f5c711456/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%40b9f42abd24844832aa1e62748dfdc4e8">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/183281b7132e8ad2fb27599527c0719c/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/video.jpg" style="margin: 0.1em;" alt="Picture of an embedded video" title="Picture of an embedded video" width=200>
  </a></div>
</div>

`audio` and `video` are new HTML 5 elements that were highly anticipated. With HTML5 support for multimedia, this has become much easier, than previous methods. 


#### Audio tag

You can use the `<audio>` tag to embed audio in your page.

```html
<audio src="sounds/flute.mp3">
  Your browser does not support the audio file.
</audio>
```

Any text within the `<audio>` tags will be displayed if the browser does not support the audio element. You should add such a message to provide better user experience for your page as it will be viewed in all types of devices and browsers.

The audio element has several attributes that can be used to configure audio playback. The following table lists the audio element's attributes:

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Attribute</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="50%">Description</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Usage</td>
  </tr>
  <tr>
    <td>src</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Used to specify the URL of the audio file to embed.</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">Values:</span></p>
      <ul>
        <li><span style="font-family: arial,helvetica,sans-serif;">absolute URL (file residing somewhere on the Web)</span></li>
        <li><span style="font-family: arial,helvetica,sans-serif;">relative URL (within your Web site)</span></li>
      </ul>
    </td>
    <td>
    <p><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3"&gt;&lt;/audio&gt;</span></p>
    </td>
  </tr>
  <tr>
    <td>controls</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified provides controls for the user like play, pause, seek bar and volume</span></p>
      <p><img alt="Controls from HTML5 audio" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/327f2b7346ed0f5b804d41e3d49dd8ea/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/audio-controls.PNG" type="saveimage" target="[object Object]" isimmediatepropagationstopped="function t(){return!1}" ispropagationstopped="function t(){return!1}" isdefaultprevented="function t(){return!1}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" stoppropagation="function (){r.isPropagationStopped=n}" preventdefault="function (){r.isDefaultPrevented=n}" width="263" height="26"></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls&gt;&lt;/audio&gt;</span></td>
  </tr>
  <tr>
    <td>loop</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified loops media content</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls loop&gt;&lt;/audio&gt;</span></td>
  </tr>
  <tr>
    <td>muted</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified mutes media when playback begins</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls muted&gt;&lt;/audio&gt;</span></td>
  </tr>
  <tr>
    <td>preload</td>
    <td>
    <p><span style="font-family: arial,helvetica,sans-serif;">Allows author to communicate to the browser which settings will work best - audio should not be preloaded (none), only audio metadata is fetched (metadata), audio file can be downloaded when page loads (auto)</span><br><span style="font-family: arial,helvetica,sans-serif;">values: none, metadata, auto</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls preload="auto"&gt;&lt;/audio&gt;</span></td>
  </tr>
  <tr>
    <td>autoplay</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified will automatically begin playing the source file as soon as it can without waiting for the entire audio file to finish downloading</span></p>
      <p></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls autoplay&gt;&lt;/audio&gt;</span><audio autoplay="autoplay"></audio></td>
  </tr>
</tbody>
</table>

Here is an example code:

```html
<audio src="https://archive.org/download/Music_Calgary_PD_1/The.good.the.bad.and.the.ashy.mp3" controls loop muted preload="none">
  Your browser does not support the audio file.
</audio>
```

Output for the code above (try playing):

<p><audio src="https://archive.org/download/Music_Calgary_PD_1/The.good.the.bad.and.the.ashy.mp3" preload="none" loop="loop" controls="controls" muted="">
  Your browser does not support the audio file.
</audio></p>

If you hit play and didn't hear anything, remember that we have added the muted attribute. So the audio will be muted when playback begins. Increase the volume to hear the music.


#### Audio file formats

Just like image file formats, not all audio file formats are supported by all browsers. You will want to use common audio file formats for browser compatibility ensuring the highest probability that your audio file will play. 

The most common ones are MP3, WAV and Ogg. 

[This page](https://developer.mozilla.org/en-US/docs/Web/HTML/Supported_media_formats) under 'Browser Compatibility' lists the `audio` formats supported by the audio element and their browser support.

Here is some information regarding different types of audio formats and their compression techniques that can help you decide which audio format to choose apart from `audio` element and browser compatibility:

+ There are three major groups of audio file formats - uncompressed (eg: WAV), lossless compressed (eg: MPEG-4, WMA Lossless) and lossy compressed (eg: Opus, MPC, AAC, WMA Lossy).
+ In uncompressed audio file formats, no compression is applied to the audio file. The memory used for both sound and silence is the same though silence contains less information/data.
+ In lossless compression, no data is lost but the file is compressed as silence is designed to take up very little space. Compared to uncompressed, lossless compression's compression ratio is approximately 2:1.
+ Lossy compression provides the greatest compression by simplifying the data and removing some audio information resulting in some loss of quality. It is also the most popular. There are techniques in place to ensure that the parts of sound that is lost has little effect on quality. You can also select a range of compression rates. The larger the rate of compression, the bigger the loss in quality and smaller the file size. 
+ The audio format Ogg Opus has two parts to it. 'Ogg' is a digital container format. It is a specification that describes how different elements of data and metadata work in an audio file. However, it provides no information on how the data is compressed. So a program that opens a container file like 'Ogg' might not know how to decode it. 'Opus', the second part of the audio format, represents the encoding or decoding mechanism for that stream of audio. Opus is a lossy audio coding format.
+ If you have an audio file in one format and wish to convert it to another, there are a lot of software applications available to help you do that.


#### Source element for multiple source files

The `source` element, also new in HTML5, serves the same purpose as the `src` attribute in an `audio` element. It is used to specify source files for the `audio` and `video` elements. Using the source element, you can specify multiple source files. The `<source>` tag is self-closing, therefore, it does not require a closing tag.

Example:

```html
<audio controls>
  <source src="https://courses.edx.org/asset-v1:W3Cx+HTML5.0x+3T2016+type@asset+block@splash.wav" type="audio/wav">
  <source src="https://courses.edx.org/asset-v1:W3Cx+HTML5.0x+3T2016+type@asset+block@splash.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
```

Output for code above (try playing):

<p><audio controls="controls">
  <source src="https://courses.edx.org/asset-v1:W3Cx+HTML5.0x+1T2016+type@asset+block@splash.wav" type="audio/wav">
  <source src="https://courses.edx.org/asset-v1:W3Cx+HTML5.0x+1T2016+type@asset+block@splash.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio></p>

The advantage of providing multiple source files in different formats is that if the browser doesn't support the first format, it will try the second source file. The browser can select from the list based on its file format or codec support. In the code snippet example above, Internet Explorer does not support .wav files. So if you tried to play the file above in Internet Explorer, the browser would have tried to play .wav, failed and played the .mp3 version instead. 

The following table lists the `<source>` element's attributes:

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Attribute</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="50%">Description</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Usage</td>
  </tr>
  <tr>
    <td>src</td>
    <td><span style="font-family: arial,helvetica,sans-serif;">Specifies the URL of the media file</span></td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;source src="sounds/flute.mp3"&gt;</span></td>
  </tr>
  <tr>
    <td>type</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Specifies the internet media type, also known as the MIME type for the audio resource. A media type is an identifier for file formats and format contents transmitted over the internet like text and audio files.</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">It consists of a type and a sub-type. Eg: "audio/mpeg" - <strong>audio</strong> is the type and <strong>mpeg</strong> is the subtype. It can also take optional parameters that can be specified after a semicolon - "audio/ogg; codecs=opus" means the audio is in the ogg format and uses the opus codec. If the browser supports the Ogg format but not the Opus codec, the audio file will not load.</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">If the type attribute is not specified, the media type is retrieved from the server.</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;source src="sounds/flute.mp3" type="audio/mpeg"&gt;</span></td>
  </tr>
</tbody>
</table>


#### Knowledge check 5.3.1

How do you handle browsers that do not support the audio element?

  1. Don't do anything
  2. Add text in your audio element with a message stating that your browser does not support the audio element or audio format
  3. Do not include the 'autoplay' attribute so as to avoid an error being displayed
  4. Add multiple source elements

  Ans: 2 <br/>
  Explanation: You can add text within your audio tags that will be displayed if a browser does not support the audio element. This is highly recommended as your page will be viewed by a variety of browsers. Learn more about audio element support in browsers [here](http://caniuse.com/#search=%3Caudio%3E)


### Video element

Video is fairly new in HTML5. Previously, the most reliable way to add video was the Adobe Flash Player for example. 

You can use the video element to embed video in your page. You can specify the location of your video file using the src attribute or source element (for multiple source files).

```html
<video src="multimedia/running.mp4">
  Your browser does not support the HTML5 video element.
</video>
```

Any text within the `<video>` tags will be displayed if the browser does not support the `video` element. You should add such a message to provide better user experience for your page as it will be viewed in all types of devices and browsers.

Similar to the `audio` element, the `video` element has several attributes that can be used to configure playback. The following table lists the video element's attributes:

<table style="font-family: arial,helvetica,sans-serif; max-width: 100%;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Attribute</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="50%">Description</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Usage</td>
  </tr>
  <tr>
    <td>src</td>
    <td>specifies the URL or location of the media file</td>
    <td width="40%">&lt;video&nbsp;src="multimedia/running.mp4"&gt;&lt;/video&gt;</td>
  </tr>
  <tr>
    <td>autoplay</td>
    <td>Boolean attribute when specified will automatically begin playing source file as soon as it can without waiting for the entire video&nbsp;file to finish downloading. Note: Some versions of chrome support autostart instead of autoplay</td>
    <td width="40%">
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;autoplay&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>controls</td>
    <td>
      <p>Boolean attribute when specified provides controls for the user like play, pause, seek bar and volume</p>
      <p><img alt="Image of HTML5 video controls" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b30f1164c96da183a2c339b152ebe472/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/video-controls.PNG" type="saveimage" target="[object Object]" isimmediatepropagationstopped="function t(){return!1}" ispropagationstopped="function t(){return!1}" isdefaultprevented="function t(){return!1}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" stoppropagation="function (){r.isPropagationStopped=n}" preventdefault="function (){r.isDefaultPrevented=n}" width="232" height="26"></p>
    </td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>loop</td>
    <td>Boolean attribute when specified loops media content</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&nbsp;loop&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>muted</td>
    <td>Boolean attribute when specified mutes media when playback begins</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&nbsp;muted&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>preload</td>
    <td>Allows author to communicate to the browser which settings will work best - video&nbsp;should not be preloaded (none), only video&nbsp;metadata is fetched (metadata), video&nbsp;file can be downloaded (auto)<br>values: none, metadata, auto</td>
    <td>
      <p>&lt;video&gt; src="multimedia/running.mp4"&nbsp;controls&nbsp;preload="auto"&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>poster</td>
    <td>Specifies the URL of the frame you want to display as&nbsp;the video cover until the user starts or seeks the video. By default, the first frame is considered the poster frame. &nbsp;The poster can also be an arbitrary image, not necessarily in any frame of the video.</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;poster="/images/video-screenshot.png" controls&gt;</p>
    </td>
  </tr>
  <tr>
    <td>height, width</td>
    <td>height and width of the video's play area in pixels. Always set height and width for a video so the browser can allocate the specified space for it when it loads the page.&nbsp;</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&nbsp;width="320" height="240"&gt;&lt;/video&gt;</p>
    </td>
  </tr>
</tbody>
</table>

```html
<video src="multimedia/running.mp4" controls width="320" height="240"></video>

<video src="http://techslides.com/demos/sample-videos/small.mp4" controls loop muted preload="none" 
  poster="https://courses.edx.org/asset-v1:W3Cx+HTML5.0x+3T_2016+type@asset+block@badgehtml5.png" 
  height="320" width="240">
  Your browser does not support the HTML5 video element.
</video>
```

Output for code above (try playing):

<p><video src="http://techslides.com/demos/sample-videos/small.mp4" preload="none" loop="loop" controls="controls" muted="" poster="https://courses.edx.org/asset-v1:W3Cx+HTML5.0x+1T2016+type@asset+block@badgehtml5.png" width="180" height="270">
  Your browser does not support the HTML5 video element.
</video></p>


#### Poster attribute

The `<video>` tag has an important attribute that you don't find on the audio element.  The poster attribute is used to specify what picture is shown before the video starts playing.  By default, the poster shown is simply the first frame of the video, but the poster attribute can be used to specify a different image.  It can specify a particular frame of the video or, like a real movie poster, it can be an image that doesn't actually appear in the video.


#### Video file formats

Just like audio file formats, not all video file formats are supported by all browsers. You should use common video file formats for browser compatibility ensuring the highest probability that your video file will play.

The most common ones are MP4, WebM and Ogg.

[This page](https://developer.mozilla.org/en-US/docs/Web/HTML/Supported_media_formats) under 'Browser Compatibility' lists the video formats supported by the `video` element and their browser support for both desktop and mobile. Using the `source` element, you will have to provide a combination of video formats to target most browsers.

Here is some information regarding different types of video formats and their compression techniques that can help you decide which video format to choose apart from `video` element and browser compatibility:

+ Most videos go through some form of compression to reduce redundancy in video files and make them smaller, allowing them to download faster. Most also use audio compression techniques to compress sound in video files.
+ Like audio, there are three major groups of video file formats - uncompressed, lossless compressed ([list of lossless video compression formats](https://en.wikipedia.org/wiki/List_of_codecs#Lossless_video_compression)) and lossy compressed ([list of lossy video compression formats](https://en.wikipedia.org/wiki/List_of_codecs#Lossy_compression_2)).
+ In uncompressed video file formats, no compression is applied to the video file.
+ In lossless compression, no data is lost. If you were to uncompress a file compressed using the lossless technique, you will get back the exact same data you started with.
+ Most videos use lossy compression as it results in significantly smaller video files. Lossy compression provides compression by simplifying the data and removing video information resulting in some loss of quality. There are techniques in place to ensure that the parts of the video that are lost have little effect on quality. You can also select a range of compression rates. The larger the rate of compression, the bigger the loss in quality and smaller the file size. However, if you uncompress a video file that was compressed using the lossy technique, you will not be able to retrieve the same data you put in. With text or spreadsheets, loss of data might be a significant problem. However, with images and video losing a bit of quality is not going to affect the file because you can still make out what the video is about.
+ The video format 'H.264 and MP3 in MP4' has three parts to it. H.264 is a video compression standard. MP3 is an audio coding format that uses lossy compression for sound in the video. MP4, like Ogg, is a digital container format. It stores audio and video data rather than code the information. A program that opens a container file like MP4 might not know how to decode it. So it requires other standards like H.264 and MP3 to dictate how the video will be coded and possibly compressed.
+ If you have a video file in one format and wish to convert it to another, there are a lot of software applications available to help you do that.


#### Knowledge check 5.3.2

Which of the following attributes is used to provide a placeholder frame before user starts or seeks the video?

  1. muted
  2. controls
  3. poster
  4. frame
  
  Ans: 3<br/>
  Explanation: A placeholder frame can be any image you can add to display before the user plays or seeks the video. This can be added using the 'poster' attribute. Refer to the first code snippet on this video unit to see its usage.


### Video - Source/Track elements

#### Source element for multiple source files

The source element that we saw in the previous unit is also used to specify multiple source files for the video element. The `<source>` tag is self-closing and so does not require a closing tag.

```html
<video controls height="320" width="240">
  <source src="http://techslides.com/demos/sample-videos/small.mp4" type="video/mp4">
  <source src="http://techslides.com/demos/sample-videos/small.webm" type="video/webm">
  <source src="http://techslides.com/demos/sample-videos/small.ogv" type="video/ogg">
  Your browser does not support the HTML5 video element.
</video>
```

<video src="http://techslides.com/demos/sample-videos/small.mp4" controls="controls" width="240" height="320">
  <source src="http://techslides.com/demos/sample-videos/small.mp4" type="video/mp4">
  <source src="http://techslides.com/demos/sample-videos/small.webm" type="video/wemb">
  <source src="http://techslides.com/demos/sample-videos/small.ogv" type="video/ogg">
  Your browser does not support the HTML5 video element.
</video>

The advantage of providing multiple source files in different formats is that if the browser doesn't support the first format, it will try the second source file. The browser can select from the list based on its file format or codec support. There is no one format that is supported by all browsers. So you will have to use the `source` element to list a combination of formats.

The following table lists the `source` element's attributes:

<table style="font-family: arial,helvetica,sans-serif; max-width: 100%;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff; min-width: 5em;">Attribute</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;">Description</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff; min-width: 13em;">Usage</td>
  </tr>
  <tr>
    <td>src</td>
    <td>Specifies the URL or location of the media file</td>
    <td>&lt;source src="multimedia/small.mp4"&gt;&lt;/source&gt;</td>
  </tr>
  <tr>
    <td>type</td>
    <td>
      <p>Specifies the internet media type, also known as the MIME type for the audio/video resource. A media type is an identifier for file formats and format contents transmitted over the internet like text and audio files.</p>
      <p>It consists of a type and a sub-type. Eg: "video/mp4" - <b>video</b>&nbsp;is the type and <strong>mp4</strong>&nbsp;is the subtype. It can also take optional parameters that can be specified after a semicolon - "video/mp4; codecs="avc1.42E01E, mp4a.40.2"" means the video&nbsp;is in the mp4 format and uses the codecs -&nbsp;avc1.42E01E, mp4a.40.2. If the browser supports the mp4&nbsp;format but none of the&nbsp;avc1.42E01E, mp4a.40.2&nbsp;codecs, the video file will not load.</p>
      <p>If the type attribute is not specified, the media type is retrieved from the server.</p>
    </td>
    <td>&lt;source src="multimedia/small.mp4" type="video/mp4"&gt;&lt;/source&gt;</td>
  </tr>
</tbody>
</table>


#### Track element for captions and subtitles

The `<video>` element is very similar to the HTML5 `<audio>` element except for one addition - the `<track>` element. The `<track>` element is used to add timed text like subtitles, captions or any text you would like to display to the user when the video is playing.

+ Web Video Text Tracks (WebVTT) files are the standard to include subtitles or captions. You can learn [how to create them here](https://w3c.github.io/webvtt/).
+ Captions and subtitles are not the same. Subtitles are meant to translate the language (for those who do not understand the language being spoken in the video). Captions are meant for the deaf or people who have difficulty hearing. It includes sound effects and other significant audio like music and lyrics and is usually in the same language as the audio. Read more about their difference [here](https://www.alsintl.com/blog/subtitles-captions-difference/).
+ Like the `<source>` tag, you can add multiple `<track>` tags in your video element to add multiple subtitle/caption tracks. This is commonly done when providing them in different languages. 

The `<track>` tag is self-closing and so does not require a closing tag. You specify the `<track>` element as a child element of your `<video>` tag like this:

```html
<video width="320" height="240" controls>
  <source src="module.mp4" type="video/mp4">
  <track src="module-captions.vtt" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video>
```

The following table lists the `<track>` element's attributes:

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Attribute</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="50%">Description</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Usage</td>
  </tr>
  <tr>
    <td>default</td>
    <td>It is a boolean attribute. If you have multiple tracks for the same video file, you can specify which one is the default using this attribute. It can be used on one  track element in a video. If you only have one track element, default should still be added to deliver the video with captions turned on in most browsers.</td>
    <td>
      <p>&lt;video src="multimedia/small.mp4" controls&gt;</p>
      <p>&nbsp; &lt;track src="captions/small-en.vtt" label="english" default&gt;</p>
      <p>&nbsp; &lt;track src="captions/small-fr.vtt" label="French"&gt;</p>
      <p>&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>kind</td>
    <td>Specifies the kind of the source&nbsp;file. <br>Values: subtitles (default value), captions, descriptions (textual description of the video best suited for the   blind who cannot be seen), chapters (meant for chapter titles), metadata (kind of track that is used by scripts and is not visible to the user).</td>
    <td>
      <p>&lt;track src="captions/small-en.vtt" kind="captions"&gt;</p>
    </td>
  </tr>
  <tr>
    <td>label</td>
    <td>Label of the track.&nbsp;Browser uses the label value to display track options for user to select.&nbsp;</td>
    <td>
      <p>&lt;track src="captions/small-en.vtt" label="English"&gt;</p>
      <p><span style="line-height: 22.4px;">&lt;track src="captions/small-fr.vtt" label="French"&gt;</span></p>
    </td>
  </tr>
  <tr>
    <td>src</td>
    <td>URL of track. The <strong>file must be on a Web server</strong>. The .vtt file cannot be loaded from a file (file://) protocol.</td>
    <td>
      <p>&lt;track src="http://www.xyz.org/small-en.vtt"&gt;</p>
    </td>
  </tr>
  <tr>
    <td>srclang</td>
    <td>Language of text track. Eg: en, fr. <br>If kind&nbsp;is 'subtitles', then the srclang attribute must be specified.</td>
    <td>
      <p>&lt;track src="captions/small-en.vtt" kind="subtitles" srclang="en"&gt;</p>
    </td>
  </tr>
</tbody>
</table>


### Audio and video elements

<video src="https://edx-video.net/W3CHTM502016-V009400_DTH.mp4" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/xblock/block-v1:W3Cx+HTML5.0x+1T2019+type@video+block@2976a5da37de4f66b1143b0a4bafb2e9/handler/transcript/download" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>

[Example code](src/5.3.4-AudioVideo.html)



### Activities - Multimedia

1. Embed an audio file in an HTML page with the following requirements:

  + Player has controls to play, pause, seek, etc.
  + Audio must automatically start playing when page loads
  + Audio must be muted when playback begins

  [Sample code](src/5.3.5-Multimedia1.html)

2. Create an HTML audio player that plays an audio file of your choice in Google Chrome, Internet Explorer and Mozilla Firefox. Use multiple sources if you have to.

  [Sample code](src/5.3.5-Multimedia2.html)

3. Create an HTML video player that plays a video file of your choice in Google Chrome, Internet Explorer and Mozilla Firefox. Use multiple sources if you have to.

  [Sample code](src/5.3.5-Multimedia3.html)

4. Create a WebVTT file for [this video](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5315ef6081b631a89442c13f916325c2/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/cat__online-video-cutter.com_.mp4). Then embed this video in an HTML page with the captions you created.

  [Sample code](src/5.3.5-Multimedia3.html)

__Note 1:__ If you wish to share your HTML code in the discussions, you can paste your code directly in a discussion forum post (highlight code and Ctrl+K/use the code widget) or use one of the following online code editors:

+ JS Bin: http://jsbin.com ([JS Bin tutorial](http://code.tutsplus.com/tutorials/javascript-tools-of-the-trade-jsbin--net-36843))
+ CodePen: http://codepen.io ([CodePen tutorial](https://css-tricks.com/video-screencasts/112-using-codepen/))

These are HTML, CSS, and JavaScript code editors that preview/showcase your code bits in your browser. It helps with cross-device testing, realtime remote pair programming.

__Note 2__: If you miss the "pizza cats" video already, don't worry! This video is extensively used in the next HTML5 courses: [HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-w3cx-html5-1x-2) and [HTML5 Apps and Games](https://www.edx.org/course/html5-apps-games-advanced-techniques-w3cx-html5-2x))


## 5.4 Embedding content

### The iframes tag

There are tags for all kinds of content in your Web page, text, images, videos, animations.  There's even a tag that allows you to put another Web page in your Web page - the `<iframe>` tag (HTML Inline Frame Element).  Why would you want to do this?  Well, it enables a lot of possibilities.

The popular online code editor CodePen has several iframes in it to display html, css, javascript and output together. Iframes are generally used in Web pages to show external content/resources. The type of content is not limited to other Web pages. You can add YouTube videos or display a PDF file (some browsers will display the file inline while some older browsers will try to download it instead). 

An `<iframe>` tag can be as simple as this:

```html
<p>This is a parent page that will host the iframe.</p>
<iframe src="https://www.w3.org/">
  <p>Your browser does not support iframes.</p>
</iframe>
```

[Sample code](src/5.4.1-iframe.html)

Because iframes are HTML elements, they can be styled just like other elements, with borders, margins, sizes specified with CSS rules:

<p><iframe src="https://www.youtube.com/embed/YE7VzlLtp-4" style="border: 10px solid red; padding: .5rem; margin: 1rem; box-shadow: 20px 20px 10px #888888; width: 355; height: 200;"></iframe></p>

Here, we've embedded a YouTube video with an iframe like this:

```html
<iframe src="https://www.youtube.com/embed/YE7VzlLtp-4"></iframe>
```

And we've added styling like this to get the border and drop-shadow:

```css
iframe {
  border: 10px solid red;
  padding: .5rem;
  margin: 1rem;
  box-shadow: 20px 20px 10px #888888;
  width: 355;
  height: 200;
}
```

There is one significant problem with iframes. Suppose you create your Web page, containing only an iframe with `src="http://foo.com"`, with no borders, padding or margin. By all appearances, you would seem to be on the Web site foo.com. If you don't look at the URL, it might be difficult to tell. For reasons like this, some Web sites disallow their inclusion, so if you create an iframe with `src="https://google.com"`, you'll get a blank frame and an error message in the console.  This isn't a bug, it's a feature.

There are a number of important attributes for an `<iframe>` tag, but for now we'll just look at a few of them:

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=100%>
<tbody>
  <tr>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Attribute</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Description</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="25%">Value</td>
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="25%">Example</td>
  </tr>
  <tr>
    <td>src</td>
    <td>Specifies the address of the page you want to display in your frame. This is the primary attribute of interest in the iframe.</td>
    <td>URL</td>
    <td>&lt;iframe src="https://www.w3.org/"&gt;&lt;/iframe&gt;</td>
  </tr>
  <tr>
    <td>allowfullscreen</td>
    <td>This will allow the iframe to open "Full screen mode", often used with videos. Without this attribute, full screen mode is disabled for the iframe.</td>
    <td>no value</td>
    <td><span style="line-height: 22.4px;">&lt;iframe src="https://www.w3.org/" allowfullscreen&gt;&lt;/iframe&gt;</span></td>
  </tr>
  <tr>
    <td>name</td>
    <td>Specifies a name for the iframe. Using the name attribute, the iframe can act as a target for a link. Just as the 'self' target will replace the current window with  the site at the href URL, and "_blank" will open a new window at that URL, if you set the name attribute, that name can be used as a target so that when you click on it,   the new page will open up in that iframe.</td>
    <td>text</td>
    <td>
      <p>&lt;iframe name="frame-one" src="https://www.w3.org/"&gt;&lt;/iframe&gt;</p>
      <p>&lt;a href="https://www.wikipedia.org/" target="frame-one"&gt;&lt;/a&gt;</p>
    </td>
  </tr>
  <tr>
    <td>sandbox</td>
    <td>
      <p>This can&nbsp;apply a number of restrictions on the iframe, preventing the site in the iframe from using pop-ups, running scripts, automatically running videos and  numerous other things. &nbsp;This helps avoid some of the potential security issues that iframes may be prone to.</p>
    </td>
    <td><no value="">no value (applies all restrictions)  <br>allow-forms<br>allow-modals<br>allow-orientation-lock<br>allow-pointer-lock<br>allow-popups<br>allow-same-origin<br>allow-scripts<br>allow-top-navigation<br></no></td>
    <td>
      <p>&lt;iframe src="https://www.w3.org/" sandbox&gt;&lt;/iframe&gt;</p>
      <p>OR</p>
      <p>&lt;iframe src="https://www.w3.org/" sandox="allow-popups"&gt;&lt;/iframe&gt;</p>
    </td>
  </tr>
  <tr>
    <td>width, height</td>
    <td>While width and height are valid attributes for an iframe, they should be avoided in favor of CSS properties.</td>
    <td>pixels</td>
    <td>&lt;iframe src="https://www.w3.org/" width="500"&gt;&lt;/iframe&gt;</td>
  </tr>
</tbody>
</table>

Notes:

1. Certain Web sites like Google and Yahoo disallow embedding their Web pages in iframes. So you will not be able to use these pages in an iframe.
2. Not all attributes are supported in all browsers. You are encouraged to explore their browser support before adding to your HTML.
3. You can find more details about iframes from the [W3C Specification](https://www.w3.org/TR/html5/embedded-content-0.html#the-iframe-element).

<hr/>
Iframes can be very useful:

+ Iframes load separately from the main page. However, they do block the main page's load command until its content finishes loading. You can avoid this by applying some Javascript. This allows them to load independently. Then, if the embedded page you are displaying loads slower, you can use your parent page to keep the reader occupied.
+ Sandboxing provides security.
+ Great for third party content like ads.
+ It is convenient to use if you need to have one part of your page static while the other is changed - i.e. navigation menus. Helps reduce bandwidth and server load because we can avoid loading the same content every time a new page is visited in your webpage.

However, there can be some disadvantages:

+ It is easy to misuse them. It should be considered a piece of content in the webpage and not as an integral part of it.
+ Accessibility of iframes is poor. Screenreaders do not process them well but you can proceed to use iframes with a notice for the reader.
+ You have no control over the content in an iframe if you display external content. That content can change anytime or can upload malicious content without your permission.
+ Search engines have trouble accessing and in turn indexing the content in your iframes. This doesn't help your search ranking.


#### Knowledge check 5.4.1

If you want to embed a video that can be viewed in full screen mode, which attribute would you use?

  1. sandbox
  2. name
  3. allowfullscreen
  4. src

  Ans: 3 <br/>
  Explanation:
  + sandbox by default provides a bunch of restriction to your iframe. You can change these restrictions by providing the appropriate value for this attribute.
  + Using the name attribute you can make the iframe the target of a link
  + allowfullscreen: This will permit the web page in the iframe to request full screen mode
  + src gives the address of the page you want to display in your frame.
  + Submit Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.


### The ismap and usemap attributes

__Important__: The attributes we will see in this unit - `ismap` and `usemap` are __image attributes__. Since they use the `<link>` tag, having learned hyperlinks, now would be a good time to explore them. Be sure to watch the video at the end of this unit. 

Adding the `ismap` or `usemap` attributes to the `<img>` tag means that the picture is an image with clickable areas. Imagine a picture of a world map where different countries on the map can be clicked and it navigates to another page like the country's wikipedia page. Simply put, we say such an image is mapped. [Here is an example](http://html.cita.illinois.edu/text/map/map-example.php) of an image-map.


#### The 'ismap' attribute

```html
<img src="images/logo.png" alt="ismap tutorial" ismap>
```

`ismap` is a __boolean attribute__ i.e. its value is either true or false. Thus, just the presence of the attribute indicates that it is a mapped image. To be more precise, we say it is a server-side image-map.

An `<img>` tag with the src  and ismap attributes creates an image with the image source file and indicates it is a server-side image-map. How will your code know that if you click on a part of your image, i.e. 'Australia in a world map', it should navigate to the country's Wikipedia page? We need to create a map file with these details and then add the location of this map file using the anchor element. Here is a code sample:

```html
<a href="/ismap-image/ismap.cgi" target="_self">
   <img src="images/logo.png" alt="ismap tutorial" ismap>
</a>
```

Here, the `href` attribute points to the location of the map file. The `target` attribute indicates where the page it navigates to should open. '_self' will open in the same page whereas '_blank' will open it in a new tab or window. 

`ismap` only works if the `<img>` tag is used within the anchor element like in the code above. This is important because without a link to the target map file, it has no idea what to do with your `ismap` specification.

Let's look at how the code above works.

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/5854bfc005394517ae62fc55fd58242e/2ccb5b1d17534407918e7f2d963617d9/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%40fd6fc633e26d417290e6e78df5bb300d">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e9ac0c6a8e11be57f47e7b43dca6ffa3/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/2.4-ismap3.jpg" style="margin: 0.1em;" alt="Image illustrating how an image map works, how it processes mouse click coordinates using a map file that define target areas" title="Image illustrating how an image map works, how it processes mouse click coordinates using a map file that define target areas" width=250>
  </a></div>
</div>

Let's go back to our world map example where clicking on different parts of the image will take you to a page about the country you clicked on. The map file <strong>'/ismap-image/ismap.cgi'</strong> defines target areas. We can define the image in terms of coordinates. When a user clicks on a part of the image, we can calculate the exact 'x' and 'y' coordinates of the image that was clicked. When the user clicks, the browser will consult with the map file on the server (specified in the anchor tag), by sending these mouse click coordinates to the server. Based on these coordinates, the map file will return the Web page it should navigate to, to the browser. 

Read more about image maps [on wikipedia](https://en.wikipedia.org/wiki/Image_map). You might be inclined to assume an image map will only be used for an actual map. However, there are a lot more use cases for it. The [Atlas Magazine](http://www.atlasmagazine.com/win98r.html) is a good example.

Try this: Navigate to the Atlas magazine and explore the header image with a 'laughing budha' like image. The image acts as a site navigator. Clicking on different parts of the image will bring you to different parts of the Web page. You can use image maps in many creative ways. 


#### The 'usemap' attribute

`usemap` is a lot like `ismap` and is more widely used. `ismap` deals with server-side image-maps whereas `usemap` deals with client-side image-maps. 

+ Server-side image-maps: use separate map files that have to be downloaded. They depend on the server for translating the request. They also create additional network traffic.
+ Client-side image-maps: reside within an HTML document. The browser takes care of the translation (translating mouse coordinates clicked to corresponding Web pages).

Client-side maps are becoming increasingly popular. usemap is NOT of type boolean. It takes in the name of the map with a '#' character preceding it.

```html
<img src="navigator.jpg" alt="Pages in this Web site" usemap="#navigatormap">
```

Like `ismap`, `usemap` cannot be used by itself. In `ismap`, we used the anchor tag to specify the map file. In usemap, we use the `<area>` element as a child of `<map>` element to specify the coordinates and the page it should navigate to. The `usemap` value should match the map element's name or id attribute. 

```html
<img src="images/crossroads.jpg" alt="Crossroads" usemap="#navigatormap">
<map name="navigatormap">
  <area shape="rect" coords="0,0,195,439" href="https://en.wikipedia.org/wiki/Millery" alt="Millery">
  <area shape="rect" coords="196,0,390,439" href="https://en.wikipedia.org/wiki/Nomeny" alt="Nomeny">
</map>
```

`<map>` - defines a client-side image map and is used to create a relationship between the image and the map by matching the map name and usemap's value. It contains a set of area elements.

`<area>` - defines the areas that can be clicked and the pages it should navigate to. Typically takes the shape of the area, coordinates of the area, URL of the page it should redirect to and the alt attribute (short description). 

The `shape` attribute in the `<area>` tag has four values:

+ circle - The clickable area is a circle. You need to specify three coordinates. E.g. coords="89,52,6". The first two is the coordinate center of the circle and the last is the radius.
+ rect - The clickable area is a rectangle. You need to specify four coordinates. E.g. coords="0,0,195,439". This is the x & y coordinates of the top left corner and the x & y coordinates of the bottom right corner.
+ poly - The clickable area is a polygon of any number of sides. This shape is very flexible and takes as many pairs of coordinates as you need to form your polygon.  E.g. coords="277,85,322,87,275,173,269,138". The last set of coordinates can match the first set. If it doesn't, the browser will automatically match it for you to close the polygon.
+ default - The clickable area is the whole image.

Read more about the [area tag here](https://www.w3.org/wiki/HTML/Elements/area).

Here is a working example of usemap.

```html
<img src="images/crossroads.jpg" alt="Crossroads" usemap="#navigatormap">
<map name="navigatormap">
  <area shape="rect" coords="0,0,195,439" href="https://en.wikipedia.org/wiki/Millery" alt="Millery">
  <area shape="rect" coords="196,0,390,439" href="https://en.wikipedia.org/wiki/Nomeny" alt="Nomeny">
</map>
```

Result:

Try this: Click on the left and right side of the images to check out how usemap works :) Remember to navigate back to the course!

<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/5854bfc005394517ae62fc55fd58242e/2ccb5b1d17534407918e7f2d963617d9/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%40fd6fc633e26d417290e6e78df5bb300d">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6b92cf65974c9fc413cb88abc50b5360/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/img-usemap.jpg" style="margin: 0.1em;" alt="Signpost in France. Select to find out more information about each town." title="Signpost in France. Select to find out more information about each town." width=200>
  </a></div>
</div>


Note: If the `<img>` is inside an `<a>` or `<button>` element, clicking on it will be interpreted as clicking on the link or button and usemap will not work.


#### 'ismap' & 'usemap' Attributes Activity

To get a better understanding on the usemap attribute, edit this project on [CodePen](http://codepen.io/w3devcampus/pen/BROBwG/) shown below.

[Sample code](src/5.4.2-IsmapUsemap.html)

It showcases two image maps that can be used for page navigation with the areas mapped using 'rect' and 'poly' shapes. The coordinates were generated using an online image map generator tool.

Experiment with it and try your own image map variations. 


#### Knowledge check 2.5.4

The map element's name or id attribute should match the ______ attribute's value.

  1. ismap
  2. coord
  3. usemap
  4. href

  Ans: 3<br/>
  Explanation: Usemap cannot be used by itself and should be associated with the map element. Matching the map element's name/id with the usemap attribute's value creates a relationship between the map and the image.


### Activities - Embedding content

1. How can you inform screen readers that you are using an iframe in your Web page since iframes have poor accessibility?
2. Try the following code in your HTML editor:

  ```html
  <iframe src="http://facebook.com">
    <p>Your browser does not support iframes.</p>
  </iframe>
  ```

  What happens? Why does it behave the way it does?

[Sample code](src/5.4.3-Embedding.html)

Ans: www.facebook.com refused to connect.


## 5.5 CSS tricks

### Decorative images and backgrounds

As we saw earlier, the `<img>` tag is meant to be used for semantically important imagery.  For example, the pictures that accompany a news story are important to understanding the news story and therefore should be displayed with the `<img>` tag.  The example of the cool banner with teletypes and coffee was meant to evoke competence and urgency, however, that image is __not__ essential to understanding the news story. That image is decorative.

Decorative images are incorporated via CSS.

There are quite a few CSS properties for controlling borders, background images and colors. Let's look at the most common. Take notice that as you leverage borders and backgrounds that you will begin to see the underside of the Web. How big is the area around a link? You might have never thought about it before, now it'll be visible. Can we make it larger or smaller? Are these items butted against each other? Can we space them out, or bring them closer? We will touch on these things as well.

Let's look at the most common CSS properties: `background-color`, `background-image`, `background-repeat`, `background-size`, and `background-position`.


#### background-color

The `background-color` CSS property will fill the rectangle of the given element with a solid background color. In addition to the values of <span style="color: #ff6000;">transparent</span> and <span style="color: #ff6000;">none</span>, there are all the values of  that we saw applicable to the color property.

In the example below we apply a variety of background colors to a hyperlink (`<a>`), paragraph (`<p>`), unordered list (`<ul>`) and list items (`<li>`):

<div>
<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">HTML</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">CSS</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Result</th>
  </tr>
  <tr>
    <td>
      <pre style="border: none;">&lt;p class="p-blue"&gt;This is the list of critters<br/>&lt;a href="#req"&gt;requested&lt;/a&gt; by the owners&lt;/p&gt;<br/>&lt;ul&gt;
    &lt;li&gt;Wasp&lt;/li&gt;<br/>  &lt;li&gt;Ant&lt;/li&gt;<br/>  &lt;li&gt;Moth&lt;/li&gt;<br/>  &lt;li&gt;Ostritch&lt;/li&gt;<br/>&lt;/ul&gt;</pre>
  </td>
    <td style="white-space: nowrap;">
      <pre style="border: none;"><span style="color: #0000ff;">   p</span> { <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">#3E3F67</span>; }<br/><span style="color: #0000ff;">p a</span> { <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">#6E7099</span>; }<br/><span style="color: #0000ff;">  ul </span>{ <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">#FFC592</span>; }<br/><span style="color: #0000ff;">   li </span>{ <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">#CC602D</span>; }<br/><br/></pre>
    </td>
    <td>
      <p style="background-color: #3E3F67; color: #52B3FF !important;">This is the list of critters <a href="#req">requested</a> by the owners</p>
      <ul style="background-color: #FFC592;">
        <li style="background-color: #CC602D; color: #52B3FF;">Wasp</li>
        <li style="background-color: #CC602D; color: #52B3FF;">Ant</li>
        <li style="background-color: #CC602D; color: #52B3FF;">Moth</li>
        <li style="background-color: #CC602D; color: #52B3FF;">Ostritch</li>
      </ul>
    </td>
  </tr>
</tbody>
</table>
</div>


#### background-image

The `background-image` property is used to set an external image file as the background to a particular HTML element.  To bind in an external file, the value is <span style="color: #ff6000;">url</span>, followed by an open parenthesis <span style="color: #ff6000;">(</span>, followed by a quote <span style="color: #ff6000;">"</span>, then the path, a closing quote <span style="color: #ff6000;">"</span> and a closing parentheses <span style="color: #ff6000;">)</span>.  The path can be a URL, or a path relative from the file the CSS is in.

<code><span style="color: #0000ff; margin: 1em;">div</span> { <span style="color: #333399;">background-image</span>: <span style="color: #ff6600;">url</span>(<span style="color: #ff6600;">"https://www.w3.org/2008/site/images/logo-w3c-mobile-lg"</span>); } <br><span style="color: #0000ff;  margin: 1em;">div</span> { <span style="color: #333399;">background-image</span>: <span style="color: #ff6600;">url</span>(<span style="color: #ff6600;">"images/kitten.png"</span>); }</code>

As these are decorative images, there are quite a few different usage scenarios that can leverage background images. For instance, an image can be used as repeating tile, or a background image can fit its parent element, or be a large panoramic image not fully viewed.  These scenarios can be constructed with other CSS properties, like background-repeat, background-size, and background-attach (as well as several others). 

<div>
<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">HTML</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">CSS</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Result</th>
  </tr>
  <tr>
    <td>
      <pre style="border: none;">&lt;p class="kitten"&gt;Women and cats will do as they please, and men and dogs should relax and get used to the idea. &lt;br /&gt;- Robert A. Heinlein&lt;/p& gt;</pre>
    </td>
    <td style="width: 320px;">
<pre style="border: none;"><span style="color: #0000ff;"> 
.kitten</span> { <br><span style="color: #333399;">   background-image</span>: <span style="color: #ff6600;">url</span>(<span style="color: #ff6600;">"kittens.jpg"</ span>); <br> }

</pre>
    </td>
    <td style="width: 320px;">
      <p style="background-image: url(https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e2f19da73069f153ebe3d3ca51ce8a3f/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/kitten2.jpg); background-size: cover; font-size: 24px; padding: 30px; color: white; font-family: serif;">Women and cats will do as they please, and men and dogs should relax and get used to the idea. <br>- Robert A. Heinlein</p>
    </td>
  </tr>
</tbody>
</table>
</div>


#### background-repeat

By default, if the rectangular area of an element is bigger than the image itself, then the image will repeat and fill the space, like tiles.  For example:

<div>
<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>CSS</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=30%>Result</th>
  </tr>
  <tr>
    <td style="vertical-align: top;">
<pre style="border: none;"><span style="color: #0000ff;"> 
.tile</span> { <br><span style="color: #333399;">   background-image</span>: <span style="color: #ff6600;">url</span>(<span style="color: #ff6600;">"https://www.w3.org/2008/site/images/logo-w3c-mobile-lg"</span>); 
  <span style="color: #808080;">/* use padding to keep the text away from the edges of the paragraph box */</span>
  <span style="color: #333399;">padding-top</span>:    <span style="color: #ff6600;">15px</span>;
  <span style="color: #333399;">padding-right</span>:  <span style="color: #ff6600;">50px</span>;
  <span style="color: #333399;">padding-bottom</span>: <span style="color: #ff6600;">30px</span>;
  <span style="color: #333399;">padding-left</span>:  <span style="color: #ff6600;">100px</span>;
}

</pre>
    </td>
    <td class="tile-img">
      <p style="background-image: url(https://www.w3.org/2008/site/images/logo-w3c-mobile-lg); font-size: 24px !important; line-height: 48px !important; padding: 15px 50px 30px 100px; text-shadow: 1px 1px 1px black, -1px -1px 1px black; color: yellow; font-family: serif;">The World Wide Web Consortium (W3C) is an international community where Member organizations, a full-time staff, and the public work together to develop Web standards.</p>
    </td>
  </tr>
</tbody>
</table>
</div>

The background-repeat property can be used to control this.  It's more commonly used values are: <span style="colot: #ff6000;">repeat</span>, <span style="colot: #ff6000;">repeat-x</span>, <span style="colot: #ff6000;">repeat-y</span>, and <strong><span style="colot: #ff6000;">no-repeat</span></strong>. The no-repeat value is very useful, and bears repeating.

There are advanced uses of this property.  Notice in the above example, that if the size of the parent element is not exactly a multiple of the tile, then the image may be "cropped" and bleed off the side.  That can be managed by centering the tile (with `background-position: center;`).  Additionally the background-repeat property can also be used to control how it repeats. The <span style="colot: #ff6000;">space</span> value will result in cropped images; it means "repeat, and add space between the elements so there is no cropping".  Note that this property does not let you directly manipulate the amount of spacing. That is calculated for you.

<div>
<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
<tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;">background-repeat: space</th><thstyle="text-align: center; background-color: #3d64ff; color: #ffffff;"></th></tr>
<tr>
<td style="width: 50%;">
<p style="background-image: url(https://www.w3.org/2008/site/images/logo-w3c-mobile-lg); font-size: 24px; padding: 15px 50px 30px 100px; text-shadow: 1px 1px 1px black, -1px -1px 1px black; color: yellow; font-family: serif;">The World Wide Web Consortium (W3C) is an international community where Member organizations, a full-time staff, and the public work together to develop Web standards.</p>
</td>
<td></td>
</tr>
</tbody>
</table>
</div>


#### background-size

When _not_ repeating, it is very useful to size a background image to fit its element.  The `background-size` can be used for this.  There are two very useful values:  `contain` and `cover`.   The `contain` value will put the entire image into the space of the element, however, the space of the element may not be completely filled if the aspect ratio of the element and the image do not match.  The `cover` value is the opposite. It will completely fill the element but the image may be cropped off two opposite sides.  Neither contain or cover will distort or squish the image.  Its aspect ratio is maintained.

Here we demonstrate the difference. A border has been applied to the paragraph to clearly show the bounds of the parent `<p>` element.

<div>
<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=50%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>background-size: contain</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">background-size: cover</th></tr>
  <tr>
    <td style="color: rgb(211, 211, 211);">
      <p style="background-image: url(https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e2f19da73069f153ebe3d3ca51ce8a3f/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/kitten2.jpg); background-repeat: no-repeat; font-size: 20px !important; padding: 15px; color: lightgray !important; font-family: serif; width: 180px; height: 180px; border: 2px solid black; background-size: contain;">Women and cats will do as they please, and men and dogs should relax and get used to the idea. <br>- Robert A. Heinlein</p>
    </td>
    <td style="color: rgb(211, 211, 211);">
      <p style="background-image: url(https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e2f19da73069f153ebe3d3ca51ce8a3f/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/kitten2.jpg); background-repeat: no-repeat; font-size: 20px !important; padding: 15px; color: lightgray !important; font-family: serif; width: 180px; height: 180px; border: 2px solid black; background-size: cover;">Women and cats will do as they please, and men and dogs should relax and get used to the idea. <br>- Robert A. Heinlein</p>
    </td>
  </tr>
</tbody>
</table>
</div>

The `background-size` property can also be used to more exactly size the image.  When used in this fashion, it takes two values separated by a space. The first governs the width, the second the height.  Examples:

```css
.kittens  { background-size: 100px 120px; } /* might distort */
.puppies  { background-size: 100px auto; }  /* auto preserves aspect ratio, no distorting */
.munchies { background-size: 50% auto; }    /* % is of percentage of parent (not of image). */
```

 The px and % units were covered in the units section. Note that other units (rem, vh, etc.) have no guarantee of support.  

When specifying exact sizes, the <span style="color: #ff6000;">auto</span> value is extremely useful. It allows you to worry only about one dimension, and then the other will handle it for you. Otherwise there is a risk of stretching/distorting images.

<div>
<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>background-size: 140px 100px;<br>/* will distort */</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>background-size: 130px auto;</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>background-size: 50% auto;</th></tr>
  <tr>
    <td style="color: rgb(211, 211, 211);">
      <p style="background-image: url(https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e2f19da73069f153ebe3d3ca51ce8a3f/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/kitten2.jpg); background-repeat: no-repeat; font-size: 20px !important; padding: 15px; color: lightgray !important; font-family: serif; width: 180px; height: 180px; border: 2px solid black; background-size: 140px 100px;">Women and cats will do as they please, and men and dogs should relax and get used to the idea. <br>- Robert A. Heinlein</p>
    </td>
    <td style="color: rgb(211, 211, 211);">
      <p style="background-image: url(https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e2f19da73069f153ebe3d3ca51ce8a3f/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/kitten2.jpg); background-repeat: no-repeat; font-size: 20px !important; padding: 15px; color: lightgray !important; font-family: serif; width: 180px; height: 180px; border: 2px solid black; background-size: 130px auto;">Women and cats will do as they please, and men and dogs should relax and get used to the idea. <br>- Robert A. Heinlein</p>
    </td>
    <td style="color: rgb(211, 211, 211);">
      <p style="background-image: url(https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e2f19da73069f153ebe3d3ca51ce8a3f/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/kitten2.jpg); background-repeat: no-repeat; font-size: 20px !important; padding: 15px; color: lightgray !important; font-family: serif; width: 180px; height: 180px; border: 2px solid black; background-size: 50% auto;">Women and cats will do as they please, and men and dogs should relax and get used to the idea. <br>- Robert A. Heinlein</p>
    </td>
  </tr>
</tbody>
</table>
</div>


#### background-position

Like `background-size`, `background-position` can be used to place or offset a background image in the element. It takes two values (x and y) separated by a space when used to exactly specify a position. 

The most useful is the `center` value.  It is position the center of the image in the center of the element. This is useful even with repeating tiles. 

<div>
<table style="font-family: arial,helvetica,sans-serif; border-collapse: collapse" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=60%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff; font-size: 1.3em;" width=100% colspan="2">background-position:center</th></tr>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>background-size: contain</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>background-size: cover</th>
  </tr>
  <tr>
    <td style="border: 1px solid black;">
      <p style="background-image: url(https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e2f19da73069f153ebe3d3ca51ce8a3f/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/kitten2.jpg); background-repeat: no-repeat; font-size: 20px !important; padding: 15px; color: lightgray !important; font-family: serif; width: 180px; height: 180px; border: 2px solid black; background-size: contain; background-position: center;">Women and cats will do as they please, and men and dogs should relax and get used to the idea. <br>- Robert A. Heinlein</p>
    </td>
    <td class="cover">
      <p style="background-image: url(https://prod-edxapp.edx-cdn.org/assets/courseware/v1/e2f19da73069f153ebe3d3ca51ce8a3f/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/kitten2.jpg); background-repeat: no-repeat; font-size: 20px !important; padding: 15px; color: lightgray !important; font-family: serif; width: 180px; height: 180px; border: 2px solid black; background-size: cover; background-position: center;">Women and cats will do as they please, and men and dogs should relax and get used to the idea. <br>- Robert A. Heinlein</p>
    </td>
  </tr>
</tbody>
</table>
</div>



### Decorative borders and shadows

In the previous sub-section, we looked at decorative backgrounds and images. We will continue this theme by examining decorative borders and shadows.  Like background colors, once we start using borders we will be directly facing the underpinnings of HTML. Where does a span inside a paragraph begin and end? How far does it extend? We'll see how the various techniques for managing decorative CSS in the following sub-section.

For now, let's look at these new properties: `border-style`, `border-color`, `border-width`, border abbreviations, `border-radius` and `text-shadow`.


#### border-style

```css
p { border-style: solid; }
```

This property sets the style of a border.  Possible values include <span style="color: #ff6000;">none, hidden, solid, dotted, dashed, double, groove, ridge, inset</span>, and <span style="color: #ff6000;">outset</span>. Here the visible border styles displayed on a gray border:

<table style="border-collapse: separate; border-spacing: 4px;" width=100%>
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


Note that the <span style="color: #ff6000;">groove, ridge, inset</span> and <span style="color: #ff6000;">outset</span> borders all use black in addition to any explicit border-color.  So if the border-color is also black they won't be effective.  Also <span style="color: #ff6000;">double, groove</span> and <span style="color: #ff6000;">ridge</span> are usually not satisfactory on thin borders.  They'll require a fat `border-width`.

The difference between <span style="color: #ff6000;">none</span> and <span style="color: #ff6000;">hidden</span> has to do with the sizing and positioning of the element. An item with a hidden border is positioned as if it had a border, but the border is not drawn. Whereas with border-style of none, no space is allocated for the border at all.


#### border-color

Sets the color of the border.  


#### border-width

Sets the width of the border.  Supports a variety of units (px, em, rem ).  


#### border abbreviations

All border styles just introduced are actually abbreviations that can be broken out if needed. For example, here we set four different styles for a border:  

```css
p { 
   border-left-style: solid; 
   border-right-style: dotted; 
   border-bottom-style: dashed; 
   border-left-style: hidden; 
}
```

This same thing can be done with `border-width` and `border-color` (`border-left-color`, `border-top-width`, etc).

Or, going in the other direction, the CSS property border can help abbreviate even further.  Use the formula  border: `<width> <style> <color>`;   separating the values with spaces:

```css
p { border: 1px solid gray; }
```


#### border-radius

Sometimes it seems that the whole of the World Wide Web consists of round cornered rectangles.  Join the fun by using the border-radius property:  

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>Result</th></tr>
  <tr>
    <td>
<pre style="border: none;"><span style="color: #0000ff;"> .rrect</span> { 
   <span style="color: #333399;">border-width</span>: <span style="color: #008000;">4px</span>;
   <span style="color: #333399;">border-style</span>: <span style="color: #ff6600;">double</span>;
   <span style="color: #333399;">border-radius</span>: <span style="color: #008000;">20px</span>;  <span style="color: #808080;">/* round corners */</span>
   <span style="color: #333399;">padding</span>: <span style="color: #008000;">15px</span>;
   <span style="color: #333399;">text-align</span>: <span style="color: #ff6600;">center</span>;
  }  
</pre>
    </td>
    <td>
      <p style=" border-width: 4px; border-style: double; border-radius: 20px; padding: 15px; text-align: center;">Silence is Golden</p>
    </td>
  </tr>
</tbody>
</table>

Note this is fun to use with a background color or background image and no border at all:

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>Result</th></tr>
  <tr>
    <td>
<pre style="border: none;"><span style="color: #0000ff;"> .rrectbg</span> { 
   <span style="color: #333399;">border-style</span>: <span style="color: #ff6600;">none</span>; <span style="color: #808080;">/* no border at all */</span>
   <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">beige</span>;
   <span style="color: #333399;">border-radius</span>: <span style="color: #008000;">20px</span>;
   <span style="color: #333399;">padding</span>: <span style="color: #008000;">15px</span>;
   <span style="color: #333399;">text-align</span>: <span style="color: #ff6600;">center</span>;
  }  
</pre>
    </td>
    <td>
      <p style="border-style: none; background-color: beige; border-radius: 20px; padding: 15px; text-align: center;">Silence is Golden</p>
    </td>
  </tr>
</tbody>
</table>


#### box-shadow

A shadow effect can be applied to the outlining rectangle of an element with the `box-shadow` CSS property.  The `box-shadow` property is typically controlled with four values separated by spaces:

<code><span style="color: #333399; margin-left: 2em;">box-shadow</span>: <span style="color: #ff6600;">&lt;x-offset&gt; &lt;y-offset&gt; &lt;blur&gt; &lt;color&gt;</span>;</code>

The offset values are dimension units (px, em, etc) can be positive or negative. Positive x values place the shadow to the right, and negative values place the shadow to the left. Similarly positive y values place the shadow vertically lower than the element and negative values move it up.

The `blur` value is also a dimension unit, but can only be 0 or positive.

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>Result</th></tr>
  <tr>
    <td>
<pre style="border: none;"><span style="color: #0000ff;">  
.illuminati</span> { <span style="color: #333399;">box-shadow</span>: <span style="color: #008000;">1px 1px 2px</span> <span style="color: #ff6600;">black</span>; }<br>
<span style="color: #0000ff;">.urakai</span> { <span style="color: #333399;">box-shadow</span>: <span style="color: #008000;">0px 0px 6px</span> <span style="color: #ff6600;">black</span>; }<br>
<span style="color: #0000ff;">p</span> { 
    <span style="color: #333399;">text-align</span>: <span style="color: #ff6600;">center</span>;
    <span style="color: #333399;">padding</span>: <span style="color: #008000;">10px</span>; <span style="color: #808080;">/* make the box a little bigger */</span>
}
</pre>
    </td>
    <td>
      <p style="box-shadow: 1px 1px 2px black; text-align: center; padding: 10px;">Illuminati</p>
      <p style="box-shadow: 0px 0px 6px black; text-align: center; padding: 10px;">Urakai</p>
    </td>
  </tr>
</tbody>
</table>


#### text-shadow

This CSS property takes the same values as box-shadow, however, the shadow is applied directly to the text shapes:

<code><span style="color: #333399; margin-left: 2em;">text-shadow</span>: &nbsp;<span style="color: #ff6600;">&lt;x-offset&gt; &lt;y-offset&gt; &lt;blur&gt; &lt;color&gt;</span>;</code>

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=80%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>Result</th></tr>
  <tr>
    <td>
<pre style="border: none;"><span style="color: #0000ff;">  .majestic-12</span> { <span style="color: #333399;">text-shadow</span>: <span style="color: #008080;">1px 1px 3px</span> <span style="color: #ff6600;">black</span>; }
</pre>
    </td>
    <td>
      <p style="text-shadow: 1px 1px 3px black;">Majestic-12</p>
    </td>
  </tr>
</tbody>
</table>



### Managing element size

As you start to leverage borders, background colors, and the other decorative CSS properties we have seen in the previous sections you will need to become more aware of the element size and how to manage it.


#### The wrong way

A common trap that newbies fall into is to discover the `width`, `height`, `left` and `top` CSS properties and to start blindly using them.

These are useful properties, however, they should __not__ be your first choice.  These CSS properties depend upon other properties before they can even be used, and they can have unintended consequences. We'll explore them more in next module when covering Layout.  

Here is a simple example of a common error:

<table style="font-family: arial,helvetica,sans-serif; word-break: normal;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=60%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>Result</th></tr>
  <tr>
    <td>
<pre><span style="color: #0000ff;">div</span> {
  <span style="color: #333399;">width</span>: <span style="color: #008000;">40px</span>;
  <span style="color: #333399;">border</span>: <span style="color: #008000;">2px</span> <span style="color: #ff6600;">solid red</span>;
  <span style="color: #333399;">font-size</span>: <span style="color: #008000;">18px</span>;
 }
</pre>
    </td>
    <td>
      <div style="    display: block; width: 40px; border: 2px solid red; font-size: 18px;">
        <p>CSS is Awesome</p>
      </div>
    </td>
  </tr>
</tbody>
</table>


#### Padding - The right way

The best way to control an element's size for the purpose of controlling how a border or background extends relative to the item itself is with the padding properties.

Padding is a way of making an element a little bigger than it would normally be.  Similar to margin, there are four padding properties.  The values are dimension units that can be 0 or a positive value; negative values are not allowed.

<pre style="padding-left: 30px; border: none;"><span style="color: #333399;">padding-top</span>:    <span style="color: #008000;">0</span>;
<span style="color: #333399;">padding-right</span>:  <span style="color: #008000;">1em</span>;
<span style="color: #333399;">padding-bottom</span>: <span style="color: #008000;">10px</span>;
<span style="color: #333399;">padding-left</span>:   <span style="color: #008000;">12px</span>;</pre>

Similar to margin, this can be abbreviated with the `padding` property.

<pre style="padding-left: 30px; border: none;"><span style="color: #333399;">padding</span>: <span style="color: #ff6600;">&lt;top&gt; &lt;right&gt; &lt;bottom&gt; &lt;left&gt;</span>;
<span style="color: #333399;">padding</span>: <span style="color: #ff6600;">&lt;top and bottom&gt; &lt;right and left&gt;</span>;
<span style="color: #333399;">padding</span>: <span style="color: #ff6600;">&lt;all&gt;</span>;</pre>

When decorative CSS is not used by many CSS newbies, use padding like margin, to space things out. Note: That is not correct. Margins make space between elements and padding makes an element larger.

In this example, note that the use of padding does not make the text deviate from the baseline.  In addition, note that in the first paragraph we apply the same padding to all four sides. However, in the second paragraph we use different padding for different sides, thus placing the rectangle of the element relative to the text itself.

<table style="font-family: arial,helvetica,sans-serif; word-break: normal;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" colspan="2">HTML</th></tr>
  <tr>
    <td colspan="2">
<pre style="border: none;">&lt;p class="even-pad"&gt;My friends &lt;span&gt;Mr. Thomas&lt;/span&gt; and &lt;span&gt;Mr. Joyce&lt;/span&gt; both hail from Ireland.&lt;/p&gt;

&lt;p&gt;But &lt;span class="proust"&gt;Mssr. Proust&lt;/span&gt; and &lt;span class="voltaire"&gt;Mssr. Arouet&lt;/span&gt; are from France.&lt;/p&gt;
</pre>
    </td>
  </tr>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>Result</th></tr>

  <tr>
    <td>
<pre style="border: none;"><span style="color: #0000ff;">span</span> {
  <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">tan</span>;
}
<span style="color: #0000ff;">.even-pad span</span> {
  <span style="color: #333399;">padding</span>: <span style="color: #008000;">15px</span>;
 }
<span style="color: #0000ff;">.proust</span> {
  <span style="color: #333399;">padding</span>: <span style="color: #008000;">2px 15px 15px 2px</span>;
}
<span style="color: #0000ff;">.voltaire</span> {
  <span style="color: #333399;">padding</span>: <span style="color: #008000;">15px 2px 2px 15px</span>;
}
  </pre>
    </td>
    <td>
      <p>My friends <span style="background-color: tan; padding: 15px;">Mr. Thomas</span> and <span style="background-color: tan; padding: 15px;">Mr. Joyce</span> both hail from Ireland.</p>
      <p>&nbsp;</p>
      <p style="font-size: 12px; margin-top: 20px;">But <span style="padding: 2px 15px 15px 2px; background-color: tan;">Mssr. Proust</span> and <span style="background-color: tan; padding: 15px 2px 2px 15px;">Mssr. Arouet</span> are from France.</p>
    </td>
  </tr>
</tbody>
</table>

I'm confused - are you saying that I shouldn't use the width property to change the width?

Essentially yes. Let's qualify that a bit so there is no confusion.

This section has been about the decorative CSS properties, like borders, background colors, background images, and shadows. In the context of these things users often want to make an element "bigger", or keep the border a bit away. And in this context the `padding` property is absolutely the correct property that should be used to increase the elements size.  Do not use the `width` or `height` properties for this.

Furthermore, there are other issues associated with the `width` and `height` properties. We will discuss these in-depth in the next module. Here is a quick rundown:

+ `height` and `width` properties do not work on inline elements.
+ Many elements have natural behaviors that occur when height and width are __not__ set. These are generally advantageous. However, by setting the width and height you __lose__ those advantages. We'll understand this in next module.
= Most Web pages are viewed in a variety of browser sizes, especially on mobile devices like phones or tablets. Overuse of explicit width and height can make your page unviewable on smaller devices.
= The flexbox layout system (which we will see next) is incredibly powerful, but by over-determining explicit heights and widths you reduce its usefulness to you and your viewer.



### Knowledge checks

The following questions are ungraded. They are here to self-check your understanding of the concepts.

Style rule for questions 1 and 2:

```css
p {
  border: 2px solid black;
  background-color: rgb(150, 50, 20);
}
```

1. Color flush

  Examine the style rule above. Will the color always run flush to the border or will there sometimes be a gap?

  1. Always flush
  2. Sometimes a gap

  Ans: 1


2. Extend flush

  We add a second style rule: `p { padding: 20px; }`. Will the background color still extend flush without a gap to the border?

  1. Yes, always flush
  2. No, there will be a gap

  Ans: 1, x2


3. Which of these statements are true?

  ```css
  div {
  border: 2px solid black;
  background-image: url('images/sumptuous_eyes.jpg');
  }
  ```

  Which of these statements are true? Check all that qualify.
  
  1. As written above, the image would fill the `<div>` flush to the border without gaps. The image will tile/repeat if necessary.
  2. As written above, the image will stretch as necessary to fill the `<div>` flush to the border without gaps.
  3. With the additional style rule of background-repeat:no-repeat; we could potentially introduce a gap between the image and the border.

  Ans: 13


4. Larger

  If you need to make an element a little larger, which property should you use?

  Ans: padding or padding-left or padding-top or padding-right or padding-bottom


5. Extra space

  If a border or box-shadow is too snug to the content, what property can you use to get some extra space?

  Ans: padding or padding-left or padding-top or padding-right or padding-bottom


6. Padding property

  Will the padding property have any effect on the text-shadow property?

  Ans: No

7. Negative padding

  Can negative padding be used to make an element smaller?

  Ans: No



### Pseudo classes and cursor

#### Refined CSS selectors - pseudo classes

If you have a page with some links on it, and you look at them carefully, you may notice that some of the links that you've visited before are a different color than those you haven't (purple versus blue, typically). Plus, if the mouse is brought over a link, it may change color again, or highlight in some other way. In addition, if you click down and don't let the mouse down, then maybe the link may change yet again. Lastly, if you visit some other sites and make these same explorations, you may observe visual differences from site to site. You may conclude that the styling of the elements are being changed, and you will be right. How did the author of the style sheet know which links you've been to already?

"Pseudo Classes" is a fancy term for simply being able to refine our CSS selection to something that isn't just another element. Pseudo Classes allow us to apply styles to the different states of an element. Or to various children of an element based on their index, or to other interactions with the browser. Best of all, pseudo classes are easy to use.

```css
a:visited { color: purple; }
```

Above us we see a tag selector (`a`) followed by a pseudo class, which consists of a colon and a word (e.g. `:visited`). This particular CSS rule will be applied to any `<a>` tag that the user has already visited. There can be no spaces on either side of the colon. Pseudo classes can be amended onto _any_ CSS selector, not just tag selectors.

A full list of pseudo classes can be found [here](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes). Let's look at some of the most common ones.


#### :visited

```css
a:visited { color: purple; }
```

The `:visited` pseudo class is usually put on a selector that resolves to an `<a>` tag. It enables you to define a style for the visited state of the link. For example, if the user has already been to that Web site, the :visited style will be applied.


#### :hover / :active

```css
li:hover  { background-color: red; }
li:active { background-color: green; }
```

The `:hover` pseudo class lets you change the style for an element when the mouse is hovering above it.  The `:active` pseudo class is applied when the mouse is depressed into its area.  Note that the mouse is rarely hovering or clicking over/into "just one" item. At any given moment, the mouse is usually over several elements, because if it is over a child element, it will be over the parent, grandparent, and great grandparent.  Therefore, if you have two different style rules, such as `li:hover` and `ul:hover`, then they will both be activated,  when the mouse is over one of the list items.  

<table style="font-family: arial,helvetica,sans-serif; word-break: normal;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=20%>CSS</th><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=10%>Result (Try It!)</th></tr>
  <tr>
    <td>
<pre style="border: none;"><span style="color: #3366ff;">li</span>:hover  { <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">lightblue</span>; }
<span style="color: #3366ff;">li</span>:active { <span style="color: #333399;">background-color</span>: <span style="color: #ff6600;">red</span>;  }
<span style="color: #3366ff;">ul</span>:active { <span style="color: #333399;">border</span>: <span style="color: #339966;">1px</span> <span style="color: #ff6600;">solid pink</span>; }
 </pre>
    </td>
    <td>
      <ul style="list-style: none;">
        <li style="margin-bottom: 0.70788em;">shark</li>
        <li style="margin-bottom: 0.70788em;">marlin</li>
        <li style="margin-bottom: 0.70788em;">tuna</li>
        <li style="margin-bottom: 0.70788em;">whale</li>
        <li style="margin-bottom: 0.70788em;">koi</li>
        <li style="margin-bottom: 0.70788em;">barracuda</li>
        <li style="margin-bottom: 0.70788em;">octopus</li>
      </ul>
    </td>
  </tr>
</tbody>
</table>


#### :nth-child

```css
tr:nth-child(odd)  { background-color: lightgray; }
tr:nth-child(even) { background-color: white; }
```

The `:nth-child` pseudo class is very handy.  Unlike the pseudo classes we've seen so far, it expects a parameter. The pseudo class always ends with a pair of parentheses with an expression inside.  This expression is simply the term odd or even, however, there are other more advanced possibilities with mathematical equations containing the term `n`.

This selector is most commonly used to apply "transaction ledger" styles to tables or lists.

<table style="font-family: arial,helvetica,sans-serif; word-break: normal;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=60%>
<tbody>
  <tr><th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width=20%>Example: nth-child(even)</th></tr>
    <tr>
    <td>
      <ul style="list-style: none;">
        <li style="margin-bottom: 0.70788em; padding: 4px 15px; ">shark</li>
        <li style="margin-bottom: 0.70788em; padding: 4px 15px; background-color: whitesmoke;">marlin</li>
        <li style="margin-bottom: 0.70788em; padding: 4px 15px; ">tuna</li>
        <li style="margin-bottom: 0.70788em; padding: 4px 15px; background-color: whitesmoke;">whale</li>
        <li style="margin-bottom: 0.70788em; padding: 4px 15px; ">koi</li>
        <li style="margin-bottom: 0.70788em; padding: 4px 15px; background-color: whitesmoke;">barracuda</li>
        <li style="margin-bottom: 0.70788em; padding: 4px 15px; ">octopus</li>
      </ul>
    </td>
  </tr>
</tbody>
</table>


#### Cursor property

```css
li { cursor: pointer; }
```

Since we've broached the topic of mouse-responding pseudo classes, it makes sense to also cover the `cursor` CSS property.

The cursor CSS property lets you change the cursor that is displayed when the mouse is over the element in question.  This does not have to be relegated to a :hover style, it can be applied anywhere. Though, if you want to change the cursor when an element is depressed,  set the `cursor` property in the context of an `:active` style.

There are many possible values for the cursor property.  Their exact representation may vary slightly from browser to browser.  Common values include: `default`, `pointer`, `text`, `move` and `grab`. (Hover over each value to see). In addition, some browsers support a custom image as well  (`cursor: url("images/my_pointer.png");`).

For more information, please visit the [MDN page on cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor).


#### Knowledge check 5.5.5

You are developing a Web page, and desire that the hyperlinks italicize as the mouse is over them. Which of these rules will achieve that?

  1. This cannot be achieved without JavaScript
  2. mouseover { font-style: italic; }
  3. a:hover { font-style:italic; }
  4. a { font-style: italic; }
  
  Ans: 3



### CSS best practices

You will find below an excerpt of CSS best practices (see the [full slide set](http://fantasai.inkedblade.net/style/talks/best-practices/#title)) that were written by  Elika J. Etemad (also known as [fantasai](http://fantasai.inkedblade.net/)). Elika is an expert on the [W3C CSS Working Group](http://www.w3.org/Style/CSS/) (since 2004!) and a longtime contributor to the Mozilla Project. In addition to editing many of the CSS3 specifications, she’s worked on layout engine testing and development for Gecko and managing the CSS test suites at W3C.


#### Executive summary

+ __Logical source order__:

  The order of the HTML content should make sense even without the CSS: for accessibility, mobile optimization, device adaptability, and long-term maintainability.
+ __Liquid layouts and relativity__:
  
  Use smart relative sizing: to optimize layouts while minimizing media query code forks.
+ __Media queries__:
  
  Adapt to screen size changes; get font size adaptation free by using ems.
+ __Prevent zombie code__:
  Dead code may come alive as CSS changes. Delete it before it does, and ruins your layout.

+ __Test in multiple browsers__:
  
  Your favorite browser is not always right.
+ __Don't use proprietary features!__

  Keep the Web open to everyone! Don't rely on the latest -WebKit- invention.
+ __Turn off CSS__:

  A well-coded page will be understandable without it.


#### Foundations

+ Indent your code for readability ease
+ Learn how to code CSS before relying on frameworks (such as Bootstrap, etc.)
+ __Separate content and style__
  + Use semantic markup, ie., "classes for meaning, not for show".<br/>
    The following article is helpful to understand this concept: [Meaningful CSS: Style Like You Mean It](http://alistapart.com/article/meaningful-css-style-like-you-mean-it) (Tim Baxter, May 2016 - A list apart).
  + Use `<table>` for tabular data: don't use tables for layout, but if your content is tabular like a catalog, a calendar, or a price list, then the table element is the correct markup.
+ __Linearized logical source order__<br/>
  The order of the HTML content should make sense even without the CSS.<br/>
  Benefits are numerous as it works best:
  + for long-term site maintainability
  + for mobile
  + for accessibility
  + as a foundation for device adaptation (media queries)
+ __Linguistic variations__: set the language correctly for better typography (see the section entitled "[why Internationalization is important](https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+3T2017/courseware/8f5154ed51d0431ea5473cf0f8c287b3/8d4931e47ad24c74aac87e773cea2497/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B3T2017%2Btype%40vertical%2Bblock%40ee99c75e1e9f42d4958ee79add48b2ee")


#### Testing

+ __Test without CSS__: turn off CSS, and if the page makes no sense, fix your markup.
+ __Test in multiple environments__:
  + Resize the window
  + Zoom the text
  + Try a mobile browser
  + Navigate by keyboard
+ __Test in multiple browsers__: remember that just testing in Chrome does not work for everyone!  ;)


#### Adaptability

+ __Media queries__: set media query breakpoints in em or ch, not always in px.
+ __Liquid layouts and relativity__: what is your sizing based on?
  + Containing block size? → Use percents.
  + Viewport size? → Use viewport units: `vw`, `vh`, `vmin`, `vmax`
  + Font height? → Use `em` or `rem`.
  + Font pitch? → Use `em` or `ch`.
  + Content size? → Use `auto` or `min-content`/`max-content`.
  + Combination of the above? → Use the appropriate layout formulas: `flex`, `min-width`, `max-width`, etc.

Absolute units are usually the wrong answer.


#### Defensive Coding

+ `!important` means never override- to use with caution
  + Use `!important` to define overriding rules, not for fixups
  + Duplicate selectors if you need to increase specificity, or
  + Simplify selectors if you need to decrease specificity
+ __Don't over-escalate__: understand your code, and don't overkill.

<p style="margin-left:1.5em;"><em>For example, avoid:<br></em><code>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; . z-index: 9999999999999999999999999999999999999;<br> &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; . position: absolute; left: -10000000000px<br> </code></p>

+ __Drop dead code__: you tried something and it didn't work? Delete it right away!
+ Code to Standard
+ Don't rely on proprietary extensions
+ Don't use experimental features in production or commit to keeping up-to-date.
+ Provide fallbacks / use `@supports`.



### Recipe project - Module 5

Let's up some of our code, as well as improve the look and feel of our Web page! Try moving all of your CSS code to a separate file (don't forget to link to it).

We're also going to make the nav element move out of the way when we're not using it, so that it only slides out when we're hovering on it.

Finally, we'll convert the Ingredients list to a table with ingredients and amounts.

Give it a try, and when you're done (or if you get stuck), watch the video below to see what we did.

[Sample code](src/5.5.7-Recipe.html)


### Vido: Recipe project - Module 5




## 5.6 Exercises - Module 5

### Tables exercises (1-12)




### Multimedia exercises (13-20)




### CSS exercises (21-25)




