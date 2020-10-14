# HTML Forms

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



## Reference: Methods for regular expressions in JavaScript

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 55vw;" cellspacing="0" cellpadding="5" border="1">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/y22np4b5">Methods using regular expressions</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Method</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
  </tr>
  </thead>
  <tbody>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec"><code>exec()</code></a></td><td>Executes a search for a match in a string. It returns an array of information or <code>null</code> on a mismatch.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test"><code>test()</code></a></td><td>Tests for a match in a string. It returns <code>true</code> or <code>false</code>.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match"><code>match()</code></a></td><td>Returns an array containing all of the matches, including capturing groups, or <code>null</code> if no match is found.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll"><code>matchAll()</code></a></td><td>Returns an iterator containing all of the matches, including capturing groups.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search"><code>search()</code></a></td><td>Tests for a match in a string. It returns the index of the match, or <code>-1</code> if the search fails.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace"><code>replace()</code></a></td><td>Executes a search for a match in a string, and replaces the matched substring with a replacement substring.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll"><code>replaceAll()</code></a></td><td>Executes a search for all matches in a string, and replaces the matched substrings with a replacement substring.</td></tr>
    <tr><td><a href="https://developer.mozilla.org//en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split"><code>split()</code></a></td><td>Uses a regular expression or a fixed string to break a string into an array of substrings.</td></tr>
  </tbody>
</table>


