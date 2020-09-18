# Week 1: HTML5 Basics

## 1.4 Other elements and attributes


### 1.4.0 Lecture Notes

+ Foldable zone in an HTML document
  + `<details>` element:
    + generate a simple widget to show/hide element contents
    + able to be embedded inside one another
  + `<summary>` element: (optional) children element of `<details>` element
  + `<summary>...</summary>` located inside a `<details>...</details>` element

+ Styling summary icons w/ CSS
  + modifying color and background of the icon w/ `::-webkit-details-marker`

    ```css
    summary::-webkit-details-marker {
      color:#FF0000;
      background:#FFFFFF;
    }
    ```

  + `details[open]` selector handling the unfolded `<details>`

    ```css
    details[open] summary::-webkit-details-marker {
      color:#0000FF;
      background:#00FFFF;
    }
    ```

  + using `+` shaped icon for expansion

    ```css
    summary:after {
      content: "+";
      color: #FF00FF;
      float: left;
      font-size: 1.5em;
      font-weight: bold;
      margin: -5px 5px 0 0;
      padding: 0;
      text-align: center;
      width: 20px;
    }
    ```

  + using `-` shaped icon to callops details

    ```css
    details[open] summary:after {
      content: "-";
      color: #FFFFFF
    }
    ```

+ The `<time>` element
  + useful for marking a time or a duration in a document
  + expression
    + human readable part (the part between `<time>` and `</time>`)
    + machine readable part contained within a `datetime` attribute
    + date: expressed as `YYYY-MM-DD`
  + machine readable used by 
    + search engines for indexing
    + browsers or browser extensions
    + JavaScript code
  + useful scenarios
    + generating alerts for birthdays
    + automatically adding dates or events that contain `<time>` elements in a calendar

+ The `datetime` attribute
  + used for indicating a date/time or a duration
  + Different syntaxes of the datetime attribute

    <table style="text-rendering: optimizelegibility; border-spacing: 0px; margin: 20px 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'PT Sans', Arial, Helvetica, sans-serif; font-size: 13px; font-stretch: inherit; line-height: 25px; vertical-align: baseline; width: 814px; max-width: 100%; margin: auto;" cellpadding="10" border="1">
    <caption style="font-size: 1.2em;">Different syntaxes of the <span style="font-family: 'courier new', courier;">datetime attribute</caption>
    <tbody>
    <tr><th scope="”row”">datetime attribute values</th><th scope="”row”">Interpretation</th></tr>
    </tbody>
    <tbody style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The year 2020</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 2020</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="11-13"&gt;&nbsp;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 13th (any year)</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-W21"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Week 21 from year 2020</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11-13 09:00"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 13th year 2020, time = 9:00</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11-13<span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; color: #ff0000;">T09:00"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Same as previous example, both syntaxes are supported, with and without the "T" between date and time.</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00Z"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00-05"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT minus 5 hours</td>
    </tr>
    <tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00+05:45"&gt;</td>
    <td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT plus 5 hours 45 minutes, (for example, Nepal&nbsp;is 5:45 ahead of&nbsp; GMT)</td>
    </tr>
    </tbody>
    </table>

  + duration values
    + format: `<time datetime="P4D">` = `<time datetime="P 4 D">`
      + prefix “P” for “period”
      + a duration value that ends with another letter indicating the unit used
      + unit
        + "D" for "days"
        + “H” for hours
        + “M” for minutes
        + “S” for seconds
    + “T” after the “P” marker indicating a more accurate duration time, e.g., `<time datetime="PT4H 6M 12.55S">` a duration of 4 hours, 6 minutes and 12.55 seconds
    + the <time> element with no attributes
      + the value between the opening `<time>` and closing `</time>` should follow the syntax given by the specification
      + recommended to use a `datetime` attribute

+ The `<mark>` element
  + used for indicating text as marked or highlighted for reference purposes
  + useful cases
    + search results with search strings highlighted
    + highlight important parts of a text
    + replacing `<strong>` and `<em>` with `<mark>` when suitable
  + change default style: using `background-color` and `color`

