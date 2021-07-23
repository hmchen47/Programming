# IndexedDB


## Concepts

+ [IndexedDB overview](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-361-concepts-part-1)
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

+ [Summary of IndexedDB](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-361-concepts-part-1)
  + IndexedDB: a transactional Object Store where able to store JavaScript objects
  + indexes on same properties of these objects facilitate faster retrieval and search
  + applications using IndexedDB able to work both online and offline
  + IndexedDB transactional: managing concurrent access to data

+ [Resources](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-361-concepts-part-1)
  + [IndexedDB API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)
  + [IndexedDB key characteristics and basic terminology](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology)
  + [Using IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB)
  + [W3C Indexed Database API](https://www.w3.org/TR/IndexedDB/)
  + R. Dabler, [Getting Started with Persistent Offline Storage with IndexedDB](https://bit.ly/3hoTemr)


+ [Main concepts of IndexedDB](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
  + store and retrive objects indexed by a key
  + transaction: changes to the databases
  + same-origin policy: only accessing data within the same domain, not able to access across domains
  + extensive use of an asynchronous API: most processing done in callback functions




## KeyPath

+ [Keypath](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
  + a must-have property defined by object stores
  + equivalent to Primary key in relational database
  + unique
  + able to be explicit (ssn) or implicit (auto-incremented primary key in SQL) 
  + implicit KeyPath: not appeared in the stored objects themselves
  + stored objects w/o a rigidly defined schema
  + only key to be shared, other keys probably varying btw stored objects
  + example: `{firstName: 'Michel', lastName: 'Buffa', ssn: "1122334455"}` $\to$ ssn as Keypath




## Indexes

+ [Indexes](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
  + stored object able to have one or more indexes $\to$ faster searching
  + a common concept in database
  + unique or non-unique
  + making lookup possible using any arbitrary property of the store objects
  + speeding up object retrieval and allowing multi-criteria searches
  + possible to have non unique indexes $\to$ all matching objects
  + example: "lastName" property of each person as an index $\to$ make search faster for some persons by "lastName"

+ [Key-value pairs](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
  + IndexedDB storing key-value pairs
  + values: complex objects (think of JSON objects)
  + keys: properties of the objects
  + creating indexes w/ any property of the objects for faster searching and ordering results
  + example: 
    + declare key-value pairs<a name="cxData"></a>: `const customerData = [{ ssn: "444-44-4444", name: "Bill", age: 35, email: "bill@company.com" }, { ssn: "555-55-5555", name: "Donna", age: 32, email="donna@home.org" }];`
    + `customerData`: an array of "customers"
    + customer properties: `ssn` for social security number, a `name`, an `age` and an `email` address




## Transaction

+ [Transaction](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
  + transactional database: ensuring concurrent access to data not compromised
  + using "locking system" to prevent compromising
  + scenarios to lock system
    + multiple tabs opened on the same WebApp (same domain)
    + multiple apps running "out of traditional browser" (game console, windows desktop, etc.)

+ [IndexedDB and transaltion model](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
  + IndexedDB built on a transactional database model
  + operations in IndexedDB $\to$ operated in the context of a transaction
  + IndexedDB API providing lots of objects representing indexes, tables, cursors, etc.
  + API tied to a particular transaction
  + unable to execute commands or open cursors outside a transaction
  + transaction committed automatically, unable to committ manually
  + useful when considering what might happen if a user opened two of the web apps in two different tabs simultaneously

+ [Typical syntax of a transaction](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
  + open a transaction for reading and writing  on the DB "customer": `var transaction = db.transaction("customers", "readwrite");`
  + add complete listener: `transaction.oncomplete = function(evt) { alert("All done!"); };`
  + add error listener: `transaction.onerror = function(evt) { // error handling };`
  + access data<a name="objStore"></a>: `var objectStore = transaction.objectStore("costomers");`
  + iterate through to add data<a name="addData"></a>: `for (var i in customerData) {...}`
    + add data: `var request = objectStore.add(customerData[i]);`
    + add success listener: `request.onsuccess = function(evt) { // evt.target.result === customerData[i].ssn };`



## Asynchronous IDB API

+ [IndexedDB API and asynchronous](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
  + most IndexedDB API asynchronous
  + API not providing returned data but passed a callback function
  + not "store" a value or "retrieve" a value out of the database but "request" that a database operation happens
  + database system notifying caller via a DOM event once operation done
  + the type of event specifying the success or failure of the operation
  + examples: `transaction.oncomplete`, `transaction.onsuccess`, `request.onerror`, etc.

+ [IndexedDB and requests](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
  + requests:
    + objects receiving the success or failure DOM events
    + `onsuccess` and `onerror` properties
  + using `addEventListener()` and `removeEventListener()` to add and remove listeners
  + status of a request: `readyState`, `result`, and `errorCode`
  + meaning of `result` depending on how the request was generated, e.g., `IDBCursor` instance or the key for a value

+ [IndexedDB and DOM events](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
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




## Object-Orientation

+ [IndexedDB and object-oriented](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
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




## Same-Origin Policy

+ [Same-origin policy](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-362-concepts-part-2)
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





