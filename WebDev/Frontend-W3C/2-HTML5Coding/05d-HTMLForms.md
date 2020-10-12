# Week 5: HTML5 Forms


## 5.4 Input types


### 5.4.0 Lecture Notes





+ [`<input>` types](https://tinyurl.com/yxud45vl)

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 55vw;" cellspacing="0" cellpadding="5" border="1">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/yxud45vl">&lt;input&gt; types</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 5%;">Type</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Basic Examples</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 5%;">Spec</th>
  </tr>
  </thead>
<tbody>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/button" title="<input> elements of type button are rendered as simple push buttons, which can be programmed to control custom functionality anywhere on a webpage as required when assigned an event handler function (typically for the click event).">button</a></td>
  <td>A push button with no default behavior displaying the value of the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/inpu#htmlattrdefvalue">value</a> attribute, empty by default.</td>
  <td id="examplebutton">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>button<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>button<span class="token punctuation">"</span></span> <span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplebutton" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplebutton?revision=1645029" width="200"></iframe></td>
  <td></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/checkbox" title="<input> elements of type checkbox are rendered by default as boxes that are checked (ticked) when activated, like you might see in an official government paper form. The exact appearance depends upon the operating system configuration under which the browser is running. Generally this is a square but it may have rounded corners. A checkbox allows you to select single values for submission in a form (or not).">checkbox</a></td>
  <td>A check box allowing single values to be selected/deselected.</td>
  <td id="examplecheckbox">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>checkbox<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>checkbox<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplecheckbox" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplecheckbox?revision=1645029" width="200"></iframe></td>
  <td></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/color" title="<input> elements of type color provide a user interface element that lets a user specify a color, either by using a visual color picker interface or by entering the color into a text field in #rrggbb hexadecimal format.">color</a></td>
  <td>A control for specifying a color; opening a color picker when active in supporting browsers.</td>
  <td id="examplecolor">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>color<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>color<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplecolor" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplecolor?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/date" title="<input> elements of type=&quot;date&quot; create input fields that let the user enter a date, either with a textbox that validates the input or a special date picker interface.">date</a></td>
  <td>A control for entering a date (year, month, and day, with no time). Opens a date picker or numeric wheels for year, month, day when active in supporting browsers.</td>
  <td id="exampledate">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>date<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>date<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_exampledate" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/exampledate?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/datetime-local" title="<input> elements of type datetime-local create input controls that let the user easily enter both a date and a time, including the year, month, and day as well as the time in hours and minutes.">datetime-local</a></td>
  <td>A control for entering a date and time, with no time zone. Opens a date picker or numeric wheels for date- and time-components when active in supporting browsers.</td>
  <td id="exampledtl">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>datetime-local<span class="token punctuation">"</span></span> 
    <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>datetime-local<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_exampledtl" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/exampledtl?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/email" title="<input> elements of type email are used to let the user enter and edit an e-mail address, or, if the multiple attribute is specified, a list of e-mail addresses.">email</a></td>
  <td>A field for editing an email address. Looks like a <code>text</code> input, but has validation parameters and relevant keyboard in supporting browsers and devices with dynamic keyboards.</td>
  <td id="exampleemail">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>email<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>email<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_exampleemail" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/exampleemail?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/file" title="<input> elements with type=&quot;file&quot; let the user choose one or more files from their device storage. Once chosen, the files can be uploaded to a server using form submission, or manipulated using JavaScript code and the File API.">file</a></td>
  <td>A control that lets the user select a file. Use the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/inpu#htmlattrdefaccept">accept</a> attribute to define the types of files that the control can select.</td>
  <td id="examplefile">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>file<span class="token punctuation">"</span></span> <span class="token attr-name">accept</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>image/*, text/*<span class="token punctuation">"</span></span> 
    <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>file<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplefile" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplefile?revision=1645029" width="100%"></iframe></td>
  <td></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/hidden" title="<input> elements of type hidden let web developers include data that cannot be seen or modified by users when a form is submitted. For example, the ID of the content that is currently being ordered or edited, or a unique security token. Hidden inputs are completely invisible in the rendered page, and there is no way to make it visible in the page's content.">hidden</a></td>
  <td>A control that is not displayed but whose value is submitted to the server. There is an example in the next column, but it's hidden!</td>
  <td></td>
  <td></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/image" title="<input> elements of type image are used to create graphical submit buttons, i.e. submit buttons that take the form of an image rather than text.">image</a></td>
  <td>A graphical <code>submit</code> button. Displays an image defined by the <code>src</code> attribute. The <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/inpu#htmlattrdefalt">alt</a> attribute displays if the image <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/inpu#htmlattrdefsrc">src</a> is missing.</td>
  <td id="exampleimage">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>image<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>image<span class="token punctuation">"</span></span>
    <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span><span class="token punctuation">"</span></span> <span class="token attr-name">alt</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>image input<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_exampleimage" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/exampleimage?revision=1645029" width="200"></iframe></td>
  <td></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/month" title="<input> elements of type month create input fields that let the user enter a month and year allowing a month and year to be easily entered. The value is a string whose value is in the format &quot;YYYY-MM&quot;, where YYYY is the four-digit year and MM is the month number.">month</a></td>
  <td>A control for entering a month and year, with no time zone.</td>
  <td id="examplemonth">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>month<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>month<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplemonth" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplemonth?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/number" title="<input> elements of type number are used to let the user enter a number. They include built-in validation to reject non-numerical entries.">number</a></td>
  <td>A control for entering a number. Displays a spinner and adds default validation when supported. Displays a numeric keypad in some devices with dynamic keypads.</td>
  <td id="examplenumber">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>number<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>number<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplenumber" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplenumber?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/password" title="<input> elements of type password provide a way for the user to securely enter a password.">password</a></td>
  <td>A single-line text field whose value is obscured. Will alert user if site is not secure.</td>
  <td id="examplepassword">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>password<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>password<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplepassword" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplepassword?revision=1645029" width="200"></iframe></td>
  <td></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/radio" title="<input> elements of type radio are generally used in radio groups—collections of radio buttons describing a set of related options.">radio</a></td>
  <td>A radio button, allowing a single value to be selected out of multiple choices with the same <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/inpu#htmlattrdefname">name</a> value.</td>
  <td id="exampleradio">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>radio<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>radio<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_exampleradio" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/exampleradio?revision=1645029" width="200"></iframe></td>
  <td></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/range" title="<input> elements of type range let the user specify a numeric value which must be no less than a given value, and no more than another given value. The precise value, however, is not considered important. This is typically represented using a slider or dial control rather than a text entry box like the number input type.">range</a></td>
  <td>A control for entering a number whose exact value is not important. Displays as a range widget defaulting to the middle value. Used in conjunction <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/inpu#htmlattrdefmin">min</a> and <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/inpu#htmlattrdefmax">max</a> to define the range of acceptable values.</td>
  <td id="examplerange">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>range<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>range<span class="token punctuation">"</span></span> 
    <span class="token attr-name">min</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>0<span class="token punctuation">"</span></span> <span class="token attr-name">max</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>25<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplerange" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplerange?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/reset" title="<input> elements of type &quot;reset&quot;&nbsp; are rendered as buttons, with a default click event handler that resets all of the inputs in the form to their initial values.">reset</a></td>
  <td>A button that resets the contents of the form to default values. Not recommended.</td>
  <td id="examplereset">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>reset<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>reset<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplereset" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplereset?revision=1645029" width="200"></iframe></td>
  <td></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/search" title="<input> elements of type search are text fields designed for the user to enter search queries into. These are functionally identical to text inputs, but may be styled differently by the user agent. ">search</a></td>
  <td>A single-line text field for entering search strings. Line-breaks are automatically removed from the input value. May include a delete icon in supporting browsers that can be used to clear the field. Displays a search icon instead of enter key on some devices with dynamic keypads.</td>
  <td id="examplesearch">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>search<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>search<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplesearch" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplesearch?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/submit" title="<input> elements of type submit are rendered as buttons. When the click event occurs (typically because the user clicked the button), the user agent attempts to submit the form to the server.">submit</a></td>
  <td>A button that submits the form.</td>
  <td id="examplesubmit">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>submit<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>submit<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_examplesubmit" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/examplesubmit?revision=1645029" width="200"></iframe></td>
  <td></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/tel" title="<input> elements of type tel are used to let the user enter and edit a telephone number. Unlike <input type=&quot;email&quot;> and <input type=&quot;url&quot;> , the input value is not automatically validated to a particular format before the form can be submitted, because formats for telephone numbers vary so much around the world.">tel</a></td>
  <td>A control for entering a telephone number. Displays a telephone keypad in some devices with dynamic keypads.</td>
  <td id="exampletel">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>tel<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>tel<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_exampletel" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/exampletel?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/text" title="<input> elements of type text create basic single-line text fields.">text</a></td>
  <td>The default value. A single-line text field. Line-breaks are automatically removed from the input value.</td>
  <td id="exampletext">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>text<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>text<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_exampletext" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/exampletext?revision=1645029" width="200"></iframe></td>
  <td></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/time" title="<input> elements of type time create input fields designed to let the user easily enter a time (hours and minutes, and optionally seconds).">time</a></td>
  <td>A control for entering a time value with no time zone.</td>
  <td id="exampletime">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>time<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>time<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_exampletime" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/exampletime?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/url" title="<input> elements of type url are used to let the user enter and edit a URL.">url</a></td>
  <td>A field for entering a URL. Looks like a <code>text</code> input, but has validation parameters and relevant keyboard in supporting browsers and devices with dynamic keyboards.</td>
  <td id="exampleurl">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>url<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>url<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_exampleurl" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/exampleurl?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
  <tr>
  <td><a href="https://developer.mozilla.org//en-US/docs/Web/HTML/Element/input/week" title="<input> elements of type week create input fields allowing easy entry of a year plus the ISO 8601 week number during that year (i.e., week 1 to 52 or 53).">week</a></td>
  <td>A control for entering a date consisting of a week-year number and a week number with no time zone.</td>
  <td id="exampleweek">
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>week<span class="token punctuation">"</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>week<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
    <iframe class="live-sample-frame nobutton" frameborder="0" height="55" id="frame_exampleweek" src="https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input$samples/exampleweek?revision=1645029" width="200"></iframe></td>
  <td><span class="inlineIndicator htmlVer htmlVerInline"><a href="https://developer.mozilla.org//en-US/docs/HTML/HTML5">HTML5</a></span></td>
  </tr>
</tbody>
</table>


### 5.4.1 Input types

In this section, we briefly present the input types, attributes, and elements related to the forms that came with HTML5. Details are given later, illustrated by multiple interactive examples.

Compared to HTML4, HTML5 introduced 13 new input types, covering most of the needs of  Web developers. HTML5 packages some of the "form best practices" in its specification. Web browsers providing native implementation give a boost in performance, and reduce the size of JavaScript embedded in complex Web pages.

MDN's Web docs [article on `<input>` types](https://tinyurl.com/yxud45vl) lists all input types and highlights those that came with HTML5.

Now, let's play with some of these input types and attributes.


### 5.4.2 "color"

For years, we used hundreds of lines of JavaScript for selecting colors. Now, it's bundled in the browser!

Here is how it looks on some mobile devices:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y452y3ur')"
    src    ="https://tinyurl.com/yxnpbsf2"
    alt    ="HTML5 input type=color on an android phone"
    title  ="HTML5 input type=color on an android phone"
  />
</figure>


#### Typical use

Inserting a color chooser is as simple as:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;&lt;head&gt;...&lt;/head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Choose a color : </span><strong><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"color" value="#FF00FF"</span><span class="tag">/&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

Note: In this chapter we are simplifying the examples, as we usually embed input elements in a `<form>`...`</form>`.

Try `<input type="color">` online with this [JSBin example](https://jsbin.com/cajuzob/1/edit?html,output). Or do it here in your browser: just click on the purple square below : <input value="#FF00FF" type="color"> ([Local Example - ])

Here is the result on Google Chrome (works with other browsers too, though the look and feel may differ):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y452y3ur')"
    src    ="https://tinyurl.com/y2spxe7s"
    alt    ="input type=color in google chrome"
    title  ="input type=color in google chrome"
  />
</figure>


__Example: changing the background color of the page__

The `<input type="color">` can fire `change` or `input` events. Here is an example that changes the background color of the page when a color is chosen. [Try it online at JSBin](https://jsbin.com/jozuter/1/edit?html,css,js,console,output).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y452y3ur')"
    src    ="https://tinyurl.com/y4fhse8z"
    alt    ="change background color of the body"
    title  ="change background color of the body"
  />
</figure>


Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;&lt;head&gt;&lt;/head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; Select a color : </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"color"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"colorChooser"</span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> colorInputField </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#colorChooser"</span><span class="pun">);<br></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>colorInputField</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'input'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">backgroundColor </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


#### Offer a limited choice of colors

By default, the color selector offers many options that may either frighten some users or just not be appropriate for the purpose of the application. 

Good news: it is possible to restrict the choices, and also simplify the user interface, by using a `<datalist>` with some `<option>` elements inside. 

Example: click the black rectangle on the right: `<input list="colors" value="#333333" type="color">`. The following should be displayed:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y452y3ur')"
    src    ="https://tinyurl.com/y4wpv7ne"
    alt    ="restricted choice of color"
    title  ="restricted choice of color"
  />
</figure>


[Online example at JSBin](https://jsbin.com/lahapu/edit?html,output)

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"color"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"#333333"</span><span class="pln"> </span><strong><span class="atn">list</span><span class="pun">=</span><span class="atv">"colors"</span></strong><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;datalist</span><span class="pln"> </span><strong><span class="atn">id</span><span class="pun">="</span><span class="atv">colors"</span></strong><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option&gt;</span><span class="pln">#0000FF</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option&gt;</span><span class="pln">#00FF00</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option&gt;</span><span class="pln">#FF0000</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/datalist&gt;</span></li>
</ol></div>

Note that the id of the `<datalist>` element should be the same as the value of the list attribute of the input field.


#### What are the main problems with this element?

The main criticism that Web designers make about this element is related to its default appearance being strongly dependent on the browser and its underlying operating system. Changing the look and feel is not possible, except with the use of the options we saw in the previous sections of this page. This problem is also true for other input elements that renders as complex widgets, like <input type="date"> and its variants.

Another problem is that there is no way to control where the dialog that contains the color chooser will appear - no positioning via CSS or JavaScript is possible. The specification does not say anything about how to position it over the page, thus the result is vendor specific.

The solution proposed by the W3C and its contributors is called Web Components, a new approach for designing HTML5 widgets, that is covered in the W3Cx HTML5 Apps and Games course.


#### Knowledge check 5.4.2 

1. On mobile devices, `<input type=color>` pops up a dialog that is adapted to each operating system (IOS, Android, etc.). On desktops, the native implementations differ in their look'n' feel. Is it possible to thoroughly customize the look'n' feel of this input type using only CSS and HTML attributes? (Yes/No)

  Ans: 






