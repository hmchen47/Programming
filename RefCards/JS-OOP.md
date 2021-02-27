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



## `this` keyword

+ [`this` keyword](../WebDev/Frontend-W3C/5-JavaScript/04b-StructureData.md#426-this-accessing-properties)
  + accessing an object property or calling another method from an object method
  + meaning "from this object"
  + followed by '.' operator every time to access current value of an object property or call method within
  + bound to calling object when the function called, not when the function created
  + confusion: in cases of event listeners, the callbacks called by the browser
  + best practice: not to have event listeners in an object








