# Module 4: Structuring data

## 4.3 Objects (part 3): creating multiple objects

### 4.3.1 Classes: definition

Let's study what is the concept of "class" in object oriented programming languages.

So far in this course, we've only used singleton objects: objects that only occur once: player, darkVador, etc.

Ok, this is not quite true, I'd forgotten that we created many balls in the module 2 game. We'll come back to this example further down the page!

But even with the balls from module 2, we did not use a template to tell us how to easily create multiple objects that share the same properties and the same methods, but whose properties' values may differ.

For example, imagine Luke Skywalker, Ian Solo and Dark Vador. What do they have in common? They all are Star Wars heroes, they all have a name, they all belong to one side (the good/bad people, or rebels vs empire), etc. Imagine that we have a way of programming that describes not the objects themselves, but a "model", a "template" for these objects. We could call it StarWarsHero and use it for creating our heroes' objects.

Imagine the balls from module 2: they all had the same shape (circle), the same x, y, radius and color properties, but they were all different. They all belonged to the same class of object (ball), but they were all different in terms of their properties' values.

<span style="color: brown; font-weight: bold;">In many programming languages, these templates are called "classes".

+ Before 2015, in JavaScript 5 (also called ES5), we did not have such a concept, instead we had "constructor functions".
+ In modern JavaScript (after 2015),  we have the concept of classes, and the syntax is rather similar to what we find in other object oriented programming languages.

Let's introduce these two ways of defining "pseudo classes" with ES5's function constructors, and with modern JavaScript's classes!


#### Notes for 4.3.1 Classes: definition

