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

+ Example: [comparisons of constructor function and class](../WebDev/Frontend-W3C/5-JavaScript/04d-StructureData.md#441-class-and-constructor)
  + constructor function: `function createBalls1(n) {...}`
  + constructor function w/ `new` keyword: `function createBalls2(n) {...}`
  + ES5 class: `class Ball() {...}`

+ Example: [draw and move balls w/ functions](../WebDev/Frontend-W3C/5-JavaScript/04d-StructureData.md#442-adding-methods-classes)
  
+ Example: [draw and move balls w/ methods](../WebDev/Frontend-W3C/5-JavaScript/src/04d-example01.html)




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



## Getters and Setts Methids

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









