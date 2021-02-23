# Module 4: Structuring data

## 4.3 Objects (part 3): creating multiple objects

### 4.3.1 Classes: definition

Let's study what is the concept of "class" in object oriented programming languages.

So far in this course, we've only used singleton objects: objects that only occur once: player, darkVador, etc.

Ok, this is not quite true, I'd forgotten that we created many balls in the module 2 game. We'll come back to this example further down the page!

But even with the balls from module 2, we did not use a template to tell us how to easily create multiple objects that share the same properties and the same methods, but whose properties' values may differ.

For example, imagine Luke Skywalker, Ian Solo and Dark Vador. What do they have in common? They all are Star Wars heroes, they all have a name, they all belong to one side (the good/bad people, or rebels vs empire), etc. Imagine that we have a way of programming that describes not the objects themselves, but a "model", a "template" for these objects. We could call it StarWarsHero and use it for creating our heroes' objects.

Imagine the balls from module 2: they all had the same shape (circle), the same x, y, radius and color properties, but they were all different. They all belonged to the same class of object (ball), but they were all different in terms of their properties' values.

<span style="color: brown; font-weight: bold;">In many programming languages, these templates are called "classes".</span>

+ Before 2015, in JavaScript 5 (also called ES5), we did not have such a concept, instead we had "constructor functions".
+ In modern JavaScript (after 2015),  we have the concept of classes, and the syntax is rather similar to what we find in other object oriented programming languages.

Let's introduce these two ways of defining "pseudo classes" with ES5's function constructors, and with modern JavaScript's classes!


#### Notes for 4.3.1 Classes: definition

+ Classes
  + singleton objects: objects only occurred once
  + templates w/ same properties and methods
    + prior ES5: not having such concept but "constructor functions"
    + since ES5: concept of classes and the syntax developed similar to what other object-oriented programming language
  + example: balls w/ the same shape (circle), the sam ex,y, radius, and color properties but different values


### 4.3.2 The "new" keyword

#### Live coding video: ES5 constructor functions, the "new" keyword

<a href="https://edx-video.net/W3CJSIXX2016-V004200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/298bdbxb)

__Source code shown in the video__

