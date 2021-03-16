# Module 5: Working with forms


## 5.4 The JSON notation

### 5.4.1 What is JSON?


#### Live coding video: JSON notation, working with LocalStorage and remote data

<a href="https://edx-video.net/W3CJSIXX2016-V005000_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/s8z7kkhc)


JSON stands for <b>J</b>ava<b>S</b>cript <b>O</b>bject <b>N</b>otation. It's a standard for transforming nearly any object into a string representation that is human readable. It became a standard for exchanging data to/from a remote HTTP server, and is available for many other languages in addition to JavaScript.

A JavaScript object o in JSON looks a lot like what `o.toString()` returns.

<div style="border: 1px solid; margin: 20px; padding: 20px;">
<p><strong>There are two main methods to know:</strong></p>
<ol><ol>
<li><span style="color: #ff0000;">Transform any JavaScript object in JSON</span>: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="font-family: 'courier new', courier;"><strong>var jsonStr =&nbsp;</strong><strong>JSON.stringify(obj);</strong></span></li>
<li><span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif; color: #ff0000;">Transform any JSON string into a JavaScript object: &nbsp; &nbsp;<span style="font-family: 'courier new', courier; color: #008888;"><strong>var jsObj &nbsp;= JSON.parse(jsonStr);</strong></span></span></li>
</ol></ol></div>

Let's see some examples:

<div class="source-code"><ol>
<li value="1">&gt; var x = 3;</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt;<strong> JSON.stringify(x);</strong></li>
<li>"3"</li>
<li>&nbsp;</li>
<li>&gt; var&nbsp;simpleObject&nbsp;= {x:12, y:30};</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt;<strong> JSON.stringify(<span style="color: #008888;" color="#008888">simpleObject);</span></strong></li>
<li>"{"x":12,"y":30}"</li>
<li>&nbsp;</li>
<li>&gt; var anArray&nbsp;= ['Monday', 'Tuesday', 'Wednesday'];</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt;<strong> JSON.stringify(anArray);</strong></li>
<li>"["Monday","Tuesday","Wednesday"]"</li>
<li>&nbsp;</li>
<li>&gt; var&nbsp;complexObject&nbsp;= {name:'Metallica', </li>
<li>&nbsp; &nbsp; albums:[</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; {name:"Master of Puppets", year:1986}, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; {name:"Black Album", year:1991}</li>
<li>&nbsp; &nbsp; ]</li>
<li>&nbsp; };</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt;<strong> JSON.stringify(<span style="color: #008888;" color="#008888">complexObject);</span></strong></li>
<li>"{"name":"Metallica","albums":[{"name":"Master of Puppets","year":1986},{"name":"Black Album","year":1991}]}"</li>
</ol></div>

In the above examples, you can see JSON representations of a simple variable of a predefined type, of an array, of a simple object, of an object that contains an array of objects (Metallica example).

And indeed, it looks like the code you typed to create the objects, with quotes around it and around the property names. This is why it is called JavaScript Object Notation ;-)


#### JSON objects as JavaScript objects

__You cannot use JSON objects as JavaScript objects__

The JSON representation of JavaScript objects is a string. JSON has been developed mainly for replacing XML as a format for exchanging data between a client and a remote HTTP server. It has become very popular as the format for exchanging data when a Web Application uses Ajax for its communications with the HTTP server. Ajax is a way to send / receive data in the background, without the need to reload the Web page. Along with the DOM API, the appearance of this technology in 2005 with Internet Explorer, made it possible to make Web pages more dynamic. Google Maps was one of the first popular Ajax-powered Web application: as you moved the map, new parts arrived (downloaded in the background from the Gmap HTTP server), and the page updated to display these new parts.

JSON is also very practical for storing objects where strings are expected. There is a data store in your browser called LocalStorage that can be used as a small database for Web applications, but it stores only pairs of key/values in the string format. If you want to save a JavaScript object, you will have to turn it into JSON, then save it. When you read it from the data store, you will need to turn it back from JSON to JavaScript.

