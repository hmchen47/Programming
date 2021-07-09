# Module 3: HTML5 file upload and download section


## 3.6 IndexedDB


### 3.6.1 Concepts (part 1)


#### Video: IndexedDB's concepts (part 1)

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V003200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3hpT1PH)


#### Introduction to IndexedDB

IndexedDB is presented as an alternative to the WebSQL Database, which the W3C deprecated on November 18, 2010 (while still available in some browsers, it is no longer in the HTML5 specification). Both are solutions for storage, but they do not offer the same functionalities. WebSQL Database is a relational database access system, whereas __IndexedDB is an indexed table system__.

> From [the W3C specification about IndexedDB](https://www.w3.org/TR/IndexedDB/): "User agents (apps running in browsers) may need to store large numbers of objects locally in order to satisfy off-line data requirements of Web applications. Where WebStorage (as seen in the HTML5 part 1 course -localStorage and sessionStorage) is useful for storing pairs of keys and their corresponding values, IndexedDB provides in-order retrieval of keys, efficient searching of values, and the storage of duplicate values for a key".

The W3C specification provides a concrete API to perform advanced key-value data management that is at the heart of most sophisticated query processors. It does so by using transactional databases to store keys and their corresponding values (one or more per key), and providing a means of traversing keys in a deterministic order. This is often implemented through the use of persistent B-tree data structures which are considered efficient for insertion and deletion, as well as for in-order traversal of very large numbers of data records.

<div style="margin: 10px;">
<p><span style="color: #ff0000;"><strong>To sum up:</strong></span></p>
<ol style="list-style-type: decimal;">
<li><span style="color: #ff0000;"><strong>IndexedDB is a transactional Object Store in which you will be able to<span style="color: #008000;"> store JavaScript objects</span>.</strong></span></li>
<li><span style="color: #ff0000;"><strong>Indexes on some properties of these objects facilitate&nbsp;<span style="color: #008000;">faster retrieval and search</span>.</strong></span></li>
<li><span style="color: #ff0000;"><strong>Applications using IndexedDB can <span style="color: #008000;">work both online and offline</span>.</strong></span></li>
<li><span style="color: #ff0000;"><strong>IndexedDB is transactional: it manages <span style="color: #008000;">concurrent access to data</span>.</strong></span></li>
</ol></div>


__Examples of applications where IndexedDB should be considered__

+ A catalog of DVDs in a lending library.
+ Mail clients, to-do lists, notepads.
+ Data for games: high-scores, level definitions, etc.
+ Google Drive uses IndexedDB extensively...

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3xuB207')"
    src    = "https://bit.ly/3qUQbp8"
    alt    = "google drive uses indexedDB"
    title  = "google drive uses indexedDB"
  />
</figure>


#### External resources

Much of this chapter either builds on or is an adaptation of articles posted on the Mozilla Developer Network (MDN) Web site ([IndexedDB](https://developer.mozilla.org/en-US/docs/IndexedDB), [Basic Concepts of IndexedDB](https://developer.mozilla.org/en-US/docs/IndexedDB/Basic_Concepts_Behind_IndexedDB) and [Using IndexedDB](https://developer.mozilla.org/en-US/docs/IndexedDB/Using_IndexedDB)).

+ [W3C specification about IndexedDB](https://www.w3.org/TR/IndexedDB/)
+ [MDN's page about the IndexedDB API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)
+ [Getting Started with Persistent Offline Storage with IndexedDB](https://bit.ly/3hoTemr)

[Current support](https://caniuse.com/#search=indexed) is excellent both on mobile and desktop browsers.


#### Notes for 3.6.1 Concepts (part 1)

+ IndexedDB
  + a front end NoSQL database
  + an alternative to the WebSQL Database, deprecated by 2010-11-18
    + WebSQL Database:
      + a relational database access system
      + useful for storing pairs of keys and their corresponding values
    + IndexedDB:
      + an indexed table system
      + providing in-order retrieval of keys, efficient searching of values, and the storage of duplicate values for a key
  + requirement: user agents (apps running in browsers) probably requiring to store a large numbers of objects locally to satisfy off-line data query of Web applications
  + databases
    + Object Stores
    + w/ a name and attached to a "domain"
  + sharing features of full SQL databases (transactions, indexes, ,,,) and of `LocalStorage` (key=value pairs)
  + values: fill JavaScript objects
  + indexing system based on object properties for faster retrieval and search
  + example: `{firstName: 'Michel', lastName: 'Buffa'}`
  + designed to work w/ huge amount of data
  + __asynchronous__ (callbacks for each operation): CALLBACKS EVERYWHERE!
  + WC3 spec. providing a concrete API to perform advanced key-value data management
    + data management at the heart of most sophisticated query processors
    + using transactional databases to store keys and their corresponding values (one or more per key)
    + providing a means of traversing keys in a deterministic order
    + often implemented through the use of B-tree data structures
    + B-tree: considered efficient for inertion and deletion, as well as for in-order traversal of vary large numbers of data records
  + sample applications:
    + Google Drive
    + Guitar pedalbord
    + examples form from the courses
    + PS4/XBox One/Windows desktop or car dashboard

+ Summary of IndexedDB
  + IndexedDB: a transactional Object Store where able to store JavaScript objects
  + indexes on same properties of these objects facilitate faster retrieval and search
  + applications using IndexedDB able to work both online and offline
  + IndexedDB transactional: managing concurrent access to data

+ Resources
  + [IndexedDB API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)
  + [IndexedDB key characteristics and basic terminology](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology)
  + [Using IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB)
  + [W3C Indexed Database API](https://www.w3.org/TR/IndexedDB/)
  + R. Dabler, [Getting Started with Persistent Offline Storage with IndexedDB](https://bit.ly/3hoTemr)


### 3.6.2 Concepts (part 2)


#### Video: IndexedDB's concepts (part 2)

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V003100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/36nEMET)


IndexedDB is very different from SQL databases, but don't be afraid if you've only used SQL databases: IndexedDB might seem complex at first sight, but it really isn't.

Let's quickly look at the main concepts of IndexedDB, as we will go into detail later on:

+ IndexedDB stores and retrieves objects which are indexed by a "key".
+ Changes to the database happen [within transactions](https://en.wikipedia.org/wiki/Database_transaction).
+ IndexedDB follows a [same-origin policy](https://www.w3.org/Security/wiki/Same_Origin_Policy). So while you can access stored data within a domain, you cannot access data across different domains.
+ It makes extensive use of an asynchronous API: most processing will be done in callback functions - and we mean _LOTS of callback functions_!


#### Detailed overview

__IndexedDB databases store key-value pairs.__ The values can be complex structured objects (hint: think in terms of JSON objects), and keys can be properties of those objects. You can create indexes that use any property of the objects for faster searching, as well as ordering results.

Example of data (we reuse a sample from this MDN tutorial: "[Using IndexedDB](https://developer.mozilla.org/en-US/docs/IndexedDB/Using_IndexedDB)"):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// This is what our customer data looks like.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">const</span><span class="pln"> customerData </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">{</span><span class="pln"> ssn</span><span class="pun">:</span><span class="pln"> </span><span class="str">"444-44-4444"</span><span class="pun">,</span><span class="pln"> name</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Bill"</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="pln"> </span><span class="lit">35</span><span class="pun">,</span><span class="pln"> email</span><span class="pun">:</span><span class="pln"> </span><span class="str">"bill@company.com"</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">{</span><span class="pln"> ssn</span><span class="pun">:</span><span class="pln"> </span><span class="str">"555-55-5555"</span><span class="pun">,</span><span class="pln"> name</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Donna"</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="pln"> </span><span class="lit">32</span><span class="pun">,</span><span class="pln"> email</span><span class="pun">:</span><span class="pln"> </span><span class="str">"donna@home.org"</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">];</span></li>
</ol></div>

Where `customerData` is an array of  "customers", each customer having several properties: `ssn` for the social security number, a `name`, an `age` and an `email` address.

__IndexedDB is built on a transactional database model.__ Everything you do in IndexedDB happens in [the context of a transaction](https://developer.mozilla.org/en-US/docs/IndexedDB/Basic_Concepts_Behind_IndexedDB#gloss_transaction). The IndexedDB API provides lots of objects that represent indexes, tables, cursors, and so on, but each is tied to a particular transaction. Thus, you cannot execute commands or open cursors outside a transaction.

Example of a transaction:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Open a transaction for reading and writing on the DB "customer"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> transaction </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">([</span><span class="str">"customers"</span><span class="pun">],</span><span class="pln"> </span><span class="str">"readwrite"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// Do something when all the data is added to the database.</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">transaction</span><span class="pun">.</span><span class="pln">oncomplete </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">"All done!"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">transaction</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Don't forget to handle errors!</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// Use the transaction to add data...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln"> transaction</span><span class="pun">.</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="kwd">in</span><span class="pln"> customerData</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> objectStore</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">customerData</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// event.target.result == customerData[i].ssn</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Transactions have a well-defined lifetime. Attempting to use a transaction after it has completed throws an exception.

_Transactions auto-commit, and cannot be committed manually._

This transaction model is really useful when you consider what might happen if a user opened two instances of your web app in two different tabs simultaneously. Without transactional operations, the two instances might stomp all over each others' modifications. 

__The IndexedDB API is mostly asynchronous.__ The API doesn't give you data by returning values; instead, you have to pass a callback function. You don't "store" a value in the database, or "retrieve" a value out of the database through synchronous means. Instead, you "request" that a database operation happens. You are notified by a DOM event when the operation finishes, and the type of event lets you know if the operation succeeded or failed. This may sound a little complicated at first, but there are some sanity measures baked-in. After all, you are a JavaScript programmer, aren't you? ;-)

So, please review the previous code extracts noting: `transaction.oncomplete`, `transaction.onerror`, `request.onsuccess`, etc.

__IndexedDB uses requests all over the place.__ Requests are objects that receive the success or failure DOM events mentioned previously. They have `onsuccess` and `onerror` properties, and you can call `addEventListener()` and `removeEventListener()` on them. They also have `readyState`, `result`, and `errorCode` properties which advise the status of a request.

The `result` property is particularly magical, as it can be many different things, depending on how the request was generated (for example, an `IDBCursor` instance, or the key for a value that you just inserted into the database). We will see this in detail during a future lecture: "Using IndexedDB".

__IndexedDB uses DOM events to notify you when results are available.__ DOM events always have a `type` property (in IndexedDB, it is most commonly set to "`success`" or "`error`"). DOM events also have a `target` property that shows where the event is headed. In most cases, the `target` of an event is the `IDBRequest` object that was generated as a result of doing some database operation. Success events don't bubble up and they can't be cancelled. Error events, on the other hand, do bubble, and can be cancelled. This is quite important, as error events abort the transaction, unless they are cancelled.

__IndexedDB is object-oriented.__ IndexedDB is not a relational database, which has tables with collections of rows and columns. This important and fundamental difference affects the way you design and build your applications. IndexedDB is an Object Store!

In a traditional relational data store, you would have a table that stores a collection of rows of data and columns of named types of data. IndexedDB, on the other hand, requires you to create an object store for a type of data and simply persist JavaScript objects to that store. Each object store can have a collection of indexes (corresponding to the properties of the JavaScript object you store in the store) that enable efficient querying and iteration.

__IndexedDB does not use Structured Query Language (SQL).__ It phrases a query in terms of an index, that produces a cursor, which you use to iterate through the result set. If you are not familiar with NoSQL systems, read [the Wikipedia article on NoSQL](https://en.wikipedia.org/wiki/NoSQL).

__IndexedDB adheres to a same-origin policy.__ An origin consists of the domain, the application layer protocol, and the port of a URL of the document where the script is being executed. Each origin has its own associated set of databases. Every database has a name that identifies it within an origin. Think of it as: "an application + a Database".

The concept of "same origin" is defined by the combination of all three components mentioned earlier (domain, protocol, port). For example, an app in a page with the URL `https://www.example.com/app/`, and a second app at `https://www.example.com/dir/`, may both access the same IndexedDB database because they have the same origin (https, example.com, and 80). Whereas apps at `https://www.example.com:8080/dir/` (different port) or `https://www.example.com/dir/` (different protocol), do not satisfy the same origin criteria (port or protocol differ from `https://www.example.com`)

See this article from MDN about the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) for further details and examples.