+ Classes
  + JS not real classes
    + two types of object-oriented languages: classes-based and prototype-based
    + JS: a prototype-based language
  + singleton objects: objects only occurred once
  + templates w/ same properties and methods
    + ES5: not having such concept but "constructor functions"
    + post ES5: concept of classes and the syntax developed similar to what other object-oriented programming language
  + example: balls w/ the same shape (circle), the same x, y, radius, and color properties but different values


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

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><strong><span style="color: #008888;">function</span><span>&nbsp;</span><span style="color: #AA0066;">Hero</span><span style="color: #666600;">(</span><span>name</span><span style="color: #666600;">,</span><span>&nbsp;side</span><span style="color: #666600;">)</span><span>&nbsp;</span><span style="color: #666600;">{</span></strong></li>
<li><span></span><span style="color: #008888;">&nbsp; &nbsp; this</span><span style="color: #666600;">.</span><span>name&nbsp;</span><span style="color: #666600;">=</span><span>&nbsp;name</span><span style="color: #666600;">; // code outside of methods is usually for initializing</span></li>
<li><span></span><span style="color: #008888;">&nbsp; &nbsp; this</span><span style="color: #666600;">.</span><span>side&nbsp;</span><span style="color: #666600;">=</span><span>&nbsp;side</span><span style="color: #666600;">; // the properties. Very often, they match the parameters</span></li>
<li><span></span></li>
<li><span></span><span style="color: #008888;">&nbsp; &nbsp; this</span><span style="color: #666600;">.</span><span>speak&nbsp;</span><span style="color: #666600;">=</span><span>&nbsp;</span><span style="color: #008888;">function</span><span style="color: #666600;">()</span><span>&nbsp;</span><span style="color: #666600;">{</span></li>
<li><span></span><span style="color: #008888;">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span>&nbsp;</span><span style="color: #008800;">"&lt;p&gt;My name is "</span><span>&nbsp;</span><span style="color: #666600;">+</span><span>&nbsp;</span><span style="color: #008888;">this</span><span style="color: #666600;">.</span><span>name&nbsp;</span><span style="color: #666600;">+</span></li>
<li><span></span><span style="color: #008800;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;", I'm with the "</span><span>&nbsp;</span><span style="color: #666600;">+</span><span>&nbsp;</span><span style="color: #008888;">this</span><span style="color: #666600;">.</span><span>side&nbsp;</span><span style="color: #666600;">+</span><span>&nbsp;</span><span style="color: #008800;">".&lt;/p&gt;"</span><span style="color: #666600;">;</span></li>
<li><span></span><span style="color: #666600;">&nbsp; &nbsp; }</span></li>
<li><strong><span style="color: #666600;">}</span></strong></li>
<li><span>&nbsp;</span></li>
<li><strong><span style="color: #008888;">var</span><span>&nbsp;darkVador&nbsp;</span><span style="color: #666600;">=</span><span>&nbsp;</span><span style="color: #008888;">new</span><span>&nbsp;</span><span style="color: #AA0066;">Hero</span><span style="color: #666600;">(</span><span style="color: #008800;">"Dark Vador"</span><span style="color: #666600;">,</span><span>&nbsp;</span><span style="color: #008800;">"empire"</span><span style="color: #666600;">);</span></strong></li>
<li><strong><span style="color: #008888;">var</span><span>&nbsp;luke&nbsp;</span><span style="color: #666600;">=</span><span>&nbsp;</span><span style="color: #008888;">new</span><span>&nbsp;</span><span style="color: #AA0066;">Hero</span><span style="color: #666600;">(</span><span style="color: #008800;">"Luke Skywalker"</span><span style="color: #666600;">,</span><span>&nbsp;</span><span style="color: #008800;">"rebels"</span><span style="color: #666600;">);</span></strong></li>
<li><strong><span style="color: #008888;">var</span><span>&nbsp;ianSolo&nbsp;</span><span style="color: #666600;">=</span><span>&nbsp;</span><span style="color: #008888;">new</span><span>&nbsp;</span><span style="color: #AA0066;">Hero</span><span style="color: #666600;">(</span><span style="color: #008800;">"Ian Solo"</span><span style="color: #666600;">,</span><span>&nbsp;</span><span style="color: #008800;">"rebels"</span><span style="color: #666600;">);</span></strong></li>
<li><span>&nbsp;</span></li>
<li><span style="color: #008888;">function</span><span>&nbsp;makeHeroesSpeak</span><span style="color: #666600;">()</span><span>&nbsp;</span><span style="color: #666600;">{</span></li>
<li><span>&nbsp; &nbsp; document</span><span style="color: #666600;">.</span><span>body</span><span style="color: #666600;">.</span><span>innerHTML&nbsp;</span><span style="color: #666600;">+=</span><span>&nbsp;darkVador</span><span style="color: #666600;">.</span><span>speak</span><span style="color: #666600;">();</span></li>
<li><span>&nbsp; &nbsp; document</span><span style="color: #666600;">.</span><span>body</span><span style="color: #666600;">.</span><span>innerHTML&nbsp;</span><span style="color: #666600;">+=</span><span>&nbsp;luke</span><span style="color: #666600;">.</span><span>speak</span><span style="color: #666600;">();</span></li>
<li><span>&nbsp; &nbsp; document</span><span style="color: #666600;">.</span><span>body</span><span style="color: #666600;">.</span><span>innerHTML&nbsp;</span><span style="color: #666600;">+=</span><span>&nbsp;ianSolo</span><span style="color: #666600;">.</span><span>speak</span><span style="color: #666600;">();</span></li>
<li><span style="color: #666600;">}</span></li>
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
    + `speak` method: `this.speak = function() { return "<p>My name is " + this.name + ", I'm with the " + this.side + ".</p>"; }`  
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

<div><ol>
<li value="1"><strong>class Hero {</strong></li>
<li>&nbsp; &nbsp; <strong>constructor</strong><strong>(name, side) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.name = name; // property</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.side = side; // property</li>
<li>&nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp;<strong> speak</strong><strong>() { // method, no more "function"</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; return "&lt;p&gt;My name is " + this.name +</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;", I'm with the " + this.side + ".&lt;/p&gt;";</li>
<li>&nbsp; &nbsp; }</li>
<li>}</li>
<li>&nbsp;</li>
<li>var darkVador = new Hero("Dark Vador", "empire");</li>
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
    + simply define a class using the keyword `class` followed by the name of the class
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
    + declare method: `speak() { return "<p>My name is " + this.name + ", I'm with the " + this.side + ".</p>"; }`
  + declare a new instance: `var darkVador = new Hero("Dark Vador", "empire");`


### 4.3.4 Declaring a class before using it


__You must declare a class before using it!__

Unlike functions, classes must be declared BEFORE using them.

An important difference between function declarations and class declarations is that function declarations are "hoisted" and class declarations are not. This means that you can call a function BEFORE it has been declared in your source code. This is not the case with ES6 classes!

__You first need to declare your class and then access it, otherwise code like the following will throw a ReferenceError:__

