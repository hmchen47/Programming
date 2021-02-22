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
+ The "this" object that you very often encounter in Object Oriented JavaScript code,
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

  Ans: <br>
  Explanation: 