+ The `download` attribute
  + download resources rather than navigating to them
  + example

    <div class="source-code"><ol class="linenums">
    <li style="margin-bottom: 0px;">&lt;a</span> </span>href</span>=</span>"normal.gif"</span></span> </span><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">download</span>=</span>"MichelBuffa.gif"</span></span></span>&gt;</span></li>
    <li style="margin-bottom: 0px;">&nbsp; &nbsp; download a picture of Michel Buffa</span></li>
    <li style="margin-bottom: 0px;">&lt;/a&gt;</span></li>
    </ol></div>
  
    + force the download of an image with a filename different from its original filename on the server side
    + original image" "normal.gif"
    + downloaded file: "MichelBuffa.gif"
  + security: the image should be located on the same domain as the HTML page that contains the link

+ The HTML5 `translate` attribute
  + used to limit the impact of translation tools
  + useful scenarios
    + source code
    + video game Web sites proposing cheat codes
    + street names, author names, etc.
  + Google translate and Microsoft online translation services: able to prevent translation of content by themselves
  + providing a standard approach
  + enumerated attribute
    + used to specify whether an element's attribute values and the values of its Text node children to be translated when the page is localized, or whether to leave them unchanged
    + default: "no"
    + e.g., `<span translate="no" class="author">Michel Ham</span>`


### 1.4.1 The `<details>` and `<summary>` elements

These elements have been introduced for displaying a foldable zone in an HTML document.

In the screenshot below, taken from the W3C specification page, the text next to the horizontal arrow is a `<summary>` element, and the text displayed when we click on the summary part, is the `<details>` element. This is a sort of "accordion" with foldable content.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y43kqw9a"
    alt    ="Example of summary details elements from the W3C specification"
  />
  <figcaption> Example of summary details elements from the W3C specification </figcaption>
</figure>


The `<details>` element generates a simple widget to show/hide element contents, optionally by clicking on its child `<summary>` element.

