# Module 4: Structuring data


## 4.2 Objects (part 2): properties and methods

### 4.2.1 Introduction

You're already familiar with the concept of objects, but so far we've only seen one simple form, called "objects literals" or "singleton objects". I think we've referred to them as "simple objects" in the course. Here is an example:

<div><ol>
<li value="1">var js1 = {</li>
<li>&nbsp; &nbsp; courseName<strong>:</strong> 'JavaScript intro',</li>
<li>&nbsp; &nbsp; weeks<strong>:</strong> 5,</li>
<li>&nbsp; &nbsp; madeBy:&nbsp;'W3Cx',</li>
<li>&nbsp; &nbsp; author: 'Michel Buffa' // no "," after the last property!, even if ES5/6 accept it</li>
<li>}</li>
</ol></div>

And we access properties values using the "." operator, like this:

<div><ol>
<li value="1">&gt; js1.author</li>
<li>"Michel Buffa"</li>
<li>&nbsp;</li>
<li>&gt; js1.weeks</li>
<li>5</li>
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

<div><ol>
<li value="1">&gt; <strong>var darkVador = ['villain', 'half human half machine'];</strong> </li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; darkVador[0]</li>
<li>"villain"</li>
<li>&nbsp;</li>
<li>&gt; darkVador[1]</li>
<li>"half human half machine"</li>
</ol></div>

And now, look at this object:

<div><ol>
<li value="1">var darkVador = {</li>
<li>&nbsp; &nbsp; job: 'villain',</li>
<li>&nbsp; &nbsp; race: 'half human half machine'</li>
<li>}; </li>
</ol></div>

They look a bit similar, don't they?

+ Same name of the variable that contains the object = `darkVador`
+ Instead of '<span style="color: brown;">[' and '<span style="color: brown;">]</span>' that we used for defining an array, we use '<span style="color: brown;">{</span>' and '<span style="color: brown;">}</span>' for defining an object
+ The elements of the object (its <span style="font-weight: bold; text-decoration: underline">properties</span>) are separated by a comma ','
+ The pairs of keys/values are separated by '<span style="color: brown;">:</span>' as in <code>race<span style="color: brown;">:</span> 'half human, half machine</span>'</code>
+ The last pair of keys/values has no ',' at the end.

__It is possible to access the object's properties with "." or with brackets__

We saw that we can use the "." operator, followed by the property name. It's also possible to use the bracket notation, and manipulate the object as an array whose indexes, instead of being 0, 1, 2 etc., are the property names!

<div><ol>
<li value="1">&gt; var book = {</li>
<li> title: 'Le Petit Prince',</li>
<li> author: 'Saint-Exupery'</li>
<li>};</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; <strong>var title = book.title;</strong></li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt;<strong> title;</strong></li>
<li><strong>"Le Petit Prince"</strong></li>
<li>&nbsp;</li>
<li>&gt; <strong>var title = book['title'];</strong></li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt;<strong> title</strong></li>
<li><strong>"Le Petit Prince";</strong></li>
<li>&nbsp;</li>
<li>&gt; var author = book['author'];</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; author;</li>
<li>"Saint-Exupery"</li>
</ol></div>

As you can see, if you look at _lines 7-10_ and _13-16_, writing `book.title` or `book['title']` is equivalent!

<span style="color: brown; font-weight: bold">In JavaScript, objects are arrays whose indexes are property names: please remember this!</span>


#### Notes for 4.2.2 From objects to arrays

+ Singleton objects
  + singleton object: a table whose keys/indexes defined
  + __object literal__
    + a comma-separated list of name-value pairs wrapped in curly braces
    + encapsulating data, enclosing it in a tidy package
  + minimizing the use of global variables which can cause problems when combining code
  + array defined w/ '<span style="color: brown; font-weight: bold;">[</span>' and '<span style="color: brown; font-weight: bold;">]</span>'
  + characteristics font-weight: bold;
    + object defined w/ '<span style="color: brown; font-weight: bold;">{</span>' and '<span style="color: brown; font-weight: bold;">}</span>'
    + elements (properties) of object separated by a comma '<span style="color: brown; font-weight: bold;">,</span>'
    + pairs of keys/values separated by '<span style="color: brown; font-weight: bold;">:</span>'
    + the last pair of keys/values w/o '<span style="color: brown; font-weight: bold;">,</span>' at the end
  + accessing properties w/ '<span style="color: brown; font-weight: bold;">.</span>' or brackets followed by the property name
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