## Reference: Special characters in regular expressions

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 55vw;" cellspacing="0" cellpadding="5" border="1">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/y9jzpgll">Special characters in regular expressions</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Characters</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Meaning</th>
  </tr>
  </thead>
  <tbody>
    <tr><th colspan="2" style="text-align: center; background-color: lightgray; color: gray; font-size: 1.2em;"><a href="https://tinyurl.com/yxtgs26n">Character Classes</a></th></tr>
		<tr>
			<td><code>.</code></td>
			<td>
			<p>Has one of the following meanings:</p>
			<ul>
				<li>Matches any single character <em>except</em> line terminators: <code>\n</code>, <code>\r</code>, <code>\u2028</code> or <code>\u2029</code>.&nbsp;For example, <code>/.y/</code> matches "my" and "ay", but not "yes", in "yes make my day".</li>
				<li>Inside a character set, the dot loses its special meaning and matches a literal dot.</li>
			</ul>
			<p>Note that the <code>m</code> multiline flag doesn't change the dot behavior. So to match a pattern across multiple lines, the character set <code>[^]</code> can be used — it will match any character including newlines.</p>
			<p>ES2018 added&nbsp;the <code>s</code> "dotAll" flag, which allows the dot to also match line terminators.</p>
			</td>
		</tr>
		<tr>
			<td><code>\d</code></td>
			<td>
			<p>Matches any digit (Arabic numeral). Equivalent to <code>[0-9]</code>. For example, <code>/\d/</code> or <code>/[0-9]/</code> matches "2" in "B2 is the suite number".</p>
			</td>
		</tr>
		<tr>
			<td><code>\D</code></td>
			<td>
			<p>Matches any character that is not a digit (Arabic numeral). Equivalent to <code>[^0-9]</code>. For example, <code>/\D/</code> or <code>/[^0-9]/</code> matches "B" in "B2 is the suite number".</p>
			</td>
		</tr>
		<tr>
			<td><code>\w</code></td>
			<td>
			<p>Matches any alphanumeric character from the basic Latin alphabet, including the underscore. Equivalent to <code>[A-Za-z0-9_]</code>. For example, <code>/\w/</code> matches "a" in "apple", "5" in "$5.28", "3" in "3D" and "m" in "Émanuel".</p>
			</td>
		</tr>
		<tr>
			<td><code>\W</code></td>
			<td>
			<p>Matches any character that is not a word character from the basic Latin alphabet. Equivalent to <code>[^A-Za-z0-9_]</code>. For example, <code>/\W/</code> or <code>/[^A-Za-z0-9_]/</code> matches "%" in "50%" and "É" in "Émanuel".</p>
			</td>
		</tr>
		<tr>
			<td><code>\s</code></td>
			<td>
			<p>Matches a single white space character, including space, tab, form feed, line feed, and other Unicode spaces. Equivalent to <code>[ \f\n\r\t\v\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]</code>. For example, <code>/\s\w*/</code> matches " bar" in "foo bar".</p>
			</td>
		</tr>
		<tr>
			<td><code>\S</code></td>
			<td>
			<p>Matches a single character other than white space. Equivalent to <code>[^ \f\n\r\t\v\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]</code>. For example, <code>/\S\w*/</code> matches "foo" in "foo bar".</p>
			</td>
		</tr>
		<tr><td><code>\t</code></td><td>Matches a horizontal tab.</td></tr>
		<tr><td><code>\r</code></td><td>Matches a carriage return.</td></tr>
		<tr><td><code>\n</code></td><td>Matches a linefeed.</td></tr>
		<tr><td><code>\v</code></td><td>Matches a vertical tab.</td></tr>
		<tr><td><code>\f</code></td><td>Matches a form-feed.</td></tr>
		<tr>
			<td><code>[\b]</code></td>
			<td>Matches a backspace. If you're looking for the word-boundary character (<code>\b</code>), see <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Boundaries">Boundaries</a>.</td>
		</tr>
		<tr><td><code>\0</code></td><td>Matches a NUL character. Do not follow this with another digit.</td></tr>
		<tr>
			<td><code>\c<em>X</em></code></td>
			<td>
			<p>Matches a control character using <a class="external" href="https://en.wikipedia.org/wiki/Caret_notation" rel="noopener">caret notation</a>, where "X" is a letter from A–Z (corresponding to codepoints <code>U+0001</code><em>–</em><code>U+001F</code>). For example, <code>/\cM/</code>&nbsp;matches "\r"&nbsp;in&nbsp;"\r\n".</p>
			</td>
		</tr>
		<tr><td><code>\x<em>hh</em></code></td><td>Matches the character with the code <code><em>hh</em></code> (two hexadecimal digits).</td></tr>
		<tr><td><code>\u<em>hhhh</em></code></td><td>Matches a UTF-16 code-unit with the value <code><em>hhhh</em></code> (four hexadecimal digits).</td>
		</tr>
		<tr><td><code>\u<em>{hhhh} </em>or <em>\u{hhhhh}</em></code></td><td>(Only when the <code>u</code> flag is set.) Matches the character with the Unicode value <code>U+<em>hhhh</em></code> or&nbsp;<code>U+<em>hhhhh</em></code> (hexadecimal digits).</td>
		</tr>
		<tr><td><code>\</code></td><td>
			<p>Indicates that the following character should be treated specially, or "escaped". It behaves one of two ways.</p>
			<ul>
				<li>For characters that are usually treated literally, indicates that the next character is special and not to be interpreted literally. For example, <code>/b/</code> matches the character "b". By placing a backslash in front of "b", that is by using <code>/\b/</code>, the character becomes special to mean match a word boundary.</li>
				<li>For characters that are usually treated specially, indicates that the next character is not special and should be interpreted literally. For example, "*" is a special character that means 0 or more occurrences of the preceding character should be matched; for example, <code>/a*/</code> means match 0 or more "a"s. To match <code>*</code> literally, precede it with a backslash; for example, <code>/a\*/</code> matches "a*".</li>
			</ul>
			<div class="blockIndicator note">
			<p>To match this character literally, escape it with itself. In other words to search for <code>\</code>&nbsp;use <code>/\\/</code>.</p>
			</div>
			</td>
		</tr>
    <tr><th colspan="2" style="text-align: center; background-color: lightgray; color: gray; font-size: 1.2em;"><a href="https://tinyurl.com/y4lgft7c">Boundary-type Assertions</a></th></tr>
  <tr><td><code>^</code></td><td>
    <p>Matches the beginning of input. If the multiline flag is set to true, also matches immediately after a line break character. For example, <code>/^A/</code> does not match the "A" in "an A", but does match the first "A" in "An A".</p>
    <div class="blockIndicator note">
    <p>This character has a different meaning when it appears at the start of a <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Groups_and_Ranges">group</a>.</p>
    </div>
   </td>
  </tr>
  <tr><td><code>$</code></td><td>
    <p>Matches the end of input. If the multiline flag is set to true, also matches immediately before a line break character. For example, <code>/t$/</code> does not match the "t" in "eater", but does match it in "eat".</p>
   </td>
  </tr>
  <tr><td><code>\b</code></td><td>
    <p>Matches a word boundary. This is the position where a word character is not followed or preceded by another word-character, such as between a letter and a space. Note that a matched word boundary is not included in the match. In other words, the length of a matched word boundary is zero.</p>
    <p>Examples:</p>
    <ul>
     <li><code>/\bm/</code>&nbsp;matches the "m" in "moon".</li>
     <li><code>/oo\b/</code>&nbsp;does not match the "oo" in "moon", because "oo" is followed by "n" which is a word character.</li>
     <li><code>/oon\b/</code>&nbsp;matches the "oon" in "moon", because "oon" is the end of the string, thus not followed by a word character.</li>
     <li><code>/\w\b\w/</code>&nbsp;will never match anything, because a word character can never be followed by both a non-word and a word character.</li>
    </ul>
    <p>To match a backspace character (<code>[\b]</code>), see <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Character_Classes">Character Classes</a>.</p>
   </td>
  </tr>
  <tr><td><code>\B</code></td><td>
    <p>Matches a non-word boundary. This is a position where the previous and next character are of the same type: Either both must be words, or both must be non-words, for example between two letters or between two spaces.&nbsp;The beginning and end of a string are considered non-words. Same as the matched word boundary, the matched non-word boundary is also not included in the match. For example, <code>/\Bon/</code> matches "on" in "at noon", and <code>/ye\B/</code> matches "ye" in "possibly yesterday".</p>
   </td>
  </tr>
  <tr><th colspan="2" style="text-align: center; background-color: lightgray; color: gray; font-size: 1.2em;"><a href="https://tinyurl.com/y4lgft7c">Boundary-type Assertions</a></th></tr>
  <tr><td><code>x(?=y)</code></td><td>
    <p><strong>Lookahead assertion:&nbsp;</strong>Matches "x" only if "x" is followed by "y". For example, /<code>Jack(?=Sprat)/</code> matches "Jack" only if it is followed by "Sprat".<br>
     <code>/Jack(?=Sprat|Frost)/</code> matches "Jack" only if it is followed by "Sprat" or "Frost". However, neither "Sprat" nor "Frost" is part of the match results.</p>
   </td>
  </tr>
  <tr><td><code>x(?!y)</code></td><td>
    <p><strong>Negative lookahead assertion:&nbsp;</strong>Matches "x" only if "x"<span> is not followed by </span>"y"<span>.</span>&nbsp;For example, <code>/\d+(?!\.)/</code><span> matches a number only if it is not followed by a decimal point.&nbsp;</span><code>/\d+(?!\.)/.exec('3.141')</code> matches "141" but not "3.</p>
   </td>
  </tr>
  <tr><td><code>(?&lt;=y)x</code></td><td>
    <p><strong>Lookbehind assertion:&nbsp;</strong>Matches "x" only if "x" is preceded&nbsp;by "y".&nbsp;For example, <code>/(?&lt;=Jack)Sprat/</code><span> matches "Sprat" only if it is preceded by "Jack".&nbsp;</span><code>/(?&lt;=Jack|Tom)Sprat/</code> matches "Sprat" only if it is preceded by "Jack" or "Tom". However, neither "Jack" nor "Tom" is part of the match results.</p>
   </td>
  </tr>
  <tr>
   <td><code>(?&lt;!y)x</code></td>
   <td>
    <p><strong>Negative lookbehind assertion:&nbsp;</strong>Matches "x" only if "x" is not preceded&nbsp;by "y".&nbsp;For example, <code>/(?&lt;!-)\d+/</code><span> matches a number only if it is not preceded by a minus sign.&nbsp;</span><code>/(?&lt;!-)\d+/.exec('3')</code> matches "3".&nbsp;<code>/(?&lt;!-)\d+/.exec('-3')</code> &nbsp;match is not found because the&nbsp;number is preceded by the minus sign.</p>
   </td>
  </tr>
  <tr><th colspan="2" style="text-align: center; background-color: lightgray; color: gray; font-size: 1.2em;"><a href="https://tinyurl.com/y4687y4a">Groups and Ranges</a></th></tr>
  <tr><td><code><em>x</em>|<em>y</em></code></td><td>
    <p>Matches either "x" or "y". For example, <code>/green|red/</code> matches "green" in "green apple" and "red" in "red apple".</p>
   </td>
  </tr>
  <tr>
   <td><code>[xyz]<br>
    [a-c]</code></td>
   <td>
    <p>A character set. Matches any one of the enclosed characters. You can specify a range of characters by using a hyphen, but if the hyphen appears as the first or last character enclosed in the square brackets it is taken as a literal hyphen to be included in the character set as a normal character. It is also possible to include a character class in a character set.</p>
    <p>For example, <code>[abcd]</code> is the same as <code>[a-d]</code>. They match the "b" in "brisket", and the "c" in "chop".</p>
    <p>For example, <code>[abcd-]</code> and <code>[-abcd]</code> match the "b" in "brisket", the "c" in "chop", and the "-" (hyphen) in "non-profit".</p>
    <p>For example, <code>[\w-]</code> is the same as <code>[A-Za-z0-9_-]</code>. They both match the "b" in "brisket", the "c" in "chop", and the "n" in "non-profit".</p>
   </td>
  </tr>
  <tr>
   <td>
    <p><code>[^xyz]<br>
     [^a-c]</code></p>
   </td>
   <td>
    <p>A negated or complemented character set. That is, it matches anything that is not enclosed in the brackets. You can specify a range of characters by using a hyphen, but if the hyphen appears as the first or last character enclosed in the square brackets it is taken as a literal hyphen to be included in the character set as a normal character. For example, <code>[^abc]</code> is the same as <code>[^a-c]</code>. They initially match "o" in "bacon" and "h" in "chop".</p>
    <div class="blockIndicator note">
    <p>The ^ character may also indicate the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Boundaries">beginning of input</a>.</p>
    </div>
   </td>
  </tr>
  <tr><td><code>(<em>x</em>)</code></td><td>
    <p><strong>Capturing group:&nbsp;</strong>Matches <code><em>x</em></code> and remembers the match. For example, <code>/(foo)/</code> matches and remembers "foo" in "foo bar".&nbsp;</p>
    <p>A regular expression may have multiple capturing groups. In results, matches to capturing groups typically in an array whose members are in the same order as the left parentheses in the capturing group. This is usually just the order of the capturing groups themselves. This becomes important when capturing groups are nested. Matches are accessed using the index of the the result's elements (<code>[1], ..., [n]</code>) or from the predefined <code>RegExp</code> object's properties (<code>$1, ..., $9</code>).</p>
    <p>Capturing groups have a performance penalty. If you don't need the matched substring to be recalled, prefer non-capturing parentheses (see below).</p>
    <p><code><a href="/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match">String.match()</a></code> won't return groups if the <code>/.../g</code> flag is set. However, you can still use <code><a href="/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll">String.matchAll()</a></code> to get all matches.</p>
   </td>
  </tr>
  <tr><td><code>\<em>n</em></code></td><td>
    <p>Where "n" is a positive integer. A back reference to the last substring matching the n parenthetical in the regular expression (counting left parentheses). For example, <code>/apple(,)\sorange\1/</code> matches "apple, orange," in "apple, orange, cherry, peach".</p>
   </td>
  </tr>
  <tr><td><code>\k&lt;Name&gt;</code></td><td>
    <p>A back reference to the last substring matching the <strong>N</strong><strong>amed capture&nbsp;group </strong>specified by <code>&lt;Name&gt;</code>.</p>
    <p>For example, <code>/(?&lt;title&gt;\w+), yes \k&lt;title&gt;/</code>&nbsp;matches "Sir, yes Sir" in "Do you copy? Sir, yes Sir!".</p>
    <div class="blockIndicator note">
    <p><code>\k</code> is&nbsp;used literally here to indicate the beginning of a back reference to a Named capture group.</p>
    </div>
   </td>
  </tr>
  <tr><td><code>(?&lt;Name&gt;x)</code></td><td>
    <p><strong>Named capturing group:&nbsp;</strong>Matches "x" and stores it on the groups property of the returned matches under the name specified by <code>&lt;Name&gt;</code>. The angle brackets (<code>&lt;</code> and <code>&gt;</code>) are required for group name.</p>
    <p>For example, to extract the United States area code from a phone number, we could use <code>/\((?&lt;area&gt;\d\d\d)\)/</code>. The resulting number would appear under <code>matches.groups.area</code>.</p>
   </td>
  </tr>
  <tr><td><code>(?:<em>x</em>)</code></td><td><strong>Non-capturing group:&nbsp;</strong>Matches "x" but does not remember the match. The matched substring cannot be recalled from the resulting array's elements (<code>[1], ..., [n]</code>) or from the predefined <code>RegExp</code> object's properties (<code>$1, ..., $9</code>).</td>
  </tr>
  <tr><th colspan="2" style="text-align: center; background-color: lightgray; color: gray; font-size: 1.2em;"><a href="https://tinyurl.com/y3k4gtxx">Quantifiers</a></th></tr>
  <tr><td><code><em>x</em>*</code></td><td>
    <p>Matches the preceding item "x" 0 or more times. For example, <code>/bo*/</code> matches "boooo" in "A ghost booooed" and "b" in "A bird warbled", but nothing in "A goat grunted".</p>
   </td>
  </tr>
  <tr><td><code><em>x</em>+</code></td><td>
    <p>Matches the preceding item "x" 1 or more times. Equivalent to <code>{1,}</code>. For example, <code>/a+/</code> matches the "a" in "candy" and all the "a"'s in "caaaaaaandy".</p>
   </td>
  </tr>
  <tr><td><code><em>x</em>?</code></td><td>
    <p>Matches the preceding item "x" 0 or 1 times. For example, <code>/e?le?/</code> matches the "el" in "angel" and the "le" in "angle."</p>
    <p>If used immediately after any of the quantifiers <code>*</code>, <code>+</code>, <code>?</code>, or <code>{}</code>, makes the quantifier non-greedy (matching the minimum number of times), as opposed to the default, which is greedy (matching the maximum number of times).</p>
   </td>
  </tr>
  <tr><td><code><em>x</em>{<em>n</em>}</code></td><td>
    <p>Where "n" is a positive integer, matches exactly "n" occurrences of the preceding item "x". For example, <code>/a{2}/</code> doesn't match the "a" in "candy", but it matches all of the "a"'s in "caandy", and the first two "a"'s in "caaandy".</p>
   </td>
  </tr>
  <tr><td><code><em>x</em>{<em>n</em>,}</code></td><td>
    <p>Where "n" is a positive integer, matches at least "n" occurrences of the preceding item "x". For example, <code>/a{2,}/</code> doesn't match the "a" in "candy", but matches all of the a's in "caandy" and in "caaaaaaandy".</p>
   </td>
  </tr>
  <tr><td><code><em>x</em>{<em>n</em>,<em>m</em>}</code></td><td>
    <p>Where "n" is 0 or a positive integer, "m" is a positive integer, and <code><em>m</em> &gt; <em>n</em></code>, matches at least "n" and at most "m" occurrences of the preceding item "x". For example, <code>/a{1,3}/</code> matches nothing in "cndy", the "a" in "candy", the two "a"'s in "caandy", and the first three "a"'s in "caaaaaaandy". Notice that when matching "caaaaaaandy", the match is "aaa", even though the original string had more "a"s in it.</p>
   </td>
  </tr>
  <tr>
   <td><p><code><em>x</em>*?</code><br><code><em>x</em>+?</code><br><code><em>x</em>??</code><br><code><em>x</em>{n}?</code><br><code><em>x</em>{n,}?</code><br><code><em>x</em>{n,m}?</code></p></td><td>
    <p>By default quantifiers like <code>*</code> and <code>+</code> are "greedy", meaning that they try to match as much of the string as possible. The <code>?</code> character after the quantifier makes the quantifier "non-greedy": meaning that it will stop as soon as it finds a match. For example, given a string like "some &lt;foo&gt; &lt;bar&gt; new &lt;/bar&gt; &lt;/foo&gt; thing":</p>
    <ul>
     <li><code>/&lt;.*&gt;/</code> will match "&lt;foo&gt; &lt;bar&gt; new &lt;/bar&gt; &lt;/foo&gt;"</li>
     <li><code>/&lt;.*?&gt;/</code> will match "&lt;foo&gt;"</li>
    </ul>
   </td>
  </tr>
  </tbody>
</table><br/>







