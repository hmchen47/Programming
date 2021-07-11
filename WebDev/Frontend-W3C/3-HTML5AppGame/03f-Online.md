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

+ key-value pairs
  + IndexedDB storing key=value pairs
  + values: complex objects (think of JSON objects)
  + keys: properties of the objects
  + creating indexes w/ any property of the objects for faster searching and ordering results
  + example: 
    + declare key-value pairs: `const customerData = [{ ssn: "444-44-4444", name: "Bill", age: 35, email: "bill@company.com" }, { ssn: "555-55-5555", name: "Donna", age: 32, email="donna@home.org" }];`
    + `customerData`: an array of "customers"
    + customer properties: `ssn` for social security number, a `name`, an `age` and an `email` address

+ IndexedDB and transaltion model
  + IndexedDB built on a transactional database model
  + operations in IndexedDB $\to$ operated in the context of a transaction
  + IndexedDB API provideing lots of objects represting indexes, tables, cursors, etc.
  + API tied to a particular transaction
  + unable to execute commands or open cursors outside a transaction
  + transaction committed automatically, unable to committ manually
  + useful when considering what might happen if a user opened two of the web app in two different tabs simultaneously

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
  + not "store" a value or "retrieve" a value out of the database but "request" that a datbase operation happens
  + database system notifying caller via a DOM event once operation done
  + the type of event specifying the success or failure of the operation
  + examples: `transaction.oncomplete`, `transaction.onsuccess`, `request.onerror`, etc.

+ IndexedDB and requests
  + requests:
    + objects receiving the success or failure DOM events
    + `onsuccess` and `onerror` properties
  + using `addEventListener()` and `removeEventListener()` to add and remove listeners
  + status of a request: `readyState`, `result`, and `errorCode`
  + meaning of `result` depending on how the request eas generated, e.g., `IDBCursor` instance or the key for a value

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
  + every database having a name to identify itself within the originn
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
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> objectStore</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">customerData</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>request</strong></span><strong><span class="pun">.</span><span class="pln">onsuccess </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
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
    + used to identifY a databas within a specific origin
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
  + the mechanism by which data is stored in the datbase
  + name of object store
    + must have property
    + unique within the database to which it belongs
  + records (JavaScript objects)
    + key-value pairs persistently held
    + one of these keys as a kind of "primary key" in the SQL database sense
    + key: a property that every object in the datastore must contain
    + values: structured but probably varied bte objects
    + example: person contacts in database, email as "the key all objects must define", some amy have first name and last name. others may have abn address or no address at all
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
  + changing the the version by opening it w/ a higher version number tha the current one
  + syntax: starting a `versionchange` transaction and triggering an `upgradeneeded` event
  + the handler of the event: only place to update the schema of the database
  + `IDBDatabase.setVersion()` method deprecated

+ Transaction
  + an atomic and durable set of data-access and data-modification operation
  + used to interact w/ the data in a database
  + data read and written to the datbase done by using a transaction
  + mode:
    + type: `read`, `readwrite`, or `versionchange`
    + determining which types of interaction performed upon that transaction
    + set when transaction created amd remain fixed for the life of the transaction
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
    + multiple reads allowed at the same time while writes in sequence, only one at a timeoverlapped
    + a `versionchange` transaction
      + never runs concurrently w/ other transactions
      + automatically created when a database w/ higher version number is provided
      + transaction activated inside the `onupgradeneeded` event handler, allowing the creation of new object stores and indexes
    + `readwrite` transactions w/ overlapped scopes always run in the order they were created and never run in parallel
  + example:
    + existing a writing transaction in a database connection
    + scope of the transaction covering only the `flyingMonkey` object store
    + starting a second transaction w/ a scope of the `unicornCentaur` and `unicornPegasus` object stores
    + allowing several reading transactions and probably 

+ Request
  + issued as the reading and writing on a database done
  + represeting one read or one write operation
  + always run within a transaction
  + example: add a customer to the object store named "customers"
    + [access data](#objStore)
    + iterate through to [add data](#addData)

+ Index
  + sometimes useful to retrieve records from an object store through means their than their key
    + allowing the user to look up records in an object store by using the properties of the values inb the object store's records
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
  + a key stored separately from the value being store
  + an auto-incremental id not part of the 

+ Key path
  + where the browser should extract the key from a value in the object store or index
  + valid key path including one of
    + an empty string
    + a JavaScript identifier
    + multiple JavaScript identifiers separated by period w/o spaces

+ Value
  + each record w/ a value
  + anything abel to be expresseds in JavaScript, including, boolean, number, string, date, object, array, regexp, undefined and null
  + object/array: the properties and values in it able to be anything but valid
  + blog and files support by all major browsers, IE > 9

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