Incorrect version => you try to create an instance of a class before it has been declared:

<div><ol>
<li value="1">var p = new Rectangle(); // ReferenceError</li>
<li>&nbsp;</li>
<li>class Rectangle {...}</li>
</ol></div>

Correct version $\implies$

<div><ol>
<li value="1">class Rectangle {...}</li>
<li>&nbsp;</li>
<li>var p = new Rectangle(); // WORKS !</li>
</ol></div>


### 4.3.5 Creating objects with functions (factories)

We have already seen three different ways to create objects (literals, constructor functions and ES6 classes).

Objects can be created as “literals”:

<div><ol>
<li value="1">var darkVador = { firstName:'Dark', lastName:'Vador'};</li>
</ol></div>

Objects can be created with the keyword `new` and a constructor function or an ES6 class:

<div><ol>
<li value="1">var darkVador = new Hero('Dark Vador',&nbsp;'empire');</li>
</ol></div>

Objects can also be created by functions that return objects (factories):

<div><ol>
<li value="1">function getMousePos(event, canvas) {</li>
<li>&nbsp; &nbsp; var rect = canvas.getBoundingClientRect();</li>
<li>&nbsp; &nbsp; var&nbsp;mxx = event.clientX - rect.left;</li>
<li>&nbsp; &nbsp; var&nbsp;my = event.clientY - rect.top;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; <strong>return</strong><strong> { // the getMousePos function returns an object. It's a factory</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; x:&nbsp;mx,</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; y:&nbsp;my</strong></li>
<li><strong>&nbsp; &nbsp; }</strong></li>
<li>}</li>
</ol></div>

And here is how you can use this:

<div><ol>
<li value="1">var mousePos = getMousePos(evt, canvas);</li>
<li>&nbsp;</li>
<li>console.log("Mouse position x = " + mousePos.x + " y = " + mousePos.y);</li>
</ol></div>

The call to `getMousePos` returns an object that has an `x` and a `y` property.


#### Notes for 4.3.5 Creating objects with functions (factories)

