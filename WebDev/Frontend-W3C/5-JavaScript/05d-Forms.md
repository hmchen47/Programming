# Module 5: Working with forms


## 5.4 [The JSON notation

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
<li><span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif; color: #ff0000;">Transform any JSON string into a JavaScript object: &nbsp; &nbsp;<span style="font-family: 'courier new', courier; color: #000000;"><strong>var jsObj &nbsp;= JSON.parse(jsonStr);</strong></span></span></li>
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
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">stringify</span><span class="pun">(<span style="color: #000000;" color="#000000">simpleObject</span></span><span class="pun">);</span></strong></li>
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
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">stringify</span><span class="pun">(<span style="color: #000000;" color="#000000">complexObject</span></span><span class="pun">);</span></strong></li>
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







