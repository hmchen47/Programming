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



### Styling your table (continued)




### Create a table




### Activities - Tables




## 5.3 Multimedia

### Audio element




### Video element




### Video - Source/Track elements




### Audio and video elements




### Activities - Multimedia




## 5.4 Embedding content

### The iframes tag




### The ismap and usemap attributes




### Activities - Embedding content




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