+ Creating objects
  + created as "literals", e.g., `var darkVador = { firstName:'Dark', lastName:'Vador'};`
  + created w/ keyword `new` and a constructor function as `class` in ES6; e.g., `var darkVador = new Hero('Dark Vador', 'empire');`
  + created by functions that return objects (factories), example

    ```js
    function getMousePos(event, canvas) {
        var rect = canvas.getBoundingClientRect();
        var mx = event.clientX - rect.left;
        var my = event.clientY - rect.top;
    
        return { // the getMousePos function returns an object. It's a factory
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

<div><ol>
<li value="1">class Point {</li>
<li>&nbsp; &nbsp;constructor(x, y) {</li>
<li>&nbsp; &nbsp; &nbsp; this.x = x;</li>
<li>&nbsp; &nbsp; &nbsp; this.y = y;</li>
<li>&nbsp; &nbsp; &nbsp; <strong>// static property</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; Point.nbPointsCreated++;</strong></li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// static method</li>
<li>&nbsp; &nbsp;<strong>static</strong><strong> distance(a, b) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; const dx = a.x - b.x;</li>
<li>&nbsp; &nbsp; &nbsp; const dy = a.y - b.y;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; return Math.sqrt(dx*dx + dy*dy);</li>
<li>&nbsp; &nbsp;}</li>
<li>}</li>
<li><strong>// static property definition is necessarily outside of the class with ES6</strong></li>
<li><strong>Point.nbPointsCreated=0;</strong></li>
<li>&nbsp;</li>
<li>// We create 3 points</li>
<li>const p1 = new Point(5, 5);</li>
<li>const p2 = new Point(10, 10);</li>
<li>const p3 = new Point(12, 27);</li>
<li>&nbsp;</li>
<li>document.body.innerHTML += "&lt;p&gt;Distance between points (5, 5) and (10, 10) is " + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>Point</strong><strong>.distance(p1, p2)</strong> + "&lt;/p&gt;";</li>
<li>document.body.innerHTML += "Number of Points created is " + <strong>Point.nbPointsCreated</strong>;</li>
</ol></div>

Running example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/rmOjrv)

[Local Demo](src/04c-example06.html)


#### Notes for 4.3.6 Static properties and methods

+ Static properties and methods
  + some properties and methods attached to class not instance
  + class properties and class methods: complete the instance properties and instance methods seen up to this point
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
    + declare constructor: `constructor(x, y) {...}`
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

<div><ol>
<li value="1">class Person {</li>
<li>&nbsp; &nbsp; constructor(givenName, familyName) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.givenName = givenName; // "normal name"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>this</strong><strong>._familyName = familyName; // starts with "_"</strong></li>
<li>&nbsp; &nbsp; }</li>
<li> </li>
<li><strong>&nbsp; &nbsp; get familyName()</strong> {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; return <strong>this._familyName</strong>.toUpperCase();</li>
<li>&nbsp; &nbsp; }</li>
<li> </li>
<li><strong>&nbsp; &nbsp; set familyName(newName)</strong> {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // validation could be checked here such as </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // only allowing non numerical values</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong>this</strong><strong>._familyName </strong>= newName; </li>
<li>&nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; walk() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; return (this.givenName + ' ' + <strong>this._familyName </strong>+ ' is walking.');</li>
<li>&nbsp; &nbsp; }</li>
<li>}</li>
<li></li>
<li>let p1 = new Person('Michel', 'Buffa');</li>
<li>console.log(p1.familyName); // will display BUFFA in the devtool console</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // this will call implicitly get familyName();</li>
<li>p1.familyName = 'Smith'; &nbsp; &nbsp;// this will call implicitly set familyName('Smith');</li>
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
    + set a property w/ violation check: `set familyName(newName) { this._familyName = newName; }`
    + walking method: `walk() { return (this.giveName + '' + this._familyName + 'is walking.'); }`
  + create an object: `p1 = new Person('Michel', 'Buffa');`
  + display family name capitalized: `console.log(p1.familyName);` $\to$ `BUFFA`
  + implicit set familyName to 'Smith': `p1.familyName = 'Smith';`


### 4.3.8 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics

+ Did you know that modern JavaScript's classes are just "a syntactic sugar"? In fact they are equivalent to constructor functions from ES5...
+ There are two sorts of object-oriented languages: class-based languages and prototype-based languages.
JavaScript is a prototype-based language. In this introductory course, we managed to avoid this term! Without getting into too much details, you might be curious about prototypes and maybe read some Web pages related to those. 

  And yes, ES6 classes are not "real classes"... They are meant to make developers' lives easier, i.e., for the developers who already know a class-based language such as Java, C#, etc.


#### Optional projects

+ Try to write one of the example from the previous modules without using any single time the keyword "function", use only JavaScript classes and instances. In case of problems -> go the the forum and share your experience, this will be very useful for all students to see what sort of problems can occur when moving from a functional approach to an object-oriented approach
+ Build a class-based contact manager!
  
  1. Try to build a small database (in a JavaScript array) that will hold your contacts. You will use classes for defining:<br>
    1) a `Contact` class, with `givenName`, `familyName`, `phoneNumber`, etc. and<br>
    2) an HTML set of input fields (not inside a form) for creating new contacts + an "Add contact" button. When you click on the button, it calls an `addContact()` callback of your own that will create a new contact and add it to your database (using the push method on arrays).
  2. [ADVANCED] input fields and buttons inside a form!

    __Beware__: either do not put your input fields and buttons inside a `<form>` or the buttons will submit the form (this is their default behavior, unless you add an attribute `type="button"` to the buttons). Or you might also declare `<form onsubmit = "return processMyForm();">`, this will call the method `processMyForm` (You can change this name if you like) when the form is submitted. In the `processMyForm` method, get the content of the input fields, build a contact, add it to the array etc. And then, do not forget to return `false` to avoid the submission of the HTML form).

  3. It would be cool to also have a `listContact()` function that will generate a list of contacts (create `<ul>...</ul>` with `<li>...</li>` inside, one for each contact).
  4. Now, try to write an ES6 class `ContactManager` (or you could also use an object literal for that..., but let's try  practicing JavaScript classes!), that will have the array of contact as a property.
  5. Create an instance `db` of this class: `let db = new ContactManager();`
  6. Add in the `ContactManager` class an `add(c)` and a `list()` method (for adding a contact `c` to the array of contacts, and for listing the contacts).
  7. Now, when you press the buttons, the `addContact()` method from step 1 will call `db.addContact(c)` where `db` is the instance of your `ContactManager` class and `c` is an instance of the `Contact` class.
  8. Feel free to customize this project with nice CSS, etc.



