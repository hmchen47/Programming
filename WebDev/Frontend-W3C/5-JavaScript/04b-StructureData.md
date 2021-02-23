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
+ The pairs of keys/values are separated by '<span style="color: brown;">:</span>' as in <code>race<span style="color: brown;">:</span> 'half human, half machine</span>'</code>
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
  + objects = arrays w/ indexes as __property names__
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

  Ans: a<br>
  Explanation: We saw that we can use the "." operator, followed by the property name, like `michel.job`. It's also possible to use the bracket notation, and manipulate the object as an array whose indexes, instead of being 0, 1, 2, etc., are the property names! So `michel.job` and michel followed by brackets with 'job' or "job" as an index are equivalent.


### 4.2.3 Property declaration syntax


#### Property names: different possibilities

We can put single or double quotes around the name of the property, or nothing at all:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd">var</span><span class="pln"> louis </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">age</span><span class="pun">:</span><span class="pln"> </span><span class="lit">40</span><span class="pun">}; // WE DO THIS MOST OF THE TIME!</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> louis </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="str">"age"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">40</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> louis </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="str">'age'</span><span class="pun">:</span><span class="pln"> </span><span class="lit">40</span><span class="pun">};</span><span class="pln"> </span></li>
</ol></div>


#### In some cases we have to put quotes around the property name

+ When it is a reserved word from JavaScript,
+ Or it contains spaces or special characters,
+ Or it begins with a number.

Examples:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pln">book</span><span class="pun">.</span><span class="lit">1stPublication</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">'6 April 1943'</span><span class="pun">;</span><span class="pln"> </span><span class="com">// begins with a number</span></strong></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // Throws a SyntaxError</strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">book</span><span class="pun">[</span><span class="str">'1stPublication'</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">'6 April 1943'</span><span class="pun">;</span><span class="pln"> </span><span class="com">// OK</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">book.date of publication =&nbsp;</span>'6 April 1943'<span class="pun">; // spaces not allowed!<br></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">book['date of publication']&nbsp;</span>=&nbsp;'6 April 1943'<span class="pun">; // allowed, but avoid!</span></li>
</ol></div>


#### Another classic case where the name of a property is in a variable

In this case it is necessary  to use the syntax with '[' and ']' ...

Example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> key </span><span class="pun">=</span><span class="pln"> </span><span class="str">'title'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> book</span><span class="pun">[</span><span class="pln">key</span><span class="pun">];</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"Le Petit Prince"</span></li>
</ol></div>


#### Notes for 4.2.3 Property declaration syntax

+ Property declaration
  + property name: single or double quotes around the name of the perperty, or nothing at all
  + recommended: no single or double quotes
  + exceptions: single or double quotes required
    + reserved words in JS
    + containing spaces or special characters
    + begining w/ a number
  + the name of property used as a variable
  + example:

    ```js
    var louis = {age: 40};
    var louis = {"age": 40};
    var louis = {'age': 40};

    book.1stPublication = '6 April 1943';
    book['1stPublication'] = '6 April 1943';

    var key = 'title';  // title as property name
    book[key];
    ```


### 4.2.4 An object can contain another object

Example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> book </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; name</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Catch-22'</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; published</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1961</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>author</strong></span><strong><span class="pun">:</span><span class="pln"> </span><span class="pun">{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // embedded object!</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; givenName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Joseph'</span><span class="pun">,</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; familyName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Heller'</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> book</span><span class="pun">.</span><span class="pln">author</span><span class="pun">.given</span><span class="pln">Name</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">"Joseph"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> book</span><span class="pun">.</span><span class="pln">author</span><span class="pun">.family</span><span class="pln">Name</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"Heller"</span></li>
</ol></div>

Accessing the embedded object `author` is done by chaining property accesses using the "." operator, like in `book.author.givenName` (here we access the `givenName` property of the object `author`, which is also a property of the `book` object).


#### Notes for 4.2.4 An object can contain another object

+ Object in object
  + accessing the embedded object by chaining property using the '.' operator
  + example:

    ```js
    var book = {
      name: 'Catch-22',
      published: 1961,
      author: {                 // embedded object!
          givenName: 'Joseph',
          familyName: 'Heller'
      }
    };

    book.author.givenName;  // "Joseph"
    ```


### 4.2.5 Elements, properties and methods

#### Live coding video: object methods

<a href="https://edx-video.net/W3CJSIXX2016-V004000_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/347phojc)


__Source code of the live video example__

