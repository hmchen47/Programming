# HTML Forms

## Reference: HTML Form Tags

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 50vw;" cellspacing="0" cellpadding="5" border="1">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.javatpoint.com/html-form#h5o-3">HTML Form Tags</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 5%;">Tag</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
  </tr>
  </thead>
  <tbody>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y2efbybz">&lt;form&gt;</td><td>define an HTML form to enter inputs by the used side.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y2ffg7b6">&lt;input&gt;</td><td>define an input control.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y4lluqnb">&lt;textarea&gt;</td><td>define a multi-line input control.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y5ep4bhs">&lt;label&gt;</td><td>define a label for an input element.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y2oqkqu8">&lt;fieldset&gt;</td><td>group the related element in a form.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y6zqvp5p">&lt;legend&gt;</td><td>define a caption for a &lt;fieldset&gt; element.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y3e8qdrd">&lt;select&gt;</td><td>define a drop-down list.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y3mztlhq">&lt;optgroup&gt;</td><td>define a group of related options in a drop-down list.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y6dnaxso">&lt;option&gt;</td><td>define an option in a drop-down list.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y49fsy5a">&lt;button&gt;</td><td>define a clickable button.</td></tr>
    <tr><td colspan="2" style="font-size: 1.3em; text-align: center; color: #3d64ff;">HTML 5 Form Tag</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y62577nm">&lt;datalist&gt;</td><td>specify a list of pre-defined options for input control.</td></tr>
    <tr><td style="font-weight: bold;"><a href="">&lt;keygen&gt;</td><td>define a key-pair generator field for forms.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/yyoz4alq">&lt;output&gt;</td><td>define the result of a calculation.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y27klaa2">&lt;progress&gt;</td><td>provide an easy way for web developers to create progress bar on the website.</td></tr>
    <tr><td style="font-weight: bold;"><a href="https://tinyurl.com/y4ebasra">&lt;meter&gt;</td><td>provide an easy way for web developers to create progress bar on the website.</td></tr>
  </tbody>
</table>