<div><ol>
<li value="1"><strong>var louis = {age: 40}; // WE DO THIS MOST OF THE TIME!</strong></li>
<li>var louis = {"age": 40};</li>
<li>var louis = {'age': 40}; </li>
</ol></div>


#### In some cases we have to put quotes around the property name

+ When it is a reserved word from JavaScript,
+ Or it contains spaces or special characters,
+ Or it begins with a number.

Examples:

<div><ol>
<li value="1"><strong>book.1stPublication = '6 April 1943'; // begins with a number</strong></li>
<li value="1"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // Throws a SyntaxError</strong></li>
<li>book['1stPublication'] = '6 April 1943'; // OK</li>
<li></li>
<li>book.date of publication =&nbsp;'6 April 1943'; // spaces not allowed!<br></li>
<li>book['date of publication']&nbsp;=&nbsp;'6 April 1943'; // allowed, but avoid!</li>
</ol></div>


#### Another classic case where the name of a property is in a variable

In this case it is necessary  to use the syntax with '[' and ']' ...

Example:

<div><ol>
<li value="1">&gt; var key = 'title';</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt;<strong> book[key];</strong></li>
<li>"Le Petit Prince"</li>
</ol></div>


#### Notes for 4.2.3 Property declaration syntax

+ Property name
  + single or double quotes around the name of the property, or nothing at all
  + recommendation: no single or double quotes
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

    book.1stPublication = '6 April 1943';   // throws a SyntaxError
    book['1stPublication'] = '6 April 1943';

    var key = 'title';  // title as property name
    book[key];
    ```


### 4.2.4 An object can contain another object

Example:

<div><ol>
<li value="1">&gt; var book = {</li>
<li>&nbsp; &nbsp; name: 'Catch-22',</li>
<li>&nbsp; &nbsp; published: 1961,</li>
<li>&nbsp; &nbsp; <strong>author</strong><strong>: { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // embedded object!</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; givenName: 'Joseph',</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; familyName: 'Heller'</strong></li>
<li><strong>&nbsp; &nbsp; }</strong></li>
<li>};</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; book.author.givenName;</li>
<li>"Joseph"</li>
<li>&nbsp;</li>
<li>&gt; book.author.familyName;</li>
<li>"Heller"</li>
</ol></div>

Accessing the embedded object `author` is done by chaining property accesses using the "." operator, like in `book.author.givenName` (here we access the `givenName` property of the object `author`, which is also a property of the `book` object).


#### Notes for 4.2.4 An object can contain another object

+ Embedded objects in singleton object
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

+ For <span style="color: brown; font-weight: bold;">arrays, we speak of <span style="color: brown; font-weight: bold;">elements</span>
+ For <span style="color: cyan; font-weight: bold;">objects</span>, we talk about <span style="color: cyan; font-weight: bold;">properties</span>
+ But <span style="color: lightgreen; font-weight: bold;">a property can also be a function</span>, in which case it is called a <span style="color: lightgreen; font-weight: bold; text-decoration: underline;">method</span>

__Yes, it is possible for an object's property to be a function!__

A very simple example:

<div><ol>
<li value="1">var medor = {</li>
<li>&nbsp; &nbsp; name: 'Benji',</li>
<li>&nbsp; &nbsp; bark: function(){</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; alert('Ouarf, Ouarf!');</li>
<li>&nbsp; &nbsp; }</li>
<li>};</li>
</ol></div>

In this example, the bark property's value is a function, so we call bark "a method".

__A method is a special property that corresponds to the object's behavior__

<div>
<p><strong><span style="color: #3366ff;">Properties correspond to <span style="color: #3366ff;">an object's DNA</span> (its characteristics), <br><span style="color: #3366ff;">and are nouns</span> (age, name, etc.)</strong></p>
<p><strong><span style="color: #008000;">Methods</span> correspond to <span style="color: #008000;">an object's behavior <br></span>and <span style="color: #008000;">are verbs</span> (bark, move, changeSpeed, etc.)</strong></p>
</div>

#### Calling a method

Since a method is a property we can use the '.' operator (or brackets with the method's name as a string index).

Let's see some examples:


[CodePen Demo](https://codepen.io/w3devcampus/pen/RpmzQY)

[Local Demo](src/04b-example03.html)

JavaScript source code:

<div><ol>
<li value="1">var<strong> darkVador </strong>= {</li>
<li>&nbsp; &nbsp; race: 'human',</li>
<li>&nbsp; &nbsp; job: 'villain',</li>
<li>&nbsp; &nbsp; <strong>talk</strong><strong>: function() {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; return 'come to the dark side, Luke!';</strong></li>
<li><strong>&nbsp; &nbsp; }</strong></li>
<li>}</li>
<li>&nbsp;</li>
<li>function dvSpeak() {</li>
<li>&nbsp; &nbsp; document.body.innerHTML += '&lt;p&gt;Dark Vador says ' +<strong> darkVador.talk();</strong> + '&lt;/p&gt;';</li>
<li>}</li>
</ol></div>

In _line 1_, we created a simple object named `darkVador`, that has two properties (`race` and `job`) and a method (`talk`).

In the dvSpeak function, at line 10, we call `darkVador`'s talk method. The syntax is a mix between the one for accessing a property (with the '.' operator), and the one for calling a function (with parentheses and ';' at the end).

When we write darkVador.talk(), we are executing the talk method of the object `darkVador`, but in plain English, we're just asking Dark Vador to talk. We invoke its behavior!


__Another example with the player we saw briefly in Module 2__

Here is the last version of the player object we saw in our small game:

[CodePen Demo](https://codepen.io/w3devcampus/pen/xqNoJX)

[Local Demo](src/04b-example04.html)

JavaScript source code:

<div><ol>
<li value="1">var player = {</li>
<li>&nbsp; &nbsp; x:10,</li>
<li>&nbsp; &nbsp; y:10,</li>
<li>&nbsp; &nbsp; width:20,</li>
<li>&nbsp; &nbsp; height:20,</li>
<li>&nbsp; &nbsp; color:'red'</li>
<li>}</li>
<li>&nbsp;</li>
<li>// and we also used two other functions for moving the player with the mouse</li>
<li>// and for drawing it as a filled rectangle</li>
<li>&nbsp;</li>
<li>function movePlayerWithMouse() {</li>
<li>&nbsp; &nbsp; if(mousePos !== undefined) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; player.x = mousePos.x;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; player.y = mousePos.y;</li>
<li>&nbsp; &nbsp; }</li>
<li>}</li>
<li>&nbsp;</li>
<li>function drawFilledRectangle(r) {</li>
<li>&nbsp; &nbsp; // BEST practice: save the context, use 2D transformations</li>
<li>&nbsp; &nbsp; ctx.save();</li>
<li> </li>
<li>&nbsp; &nbsp; // translate the coordinate system, draw relative to it</li>
<li>&nbsp; &nbsp; ctx.translate(r.x, r.y);</li>
<li> </li>
<li>&nbsp; &nbsp; ctx.fillStyle = r.color;</li>
<li>&nbsp; &nbsp; // (0, 0) is the top left corner of the monster</li>
<li>&nbsp; &nbsp; ctx.fillRect(0, 0, r.width, r.height);</li>
<li> </li>
<li>&nbsp; &nbsp; // BEST practice: restore the context</li>
<li>&nbsp; &nbsp; ctx.restore();</li>
<li>}</li>
</ol></div>

__Now that we've seen that we can include methods into objects, here is a better, more readable and more encapsulated version of our player object:__

<div><ol>
<li value="1">var player = {</li>
<li>&nbsp; &nbsp; x:10,</li>
<li>&nbsp; &nbsp; y:10,</li>
<li>&nbsp; &nbsp; width:20,</li>
<li>&nbsp; &nbsp; height:20,</li>
<li>&nbsp; &nbsp; color:'red',</li>
<li> </li>
<li>&nbsp; &nbsp; <strong>move</strong><strong>(x, y) {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; // change x and y coordinates of the player</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; // TODO!</strong></li>
<li><strong>&nbsp; &nbsp; },</strong></li>
<li><strong> </strong></li>
<li><strong>&nbsp; &nbsp; draw() {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; // draw the player at its current position</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; // with current width, height and color</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; // TODO!</strong></li>
<li><strong>&nbsp; &nbsp; }</strong></li>
<li>}</li>
</ol></div>


Assuming that the move and draw methods are fully implemented, we will now be able to call:

+ `player.move(mousePos.x, mousePos.y)` to change the position of the player,
+ `player.draw()` to draw the player at its current position, with its current size and color.

Readability is better, it is like asking the player to move, or asking it to draw itself. And we do not need to pass the x, y, width, height, color to the draw method: it is inside the player object, and it can access all its internal property values!

In the next section we will look at how we can access other object's properties from a method or call other methods.


#### Notes for 4.2.5 Elements, properties and methods

+ Singleton object declaration
  + definitions
    + element for arrays
    + property for objects
    + method: a function as a property in objects
  + properties
    + an object's DNS, its characteristics
    + nouns, e.g., age, name, etc.
  + methods
    + an object's behavior
    + verb, e.g., bank, move, changeSpeed, etc.
  + calling a method (similar to a property) w/ '.' or brackets w/ the method's name as a string index
  + including methods into object $\to$ more readable and more encapuslated version of an property-only object

+ Example: [declare singleton object](src/04b-example03.html)

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
        x:10, y:10,
        width:20, height:20,
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



#### Knowledge check 4.2.5

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

<div><ol>
<li value="1">var player = {</li>
<li>&nbsp; &nbsp; x:10,</li>
<li>&nbsp; &nbsp; y:10,</li>
<li>&nbsp; &nbsp; width:20,</li>
<li>&nbsp; &nbsp; height:20,</li>
<li>&nbsp; &nbsp; color:'red',</li>
<li> </li>
<li>&nbsp; &nbsp; move: function(x, y) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>this</strong><strong>.x = x</strong><strong>;</strong> // this.x is the property of "this object"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>this</strong><strong>.y = y;</strong></li>
<li>&nbsp; &nbsp; },</li>
<li> </li>
<li>&nbsp; &nbsp; draw: function(ctx) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // draw the player at its current position</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // with current width, height and color</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; //&nbsp;it's nearly the same code as the old drawFilledRect function</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.save();</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // translate the coordinate system, draw relative to it</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.translate(<strong>this.x, this.y</strong>);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.fillStyle = <strong>this.color;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // (0, 0) is the top left corner of the monster</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.fillRect(0, 0, <strong>this.width, this.height</strong>);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // BEST practice: restore the context</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.restore(); </li>
<li>&nbsp; &nbsp; }</li>
<li>}</li>
</ol></div>

Notice that we've used this followed by the '.' operator every time we've had to access the current value of an object's property (_lines 9, 10, 20, 22 and 24_).

We passed the canvas' graphic context as a parameter to the draw method (it's always good not to create dependencies when making objects). Passing the context as a parameter avoids using it as a global variable. If in another project we've got a context named "context" instead of "ctx", then we will just change the parameter when we call `player.draw`, otherwise we would have had to rename all occurrences of `ctx` in the code).

Same with the mouse coordinates we passed to the `move` method.

__Let's see the Dark Vador example with the use of `this` in a method__

[CodePen Demo](https://codepen.io/w3devcampus/pen/JWqgGZ)

[Local Demo](src/04b-example06.html)


JavaScript source code:

<div><ol>
<li value="1">var darkVador = {</li>
<li>&nbsp; &nbsp; race: 'human',</li>
<li>&nbsp; &nbsp; job: 'villain',</li>
<li>&nbsp; &nbsp; talk: function() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; return 'come to the dark side, Luke!' + <strong>this.breathe();</strong></li>
<li>&nbsp; &nbsp; },</li>
<li>&nbsp; &nbsp; describeYourself: function() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; return "I'm a " + <strong>this.race </strong>+ " and I'm a " + <strong>this.job </strong>+ </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;" in a series of movies!" + <strong>this.breathe();</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; },</li>
<li>&nbsp; &nbsp; breathe() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; return ".....shhhhhhhhh.....";</li>
<li>&nbsp; &nbsp; }</li>
<li>}</li>
<li>&nbsp;</li>
<li>function dvSpeak() {</li>
<li>&nbsp; &nbsp; document.body.innerHTML += '&lt;p&gt;Dark Vador describes himself: ' +&nbsp; &nbsp; &nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; darkVador.describeYourself(); + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; '&lt;/p&gt;'; </li>
<li>&nbsp; &nbsp; document.body.innerHTML += '&lt;p&gt;Dark Vador says: ' + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; darkVador.talk(); + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; '&lt;/p&gt;';</li>
<li>}</li>
</ol></div>

In this example, notice that the `describeYourself` method from the `darkVador` object uses the two properties `name` and `job` using the `this` keyword. We also call the `breathe` method from the two methods `describeYourself` and `talk`, using `this.breathe();`


#### Notes for 4.2.6 "this": accessing properties

+ `this` keyword
  + accessing an object property or calling another method from an object method
  + meaning "from this object"
  + followed by '.' operator every time to access current value of an object property or call method within
  + bound to calling object when the function called, not when the function created
  + confusion: in cases of event listeners, the callbacks called by the browser
  + best practice: not to have event listeners in an object
  + example: using `this` to access values and methods within an object

    ```js
    var player = {
        x:10,       y:10,
        width:20,   height:20,
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

<div><ol>
<li value="1">// empty object with properties/methods</li>
<li>var darkVador = {};</li>
<li>&nbsp;</li>
<li>// add properties after darkVador has been created</li>
<li> darkVador.race = 'human';</li>
<li> darkVador.job = 'villain';</li>
<li>&nbsp;</li>
<li>// add some methods</li>
<li> darkVador.talk = function() {</li>
<li>&nbsp; &nbsp; return 'come to the dark side, Luke!' + this.breathe();</li>
<li> };</li>
</ol></div>

_Lines 5, 6 and 9_: we can add properties and methods after the object has been created empty at _line 2_.


#### Deleting a property or a method

You can use the JavaScript keyword "delete" to delete an object's property (it will become `undefined`).

Example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/RpzNEP)