[CodePen Demo](https://codepen.io/w3devcampus/pen/EXNrjB?editors=0011)

[Local Demo](src/04b-example02.html)


#### Elements, properties and methods

__Some vocabulary:__

+ For <span style="color: brown; font-weight: bold;">arrays</span>, we speak of <span style="color: brown; font-weight: bold;">elements</span>
+ For <span style="color: cyan; font-weight: bold;">objects</span>, we talk about <span style="color: cyan; font-weight: bold;">properties</span>
+ But <span style="color: lightgreen; font-weight: bold;">a property can also be a function</span>, in which case it is called a <span style="color: lightgreen; font-weight: bold; text-decoration: underline;">method</span>

__Yes, it is possible for an object's property to be a function!__

A very simple example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> medor </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; name</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Benji'</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; bark</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">'Ouarf, Ouarf!'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div>

In this example, the bark property's value is a function, so we call bark "a method".

__A method is a special property that corresponds to the object's behavior__

<div class="exampleHTML">
<p><strong><span style="color: #3366ff;">Properties</span> correspond to <span style="color: #3366ff;">an object's DNA</span> (its characteristics), <br><span style="color: #3366ff;">and are nouns</span> (age, name, etc.)</strong></p>
<p><strong><span style="color: #008000;">Methods</span> correspond to <span style="color: #008000;">an object's behavior <br></span>and <span style="color: #008000;">are verbs</span> (bark, move, changeSpeed, etc.)</strong></p>
</div>

#### Calling a method

Since a method is a property we can use the '.' operator (or brackets with the method's name as a string index).

Let's see some examples:


[CodePen Demo](https://codepen.io/w3devcampus/pen/RpmzQY)

[Local Demo](src/04b-example03.html)

JavaScript source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><strong><span class="pln"> darkVador </span></strong><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; race</span><span class="pun">:</span><span class="pln"> </span><span class="str">'human'</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; job</span><span class="pun">:</span><span class="pln"> </span><span class="str">'villain'</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>talk</strong></span><strong><span class="pun">:</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="str">'come to the dark side, Luke!'</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> dvSpeak</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">'&lt;p&gt;Dark Vador says '</span><span class="pln"> </span><span class="pun">+</span><strong><span class="pln"> darkVador</span><span class="pun">.</span><span class="pln">talk</span><span class="pun">();</span></strong><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">'&lt;/p&gt;'</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

In _line 1_, we created a simple object named `darkVador`, that has two properties (`race` and `job`) and a method (`talk`).

In the dvSpeak function, at line 10, we call `darkVador`'s talk method. The syntax is a mix between the one for accessing a property (with the '.' operator), and the one for calling a function (with parentheses and ';' at the end).

When we write darkVador.talk(), we are executing the talk method of the object `darkVador`, but in plain English, we're just asking Dark Vador to talk. We invoke its behavior!


__Another example with the player we saw briefly in Module 2__

Here is the last version of the player object we saw in our small game:

[CodePen Demo](https://codepen.io/w3devcampus/pen/xqNoJX)

[Local Demo](src/04b-example04.html)

JavaScript source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> player </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; x</span><span class="pun">:</span><span class="lit">10</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; y</span><span class="pun">:</span><span class="lit">10</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; width</span><span class="pun">:</span><span class="lit">20</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; height</span><span class="pun">:</span><span class="lit">20</span><span class="pun">,</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; color</span><span class="pun">:</span><span class="str">'red'</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// and we also used two other functions for moving the player with the mouse</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">// and for drawing it as a filled rectangle</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> movePlayerWithMouse</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pun">(</span><span class="pln">mousePos </span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; player</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; player</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> drawFilledRectangle</span><span class="pun">(</span><span class="pln">r</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // BEST practice: save the context, use 2D transformations</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // translate the coordinate system, draw relative to it</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">r</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> r</span><span class="pun">.</span><span class="pln">y</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> r</span><span class="pun">.</span><span class="pln">color</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // (0, 0) is the top left corner of the monster</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> r</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> r</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // BEST practice: restore the context</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

__Now that we've seen that we can include methods into objects, here is a better, more readable and more encapsulated version of our player object:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> player </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; x</span><span class="pun">:</span><span class="lit">10</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; y</span><span class="pun">:</span><span class="lit">10</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; width</span><span class="pun">:</span><span class="lit">20</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; height</span><span class="pun">:</span><span class="lit">20</span><span class="pun">,</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; color</span><span class="pun">:</span><span class="str">'red'</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>move</strong></span><strong><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // change x and y coordinates of the player</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // TODO!</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; },</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln"> </span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; draw</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // draw the player at its current position</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // with current width, height and color</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // TODO!</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


Assuming that the move and draw methods are fully implemented, we will now be able to call:

+ `player.move(mousePos.x, mousePos.y)` to change the position of the player,
+ `player.draw()` to draw the player at its current position, with its current size and color.

Readability is better, it is like asking the player to move, or asking it to draw itself. And we do not need to pass the x, y, width, height, color to the draw method: it is inside the player object, and it can access all its internal property values!

In the next section we will look at how we can access other object's properties from a method or call other methods.


#### Notes for 4.2.5 Elements, properties and methods

+ Object declaration
  + definitions
    + element for arrays
    + property for objects
    + method: a function as a property in objects
  + properties
    + an objects DNS, its characteristics
    + nouns, e.g., age, name, etc.
  + methods
    + an object's behavior
    + verb, e.g., bank, move, changeSpeed, etc.
  + calling a method (similar to a propert) w/ '.' or brackets w/ the method's name as a string index
  + including methods into object $\to$ more readable and more encapuslated version of an property-only object

+ Example: [declare an object](src/04b-example03.html)

  ```js
  var darkVador = {
    race: 'human',    // property
    job: 'villain',   // property
    talk: function() {    // method
      return 'come to the dark side, Luke!';
    },
    describeYourself: function() {    // method
      return "I'm a " + this.race + " and I'm a " + this.job + " in a series of movies!";
    }
  }

  function dvSpeak() {
    document.body.innerHTML += '<p>Dark Vador describes himself: ' + 
        darkVador.describeYourself(); + '</p>';
    document.body.innerHTML += '<p>Dark Vador says ' + darkVador.talk(); + '</p>';
  }
  ```

+ Example: [moving player](src/04b-example04.html)
  + player object declarartion

    ```js
    var player = {
        x:10,
        y:10,
        width:20,
        height:20,
        color:'red',
        move(x, y) {
            // change x and y coordinates of the player ...
        },
        draw() {
            // draw the player at its current position
        }
    }
    ```

  + `player.move(mousePos.x, mousePos.y)`: change the position of the player
  + `player.draw()`: draw the player at its current position



#### Knowledge check 4.2.3

```js
let anObject = {
    propertyName1: propertyValue1,
    propertyName2: propertyValue2,
    methodName1: function(...) { 
              // some code....
    },    
    methodName2: function(...) { 
              // some code....
    }
}
```

1. In a JavaScript object, properties are nouns and methods are verbs. True or false?

  Ans: True<br/>
  Explanation: Indeed, properties correspond to an object's DNA (its characteristics), and are nouns (age, name, etc.), and methods correspond to an object's behavior and are verbs (bark, move, changeSpeed, etc.).


### 4.2.6 "this": accessing properties

#### Live coding video: add methods to the player object from the game

<a href="https://edx-video.net/W3CJSIXX2016-V004100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/2sgovdkj)

Source code of examples shown in the above video

+ Game without methods in the player object (example included in the previous course page),
  + [CodePen Demo](https://codepen.io/w3devcampus/pen/xqNoJX)
  + [Local Demo](src/04b-example04.html)
+ Game with methods (example also included in this course page),
  + [CodePen Demo](https://codepen.io/w3devcampus/pen/oZRrQd/)
  + [Local Demo](src/04b-example05.html)


#### The `this` keyword: accessing properties from a method

__The `this` keyword!__

When one wants to access an object property or wants to call another method from an object method, we must use the `this` keyword. In the code of the player object, `this` means "from this object".

__Let's look at our game again, with a new version of the player object - this time fully functional:__

[CodePen Demo](https://codepen.io/w3devcampus/pen/oZRrQd/)

[Local Demo](src/04b-example05.html)


JavaScript code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> player </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; x</span><span class="pun">:</span><span class="lit">10</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; y</span><span class="pun">:</span><span class="lit">10</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; width</span><span class="pun">:</span><span class="lit">20</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; height</span><span class="pun">:</span><span class="lit">20</span><span class="pun">,</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; color</span><span class="pun">:</span><span class="str">'red'</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; move: function</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; <strong>this</strong></span><strong><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> x</span></strong><span class="pun"><strong>;</strong> // this.x is the property of "this object"</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; <strong>this</strong></span><strong><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> y</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; },</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; draw: function</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // draw the player at its current position</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // with current width, height and color</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; //&nbsp;it's nearly the same code as the old drawFilledRect function</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // translate the coordinate system, draw relative to it</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">y</span></strong><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">color</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // (0, 0) is the top left corner of the monster</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">height</span></strong><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // BEST practice: restore the context</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Notice that we've used this followed by the '.' operator every time we've had to access the current value of an object's property (_lines 9, 10, 20, 22 and 24_).

We passed the canvas' graphic context as a parameter to the draw method (it's always good not to create dependencies when making objects). Passing the context as a parameter avoids using it as a global variable. If in another project we've got a context named "context" instead of "ctx", then we will just change the parameter when we call `player.draw`, otherwise we would have had to rename all occurrences of `ctx` in the code).

Same with the mouse coordinates we passed to the `move` method.

__Let's see the Dark Vador example with the use of `this` in a method__

[CodePen Demo](https://codepen.io/w3devcampus/pen/JWqgGZ)

[Local Demo](src/04b-example06.html)


JavaScript source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> darkVador </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; race</span><span class="pun">:</span><span class="pln"> </span><span class="str">'human'</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; job</span><span class="pun">:</span><span class="pln"> </span><span class="str">'villain'</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; talk</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="str">'come to the dark side, Luke!'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">breathe</span><span class="pun">();</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; },</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; describeYourself</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="str">"I'm a "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">race </span></strong><span class="pun">+</span><span class="pln"> </span><span class="str">" and I'm a "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">job </span></strong><span class="pun">+</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;" in a series of movies!"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">breathe</span><span class="pun">();</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; },</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; breathe</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="str">".....shhhhhhhhh....."</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> dvSpeak</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">'&lt;p&gt;Dark Vador describes himself: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln">&nbsp; &nbsp; &nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; darkVador</span><span class="pun">.</span><span class="pln">describeYourself</span><span class="pun">();</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; '&lt;/p&gt;'</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">'&lt;p&gt;Dark Vador says: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; darkVador</span><span class="pun">.</span><span class="pln">talk</span><span class="pun">();</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; '&lt;/p&gt;'</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

In this example, notice that the `describeYourself` method from the `darkVador` object uses the two properties `name` and `job` using the `this` keyword. We also call the `breathe` method from the two methods `describeYourself` and `talk`, using `this.breathe();`


#### Notes for 4.2.6 "this": accessing properties

+ `this` keyword
  + accessing an object property or calling another method from an object method
  + meaning "from this object"
  + followed by '.' operator every time to access current value of an object property or call 
  + example: using `this` to access values and methods within an object

    ```js
    var player = {
        x:10,
        y:10,
        width:20,
        height:20,
        color:'red',
        move: function(x, y) {
            this.x = x; // this.x is the property of "this object"
            this.y = y;
        },
        draw: function(ctx) {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.fillStyle = this.color;
            ctx.fillRect(0, 0, this.width, this.height);
            ctx.restore();
        }
    }
    ```


### 4.2.7 Adding/deleting properties and methods

Properties and methods can be added/deleted after an object has been defined.

__Unlike other object-oriented languages, it is possible in JavaScript to add or to remove properties after an object has been created.__

Examples:

[CodePen Demo](https://codepen.io/w3devcampus/pen/WpqeyK)

[Local Demo](src/04b-example07.html)


JavaScript code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// empty object with properties/methods</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> darkVador </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// add properties after darkVador has been created</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> darkVador</span><span class="pun">.</span><span class="pln">race </span><span class="pun">=</span><span class="pln"> </span><span class="str">'human'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> darkVador</span><span class="pun">.</span><span class="pln">job </span><span class="pun">=</span><span class="pln"> </span><span class="str">'villain'</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// add some methods</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> darkVador</span><span class="pun">.</span><span class="pln">talk </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; return</span><span class="pln"> </span><span class="str">'come to the dark side, Luke!'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">breathe</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div>

_Lines 5, 6 and 9_: we can add properties and methods after the object has been created empty at _line 2_.


#### Deleting a property or a method

You can use the JavaScript keyword "delete" to delete an object's property (it will become `undefined`).

Example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/RpzNEP)

[Local Demo](src/04b-example08.html)

JavaScript code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> deleteSomeProperties</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; <strong>delete</strong></span><strong><span class="pln"> darkVador</span><span class="pun">.</span><span class="pln">race</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; delete</span><span class="pln"> darkVador</span><span class="pun">.</span><span class="pln">job</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Notes for 4.2.7 Adding/deleting properties and methods

+ Manipulating properties and methods
  + JS the only object-oriented language able to add or remove properties after an object has been created
  + example: [adding properties & method](src/04b-example07.html)
    + declare an empty object: `var darkVador = {};`
    + add properties after object created: `darkVador.race = 'human'; darkVador.job = 'villain';`
    + add methods after object created: `darkVador.talk = function() { return 'come to the dark side, Luke!' + this.breathe(); };`
  + example: [delete properties & methods](src/04b-example08.html)
    + delcare and add properties as the previous example
    + delete properties: `function deleteSomeProperties() { delete darkVador.race; delete darkVador.job; }`


#### Knowledge check 4.2.4

```js
let pacman = {};
pacman.color:'yellow';
pacman.shape: 'pizza';
```

1. Is the above code correct? (No/Yes)

  Ans: <br>
  Explanation: 










