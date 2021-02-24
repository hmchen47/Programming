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
    + ES5: not having such concept but "constructor functions"
    + post ES5: concept of classes and the syntax developed similar to what other object-oriented programming language
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
5. <span style="color: brown; font-weight: bold;">Very often some properties are initialized using the constructor function parameters,</span> so that the newly constructed objects will get an initial value for their properties. In this case, we use the `this` keyword to distinguish the property from the constructor function parameter:

  Example:

  ```js
  function Hero(name) {
      this.name = name;
      ...
  }
  ```


#### Full interactive example that uses a constructor function

[CodePen Demo](https://codepen.io/w3devcampus/pen/KWjMRw)

[Local Demo](src/04c-example02.html)


JavaScript source code:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;</span><span class="typ" style="color: #AA0066;">Hero</span><span class="pun" style="color: #666600;">(</span><span class="pln">name</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;side</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd" style="color: #008888;">&nbsp; &nbsp; this</span><span class="pun" style="color: #666600;">.</span><span class="pln">name&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;name</span><span class="pun" style="color: #666600;">; // code outside of methods is usually for initializing</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd" style="color: #008888;">&nbsp; &nbsp; this</span><span class="pun" style="color: #666600;">.</span><span class="pln">side&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;side</span><span class="pun" style="color: #666600;">; // the properties. Very often, they match the parameters</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd" style="color: #008888;">&nbsp; &nbsp; this</span><span class="pun" style="color: #666600;">.</span><span class="pln">speak&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #666600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd" style="color: #008888;">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;p&gt;My name is "</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #666600;">.</span><span class="pln">name&nbsp;</span><span class="pun" style="color: #666600;">+</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="str" style="color: #008800;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;", I'm with the "</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #666600;">.</span><span class="pln">side&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">".&lt;/p&gt;"</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun" style="color: #666600;">&nbsp; &nbsp; }</span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pun" style="color: #666600;">}</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;darkVador&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #AA0066;">Hero</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"Dark Vador"</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"empire"</span><span class="pun" style="color: #666600;">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;luke&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #AA0066;">Hero</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"Luke Skywalker"</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"rebels"</span><span class="pun" style="color: #666600;">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;ianSolo&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #AA0066;">Hero</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"Ian Solo"</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"rebels"</span><span class="pun" style="color: #666600;">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;makeHeroesSpeak</span><span class="pun" style="color: #666600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; document</span><span class="pun" style="color: #666600;">.</span><span class="pln">body</span><span class="pun" style="color: #666600;">.</span><span class="pln">innerHTML&nbsp;</span><span class="pun" style="color: #666600;">+=</span><span class="pln">&nbsp;darkVador</span><span class="pun" style="color: #666600;">.</span><span class="pln">speak</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; document</span><span class="pun" style="color: #666600;">.</span><span class="pln">body</span><span class="pun" style="color: #666600;">.</span><span class="pln">innerHTML&nbsp;</span><span class="pun" style="color: #666600;">+=</span><span class="pln">&nbsp;luke</span><span class="pun" style="color: #666600;">.</span><span class="pln">speak</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; document</span><span class="pun" style="color: #666600;">.</span><span class="pln">body</span><span class="pun" style="color: #666600;">.</span><span class="pln">innerHTML&nbsp;</span><span class="pun" style="color: #666600;">+=</span><span class="pln">&nbsp;ianSolo</span><span class="pun" style="color: #666600;">.</span><span class="pln">speak</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div>

_Lines 1-9_: see how the constructor function is declared: the function name starts with an uppercase letter 'Hero'. The parameters have the same name as the properties they correspond to (`name`, `side`). And in the first source code lines after the function declaration, we initialize some properties using these parameters (_lines 2 and 3_). We use the `this` keyword to distinguish the property and the parameter. You will often see things like: `this.name = name; this.age = age;` etc.

_Lines 11-13_: creation of three heroes. We use the same constructor function (Hero) along with the `new` keyword. Luke, darkVador and ianSolo ARE each a Hero, and share the same properties (name, side, _lines 2 and 3_) and the same behavior (they can speak, they all have a `speak` method, declared at _line 5_).


#### Notes for 4.3.2 The "new" keyword

+ The 'new' keyword
  + constructor functions
    + ES5 and prior
    + a pseudo-class template
  + syntax of constructor functions same as creating a function w/ exceptions
    + name w/ capitalized on 1st letter
      + a good practice for readability
      + a noun: the name of the class of objects to build
      + examples: `Person`, `Vehicle`, `Enemy`, `Circle`, `Ball`, `Player`, `Hero`. etc.
    + the `new` keyword for new objects, examples
      + Car instance: `var car = new Car('Ferrari', 'red');`
      + Hero instance: `var luke = new Hero('Luke Skywalker', 'rebels");`
      + Ball instance: `var ball1 = new Ball(10, 10, 20, 'blue'); // x=10, y=10, radius = 20, color = 'blue'`
    + constructor parameters
      + the parameters of the function
      + the new building object w/ parameters as its initial values of properties
      + example: building a Hero must give a name, a side, etc.
    + using the `this` keyword to define the property names and method names
      + syntax not the same as the syntax used for single/simple objects
      + using "=" and ";" instead of ":" and ","
    + properties initialized w/ the constructor function parameters
      + newly constructed objects given an initial value for their properties
      + using `this` keyword to distinguish the property from the construction function parameters
      + example: `function Hero(name) { this.name = name; ... }`
  + code outside of methods usually for initializing the properties

+ Example: [a constructor function](src/04c-example02.html)
  + declare constructor function: `function Hero(name, side) {...}`
    + `name` property: `this.name = name;`
    + `side` property: `this.side = side;`
    + `speak` method: `this.speak = function() { return "<p>My name is " + this.name + ", I'm with the " + this.side + ".</p>"; } }`  
  + create instances: `var darkVador = new Hero("Dark Vador", "empire"); var luke = new Hero("Luke Skywalker", "rebels"); ...`
  + function for heros to speak: `function makeHeroesSpeak() { document.body.innerHTML += darkVador.speak(); ...}`



### 4.3.3 Creating objects using modern JavaScript's classes

#### Live coding video: modern JavaScript's classes

<a href="https://edx-video.net/W3CJSIXX2016-V004300_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/f4e664fz)

__Source code from above video examples__

[CodePen Demo](https://codepen.io/w3devcampus/pen/mwOYWm)

[Local Demo](src/04c-example03.html)

#### Creating classes

ES5's constructor function syntax is not easy to read. If someone does not respect the "conventions" that we've just discussed (start the class with an uppercase, etc.), then the code may work, but it will be difficult to guess that we are not in front of a regular function. 

Modern JavaScript now provides a `class` keyword and a `constructor` keyword, along with advanced concepts that will be the subject of a future " JavaScript advanced" course. 

Main changes:

1. <span style="color: cyan; font-weight: bold;">A class is simply defined using the keyword <code>class</code> <span style="color: brown;">followed by the name of the class</span></span>
2. <span style="color: brown; font-weight: bold;">The <span style="color: cyan;">unique constructor</span> is defined using the <code>constructor</code> keyword followed by the parameters</span>

    + <span style="color: brown; font-weight: bold;">The constructor is executed when an object is created using the keyword <code>new</code></span> <br>Example: `let h1 = new Hero('Ian Solo', 'rebels');`<br>
    This will call `constructor(name, side)` in the example below.
3. <span style="color: cyan; font-weight: bold;">A method is simply defined by its name <span style="color: brown;">followed by its parameters</span> (we no more use the keyword "function")</span><br>Example: `speak() {...}` in the source code below.

Here is the new version of the Hero "template", this time with the ES6 class syntax:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd">class</span><span class="pln"> </span><span class="typ">Hero</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>constructor</strong></span><strong><span class="pun">(</span><span class="pln">name</span><span class="pun">,</span><span class="pln"> side</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">name </span><span class="pun">=</span><span class="pln"> name</span><span class="pun">; // property</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">side </span><span class="pun">=</span><span class="pln"> side</span><span class="pun">; // property</span><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong> speak</strong></span><strong><span class="pun">()</span><span class="pln"> </span><span class="pun">{ // method, no more "function"</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="str">"&lt;p&gt;My name is "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">name </span><span class="pun">+</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;", I'm with the "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">side </span><span class="pun">+</span><span class="pln"> </span><span class="str">".&lt;/p&gt;"</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> darkVador </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Hero</span><span class="pun">(</span><span class="str">"Dark Vador"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"empire"</span><span class="pun">);</span></li>
</ol></div>

+ _Line 1_: a class is simply defined using the keyword `class` followed by the name of the class. Like for constructor functions, the convention is to use a noun, capitalized.
+ _Line 2_: the constructor is defined using the `constructor` keyword. __THERE CAN BE ONLY ONE CONSTRUCTOR in the class.__  A SyntaxError will be thrown if the class contains more than one occurrence of a constructor method. No more use of the `function` keyword. Simply use the `constructor` keyword followed by the parameters.

<span style="color: cyan;">The instructions in the body of the constructor are executed when an object is created using the keyword new followed by the name of the class, with arguments between parentheses. These arguments will be passed to the constructor.</span>

+ _Line 7_: a method is simply defined by its name followed by its parameters. <span style="color: cyan; font-weight: bold;">Again, no more use of the <code>function</code> keyword.</span>

See below an interactive example that uses an ES6 class to create Star Wars' heroes.

[CodePen Demo](https://codepen.io/w3devcampus/pen/PpMpBo)

[Local Demo](src/04c-example03.html)



#### Notes for 4.3.3 Creating objects using modern JavaScript's classes

+ Declare classes
  + ES5 constructor functions: not eay to read and probably not followed name convention
  + ES6 introducing `new` and `constructor` keywords
    + simply define a class using the keyword `class` followed by the nam eof the class
    + the `contrustor` keyword followed by the parameters
      + only one constructor in the class
      + constructor executed when an object created using the keyword `new`
      + the instructions in `constructor` block extecuted when an object created
      + example: `let h1 = new Hero('Ian Solo', 'rebels');` $\to$ calling `constructore(name, side)`
    + method:
      + simply defined by the name followed by its parameters
      + no `function` keyword required
  + declaring a class before using it, otherwise, throwing a `ReferenceError` message
  
+ Example: [creating class and objects](src/04c-example03.html)
  + declare class: `class Hero {...}`
    + declare constructor: `constructor(name, side) {...}`
    + declare properties within constructor: `this.name = name; this.side = side;`
    + declare method: `speak( return "<p>My name is " + this.name + ", I'm with the " + this.side + ".</p>"; }`
  + declare a new instance: `var darkVador = new Hero("Dark Vador", "empire");`


### 4.3.4 Declaring a class before using it


__You must declare a class before using it!__

Unlike functions, classes must be declared BEFORE using them.

An important difference between function declarations and class declarations is that function declarations are "hoisted" and class declarations are not. This means that you can call a function BEFORE it has been declared in your source code. This is not the case with ES6 classes!

__You first need to declare your class and then access it, otherwise code like the following will throw a ReferenceError:__

Incorrect version => you try to create an instance of a class before it has been declared:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> p </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Rectangle</span><span class="pun">();</span><span class="pln"> </span><span class="com">// ReferenceError</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">class</span><span class="pln"> </span><span class="typ">Rectangle</span><span class="pln"> </span><span class="pun">{...}</span></li>
</ol></div>

Correct version $\implies$

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">class</span><span class="pln"> </span><span class="typ">Rectangle</span><span class="pln"> </span><span class="pun">{...}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> p </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Rectangle</span><span class="pun">();</span><span class="pln"> </span><span class="com">// WORKS !</span></li>
</ol></div>


### 4.3.5 Creating objects with functions (factories)

We have already seen three different ways to create objects (literals, constructor functions and ES6 classes).

Objects can be created as “literals”:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> darkVador </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> firstName</span><span class="pun">:’</span><span class="typ">Dark</span><span class="pun">’,</span><span class="pln"> lastName</span><span class="pun">:</span><span class="typ">’Vador</span><span class="pun">’};</span></li>
</ol></div>

Objects can be created with the keyword `new` and a constructor function or an ES6 class:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> darkVador </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Hero</span><span class="pun">(</span><span class="typ">’Dark</span><span class="pln"> </span><span class="typ">Vador</span><span class="pun">’,</span><span class="pln">&nbsp;</span><span class="pln">’empire</span><span class="pun">’);</span></li>
</ol></div>

Objects can also be created by functions that return objects (factories):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> rect </span><span class="pun">=</span><span class="pln"> canvas.getBoundingClientRect</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln">&nbsp;mxx </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">clientX </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">left</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln">&nbsp;my </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">clientY </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">top</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; <strong>return</strong></span><strong><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span><span class="com">// the getMousePos function returns an object. It’s a factory</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; x</span><span class="pun">:</span><span class="pln">&nbsp;mx</span><span class="pun">,</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; y</span><span class="pun">:</span><span class="pln">&nbsp;my</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

And here is how you can use this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> mousePos </span><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Mouse position x = "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> </span><span class="str">" y = "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">);</span></li>
</ol></div>

The call to `getMousePos` returns an object that has an `x` and a `y` property.


#### Notes for 4.3.5 Creating objects with functions (factories)

+ Creating objects
  + created as "literals", e.g., `var darkVador = { firstName:’Dark’, lastName:’Vador’};`
  + created w/ keyword `new` and a constructor function as `class` in ES6; e.g., `var darkVador = new Hero(’Dark Vador’, ’empire’);`
  + created by functions that return objects (factories), example

    ```js
    function getMousePos(event, canvas) {
        var rect = canvas.getBoundingClientRect();
        var mxx = event.clientX - rect.left;
        var my = event.clientY - rect.top;
    
        return { // the getMousePos function returns an object. It’s a factory
            x: mx,
            y: my
        }
    }

    var mousePos = getMousePos(evt, canvas);
    ```


### 4.3.6 Static properties and methods

#### Live coding video: static properties and methods

<a href="https://edx-video.net/W3CJSIXX2016-V004400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/227zv2av)

__Source code from the examples in the above video__

+ The first example
  + [CodePen Demo](https://codepen.io/w3devcampus/pen/NgbVQo?editors=0012)
  + [Local Demo](src/04c-example05.html)
+ The second example is further in this page, or at CodePen
  + [CodePen Demo](https://codepen.io/w3devcampus/pen/rmOjrv?editors=0011)
  + [Local Demo](src/04c-example06.html)


#### Class properties and methods vs. instances' properties and methods

Sometimes, there are methods "attached" to a class, not to an instance of a class.

For example, imagine the `Hero` class we've already seen, and we would like to know how many Star Wars's heroes have been created. If zero hero has been created, it's obvious that we could not use this property with an instance of the class such as Dark Vador: `darkVador.getNbHeroes();` this would make no sense.

Instead, object oriented programming languages have the concept of "class properties" and "class methods" that complete the "instance properties" and "instance methods" that we've seen up to this point. `Hero.getNbHeroes()` means "Hey, class Hero, can you tell me how many heroes have been created using your class?". Class methods define the "class behavior", and instance methods define the instances' behavior. `darVador.speak();` means "Hey, Dark Vador, please, tell us something!". I speak to Dark Vador and I'm expecting something creative from him, such as "I'm your father, Luke!".

It's the same for properties. If there is a property named `nbHerosCreated` in the class Hero, it represents the DNA of the class, not of the instances. You can say "the Hero class has the number of heroes it created", and you can say "Dark Vador has a name and belongs to the empire side", but not "Dark Vador has a number of heroes he created". We have class properties and instance properties.


#### Class methods

__The `static` keyword is used for defining class methods__

How do we distinguish them? By using the static keyword. When you see a method preceded by the `static` keyword, it means that you see a class property or a class method.

<p style="border: 1px solid; padding: 20px; margin: 20px; text-align: center;"><span style="color: #ff0000;"><strong>The <span style="font-family: 'courier new', courier;">static</span> keyword defines a static method for a class. <br><br><span style="color: #0000ff;">Static methods are called without instantiating their class <br>and can&nbsp;not&nbsp;be called through a class instance.</span> <br><br><em>Consequence</em>: do not use instance properties in their body!<br><br>Static methods are often used to create utility functions for an application (source: MDN).<br><br></strong></span></p>


#### Class properties

Class properties should be defined after the class definition, and declared using the name of the class followed by the . operator and the name of the property.

Example: `Point.nbPointsCreated` in the example below. A best practice is to ALWAYS use them this way.

There is another way to declare Class properties (using static getters and setters -- see next section, for advanced users), but we recommend using this one for beginners.

#### Example to create class methods

__Example of creation and use of class methods and properties using an ES6 class__

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">class<span class="pln"> </span><span class="typ">Point</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;constructor</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> x</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> y</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; <strong>// static property</strong></span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="typ">&nbsp; &nbsp; &nbsp; Point</span><span class="pun">.</span><span class="pln">nbPointsCreated</span><span class="pun">++;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp;}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp;// static method</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp;<strong>static</strong></span><strong><span class="pln"> distance</span><span class="pun">(</span><span class="pln">a</span><span class="pun">,</span><span class="pln"> b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; const</span><span class="pln"> dx </span><span class="pun">=</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">x </span><span class="pun">-</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; const</span><span class="pln"> dy </span><span class="pun">=</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">y </span><span class="pun">-</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sqrt</span><span class="pun">(</span><span class="pln">dx</span><span class="pun">*</span><span class="pln">dx </span><span class="pun">+</span><span class="pln"> dy</span><span class="pun">*</span><span class="pln">dy</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp;}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="com">// static property definition is necessarily outside of the class with ES6</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="typ">Point</span><span class="pun">.</span><span class="pln">nbPointsCreated</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">// We create 3 points</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">const</span><span class="pln"> p1 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Point</span><span class="pun">(</span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">const</span><span class="pln"> p2 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Point</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">const</span><span class="pln"> p3 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Point</span><span class="pun">(</span><span class="lit">12</span><span class="pun">,</span><span class="pln"> </span><span class="lit">27</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"&lt;p&gt;Distance between points (5, 5) and (10, 10) is "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="typ">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>Point</strong></span><strong><span class="pun">.</span><span class="pln">distance</span><span class="pun">(</span><span class="pln">p1</span><span class="pun">,</span><span class="pln"> p2</span><span class="pun">)</span></strong><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&lt;/p&gt;"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"Number of Points created is "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><strong><span class="typ">Point</span><span class="pun">.</span><span class="pln">nbPointsCreated</span></strong><span class="pun">;</span></li>
</ol></div>

Running example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/rmOjrv)

[Local Demo](src/04c-example06.html)


#### Notes for 4.3.6 Static properties and methods

+ Static properties and methods
  + some properties and methods attached to class not instance
  + class properties and class methos: complete the instance properties and instance methods seen up to this point
  + class and instance
    + class method: define the class' behavior
    + instance method: define the instance's behavior
    + class property: DNA of the class, not of the instances
    + instance property: DNA of the instance
  + declare class methods
    + `static` keyword: used for defining class methods
    + called w/o instantiating their class and unable to be called through a class instance
    + often used to create utility functions for an application
  + declare class properties
    + defined after the class definition
    + definition necessarily outside of the class w/ ES6
    + declare using the name of the class followed by the operator and the name of the property
    + best practice: ALWAYS using the format `ClassName.property`
    + alternative: using static setters and getters

+ Example: [declare class methods and class properties](src/04c-example06.html)
  + declare class: `class Point {...}`
    + declare constructor: ``constructor(x, y) {...}`
      + instance properties: `this.x = x; this.y = y;`
      + static/class property: `Point.nbPointsCreated++;`
    + class method: `static distance(a, b) { const dx = a.x - b.x; const dy = a.y - b.y; return Math.sqrt(dx*dx + dy*dy) }`
  + <span style="color: brown;">static property definition</span>: `Point.nbPointCreated = 0;`
  + create points: `const p1 = new Point(5, 5); const p2 = new Point(10, 10); const p3 = new Point(12, 27);`
  + display number of point created: `document.body.innerHTML += "Number of Points created is " + Point.nbPointsCreated;`
  + display the distance btw (5, 5) and (10, 10): `document.body.innerHTML += "<p>Distance between points (5, 5) and (10, 10) is " + Point.distance(p1, p2) + "</p>";`


### 4.3.7 [Advanced] Modern JavaScript's getters and setters

It is possible to use special methods that are called __getters__ and __setters__. They allow to make some checks when one is trying to set a value to a property, or to do some processing when accessing it (for example for displaying it in uppercase, even if its value is in lowercase).

These special functions are called "getters" and "setters", and are declared using the keywords `get` and `set` followed by the name of the property they define.

Typical use (_lines 7 and 11_):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">class</span><span class="pln"> </span><span class="typ">Person</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; constructor</span><span class="pun">(</span><span class="pln">givenName</span><span class="pun">,</span><span class="pln"> familyName</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">givenName </span><span class="pun">=</span><span class="pln"> givenName</span><span class="pun">;</span><span class="pln"> </span><span class="com">// "normal name"</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; <strong>this</strong></span><strong><span class="pun">.</span><span class="pln">_familyName </span><span class="pun">=</span><span class="pln"> familyName</span><span class="pun">;</span><span class="pln"> </span><span class="com">// starts with "_"</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><strong><span class="kwd">&nbsp; &nbsp; get</span><span class="pln"> familyName</span><span class="pun">()</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">_familyName</span></strong><span class="pun">.</span><span class="pln">toUpperCase</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><strong><span class="kwd">&nbsp; &nbsp; set</span><span class="pln"> familyName</span><span class="pun">(</span><span class="pln">newName</span><span class="pun">)</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // validation could be checked here such as </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // only allowing non numerical values</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong>this</strong></span><strong><span class="pun">.</span><span class="pln">_familyName </span></strong><span class="pun">=</span><span class="pln"> newName</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; walk</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">givenName </span><span class="pun">+</span><span class="pln"> </span><span class="str">' '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">_familyName </span></strong><span class="pun">+</span><span class="pln"> </span><span class="str">' is walking.'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">let p1 = new Person('Michel', 'Buffa');</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">console.log(p1.familyName); // will display BUFFA in the devtool console</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // this will call implicitly get familyName();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">p1.familyName = 'Smith'; &nbsp; &nbsp;// this will call implicitly set familyName('Smith');</span></li>
</ol></div>

Notice that when you declare `get familyName() {...}` for example, you define implicitly a property whose name is "`familyName`" and that will be accessible using `object.familyName`, where `object` is an instance of the class. See _lines 22-25_ in the example above. Displaying the value of `p1.familyName` will call implicitly `get familyName()`, while `p1.familyName = 'Smith';` will call set `Name('Smith');`

As `get familyName()` defines an implicit property named `familyName`, the convention is to use `this._familyName` for storing its value (the same name preceded by an underscore).

Example at CodePen:

[CodePen Demo](https://codepen.io/w3devcampus/pen/WOoQgw)

[Local Demo](src/js/04c-example07.js)


#### Notes for 4.3.7 [Advanced] Modern JavaScript's getters and setters

+ getters and setters methods
  + useful for processing properties, doing checks, changing them before returning their values, etc.
  + setters methods:
    + making some checks when trying to set a value to a property
    + declare w/ the keyword `set` followed by the name of the property defined
    + violation check
  + getters methods:
    + doing some processing when accessing the value of a property
    + declare w/ the keyword `get` followed by the name of the property defined
    + `get propertyName()` usage:
      + equivalent to declaring a property named `propertyName`
      + define an implicit property name `propertyName`
      + have to use ANOTHER name for the variable used to store the property value
      + convention: keep the same name but add an underscore at the beginning
      + example: `get name(n) { this._name = n; }`

+ Example: [getters and setters](src/js/04c-example07.js)
  + declare class: `class Person {...}`
    + declare constructor: `constructor(givenName, familyName) {...}`
      + declare `givenName` property: `this.givenName = givenName;`
      + declare `_familyName` property (start w/ '_'): `this._familyName = familyName;`
    + access a property w/ uppercase: `get familyName() {return this._familyName.toUpperCase(); }`
    + set a property checking violation: `set familyName(newName) { this.familyName = newName; }`
    + walking method: `walk() { return (this.giveName + '' + this._familyName + 'is walking.'); }`
  + create an object: `p1 = new Person('Michel', 'Buffa');`
  + display family name capitalized: `console.log(p1.familyName);` $\to$ `BUFFA`
  + implicit set familyName to 'Smith': `p1.familyName = 'Smith';`




