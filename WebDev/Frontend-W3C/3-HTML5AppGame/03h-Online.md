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

<div><ol>
<li value="1">// Load a binary file from a URL as an ArrayBuffer.</li>
<li>function loadSoundFile(url) {</li>
<li>&nbsp;&nbsp;var xhr = new XMLHttpRequest();</li>
<li>&nbsp; xhr.open('GET', url, true);</li>
<li>&nbsp;</li>
<li>&nbsp; xhr.responseType = 'arraybuffer';&nbsp;</li>
<li> </li>
<li>&nbsp; xhr.onload = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp;initSound(this.response);&nbsp;</li>
<li>&nbsp;&nbsp;};</li>
<li>&nbsp;</li>
<li>&nbsp; xhr.send();</li>
<li>}</li>
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

<div><ol>
<li value="1">&lt;progress id="downloadProgress" value=0&gt;&lt;progress&gt;</li>
</ol></div>

JavaScript:

<div><ol>
<li value="1">....</li>
<li>// progress element</li>
<li>var progress = document.querySelector('#downloadProgress');</li>
<li> </li>
<li>...</li>
<li>&nbsp;</li>
<li>function downloadSoundFile(url) {</li>
<li>&nbsp;&nbsp;var xhr = new XMLHttpRequest();</li>
<li>&nbsp; xhr.open('GET', url, true);</li>
<li> </li>
<li>&nbsp;&nbsp;...</li>
<li>&nbsp;&nbsp;// Monitor progress by updating the progress element</li>
<li>&nbsp; xhr.<span style="color: #ff0000;"><strong>AAA</strong>&nbsp;= function(e) {</li>
<li>&nbsp; &nbsp; progress.value = e.<span style="color: #ff0000;"><strong>BBB</strong>;</li>
<li>&nbsp; &nbsp; progress.max = e.<span style="color: #ff0000;"><strong>CCC</strong>;</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp; xhr.send();</li>
<li>}</li>
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

<div><ol>
<li value="1">&lt;ol ondragstart="dragStartHandler(event)"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;li data-value="fruit-apple"&gt;Apples&lt;/li&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;li data-value="fruit-orange"&gt;Oranges&lt;/li&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;li data-value="fruit-pear"&gt;Pears&lt;/li&gt;</li>
<li>&lt;/ol&gt;</li>
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
  c. We need to wrap `<span draggable=true>...` around the selected text<br>

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

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li> &lt;/head&gt;</li>
<li> &lt;script&gt;</li>
<li> function dragLeaveHandler(event) {</li>
<li>&nbsp; &nbsp; ...</li>
<li> }</li>
<li> function dragEnterHandler(event) {</li>
<li>&nbsp; &nbsp;...</li>
<li> }</li>
<li> function dragOverHandler(event) {</li>
<li>&nbsp; &nbsp; event.stopPropagation();</li>
<li>&nbsp; &nbsp; event.preventDefault();</li>
<li> }</li>
<li> function dropHandler(event) {</li>
<li>&nbsp; &nbsp; event.stopPropagation();</li>
<li>&nbsp; &nbsp; event.preventDefault();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;var files = event.dataTransfer.files;</li>
<li>&nbsp; &nbsp; ...</li>
<li> }</li>
<li> ...</li>
<li> &lt;/script&gt;</li>
<li> &lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;h2&gt;Drop your files here!&lt;/h2&gt;</li>
<li> &lt;div id="droppableZone" ondragenter="dragEnterHandler(event)" ondrop="dropHandler(event)" </li>
<li> ondragover="dragOverHandler(event)" ondragleave="dragLeaveHandler(event)"&gt;</li>
<li> Drop zone</li>
<li> &lt;ol id="droppedFiles"&gt;&lt;/ol&gt;</li>
<li> &lt;/div&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;html&gt;</li>
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



### 3.8.4 IndexedDB (15-26)

15. What is IndexedDB?

  IndexedDB is: (3 correct answers.)

  a. a relational database located in the browser<br>
  b. an indexed table system<br>
  c. designed for managing concurrent access to data<br>
  d. using SQL for manipulating data<br>
  e. a transactional object store in which you can store JavaScript objects<br>

  Ams: bce<br>
  Explanation: IndexedDB is a transactional database which supports indexes. Each database can contain object stores. IndexedDB is an indexed table system and therefore designed to manage concurrent access to data.


16. We're only interested in high-value transactions...

  A transaction is:

  a. a term used when we store money in a database and transfer it from one account to another, for example.<br>
  b. an atomic set of data-access and data-modification operations against a particular database. Either they all succeed or all fail.<br>
  c. a name we give to an operation that manipulates data in the database.<br>

  Ams: b<br>
  Explanation: IndexedDB is a transactional database which supports indexes. Each database can contain object stores. IndexedDB is an indexed table system and therefore designed to manage concurrent access to data.


17. All together now

  What particular object related to IndexedDB manages concurrent access to data?

  a. The transaction<br>
  b. The request<br>

  Ams: a<br>
  Explanation: The transaction is the mechanism that prevents data from being corrupted during concurrent access, in particular when multiple write operations occur.


18. Any last requests?

  IndexedDB requests for creating, updating, deleting or searching data are:

  a. Asynchronous<br>
  b. Synchronous<br>

  Ams: a<br>
  Explanation: All requests are always asynchronous. Results or errors are processed in callback functions.


19. Always transactional?

  IndexedDB requests for creating, updating, deleting or searching data:

  a. are completed within a transaction<br>
  b. can be done without a transaction, for better performance<br>

  Ams: a<br>
  Explanation: All requests take place in a transaction.


20. Here is my Id

Each IndexedDB database must have...

  a. data in it<br>
  b. a name and a version<br>
  c. a name<br>

  Ams: b<br>
  Explanation: Each indexedDB database must have a name and a version.


<hr>

__Source code for the next 3 questions (21, 22 and 23)__

<div><ol>
<li value="1">var db;&nbsp;</li>
<li>&nbsp;</li>
<li>function createDatabase() {</li>
<li>&nbsp;&nbsp;if(!window.indexedDB) {</li>
<li>&nbsp; &nbsp; &nbsp;window.alert("Your browser does not support a stable version </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;of IndexedDB");</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;var customerData = [</li>
<li>&nbsp; &nbsp; { ssn: "444-44-4444", name: "Bill", age: 35, email: </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"bill@company.com" },</li>
<li>&nbsp; &nbsp;&nbsp;{ ssn: "555-55-5555", name: "Donna", age: 32, email: </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"donna@home.org" }</li>
<li>&nbsp;&nbsp;];</li>
<li>&nbsp;&nbsp;var&nbsp;n&nbsp;= "MyCustomers";</li>
<li></li>
<li>&nbsp;&nbsp;var request = indexedDB.open(n, 2);</li>
<li> </li>
<li>&nbsp; request.onerror = function(event) {</li>
<li>&nbsp; &nbsp; &nbsp;console.log("request.onerror" + event.target.errorCode);</li>
<li>&nbsp;&nbsp;};</li>
<li>&nbsp; request.onupgradeneeded = function(event) {</li>
<li>&nbsp; &nbsp; &nbsp; db = event.target.result;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var objectStore = db.createObjectStore("customers", </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{ keyPath: "ssn" });</li>
<li>&nbsp; &nbsp; &nbsp; objectStore.createIndex("name", "name", { unique: false });</li>
<li>&nbsp; &nbsp; &nbsp; objectStore.createIndex("email", "email", { unique: true });</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// Store values in the newly created objectStore.</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;for (var i in customerData) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; objectStore.add(customerData[i]);</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;}; // end of request.onupgradeneeded</li>
<li> </li>
<li>&nbsp; request.onsuccess = function(event) {</li>
<li>&nbsp; &nbsp; &nbsp;console.log("request.onsuccess, database opened, now we can add</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; / remove / look for data in it!");</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// The result is the database itself</li>
<li>&nbsp; &nbsp; &nbsp;db = event.target.result; </li>
<li>&nbsp;&nbsp;};</li>
<li>} // end of function createDatabase</li>
</ol></div>

21. Database name?

What is the name of the database we create/open? Enter exactly the right name.

  Ams: MyCustomers<br>
  Explanation: The database name is at line 14. It is MyCustomers.


22. Who are they?

  What is the name of the object store? Enter exactly the right name.

  Ams: customers<br>
  Explanation: The object store name is at line 23. It is customers.


23. KeyPath?

  What is the name of the keypath (equivalent to primary key)? Enter exactly the right name.

  Ams: ssn<br>
  Explanation: The keypath is the social security number ssn, occuring at line 23.


24. Index me please!

  What is an index?

  a. A faster means of looking for data using a property of the objects (looking for a person by email will be much faster if email is indexed)<br>
  b. If a stored object has a property named "index" then we can use it to gain faster access to the object, using a means other than the keypath<br>

  Ams: a<br>
  Explanation: An index allows the user to look up records in an object store using the properties of the values in the object store's records. Indexes are a common concept in databases. They can speed up object retrieval and allow multi-criterion searches. For example, it will be much quicker to find a particular person by email if you store persons in your object store, and add an index on the "email" property of each person.


25. Multiple me?

  If we have multiple objects which hold the same value for some property, eg: `favoriteColor="green"`, can we index that property? (Yes/No)

  Ams: Yes<br>
  Explanation: Yes! This is the case for the "name" index in the previous source code. KeyPath, on the other hand, must be unique.


26. Multiple results how to...

  When we look for objects and get a collection of results, how can we iterate over this result?

  a. Result is a JavaScript object. We can iterate on the array like we do on any JavaScript array.<br>
  b. Using a cursor<br>
  c. Using an index<br>

  Ams: b<br>
  Explanation: A cursor is the mechanism for iterating over multiple records within a key range. The cursor has a source that indicates which index or object store it is currently presenting. It has a position within the range, and moves in a direction that is increasing or decreasing in the order of record keys.




