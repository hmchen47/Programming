# Object-Oriented Programming w/ JavaScript


## Objects - Overview

+ [JavaScript object](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-131-the-best-way-to-learn-javascript)
  + defined by two braces `{...}` w/ a set of properties/values inside, separated by a comma
  + more structured values

+ [Embedded objects](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-131-the-best-way-to-learn-javascript)
  + arrays: using brackets to create arrays of things
  + different elements within an arrays seperated by commas `,`

+ [Objects](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-159-objects-part-1)
  + declaration
    + using "{" and "}"
    + properties & values
  + accessing properties or method
    + using `.` operator
    + pre-defined objects: `window`, `document`, `navigator`, `console`, etc.

+ [Common objects & properties](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-159-objects-part-1)
  + auto-completion w/ `.` to display options in devtools console tab
  + the size of current browser window: `window.innerWidth` & `window.innerHeight`
  + current URL w/ the page: `window.location`
  + vendor of browser: `navigator.vender`


+ [Creating objects](..WebDev/Frontend-W3C/5-JavaScript/04c-StructureData.md#435-creating-objects-with-functions-factories)
  + created as "literals", e.g., `var darkVador = { firstName:'Dark', lastName:'Vador'};`
  + created w/ keyword `new` and a constructor function as `class` in ES6; e.g., `var darkVador = new Hero('Dark Vador', 'empire');`
  + created by functions that return objects (factories); e.g., `function getPos(mx, my) { return { x: mx, y: my } }`

+ [References and objects](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#521-references-and-objects)
  + pointer variable: containing the actual address of an object within the variable
  + reference variable: an alias to a variable
  + when modifying a reference variable, the original variable is modified $\gets$ two variables w/ the same object
  + types of values of a variable
    + primitive value (number, string, or boolean):
      + the variable containing the value directly
    + object:
      + containing the memory address of the object
      + pointing to an object or reference of this object
      + accessing the variable automatically resolving the reference
      + the value of the variable = the referenced object
  + arguments of function
    + primitive values
      + a "pass by value" language
      + passing a variable to a function as argument, the value of the variable copied into the argument
    + objects
      + reference of object copied into the argument
      + able to modify the reference object
      + change of reference: the origin variable (now point to another object) not modified

+ [Object comparison](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#522-comparing-two-objects)
  + returning boolean value whether w/ the same reference (pointing to the same objects)
  + identical objects but unequal
    + returning `false` (`===` or `==`)
    + objects w/ same type, same property values
    + w/ different references
    + pointing to different places in memory

+ Example: [draw and move balls w/ methods](../WebDev/Frontend-W3C/5-JavaScript/src/04d-example01.html)

+ Example: [comparisons of constructor function and class](../WebDev/Frontend-W3C/5-JavaScript/04d-StructureData.md#441-class-and-constructor)
  + constructor function: `function createBalls1(n) {...}`
  + constructor function w/ `new` keyword: `function createBalls2(n) {...}`
  + ES5 class: `class Ball() {...}`

+ Example: [draw and move balls w/ functions](../WebDev/Frontend-W3C/5-JavaScript/04d-StructureData.md#442-adding-methods-classes)

+ Example: [modifying copied object to modify original object](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#521-references-and-objects)
  + original object: `var originalObject = { name: 'Michel' };`
  + copied object: `var copy = originalObject;`
  + verification: `copy.name; // 'Michel'`
  + modify copied object: `copy.name = 'Dark Vador';`
  + original object verification: `originalObject.name; // 'Dark Vador'`



## Singleton Object

+ [Singleton objects](../WebDev/Frontend-W3C/5-JavaScript/04b-StructureData.md#422-from-objects-to-arrays)
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

+ [Property name](../WebDev/Frontend-W3C/5-JavaScript/04b-StructureData.md#423-property-declaration-syntax)
  + single or double quotes around the name of the property, or nothing at all
  + recommendation: no single or double quotes
  + exceptions: single or double quotes required
    + reserved words in JS
    + containing spaces or special characters
    + begining w/ a number
  + the name of property used as a variable


+ [Singleton object declaration](../WebDev/Frontend-W3C/5-JavaScript/04b-StructureData.md#425-elements-properties-and-methods)
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

+ [Manipulating properties and methods](../WebDev/Frontend-W3C/5-JavaScript/04b-StructureData.md#427-addingdeleting-properties-and-methods)
  + JS the only object-oriented language able to add or remove properties after an object has been created
  + example: [add properties & methods](../WebDev/Frontend-W3C/5-JavaScript/src/04b-example07.html)
  + example: [delete properties & methods](../WebDev/Frontend-W3C/5-JavaScript/src/04b-example08.html)

+ Example: [declare singleton object](../WebDev/Frontend-W3C/5-JavaScript/04b-StructureData.md#425-elements-properties-and-methods)

+ Example: [moving player](../WebDev/Frontend-W3C/5-JavaScript/04b-StructureData.md#425-elements-properties-and-methods)


## Classes and Objects

+ [Classes](../WebDev/Frontend-W3C/5-JavaScript/04c-StructureData.md#431-classes-definition)
  + JS not real classes
    + two types of object-oriented languages: classes-based and prototype-based
    + JS: a prototype-based language
  + singleton objects: objects only occurred once
  + templates w/ same properties and methods
    + ES5: not having such concept but "constructor functions"
    + post ES5: concept of classes and the syntax developed similar to what other object-oriented programming language


+ [Declare classes](../WebDev/Frontend-W3C/5-JavaScript/04c-StructureData.md#433-creating-objects-using-modern-javascripts-classes)
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



## Class Properties and Class Methods

+ [Static properties and methods](../WebDev/Frontend-W3C/5-JavaScript/04c-StructureData.md#436-static-properties-and-methods)
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

+ Example: [declare class methods and class properties](../WebDev/Frontend-W3C/5-JavaScript/src/04c-example06.html)


## `this` keyword

+ [`this` keyword](../WebDev/Frontend-W3C/5-JavaScript/04b-StructureData.md#426-this-accessing-properties)
  + accessing an object property or calling another method from an object method
  + meaning "from this object"
  + followed by '.' operator every time to access current value of an object property or call method within
  + bound to calling object when the function called, not when the function created
  + confusion: in cases of event listeners, the callbacks called by the browser
  + best practice: not to have event listeners in an object


## `new` Keyword

+ [The 'new' keyword](../WebDev/Frontend-W3C/5-JavaScript/04c-StructureData.md#432-the-new-keyword)
  + constructor functions
    + ES5 and prior
    + a pseudo-class template
  + syntax of constructor functions same as creating a function w/ exceptions
    + name w/ capitalized on 1st letter
      + a good practice for readability
      + a noun: the name of the class of objects to build
    + the `new` keyword for new objects
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
  + code outside of methods usually for initializing the properties

+ Example: [a constructor function](../WebDev/Frontend-W3C/5-JavaScript/src/04c-example02.html)
  + declare constructor function: `function Hero(name, side) {...}`
    + `name` property: `this.name = name;`
    + `side` property: `this.side = side;`
    + `speak` method: `this.speak = function() { return "<p>My name is " + this.name + ", I'm with the " + this.side + ".</p>"; }`  
  + create instances: `var darkVador = new Hero("Dark Vador", "empire"); var luke = new Hero("Luke Skywalker", "rebels"); ...`
  + function for heros to speak: `function makeHeroesSpeak() { document.body.innerHTML += darkVador.speak(); ...}`



## Getters and Setters Methids

+ [getters and setters methods](../WebDev/Frontend-W3C/5-JavaScript/04c-StructureData.md#437-advanced-modern-javascripts-getters-and-setters)
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

+ Example: [getters and setters](../WebDev/Frontend-W3C/5-JavaScript/src/js/04c-example07.js)




## The "global" window object

+ [`window` object](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#523-the-global-window-object)
  + JS executed by an environment
    + usually a Web browser
    + some HTTP Web servers using JS for coding the servicer side of Web sites of applications
  + environment as 'global object'
    + Web server: global object named `window`
    + global variables defined w/ keyword `var`: properties of the `window` object, e.g., `var a = 1;` $\to$ `a === window.a` the same variable
    + predefined functions as the methods of the `window` object, including `prompt`, `alert`, etc.
    + global variable created w/ keyword `let`: not part of the `window` object
    + top-level of programs and functions: not part of the `window` object
  + best practice: global variables declared w/ `let`
    + declared w/ `var` instead to inspect from the devtool console
    + switching back to use `let`, later
  + predefined objects: `navigator === window.navigator` & `document === window.document`
  + predefined functions and methods:
    + functions: `parseInt('10 little children'); // 10` & `window.parseInt('10 little children'); // 10`
    + methods: `alert === window.alert;  prompt === window.prompt`



## Built-in JS class: Object

+ [`Object` class](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#524-built-in-js-class-object)
  + father of all objects
  + all objects inherit the properties and methods from the special class
  + `var o = {};` equivalent to `var o = new Object();`

+ [The `toString()` method](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#524-built-in-js-class-object)
  + inherited from `Object` by all objects
  + transformed into a string by calling `toString()` implicitly when trying to display an object
  + using `+` operator to concantate string will force the other arguments to convert to string by implicitly calling `toString()` method

+ [The `valueOf()` method](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#524-built-in-js-class-object)
  + return the value of an object
  + inherited from `Object` by all objects
  + example: `var t = [1, 2, 3]; t.valueOf(); // [1, 2, 3]`, `t.toString(); // "1,2,3"`

+ [`toString()` method: specification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
  + syntax: `obj.toString()`
  + docstring:
    + every object w/ a `toString()` method that automatically called when the object is to be represented as a text value or when an objkject is referred to be in manner in which a string is expected
    + by default, inherited by every object descent from `Object`
  + parameter
    + `radix` (option): $2 \le \text{ radix } \le 36$
  + return:  a string representing the object

+ [`valueOf()` method: specification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)
  + syntax: `obj.value()`
  + docstring:
    + convert an object to a primitive value
    + rarely invoked by user
    + automatically invoked by JS when encountering an object where a primitive value is expected
    + by default, inherited by every object descended from `Object`
  + return: the primitive value of the specified object



## Built-in JS class: Array

+ [`Array()` constructor](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#525-built-in-js-class-array)
  + syntax:
    + `[element0, element1, ..., elementN]`
    + `new Array(element0, element1[, ...[, elementN]])`
    + `new Array(arrayLength)`
  + docstring: used to create `Array` objects
  + parameters
    + `elementN`:
      + initialized w/ the given elements, except in the case where a single argument is passed to the `Array` constructor
      + applied to JS arrays created w/ the `Array` constructor, not array literals created w/ the bracket syntax
    + `arrayLength`
      + the only argument
      + an interger btw 0 and $2^{32} - 1$ (inclusive)
      + return a new JS array w/ its `length` property set to the number
      + an array of `arrayLength` empty slots



## Built-in JS class: `Number`

+ [`Number` class](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#526-the-most-useful-methods-of-the-class-array)
  + used to transform strings into numbers
  + recommendation: using `parseInt` or `parseFloat` instead
  + constructing w/ `Number` class
    + `new` keyword, e.g., `var n = Number('3.1416'); n; // 3.1415`
    + type of variable: `typeof n; // "number"`
  + convert a string to an integer number: `var n = parseInt('3.1416'); n; // 3`
  + convert a string to a float number: `var n = parseFloat('3.1416'); n; // 3.1416`
  + `MAX_VALUE` and `MIN_VALUE`: useful non-modifiable properties (constants)
    + `Number.MAX_VALUE`: 1.7976931348623157e+308
    + `Number.MIN_VALUE`: 5e-324

+ [Useful methods for converting numbers](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#526-the-most-useful-methods-of-the-class-array)
  + `toFixed()`: set the number of digits for the deccimal part of a number
  + `toPrecision()`: return numbers in scientific notation
  + `toExponential()`:
    + a number to use a scientific notation
    + example: `var a = 1000; a.toExponential(); console.log(a); // le+3`
  + `toString([b])`:
    + convert a number to its string representation
    + `b`: base, default base 10
    + example: `let n = 10; n.toString(); // 10` & `n.toString(2); // 1010`

+ [`Number()` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number)
  + syntax: `new Number(value)`
  + docstring: create a `Number` object
  + parameter
    + `value`: the numeric value of the object being created

+ [`Number.prototype.toFixed()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)
  + syntax: `numObj.toFixed([digits])`
  + docstring: format a number using fixed-point notation
  + parametre
    + `digits` (optional):
      + the number of digits to apprear after the decimal point
      + range: [0, 20]
      + default: 0
  + return: a string representing the given number using fixed-point notation

+ [`Number.prototype.toExponential()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toExponential)
  + syntax: `numObj.toExponential([fractionDigits])`
  + docstring: return a string representing the `Number` object in exponential notation
  + parameter
    + `fractionDigits` (optional):
      + specify the number of digits after the decimal point
      + default: as many digits as necessary to specify the number
  + return: a string representing the given `Number` object in exponential notation w/ one digit before the decimal point, rounded to `fractionDigits` digits after the decimal point

+ [`Number.prototype.toString()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString)
  + syntax: `numObj.toString([radix])`
  + docstring: return a string representing the specified `Number` object
  + parameter
    + `radix` (optional): specify the base to use for representing numeric values, [0, 36]
  + return: a string representing the specified `Number` object



## Built-in JS class: String

+ [`String` class](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#528-built-in-js-class-string)
  + used to build new strings
  + constructor: `var name = new String('Miche');`
  + recommendaton: using the standard syntax, e.g., `var name = 'Michel';`
  + properties and methods: `var name = 'Michel';`
    + `length` property: `name.length; // 6`
    + string as an array w/ index: `name[0]; // "M"`
    + not modifiable: `name[0] = 'Z'; // "Z"` and `name; // 'Michel'`
    + other expression: `'Michel'.length; // 6` and `'Michel'[0]; // "M"`
  + changing character(s)
    + string not modifiable
    + build a new string by concatenating substrings
    + reference to another address in memory

+ [Useful methods of `String` class](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#528-built-in-js-class-string)
  + `toUpperCase`: return the string in upper case, not changing the original string
  + `toLowerCase`: return the string in lower case, not changing the original string
  + `indexOf(char[, start])`:
    + looking for string value `char` starting from `start`
    + return the index of string valuse passed as parameter (`char`)
    + return `-1` if nothing matched
  + `charAt`:
    + return the char at the index passed as parameters
    + return empty string if index out of bound (< 0 or > str.length )
  + `lastIndexOf`: return the last index of the string value passed as parameter

+ [The `slice` and `substring` methods](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#529-the-most-useful-methods-of-the-class-string)
  + both used to extract a substring from a string
  + similarity
    + two parameters: `start` and `stop` index
    + excluding element at `stop` index
    + the original string remaining unchanged
    + `start = stop`: return an empty string
    + `stop` omitted: extract characters to the end of the string
    + either arguments > `str.length`: using `str.length` instead
  + difference
    + occuring only when the second parameter is negative
    + recommendation: using `substring` for most common cases
    + `slice()`
      + w/ negative `stop`: extract substring starting from index `start` to `length + stop`
      + `start > stop`: NOT swap these two arguments
      + `start < 0`: set char from the end of string
      + `stop < 0`: set stop to `length + stop`
    + `substring`
      + w/ negative `stop`: extract substring reverse from index start to `start + stop`
      + `start > stop`: swap these two parameters
      + either argument negative or NaN: treated as 0

+ [The `split()`, `join()` and `concat()` methods](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#529-the-most-useful-methods-of-the-class-string)
  + `split()`:
    + return an array of strings w/ parameter as separator
    + original string unchanged
  + `join()`: build a string from an array of strings
  + `concat`:
    + return concatenated strings
    + original string unchanged
    + `+` operator same effect but change the original string

+ [`String.prototype.indexOf()` method](https://tinyurl.com/n2m66t3p)
  + syntax: `str.indexOf(searchValue [, fromIndex])`
  + docstring: return the index within the calling `String` object of the 1st occurrence of the specified value
  + parameters:
    + `searchValue`: the string value to search for
    + `fromIndex` (optional): an integer representing the index at which to start the search, defaults to 0
  + return: the index of the first occurrent of `searchValue` or `-1` if not found


## Built-in JS class: Math

+ [`Math` class](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#5210-built-in-javascript-class-math)
  + many properties and methods useful for arithmetic expressions
  + properties and methods by using the name of the class followed by the dot operator to access them
  + no constructor existed: `var m = new Math(); // M5777:1 Uncaught TypeError: Math is not a constructor ...`
  + common properties:
    + $\pi$: `Math.PI; // 3.141592653589793`
    + $\sqrt{2}$: `Math.SQRT2; // 1.4142135623730951`
    + Euler constant: `Math.E; // 2.718281828459045`
    + Neperian log of 2: `Math.LN2; // 0.6931471805599453`
    + Neperian log of 10: `Math.LN10; // 2.302585092994046`
  
+ [`Math.random()` method](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#5210-built-in-javascript-class-math)
  + generate random numbers btw 0 and 1
  + return a float value btw 0 and 1
  + get a number btw a min and max value: `val = ((max - min) * Math.random()) + min;`
  + examples:
    + random number in [0, 1]: `Math.random(); // 0.6033316111663034`
    + random number in [0, 100]: `Math.random() * 100; // 11.780563288516422`
    + function to generate random number in [min, max]: `function getRandomValue(min, max) { return ((max - min) * Math.random()) + min; }`
    + random number in [5, 10]: `getRandomValue(5, 10); // 5.064160540161435`

+ [Math and rounding methods](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#5210-built-in-javascript-class-math)
  + `round`: get the closest integer value
  + `ceil`: always round a number up to the next largest integer
  + `floor`: return the largest integer less than or equal to a given number
  + example - rounding a number: `Math.round(Math.random()); // 0 or 1`

+ [The `max()` and `min()` methods](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#5210-built-in-javascript-class-math)
  + get max and min values w/ `Math.max(a, b)` and `Math.min(a, b)`
  + useful for restrict a value btw minimum and maximum bounds
  + examples
    + min of two values: `Math.min(12, 4); // 4`
    + max of two values: `Math.max(14, 4); // 14`
    + function to set restrict values: `function restrictValue(value, min, max) { return Math.min(Math.max(1, value), max) }`
    + apply restrict function: `restrictValue(40, 1, 20); // 20`, `restrictValue(-10, 1, 20); // 1`, and `restrictValue(10, 1, 20); // 10`

+ [Some arithmetical methods](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#5210-built-in-javascript-class-math)
  + `sin()`: sine function in radians
  + `cos()`: cosine function in radians
  + `tan()`: tangent function in radians
  + `atan()`: arctangent function in radians
  + `atan2()`: arctangent function returning in angle in the plane; useful for getting an angle btw a point in a canvas and the mouse cursor


## Built-in JS class: Date

+ [`Date` class](../WebDev/Frontend-W3C/5-JavaScript/05b-Forms.md#5211-built-in-js-class-date)
  + constructor: `new Date(arg);`
    + return value actually a `Date` object but displayed by calling `toString()` on this object
    + `arg` omitted: return the current date
    + `arg`:
      + a string encoding a date
      + a set of numeric values separated by a comma for month, day, hour, and so on
      + a Unix "timestamp" (number of milliseconds elapsed since 1970)
  + numerical parameters:
    + order: year, month (0-11), dat (1-31), time (0-23), minutes (0-59), second, milliseconf (0-999)
    + not always w/ them all
    + must always be in the order
  + calling `Date` constructor w/o new: return currrent date
  + useful instance methods: [`getXXX` and `setXXX`](https://tinyurl.com/htvdv7ep)
    + set and get `XXX`
    + `XXX`: `FullYear`, `Month`, `Day`, `Hours`, `Minutes`, `Seconds`, `MilliSeconds`


## The `table` object

+ [The table object](../WebDev/Frontend-W3C/5-JavaScript/05c-Forms.md#532-the-html-table-javascript-api)
  + make dynamic table management possible
  + enable to add or delete a row, a cell, and modify the contents of the cells, etc.
  + most useful properties
    + `rows`: a collection of all `<tr>` elements in a table
    + `caption`: the `<caption>` element of a table
    + `tFoot`: a reference to the `<tfoot>` element of a table
    + `tHead`: a reference to the `<thead>` element of a table
  + most useful methods
    + `insertRow()`:
      + create an empty `<tr>` element and add it to the table
      + insert a new row at the end of the table: `var row = table.insertRow();`
      + insert at the index = `idx` and push down all the rows after: `var row = table.insertRow(idx);`
    + `deleteRow()`: remove a row `<tr>` from the table, e.g., `table.deleteRow(0);` delete the row at index 0
    + `createCaption()`: create an empty `<caption>` element and add it to the table
    + `deleteCaption()`: remove the first `<caption>` element from the table
    + `createTHead()`: create an empty `<thead>` element and add it to the table
    + `deleteTHead()`: remove the `<thead>` element from the table
    + `createTFoot()`: create an empty `<tfoot>` element and add it to the table
    + `deleteTFoot()`: remove the `<tfoot>` element from the table

+ [The tableRow object (`<tr>`)](../WebDev/Frontend-W3C/5-JavaScript/05c-Forms.md#532-the-html-table-javascript-api)
  + access a row using the DOM API or the selector API
  + create a row using the DOM API to get a Row object
  + most useful properties
    + `cells`: a collection of all `<td>` ot `<th>` elements in a table row
    + `rowIndex`: the position of a row in the `rows` collection of a table
    + `sectionRowIndex`: the position of a row in the `rows` collection of a `<tbody>`, `<thead>` or `<tfoot>`
  + most useful methods
    + `insertCell()`:
      + insert a cell into the current table `row`
      + no parameters: append a cell after the last cell of the row
      + index of the cell as a unique parameter: insert the row and push other cells to the right
      + `index = 0`: insert at the first position
      + `index = -1`: insert at the last position
    + `deleteCell()`:
      + delete a cell from the current table row
      + unique parametre: the index of the cell to remove
      + `index = 0`: delete the first cell
      + `index = -1`: delete the last cell


## Accessible forms

+ [HTML input submit w/o JavaScript](../WebDev/Frontend-W3C/5-JavaScript/05c-Forms.md#534-html-forms-and-javascript)
  + several ways to collect server-side data from a form in Web page: REST Web service, servlets, MS ASP pages, etc.
  + client-side forms indicate to which server and how the data sent by `action` and `method` attributes, respectively
  + `<button type="submit">` and `<input type=submit>` used to submit the form content

+ [HTML input submit w/ Ajax/JavaScript](../WebDev/Frontend-W3C/5-JavaScript/05c-Forms.md#534-html-forms-and-javascript)
  + JS used for validating user input "on the fly"
  + event listeners used for tracking user's interactions in real time, including typing or selecting a color, moving a slide, etc.
  + perform validation steps along w/ visual feedback
  + used for more global validation before sending a form to a remote server, e.g., checking password by entering twice in two different fields
  + used to make a WebApp using form data locally, perhaps w/ some client-side persistence API, e.g. data displayed in a dynamic HTML table w/o remote database but saving data locally

+ Example: [validate input on the fly](../WebDev/Frontend-W3C/5-JavaScript/05c-Forms.md#534-html-forms-and-javascript)


## Example: A Contact Manager

+ [`Contact` and `ContactManager` classes](../WebDev/Frontend-W3C/5-JavaScript/05e-Forms.md#551-a-contact-manager-part-1)
  + `Contact` class: a person w/ a name and an email

    ```js
    class Contact {
      constructor(name, email) {
        this.name = name;
        this.email = email;
      }
    }
    ```

  + `ContactManager` class:
    + a minimal ES6 class to build a contact manager
    + only one property: the list of contacts
    + two methods: add and remove contact

    ```js
    class ContactManager {
      constructor() {   // built the contact manager w/ empty list of contacts
        this.listOfContacts = [];
      }

      add(contact) {
        this.listOfContacts.push(contact);
      }

      remove(contact) {
        for (let i = 0; i < this.listOfContacts.length; i++) {
          var c = this.listOfContacts[i];

          if (c.email === c.email) {
            this.listOfContacts.splice(i, i);
            break;
          }
        }
      }

      printContactsToConsole() {
        this.listOfContacts.forEach(function(c) {
          console.log(c.name);
        });
      }
    }
    ```

+ [`Contact` and `ContactManager` verification](../WebDev/Frontend-W3C/5-JavaScript/05e-Forms.md#551-a-contact-manager-part-1)
  + create contacts: `var cm = new ContactManager(); var c1 = new Contact("Jimi Hendrix", "jimi@rip.com"); var c2 = new Contact("Robert Fripp", "robert.fripp@kingcrimson.com"); var c3 = new Contact("Angus Young", "angus@acdc.com"); var c4 = new Contact("Arnold Schwarzenneger", "T2@terminator.com");`
  + add contacts into contact manager: `cm.add(c1); cm.add(c2); cm.add(c3); cm.add(c4);`
  + display to verify: `cm.printContactsToConsole();`
  + delete a contact: `cm.remove(c2);`
  + display to verify: `cm.printContactsToConsole();`

+ [Sorting contacts in manager](../WebDev/Frontend-W3C/5-JavaScript/05e-Forms.md#551-a-contact-manager-part-1)
  + define `sort` method in `ContactManager`: `sort() { this.listOfContacts(ContactManager.compareByName); }`
  + class method for comparing two contacts by name: 
  
    ```js
    static compareName(c1, c2) {
      if (c1.name < c2.name>)
        return -1;
      
      if (c.name > c2.name)
        return 1;
      
      return 0;
    }
    ```

+ [Load and save w/ Local Storage](../WebDev/Frontend-W3C/5-JavaScript/05e-Forms.md#552-persistence-part-2)
  + loading / saving from a key/value pair database located in hard disk
  + associated to the domain of Web application
  + add `load` and `save` methods for constructor
  + convert array of contacts to JSON and save into local storage: `save() { localStorage.contacts = JSON.stringify(this.lostOfContacts); }`
  + verify `LocalStorage` w/ devtool:
    + Chrome: devtool > Application > Local Storage (left panel) > `https://js.codepen.io` > Key/Value pair (right panel)
    + Firefox: devtool > setting icon on top-right corner > Storage (left panel)
    + Safari: devtool > Storage (top banner) > Local Storage > `https://js.codepen.io` > key/value pair
  + empty list of contacts: `empty() { this.listOfContacts = []; }`
  + load contacts from `LocalStorage` and convert JSON back into JS object: `load() { if (localStorage.contact != undefined) { this.listOfContacts = JSON.parse(localStorage.contacts); }}`
  + verify `save()`, `empty()` and `load()` w/ printing in console
    + `console.log("---Saving contacts to local storage---"); cm.save();`
    + `console.log("---Empty the list of contacts---"); cm.empty(); cm.printContactsToConsole();`
    + `console.log("---Loading contacts from local storage---); cm.load(); cm.printContactsColsole();`

+ [Display contacts in HTML5 table w/ Xhr2](../WebDev/Frontend-W3C/5-JavaScript/05e-Forms.md#553-display-contacts-in-an-html5-table-part-3)
  + Refer to Xhr2 of [JSON data from a REST Web Service](../WebDev/Frontend-W3C/5-JavaScript/05d-Forms.md#examples)
  + add container to display contact table: `<div id="contacts"></div>`
  + add function to display users in table: `function displayUsersAsTable(users) {...}`
    + empty the container: `var usersDiv = document.querySelector("#users"); usersDiv.innerHTML = "";`
    + create and populate the table w/ users: `var table = document.createElement("table");`
    + iterate to display users of array: `usersDiv.forEach(function(currentUser) {...});`
      + create a row: `var row = table.insertRow();`
      + insert cells in the row: `var nameCell = row.insertCell(); nameCell.innerHTML = currentUser.name; var cityCell = row.insertCell(); cityCell.innerHTML = currentuser.address.city;`
    + add the table to the container: `usersDiv.appendChild(table);`

+ [Display contacts in HTML5 table](../WebDev/Frontend-W3C/5-JavaScript/05e-Forms.md#553-display-contacts-in-an-html5-table-part-3)
  + implementation w/ `class ContactManager` 
  + add button element: `<button onclick="search();">Get a remote list of users' names and emails</button>`
  + add empty container for table: `<div id="users"></div>`
  + specify table styles: `table { margin-top: 20px; }` & `table, tr, td { border: 1px solid; }`
  + add method to display contacts in table: `displayContactsAsTable(idOfContainer) {...}`
    + empty the container: `let container = document.querySelector('#' + idOfContainer); container.innerHTML = "";`
    + no contact: `if (this.listOfContacts.length === 0) { container.innerHTML = "<p>No contacts to sdisplay!>/p>"; return; }`
    + create and populate the table w/ users: `let table = document.createElement("table");`
    + iterate the users of the array: `this.listOfContacts.forEach(function(currentContact) {...});`
      + create row: `let row = table.insertRow();`
      + add data of the row: `row.innerHTML = "<td>" + currentContact.name + "</td>" + "<td>" + currentComtact.email + "</td>";`
    + add table to the div container: `container.appendChild(table);`

+ [Input form to add new contact](../WebDev/Frontend-W3C/5-JavaScript/05e-Forms.md#554-use-a-form-to-enter-new-contacts-part-4)
  + event listener: `<form onsubmit="return formSubmitted();">...</form>`
  + grouping inputs fields and submit button: `<fieldset>...</field>`
    + legend of group: `<legend>Personal information</legend>`
    + name input form: `<label> Name : <input type="text" id="name" required> </label>`
    + email input form: `<label> Email : <input type="email" id="email" required> </label>`
    + submit button: `<button>Add new Contact</button>`
  + add buttons for table displaying: `<div id="contacts"></div>`
    + empty button: `<button onclick="emptyList();">Empty</button>`
    + save button: `<button onclick="cm.save();">Save</button>`
    + reload button: `<button onclick="loadList();"></button>`
  + callback function once button clicked: `function formSubmitted() {...}`
    + access elements: `let name = document.querySelector("#name"); let email = document.querySelector("#email");`
    + assign values in a new contact: `let newContact = new Contact(name.value, email.value); cm.add(newContact);`
    + empty the input fields: `name.value = ""; email.value = "";`
    + refresh the table: `cm.displayContactsAsATable("contacts");`
    + prevent from submitting by the browser to reload the HTTP page: `return false;`
  + empty list: `function emptyList() { cm.empty(); cm.displayContactsAsATable("contacts"); }`
  + load list: `function loadList() { cm.load(); cm.displayContactsAsATable("contacts"); }`
  + save strings in Local Storage: `localStorage.contacts = JSON.stringify(this.listOfContacts);`






