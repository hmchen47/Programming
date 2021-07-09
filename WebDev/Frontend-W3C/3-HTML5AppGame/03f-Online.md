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