Here is a first example that turns an object into JSON and back into a JavaScript object:

<div class="source-code"><ol>
<li value="1">&gt; var metallica = {name:'Metallica', albums:[{name:"Master of Puppets", year:1986}, <br>&nbsp; &nbsp; &nbsp; &nbsp;{name:"Black Album", year:1991}]};</li>
<li>undefined</li>
<li></li>
<li>&gt; var metallicaJSON = JSON.stringify(metallica);</li>
<li>undefined</li>
<li></li>
<li>&gt; metallicaJSON;</li>
<li>"{"name":"Metallica","albums":[{"name":"Master of Puppets","year":1986},<br>&nbsp; &nbsp; &nbsp; &nbsp;{"name":"Black Album","year":1991}]}"</li>
<li></li>
<li>&gt; metallicaJSON.name; // metallicaJSON is not a JavaScript object</li>
<li>undefined</li>
<li></li>
<li>&gt; metallica.name; // metallica is an object</li>
<li>"Metallica"</li>
<li></li>
<li>&gt; var obj = JSON.parse(metallicaJSON); // JSON -&gt; object</li>
<li>undefined</li>
<li></li>
<li>&gt; obj.name; // this is&nbsp;an object</li>
<li>"Metallica"</li>
</ol></div>

With the JSON representation of an object you cannot access the original object's properties using the "." operator, nor call its methods. __The JSON format only stores the list of the object properties (name and value) as a string.__ Look at _line 10_: we cannot access the name property of the JSON representation of the `metallica` object defined at line 1.

When we parse a JSON string using `JSON.parse()`, we get a real JavaScript object, and we can access its properties (_lines 16 and 19_).


#### Notes for 5.4.1 What is JSON?

+ JavaScript Object Notation (JSON)
  + a standard for transforming nearly any object into a string representation
  + a standard for exchangig data to/from a remote HTTP server
  + available for many other languages
  + developed mainly for replacing XML as a format for exchanging data btw a client and HTTP server
  + popularity: as the format for exchanging data under Ajax to communicate btw Web Applications and the HTTP server
  + MS IE 2005: first appearance
  + Google Maps: one of the first popular Ajax-powered Web application
  
+ JSON objects and JavaScript objects
  + unable to use JSON object as JS object
  + JSON representation of JS object: a string
  + JSON format: only storing the list of object properties (name and value) as a string
  + main methods
    + JS object $\to$ JSON: `var jsonStr = JSON.stringify(obj);`
    + JSON $\to$ JS object: `var jsObj = JSON.parse(jsonStr);`
  + representations of a simple variable of a predefined type, of an array, of a simple object, of an object containing an array of object
  + visual: an object created in JS code w/ quote around it and the property name
  + JSON very practical for storing objects where string are expected
  + LocalStorage:
    + a data store in browser to store a small database for Web application
    + store only pairs of key/values in the string format
    + convert into JSON object to save a JS object

+ Example: JS object $\to$ JSON
  + number to JSON: `var x = 3; JSON.stringify(x); // "3"`
  + simple object to JSON: `var simpleObj = {x: 12, y: 30}; JSON.stringify(simpleObj); // "{"x":12,"y":30}"`
  + array to JSON: `var anArray = ['Monday', 'Tuesday', 'Wednesday']; JSON.stringify(anArray); // "["Monday","Tuesday","Wednesday"]"`
  + complex object to JSON:

    ```js
    var complexObject = {name:'Metallica',
      albums:[
          {name:"Master of Puppets", year:1986},
          {name:"Black Album", year:1991}
      ]
    };

    JSON.stringify(complexObject); 
    // "{"name":"Metallica","albums":[{"name":"Master of Puppets","year":1986},
    //  {"name":"Black Album","year":1991}]}"
    ```

