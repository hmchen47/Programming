# HTML5 - Tags


## Definition and Characteristics of Tags

+ The annotations with "<" amd ">" separated from the regular text

+ Use to organize a text file (which is just a long string of characters) such that it represents a tree of elements that make up the html document

+ The bits of text you use to tell the computer where an element begins and ends

+ HTML can indicate the beginning and end of a tag, i.e. the presence of '<' tells the browser 'this next bit is markup, pay attention'.

+ To stop using that tag and do something else, so '<' and '>' are again used by adding a '/' right after the '<' to indicated that it's a 'close tag'.

+ "self closing" tags: an element completely described by its attributes, and thus no need for other content

+ [Semantic vs Style tags](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#separating-content-style)
  + Style tags
    + focused purely on presentation and design in HTMl4
    + how the text should look like on the screen in HTMl4
    + not produce appropriate styling for some parts of the world, e.g., Chinese characters using underlining than bold
    + HTML5: recommend to use class attributes to identify the semantic intention of the markup; important for pages that get translated
    + Bold:
      + a style that makes letters thicker so it stands out among other text but it has no semantic meaning
      + for example for voice browsers, screen readers, and other types of ways to access the Web
      + HTML5: used as a stylistic offset such as keywords in a document, product names or action words without making them as important
    + Italic:
      + slants text
      + usually italicize names of magazine, books, TV shows etc.
      + purely for presentation purposes
      + HTML5: used for text in a different mood or voice, such as foreign words, a thought or technical terms
  + Semantic tags
    + referred to the meaning of words in a language in HTMl4
    + something about the semantic of the tag, meaning in HTMl4
    + netstable
    + E.g., `<em>`, `<strong>`
    + Strong:
      + an indication of how something should be
      + like bold in a browser, but mean 'speak with urgency or seriousness' when reading text aloud
      + represent importance, seriousness, or urgency for its content
    + Emphasis
      + used to stress emphasis of its contents
      + emphasizing word in a sentence able to change the whole meaning
      + HTML5: used for words and sentences you would pronounce differently
      + HTML5: not used to convey importance
  + Ref: [Using `<b>` and `<i>` elements](https://www.w3.org/International/questions/qa-b-and-i-tags)


<div style="display:flex;justify-content:center;align-items:center;flex-flow:row wrap;">
  <div><a href="https://courses.edx.org/courses/course-v1:W3Cx+HTML5.0x+1T2019/courseware/633117d2ef0f4bb59cda68d966b6d288/f36ef1f210bf460e9e0f43be78fb0bd5/1?activate_block_id=block-v1%3AW3Cx%2BHTML5.0x%2B1T2019%2Btype%40vertical%2Bblock%40427074c031424e189e4898d969d7dcd9">
    <img src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9df11f203d18addb831da2f379cb49a5/asset-v1:W3Cx+HTML5.0x+1T2019+type@asset+block/tags.png" style="margin: 0.1em;" alt="Diagram of an element" title="Diagram of an element" width="250">
  </a></div>
</div>


## Comment Tags

+ Inline: `<!-- This is a comment -->`

+ Multiple lines:

  ```html
  <!--
  Beginning of comment
  ... 
  End of comment
  -->
  ```

+ Comments cannot be nested


## List of Typical Tags

<table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
<thead>
  <tr style="border-bottom: double black;">
    <th style="background-color: #3d64ff; color: #ffffff; width: 10%">Tag</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 70%">Description</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 15%">Link</th>
  </tr>
</thead>
<tbody>
  <tr><td>&lt;!DOCTYPE html&gt;</td>
    <td> declaration "This is an HTML5 file, in case you were wondering"</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#all-together-now">DOC18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">DOC19</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">Tags18</a></td></tr>
  <tr><td> &lt;html&gt;</td>
    <td> where the actual HTML code begins and end</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#all-together-now">All18</a>, <a href="/WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">HTML19</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">Tags18</a></td></tr>
  <tr><td> &lt;meta&gt;</td>
    <td> metadata content; represent metadata that cannot be represented by other HTML meta-related elements</td>
    <td><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#the-meta-tag">Meta</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta">MDN</a></td></tr>
  <tr><td> &lt;head&gt;</td>
    <td> where the browser can find style tips, and what the title of the page is</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#everything-in-html">HEAD18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">HEAD19</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">Tags18</a></td></tr>
  <tr><td> &lt;body&gt;</td>
    <td> contains all of the content of your page, essentially what the user sees</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#15-best-practices">Body18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">Body19</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">Tags18</a></td></tr>
  <tr><td> &lt;h1&gt; ~ &lt;h6&gt;</td>
    <td> a whole collection of heading tags</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">Heading18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">Heading19</a></td></tr>
  <tr><td> &lt;p&gt;</td>
    <td> paragraph; text wrapped in may be indented or have extra vertical white space before starting; typically be a new line</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#tags-we-have-already-used">P18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#tags-we-have-already-used">P19</a></td></tr>
  <tr><td> &lt;q&gt;</td>
    <td> quotes; used when you want to quote a person or written work in your Web page; customarily displayed using quotation marks, again unrelated to strings</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">Quote18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">Quote19</a></td></tr>
  <tr><td> &lt;blockquote&gt;</td>
    <td> quote a larger passage; typically set the quoted text apart from the surrounding text and indent it, to make clear that it is quoted text</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">BlkQuote18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">BlkQuote19</a></td></tr>
  <tr><td> &lt;ul&gt;, &lt;ol&gt;</td>
    <td> indicate a list of things; &lt;ol&gt;: "ordered" list; &lt;ul&gt;: "unordered" list</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">List18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">List19</a></td></tr>
  <tr><td> &lt;li&gt;</td>
    <td> List Item; nested inside a list (&lt;ul&gt; or &lt;ol&gt;)</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">Item18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">Item19</a></td></tr>
  <tr><td> &lt;hr&gt;</td>
    <td> Horizontal Rule; a horizontal line across the width of the text</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">Rule18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">Rule19</a></td></tr>
  <tr><td> &lt;br&gt;</td>
    <td> line break; break the "white space" rule: where spaces and carriage returns are generally treated the same; treated as a <i>required carriage return</i></td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">Break18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">Break19</a></td></tr>
  <tr><td> &lt;pre&gt;</td>
    <td> "PREformatted text", meaning "I've set this up just the way I want it, don't mess with it."; monospace font, and none of the spaces, tabs or carriage-returns are ignored </td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/01.FirstWebPage.md#a-few-new-tags-to-learn">Format18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/01-FirstPage.md#a-few-new-tags-to-learn">Format19</a></td></tr>
  <tr><td> &lt;i&gt;</td>
    <td> italic text; used for text in a different mood or voice, such as foreign words, a thought or technical terms</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#changes-in-html5">Tags18</a>, <a href="">Tags19</a></td></tr>
  <tr><td> &lt;b&gt;</td>
    <td> bolded text; used as a stylistic offset such as keywords in a document, product names or action words without making them as important; can also be used as headings in list items</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#changes-in-html5">Tags18</a>, <a href="">Tags19</a></td></tr>
  <tr><td> &lt;em&gt;</td>
    <td> Emphasizes text; semantic tag; stress emphasis of its contents</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#semantic-vs-style-tags">Tags18</a>, <a href="">Tags19</a></td></tr>
  <tr><td> &lt;strong&gt;</td>
    <td> Important text; semantic tag; indication of how something should be</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#semantic-vs-style-tags">Tags18</a>, <a href="">Tags19</a></td></tr>
  <tr><td> &lt;a&gt;</td>
    <td> create a hyperlink to other web pages, files, locations within the same page, email addresses, or any other URL</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02-HTML_CSS.md#anchor-element">Tags18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#anchor-element">Tags19</a></td></tr>
  <tr><td> &lt;style&gt;</td>
    <td> place CSS directly into an HTML document; anywhere in an HTML document;most common place: &lt;head&gt; section</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#3-2-css-basic-syntax">Tags18</a>, <a href="">Tags19</a></td></tr>
  <tr><td> &lt;link&gt;</td>
    <td> specify .css file within &lt;head&gt; section</td>
    <td><a href="../WebDev/Frontend-W3C/1.HTML5CSS/03.CSS.md#3-2-css-basic-syntax">Tags18</a>, <a href="">Tags19</a></td></tr>
</tbody>
</table>

