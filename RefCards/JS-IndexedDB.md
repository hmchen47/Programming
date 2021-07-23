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

+ [Database](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
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



## Creation and Deletion IDB

+ [Creating database](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-365-creating-and-deleting-a-database)
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

+ Example: [creating database](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-365-creating-and-deleting-a-database)

+ [Deleting the database](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-365-creating-and-deleting-a-database)
  + syntax: `indexedDB.deleteDatabase("dbName");`
  + common practice for learner: execute the command in devtools > console



## Object Stores

+ [Object store](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
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




## Version

+ [Version](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
  + version 0: a database first created
  + one version ar a time
  + no multiple versions existed at once
  + changing the version by opening it w/ a higher version number tha the current one
  + syntax: starting a `versionchange` transaction and triggering an `upgradeneeded` event
  + the handler of the event: only place to update the schema of the database
  + `IDBDatabase.setVersion()` method deprecated



## Key

+ [Key](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
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
  
+ [Key generator](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
  + a mechanism for producing new key in an ordered sequence
  + an object store w/o a key generator $\to$ application must provide keys for records being stored
  + similar to auto-generated primary keys in SQL databases

+ [In-line key](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
  + a key stored as part of of the stored 
  + found using a key path
  + probably generated using a generator
  + stored in the value using the key path or used as a key once generated
  + example: the email of a person or a student number in an object representing a student in a student store

+ [Out-of-line key](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
  + a key stored separately from the value being stored
  + an auto-incremental `id` not part of the key




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

+ [Key path](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
  + where the browser should extract the key from a value in the object store or index
  + valid key path including one of
    + an empty string
    + a JavaScript identifier
    + multiple JavaScript identifiers separated by period w/o spaces




## Values

+ [Value](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
  + each record w/ a value
  + anything abel to be expressed in JavaScript, including, boolean, number, string, date, object, array, regexp, undefined and null
  + object/array: the properties and values in it able to be anything but valid
  + blog and files supported by all major browsers, IE > 9




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

+ [Index](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
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

+ [Transaction](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
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

+ [Transaction w/ data](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-366-working-with-data)
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




## Scope

+ [Scope](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
  + the set of object stores and indexes to which a transaction applies
  + read-only transactions: able to overlap and execute at the same time
  + writing transaction:
    + unable to overlap
    + multiple transactions w/ same scope at the same time allowed but queue up and execute in sequence





## Request

+ [Request](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
  + issued as the reading and writing on a database done
  + represeting one read or one write operation
  + always run within a transaction
  + example: add a customer to the object store named "customers"
    + [access data](#objStore)
    + iterate through to [add data](#addData)



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



## Cursor

+ [Cursor](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
  + a mechanism for iterating over multiple records within a key range
  + existing a source defining which index or object store it is iterating
  + having a position within the range
  + retrieving records sequentially according to the value of their keys in descending or ascending way

+ [Key range](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-363-definitions)
  + a continuous interval over some data type used for keys
  + retrieving records via object stores and indexes using keys or a range of keys
  + able to limit and filter the range using lower and upper bounds
  + example: iterate over all values of a key btw x and y



## Inserting, Removing and Modifying Records

+ [Typical procedure to inset data](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-367-inserting-data)
  + create a transaction
  + map the transaction onto the object store
  + create an "add" request that will take part in the transaction

+ Example: [basic steps](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-367-inserting-data)
  + tasks
    + get a transaction on the "customer" object store in `readwrite` mode
    + init transaction on the ObjectStore
    + get request from the transaction for adding a new object

+ Example: [adding data to DB from a form](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-367-inserting-data)
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

+ Example: [removing data](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-368-removing-data)
  + procedure
    + click "create database button" to ensure the open of the existing database
    + use devtools to check the customer w/ `ssn=444-44-4444`, if not existed, add the customer from the input forms
    + refresh IndexedDB in devtools to observe the customer
    + click the "Remove the customer" button and observe the data object in devtools after refreshing

+ Example: [modifying data](../WebDev/Frontend-W3C/3-HTML5AppGame/03f-Online.md#notes-for-369-modifying-data)