+ Example: JS object $\leftrightarrow$ JSON
  + declare object: `var metallica = {name:'Metallica', albums:[{name:"Master of Puppets", year:1986}, {name:"Black Album", year:1991}]};`
  + JS object $\to$ JSON: `var metallicaJSON = JSON.stringify(metallica);`
  + display JSON: `metallicaJSON; // "{"name":"Metallica","albums":[{"name":"Master of Puppets","year":1986}, {"name":"Black Album","year":1991}]}"`
  + JSON format not a JS object: `metallica.name; // undefined`
  + convert back to JS object: `var obj = JSON.parse(metallicaJSON); obj.name; // "Metallica"`

+ [`JSON.stringify()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)

+ [`JSON.parse()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)


### 5.4.2 Consuming JSON remote data


#### Live coding Video: Xhr2, remote JSON data, dynamic table

<a href="https://edx-video.net/W3CJSIXX2016-V005100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/2583mdt3)

__Source code from the above live coding video__

[CodePen Demo](https://codepen.io/w3devcampus/pen/bRRjvv?editors=0011)

[Local Demo](src/05d-example01.html)


#### JSON data from a REST Web Service

Most "big sites" provide what we call a REST API. This means "they propose to send/receive data to/from programs over HTTP", and most of the time the JSON format is one of the possible transport formats for the data. Google APIs, Facebook and Amazon APIs are like this.

JSONPlaceholder is a free online REST service that you can use whenever you need some fake data in JSON. Faking a server is great for tutorials, and this is exactly what the next example does. It will consume data from [this URL](https://jsonplaceholder.typicode.com/users).

Please click on it - you will see some JSON data coming from the server and being displayed in your browser:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://tinyurl.com/4t6djrf7')"
    src    = "https://tinyurl.com/p9drwnen"
    alt    = "JSON data coming from https://jsonplaceholder.typicode.com/users"
    title  = "JSON data coming from https://jsonplaceholder.typicode.com/users"
  />
</figure>

And we would like to use these data in our code, manipulating them as a JavaScript object.

This course does not cover Ajax and what we call "asynchronous JavaScript". However, we can show you two simple examples that use the Xhr2 API for Ajax requests and the new fetch API that is simplest to use.


#### Examples

__Downloading JSON data using the Xhr2 API__

[CodePen Demo](https://codepen.io/w3devcampus/pen/vmLMRN)

[Local Demo](src/05d-example02.html)

JavaScript source code extract:

<div class="source-code"><ol>
<li value="1">function search() { </li>
<li>&nbsp; &nbsp; var queryURL = "https://jsonplaceholder.typicode.com/users";</li>
<li> </li>
<li>&nbsp; &nbsp; var xhr = new XMLHttpRequest();</li>
<li>&nbsp; &nbsp; xhr.open('GET', queryURL, true);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; // called when the response has arrived</li>
<li>&nbsp; &nbsp; xhr.onload = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>var</strong><strong> jsonResponse = this.response;</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>// turn the response into a JavaScript object</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>var</strong><strong> users = JSON.parse(jsonResponse);</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; displayUsersAsATable(users);</li>
<li>&nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; // in case of error</li>
<li>&nbsp; &nbsp; xhr.onerror = function(err) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log("Error: " + err);</li>
<li>&nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; // sends the request</li>
<li>&nbsp; &nbsp; xhr.send();</li>
<li>} </li>
</ol></div>

__Explanations:__

+ _Lines 4 and 5_ build an Ajax request using XhR2.
+ _Line 22_ is executed after: the request is sent in the background (we say "asynchronously").
+ _Line 8_: when the server answers, this callback is executed, and inside it, this.response corresponds to the response from the HTTP server. It's in JSON format (_line 9_)
+ _Line 12_: we turn the JSON response into a regular JavaScript object we can work with, using `JSON.parse()`.
+ _Line 13_: we pass this list of users, now a JavaScript object, to the displayUsersAsATable method, that will use the HTML table API we saw earlier in the course.



#### [Advanced] Downloading JSON data using the fetch API

The [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) provides a JavaScript interface for accessing and manipulating parts of the HTTP pipeline, such as requests and responses. It also provides a global [fetch()](https://developer.mozilla.org/en-US/docs/Web/API/GlobalFetch/fetch) method that provides an easy, logical way to fetch resources asynchronously across the network. You __fetch__ data from a URL, __then__, you do something with the response, then you do something else. If there is an error you can __catch__ this error and display, for example, an error message.

See [this blog post](https://javascript.info/fetch-api) for a detailed tutorial. Asynchronous JavaScript and JavaScript promises (the fetch...then...then... is based on the concept of "promises") is not detailed in this course.

[CodePen Demo](https://codepen.io/w3devcampus/pen/xgoZdg)

[Local Demo](src/05d-example03.hrml)

JavaScript source code extract:

<div class="source-code"><ol>
<li value="1"> function search() { </li>
<li>&nbsp; &nbsp; var queryURL = "https://jsonplaceholder.typicode.com/users";</li>
<li> </li>
<li>&nbsp; &nbsp; fetch(queryURL)</li>
<li>&nbsp; &nbsp; &nbsp; .then(function(response) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>// response is a json string,</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // convert it to a pure JavaScript object</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return response.json();</strong></li>
<li>&nbsp; &nbsp; &nbsp; })</li>
<li>&nbsp; &nbsp; &nbsp; .then(function(users) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong> // users is a JavaScript object here</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayUsersAsATable(users)</li>
<li>&nbsp; &nbsp; &nbsp; })</li>
<li>&nbsp; &nbsp; &nbsp; .catch(function(error) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console.log('Error during fetch: ' + error.message);</li>
<li>&nbsp; &nbsp; &nbsp; });</li>
<li> }</li>
</ol></div>

The fetch API will also be covered in an advanced JavaScript course to come. In contrast to XhR2, fetch is based on a concept called "JavaScript promises" (also covered in the advanced course!). You recognize promises when you see ".then..." ".then...".


#### Notes for 5.4.2 Consuming JSON remote data

+ JSON data w/ REST service
  + REST API: send/receive data to/from programs over HTTP
  + JSON format: one of the possible transport formats for the data
  + [JSONPlaceholder](https://jsonplaceholder.typicode.com/users)
    + a free online REST service
    + provide fake data in JSON
  + Xhr2 (XML HTTP Request 2) API: Ajax requests w/ newly simplied fetch API
  + [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
    + provide a JS interface for accessing and manipulating parts of th HTTP pipeline
    + global `fetch()` method:
      + provide an easy, logical way to fetch resources asynchronous across the network
      + fetch data from a URL, then processing w/ response
    + catch error and display error message

+ Example: [JSON data w/ Xhr2 API](src/05d-example02.html)
  + button element: `<button onclick="search();">Get a remote list of users' names and emails</button>`
  + empty container for display: `<div id="users"></div>`
  + request function: `function search() {...}`
    + build an Ajax request using Xhr2: `var queryURL = "https://jsonplaceholder.typicode.com/users"; var xhr = new XMLHttpRequest();`
    + asynchronously send the request: `xhr.send();`
    + open the connection: `xhr.open('GET', queryURL, true);`
    + callback executed to response arrival: `xhr.onload = function(e) {...}`
      + create object to store response: `var jsonResponse = this.response;`
      + covert data into JSON: `var users = JSON.parse(jsonResponse);`
      + display users w/ HTML table: `displayUsersAsTable(users);`
    + callback for error handling: `xhr.onerror = function(err) { console.log("Error " + err); }`
  + display info: `function displayUsersAsATable(users) {...}`
    + empty the container: `var usersDiv = document.querySelector("#users"); usersDiv.innerHTML = "";`
    + create a table within container: `var table = document.createElement("table");`
    + iterate to display each row: `users.forEach(function(currentUser)) {...});`
      + insert row: `var row = table.insertRow();`
      + display HTML data: `row.innerHTML = "<td>"+ currentUser.name+ "</td><td>" + currentUser.email + "</td>";`
    + append table: `usersDiv.append(table);`

+ Example: [JSON data w/ the fetch API](src/05d-example03.html)
  + request function: `function search() {...}`
    + specify the URL: `var queryURL = "https://jsonplaceholder.typicode.com/users";`
    + fetch data:

      ```js
      fetch(queryURL)
        .then(function(response) { // convert to a pure JavaScript object
            return response.json();
        })
        .then(function(users) { // users is a JavaScript object here
          displayUsersAsATable(users)
        })
        .catch(function(error) {
          console.log('Error during fetch: ' + error.message);
        });
      ```


### 5.4.3 The LocalStorage API

Let's look at an example of use: the LocalStorage API as a client-side database for JavaScript objects

#### The Web Storage API (`localStorage`, `sessionStorage`)

The Web storage API (see the [related W3C specification](https://www.w3.org/TR/webstorage/)) introduces "two related mechanisms, similar to HTTP session cookies, for storing structured data on the client side".

Indeed, Web Storage provides two interfaces - `sessionStorage` and `localStorage` - whose main difference is data longevity. This specification defines an API for persistent data storage of key-value pair data in Web clients.

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong>With&nbsp;<span style="font-family: 'courier new', courier;">localStorage</span>&nbsp;the data will remain until it is deleted, whereas with&nbsp;<span style="font-family: 'courier new', courier;">sessionStorage</span>&nbsp;the data is erased when the tab/browser is closed.</strong></p>

For convenience, we will mainly illustrate the `localStorage` object. Just change "local" to "session" and it should work (this time with a session lifetime).


__Simple key-value stores, one per domain (following the [same origin policy](https://en.wikipedia.org/wiki/Same-origin_policy))!__

`localStorage` is a simple key-value store, in which the keys and values are strings. There is only one store per domain. This functionality is exposed through the globally available `localStorage` object. The same applies to `sessionStorage`.

Example:

<div class="source-code"><ol>
<li value="1">// Using localStorage</li>
<li></li>
<li>// store data</li>
<li>localStorage.lastName&nbsp;=&nbsp;"Bunny";</li>
<li>localStorage.firstName&nbsp;=&nbsp;"Bugs";</li>
<li>localStorage.location&nbsp;=&nbsp;"Earth";</li>
<li></li>
<li>// retrieve data</li>
<li>var&nbsp;lastName&nbsp;=&nbsp;localStorage.lastName;</li>
<li>var&nbsp;firstName&nbsp;=&nbsp;localStorage.firstName;</li>
<li>var&nbsp;location&nbsp;=&nbsp;localStorage.location;</li>
</ol></div>

This data is located in a store attached to the origin of the page. We've created a JsBin example in which we've included the above code.

[JsBin Demo](http://jsbin.com/hebino/1/edit?html,output)

[Local Demo](src/05d-example04.html)

Once opened in your browser, the JavaScript code is executed. With the browser dev. tools, we can check what has been stored in the `localStorage` for this domain:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/9hy8ejpa" ismap target="_blank">
    <img style="margin: 0.1em;" height=300
      src   = "https://tinyurl.com/5hw7z2ea"
      alt   = "example of localStorage"
      title = "example of localStorage"
    >
    <img style="margin: 0.1em;" height=300
      src   = "https://tinyurl.com/57a8mhep"
      alt   = "dev tools can be used to show what is in the local storage"
      title = "dev tools can be used to show what is in the local storage"
    >
  </a>
</div>


#### Differences with cookies?

Cookies are also a popular way to store key-value pairs. Web Storage, however, is a more powerful technique than cookies. The main difference is in size limits: cookies are limited to a few KBytes whereas Web Storage may extend to several MBytes. Also, cookies generate additional HTTP request traffic (whether to request a Web page, an image, a stylesheet, a JavaScript file, etc.).

Objects managed by Web Storage are no longer carried on the network and HTTP, and are easily accessible (read, change and delete) from JavaScript, using the Web Storage API.

#### External resources

+ [The W3C Web Storage API recommendation](http://www.w3.org/TR/webstorage/)
+ [An Overview of Client-Side Storage](https://css-tricks.com/overview-client-side-storage/)


#### Notes for 5.4.3 The LocalStorage API

+ The Web Storage API
  + two mechanisms, similar to HTTP session cookies, for storing structured data on the client side
  + providing two interfaces: `sessionStorage` and `localStorage`
  + difference btw `sessionStorage` and `localStorage`: longevity
    + `sessionStorage`: remain until deleted
    + `localStorage`: erased when tab/browser closed
  + define an API for persistent data storage of key-value pair data in Web service

+ Key-value stores
  + keys & values: strings
  + only one store per domain
  + functionality: expose through the globally available `localStorage`/`sessionStorage` object

+ Example: [store and retrieve data](src/05d-example04.html)
  + set `localStore` store data: `localStorage.lastName = "Bunny"; localStorage.firstName = "Bugs"; localStorage.location = "Earth";`
  + retrieve data: `var lastName = localStorage.lastName; var firstName = localStorage.firstName; var location = localStorage.location;`

+ Web Storage vs cookies
  + cookie:
    + a popular way to store key-value pair
    + generate additional HTTP request traffic
  + Web Storage:
    + more powerful technique than cookie
    + managed objects no longer carried on the network and HTTP
    + easily accessible (read, change, and delete) from JS via API
  + difference
    + cookie: limited to a few KBytes
    + Web Storage: may extend to several MBytes

+ [`XMLHttpRequest` (XHR) object](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
  + used to interact w/ servers
  + able to retrieve data from a URL w/o a full page refresh
  + enable a Web page to update just part of a page w/o disrupting what the user is doing
  + heavily used in AJAX programming

+ [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
  + provide an interface for fetching resources (including across the network)
  + provide a generic definition of `Request` and `Response` objects
  + define related concepts such as CORS and the HTTP Origin header semantics, supplanting their separate definition elsewhere
  
+ [`WindowOrWorkerGlobalScope.fetch()` method](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch)
  + syntax: `const fetchResponsePromise = fetch(resource [, init])`
  + docstring:
    + starts the process of fetching a resource from the network
    + return a `Promise` object (the eventual completion/failure of ab asynchronouse operation) that resolves to the `Response` to the request
  + parameters
    + `resource`: define the resource to fetch
      + a string or any other object w/ a `stringifer`, including a URL object
      + a `Request` object
    + `init` (optional): object containing any customer settings applied to the request
      + `method`: request method, e.g., `GET`, `POST`
      + `headers`: any headers added to the request contained within a Header object or an object literal w/ ByteString values
      + `body`: any bod added to the request, including `Blob`, `BufferSource`, `FormData`, `URLSearchParams`, `USVString`, or `ReadableStream` objects
      + `mode`: mode used for the request, e.g., `1cors`, `no-cors`, or `same-origin`
      + `credentials`: control what browsers do w/ credentials (cookies, HTTP authentication entries, and TLS client certificates)
      + `redirect`: how to handle a `redirect` response, including `follow`, `error`, and `manual`
      + `referrer`: a `USVString` specifying the referrer of the request
      + `referrerPolicy`: specify referrer policy to use for the request
      + `integrity`: contain the subresource integrity value of the request
      + `keepalive`: used to allow the request to outlive the page
      + `signal`: an `AbortSignal` object instance to communicate w/ a fetch request and abort it
  + return: a `Promise` resolving to a `Response` object


### 5.4.4 Discussion and projects

Here is the discussion forum for this part of the course.

#### Suggested topic

Did you know that using XhR2 for getting remote data, you can also monitor the download progression using n `xhr.onprogress =` event listener and a `<progress>` HTML element. See [this example](https://jsbin.com/nuxanaf/edit?html,output)! This is not directly possible using [the new fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) (you need to give a look at the streams API that can be used altogether with the fetch API for [monitoring uploads and downloads](https://fetch-progress.anthum.com/)).

[JsBin Demo](https://jsbin.com/nuxanaf/edit?html,output)

[Local Demo](src/05d-example05.html)

#### Optional projects

+ Please display the data [from this URL](https://tinyurl.com/3j3dy5rn) in a dynamic table.
+ Try to add a "hi-score" table to the game developed during this course. The table will be displayed when you lose, and will show only the 10 best scores.




