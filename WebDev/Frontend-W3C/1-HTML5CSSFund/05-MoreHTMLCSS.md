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
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Attributes for &lt;th&gt;</td>
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
    <td style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Attributes for &lt;td&gt;</td>
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




### Styling your table




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




