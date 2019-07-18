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

Please post your observations and findings in the discussion below.




## 5.5 CSS tricks

### Decorative images and backgrounds




### Decorative borders and shadows




### Managing element size




### Knowledge checks




### Pseudo classes and cursor




### CSS best practices




### Recipe project - Module 5




### Recipe project - Module 5




## 5.6 Exercises - Module 5

### Tables exercises (1-12)




### Multimedia exercises (13-20)




### CSS exercises (21-25)