## Reference: `<input>` types

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
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>file<span class="token punctuation">"</span></span> 
    <span class="token attr-name">accept</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>image/*, text/*<span class="token punctuation">"</span></span> 
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
    <pre class="brush: html hidden notranslate line-numbers language-html"><code class=" language-html"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>  <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>password<span class="token punctuation">"</span></span> 
    <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>password<span class="token punctuation">"</span></span><span class="token punctuation">/&gt;</span></span><span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
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

<br/>

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 55vw;" cellspacing="0" cellpadding="5" border="1">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/y5bx7m6l">List Attributes of &lt;input&gt;</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Keyword</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">State</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Data Type</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Control Type</th>
  </tr>
  </thead>
  <tbody>
    <tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-hidden"><code>hidden</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-hidden"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-hidden" id="ref-for-element-statedef-input-hidden⑦">Hidden</a></code> 
    </td><td> An arbitrary string 
    </td><td> n/a 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-text"><code>text</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-text"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-text" id="ref-for-element-statedef-input-text①">Text</a></code> 
    </td><td> Text with no line breaks 
    </td><td> A text field or combo box 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-search"><code>search</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-search"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-search" id="ref-for-element-statedef-input-search①">Search</a></code> 
    </td><td> Text with no line breaks 
    </td><td> Search field or combo box 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-tel"><code>tel</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-tel"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-telephone" id="ref-for-element-statedef-input-telephone②">Telephone</a></code> 
    </td><td> Text with no line breaks 
    </td><td> A text field or combo box 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-url"><code>url</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-url"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-url" id="ref-for-element-statedef-input-url①">URL</a></code> 
    </td><td> An absolute URL 
    </td><td> A text field or combo box 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-email"><code>email</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-email"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-e-mail" id="ref-for-element-statedef-input-e-mail①">E-mail</a></code> 
    </td><td> An e-mail address or list of e-mail addresses 
    </td><td> A text field or combo box 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-password"><code>password</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-password"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-password" id="ref-for-element-statedef-input-password">Password</a></code> 
    </td><td> Text with no line breaks (sensitive information) 
    </td><td> A text field that obscures data entry 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-date"><code>date</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-date"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-date" id="ref-for-element-statedef-input-date">Date</a></code> 
    </td><td> A date (year, month, day) with no time zone 
    </td><td> A date control 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-month"><code>month</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-month"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-month" id="ref-for-element-statedef-input-month">Month</a></code> 
    </td><td> A date consisting of a year and a month with no time zone 
    </td><td> A month control 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-week"><code>week</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-week"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-week" id="ref-for-element-statedef-input-week">Week</a></code> 
    </td><td> A date consisting of a week-year number and a week number with no time zone 
    </td><td> A week control 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-time"><code>time</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-time"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-time" id="ref-for-element-statedef-input-time">Time</a></code> 
    </td><td> A time (hour, minute, seconds, fractional seconds) with no time zone 
    </td><td> A time control 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-datetime-local"><code>datetime-local</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-datetime-local"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-localdatetime" id="ref-for-element-statedef-input-localdatetime">Local Date and Time</a></code> 
    </td><td> A date and time (year, month, day, hour, minute, second, fraction of a second) with no timezone offset 
    </td><td> A date and time control 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-number"><code>number</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-number"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-number" id="ref-for-element-statedef-input-number">Number</a></code> 
    </td><td> A numerical value 
    </td><td> A text field or combo box or spinner control 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-range"><code>range</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-range"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-range" id="ref-for-element-statedef-input-range">Range</a></code> 
    </td><td> A numerical value, with the extra semantic that the exact value is not important 
    </td><td> A slider control or similar 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-color"><code>color</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-color"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-color" id="ref-for-element-statedef-input-color">Color</a></code> 
    </td><td> An sRGB color with 8-bit red, green, and blue components 
    </td><td> A color well 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-checkbox"><code>checkbox</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-checkbox"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-checkbox" id="ref-for-element-statedef-input-checkbox">Checkbox</a></code> 
    </td><td> A set of zero or more values from a predefined list 
    </td><td> A checkbox 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-radio"><code>radio</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-radio"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-radio" id="ref-for-element-statedef-input-radio③">Radio Button</a></code> 
    </td><td> An enumerated value 
    </td><td> A radio button 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-file"><code>file</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-file"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-file" id="ref-for-element-statedef-input-file①">File Upload</a></code> 
    </td><td> Zero or more files each with a <a data-link-type="dfn" href="infrastructure.html#mime-type" id="ref-for-mime-type②②">MIME type</a> and optionally a file name 
    </td><td> A label and a button 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-submit"><code>submit</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-submit"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-submit" id="ref-for-element-statedef-input-submit">Submit Button</a></code> 
    </td><td> An enumerated value, with the extra semantic that it must be the last value selected and initiates <a data-link-type="dfn" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#form-submission" id="ref-for-form-submission①">form submission</a> 
    </td><td> A button 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-image"><code>image</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-image"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-image" id="ref-for-element-statedef-input-image④">Image Button</a></code> 
    </td><td> A coordinate, relative to a particular image’s size, with the extra semantic that it must be the last value selected and initiates <a data-link-type="dfn" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#form-submission" id="ref-for-form-submission②">form submission</a> 
    </td><td> Either a clickable image, or a button 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-reset"><code>reset</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-reset"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-reset" id="ref-for-element-statedef-input-reset①">Reset Button</a></code> 
    </td><td> n/a 
    </td><td> A button 
    </td></tr><tr>
    <td> <dfn data-dfn-for="input/type" data-dfn-type="attr-value" data-export="" id="attr-valuedef-input-type-button"><code>button</code><a class="self-link" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#attr-valuedef-input-type-button"></a></dfn> 
    </td><td> <code><a data-link-type="element-sub" href="https://www.w3.org/TR/html52/sec-forms.htmlsec-forms.html#element-statedef-input-button" id="ref-for-element-statedef-input-button①">Button</a></code> 
    </td><td> n/a 
    </td><td> A button 
  </td></tr>
  </tbody>
</table>





## Reference: HTML5 form attributes

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 55vw;" cellspacing="0" cellpadding="5" border="1">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/j7gv3y6">Attributes for the &lt;input&gt; element include global HTML attributes</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 5%;">Attribute</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Type or Types</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Description</th>
  </tr>
</thead>
<tbody>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefaccept">accept</a></td><td>file</td><td>Hint for expected file type in file upload controls</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefalt">alt</a></td><td>image</td><td>alt attribute for the image type. Required for accessibility</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefautocomplete"><strong style="color: cyan;">autocomplete</strong></a></td><td>all</td><td>Hint for form autofill feature</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefautofocus"><strong style="color: cyan;">autofocus</strong></a></td><td>all</td><td>Automatically focus the form control when the page is loaded</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefcapture">capture</a></td><td>file</td><td>Media capture input method in file upload controls</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefchecked">checked</a></td><td>radio, checkbox</td><td>Whether the command or control is checked</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefdirname">dirname</a></td><td>text, search</td><td>Name of form field to use for sending the element's directionality in form submission</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefdisabled">disabled</a></td><td>all</td><td>Whether the form control is disabled</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefform"><strong style="color: cyan;">form</strong></a></td><td>all</td><td>Associates the control with a form element</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefformaction"><strong style="color: cyan;">formaction</strong></a></td><td>image, submit</td><td>URL to use for form submission</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefformenctype"><strong style="color: cyan;">formenctype</strong></a></td><td>image, submit</td><td>Form data set encoding type to use for form submission</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefformmethod"><strong style="color: cyan;">formmethod</strong></a></td><td>image, submit</td><td>HTTP method to use for form submission</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefformnovalidate"><strong style="color: cyan;">formnovalidate</strong></a></td><td>image, submit</td><td>Bypass form control validation for form submission</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefformtarget"><strong style="color: cyan;">formtarget</strong> </a></td><td>image, submit</td><td>Browsing context for form submission</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefheight">height</a></td><td>image</td><td>Same as <code>height</code> attribute for <a href="/en-US/docs/Web/HTML/Element/img" title="The HTML <img> element embeds an image into the document."><code>&lt;img&gt;</code></a>; vertical dimension</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdeflist"><strong style="color: cyan;">list</strong></a></td><td>almost all</td><td>Value of the id attribute of the <a href="/en-US/docs/Web/HTML/Element/datalist" title="The HTML <datalist> element contains a set of <option> elements that represent the permissible or recommended options available to choose from within other controls."><code>&lt;datalist&gt;</code></a> of autocomplete options</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmax"><strong style="color: cyan;">max</strong></a></td><td>numeric types</td><td>Maximum value</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmaxlength">maxlength</a></td><td>password, search, tel, text, url</td><td>Maximum length (number of characters) of <code>value</code></td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmin"><strong style="color: cyan;">min</strong></a></td><td>numeric types</td><td>Minimum value</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefminlength">minlength</a></td><td>password, search, tel, text, url</td><td>Minimum length (number of characters) of <code>value</code></td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmultiple"><strong style="color: cyan;">multiple</strong></a></td><td>email, file</td><td>Boolean. Whether to allow multiple values</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefname">name</a></td><td>all</td><td>Name of the form control. Submitted with the form as part of a name/value pair.</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefpattern"><strong style="color: cyan;">pattern</strong></a></td><td>password, text, tel</td><td>Pattern the <code>value</code> must match to be valid</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefplaceholder"><strong style="color: cyan;">placeholder</strong></a></td><td>password, search, tel, text, url</td><td>Text that appears in the form control when it has no value set</td></tr>
  <tr><td><a href="/en-US/docs/Web/HTML/Attributes/readonly"><strong style="color: cyan;">readonly</strong></a></td><td>almost all</td><td>Boolean. The value is not editable</td></tr>
  <tr><td><a href="/en-US/docs/Web/HTML/Attributes/required"><strong style="color: cyan;">required</strong></a></td><td>almost all</td><td>Boolean. A value is required or must be check for the form to be submittable</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefsize">size</a></td><td>email, password, tel, text</td><td>Size of the control</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefsrc">src</a></td><td>image</td><td>Same as <code>src</code> attribute for <a href="/en-US/docs/Web/HTML/Element/img" title="The HTML <img> element embeds an image into the document."><code>&lt;img&gt;</code></a>; address of image resource</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefstep"><strong style="color: cyan;">step</strong></a></td><td>numeric types</td><td>Incremental values that are valid.</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdeftype">type</a></td><td>all</td><td>Type of form control</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefvalue">value</a></td><td>all</td><td>Current value of the form control. Submitted with the form as part of a name/value pair.</td></tr>
  <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefwidth">width</a></td><td>image</td><td>Same as <code>width</code> attribute for <a href="/en-US/docs/Web/HTML/Element/img" title="The HTML <img> element embeds an image into the document."><code>&lt;img&gt;</code></a></td> </tr>
</tbody>
</table>