[Local Demo](src/04b-example08.html)

JavaScript code extract:

<div><ol>
<li value="1">function deleteSomeProperties() {</li>
<li>&nbsp; <strong>delete</strong><strong> darkVador.race;</strong></li>
<li><strong>&nbsp; delete darkVador.job;</strong></li>
<li>}</li>
</ol></div>


#### Notes for 4.2.7 Adding/deleting properties and methods

+ Manipulating properties and methods
  + JS the only object-oriented language able to add or remove properties after an object has been created
  + example: [add properties & methods](src/04b-example07.html)
    + declare an empty object: `var darkVador = {};`
    + add properties after object created: `darkVador.race = 'human'; darkVador.job = 'villain';`
    + add methods after object created: `darkVador.talk = function() { return 'come to the dark side, Luke!' + this.breath(); };`
  + example: [delete properties & methods](src/04b-example08.html)
    + delcare and add properties as the previous example
    + delete properties: `function deleteSomeProperties() { delete darkVador.race; delete darkVador.job; }`


#### Knowledge check 4.2.7

```js
let pacman = {};
pacman.color:'yellow';
pacman.shape: 'pizza';
```

1. Is the above code correct? (No/Yes)

  Ans: No<br>
  Explanation: No, it's not correct! While adding and removing properties after the object has been declared/created (line 1 of the source code), the syntax for declaring properties INSIDE an object (with ":") is no more valid. You must use the "=" operator for the assignment. The correct code is:

  ```js
  let pacman = {};
  pacman.color = 'yellow';
  pacman.shape = 'pizza';
  ```


### 4.2.8 Discussion

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.


#### Suggested topic of discussion:

We simplified the explanations for "`this`" in this introductory course. Normally, "`this`" is the current object when you use it inside an "object literal" (like in this [CodePen example from the course](https://codepen.io/w3devcampus/pen/JWqgGZ)).

But... we also met "`this`" in event listeners (see in [this example from the course](https://codepen.io/w3devcampus/pen/gmygzV?editors=1000). Look at the <code>onchange = "changePageBackgroundColor(<b>this.value</b>);")</code> ...

In fact, the "`this`" keyword can be confusing in JavaScript. The key thing to remember is that _it is bound to the calling object when the function is called,_ not when the function is created.

And in the case of event listeners, the callbacks are called by the browser... You can conclude that it's a good habit not to have event listeners in your objects: just use methods in which there is no confusion about "`this`".

Let's discuss that (or "this"?) in the forum :-)





