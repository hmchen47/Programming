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
<p><span style="color: #ff8800;"><strong style="color: red;">To sum up:</strong></span></p>
<ol style="list-style-type: decimal;">
<li><span style="color: #ff8800;"><strong style="color: red;">IndexedDB is a transactional Object Store in which you will be able to<span style="color: #008000;"> store JavaScript objects</span>.</strong></span></li>
<li><span style="color: #ff8800;"><strong style="color: red;">Indexes on some properties of these objects facilitate&nbsp;<span style="color: #008000;">faster retrieval and search</span>.</strong></span></li>
<li><span style="color: #ff8800;"><strong style="color: red;">Applications using IndexedDB can <span style="color: #008000;">work both online and offline</span>.</strong></span></li>
<li><span style="color: #ff8800;"><strong style="color: red;">IndexedDB is transactional: it manages <span style="color: #008000;">concurrent access to data</span>.</strong></span></li>
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

+ IndexedDB overview
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
  + sharing features of full SQL databases (transactions, indexes, ...) and of `LocalStorage` (key-value pairs)
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

<strong style="color: red;">IndexedDB databases store key-value pairs.</strong> The values can be complex structured objects (hint: think in terms of JSON objects), and keys can be properties of those objects. You can create indexes that use any property of the objects for faster searching, as well as ordering results.

Example of data (we reuse a sample from this MDN tutorial: "[Using IndexedDB](https://developer.mozilla.org/en-US/docs/IndexedDB/Using_IndexedDB)"):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// This is what our customer data looks like.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">const</span><span class="pln"> customerData </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">{</span><span class="pln"> ssn</span><span class="pun">:</span><span class="pln"> </span><span class="str">"444-44-4444"</span><span class="pun">,</span><span class="pln"> name</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Bill"</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="pln"> </span><span class="lit">35</span><span class="pun">,</span><span class="pln"> email</span><span class="pun">:</span><span class="pln"> </span><span class="str">"bill@company.com"</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">{</span><span class="pln"> ssn</span><span class="pun">:</span><span class="pln"> </span><span class="str">"555-55-5555"</span><span class="pun">,</span><span class="pln"> name</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Donna"</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="pln"> </span><span class="lit">32</span><span class="pun">,</span><span class="pln"> email</span><span class="pun">:</span><span class="pln"> </span><span class="str">"donna@home.org"</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">];</span></li>
</ol></div>

Where `customerData` is an array of  "customers", each customer having several properties: `ssn` for the social security number, a `name`, an `age` and an `email` address.

