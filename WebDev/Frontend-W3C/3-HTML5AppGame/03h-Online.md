# Module 3: HTML5 file upload and download section


## 3.8 Exercises - Module 3 (26 Questions)


### 3.8.1 Ajax and XHR2 (1-6)

1. Is XHR2 twice as good?

  XHR2 improved upon the "old way" of using Ajax. Which of the following improvements came with XHR2? (3 correct answers._

  a. Data transfer is faster than before<br>
  b. The syntax has been simplified<br>
  c. Encoding / decoding of binary files is done directly within the browser<br>
  d. Progress monitoring for uploads and downloads is now possible without polling the server<br>
  e. Native support for multimedia files<br>
  
  Ans: bcd<br>
  Explanation: XHR2 improvements include: New, easier to use syntax, Encoding / decoding of binary files performed directly by the browser, Progress monitoring for uploads and downloads is possible without querying the server.


<hr>

__Source code for the next question (2)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Load a binary file from a URL as an ArrayBuffer.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> loadSoundFile</span><span class="pun">(</span><span class="pln">url</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">responseType </span><span class="pun">=</span><span class="pln"> </span><span class="str">'arraybuffer'</span><span class="pun">;</span><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;initSound</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">response</span><span class="pun">);</span><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

2. Array of buffers? ArrayBuffer? A ray buffed air?

  What is line 6 useful for?

  a. It indicates that we want the browser to decode into some binary format, the text-encoded data received from the server.<br>
  b. arrayBuffer is the name of the variable where the requested data will be stored.<br>
  
  Ans: a<br>
  Explanation: With XHR2, you can ask the browser to decode the file you send/receive natively. To do this, when you use an `XMLHttpRequest` to send or receive a file, you need to specify the type of file with a value equal to `arrayBuffer`.



<hr>

__Source code for the next 3 questions (3, 4 and 5)__

HTML:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;progress</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"downloadProgress"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">0</span><span class="tag">&gt;&lt;progress&gt;</span></li>
</ol></div>

JavaScript:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">....</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// progress element</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> progress </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#downloadProgress'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> downloadSoundFile</span><span class="pun">(</span><span class="pln">url</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Monitor progress by updating the progress element</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.<span style="color: #ff0000;"><strong>AAA</strong></span></span><span class="pln">&nbsp;</span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; progress</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.<span style="color: #ff0000;"><strong>BBB</strong></span></span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; progress</span><span class="pun">.</span><span class="pln">max </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.<span style="color: #ff0000;"><strong>CCC</strong></span></span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

3. Fill in the blank (1/3)

  What would you write instead of the AAA placeholder in the above code? Use lowercase letters please.

  Ans: `onprogress`<br>
  Explanation: `xhr.onprogress` is the correct answer. For an upload it would have been `xhr.upload.onprogress`


4. Fill in the blank (2/3)

  What would you write instead of the BBB placeholder in the above code? Use lowercase letters please.

  Ans: `loaded`<br>
  Explanation: The `loaded` property of the progress event is the correct answer.


5. Fill in the blank (3/3)

  What would you write instead of the CCC placeholder in the above code? Use lowercase letters please.

  Ans: `total`<br>
  Explanation: The `total` property of the progress event is the correct answer.


6. Give me a bag to put all these parts together!

  What object, introduced during the course, is used when sending a multipart form?

  a. The `serializeArray(form)` function<br>
  b. The `FormData` object type<br>
  c. The `arrayBuffer` type<br>

  Ans: b<br>
  Explanation: A `FormData` object is a container for parts in the multipart data that will be sent by an XHR2 POST request. If we create the `FormData` like this: `var data = new FormData(form);` where `form` is the HTML form, then `data` will contain all the input fields' values. We can add files to this object using the `data.append(name, value)` method.


### 3.8.2 Drag and Drop (7-11)

__Source file for the next question (7)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;ol</span><span class="pln"> </span><span class="atn">ondragstart</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dragStartHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-apple"</span><span class="tag">&gt;</span><span class="pln">Apples</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-orange"</span><span class="tag">&gt;</span><span class="pln">Oranges</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-pear"</span><span class="tag">&gt;</span><span class="pln">Pears</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/ol&gt;</span></li>
</ol></div>


7. Drag me or drag me not...

  We would like to drag the list items from the above code. Is it going to work? (let's assume that the dragstart event listener is ok). (No/Yes)

  Ans: No<br>
  Examplantion: You must add the `draggable="true"` attribute to all list items to be able to use them in a Drag and Drop operation.


8. Where is my clipboard?

  When we drag an object from the DOM (an HTML element)...

  a. we need to explicitly copy the data we want to process later (when we drop the object...) into the drag and drop clipboard.<br>
  b. it is automatically copied onto the drag and drop clipboard.<br>

  Ans: a<br>
  Examplantion:
    + In the `dragstart` handler, when a draggable element has been dragged, we need to copy some data related to the dragged object to the drag and drop clipboard for later use.
    + When a value is copied to this clipboard, a key/name must be given. Data copied to the clipboard is associated with this name. Using this name, we can get back the data when the object is dropped, in the drop event handler.


9. Visual feedback

  How can we add visual feedback when dragging and dropping elements (this inludes also "when the mouse cursor goes over elements while dragging")? (3 correct answers.)

  a. We should change the CSS style of draggable elements when the mouse cursor goes over them<br>
  b. The above is not necessary: the draggable elements are highlighted automatically when the mouse cursor goes over them<br>
  c. We can listen to the `dragstart`, `dragend`, `dragover`, `dragenter`, `dragleave` events (by adding listeners to the HTML element that is a drop zone), and change some CSS values styling the drop zone<br>
  d. We can customize the mouse cursor in drag and drop related listeners,<br>
  e. The `droppable=true` attribute, when added to a drop zone, automatically highlights the element when the cursor enters its area, while dragging an element.<br>

  Ans: acd<br>
  Examplantion: All answers are true except those which claim that elements are automatically highlighted when the mouse cursor hovers over them. In the course, we listened to for all sorts of events related to drag and drop: `dragstart`, `drop`, `dragenter`, `dragleave`, `dragover`... and in the corresponding listeners we changed the appearance of the mouse cursor and varied the CSS properties of the elements. The cursor can be modified using the `event.dataTransfer.effectAllowed` and `event.dataTransfer.dropEffect` and `event.dataTransfer.setDragImage` methods, in listeners.


10. Image drag

  Which of the following statements is true?

  a. If the image `src` attribute value is an external URL, it's not possible to drag and drop the image<br>
  b. `img` HTML elements are all draggable by default - there is no need to add a `draggable="true"` attribute<br>
  c. There is no need to use a `dragstart` event listener on`<img>` elements, in order to move them (using drag and drop) from one location to another within a document<br>

  Ans: b<br>
  Examplantion: Images are draggable by default.


11. Drag and drop a text selection

  What is unique about dragging and dropping a text selection?

  a. The text in the selection is automatically copied to the drag and drop clipboard, with the key "text/plain", so there is no need for a `dragstart` event handler<br>
  b. We need to get the selection in the `dragstart` event handler and copy the text to the clipboard with a key equal to "text/plain"<br>
  c. We need to wrap `<span draggable=true>...</span>` around the selected text<br>

  Ans: a<br>
  Examplantion: There is no need to add a `dragstart` handler on an element that contains text. Any selected text is automatically added to the clipboard with a name/key equal to "text/plain". Add a drop event handler on the drop zone and fetch the data from the clipboard using "text/plain" as the access key.


### 3.8.3 Drag and drop: working with files (12-15)

12. Drop a media file and see what happens

  When an image or media file is dropped onto a standard page open in the browser, what will happen?

  a. The image will be displayed in another tab or replace the current page, it depends on the browser. A media file will be played with a default player in the middle of a new page, etc.<br>
  b. Nothing<br>
  
  Ans: a<br>
  Explanation: Dropping a media file usually results in the browser displaying it or playing it with a default player.


<hr>

__Source code for the next 2 questions (13 and 14)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> dragLeaveHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;">&nbsp; &nbsp; ...</li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> dragEnterHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;">&nbsp; &nbsp;...</li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> dragOverHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">stopPropagation</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">preventDefault</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> dropHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">stopPropagation</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">preventDefault</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> files </span><span class="pun">=</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">dataTransfer</span><span class="pun">.</span><span class="pln">files</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; ...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">...</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h2&gt;</span><span class="pln">Drop your files here!</span><span class="tag">&lt;/h2&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"droppableZone"</span><span class="pln"> </span><span class="atn">ondragenter</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dragEnterHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="atv">"</span><span class="pln"> </span><span class="atn">ondrop</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dropHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="atv">"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="atn">ondragover</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dragOverHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="atv">"</span><span class="pln"> </span><span class="atn">ondragleave</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dragLeaveHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> Drop zone</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;ol</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"droppedFiles"</span><span class="tag">&gt;&lt;/ol&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/div&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;html&gt;</span></li>
</ol></div>

13. Please stop. I said stop!

The above code handles file drops in a drop zone. What are _lines 12-13_ and _16-17_ useful for?

  a. By default the browser would display/play media files in a new window/tab. They prevent the browser's default behavior, and stop the propagation of the event to the parents of the drop zone element.<br>
  b. They are just here for performance reasons, if we omit them the application will still work.<br>

  Ans: a<br>
  Explanation: We prevent the browser default behavior in the drop and dragover handlers, otherwise when we drop a media file (an image, an audio or video file), the browser will display/play it in a new window/tab. We also stop the propagation for performance reasons, because when we move a dragged object it will raise many events to the parents of the drop zone element.


14. Files or files?

  When we work with an `<input type="file">` input field, the selected files can be obtained in the files property of the field DOM object. Is this the same kind of object we have in `event.dataTransfer.files`? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, we obtain a collection of file descriptors. If we drop images, for example, or if we select them using an input type="file", we will be able to process them with the same function.









