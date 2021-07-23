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






