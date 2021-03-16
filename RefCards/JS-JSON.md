# JavaScript Object Notation (JSON)

## Overview

+ [JavaScript Object Notation (JSON)](../WebDev/Frontend-W3C/5-JavaScript/05d-Forms.md#541-what-is-json)
  + a standard for transforming nearly any object into a string representation
  + a standard for exchangig data to/from a remote HTTP server
  + available for many other languages
  + developed mainly for replacing XML as a format for exchanging data btw a client and HTTP server
  + popularity: as the format for exchanging data under Ajax to communicate btw Web Applications and the HTTP server
  + MS IE 2005: first appearance
  + Google Maps: one of the first popular Ajax-powered Web application


## JSON and JS Objects

+ [JSON objects and JavaScript objects](../WebDev/Frontend-W3C/5-JavaScript/05d-Forms.md#541-what-is-json)
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

+ [`JSON.stringify()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
  + syntax: `JSON.stringify(value[, replacer[, space]])`
  + docstring: convert a JavaScript object or value to a JSON string
  + parameters
    + `value`: the value to convert to a JSOM string
    + `replacer` (optional):
      + a function alerts the behavior of the stringification process
      + an array of `String` and `Number` serves as allowist for selecting/filtering the properties of the value object to be included in the JSON string
      + `null` or omitted: all properties of the object included in the resulting JSON string
    + `space` (optional):
      + used to insert white space into the output JSON string for readability purpose
      + `Number` object: the number or space characters to use as white space
      + `String` object: use the string as white space
  + return: a JSON string representing the given value

+ [`JSON.parse()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)
  + syntax: `JSON.parse(text[, reviver])`
  + docstring: parse a JSON string, constructing the JS value or object described by the string
  + parameters
    + `text`: the string to parse as JSON
    + `reviver` (optional): a function prescribes how the value originally produced by parsing is transformed
  + return: the `Object`, `Array`, string, number, boolean, or null value corresponding to the given JSON `text`


### Remote data

+ [JSON data w/ REST service](../WebDev/Frontend-W3C/5-JavaScript/05d-Forms.md#542-consuming-json-remote-data)
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


## Local Storage API

+ [The Web Storage API](../WebDev/Frontend-W3C/5-JavaScript/05d-Forms.md#543-the-localstorage-api)
  + two mechanisms, similar to HTTP session cookies, for storing structured data on the client side
  + providing two interfaces: `sessionStorage` and `localStorage`
  + difference btw `sessionStorage` and `localStorage`: longevity
    + `sessionStorage`: remain until deleted
    + `localStorage`: erased when tab/browser closed
  + define an API for persistent data storage of key-value pair data in Web service

+ [Key-value stores](../WebDev/Frontend-W3C/5-JavaScript/05d-Forms.md#543-the-localstorage-api)
  + keys & values: strings
  + only one store per domain
  + functionality: expose through the globally available `localStorage`/`sessionStorage` object

+ [Web Storage vs cookies](../WebDev/Frontend-W3C/5-JavaScript/05d-Forms.md#543-the-localstorage-api)
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




