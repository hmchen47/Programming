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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">3</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">stringify</span><span class="pun">(</span><span class="pln">x</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"3"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln">&nbsp;simpleObject&nbsp;</span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">x</span><span class="pun">:</span><span class="lit">12</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">:</span><span class="lit">30</span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">stringify</span><span class="pun">(<span style="color: #008888;" color="#008888">simpleObject</span></span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="str">"{"</span><span class="pln">x</span><span class="str">":12,"</span><span class="pln">y</span><span class="str">":30}"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> anArray&nbsp;</span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="str">'Monday'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'Tuesday'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'Wednesday'</span><span class="pun">];</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">stringify</span><span class="pun">(</span><span class="pln">anArray</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="str">"["</span><span class="typ">Monday</span><span class="str">","</span><span class="typ">Tuesday</span><span class="str">","</span><span class="typ">Wednesday</span><span class="str">"]"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln">&nbsp;complexObject&nbsp;</span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">name</span><span class="pun">:</span><span class="str">'Metallica'</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; albums</span><span class="pun">:[</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; {</span><span class="pln">name</span><span class="pun">:</span><span class="str">"Master of Puppets"</span><span class="pun">,</span><span class="pln"> year</span><span class="pun">:</span><span class="lit">1986</span><span class="pun">},</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; {</span><span class="pln">name</span><span class="pun">:</span><span class="str">"Black Album"</span><span class="pun">,</span><span class="pln"> year</span><span class="pun">:</span><span class="lit">1991</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; ]</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; };</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">stringify</span><span class="pun">(<span style="color: #008888;" color="#008888">complexObject</span></span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">"{"</span><span class="pln">name</span><span class="str">":"</span><span class="typ">Metallica</span><span class="str">","</span><span class="pln">albums</span><span class="str">":[{"</span><span class="pln">name</span><span class="str">":"</span><span class="typ">Master</span><span class="pln"> of </span><span class="typ">Puppets</span><span class="str">","</span><span class="pln">year</span><span class="str">":1986},{"</span><span class="pln">name</span><span class="str">":"</span><span class="typ">Black</span><span class="pln"> </span><span class="typ">Album</span><span class="str">","</span><span class="pln">year</span><span class="str">":1991}]}"</span></li>
</ol></div>

In the above examples, you can see JSON representations of a simple variable of a predefined type, of an array, of a simple object, of an object that contains an array of objects (Metallica example).

And indeed, it looks like the code you typed to create the objects, with quotes around it and around the property names. This is why it is called JavaScript Object Notation ;-)


#### JSON objects as JavaScript objects

__You cannot use JSON objects as JavaScript objects__

The JSON representation of JavaScript objects is a string. JSON has been developed mainly for replacing XML as a format for exchanging data between a client and a remote HTTP server. It has become very popular as the format for exchanging data when a Web Application uses Ajax for its communications with the HTTP server. Ajax is a way to send / receive data in the background, without the need to reload the Web page. Along with the DOM API, the appearance of this technology in 2005 with Internet Explorer, made it possible to make Web pages more dynamic. Google Maps was one of the first popular Ajax-powered Web application: as you moved the map, new parts arrived (downloaded in the background from the Gmap HTTP server), and the page updated to display these new parts.

JSON is also very practical for storing objects where strings are expected. There is a data store in your browser called LocalStorage that can be used as a small database for Web applications, but it stores only pairs of key/values in the string format. If you want to save a JavaScript object, you will have to turn it into JSON, then save it. When you read it from the data store, you will need to turn it back from JSON to JavaScript.

Here is a first example that turns an object into JSON and back into a JavaScript object:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">&gt; var</span><span class="pln"> metallica </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">name</span><span class="pun">:</span><span class="str">'Metallica'</span><span class="pun">,</span><span class="pln"> albums</span><span class="pun">:[{</span><span class="pln">name</span><span class="pun">:</span><span class="str">"Master of Puppets"</span><span class="pun">,</span><span class="pln"> year</span><span class="pun">:</span><span class="lit">1986</span><span class="pun">},</span><span class="pln"> <br></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp;{</span><span class="pln">name</span><span class="pun">:</span><span class="str">"Black Album"</span><span class="pun">,</span><span class="pln"> year</span><span class="pun">:</span><span class="lit">1991</span><span class="pun">}]};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">&gt; var</span><span class="pln"> metallicaJSON </span><span class="pun">=</span><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">stringify</span><span class="pun">(</span><span class="pln">metallica</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&gt; metallicaJSON</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">"{"</span><span class="pln">name</span><span class="str">":"</span><span class="typ">Metallica</span><span class="str">","</span><span class="pln">albums</span><span class="str">":[{"</span><span class="pln">name</span><span class="str">":"</span><span class="typ">Master</span><span class="pln"> of </span><span class="typ">Puppets</span><span class="str">","</span><span class="pln">year</span><span class="str">":1986},<br>&nbsp; &nbsp; &nbsp; &nbsp;{"</span><span class="pln">name</span><span class="str">":"</span><span class="typ">Black</span><span class="pln"> </span><span class="typ">Album</span><span class="str">","</span><span class="pln">year</span><span class="str">":1991}]}"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&gt; metallicaJSON</span><span class="pun">.</span><span class="pln">name</span><span class="pun">;</span><span class="pln"> </span><span class="com">// metallicaJSON is not a JavaScript object</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&gt; metallica</span><span class="pun">.</span><span class="pln">name</span><span class="pun">;</span><span class="pln"> </span><span class="com">// metallica is an object</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="str">"Metallica"</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">&gt; var</span><span class="pln"> obj </span><span class="pun">=</span><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">parse</span><span class="pun">(</span><span class="pln">metallicaJSON</span><span class="pun">);</span><span class="pln"> </span><span class="com">// JSON -&gt; object</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&gt; obj</span><span class="pun">.</span><span class="pln">name</span><span class="pun">; // this is</span>&nbsp;an object</li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">"Metallica"</span></li>
</ol></div>

With the JSON representation of an object you cannot access the original object's properties using the "." operator, nor call its methods. __The JSON format only stores the list of the object properties (name and value) as a string.__ Look at _line 10_: we cannot access the name property of the JSON representation of the `metallica` object defined at line 1.

When we parse a JSON string using `JSON.parse()`, we get a real JavaScript object, and we can access its properties (_lines 16 and 19_).


#### Notes for 5.4.1 What is JSON?

+ JSON (JavaScript Object Notation (JSON)
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
  + JS object #\to$ JSON: `var metallicaJSON = JSON.stringify(metallica);`
  + display JSON: `metallicaJSON; // "{"name":"Metallica","albums":[{"name":"Master of Puppets","year":1986}, {"name":"Black Album","year":1991}]}"`
  + JSON format not a JS object: `metallica.name; // undefined`
  + convert back to JS object: `var obj = JSON.parse(metallicaJSON); obj.name; // "Metallica"`

+ [`JSON.stringify()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
  + syntax: `JSON.stringify(value[, replacer[, space]])`
  + docstring: convert a JavaScript object or value to a JSON string
  + parameters
    + `value`: the value to convert to a JSOM string
    + `replacer` (optional):
      + a function alerts the behavior of the stringification process
      + an array of `String` and `Number` serves as allowist for selecting/filtering the properties of the value object to be included in the JSON string
      + `null` or omitted: all properties of the object included in the resulting JSON string
    + `space (optional):
      + used to insert white space into the output JSON string for readability purpose
      + `Number` object: the number os space characters to use as white space
      + `String` object: use the string as white space
  + return: a JSON string representing the given value

+ [`JSON.parse()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)
  + syntax: `JSON.parse(text[, reviver])`
  + docstring: parse a JSON string, constructing the JS value or object described by the string
  + parameters
    + `text`: the string to parse as JSON
    + `reviver` (optional): a function prescribes how the value originally produced by parsing is transformed
  + return: the `Object`, `Array`, string, number, boolean, or null value corresponding to the given JSON `text`


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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> search</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> queryURL </span><span class="pun">=</span><span class="pln"> </span><span class="str">"https://jsonplaceholder.typicode.com/users"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> queryURL</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // called when the response has arrived</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xhr</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; <strong>var</strong></span><strong><span class="pln"> jsonResponse </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">response</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; <strong>// turn the response into a JavaScript object</strong></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; <strong>var</strong></span><strong><span class="pln"> users </span><span class="pun">=</span><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">parse</span><span class="pun">(</span><span class="pln">jsonResponse</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; displayUsersAsATable</span><span class="pun">(</span><span class="pln">users</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // in case of error</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xhr</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">err</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Error: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> err</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // sends the request</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> search</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> queryURL </span><span class="pun">=</span><span class="pln"> </span><span class="str">"https://jsonplaceholder.typicode.com/users"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; fetch</span><span class="pun">(</span><span class="pln">queryURL</span><span class="pun">)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; .</span><span class="kwd">then</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>// response is a json string,</strong></span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // convert it to a pure JavaScript object</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> response</span><span class="pun">.</span><span class="pln">json</span><span class="pun">();</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; })</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; .</span><span class="kwd">then</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">users</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong> // users is a JavaScript object here</strong></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayUsersAsATable</span><span class="pun">(</span><span class="pln">users</span><span class="pun">)</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; })</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; .</span><span class="kwd">catch</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">error</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'Error during fetch: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> error</span><span class="pun">.</span><span class="pln">message</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; });</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
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
  + button element" `<button onclick="search();">Get a remote list of users' names and emails</button>`
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
      + insert row: `var row = table.insertRow();
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

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="com">// Using localStorage</span></li>
<li class="L1"><span class="pln"></span></li>
<li class="L2"><span class="com">// store data</span></li>
<li class="L3"><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">lastName&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="str">"Bunny"</span><span class="pun">;</span></li>
<li class="L4"><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">firstName&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="str">"Bugs"</span><span class="pun">;</span></li>
<li class="L5"><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">location&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="str">"Earth"</span><span class="pun">;</span></li>
<li class="L6"><span class="pln"></span></li>
<li class="L7"><span class="com">// retrieve data</span></li>
<li class="L8"><span class="kwd">var</span><span class="pln">&nbsp;lastName&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;localStorage</span><span class="pun">.</span><span class="pln">lastName</span><span class="pun">;</span></li>
<li class="L9"><span class="kwd">var</span><span class="pln">&nbsp;firstName&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;localStorage</span><span class="pun">.</span><span class="pln">firstName</span><span class="pun">;</span></li>
<li class="L0"><span class="kwd">var</span><span class="pln">&nbsp;location&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;localStorage</span><span class="pun">.</span><span class="pln">location</span><span class="pun">;</span></li>
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






