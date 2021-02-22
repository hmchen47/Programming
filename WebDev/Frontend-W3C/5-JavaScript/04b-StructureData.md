# Module 4: Structuring data


## 4.2 Objects (part 2): properties and methods

### 4.2.1 Introduction

You're already familiar with the concept of objects, but so far we've only seen one simple form, called "objects literals" or "singleton objects". I think we've referred to them as "simple objects" in the course. Here is an example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> js1 </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; courseName</span><strong><span class="pun">:</span></strong><span class="pln"> </span><span class="str">'JavaScript intro'</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; weeks</span><strong><span class="pun">:</span></strong><span class="pln"> </span><span class="lit">5,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; madeBy</span><span class="pun">:</span><span class="pln">&nbsp;'W3Cx'</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; author</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Michel Buffa'</span><span class="pln"> </span><span class="com">// no "," after the last property!, even if ES5/6 accept it</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

And we access properties values using the "." operator, like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> js1</span><span class="pun">.</span><span class="pln">author</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">"Michel Buffa"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> js1</span><span class="pun">.</span><span class="pln">weeks</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">5</span></li>
</ol></div>

__However, we haven't explained 90% of what is going on, and what we can do with "objects".__ Our objective in this module, is to explain the most important features of objects, while keeping it simple (more advanced topics will be taught in a future "JavaScript Advanced" course, such as prototypes, context binding, etc.).

__Features you will learn:__

+ The relationship between JavaScript objects and arrays,
+ What a "reference" is in a programming language,
+ How to embed methods in your objects (functions inside an object),
+ The "`this`" object that you very often encounter in Object Oriented JavaScript code,
+ How to add methods and properties to your objects,
+ How to make multiple objects of the same class using ES6 classes,
+ The built-in JavaScript objects and classes: `Array`, `String`, `RegExp`, `Date`, `Math`, `Error`, etc. And, we will remind you about objects such as `navigator`, `document`, `window`, `screen`, etc.


#### Knowledge check 4.2.1

```js
var myBoss = {
    position: 'The Boss!',
    givenName: 'John, John the Boss!',
    office: 31
};
```

  How do we call an object defined like the one shown above?

  a. A JavaScript object literal<br>
  b. No special name, objects are objects, that's all<br>

  Ans: a<br>
  Explanation: A JavaScript __object literal__ is a comma-separated list of name-value pairs wrapped in curly braces. Object literals encapsulate data, enclosing it in a tidy package. This minimizes the use of global variables which can cause problems when combining code.


### 4.2.2 From objects to arrays

#### Live coding video: object's properties

<a href="https://edx-video.net/W3CJSIXX2016-V003800_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/myijs29d)


__Source code of the example in the above video__

[CodePen Demo](https://codepen.io/w3devcampus/pen/XgNdLK?editors=0012)

[Local Demo](src/04b-example01.html)


#### From objects to arrays

__In Javascript, an object = a table whose keys/indexes are defined!__

__Important note:__ Darth Vader is called "Dark Vador" in the French versions of SW, and, as a French tutor, I think it's cool to give to one of the heroes an international name. :-)

Look at this array:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><strong><span class="kwd">var</span><span class="pln"> darkVador </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="str">'villain'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'half human half machine'</span><span class="pun">];</span></strong><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> darkVador</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"villain"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> darkVador</span><span class="pun">[</span><span class="lit">1</span><span class="pun">]</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">"half human half machine"</span></li>
</ol></div>

And now, look at this object:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> darkVador </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; job</span><span class="pun">:</span><span class="pln"> </span><span class="str">'villain'</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; race</span><span class="pun">:</span><span class="pln"> </span><span class="str">'half human half machine'</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">};</span><span class="pln"> </span></li>
</ol></div>

They look a bit similar, don't they?

+ Same name of the variable that contains the object = `darkVador`
+ Instead of '<span style="color: brown;">[</span>' and '<span style="color: brown;">]</span>' that we used for defining an array, we use '<span style="color: brown;">{</span>' and '<span style="color: brown;">}</span>' for defining an object
+ The elements of the object (its <span style="font-weight: bold; text-decoration: underline">properties</span>) are separated by a comma ','
+ The pairs of keys/values are separated by '<span style="color: brown;">:</span>' as in <code>race<span style="color: brown;">:</span> 'half human, half machine</span>'
+ The last pair of keys/values has no ',' at the end.

__It is possible to access the object's properties with "." or with brackets__

We saw that we can use the "." operator, followed by the property name. It's also possible to use the bracket notation, and manipulate the object as an array whose indexes, instead of being 0, 1, 2 etc., are the property names!

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> book </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> title</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Le Petit Prince'</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> author</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Saint-Exupery'</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><strong><span class="kwd">var</span><span class="pln"> title </span><span class="pun">=</span><span class="pln"> book</span><span class="pun">.</span><span class="pln">title</span><span class="pun">;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> title</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="str">"Le Petit Prince"</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><strong><span class="kwd">var</span><span class="pln"> title </span><span class="pun">=</span><span class="pln"> book</span><span class="pun">[</span><span class="str">'title'</span><span class="pun">];</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> title</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="str">"Le Petit Prince"</span><span class="pun">;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> author </span><span class="pun">=</span><span class="pln"> book</span><span class="pun">[</span><span class="str">'author'</span><span class="pun">];</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> author</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">"Saint-Exupery"</span></li>
</ol></div>

As you can see, if you look at _lines 7-10_ and _13-16_, writing `book.title` or `book['title']` is equivalent!

<span style="color: brown; font-weight: bold">In JavaScript, objects are arrays whose indexes are property names: please remember this!</span>


#### Notes for 4.2.2 From objects to arrays

+ Objects in JS
  + object: a table whose keys/indexes defined
  + __object literal__
    + a comma-separated list of name-value pairs wrapped in curly braces
    + encapsulating data, enclosing it in a tidy package
  + minimizing the use of global variables which can cause problems when combining code
  + array defined w/ '<span style="color: brown;">[</span>' and '<span style="color: brown;">]</span>'
  + characteristics
    + object defined ww/ '<span style="color: brown;">{</span>' and '<span style="color: brown;">}</span>'
    + elements (properties) of object separated by a comma ','
    + pairs of keys/values separated by ':'
    + the last pair of keys/values w/o ',' at the end
  + accessing properties w/ '.' or brackets followed by the property name
  + example:

    ```js
    var darkVador = {
      job: 'villain',
      race: 'half human half machine'
    };

    darkVador.job;      // 'villain'
    darkVador['job'];   // 'villain'
    ```


#### Knowledge check 4.2.2

```js
let michel = {
    job:'Your Teacher'
}
```

1. Check the correct proposal:

  a. `michel.job` and `michel['job']` are equivalent<br>
  b. `michel.job` and `michel['job']` are NOT equivalent<br>