[CodePen Demo](https://codepen.io/w3devcampus/pen/eRBoyr?editors=0011)

Up to 2015, with JavaScript version 5 (and previous versions), you can define a pseudo-class template called "<span style="color: brown; font-weight: bold;">a constructor function</span>". The syntax is the same as for creating a function, except that:

1. <span style="color: brown; font-weight: bold;">By convention, its name is Capitalized.</span> The first letter of the function name is in uppercase, this is a good way to know, when you read someone else's code, that this is not a regular function, but a constructor function. Its name is a noun, the name of the class of objects you are going to build. Example: Person, Vehicle, Enemy, Product, Circle, Ball, Player, Hero, etc.
2. <span style="color: brown;">You build new objects using the new keyword:</span>

  Examples (Car, Hero, Ball, Product are constructor function names):

  <span style="font-family: 'courier new', courier;">var car =&nbsp;<strong><span style="color: #ff0000;">new</span></strong>&nbsp;Car('Ferrari', 'red');</span><br>
  <span style="font-family: 'courier new', courier;">var luke =&nbsp;<strong><span style="color: #ff0000;">new</span></strong>&nbsp;Hero('Luke Skywalker', 'rebels");</span><br>
  <span style="font-family: 'courier new', courier;">var ball1 =&nbsp;<strong><span style="color: #ff0000;">new</span></strong>&nbsp;Ball(10, 10, 20, 'blue'); // x=10, y=10, radius = 20, color = 'blue'</span><br>
  <span style="font-family: 'courier new', courier;">var p1 =&nbsp;<strong><span style="color: #ff0000;">new</span></strong>&nbsp;Product('Epson printer P1232', '183', 'Mr Buffa'); // ref, price, customer</span><br>
  <span style="font-family: 'courier new', courier;">etc.</span>

3. <span style="color: brown; font-weight: bold;">The parameters of the function are the "constructor parameters": the new object that you are building will take these as its initial properties' values.</span> You can build a Hero, but you must give him/her a name, a side, etc.
4. <span style="color: brown; font-weight: bold;">You define the property names and method names using the <code>this</code> keyword.</span> But beware: the syntax is not the same as the syntax we used for singleton/simple objects. No more ":" and "," between properties. Here we use "=" and ";" like in regular functions.

  Example:

  ```js
  function Hero(name, side) {
      this.name = name;
      this.side = side;
      this.speak = function() {
          console.log("My name is " + this.name + " and I'm with the " + this.side);
      }
  }
  ```

  In a constructor function named "Hero", you will find properties declared like this: this.name this.side; and methods declared like this: this.speak = function() {...}
5. <span style="color: brown; font-weight: bold;">Very often some properties are initialized using the constructor function parameters,</span> so that the newly constructed objects will get an initial value for their properties. In this case, we use the this keyword to distinguish the property from the constructor function parameter:

  Example:

  ```js
  function Hero(name) {
      this.name = name;
      ...
  }
  ```



__Full interactive example that uses a constructor function__

[CodePen Demo](https://codepen.io/w3devcampus/pen/KWjMRw)

[Local Demo](src/04c-example02.html)


JavaScript source code:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd" style="color: #000088;">function</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="typ" style="color: #660066;">Hero</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">name</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;side</span><span class="pun" style="color: #666600;">)</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span><span class="kwd" style="color: #000088;">&nbsp; &nbsp; this</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">name&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;name</span><span class="pun" style="color: #666600;">; // code outside of methods is usually for initializing</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span><span class="kwd" style="color: #000088;">&nbsp; &nbsp; this</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">side&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;side</span><span class="pun" style="color: #666600;">; // the properties. Very often, they match the parameters</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span><span class="kwd" style="color: #000088;">&nbsp; &nbsp; this</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">speak&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">function</span><span class="pun" style="color: #666600;">()</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span><span class="kwd" style="color: #000088;">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">"&lt;p&gt;My name is "</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">this</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">name&nbsp;</span><span class="pun" style="color: #666600;">+</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span><span class="str" style="color: #008800;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;", I'm with the "</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">this</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">side&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">".&lt;/p&gt;"</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span><span class="pun" style="color: #666600;">&nbsp; &nbsp; }</span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pun" style="color: #666600;">}</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;darkVador&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">new</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="typ" style="color: #660066;">Hero</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"Dark Vador"</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">"empire"</span><span class="pun" style="color: #666600;">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;luke&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">new</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="typ" style="color: #660066;">Hero</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"Luke Skywalker"</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">"rebels"</span><span class="pun" style="color: #666600;">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;ianSolo&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">new</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="typ" style="color: #660066;">Hero</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"Ian Solo"</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">"rebels"</span><span class="pun" style="color: #666600;">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd" style="color: #000088;">function</span><span class="pln" style="color: #000000;">&nbsp;makeHeroesSpeak</span><span class="pun" style="color: #666600;">()</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">body</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">innerHTML&nbsp;</span><span class="pun" style="color: #666600;">+=</span><span class="pln" style="color: #000000;">&nbsp;darkVador</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">speak</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">body</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">innerHTML&nbsp;</span><span class="pun" style="color: #666600;">+=</span><span class="pln" style="color: #000000;">&nbsp;luke</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">speak</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">body</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">innerHTML&nbsp;</span><span class="pun" style="color: #666600;">+=</span><span class="pln" style="color: #000000;">&nbsp;ianSolo</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">speak</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div>

_Lines 1-9_: see how the constructor function is declared: the function name starts with an uppercase letter 'Hero'. The parameters have the same name as the properties they correspond to (`name`, `side`). And in the first source code lines after the function declaration, we initialize some properties using these parameters (_lines 2 and 3_). We use the `this` keyword to distinguish the property and the parameter. You will often see things like: `this.name = name; this.age = age;` etc.

_Lines 11-13_: creation of three heroes. We use the same constructor function (Hero) along with the `new` keyword. Luke, darkVador and ianSolo ARE each a Hero, and share the same properties (name, side, _lines 2 and 3_) and the same behavior (they can speak, they all have a `speak` method, declared at _line 5_).