Here is an example of what can be done using these elements ) see the [online version on JSBin](https://jsbin.com/yociyel/1/edit?html,css,js,output) or [local version](src/1.4.1-foldable.html):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y5m3tfwu"
    alt    ="Example of folded summary details"
  />
  <figcaption> Example of folded summary details </figcaption>
</figure>


And here is what is displayed after clicking on the small arrow-shaped icon to the left of the summary:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y39xph3f"
    alt    ="Example of summary details unfolded"
  />
  <figcaption> Example of summary details unfolded </figcaption>
</figure>


Here is the code of this example:

```html
<!DOCTYPE html>
<html lang="en"> ...
<body>
<details>
<summary>
```

How to beat the boss...spoiler alert !

```html
</summary>
<p> Just aim to the red spots near his eyes</p>
<p>Keep shooting at these spots until the eyes open, then hit quickly both eyes with your laser beam.</p>
</details>
</body>
</html>
```

The `<summary>...</summary>` is inside a `<details>...</details>` element. By clicking on the icon at the left of the summary, the content of the `<details>` value is displayed/hidden.

`<details>` blocks can be embedded inside one another, like in this [example](https://tinyurl.com/yxfd49zd) ([local example](src/1.4.1-foldable2.html)):

Step 1: all folded:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y466jecb"
    alt    ="Other example, unfolded"
  />
  <figcaption> Other example, unfolded </figcaption>
</figure>


Step 2: click on top level summary icon, the first "hidden" part appears...

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/yxfph294"
    alt    ="The unfolded content contains in turn a summary details folded"
  />
  <figcaption> The unfolded content contains in turn a summary details folded </figcaption>
</figure>

Step3: click on embedded summary icon inside the part that has been previously unfolded

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y6m5hp3q"
    alt    ="We unfolded the summary details inside the previous summary details. Recursive accordeons!"
  />
  <figcaption> We unfolded the summary details inside the previous summary details. Recursive accordeons! </figcaption>
</figure>


Source code of this example, see the summary/details inside another one:

```html
<details>
<summary>
  How to beat the boss...spoiler alert !
</summary>
  <p> Just aim to the red spots near his eyes</p>
  <p>Keep shooting at these spots until the eyes open, then hit quickly both 
    eyes with your laser beam.</p>
<details>
<summary>
  Bonus and spoiler No 2: get a new weapon by cutting the tail of the boss.
</summary>
  <p>Before finishing him, try to cut his trail, you will get a new weapon</p>
  <p>Just try to stay behind him as long as you can, hitting his tail with 
    your melee weapon, after a few hits the trail will fall and you will get 
    a new bonus weapon, then finish the boss.</p>
</details>
</details>
```


#### CSS pseudo classes for styling summary icons

There are CSS pseudo classes to style this icon when it is in the open or closed state. Support for these is still incomplete as of June 2020 (works on Google Chrome, Opera, Safari, not in FF).

Example 1 (see [online example](https://tinyurl.com/y3urv4kl) or [local example](src/1.4.1-example1.html)):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y3uydq7o"
    alt    ="Styling the open/close icon"
  />
  <figcaption> Styling the open/close icon </figcaption>
</figure>


The color and background of the icon on the left are specified by the following CSS rule, which uses the pseudo class `::-webkit-details-marker`

In this example: red arrow, white background.

```css
summary::-webkit-details-marker {
  color:#FF0000;
  background:#FFFFFF;
}
```

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2g33b8t')"
    src    ="https://tinyurl.com/y2mpn9ov"
    alt    ="Styled summary details icon, unfolded state"
  />
  <figcaption> Styled summary details icon, unfolded state </figcaption>
</figure>


Once opened, the selector `details[open]` can style the icon when `<details>` is unfolded. In this example: blue arrow, turquoise background. Here is the corresponding CSS rule:

```css
details[open] summary::-webkit-details-marker {
  color:#0000FF;
  background:#00FFFF;
}
```

It is also possible to change the icon itself using the CSS pseudo class `:after`

Example 2 (see it [online](https://jsbin.com/sajusop/edit?html,css,output) or [local example](src/1.4.1-example2.html)):

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2g33b8t" ismap target="_blank">
    <img style="margin: 0.1em;" width=250
      src  ="https://tinyurl.com/y466jecb" 
      alt  ="A + as a custom open icon for summary" 
      title="A + as a custom open icon for summary"
    >
    <img style="margin: 0.1em;" width=250
      src  ="https://tinyurl.com/y6blnkz5" 
      alt  ="A '-' as a custom close icon" 
      title="A '-' as a custom close icon"
    >
  </a>
</div>


CSS rules used in this example:

Use a "+" shaped icon, pink, bold, etc... :

```css
summary:after {
  content: "+";
  color: #FF00FF;
  float: left;
  font-size: 1.5em;
  font-weight: bold;
  margin: -5px 5px 0 0;
  padding: 0;
  text-align: center;
  width: 20px;
}
```

Use a "-" shaped icon, white, when details are displayed:

```css
details[open] summary:after {
  content: "-";
  color: #FFFFFF
}
```


#### Current browser support

+ On CanIUse: [compatibility table for details and summary elements](https://tinyurl.com/yy6tdwf8)


#### Knowledge check 1.4.1

1. Select the good way to define the widget:

  a.  
    ```html
    <summary>
    <details>
    How to beat the boss
    </detaill>
    </summary>
    ```

  b.  
    ```html
    <summary>
    How to beat the boss
    </summary>
    <details>
    <p> Just aim to the red spots near his eyes </p>
    </details>
    ```

  c.  
    ```html
    <details>
    <summary>
    How to beat the boss
    </summary>
    <p> Just aim to the red spots near his eyes </p>
    </details>
    ```
  
  Ans: c<br/>
  Explanation: The right answer is the third one. `<details>` contains one `<summary>`, and eventually other details/summary pairs.


### 1.4.2 The `<time>` and `<mark>` elements


#### The `<time>` element

The `<time>` element is useful for marking a time or a duration in a document.

It provides both a human readable part (the part between `<time>` and `</time>`) and a machine readable part contained within a datetime attribute. Dates are expressed as `YYYY-MM-DD`.

The machine readable part adds semantics that can be used by search engines for indexing, by browsers or by browser extensions, or by JavaScript code. Useful scenarios include generating alerts for birthdays, automatically adding dates or events that contain `<time>` elements in a calendar, etc.

Example:

```shell
We open at <time>10:00</time> every morning.

I have a meeting the <time datetime="2020-02-14">Monday 14/02/2020.</time>.
Blog posts from the year <time datetime="2020">2020</time>.
Archives, blog posts for <time datetime="2020-04">April 2020</time>
This recipe was published by Michel the <time datetime="2020-04-16">April 16, 2020</time>.
```

#### The `datetime` attribute

The `datetime` attribute can be used for indicating a date/time or a duration.

__Date/time values__

Supports different specifications of time such as "a year", "a month in a year", "a week in a year", "a time", etc... 

Here are some examples:


<table style="text-rendering: optimizelegibility; border-spacing: 0px; margin: 20px 0px; padding: 0px; border: 0px; outline: 0px; font-family: 'PT Sans', Arial, Helvetica, sans-serif; font-size: 13px; font-stretch: inherit; line-height: 25px; vertical-align: baseline; width: 814px; max-width: 100%; margin: auto;" cellpadding="10" border="1">
<caption style="font-size: 1.2em;">Different syntaxes of the <span style="font-family: 'courier new', courier;">datetime attribute</span></caption>
<tbody>
<tr><th scope="”row”">datetime attribute values</th><th scope="”row”">Interpretation</th></tr>
</tbody>
<tbody style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">The year 2020</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 2020</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="11-13"&gt;&nbsp;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 13th (any year)</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-W21"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Week 21 from year 2020</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11-13 09:00"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">November 13th year 2020, time = 9:00</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="2020-11-13<span style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline; color: #ff0000;">T09:00"&gt;</span></td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">Same as previous example, both syntaxes are supported, with and without the "T" between date and time.</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00Z"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00-05"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT minus 5 hours</td>
</tr>
<tr style="text-rendering: optimizelegibility; margin: 0px; padding: 0px; border: 0px; outline: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">&lt;time datetime="09:00+05:45"&gt;</td>
<td style="text-rendering: optimizelegibility; border-color: #cbcbcb; outline: 0px; font-family: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: 1.4em; vertical-align: baseline;">9:00 in the morning, GMT plus 5 hours 45 minutes, (for example, Nepal&nbsp;is 5:45 ahead of&nbsp; GMT)</td>
</tr>
</tbody>
</table>


__Duration values__

Duration values use the prefix “P” for “period” as in `<time datetime="P4D">` (period = four days)...

So you start the attribute string value with a "P", followed by a duration value that ends with another letter indicating the unit used: "D" for "days",  “H” for hours, “M” for minutes and “S” for seconds. 

You can separate the different elements "P", value and unit with spaces, but this is optional. So `<time datetime="P4D">` is a duration of 4 days, as is `<time datetime="P 4 D">`.

Using a “T” after the “P” marker allows you to indicate a more accurate duration time: `<time datetime="PT4H 6M 12.55S">` is a duration of 4 hours, 6 minutes and 12.55 seconds.

Alternatively, you could use also a duration time component.

From Bruce Lawson's article : _"Whichever you choose, it’s represented internally as a number of seconds. Because of this, you can’t specify a duration in terms of months, because a month isn’t a precise number of seconds; a month can last from 28 to 31 days. Similarly, a year isn’t a precise number of seconds; it’s 12 months and February sometimes has an extra day._

_You still can’t represent dates before the Christian era, as years can’t be negative. Neither can you indicate date ranges. To mark up From “21/02/2012 to 25/02/2012″, use two separate `<time>` elements."_

Examples:

```html
<h2>Recipe:</h2>
<ul>
  <li> Preparation time: <time datetime="PT30M">30 minutes</time> </li>
  <li> Cooking time:     <time datetime="PT10M">10 minutes</time> </li>
</ul>
```

__The `<time>` element with no attributes__

Used without attributes, the value between the opening `<time>` and closing `</time>` should follow the syntax given by the specification so that machines can understand it (same syntax as the one presented for the datetime attribute in the previous section). However it is recommended to use a datetime attribute, as it gives more freedom in the way you can display the date/time/duration in a human-readable form. 

__External resources:__

+ From the [specification](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-time-element)
+ On [MDN's Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
  + MDN's browser compatibility [table](https://tinyurl.com/y4vc44nq) for `<time>`
+ Old but interesting [article](https://www.brucelawson.co.uk/2012/best-of-time/) by Bruce Lawson
+ A CSS Tricks' article: "[The 'time' element](https://tinyurl.com/y2wpzh64)"


#### The `<mark>` element

The HTML `<mark>` tag is used for indicating text as marked or highlighted for reference purposes, due to its relevance in another context.

Some use cases:

+ Display search results with search strings highlighted in the results.
+ &gt; Highlight important parts of a text, such as "quoting parts", etc.
+ Replace `<strong>` and `<em>` with `<mark>` when suitable.

Example 1: [jsBin online example](https://jsbin.com/tafelic/edit?html,output) and [local example](src/1.4.2-mark.html)

Source code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset=utf-8 />
<title>JS Bin</title>
</head>
<body>
  <p>Project is due in <mark>.zip format</mark> next monday.</p>
</body>
</html>
```

Example 2:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yy4j8cp3')"
    src    ="https://tinyurl.com/y4bdq5jq"
    alt    ="Another example for marking code"
    title  ="Another example for marking code"
  />
</figure>


Source code:

```html
<body>
<pre>
<code><mark>var</mark> i = 3;</code>
</pre>
<p>The var keyword is used to declare a variable in JavaScript.</p>
</body>
```

__Change the default style of the `<mark>` element__

If you don't like the default yellow background, you may use CSS to change the style of the `<mark>` element:

For example:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yy4j8cp3')"
    src    ="https://tinyurl.com/y6cmeaog"
    alt    ="style the mark element with CSS"
    title  ="style the mark element with CSS"
  />
</figure>


... comes with this CSS rule:

```css
mark {
    background-color: green;
    color: yellow;
}
```

__External resources:__

+ From the [specification](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-mark-element)
+ On [MDN's Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
  + MDN's browser compatibility [table](https://tinyurl.com/yydyaomy) for `<time>`
+ An article on Web Platform News: "[The `<mark>` element could help make your text more scannable](https://tinyurl.com/y3awtyhc)"


#### Knowledge check 1.4.3 

1. When would you use the mark element?<br/>
  a. To download a file<br/>
  b. To highlight a text<br/>
  c. To add a link<br/>
  d. To make a text bigger<br/>

  Ans: b


### 1.4.3 The download and translate attributes

Everyone knows the classic way to make hyperlinks, using `<a href="...">some text</a>`. What happens when you click on the hyperlink depends on the MIME type received by the browser. If you link to a file the browser knows how to render (an html page, a gif, jpg, or png image, etc.) there is a good chance that the MIME type received by the browser will be something like this:

<div><ol>
<li style="margin-bottom: 0px;" value="1">Content-type: text/html, text/plain, image/gif, image/jpg, etc.</li>
</ol></div>

For example,  HTML code such as this:

<div><ol>
<li style="margin-bottom: 0px;" value="1">&lt;a href="toto.jpg"&gt;</li>
<li style="margin-bottom: 0px;" value="2">&nbsp; &nbsp; please right click this link to download </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; the toto.jpg picture&lt;/a&gt;</li>
</ol></div>

...will ask the remote HTTP server to send back the `toto.jpg` file. The browser will receive in the response HTTP header from the server (and by default the browser will display the image in a new tab):

<div><ol>
<li style="margin-bottom: 0px;" value="1">...</li>
<li style="margin-bottom: 0px;"> Content-type: image/jpg</li>
<li style="margin-bottom: 0px;">...</li>
</ol></div>

However, if the link points to some PHP code, Java servlet code, or any kind of script/application on the server side, this remote server code can send in its HTTP response a `Content-type` that may force the browser to download the image instead of rendering it.

It may also propose a name for the file to be downloaded that may be different from the one that appears in the URL of the `href` attribute. This can be done by generating, in addition to the Content-type line in the response HTTP header, a `Content-Disposition` line that looks like this:

<div><ol>
<li style="margin-bottom: 0px;" value="1">Content-Disposition: attachment; filename="<span style="color:green;">MyImage.png</span>";</li>
</ol></div>

Here are some extracts from a Java Servlet that generate a zip file and forces the browser to propose downloading it using a specified name:

<div><ol>
<li style="margin-bottom: 0px;" value="1">protected void doGet(HttpServletRequest request, HttpServletResponse response) </li>
<li style="margin-bottom: 0px;"> throws ServletException, IOException { </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp;try {</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp;// Build the zip file</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;String path = getServletContext().getRealPath("data");</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;File directory = new File(path); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;String[] files = directory.list(); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;if (files != null &amp;&amp; files.length &gt; 0) { </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;byte[] zip = zipFiles(directory, files); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ServletOutputStream sos = response.getOutputStream(); </li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// generate a HTTP response that forces the download</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">response<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">.setContentType("application/zip"); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">response<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">.setHeader("Content-Disposition", </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">"attachment; filename=\"DATA.ZIP\""); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;sos.write(zip); sos.flush(); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;} </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp;&nbsp;} catch (Exception e) { </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;e.printStackTrace(); </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp;&nbsp;} </li>
<li style="margin-bottom: 0px;"> }</li>
</ol></div>

The above example will cause the browser that invoked this server-side code to start the download of a file named "DATA.ZIP".


#### To download a file using an arbitrary name: the download attribute

HTML5 proposes the use of a new attribute named `download` to download resources rather than navigating to them. The example below shows how to trigger the download of an image by the browser (instead of rendering it, which is the default behavior) with a name different from the name of the resource.

<div><ol>
<li style="margin-bottom: 0px;">&lt;a href="normal.gif" <span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">download="MichelBuffa.gif"&gt;</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; download a picture of Michel Buffa</li>
<li style="margin-bottom: 0px;">&lt;/a&gt;</li>
</ol></div>

This will indeed force the download of an image with a filename different from its original filename on the server side. Here is a screen capture of the Web browser while downloading the picture. We can see in the status bar the name of the link (the image is "`normal.gif`") and the downloaded file is "`MichelBuffa.gif`":

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y6rsz7qo')"
    src    ="https://tinyurl.com/y5nv7ert"
    alt    ="Image saved with another names thanks to the download attribute"
    title  ="Image saved with another names thanks to the download attribute"
  />
</figure>

<p style="border: 1px solid red; magin: 20px; padding: 20px; text-align: center;"><mark style="color:red;">WARNING</mark>: since 2015, and for security reasons, <strong>the image should be located on the same domain as the HTML page that contains the link</strong> (using a relative URL works well, for example, but linking a page on another domain will not work -&nbsp;it will keep its original name).</p>

__Interesting applications: serverless download__

Serverless download demo (by E.Bilderman)

This demo shows the use of the `download` attribute together with the HTML5 File, FileSystem and FileWriter APIs (to be studied later in this course) for generating on-the-fly content from JavaScript code, and proposing downloading it to a file.  

We won't detail this demo here, but take a look if you are curious to see what can be done with this new download attribute. As the FileWriter and FileSystem APIs are still supported only by Google Chrome (other browsers need polyfills), you will need Google Chrome to try it.

We have also put the simplified [source code of this demo on JSBin.com](https://jsbin.com/muluwey/1/edit?html,css,js,output) ([local demo](src/1.4.3-serverless.html)) for you to play with. See also the [original demo by E. Bilderman](https://tinyurl.com/y5x2avow).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y6rsz7qo')"
    src    ="https://tinyurl.com/y3t5k7pf"
    alt    ="Serverless download demo: type text in a text area, press download, enter a filename and voilà! you can download the textarea content into a file, without any server."
    title  ="Serverless download demo: type text in a text area, press download, enter a filename and voilà! you can download the textarea content into a file, without any server."
  />
</figure>


__External resources:__

+ From the specification: [downloading resources](https://tinyurl.com/y6ouvh6m)
+ From CanIUse: the [browser support of the `download` attribute](https://tinyurl.com/ybqjemqh)


#### The HTML5 translate attribute

HTML5 gives us a new `translate` attribute. This attribute is used to limit the impact of  translation tools such as [Google Translate](https://translate.google.com/) by prohibiting the translation of certain content. In many cases some parts of a document should not be translated.

Use cases include:

+ HTML pages that contain source code: you would certainly not like to see the Java or PHP or whatever programming language parts of your page translated into another spoken language!
+ Video game Web sites that propose cheat codes; the codes do not have to be translated,
+ Street names, author names in an "about" page must not be translated,
+ etc.

Both [Google translate](https://translate.google.com/) and [Microsoft online translation services](https://www.microsofttranslator.com/) already offer the ability to prevent translation of content by adding markup to your content, although they do it in (multiple) different ways. Hopefully, the new attribute will help significantly by providing a standard approach.


__Principle: give hints to translating tools__

[The specification about the translate attribute](https://tinyurl.com/y2hlgqyl) tells us that  "The translate attribute is an enumerated attribute that is used to specify whether an element's attribute values and the values of its Text node children are to be translated when the page is localized, or whether to leave them unchanged.

_The attribute's keywords are the empty string, yes, and no. The empty string and the yes keyword map to the yes state. The no keyword maps to the no state. In addition, there is a third state, the inherit state, which is the missing value default (and the invalid value default)."_


__Example illustrating how to specify parts of an HTML element that should not be translated:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;span</span><span class="pln"> </span><strong><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">translate</span><span class="pun">=</span><span class="atv">"no"</span></span></span></strong><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"author"</span><span class="tag">&gt;</span><span style="text-decoration: underline;"><span class="pln" style="color: #ff0000; text-decoration: underline;">Michel Ham</span></span><span class="tag">&lt;/span&gt;</span></li>
</ol></div>

In the above example, a `<span>` element defines an author (of a blog, for example) who is named Michel Ham. However, his family name is the same as pork and would be translated to "Michel Jambon" in French, or Michel Jamón in Spanish...

Using the translate="no" attribute should prevent this behavior...

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;span</span><span class="pln"> </span><strong><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;"><span class="atn">translate</span><span class="pun">=</span><span class="atv">"no"</span></span></span></strong><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"author"</span><span class="tag">&gt;</span><span style="text-decoration: underline;"><span class="pln" style="color: #ff0000; text-decoration: underline;">Michel Ham</span></span><span class="tag">&lt;/span&gt;</span><span class="pln"> is a professor </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> from the University of Nice,France. </span></li>
</ol></div>

Will be correctly translated into French by:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="str">"<span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">Michel Ham</span></span> est un professeur de l'Université de Nice, France."</span></li>
</ol></div>

...where all of the end of the sentence has been translated except the author's name.


__Inheritance between elements__

When you define an element as not being translatable, its children inherit this behavior and are themselves not translatable. The reverse is also true. 

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;p</span><span class="pln"> </span><strong><span style="text-decoration: underline;"><span style="color: lightblue; text-decoration: underline;"><span class="atn">translate</span><span class="pun">=</span><span class="atv">"no"</span></span></span></strong><span class="tag">&gt;</span><span class="pln">This is a text in a paragraph element, that should not be translated: the p element has a translate="no" attribute.</span><span style="text-decoration: underline;"><span style="color: lightblue; text-decoration: underline;"><span class="tag">&lt;span&gt;</span><span class="pln"> This part that is in a span element embedded within the paragraph. It does not have a translate attribute but inherits the translation-mode of the p and will not be translated too</span><span class="tag">&lt;/span&gt;</span></span></span><span class="pln">. This is the end of the paragraph...&lt;/ p&gt;</span></li>
</ol></div>


#### External resources:

+ From the specification: [the translate attribute](https://tinyurl.com/yyzqajeg)
+ From [MDN's Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/translate)
  + Its corresponding [browser compatibility table](https://tinyurl.com/yxsvwpum)
+ An article from W3C's Internationalization Activity: ["Using HTML's translate attribute"](https://tinyurl.com/yy5pjwtp)


#### Knowledge check 1.4.4

<div class="source-code">
      <ol class="linenums">
        <li style="margin-bottom:0px;" class="L0" value="1">
          <span class="tag">&lt;a</span> <span class="pln"> </span> <span class="atn">href</span> <span class="pun">=</span> <span class="atv">"/images/batman_robin_car_superpower_007.rar"</span>
        </li>
        <li style="margin-bottom:0px;" class="L1">
          <span class="pln">    </span> <span class="atn">download</span> <span class="pun">=</span> <span class="atv">"Batmobile.rar"</span> <span class="tag">&gt;</span>
        </li>
        <li style="margin-bottom:0px;" class="L2">
          <span class="pln">    download a picture of Michel Buffa</span>
        </li>
        <li style="margin-bottom:0px;" class="L3">
          <span class="tag">&lt;/a&gt;</span>
        </li>
      </ol>
  </div>

1. What will be the name of the downloaded file?<br/>
  a. Batmobile.rar<br/>
  b. batman_robin_car_superpower_007.rar<br/>
  
  Ans: a