<strong style="color: red;">IndexedDB is built on a transactional database model.</strong> Everything you do in IndexedDB happens in [the context of a transaction](https://developer.mozilla.org/en-US/docs/IndexedDB/Basic_Concepts_Behind_IndexedDB#gloss_transaction). The IndexedDB API provides lots of objects that represent indexes, tables, cursors, and so on, but each is tied to a particular transaction. Thus, you cannot execute commands or open cursors outside a transaction.

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

<strong style="color: red;">The IndexedDB API is mostly asynchronous.</strong> The API doesn't give you data by returning values; instead, you have to pass a callback function. You don't "store" a value in the database, or "retrieve" a value out of the database through synchronous means. Instead, you "request" that a database operation happens. You are notified by a DOM event when the operation finishes, and the type of event lets you know if the operation succeeded or failed. This may sound a little complicated at first, but there are some sanity measures baked-in. After all, you are a JavaScript programmer, aren't you? ;-)

So, please review the previous code extracts noting: `transaction.oncomplete`, `transaction.onerror`, `request.onsuccess`, etc.

<strong style="color: red;">IndexedDB uses requests all over the place.</strong> Requests are objects that receive the success or failure DOM events mentioned previously. They have `onsuccess` and `onerror` properties, and you can call `addEventListener()` and `removeEventListener()` on them. They also have `readyState`, `result`, and `errorCode` properties which advise the status of a request.

The `result` property is particularly magical, as it can be many different things, depending on how the request was generated (for example, an `IDBCursor` instance, or the key for a value that you just inserted into the database). We will see this in detail during a future lecture: "Using IndexedDB".

<strong style="color: red;">IndexedDB uses DOM events to notify you when results are available.</strong> DOM events always have a `type` property (in IndexedDB, it is most commonly set to "`success`" or "`error`"). DOM events also have a `target` property that shows where the event is headed. In most cases, the `target` of an event is the `IDBRequest` object that was generated as a result of doing some database operation. Success events don't bubble up and they can't be cancelled. Error events, on the other hand, do bubble, and can be cancelled. This is quite important, as error events abort the transaction, unless they are cancelled.

<strong style="color: red;">IndexedDB is object-oriented.</strong> IndexedDB is not a relational database, which has tables with collections of rows and columns. This important and fundamental difference affects the way you design and build your applications. IndexedDB is an Object Store!

In a traditional relational data store, you would have a table that stores a collection of rows of data and columns of named types of data. IndexedDB, on the other hand, requires you to create an object store for a type of data and simply persist JavaScript objects to that store. Each object store can have a collection of indexes (corresponding to the properties of the JavaScript object you store in the store) that enable efficient querying and iteration.

<strong style="color: red;">IndexedDB does not use Structured Query Language (SQL).</strong> It phrases a query in terms of an index, that produces a cursor, which you use to iterate through the result set. If you are not familiar with NoSQL systems, read [the Wikipedia article on NoSQL](https://en.wikipedia.org/wiki/NoSQL).

<strong style="color: red;">IndexedDB adheres to a same-origin policy.</strong> An origin consists of the domain, the application layer protocol, and the port of a URL of the document where the script is being executed. Each origin has its own associated set of databases. Every database has a name that identifies it within an origin. Think of it as: "an application + a Database".

The concept of "same origin" is defined by the combination of all three components mentioned earlier (domain, protocol, port). For example, an app in a page with the URL `https://www.example.com/app/`, and a second app at `https://www.example.com/dir/`, may both access the same IndexedDB database because they have the same origin (https, example.com, and 80). Whereas apps at `https://www.example.com:8080/dir/` (different port) or `https://www.example.com/dir/` (different protocol), do not satisfy the same origin criteria (port or protocol differ from `https://www.example.com`)

See this article from MDN about the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) for further details and examples.


#### Notes for 3.6.2 Concepts (part 2)

+ Main concepts of IndexedDB
  + store and retrive objects indexed by a key
  + transaction: changes to the databases
  + same-origin policy: only accessing data within the same domain, not able to access across domains
  + extensive use of an asynchronous API: most processing done in callback functions

+ Keypath
  + a must-have property defined by object stores
  + equivalent to Primary key in relational database
  + unique
  + able to be explicit (ssn) or implicit (auto-incremented primary key in SQL) 
  + implicit KeyPath: not appeared in the stored objects themselves
  + stored objects w/o a rigidly defined schema
  + only key to be shared, other keys probably varying btw stored objects
  + example: `{firstName: 'Michel', lastName: 'Buffa', ssn: "1122334455"}` $\to$ ssn as Keypath

+ Indexes
  + stored object able to have one or more indexes $\to$ faster searching
  + a common concept in database
  + unique or non-unique
  + making lookup possible using any arbitrary property of the store objects
  + speeding up object retrieval and allowing multi-criteria searches
  + possible to have non unique indexes $\to$ all matching objects
  + example: "lastName" property of each person as an index $\to$ make search faster for some persons by "lastName"

+ Transaction
  + transactional database: ensuring concurrent access to data not compromised
  + using "locking system" to prevent compromising
  + scenarios to lock system
    + multiple tabs opened on the same WebApp (same domain)
    + multiple apps running "out of traditional browser" (game console, windows desktop, etc.)

+ Key-value pairs
  + IndexedDB storing key-value pairs
  + values: complex objects (think of JSON objects)
  + keys: properties of the objects
  + creating indexes w/ any property of the objects for faster searching and ordering results
  + example: 
    + declare key-value pairs<a name="cxData"></a>: `const customerData = [{ ssn: "444-44-4444", name: "Bill", age: 35, email: "bill@company.com" }, { ssn: "555-55-5555", name: "Donna", age: 32, email="donna@home.org" }];`
    + `customerData`: an array of "customers"
    + customer properties: `ssn` for social security number, a `name`, an `age` and an `email` address

+ IndexedDB and transaltion model
  + IndexedDB built on a transactional database model
  + operations in IndexedDB $\to$ operated in the context of a transaction
  + IndexedDB API providing lots of objects representing indexes, tables, cursors, etc.
  + API tied to a particular transaction
  + unable to execute commands or open cursors outside a transaction
  + transaction committed automatically, unable to committ manually
  + useful when considering what might happen if a user opened two of the web apps in two different tabs simultaneously

+ Typical syntax of a transaction
  + open a transaction for reading and writing  on the DB "customer": `var transaction = db.transaction("customers", "readwrite");`
  + add complete listener: `transaction.oncomplete = function(evt) { alert("All done!"); };`
  + add error listener: `transaction.onerror = function(evt) { // error handling };`
  + access data<a name="objStore"></a>: `var objectStore = transaction.objectStore("costomers");`
  + iterate through to add data<a name="addData"></a>: `for (var i in customerData) {...}`
    + add data: `var request = objectStore.add(customerData[i]);`
    + add success listener: `request.onsuccess = function(evt) { // evt.target.result === customerData[i].ssn };`

+ IndexedDB API and asynchronous
  + most IndexedDB API asynchronous
  + API not providing returned data but passed a callback function
  + not "store" a value or "retrieve" a value out of the database but "request" that a database operation happens
  + database system notifying caller via a DOM event once operation done
  + the type of event specifying the success or failure of the operation
  + examples: `transaction.oncomplete`, `transaction.onsuccess`, `request.onerror`, etc.

+ IndexedDB and requests
  + requests:
    + objects receiving the success or failure DOM events
    + `onsuccess` and `onerror` properties
  + using `addEventListener()` and `removeEventListener()` to add and remove listeners
  + status of a request: `readyState`, `result`, and `errorCode`
  + meaning of `result` depending on how the request was generated, e.g., `IDBCursor` instance or the key for a value

+ IndexedDB and DOM events
  + IndexedDB using DOM events to notify browser when results available
  + properties of event
    + `type`: always presented, possible values `success` or `error`
    + `target`: showing where the event is headed
  + `IDBRequest` object:
    + the most common value of the `target` of an event
    + generated as a result of doing some database operation
  + success events: neither bubbled up nor cancelled
  + error events:
    + both bubbled and able to be cancelled
    + abort the transaction, unless cancelled

+ IndexedDB and object-oriented
  + IndexedDB:
    + object-oriented, not a relational database
    + a Object Store
    + creating an object store for a type of data
    + simply persist JavaScript objects to that store
    + object store w/ a collection of indexes to enable efficient querying and iteration
    + indexes: corresponding to the properties of the JavaScript object stored in the store
  + relational database:
    + tables w/ rows and columns
    + having a table to store a collection of rows and columns of named types of data
    + using SQL for query
  + fundamental difference to affect the way to design and build applications

+ Same-origin policy
  + a origin consists of the domain, the application layer protocol, and the port of a URL of the document
  + script exected within the document
  + IndexedDB adheres to a same-origin policy
  + each origin associated to its own set of databases
  + every database having a name to identify itself within the origin
  + concept of "same origin": the combination of all three components, domain, protocol, and port
  + example:
    + an app in page w/ the URL, `https://www.example.com/app/`
    + a second app at `https://www.example.com/dir`
    + booth apps accessing the same IndexedDB batabase $\gets$ the same origin, `https`, `example.com`, and `80`
    + apps at `https://www.example.com:8080/dir` (different port) or `http://www.example.com/dir/` (different protocol) $\to$ not the same origin


### 3.6.3 Definitions

These definitions come from the W3C specification. Please read this page to familiarize yourself with the terms.

#### Database

+ Each [origin](https://www.w3.org/TR/IndexedDB/#dfn-origin) (you may consider as "each application") has an associated set of [databases](https://www.w3.org/TR/IndexedDB/#dfn-database). A database comprises one or more [object stores](https://www.w3.org/TR/IndexedDB/#dfn-object-store) which hold the data stored in the database.
+ Every database has a _name_ that identifies it within a specific origin. The name can be any string value, including the empty string, and stays constant for the lifetime of the database.
+ Each database also has a current version. When a database is first created, its [version](https://www.w3.org/TR/IndexedDB/#dfn-version) is 0, if not specified otherwise.  Each database can only have one version at any given time. A database can't exist in multiple versions at once.
+ The act of opening a database creates _a connection_. There may be multiple [connections](https://www.w3.org/TR/IndexedDB/#dfn-connection) to a given database at any given time.


#### Object store

+ An object store is the mechanism by which data is stored in the database. 
+ Every object store has _a name_. The name is unique within the database to which it belongs.
+ The object store persistently holds records (JavaScript objects), which are key-value pairs. One of these keys is  a kind of "primary key" in the SQL database sense. This "key" is a property that every object in the datastore must contain. Values in the object store are structured, but this structure may vary between objects (i.e., if we store persons in a database, and use the email as "the key all objects must define", some may have first name and last name, others may have an address or no address at all, etc.)
+ Records within an object store are sorted according to [keys](https://developer.mozilla.org/en-US/docs/IndexedDB/Basic_Concepts_Behind_IndexedDB#gloss_key), in ascending order.
+ Optionally, an object store may also have a [key generator](https://www.w3.org/TR/IndexedDB/#dfn-key-generator) and a [key path](https://www.w3.org/TR/IndexedDB/#dfn-object-store-key-path). If the object store has a key path, it is said to use in-line keys. Otherwise, it is said to use _out-of-line keys_.
+ The object store can derive [the key](https://www.w3.org/TR/IndexedDB/#key-construct) from one of three sources:
  + A key generator. A key generator generates a monotonically increasing number every time a key is needed. This is somewhat similar to auto-incremented primary keys in a SQL database.
  + Keys can be derived via a key path.
  + Keys can also be explicitly specified when [a value](https://www.w3.org/TR/IndexedDB/#value-construct) is stored in the object store.s

Further details will be given in the next chapter "Using IndexedDB".

#### Version

+ When a database is first created, its version is the integer 0. Each database has one version at a time; a database can't exist in multiple versions at once.
+ The only way to change the version is by opening it with a higher version number than the current one. This will start a `versionchange` transaction and fire an `upgradeneeded` event. The only place where the schema of the database can be updated is inside the handler of that event.

This definition describes [the most recent specification](https://w3c.github.io/IndexedDB/), which is only implemented in up-to-date browsers. Old browsers implemented the now deprecated and removed `IDBDatabase.setVersion()` method.

#### Transaction

From the specification: 

>"A transaction is used to interact with the data in a database. Whenever data is read or written to the database, this is done by using a transaction.

> All transactions are created through a connection, which is the transaction's connection. The transaction has a mode (`read`, `readwrite` or `versionchange`) that determines which types of interactions can be performed upon that transaction. The mode is set when the transaction is created and remains fixed for the life of the transaction. The transaction also has a scope that determines the object stores with which the transaction may interact."

A transaction in IndexedDB is similar to a transaction in a SQL database. It defines: "_An atomic and durable set of data-access and data-modification operations_". Either all operations succeed or all fail. 

A database connection can have several active transactions associated with it at a time, but these write transactions cannot have overlapping [scopes](https://developer.mozilla.org/en-US/docs/IndexedDB/Basic_Concepts_Behind_IndexedDB#scope) (_they cannot work on the same data at the same time_). The scope of a transaction, which is defined at creation time, determines which concurrent transactions can read or write the same data (multiple reads can occur, while writes will be sequential, only one at a time), and remains constant for the lifetime of the transaction.

So, for example, if a database connection already has a writing transaction with a scope that covers only the `flyingMonkey` object store, you can start a second transaction with a scope of the `unicornCentaur` and `unicornPegasus` object stores. As for reading transactions, you can have several of them, and they may even overlap. A "`versionchange`" transaction never runs concurrently with other transactions (reminder: we usually use such transactions when we create the object store or when we modify the schema).

Generally speaking, the above requirements mean that "`readwrite`" transactions which have overlapping scopes always run in the order they were [created](https://www.w3.org/TR/IndexedDB/#dfn-transaction-create), and never run in parallel. A "`versionchange`" transaction is automatically created when a database version number is provided that is greater than the current database version. This transaction will be active inside the `onupgradeneeded` event handler, allowing the creation of new object stores and [indexes](https://www.w3.org/TR/IndexedDB/#dfn-index).

#### Request

The operation by which reading and writing on a database is done. Every request represents one read or one write operation. Requests are always run within a transaction. The example below adds a customer to the object store named "customers".

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Use the transaction to add data...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln"> transaction</span><span class="pun">.</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="kwd">in</span><span class="pln"> customerData</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> objectStore</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">customerData</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong style="color: red;">request</strong></span><strong style="color: red;"><span class="pun">.</span><span class="pln">onsuccess </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// event.target.result == customerData[i].ssn</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

#### Index

It is sometimes useful to retrieve [records](https://www.w3.org/TR/IndexedDB/#dfn-record) from an object store through means other than their key.

An index allows the user to look up records in an object store using the properties of the values in the object store's records. Indexes are a common concept in databases. Indexes can speed up object retrieval and allow multi-criteria searches. For example, if you store persons in your object store, and add an index on the "email" property of each person, then searching for some person using his/her email address will be much faster.

An index is a specialized persistent key-value storage and has a _referenced_ object store. For example, with our "persons" object store, that is the referenced data store. Then, a reference store may have an index store associated with it, that contains indexes which map email values to key values in the reference store (for example).

An index is _a list of records_ which holds the data stored in the index. The records in an index are automatically populated whenever records in [the referenced object store](https://www.w3.org/TR/IndexedDB/#dfn-referenced) are inserted, updated or deleted. There may be several indexes referencing the same object store, in which case changes to the object store cause all such indexes to update.

An index contains a _unique flag_. When this flag is set to `true`, the index enforces the rule that no two records in the index may have the same key. If a user attempts to insert or modify a record in the index's referenced object store, such that an indexed attribute's value already exists in an index, then the attempted modification to the object store fails.

#### Key and values

__Key__

A data value by which stored values are organized and retrieved in the object store. The object store can derive the key from one of three sources: [a key generator](https://mzl.la/3wrd84w), [a key path](https://mzl.la/3AOMpSF), and an explicitly specified value.

The key must be of a data type that has a number that is greater than the one before. Each record in an object store must have a key that is unique within the same store, so you cannot have multiple records with the same key in a given object store.

__A key can be one of the following types: [string](https://mzl.la/3yL8z6w), [date](https://mzl.la/3htBJBt), float, and [array](https://mzl.la/3AHZahU).__ For arrays, the key can range from an empty value to infinity. And you can include an array within an array.

Alternatively, you can also look up records in an object store using [an index](https://developer.mozilla.org/en-US/docs/IndexedDB/Basic_Concepts_Behind_IndexedDB#gloss_index).

__Key generator__

A mechanism for producing new keys in an ordered sequence. If an object store does not have a key generator, then the application must provide keys for records being stored. Similar to auto-generated primary keys in SQL databases.

__In-line key__

A key that is stored as part of the stored value. Example: the email of a person or a student number in an object representing a student in a student store. It is found using a key path. An in-line key could be generated using a generator. After the key has been generated, it can then be stored in the value using the key path, or it can also be used as a key.

__Out-of-line key__

A key that is stored separately from the value being stored, for instance, an auto-incremented id that is not part of the object. Example: you store persons `{name:Buffa, firstName:Michel}` and `{name:Forgue, firstName: Marie}`, each will have a key (think of it as a primary key, an id...) that can be auto-generated or specified, but that is not part of the object stored.

__Key path__

Defines where the browser should extract the key from a value in the object store or index. __A valid key path can include one of the following: an empty string, a JavaScript identifier, or multiple JavaScript identifiers separated by periods. <font style="color: red;">It cannot include spaces.</font>__

__Value__

Each record has a value, which could include anything that can be expressed in JavaScript, including: [boolean](https://mzl.la/3ARyQlJ), [number](https://mzl.la/2TUEbb2), [string](https://mzl.la/3yL8z6w), [date](https://mzl.la/3htBJBt), [object](https://mzl.la/36sICN4), [array](https://mzl.la/3AHZahU), [regexp](https://mzl.la/3hygZby), [undefined](https://mzl.la/3k4AZnT), and null.

When an object or an array is stored, the properties and values in that object or array can also be anything that is a valid value.

Blobs and files can be stored, (supported by all major browsers, IE > 9). The example in the next chapter stores images using blobs.


#### Range and scope

__Scope__

The set of object stores and indexes to which a transaction applies. The scopes of read-only transactions can overlap and execute at the same time. On the other hand, the scopes of writing transactions cannot overlap. You can still start several transactions with the same scope at the same time, but they just queue up and execute one after another.

__Cursor__

A mechanism for iterating over multiple records within a _key range_. The cursor has a source defining which index or object store it is iterating. It has a position within the range, and retrieves records sequentially according to the value of their keys in either increasing or decreasing order. For the reference documentation on cursors, see [IDBCursor](https://mzl.la/3yLHGiR).

__Key range__

A continuous interval over some data type used for keys. Records can be retrieved from object stores and indexes using keys or a range of keys. You can limit or filter the range using lower and upper bounds. For example, you can iterate over all the values of a key between x and y.

For the reference documentation on key range, see [IDBKeyRange](https://mzl.la/3r3iLVh).


#### Notes for 3.6.3 Definitions

+ Database
  + each origin w/ an associated set of database
  + a database comprises one or more object stores
  + name of a database
    + used to identify a databas within a specific origin
    + any string value, including the empty string
    + remaining constant for the lifetime of the database
  + version of a database
    + current version as a property of the database
    + version 0: default value when a database created
    + only one version at any given time
  + connection
    + created as a database open
    + multiple connects existed for a given database at any given time

+ Object store
  + the mechanism by which data is stored in the database
  + name of object store
    + must have property
    + unique within the database to which it belongs
  + records (JavaScript objects)
    + key-value pairs persistently held
    + one of these keys as a kind of "primary key" in the SQL database sense
    + key: a property that every object in the datastore must contain
    + values: structured but probably varied btw objects
    + example: person contacts in database, email as "the key all objects must define", some may have first name and last name. others may have an address or no address at all
    + stored according to keys, in ascending order, within an object store
  + probably having a key generator and a key path
    + in-line keys: datastore w/ a key path
    + out-of-line keys: datastore w/o a key path
  + able to derive the key from
    + key generator: a monotonically increasing number every time a key needed, similar to auto-incremented primary keys in a SQL database
    + a key path
    + explicitly specified when a value is stored in the object stores

+ Version
  + version 0: a database first created
  + one version ar a time
  + no multiple versions existed at once
  + changing the version by opening it w/ a higher version number tha the current one
  + syntax: starting a `versionchange` transaction and triggering an `upgradeneeded` event
  + the handler of the event: only place to update the schema of the database
  + `IDBDatabase.setVersion()` method deprecated

+ Transaction
  + an atomic and durable set of data-access and data-modification operation
  + used to interact w/ the data in a database
  + data read and written to the database done by using a transaction
  + mode:
    + type: `read`, `readwrite`, or `versionchange`
    + determining which types of interaction performed upon that transaction
    + set when transaction created and remain fixed for the life of the transaction
  + a transaction in IndexedDB similar to a transaction in a SQL database
  + all succeed or all fail within all operations of a transaction
  + connection
    + transaction created through a connection
    + allowing multiple active transaltions associated w/ a connection at a time
  + scope
    + defined at creation time
    + determining the object stores w/ which the transaction may interact
    + determining which concurrent transactions can read or write the same data
    + write transactions unable to have overlapping scope. i.e., working on the same data at the same time
    + multiple reads allowed at the same time while writes in sequence, only one at a time overlapped
    + a `versionchange` transaction
      + never runs concurrently w/ other transactions
      + automatically created when a database w/ higher version number is provided
      + transaction activated inside the `onupgradeneeded` event handler, allowing the creation of new object stores and indexes
    + `readwrite` transactions w/ overlapped scopes always run in the order they were created and never run in parallel
  + example:
    + existing a writing transaction in a database connection
    + scope of the transaction covering only the `flyingMonkey` object store
    + starting a second transaction w/ a scope of the `unicornCentaur` and `unicornPegasus` object stores
    + allowing several reading transactions and probably overlapped

+ Request
  + issued as the reading and writing on a database done
  + represeting one read or one write operation
  + always run within a transaction
  + example: add a customer to the object store named "customers"
    + [access data](#objStore)
    + iterate through to [add data](#addData)

+ Index
  + sometimes useful to retrieve records from an object store through their means than their keys
    + allowing the user to look up records in an object store by using the properties of the values in the object store's records
    + able to speed up object retrieval and allow multi-criteria
  + a specialized persistent key-value storage
    + having a referenced object store
    + reference store probably w/ an index store associated w/ it
  + a list of records holding the data stored in the index
    + records in an index automatically populated whenever records in the referenced object store are inserted, updated or deleted
    + several indexes referencing the same object store $\to$ changes to the object store causing all such indexes to update
  + containing a unique flag set to `true`
    + no two records in the index w/ the same key
    + failed if attempt to insert or modify a record in the index's referenced object store
  + example: storing persons in object store
    + adding an index on the "email" property of each person $\implies$ searching for some person using his/her email address much faster
    + "persons" as the referenced object store
    + reference store containing indexes which map email values to key values in the reference store

+ Key
  + a data value by which stored values are organized and retrieved in the object store
  + key derived from one of the sources
    + a key generator
    + a key path
    + explicitly specified value
  + key w/ a data type having a number greater than the one before
  + each record in an object store must have a unique key within the same store
  + types of key
    + string
    + date
    + array: ranging from an empty in an object store using an index
  
+ Key generator
  + a mechanism for producing new key in an ordered sequence
  + an object store w/o a key generator $\to$ application must provide keys for records being stored
  + similar to auto-generated primary keys in SQL databases

+ In-line key
  + a key stored as part of of the stored 
  + found using a key path
  + probably generated using a generator
  + stored in the value using the key path or used as a key once generated
  + example: the email of a person or a student number in an object representing a student in a student store

+ Out-of-line key
  + a key stored separately from the value being stored
  + an auto-incremental `id` not part of the key

+ Key path
  + where the browser should extract the key from a value in the object store or index
  + valid key path including one of
    + an empty string
    + a JavaScript identifier
    + multiple JavaScript identifiers separated by period w/o spaces

+ Value
  + each record w/ a value
  + anything abel to be expressed in JavaScript, including, boolean, number, string, date, object, array, regexp, undefined and null
  + object/array: the properties and values in it able to be anything but valid
  + blog and files supported by all major browsers, IE > 9

+ Scope
  + the set of object stores and indexes to which a transaction applies
  + read-only transactions: able to overlap and execute at the same time
  + writing transaction:
    + unable to overlap
    + multiple transactions w/ same scope at the same time allowed but queue up and execute in sequence

+ Cursor
  + a mechanism for iterating over multiple records within a key range
  + existing a source defining which index or object store it is iterating
  + having a position within the range
  + retrieving records sequentially according to the value of their keys in descending or ascending way

+ Key range
  + a continuous interval over some data type used for keys
  + retrieving records via object stores and indexes using keys or a range of keys
  + able to limit and filter the range using lower and upper bounds
  + example: iterate over all values of a key btw x and y


### 3.6.4 Using IndexedDB

This page and the following one, entitled "Using IndexedDB", provide simple examples for creating, adding, removing, updating, and searching data in an IndexedDB database. They explain the basic steps to perform such common operations, while explaining the programming principles behind IndexedDB.

#### Contents of using IndexedDB

__In the "Using IndexedDB" pages of this course, you will learn about:__

+ Creating and populating a database
+ Working with data
+ Using transactions
+ Inserting, deleting, updating and getting data
+ Creating and populating a database

#### External resources

Additional information is available on these Web sites. Take a look at these!

+ MDN's documentation on "[Using IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB)"
+ [Storing images and files in IndexedDB](http://robertnyman.com/2012/03/06/storing-images-and-files-in-indexeddb/)
+ [Working with IndexedDB](https://developers.google.com/web/ilt/pwa/working-with-indexeddb)
+ [How to view IndexedDB content in Firefox](https://stackoverflow.com/questions/9846013/how-to-view-indexeddb-content-in-firefox)


### 3.6.5 Creating and deleting a database

#### Live coding video: using IndexedDB (part 1)

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V003400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/36rHnO6)

#### Creating a database

Our [online example at JSBin](https://jsbin.com/govuci) shows how to create and populate an object store named "CustomerDB". This example should work on both mobile and desktop versions of all major post-2012 browsers.

[Local Demo](src/03f-example01.html)

We suggest that you follow what is happening using Google Chrome's developer tools. Other browsers offer equivalent means for debugging Web applications that use IndexedDB.

With Chrome, please open the JSBin example and activate the Developer tool console (F12 or cmd-alt-i). Open the JavaScript and HTML tabs on JSBin.

Then, click the "Create CustomerDB" button in the HTML user interface of the example: it will call the `createDB()` JavaScript function that:

1. creates a new IndexedDB database and an object store in it ("customersDB"), and
2. inserts two javascript objects (look at the console in your devtools - the Web app prints lots of traces in there, explaining what it does under the hood). Note that the social security number is the "Primary key", called a key path in the IndexedDB vocabulary (red arrow on the right of the screenshot).

__Chrome DevTools (F12 or cmd-alt-i) shows the IndexedDB databases, object stores and data:__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3ATNBED')"
    src    = "https://bit.ly/3qZNXVC"
    alt    = "chrome dev tools show the content of the IndexedDB database that has been created and populated"
    title  = "chrome dev tools show the content of the IndexedDB database that has been created and populated"
  />
</figure>


Normally, when you create a database for the first time, the console should show this message:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3ATNBED')"
    src    = "https://bit.ly/3k8xdKb"
    alt    = "Message displayed in console when the database is created the first time you run the example"
    title  = "Message displayed in console when the database is created the first time you run the example"
  />
</figure>


This message comes from the JavaScript `request.onupgradeneeded` callback. Indeed, the first time we open the database we ask for a specific version (in this example: version 2) with:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> indexedDB</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="pln">dbName</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">);</span></li>
</ol></div>

...and if there is no version "2" of the database, then we enter the `onupgradeneeded` callback where we actually create the database.

You can try to click again on the button "CreateCustomerDatabase", if database version "2" exists, this time the `request.onsuccess` callback will be called. This is where we will add/remove/search data (you should see a message on the console).

Notice that the version number cannot be a float: "1.2" and "1.4" will automatically be rounded to "1".

__JavaScript code from the example:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> db</span><span class="pun">;</span><span class="pln"> </span><span class="com">// the database connection we need to initialize</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> createDatabase</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pun">(!</span><span class="pln">window</span><span class="pun">.</span><span class="pln">indexedDB</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;window</span><span class="pun">.</span><span class="pln">alert</span><span class="pun">(</span><span class="str">"Your browser does not support a stable version </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;of IndexedDB"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// This is what our customer data looks like.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> customerData </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">{</span><span class="pln"> ssn</span><span class="pun">:</span><span class="pln"> </span><span class="str">"444-44-4444"</span><span class="pun">,</span><span class="pln"> name</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Bill"</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="pln"> </span><span class="lit">35</span><span class="pun">,</span><span class="pln"> email</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"bill@company.com"</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">{</span><span class="pln"> ssn</span><span class="pun">:</span><span class="pln"> </span><span class="str">"555-55-5555"</span><span class="pun">,</span><span class="pln"> name</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Donna"</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="pln"> </span><span class="lit">32</span><span class="pun">,</span><span class="pln"> email</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"donna@home.org"</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">];</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> dbName </span><span class="pun">=</span><span class="pln"> </span><span class="str">"CustomerDB"</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// version must be an integer, not 1.1, 1.2 etc... </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> indexedDB</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="pln">dbName</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; request</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Handle errors.</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"request.onerror errcode="</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; request</span><span class="pun">.</span><span class="pln">onupgradeneeded </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"request.onupgradeneeded, we are creating a </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;new version of the dataBase"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; db </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Create an objectStore to hold information about our </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; // customers. We're&nbsp;</span>going to use "ssn" as our key path because</li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// &nbsp;it's guaranteed&nbsp;</span><span class="com">to be&nbsp;</span><span style="color: #880000; line-height: 23.2727px; background-color: #eeeeee;">unique</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">.</span><span class="pln">createObjectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{</span><span class="pln"> keyPath</span><span class="pun">:</span><span class="pln"> </span><span class="str">"ssn"</span><span class="pln"> </span><span class="pun">});</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Create an index to search customers by name. We may have &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; //&nbsp;</span>duplicates&nbsp;so we can't use a unique index.</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; objectStore</span><span class="pun">.</span><span class="pln">createIndex</span><span class="pun">(</span><span class="str">"name"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"name"</span><span class="pun">,</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> unique</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">false</span><span class="pln"> </span><span class="pun">});</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Create an index to search customers by email. We want to </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; // ensure that&nbsp;</span>no two customers have the same email, so use a</li>
<li class="L6" style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; // unique index.</li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; objectStore</span><span class="pun">.</span><span class="pln">createIndex</span><span class="pun">(</span><span class="str">"email"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"email"</span><span class="pun">,</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> unique</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pln"> </span><span class="pun">});</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Store values in the newly created objectStore.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="kwd">in</span><span class="pln"> customerData</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; objectStore</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">customerData</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span><span class="pln"> </span><span class="com">// end of request.onupgradeneeded</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; request</span><span class="pun">.</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Handle errors.</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"request.onsuccess, database opened, now we can add </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; / remove / look for data in it!"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// The result is the database itself</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;db </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span><span class="com">// end of function createDatabase</span></li>
</ol></div>

__Explanations:__

All the "creation" process is done in the onupgradeneeded callback (lines 26-50):

+ _Line 30_: get the database created in the result of the dom event: `db = event.target.result;`
+ _Line 35_: create an object store named "`customers`" with the primary key being the social security number ("`ssn`" property of the JavaScript objects we want to store in the object store): `var objectStore = db.createObjectStore("customers", {keyPath: "ssn"});`
+ _Lines 39 and 44_: create indexes on the "`name`" and "`email`" properties of JavaScript objects: `objectStore.createIndex("name", "name", {unique: false});`
+ _Lines 48-50_: populate the database: `objectStore.add(...)`.

<p style="margin: 10px; padding: 10px; border: 1px solid;">Note that we did not create any transaction, as the <code>onupgradeneeded</code> callback on a create database request is always in a default transaction that cannot overlap with another transaction at the same time.</p>

If we try to open a database version that exists, then the `request.onsuccess` callback is called. This is where we are going to work with data. The DOM event result attribute is the database itself, so it is wise to store it in a variable for later use: `db= event.target.result;`


#### Deleting a database

You can delete a database simply by running this command:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">indexedDB</span><span class="pun">.</span><span class="pln">deleteDatabase</span><span class="pun">(</span><span class="str">"databaseName"</span><span class="pun">);</span></li>
</ol></div>

A common practice, while learning how IndexedDB works, is to type this command in the devtool console. For example, we can delete the CustomerDB database used in all examples of this course section by opening one of the JsBin examples , then opening the devtool console, then executing `indexedDB.deleteDatabase("CustomerDB");` in the console:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3ATNBED" ismap target="_blank">
    <img style="margin: 0.1em;" height=250
      src   = "https://bit.ly/3xzRRXK"
      alt   = "deleting indexed DB part 1, open the devtool console"
      title = "deleting indexed DB part 1, open the devtool console"
    >
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/2UGFYkh"
      alt   = "Run the command"
      title = "Run the command"
    >
  </a>
</div>


<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3ATNBED" ismap target="_blank">
    <img style="margin: 0.1em;" height=70
      src   = "https://bit.ly/3B19zpl"
      alt   = "Execute the command"
      title = "Execute the command"
    >
    <img style="margin: 0.1em;" height=70
      src   = "https://bit.ly/3e8Ca1R"
      alt   = "Refresh IndexedDB display of objectStores"
      title = "Refresh IndexedDB display of objectStores"
    >
    <img style="margin: 0.1em;" height=70
      src   = "https://bit.ly/3AORD0R"
      alt   = "delete database"
      title = "delete database"
    >
  </a>
</div>


#### Notes for 3.6.5 Creating and deleting a database

+ Creating database
  + mainly based on Chrome but other browsers w/ equivalent means for debugging
  + executing app to create an IndexedDB w/ name = "customers"
  + calling `createDB()` function to create a database
    + creating a new IndexedDB database and an object store in it
    + inserting two JS objects
  + checking w/ devtools > Application > IndexedDB to show the IndexedDB database, object store and data
  + syntax to create database: `var request = indexedDB.open(dbName, verNo);`
    + no `verNo` $\to$ entering the `onupgradeneeded` callback where the database actually is created
    + `verNo` existed $\to$ calling `request.onsuccess` callback to add/remove/search data
  + `onupgradeneeded` callback
    + triggered on a create database request
    + always in a default transaction
    + unable to overlap w/ another transaction at the same time
  + best practice: declare a variable to store the database $\gets$ the DOM event result attribute = the database

+ Example: creating database
  + tasks:
    + create db via DOM event
    + create object store and primary key w/ SSN
    + create indexes on `email` and `name`
    + populate the db
  + declare the db connection to initialize: `var db;`
  + create db: `function createDatabase() {...}`
  + display unsupported msg: `if (!window.indexedDB) { alert("Your browser does not support a stable version of IndexedDB"); }`
  + declare [cuntomer data](#cxData)
  + set db name: `var dbName = "CustomerDB";`
  + create db to get request: `var request = indexedDB.open(dbName, 2);`
  + add error handle for creating db: `request.onerror = function(evt) { console.log("request.onerror errcode= " + evt.target.error.name); }`
  + add upgrade handler: `request.onupgradeneeded = function(evt) {...}`
    + log msg: `console.log("request.onupgradeneeded, we are creating a new version of the DB");`
    + get db from event: `db = evt.target.result;`
    + create object store and keyPath: `var objStore = db.createObjectStore("customers", {keyPath: "ssn"});`
    + declare a property as an index<a name="emailIdx"></a>: `objStore.createIndex("email", "email", {unique: true});`
    + populate db by storing values in object store: `for (var i in customerData) { objStore.add(customerData[i]); }`
  + add success handler: `request.onsuccess = function(evt) { console.log("request.onsuccess, database opened, now we can add/remove/look up for data in it!"); db = ent.target.result; }`

+ Deleting the database
  + syntax: `indexedDB.deleteDatabase("dbName");`
  + common practice for learner: execute the command in devtools > console


### 3.6.6 Working with data

Explicit use of a transaction is necessary:

<p style="text-align: center; border: 1px solid; margin: 10px; padding: 10px;"><strong style="color: red;">All operations in the database should occur within a transaction!</strong></p>

While the creation of the database occurred in a transaction that ran "under the hood" without explicit use of the "transaction" keyword, __for adding/removing/updating/retrieving data, explicit use of a transaction is required.__

We generate a transaction object from the database, indicate with which object store the transaction will be associated, and specify an access mode .

Source code example for creating a transaction associated with the object store named "customers":

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong style="color: red;"><span class="kwd">var</span><span class="pln"> transaction </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">([</span><span class="str">"customers"</span><span class="pun">],</span><span class="pln"> </span><span class="str">"readwrite"</span><span class="pun">);</span></strong><span class="pln"> </span><span class="com">// or "read"...</span></li>
</ol></div>

Transactions, when created, must have a mode set that is either `readonly`, `readwrite` or `versionchange` (this last mode is only for creating a new database or for modifying its schemas: i.e. changing the primary key or the indexes).

<p style="margin: 10px; padding: 10px; border: 1px solid">When you can, use&nbsp;readonly mode. Concurrent read transactions will become possible.</p>

In the following pages, we will explain how to insert, search, remove, and update data. A final example that merges all examples together will also be shown at the end of this section.


#### Notes for 3.6.6 Working with data

+ Transaction w/ data
  + all operations in the database happened within a transaction
  + implicit transactions during the creation of the database
  + explicit transactions for adding/removing/updating/retrieving data
  + generating a transaction object from the database:
    + indicating which object store associated
    + specifying and access mode
  + syntax: `var transaction = db.transaction(["objStoreName", ...], mode);`
    + `mode`: either `readonly`, `readwrite`, or `versionchange`
    + `versionchange`: only for creating a new database or for modifying its schemas
    + `readonly`: concurrent read transactions allowed


### 3.6.7 Inserting data

#### Live coding video: using IndexedDB (part 2)

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V003300_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3r1f1DM)


#### Basic procedure

__Example #1: basic steps__

[Online example at JSBin](https://jsbin.com/jukifo):

[Local Demo](src/03f-example02.html)

Execute this example and look at the IndexedDB object store content from the Chrome dev tools (F12 or cmd-alt-i). One more customer should have been added.

__Be sure to click on the "create database" button before clicking the "insert new customer" button.__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3wzccej')"
    src    = "https://bit.ly/2UIkS4L"
    alt    = "example on JsBin for inserting data in IndexedDB"
    title  = "example on JsBin for inserting data in IndexedDB"
  />
</figure>


The next screenshot shows the IndexedDB object store in Chrome dev. tools (use the "Resources" tab). Clicking the "Create CustomerDB" database creates or opens the database, and clicking "Add a new Customer" button adds a customer named "Michel Buffa" into the object store:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3wzccej')"
    src    = "https://bit.ly/3ARYpmA"
    alt    = "Devtools show that a new customer named Michel Buffa has been inserted"
    title  = "Devtools show that a new customer named Michel Buffa has been inserted"
  />
</figure>


__Code from the example, explanations:__

We just added a single function into the example from the previous section - the function `AddACustomer()` that adds one customer:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong style="color: red;"><span class="pun">{</span><span class="pln"> ssn</span><span class="pun">:</span><span class="pln"> </span><span class="str">"123-45-6789"</span><span class="pun">,</span><span class="pln"> name</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Michel Buffa"</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="pln"> </span><span class="lit">47</span><span class="pun">,</span><span class="pln"> email</span><span class="pun">:</span></strong><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="str">"buffa@i3s.unice.fr"</span><span class="pln"> </span><span class="pun">}</span></strong></li>
</ol></div>

Here is the complete source code of the `addACustomer` function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> addACustomer</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 1 - get a transaction on the "customers" object store</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// in readwrite, as we are going to insert a new object </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> transaction </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">([</span><span class="str">"customers"</span><span class="pun">],</span><span class="pln"> </span><span class="str">"readwrite"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Do something when all the data is added to the database.</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// This callback is called after transaction has been completely </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// executed (committed)</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transaction</span><span class="pun">.</span><span class="pln">oncomplete </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">"All done!"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// This callback is called in case of error (rollback) </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transaction</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"transaction.onerror errcode="</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// 2 - Init the transaction on the objectStore</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln"> transaction</span><span class="pun">.</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// 3 - Get a request from the transaction for adding a new object </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> objectStore</span><span class="pun">.</span><span class="pln">add</span><span class="pun">({</span><span class="pln"> ssn</span><span class="pun">:</span><span class="pln"> </span><span class="str">"123-45-6789"</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;name</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Michel Buffa"</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;age</span><span class="pun">:</span><span class="pln"> </span><span class="lit">47</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;email</span><span class="pun">:</span><span class="pln"> </span><span class="str">"buffa@i3s.unice.fr"</span><span class="pln"> </span><span class="pun">});</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// The insertion was ok</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Customer with ssn= "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result </span><span class="pun">+</span><span class="pln"> </span><span class="str">" </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; added."</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// the insertion led to an error (object already in the store, </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// for example) </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"request.onerror, could not insert customer, </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; errcode = "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Explanations:

In the code above, _lines 4, 19 and 22_ show the main calls you have to perform in order to add a new object to the store:

1. Create a transaction.
1. Map the transaction onto the object store.
1. Create an "add" request that will take part in the transaction.

The different callbacks are in _lines 9 and 14_ for the transaction, and in _lines 28 and 35_ for the request.

You may have several requests for the same transaction. Once all requests have finished, the `transaction.oncomplete` callback is called. In any other case the `transaction.onerror` callback is called, and the datastore remains unchanged.

Here is the trace from the dev tools console:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3wzccej')"
    src    = "https://bit.ly/36vbqV6"
    alt    = "Trace from the devtools console"
    title  = "Trace from the devtools console"
  />
</figure>


#### Data from a form

__Example #2: adding a form and validating inputs__

[Online example](https://jsbin.com/jayida) available at JSBin:

[Local Demo](src/03f-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3wzccej')"
    src    = "https://bit.ly/3hXL4R4"
    alt    = "a form has been added to the previous example, for creating a new customer"
    title  = "a form has been added to the previous example, for creating a new customer"
  />
</figure>


You can try this example by following these steps:

1. Press first the "Create database" button
2. then add a new customer using the form
3. click the "add a new Customer" button
4. then press F12 or cmd-alt-i to use the Chrome dev tools and inspect the IndexedDB store content. Sometimes it is necessary to refresh the view (right click on IndexedDB/refresh), and sometimes it is necessary to close/open the dev. tools to have a view that shows the changes (press F12 or cmd-alt-i twice). Chrome dev. tools are a bit strange from time to time.

This time, we added some tests for checking that the database is open before trying to insert an element, and we added a small form for entering a new customer.

Notice that the insert will fail and display an alert with an error message if:

+ The `ssn` is already present in the database. This property has been declared as the keyPath (a sort of primary key) in the object store schema, and <u>it should be unique</u>: `db.createObjectStore("customers", { keyPath: "ssn" });`
+ The `email` address is already present in the object store. Remember that in our schema, the `email` property is an index that we declared as unique: `objectStore.createIndex("email", "email", { unique: true });`
+ Try to insert the same customer twice, or different customers with the same `ssn`. An alert like this should pop up:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3wzccej')"
    src    = "https://bit.ly/3r4dtsX"
    alt    = "insert error"
    title  = "insert error"
  />
</figure>


__Here is the updated version of the HTML code of this example:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;fieldset&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; SSN: </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"ssn"</span><span class="pln"> </span><span class="atn">placeholder</span><span class="pun">=</span><span class="atv">"444-44-4444"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; required</span><span class="tag">/&gt;&lt;br&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; Name: </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"name"</span><span class="tag">/&gt;&lt;br&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; Age: </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"number"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"age"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"1"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"100"</span><span class="tag">/&gt;&lt;br&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; Email:</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"email"</span><span class="tag">/&gt;</span><span class="pln"> reminder, email must be </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;unique (we declared it as a "unique" index)</span><span class="tag">&lt;br&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/fieldset&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><strong style="color: red;"><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">addACustomer</span><span class="pun">();</span><span class="atv">"</span></strong><span class="tag">&gt;</span><span class="pln">Add a new Customer</span><span class="tag">&lt;/button&gt;</span></li>
</ol></div>

__And here is the new version of the `addACustomer()` JavaScript function:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> addACustomer</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">db </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">'Database must be opened, please click the Create </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;CustomerDB Database first'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">return</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> transaction </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">([</span><span class="str">"customers"</span><span class="pun">],</span><span class="pln"> </span><span class="str">"readwrite"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Do something when all the data is added to the database.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transaction</span><span class="pun">.</span><span class="pln">oncomplete </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"All done!"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transaction</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"transaction.onerror errcode="</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln"> transaction</span><span class="pun">.</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// adds the customer data</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> newCustomer</span><span class="pun">={};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;newCustomer</span><span class="pun">.</span><span class="pln">ssn </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#ssn"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;newCustomer</span><span class="pun">.</span><span class="pln">name </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#name"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;newCustomer</span><span class="pun">.</span><span class="pln">age </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#age"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;newCustomer</span><span class="pun">.</span><span class="pln">email </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#email"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'adding customer ssn='</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> newCustomer</span><span class="pun">.</span><span class="pln">ssn</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> objectStore</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">newCustomer</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Customer with ssn= "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result </span><span class="pun">+</span><span class="pln"> </span><span class="str">" </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; added."</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; request</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">"request.onerror, could not insert customer, errcode = "</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name&nbsp;</span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="str">". Certainly either the ssn or the email is already </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;present in the Database"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

It is also possible to shorten the code of the above function by chaining the different operations using the "." operator (getting a transaction from the db, opening the store, adding a new customer, etc.).

Here is the short version:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">([</span><span class="str">"customers"</span><span class="pun">],</span><span class="pln"> </span><span class="str">"readwrite"</span><span class="pun">)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">.</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">)</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">newCustomer</span><span class="pun">);</span></li>
</ol></div>

The above code does not perform all the tests, but you may encounter such a way of coding (!).

Also, note that it works if you try to insert empty data:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3wzccej')"
    src    = "https://bit.ly/3AReGYN"
    alt    = "devtools show that inserting blank data works"
    title  = "devtools show that inserting blank data works"
  />
</figure>


Indeed, entering an empty value for the keyPath or for indexes is a valid value (in the IndexedDB sense). In order to avoid this, you should add more JavaScript code. We will let you do this as an exercise.


#### Notes for 3.6.7 Inserting data

+ Typical procedure to inset data
  + create a transaction
  + map the transaction onto the object store
  + create an "add" request that will take part in the transaction

+ Example: basic steps
  + tasks
    + get a transaction on the "customer" object store in `readwrite` mode
    + init transaction on the ObjectStore
    + get request from the transaction for adding a new object
  + add a customer<a name="addCx"></a>: `function addACustomer() {...}`
  + create a transaction<a name="transactionRW"></a>: `var transaction = db.transaction(["customers"], "readwrite");`
  + add transaction complete handler<a name="transComplete"></a>: `transaction.oncomplete = function() { alert("All done!"); }`
  + add transaction error handler<a name="transErr"></a>: `transaction.onerror = function(evt) { console.log("transaction.onerror errcode = " + evt.target.error.name); }`
  + init to get object store<a name="initTrans"></a>: `var objStore = transaction.objectStore("customers");`
  + add new object and get request: `var request = objStore.add({ ssn: "123-45-6789", name: "Michel Buffa", age: 47, email: "buffa@i3s.unice.fr" });`
  + add request success handler<a name="reqSuccess"></a>: `request.onsuccess = function(evt) { console.log("Customer with ssn = " + evt.target.result + "added!"); }`
  + add request error handler<a name="reqErr"></a>: `request.onerror = function(evt) { console.log("request.onerror, could not insert customer, errcode = " + evt.target.error.name); }`

+ Example: adding data to DB from a form
  + process
    + press the "Create database" button first
    + add a new customer using the form
    + click the "add a new Customer" button
    + use devtools to inspect the IndexedDB store contents (refresh or close/open the devtools probably required)
  + good practice: checking the database open before interting an element
  + validation for inserting data and alerting w/ error message
    + `ssn` existed: the property declared as the keyPath (kind of primary key) in the object store schema and __unique__
    + `email` address existed: the property declared as an index and unique
    + same customer inserted twice or duplicated SSN $\to$ customized alert message
  + HTML snippet
    + group of input forms: `<fieldset>...</fieldset>`
    + SSN filed: `SSN: <input type="text" id="ssn" placeholder="444-44-4444" required/><br/>`
    + Name field: `Name: <input type="text" id="name"/> <br/>`
    + Age field: `Age: <input type="number" id="age" min=1 max=100 /></br>`
    + Email field: `Email: <input type="text" id="email"/> reminder, email must unique (declared as a "unique" index)<br/>`
    + new customer button: `<button onclick="addACustomer();">Add a new Customer</button>`
  + JavaScript snippet
    + [add a customer](#addCx) w/ additional steps
    + check the connection to db<a name="connChk"></a>: `if (db === null) { alert("Database must be opened, please click the Create CustomerDB Database first"); return; }`
    + get customer data from input fields: `var newCustomer = ();`
      + ssn: `newCustomer.ssn = document.queryelector("#ssn").value;`
      + name: `newCustomer.name = document.queryelector("#name").value;`
      + age: `newCustomer.age = document.queryelector("#age").value;`
      + email: `newCustomer.ssn = document.queryelector("#email").value;`
      + display msg: `alert('adding customer ssn=" + newCustomer.ssn);`
    + add new customer and get request: `var request = objStore.add(newCustomer);`
    + add request error handler: `request.onerror = function(evt) { console.log("request.onerror, could not insert customer, errcode = " + evt.target.error.name + ". Certainly either the ssn or the email is already present in the Database"); };`
  + JavaScript snippet - short version:
    + entering empty value for thekeyPath or for index $\to$ valid value (in the IndexedDB sense)
    + to avoid empty value $\to$ comprehensive version preferred

    ```js
    var request = db.transaction(["customers"], "readwrite")
      .objectStore("customers")
      .add(newCustomer);
    ```


### 3.6.8 Removing data

Let's move to the next [online example at JSBin](https://jsbin.com/bavifa):

[Local Demo](src/03f-example04.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3z0X8rN')"
    src    = "https://bit.ly/3AReGYN"
    alt    = "devtools show that a customer has been removed once clicked on the remove customer button"
    title  = "devtools show that a customer has been removed once clicked on the remove customer button"
  />
</figure>


See the changes in Chrome dev. tools: refresh the view (right click/refresh) or press F12 or cmd-alt-i twice. There is a bug in the refresh feature with some versions of Google Chrome.

How to try the example:

1. Be sure to click the "create database button" to open the existing database.
2. Then use Chrome dev tools  to check that the customer with `ssn=444-44-444` exists. If it's not there, just insert into the database like we did earlier in the course.
3. Right click on indexDB in the Chrome dev tools and refresh the display of the IndexedDB's content if necessary if you cannot see customer with `ssn=444-44-444`. Then click on the "Remove Customer ssn=444-44-4444(Bill)" button. Refresh the display of the database. The 'Bill' object should have disappeared!

Code added in this example:

<div class="source-code" style="line-height: 1.6;"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> removeACustomer</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">db </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">'Database must be opened first, please click the </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Create CustomerDB Database first'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">return</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> transaction </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">([</span><span class="str">"customers"</span><span class="pun">],</span><span class="pln"> </span><span class="str">"readwrite"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Do something when all the data is added to the database.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transaction</span><span class="pun">.</span><span class="pln">oncomplete </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"All done!"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transaction</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"transaction.onerror errcode="</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln"> transaction</span><span class="pun">.</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'removing customer ssn=444-44-4444'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> objectStore</span><span class="pun">.</span><span class="kwd">delete</span><span class="pun">(</span><span class="str">"444-44-4444"</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Customer removed."</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">"request.onerror, could not remove customer, errcode </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; = "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name&nbsp;</span><span class="pun">+</span><span class="pln"> </span><span class="str">". The ssn does not </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; exist in the Database"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Notice that after the deletion of the Customer (_line 23_), the `request.onsuccess` callback is called. And if you try to print the value of the `event.target.result` variable, it is "`undefined`".

__Short way of doing the delete:__

It is also possible to shorten the code of the above function a lot by concatenating the different operations (getting the store from the db, getting the request, calling delete, etc.). Here is the short version:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">([</span><span class="str">"customers"</span><span class="pun">],</span><span class="pln"> </span><span class="str">"readwrite"</span><span class="pun">)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">.</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">)</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">.</span><span class="kwd">delete</span><span class="pun">(</span><span class="str">"444-44-4444"</span><span class="pun">);</span></li>
</ol></div>


#### Notes for 3.6.8 Removing data

+ Example: removing data
  + procedure
    + click "create database button" to ensure the open of the existing database
    + use devtools to check the customer w/ `ssn=444-44-4444`, if not existed, add the customer from the input forms
    + refresh IndexedDB in devtools to observe the customer
    + click the "Remove the customer" button and observe the data object in devtools after refreshing
  + JavaScript snippet: `function removeACustomer() {...}`
    + check [the connection to db](#connChk)
    + create [a transaction](#transactionRW)
    + add [transaction complete handler](#transComplete)
    + add [transaction error handler](#transErr)
    + [init transaction](#initTrans)
    + dispaly msg: `alert('removing customer ssn=444-44-4444');`
    + create request to delete selected customer: `var request = objStore.delete("444-44-4444");`
    + add request success handler: `request.onsuccess = function(evt) { console.log("Customer removed!"); };`
    + add request error handler: `request.onerror = function(evt) { alert("request.onerror, could not remove customer, errcode = " + evt.target.error.name + ". The ssn does not exist in the Database"); };`
  + JavaScript snippet: short version

    ```js
    var request = db.transaction(["customers"], "readwrite")
      .objectStore("customers")
      .delete("444-44-4444");
    ```


### 3.6.9 Modifying data

We used `request.add(object)` to add a new customer and `request.delete(keypath)` to remove a customer. Now, to modify data from an object store with IndexedDB, we use `request.put(keypath)` to update a customer!

[Online example at JSBin](https://jsbin.com/zugowe):

[Local Demo](src/03f-example05.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/36wbbJw')"
    src    = "https://bit.ly/3AUTq4B"
    alt    = "devtools show a customer being updated in IndexedDB"
    title  = "devtools show a customer being updated in IndexedDB"
  />
</figure>


The above screenshot shows how we added an empty customer with `ssn=""`, (we just clicked on the open database button, then on the "add a new customer button" with an empty form).

Now, we fill the `name`, `age` and `email` input fields to update the object with ssn="" and click on the "update data about an existing customer" button. This updates the data in the object store, as shown in this screenshot:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/36wbbJw')"
    src    = "https://bit.ly/3xwAuaa"
    alt    = "devtools show updated customer"
    title  = "devtools show updated customer"
  />
</figure>


Here is the new code added to our example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> updateACustomer</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">db </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'Database must be opened first, please click the Create </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CustomerDB Database first'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">return</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> transaction </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">([</span><span class="str">"customers"</span><span class="pun">],</span><span class="pln"> </span><span class="str">"readwrite"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// Do something when all the data is added to the database.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transaction</span><span class="pun">.</span><span class="pln">oncomplete </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"All done!"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transaction</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"transaction.onerror errcode="</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln"> transaction</span><span class="pun">.</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> customerToUpdate</span><span class="pun">={};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;customerToUpdate</span><span class="pun">.</span><span class="pln">ssn </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#ssn"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;customerToUpdate</span><span class="pun">.</span><span class="pln">name </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#name"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;customerToUpdate</span><span class="pun">.</span><span class="pln">age </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#age"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;customerToUpdate</span><span class="pun">.</span><span class="pln">email </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#email"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'updating customer ssn='</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> customerToUpdate</span><span class="pun">.</span><span class="pln">ssn</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> objectStore</span><span class="pun">.</span><span class="pln">put</span><span class="pun">(</span><span class="pln">customerToUpdate</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Customer updated."</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">"request.onerror, could not update customer, errcode= "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name&nbsp;</span><span class="pun">+</span><span class="pln"> </span><span class="str">". The ssn is not in the </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; Database"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

The update occurs at _line 28_.


#### Notes for 3.6.9 Modifying data

+ Example: modifying data
  + update a customer: `function updateACustomer() {...}`
  + check [the connection to db](#connChk)
  + create [transaction](#transaction)
  + add [transaction complete handler](#transComplete)
  + add [transaction error handler](#transErr)
  + [init transaction to get object store](#initTrans)
  + set customer values for modifying: `var customerUpdate={};`
    + update snn from form: `customerToUpdate.ssn = document.querySelector("#ssn").value;`
    + update name from form: `customerToUpdate.name = document.querySelector("#name").value;`
    + update age from form: `customerToUpdate.name = document.querySelector("#age").value;`
    + update email from form: `customerToUpdate.name = document.querySelector("#email").value;`
  + display update info: `alert('updating customer ssn=' + customerToUpdate.ssn);`
  + modify data to get request: `var request = objStore.put(customerToUpdate);`
  + add request success handler: `request.onsuccess = function(evt) { console.log("Customer updated."); };`
  + add request error handler: `request.onerror = function(evt) { alert("request.onerror, could not update customer, errcode= " + evt.target.error.name + ". The ssn is not in the Database"); };`


### 3.6.10 Getting data

There are several ways to retrieve data from a data store.

#### First method: getting data when we know its key

The simplest function from the API is the `request.get(key)` function. It retrieves an object when we know its key/keypath.

[Online example at JSBin](https://jsbin.com/saquru):

[Local Demo](src/03f-example06.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/36tlRZv')"
    src    = "https://bit.ly/36tlRZv"
    alt    = "Getting data from IndexedDB, first enter a ssn, then press the search button"
    title  = "Getting data from IndexedDB, first enter a ssn, then press the search button"
  />
</figure>


If the `ssn` exists in the object store, then the results are displayed in the form itself (the code that gets the results and that updates the form is in the `request.onsuccess` callback).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/36tlRZv')"
    src    = "https://bit.ly/3ANR9Ii"
    alt    = "Form updated with data retrieved"
    title  = "Form updated with data retrieved"
  />
</figure>


Here is the code added to that example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> searchACustomer</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">db </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'Database must be opened first, please click the Create </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CustomerDB Database first'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">return</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> transaction </span><span class="pun">=</span><span class="pln"> db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">([</span><span class="str">"customers"</span><span class="pun">],</span><span class="pln"> </span><span class="str">"readwrite"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Do something when all the data is added to the database.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transaction</span><span class="pun">.</span><span class="pln">oncomplete </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"All done!"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transaction</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"transaction.onerror errcode="</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln"> transaction</span><span class="pun">.</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Init a customer object with just the ssn property initialized </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// from the form</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="kwd">var</span><span class="pln"> customerToSearch</span><span class="pun">={};</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong style="color: red;">customerToSearch</strong></span><strong style="color: red;"><span class="pun">.</span><span class="pln">ssn </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#ssn"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'Looking for customer ssn='</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> customerToSearch</span><span class="pun">.</span><span class="pln">ssn</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Look for the customer corresponding to the ssn in the object </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// store</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> objectStore</span><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="pln">customerToSearch</span><span class="pun">.</span><span class="pln">ssn</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong style="color: red;">console</strong></span><strong style="color: red;"><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Customer found"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">name</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#name"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">=</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">name</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#age"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">age</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#email"</span><span class="pun">).</span><span class="pln">value</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; =</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">email</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">"request.onerror, could not find customer, errcode = "</span><span class="pln"> </span><span class="pun">+</span>&nbsp;&nbsp;<span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">error.name&nbsp;</span><span class="pun">+</span><span class="pln"> </span><span class="str">".</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; The ssn is not in the Database"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

The search is inititated at _line 30_, and the callback in the case of success is `request.onsuccess`, _lines 32-38_. `event.target` with result as the retrieved object (_lines 33 to 36_).

Well, this is a lot of code, isn't it? We can considerably abbreviate this function (though, admittedly it won't take care of all possible errors). Here is the shortened version:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> searchACustomerShort</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">).</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">)</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="pln">document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#ssn"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">).</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln">&nbsp; &nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp;function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#name"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">name</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#age"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">age</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#email"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">email</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}; // end of onsuccess callback</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

You can try it on JSBin: this [version of the online example using this shortened version](https://jsbin.com/rifate) (the function is at the end of the JavaScript code):

[Local Demo](src/03f-example07.html)

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> searchACustomerShort</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">db </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">'Database must be opened first, please click the Create </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;CustomerDB Database first'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">return</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">).</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">)</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="pln">document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#ssn"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">)</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp;.</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln">&nbsp; </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp;function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#name"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">name</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#age"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">age</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#email"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">email</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

__Explanations:__

+ Since there's only one object store, you can avoid passing a list of object stores that you need in your transaction and just pass the name as a string (_line 8_),
+ We are only reading from the database, so we don't need a "readwrite" transaction. Calling `transaction()` with no mode specified gives a "`readonly`" transaction (_line 8_),
+ We don't actually save the request object to a variable. Since the DOM event has the request as its target we can use the event to get to the `result` property (_line 9_).


#### Second method: getting more than one piece of data

__Getting all of the data from the datastore: using <u>a cursor</u>__

Using `get()` requires that you know which key you want to retrieve. If you want to step through all the values in your object store, or just between those in a certain range, then you must use _a cursor_.

Here's what it looks like:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> listAllCustomers</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln">&nbsp; &nbsp; </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">).</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong style="color: red;">objectStore</strong></span><strong style="color: red;"><span class="pun">.</span><span class="pln">openCursor</span><span class="pun">().</span><span class="pln">onsuccess </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// we enter this callback for each object in the store</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong style="color: red;"><span class="com">// The result is the cursor itself</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong style="color: red;"><span class="kwd">var</span><span class="pln"> cursor </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">cursor</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">"Name for SSN "</span><span class="pln"> </span><span class="pun">+</span><strong style="color: red;"><span class="pln"> cursor</span><span class="pun">.</span><span class="pln">key </span></strong><span class="pun">+</span><span class="pln"> </span><span class="str">" is "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong style="color: red;">cursor</strong></span><strong style="color: red;"><span class="pun">.</span><span class="pln">value</span><span class="pun">.</span><span class="pln">name</span></strong><span class="pun">);</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Calling continue on the cursor will&nbsp;result in&nbsp;this callback </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp;//&nbsp;being called&nbsp;</span>again if there are other objects in the store</li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;">cursor</strong></span><strong style="color: red;"><span class="pun">.</span><span class="kwd">continue</span><span class="pun">();</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">"No more entries!"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span><span class="pln"> </span><span class="com">// end of onsuccess...</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span><span class="com">// end of listAllCustomers()</span></li>
</ol></div>

You can try this [example on JSBin](https://jsbin.com/xetumu).

[Local Demo](src/03f-example08.html)

It adds a button to our application. Clicking on it will display a set of alerts, each showing details of an object in the object store:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/36tlRZv')"
    src    = "https://bit.ly/3ANR9Ii"
    alt    = "Screenshot with a 'list all customers button' and an alert showing one of them"
    title  = "Screenshot with a 'list all customers button' and an alert showing one of them"
  />
</figure>


The `openCursor()` function can take several (optional) arguments.

+ First, you can limit the range of items that are retrieved by using a key range object - we'll get to that in a minute.
+ Second, you can specify the direction that you want to iterate.

In the above example, we're iterating over all objects in ascending order. The `onsuccess` callback for cursors is a little special. __The cursor object itself is the `result` property of the request__ (above we're using the shorthand, so it's `event.target.result`). Then __the actual key and value can be found on the key and value properties of the cursor object__. If you want to keep going, then you have to call `cursor.continue()` on the cursor.

When you've reached the end of the data (or if there were no entries that matched your `openCursor()` request) you still get a `success` callback, but the `result` property is undefined.

One common pattern with cursors is to retrieve all objects in an object store and add them to an array, like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> listAllCustomersArray</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln">&nbsp; &nbsp; </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">).</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="kwd">var</span><span class="pln"> customers </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span><span class="pln"> </span><span class="com">// the array of customers that will hold </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // results</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; objectStore</span><span class="pun">.</span><span class="pln">openCursor</span><span class="pun">().</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="kwd">var</span><span class="pln"> cursor </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">cursor</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; customers</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="pln">cursor</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span><span class="pln"> </span><span class="com">// add a customer in the </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // array</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; cursor</span><span class="pun">.</span><span class="kwd">continue</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">"Got all customers: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> customers</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun">};</span><span class="pln"> </span><span class="com">// end of onsuccess</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span><span class="com">// end of listAllCustomersArray()</span></li>
</ol></div>

You can try [this version on JSBin](https://jsbin.com/bitoqa).

[Local Demo](src/03f-example09.html)


__Getting data using an index__

Storing customer data using the `ssn` as a key is logical since the `ssn` uniquely identifies an individual. If you need to look up a customer by `name`, however, you'll need to iterate over every `ssn` in the database until you find the right one.

Searching in this fashion would be very slow. So instead we _use an index_.

Remember that we defined two indexes in our data store:

1. one on the `name` (non-unique) and
2. one on the `email` properties (unique).

Here is a function that examines by `name` the person-objects in the object store, and returns the first one it finds with a name equal to "Bill":

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> getCustomerByName</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">db </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'Database must be opened first, please click the Create </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CustomerDB Database first'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">return</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln">&nbsp; &nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">).</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="kwd">var</span><span class="pln"> index </span><span class="pun">=</span><span class="pln"> objectStore</span><span class="pun">.</span><span class="pln">index</span><span class="pun">(</span><span class="str">"name"</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong style="color: red;">index</strong></span><strong style="color: red;"><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="str">"Bill"</span><span class="pun">).</span><span class="pln">onsuccess </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">"Bill's SSN is "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><strong style="color: red;"><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">ssn </span></strong><span class="pun">+</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="str">" his email is "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><strong style="color: red;"><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">.</span><span class="pln">email</span></strong><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

The search by index occurs at _lines 11 and 13_: _line 11_ creates an "index" object that corresponds to the "name" property. _Line 13_ calls the `get()` method on this index-object to retrieve all of the person-objects from the dataStore which have a name equal to "Bill".

[Online example](https://jsbin.com/gituxa) you can try at JsBin

[Local Demo](src/03f-example10.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/36tlRZv')"
    src    = "https://bit.ly/3r6igKr"
    alt    = "retrieving data using an index. The screenshot shows a button 'look for all customers named Bill', and shows an alert with the result."
    title  = "retrieving data using an index. The screenshot shows a button 'look for all customers named Bill', and shows an alert with the result."
  />
</figure>


The above example retrieves only the first object that has a name/index with the value="Bill". Notice that there are two "Bill"s in the object store.

__Retrieving more than one result when using an index__

In order to get all the "Bills", once again we have to use _a cursor_.

When we work with indexes, we can open two different types of cursors on indexes:

1. __A normal cursor__ which maps the index property to the object in the object store, or,
2. __A key cursor__ which maps the index property to the key used to store the object in the object store.

The differences are illustrated below.

Normal cursor:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong style="color: red;"><span class="pln">index</span><span class="pun">.</span><span class="pln" style="color: #ff8800;">openCursor</span><span class="pun"><span style="color: #ff8800;">()</span>.</span><span class="pln">onsuccess </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><strong style="color: red;"><span class="kwd">var</span><span class="pln"> cursor </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">cursor</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// cursor.key is a name, like "Bill", and <strong style="color: red;"><span style="color: #ff8800;">cursor.value is the </span></strong></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // <span style="color: #ff8800;"><strong style="color: red;">whole object.</strong></span></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">"Name: "</span><span class="pln"> </span><span class="pun">+</span><strong style="color: red;"><span class="pln"> cursor</span><span class="pun">.</span><span class="pln">key </span></strong><span class="pun">+</span><span class="pln"> </span><span class="str">", SSN: "</span><span class="pln"> </span><span class="pun">+</span><span style="color: #ff8800;"><strong style="color: red;"><span class="pln"> cursor</span><span class="pun">.</span><span class="pln">value</span><span class="pun">.</span><span class="pln">ssn </span></strong></span><span class="pun">+</span><span class="pln"> </span><span class="str">", </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;email: "</span><span class="pln"> </span><span class="pun">+</span><strong style="color: red;"><span class="pln"> cursor</span><span class="pun">.</span><span class="pln">value</span><span class="pun">.</span><span class="pln">email</span></strong><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong style="color: red;">cursor</strong></span><strong style="color: red;"><span class="pun">.</span><span class="kwd">continue</span><span class="pun">();</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div>

Key cursor:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong style="color: red;"><span class="pln">index</span><span class="pun">.</span><span class="pln" style="color: #ff8800;">openKeyCursor</span><span class="pun">().</span><span class="pln">onsuccess </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> cursor </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">cursor</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com"><span style="color: #ff8800;">//</span> <span style="color: #ff8800;">cursor.key is a name, like "Bill",<strong style="color: red;"> and cursor.value is the </strong></span></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com" style="color: #ff8800;"><strong style="color: red;">&nbsp; &nbsp; &nbsp;</strong>//<strong style="color: red;"> SSN (the key)</strong>.</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// No way to directly get the rest of the stored object.</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">"Name: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> cursor</span><span class="pun">.</span><span class="pln">key </span><span class="pun">+</span><span class="pln"> </span><span class="str">", "</span><span class="pln">SSN</span><span class="pun">:</span><span class="pln"> </span><span class="str">" + <strong style="color: red;">cursor.value</strong>);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp;cursor.continue();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp;}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="str">};</span></li>
</ol></div>

Can you see the difference? 

You can try [an online example at JSBin](https://jsbin.com/kubuwof) that uses the above methods:

[Local Demo](src/03f-example11.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/36tlRZv')"
    src    = "https://bit.ly/36waTCl"
    alt    = "getting data using index. The screenshot shows two buttons: one for getting one single data and one for getting all data, using indexes"
    title  = "getting data using index. The screenshot shows two buttons: one for getting one single data and one for getting all data, using indexes"
  />
</figure>


How to try this example:

1. Press the create/Open CustomerDB database,
2. Add some more customers,
3. Then press the last button "look for all customers with name=Bill ...". This will iterate over all the customers in the object store whose name is equal to "Bill". There should be two "Bills", if this is not the case, add two customers with a name equal to "Bill", then press the last button again.

Source code extract from this example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> getAllCustomersByName</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">db </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">'Database must be opened first, please click the Create </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;CustomerDB Database first'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">return</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> objectStore </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;db</span><span class="pun">.</span><span class="pln">transaction</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">).</span><span class="pln">objectStore</span><span class="pun">(</span><span class="str">"customers"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd">var</span><span class="pln"> index </span><span class="pun">=</span><span class="pln"> objectStore</span><span class="pun">.</span><span class="pln">index</span><span class="pun">(</span><span class="str">"name"</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Only match "Bill"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd">var</span><span class="pln"> singleKeyRange </span><span class="pun">=</span><span class="pln"> </span><span class="typ">IDBKeyRange</span><span class="pun">.</span><span class="pln">only</span><span class="pun">(</span><span class="str">"Bill"</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong style="color: red;">index</strong></span><strong style="color: red;"><span class="pun">.</span><span class="pln">openCursor</span><span class="pun">(</span><span class="pln">singleKeyRange</span><span class="pun">).</span><span class="pln">onsuccess </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> cursor </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">cursor</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// cursor.key is a name, like "Bill", and cursor.value is the </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; // whole object.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">"Name: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> cursor</span><span class="pun">.</span><span class="pln">key </span><span class="pun">+</span><span class="pln"> </span><span class="str">", SSN: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> cursor</span><span class="pun">.</span><span class="pln">value</span><span class="pun">.</span><span class="pln">ssn</span><span class="pln">&nbsp;</span><span class="str">", </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+ email: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> cursor</span><span class="pun">.</span><span class="pln">value</span><span class="pun">.</span><span class="pln">email</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; cursor</span><span class="pun">.</span><span class="kwd">continue</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Notes for 3.6.10 Getting data

+ Typical syntax for adding/deleting/modifying/retrieving data
  + assign request: `var request = objectStore.get(keyPath);`
  + assign index: `var index = onjectStore.index(key);`
  + add new object: `request.add(object);`
  + remove a existing object: `request.delete(keypath);`
  + modify data from an object store w/ IndexedDB: `request.put(keypath);`
  + retrieve/search object w/ keyPath: `request.get(keyPath);`
  + search object w/ index: `index.get(key);`

+ Example: retrieving/searching data w/ key
  + search a customer: `function searchACustomer() {...}`
  + check [the connection to db](#connChk)
  + create [transaction](#transaction)
  + add [transaction complete handler](#transComplete)
  + add [transaction error handler](#transErr)
  + [init transaction to get object store](#initTrans)
  + init a customer w/ ssn: `var customerToSearch={}; customerToSearch.ssn = document.querySelector("#ssn").value;`
  + display msg for search: `alert('looking for customer ssn=' + customerToSearch.ssn);`
  + search for the customer w/ given ssn: `var request = objStore.get(customerToSearch.ssn);`
  + add request success handler: `request.onsuccess = function(evt) {...};`
    + log msg: `console.log("Customer found" + evt.target.result.name);`
    + assign name: `document.querySelector("#name").value = evt.target.result.name;`
    + assign age: `document.querySelector("#age").value = evt.target.result.age;`
    + assign email: `document.querySelector("#email").value = evt.target.result.email;`
  + add request error handler: `request.onerror = function(evt) { alert("request.onerror, errcode = " + evt.target.error.name + ". The ssn is not in the Database"); };`

+ Example: retrieving/searching data w/ key - short version
  + only one object store $\to$ not required to passing a list of object stores in transaction
  + read only: no need for "readwrite" transaction but default "readonly`
  + no request object required
  
  ```js
  function searchACustomerShort() {
    if (db === null) {
      alert('Database must be opened first, please click the Create CustomerDB Database first');
      return;
    }

    db.transaction("customer").objectStore("customer")
      .get(document.querySelector("#ssn").value)
      .onsuccess = function(evt) {
        document.querySelector("#name").value = evt.target.result.name;
        document.querySelector("#age").value = evt.target.result.age;
        document.querySelector("email").value = evt.target.result.email;
      } // end of onsuccess callback
  }
  ```

+ Searching for multiple objects
  + getting all of the data from the datastore using a `cursor`
  + [cursor](https://javascript.info/indexeddb#cursors)
    + a special object traversing the object storage, given a query, and returning one key/value at a time, thus saving memory
    + walking through the store in key order (ascending by default) as an object store stored internally by key
    + syntax: `let request = store.openCursor(query, [direction]);`
      + `query`: a key or key range, same as for `getAll`
      + `direction` (optional): 
        + `"next"`: the default, the cursor walks up from the record w/ the lowest key
        + `"prev"`: the reverse order, down from the record w/ the biggest key
        + `"nextunique"`, `"prevunique"`: same as above, but skip records w/ the same key 
  + `get()` requiring which key to retrieve
  + using a `cursor` object to step through all the values or a certain range in object
  + searching data via keyPath
    + the `onsuccess` callback for cursor and let `var cursor = evt.target.result;`
    + the `cursor` object = the result property of the request
    + the actual key and value able to be found on the key and value properties of the cursor object
    + call `cursor.continue()` to get the next object if required
    + reach end of the the data $\to$ get a `success` callback but w/ `result` property undefined

+ Example: retriving/searching more data
  + search all customers: `function listAllCustomers() {...}`
  + get object store with transaction<a name="transObjStore"></a>: `var objStore = db.transaction("customers").objectStore("customers");`
  + add cursor success handler: `objStore.openCursor().onsuccess = function(evt) {...};`
    + get cursor as the event result<a name="cursor"></a>: `var cursor = evt.target.result;`
    + check cursor existed: `if (cursor) { alert("name for SSN" + cursor.key + " is " + cursor.value.name); }`
    + check cursor non-existed: `else { alert("No more entries!"); }`

+ Example: retrieving/searching more data and storing in array
  + search all customers and keep in an array: `function listAllCustomerArray() {...}`
  + get [object store w/ transaction](#transObjStore)
  + declare the array of customers: `var customers = [];`
  + add cursor success handler: `objStore.openCursor().onsuccess = function(evt) {...};`
    + get [cursor as the event result](#cursor)
    + check cursor existed: `if (cursor) { customers.push(cursor.value); cursor.continue(); }`
    + check cursor non-existed: `else { alert("Got all customers: " + customers); }`

+ Example: getting data using an index
  + tasks:
    + create an `index` object corresponding to the "name" property
    + `get` method on the index-object to retrieve the person's object from the object store
  + search data via key: `function getCustomerByName() {...}`
  + get [object store w/ transaction](#transObjStore)
  + get index: `var index = objStore.index("name");`
  + add cursor success handler: `index.get("Bill").onsuccess = function(evt) { alert("Bill's SSN is " + evt.target.result.ssn + "his email is " + evt.target.result.email); };`

+ Types of cursors on indexes
  + __normal cursor__: mapping the index property to the object in the object store
  + __key cursor__: mapping the index property to the key used to store the object in the object store

+ Syntax for normal cursor
  + add cursor success handler: `index.openCursor().onsuccess = function(evt) {...}`
  + get cursor: `var cursor = evt.target.result;`
  + check cursor existence: `if (cursor) { alert("Name: " + cursor.key + ", SSN: " + cursor.value.ssn + ", email: " + cursor.value.email); cursor.continue(); }`

+ Syntax for key cursor
  + add key cursor success handler: `index.openKeyCursor().onsuccess = function(evt) {...}`
  + get cursor: `var cursor = evt.target.result;`
  + check cursor existence: `if (cursor) { alert("Name: " + cursor.key + ", SSN: " + cursor.value); cursor.continue(); }`

+ Example: searching w/ index
  + search all customer by name: `function searchAllCustomersByName() {...}`
  + check [the connection to db](#connChk)
  + create [transaction](#transaction)
  + create index: `var index = objStore.index("name");`
  + match name only w/ Bill: `var singleKeyRange = IDBKeyRange.only("Bill");`
  + add cursor success handler: `index.openCursor(singleKeyRange).onsuccess = function(evt) {...};`
    + get [cursor as the event result](#cursor)
    + check cursor existence: `alert("Name: " + cursor.key + ", SSN: " + cursor.value.ssn + ", email: " + cursor.value.email);`
    + retrieve next object: `customer.continue();`


### 3.6.11 Limiting the range of values in a cursor


#### Range and direction of cursor

How to specify the range and direction of cursors with IndexedDB?

It is possible to use a special object called IDBKeyRange, for "IndexedDB Key Range", and pass it as the first argument to `openCursor()` or `openKeyCursor()`. We can specify the bounds of the data we are looking for, by using methods such as upperBound() or lowerBound(). The bound may be "closed" (i.e., the key range includes the given value(s)) or "open" (i.e., the key range does not include the given value(s)). 

Let's look at some examples ([adapted from this MDN article](https://mzl.la/2VyUJG5)):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Only match "Donna"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> singleKeyRange </span><span class="pun">=</span><span class="pln"> </span><span class="typ">IDBKeyRange</span><span class="pun">.</span><span class="pln">only</span><span class="pun">(</span><span class="str">"Donna"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// Match anything past "Bill", including "Bill"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> lowerBoundKeyRange </span><span class="pun">=</span><span class="pln"> </span><span class="typ">IDBKeyRange</span><span class="pun">.</span><span class="pln">lowerBound</span><span class="pun">(</span><span class="str">"Bill"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">// Match anything past "Bill", but don't include "Bill"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> lowerBoundOpenKeyRange </span><span class="pun">=</span><span class="pln"> </span><span class="typ">IDBKeyRange</span><span class="pun">.</span><span class="pln">lowerBound</span><span class="pun">(</span><span class="str">"Bill"</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">// Match anything up to, but not including, "Donna"</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> upperBoundOpenKeyRange </span><span class="pun">=</span><span class="pln"> </span><span class="typ">IDBKeyRange</span><span class="pun">.</span><span class="pln">upperBound</span><span class="pun">(</span><span class="str">"Donna"</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// Match anything between "Bill" and "Donna", but not including "Donna"</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> boundKeyRange </span><span class="pun">=</span><span class="pln"> </span><span class="typ">IDBKeyRange</span><span class="pun">.</span><span class="pln">bound</span><span class="pun">(</span><span class="str">"Bill"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"Donna"</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// To use one of the key ranges, pass it in as the first argument of openCursor()/openKeyCursor()</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">index</span><span class="pun">.</span><span class="pln">openCursor</span><span class="pun">(</span><span class="pln">boundKeyRange</span><span class="pun">).</span><span class="pln">onsuccess </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> cursor </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">cursor</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // Do something with the matches.</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; cursor</span><span class="pun">.</span><span class="kwd">continue</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div>


#### Complete example

Adapted from an example on gitHub, today no more available ([original URL](https://bit.ly/2U5JeWk)):

Try [the online example at JsBin](https://jsbin.com/lawaju/edit) (enter "Gaming", "Batman" etc. as key range values):

[Local Demo](src/03f-example12.html)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3hCgEER" ismap target="_blank">
    <img style="margin: 0.1em;" height=350
      src   = "https://bit.ly/3yWrg7g"
      alt   = "Example of use of IdbKeyRange"
      title = "Example of use of IdbKeyRange"
    >
    <img style="margin: 0.1em;" height=350
      src   = "https://bit.ly/3hxNEhz"
      alt   = "IDBKeyRange in action"
      title = "IDBKeyRange in action"
    >
  </a>
</div>


#### Notes for 3.6.11 Limiting the range of values in a cursor

+ `IDBKeyRange` object
  + MDN Web Doc: [Specifying the range and direction of cursors](https://mzl.la/3xF01xV)
  + abbreviation of "IndexedDB Key Range"
  + passed as the 1st argument of `openCursor()` and `openKeyCursor()`
  + specifying the bounds of the data looking for
  + methods: `upperBound()` or `lowerBound()`
  + the bound probably "closed" (including the given value(s)) or "open" (excluding the given value(s))

+ Example: range of cursor
  + declare range for only one value: `var singleKeyRange = IDBKeyRange.only("Donna");`
  + set lower bound: `var lowerBoundKeyRange = IDBKeyRange.lowerBound("Bill");`
  + set open lower bound: `var lowerBoundOpenKeyRange = IDBKeyRange.lowerBound("Bill", true);`
  + set open upper bound: `var upperBoundOpenKeyRange = IDBKeyRange.upperBound("Donna", true);`
  + set close lower and open upper bounds: `var boundKeyRange = IDBKeyRange.bound("Bill", "Donna", false, true);`
  + add cursor success handler: `index.openCursor(boundKeyRange).onsuccess = fucntion(evt) { var cursor = evt.target.result; if (cursor) { //do sth.; cursor.continue(); }};`


### 3.6.12 Discussion and projects

Here is the discussion forum for this part of the course. Please post your comments/observations/questions and share your creations.


#### Suggested topics of discussion:

+ IndexedDB is certainly the most complex API presented in this course. However, using it is rather simple once you've climbed the learning curve. If you have prior experience with databases, can you tell your feelings in the forum?
+ If you found handy tools for using IndexedDB, or other external tutorials and examples, please share!


#### Optional projects:

+ Start from the examples provided in the IndexedDB course and adapt them in order to manage a database of the HTML5 interactive examples (also provided in this course). For example, objects stores in the datastore may be composed of:
  + the jsbin.com URL of the example,
  + a description,
  + the name of the week in which the example has been presented, and,
  + the name of the lesson in the chapter,
  + eventually, a screenshot for the example (URL, or if you are a bit of a geek, image content).
+ Produce an HTML page which contains your application. When loaded, it must populate the indexedDB database with at least 10 different examples, and display them in a table or in a list. The GUI must also provide a search form for retrieving all the examples from a given chapter. 





