# JavaScript Programming Language

## General

+ [JavaScript](../WebDev/Frontend-W3C/5-JavaScript/01b-JSIntro.md#notes-for-123-javascript-is-the-interactive-glue)
  + the "magic trio" of Web page: HTML5/CSS/Javascript
  + the only programming language that a browser can run
  + w/o installing any plugins or extensions
  + a real standard of Web
  + interactive glue btw HTML and CSS
    + more than just in browser
    + able to be run outside of the browser
      + a node JS interpreter on a remote server
      + in scripts run by the OS

+ Learning JavaScript: [Best practice](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-131-the-best-way-to-learn-javascript)
  + read and tweak small JavaScript code snippet
  + carfully read the references that details some important parts of the language

+ [Folder structure of Web project](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-134-where-to-put-javascript-code)
  + CSS files in `css` subfolder
  + JavaScript file in `js` subfolder

+ [Example: creating project for math function plot](../WebDev/Frontend-W3C/5-JavaScript/01d-JSIntro.md#note-for-141-creating-an-htmlcssjs-project)




## History

+ [Creation of JavaScript](../WebDev/Frontend-W3C/5-JavaScript/01b-JSIntro.md#notes-for-124-javascript-history)
  + born in 1995
  + creator: Brendan Eich's team
  + organization: Netscape, ancestor of Mozilla
  + in association w/ Sun Microsystems, depending on Java, to provide server and client-oriented solutions
  + ispired by Java but only some naming conventions remaining the same
  + success following the popularity of Netscape Navigator 2 in March 1996
  + quickly integrated into other popular browsers
  + standardized by ECMA as the EcmaScript standard in 1996
  + called JavaScript or EcmaScript

+ [Versions of JavaScript](../WebDev/Frontend-W3C/5-JavaScript/01b-JSIntro.md#notes-for-124-javascript-history)
  + stable version supported by all major browsers: EcmaScript version 5 from 2010
  + EcmaScript 6 or ES 2015: introduced many new features
  + a new version every year w/ some adjustments/novelties
  + ES####: naming convention since 2015, #### = year
  + no global support list for browsers but `caniuse.com` used to check feature by feature

+ [JavaScript programming language](../WebDev/Frontend-W3C/5-JavaScript/01b-JSIntro.md#notes-for-124-javascript-history)
  + the only programming language running in browsers
  + integrated into nearly every popular Web browser
  + some applications compiled from JavaScript/HTML/CSS version into "classic" applications w/o a browser
  + invented to work not only on the client side but also on the server side
  + an interpreted language
  + most popular JavaScript engines
    + [SpiderMonkey](https://developer.mozilla.org/fr/docs/SpiderMonkey) (included in Mozilla Firefox)
    + [JavaScriptCore](https://developer.apple.com/reference/javascriptcore) (included in Apple Safari)
    + [Chrome V8](https://developers.google.com/v8/) (included in Google Chrome, in the Node.js server)
    + [Chakra](https://github.com/Microsoft/ChakraCore) (included in Microsoft Internet Explorer and now in the Microsoft Edge browser)



## Locations of JS code

+ [Locations of JavaScript Code](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-134-where-to-put-javascript-code)
  + in HTML code between `<script>` and `</script>` tag, either within `<body>...</body>` or `<head>...</head>`
  + external file
    + in local files, usually ending w/ `.js` suffix
    + in external file located on the Web
    + advantages
      + separate HTML and code
      + easier to read and maintain
      + reuse JavaScript code
      + cached JavaScript files to speed up page loads
    + usage
      + link the script file w/ `src` attribute of `<script>` tag
      + JavaScript file must end w/ `.js`
      + no `<script>...</script>` in `.js` file
      + external JavaScript file w/ `<script src="..."></script>` = `<script>...</script>` in HTML
      + multiple JavaScript allowed w/ `<script src="..."></script>`



## Debugging

+ [Debugging in JavaScript](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#note-for-135-how-to-debug-javascript)
  + error messages: printing message for debugging code
  + basics of debuging: seeing error messages
    + in the devtool console
    + in the "console tab" of source code editor

+ [Browser devtool for debugging](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#note-for-135-how-to-debug-javascript)
  + Swiss army knife of JavaScript: browser devtools, in particular, the devtool concole
  + open dev tools of browser
    + Windows: F12 (or ctrl-shift-i)
    + MacOS: cmd-option-i
  + console tab: error message or messages of `console.log(string)` JavaScript function displayed
  + example: `console.log("Some JavaScript code has been executed");`
  + code executed in sequence when the page is loaded
  + error message to debug
    + showing the error message in console tab
    + click the top-right corner on the error message to show the source code
    + the line causing error highlighted

+ [devtool console](../WebDev/Frontend-W3C/5-JavaScript/01f-JSIntro.md#notes-for-162-the-devtool-console)
  + a common way to debug JavaScript code
  + `console.log(...)`: instruction to write message to the devtool console
  + CodePen: click on the bottom left 'console' tab to display the console
  + Browser: open devtool, then click on 'cpnsole' tab
  + using concatentate operator `+` w/ `console.log(...)` for variable value


## Standard style

+ [JavaScript Standard Style](https://tinyurl.com/ymps7k46)
  + indentation: 2 spaces
  + single quote (`'`) for strings except to avoid escaping
  + no unused variables
  + add a space after keyword
  + add a space before a functiondeclaration's parentheses
  + always using `===` instead of `==`, exception: `obj == null` is allowed to check for `null || undefined`
  + infix operators must be spaced, e.g., `var message = 'hello, ' + name + '!'`
  + commas should have a space, e.g., `function greet (name, options) { ... }`
  + keep `else` statements on the same line as their curly braces
  + for multiline if statement, use curly braces
  + always handle the `err` function parameter, e.g., `run(function (err) { if (err) throw err window.alert('done') })`
  + declare browser globals w/ a `/* global */` comment
    + exceptions: `window`, `document`, and `navigator`
    + prevent accidental use of poorly-named browser globals, including `open`, `length`, `event` and `name`
  + multiple blank lines not allowed
  + ternary operator in a multi-line setting, place `?` and `:` on their own lines
  + `var` declarations: write each declaration in its own statement
  + wrap conditional assignments w/ additional parentheses, e.g., `while ((m = text.match(expr))) { // ... }`
  + add spaces inside a single line blocks, e.g., `function foo () { return true }`
  + use camelcase when naming variables and functions
  + trailing commas not allowed, e.g., `var obj = { message: 'hello',   // ✗ avoid }`
  + commas must be placed at the end of the the current line
  + dot shout be the same line as property, e.g., `.log('hello')`
  + files must be end w/ a new line
  + no space btw function identifiers and their invocations, e.g., `console.log('hello')`
  + add space btw colon and value in key value pair, e.g., `var obj = { 'key': 'value' }`
  + constructor names must begin w/ a capital letter, e.g., `var dog = new Animal()`
  + constructor w/ no arguments must be invoked w/ parentheses, e.g., `var dog = new Animal()`
  + objects must contain a getter when a setter is defined
  + constructors of derived classes must be `super`
  + use array literals instead of array constructore, e.g., `var nums = [1, 2, 3]`
  + avoid using `arguments.callee` and `argument.caller`
  + avoid modifying variables of class declarations
  + avoid modifying variable declared using `const`
  + avoid using constant expression in conditions (except loops), e.g., `if (false) {...} // ✗ avoid`
  + no control characters in regular expressions
  + no debugger statement
  + no `delete` operator on variables
  + no duplicated arguments in function definition
  + no duplicated name in class members
  + no duplicated keys in object literals
  + no duplicate `case` labels in `switch` statements
  + use a single import statement per module, e.g., `import { myFunc1, myFunc2 } from 'module'`
  + no empty character classes in regular expressions
  + no empty destructuring patterns, e.g., `const { a: {} } = foo  // ✗ avoid`
  + no using `eval()`
  + no reassigning exceptions in `catch` clauses
  + no extending native objects, e.g., `Object.prototype.age = 21     // ✗ avoid`
  + avoid unnecessary function binding
  + avoid unnecessary boolean casts, e.g., `if (!!result) { // ✗ avoid }`
  + no unnecessary parentheses around function expression, e.g., `const myFunc = function () { }`
  + use `break` to prevent fallthrough in `switch` cases
  + no floating decimals. e.g., `const discount = .5  // ✗ avoid`
  + avoid reassigning function declaration
  + no reassigning real-only global variables
  + no implied `eval()`, e.g., `setTimeout("alert('Hello world')")  // ✗ avoid`
  + no function declarations in nested blocks
  + no invalid regular expression string in `RegExp` constructors
  + no irregular whitespace
  + no using `__iterator__`
  + no labels that share a name with an in scope variable
  + no label statements
  + no unnecessary nested blocks
  + avoid mixing spaces and tabs for indentation
  + do not use multiple spaces except for indentation
  + no multiline strings
  + no `new` w/o assigning object to a variable
  + not using the `Function`, `Object`, `Symbol`, constructors
  + not using `new require`
  + not using primitive wrapper instances
  + not calling global object properties as functions, e.g., `const math = Math()   // ✗ avoid`
  + no octal literals
  + no octal escape sequences in string literals, e.g., `const copyright = 'Copyright \251'  // ✗ avoid`
  + avoid string concatenation when using `__dirname` and `__filename`, e.g., `const pathToFile = path.join(__dirname, 'app.js')`
  + avoid using `__proto__`, using `getPrototypeOf` instead
  + no redeclaring variables
  + avoid multiple spaces in regular expression literals, e.g., `const regexp = /test {3}value/`
  + assignments in return statements must be surrounded by parentheses
  + avoid assigning a variable to itself, e.g., `name = name    // ✗ avoid`
  + avoid comparing a variable to itself
  + avoid using the comma operator, e.g., `if (doSomething(), !!test) {}   // ✗ avoid`
  + restricted names should not be shadowed
  + spares arrays not allowed, e.g., `let fruits = ['apple',, 'orange']   // ✗ avoid`
  + tabs should not be used
  + regular string must not contain template literal placeholder
  + `super` must be called before using `this`
  + only `throw` an `Error` object
  + white space not allowed at the end of line
  + initializing to `undefined` not allowed
  + no unmodified conditions for loop, e.g., `for (let i = 0; i < items.length; j++) {...}    // ✗ avoid`
  + no ternary operator when simplier alternative exist
  + no unreachable code after `return`, `throw`, `continue`, and `break` statments
  + no flow control statements in `finally` blocks
  + the left operand of relational operators must not be negated
  + avoid unnecessary use of `.call()` and `.apply()`
  + avoid using unnecessary computed property keys on objects
  + no unnecessary constructive
  + no unnecessary use of escape
  + renaming import, export, and destructured assignments to the sam ename not allowed
  + no whitespace before properties
  + not using `with` statements
  + maintain consistency of newlines btw object properties
  + no padding withing blocks
  + no whitespace btw spread operators and their expressions
  + semicolon must have a space after and no space before in `for` loop
  + must have a space before blocks, e.g., `if (admin) {...}`
  + no space inside parentheses, e.g., `getName(name)`
  + unary operator must have space after, e.g., `typeof !admin`
  + use spaces inside comments, e.g., `// comment` & `/* comment */`
  + no space in template strings, e.g., <code>const message = &grace;Hello, ${name}&grave;</code>
  + use `isNaN()` when checking for `NaN`
  + `typeof` must be compared to a valid string, e.g., `typeof name === 'undefimed'   // ✗ avoid`
  + Immediately Invoked Function Expressions (IIFEs) must be wrapped
  + the `*` in `yield*` expression must have a space before and after, e.g., `yield * increment()`
  + avoid Yoda conditions, e.g., `if (42 === age) { }    // ✗ avoid`
  + never start a line w/ `[`, `(`, `, `+`, `*`, `/`, `-`, &grave;,`, `.`


## Common syntax

+ [JavaScript common syntax and devtool console](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-151-js-variables-and-values)
  + `//` and `/* (code block */`): comments
  + devtools console: able to type and execute JavaScript Code as an interperter

## Expressions and Operators

+ [Expression](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-155-js-operators-and-expressions)
  + a small piece of code used to produce a value
  + within an expression, find values, variables, operators, and expressions
  + using parentheses to force the execution of the expression inside
  + parentheses used to indicate precedence
  + evaluate to four types: `numbers`, `strings`, `booleans`, and `objects`

+ [Operators](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-155-js-operators-and-expressions)
  + unary operator
    + applied to one expression
    + prefixed or suffixed
  + binary operator
    + applied to different expressions
    + both prefixed and suffixed
  + ternary  operator
    + `(condition) ? 'something' : 'others'`
    + example: `var kindergarten_eligible = (age < 5) ? "Too young" : socially_ready`

+ [Logical operators](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#221-boolean-values-and-logical-operators)
  + `&&` (AND): binary
  + `||` (OR): binary
  + `!` (NOT): unary, e.g., `!true // false`
  + implicit conversion
    + expression w/ logical operators
    + non-boolean value implicitly converted to boolean
  + lazy / short-circuit evaluation
    + `false &&`: always false, `&&` not tested
    + `true ||`: always true, `||` not tested
  + values evaluated as false: `false`, `undefined`, `null`, `0`, `NaN`, the empty string
  + everything else evaluated as true
  + `&&` and `||` evaluation rules
    + `A && B`: return A if A = false, otherwise return B
    + `A || B`: return A if A = true, otherwise return B

+ [Comparison operators](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#221-boolean-values-and-logical-operators)
  + Equal `==`
  + Not equal `!=`
  + Greater than `>`
  + Greater than or equal `>=`
  + Less than `<`
  + Less than or equal to `<=`
  + Strict equal `===`
  + Strict not equal `!==`

+ [Equal vs. strict equal](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#221-boolean-values-and-logical-operators)
  + Equal `==`: return true if strictly equal __w/ type conversion__
  + Strict equal `===`: return true if strictly equal __w/o type conversion__
  + triple-equals operator never doing type coercion
  + best practice: always use `===` or `!==` for comparisons

+ [Expressions](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#222-conditional-statements)
  + a statement closed w/ semicolon (`;`)
  + missing semicolon automatically inserted
  + readability: always recommended adding a semicolon at the end of all statements
  + flow of program
    + statement executed sequentially from top to bottom
    + modified by statements such as conditional statements or iteration statement
  + conditional statements: used to execute a unit of code only if a condition is evaluated as `true`
  + loop statement
    + used to run the block of code several times while a condition satisfied
    + [slowmoJS](https://toolness.github.io/slowmo-js/): online tool to check how the loop executed

+ [Block statement](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#222-conditional-statements)
  + a simple statement allowing to group a set of statements wrapped in curly braces`{` & `}`
  + used by other statements including if-statement or for-statement
  + example: 

    ```js
    {
        var i = 0; var result = false;
        console.log('i = ' + i);
    }
    ```


## Conditional Statements

+ [The `if` statement](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#222-conditional-statements)
  + syntax:
    + <code><span style="color: brown; font-weight: bold;">if</span> (Expr1) <span style="color: brown; font-weight: bold;">else</span> (Expr1)</code>
    + <code><span style="color: brown; font-weight: bold;">if</span> (Expr1)</code>
  + `Expr1` possibly including
    + logical operators: `&&`,. `||`, & `!`
    + comparison expressions: `==`, `===`, `>`, `>=`, `<`, `<=`
    + any values or expressions able to converted to boolean
  + curly brace
    + `Expr1` and `Expr2` possible block statements w/ curly braces
    + omitted curly braces allowed if only one statement in the block
    + strongly recommended enclosing if-statement in curly braces

+ [The if-then-else ternary operator](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#222-conditional-statements)
  + ternary operator:
    + using a syntax w/ "?" and ":"
    + statement: `(expr1) ? (expr2) : (expr3)`
  + a shortcut version of `if...then...else`
  + read as `if (expr1) then (expr2) else (expr3)`
  + short version not recommended except for very simple statement

+ [The switch statement](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#222-conditional-statements)
  + syntax:

    ```js
    switch (expression) {
        case value1:
            statement;
            break;
    
        case value2:
            statement;
            break;
        
        ...
    
        default:         // if no case tested true
            statement;
            break;
    }
    ```
  
  + the equality operator evaluated w/ `===`
  + all statements next to the `case` block executed sequentially until `break` keyword reached



## Loop statements

+ [`while` loop](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#223-loop-statements)
  + `while` statement
    + a block of code executed repeatedly while the specified condition satisfied
    + syntax: `while (condition) {statement}`
      + condition: a logical expression; true to execute the statement, otherwise exit
      + statement: probably a block statement
    + checking the condition first before executing the content
  + `do-while` statement
    + syntax: `do {statement} while (condition)`
    + executing the content of the loop once before checking the condition of the while
    + used for a block of code executed at least once
    + rarely used

+ [`for` loop](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#223-loop-statements)
  + `for` statement
    + adding an initialization expression and an incrementing expression to `while` or `do-while` statements
    + syntax: `for (initialization; condition; increment
  + `for-in` statement
    + used to iterate through an object
    + syntax: `for (variable in expression) statement`

+ [Loop interruption sattement](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#223-loop-statements)
  + `continue` statement
    + used to stop the execution of a block and starting the next iteration of the loop
    + syntax: `continue [label]`
    + label optional
  + `break` statement
    + used to stop an iteration, a switch or a labelled statement
    + syntax: `break [label]`



## Variables: Syntax

+ [Variables](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-151-js-variables-and-values)
  + used to "store values"
  + declaration
    + `var`: 'variable'; the only keyword to declare a variable before version 5 (2015)
    + `let` & `const`: allowed in subsequent versions (ES2015/ES2016 or JavaScript 6/7)
  + naming rules
    + first letter only "$", "_", "a" to "z", or "A" to "Z" allowed
    + other letters: "$", "_", "a" to "z", "A" to "Z", or "0" to "9"
    + case sensitive
    + reserved names: `boolean`, `if`, `delete`, `var`, `function`, etc.
  + assigning value
    + `=`: the assignment operator
    + given an id to a location somewhere in the memory of the computer
    + multiple variables allowed and saparated by ";", eg, `var myNumber1, myNumber2 = 34, myNumber3;`
  + using a variable never assigning a value: error message, eg, `Uncaught ReferenceError: k is not defined`
  + naming conventions
    + CamelCase notation preferred
    + 1st letter is lowercase and each 1st letter of each word is capitalized

+ [Constant](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-151-js-variables-and-values)
  + variables unable to be modified after set
  + naming convention: all uppercase letter w/ underscore
  + decalration
    + using `var` to declare w/ JavaScript 5 and w/o verification to modify it
    + recommended `const` after ES2015/ES2016 and raising error message if modifying

+ [Scope of JS variables](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-152-scope-of-js-variables)
  + `var` keyword in JavaScript 5 / ES5
    + declaring variable
    + scope
      + global scope for global variable
      + function scope for local variable within function
    + local variable within a function overrides a global variable w/ the same name
    + global scope / global variable
      + variable declared outside of a function
      + used anywhere in the code
    + local scope / local variable (function scope)
      + variable declared to be local to the function
      + override any global variable w/ the same name
      + local to the function
      + used anywhere inside the function
    + only declaring a variable w/ `var` keyword
      + possibly making stupid errors hard to detect
      + variable declared in function w/o the `var` keyword $\to$ global variable
    + best practice
      + always declaring a global or a local variable w/ `var`
      + using `let` if browser supporting JavaScript 6
  + `let` & `const` keywords since ES2015
    + `let` keyword to declare variables
    + `const` keywork to declare constants
    + scope
      + global scope for global variable
      + block scope for variable declared btw "{" and "}"
    + a local variable override other variables located in higher scopes
  + block variables
    + most programming languages applied
    + local variable within the block of instructions btw "{" and "}"
    + variable declared within "{" and "}"
  + highly recommended to use `let` and `const` instead of `var` for declaring variables and constants




## Data Types

+ [Types of data in JS](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-153-js-data-types)
  + primitive data types
    + __number:__ `1,2,105,3.14 ...`
    + __string:__ `'a', "one", 'two' , 'World Wide Web' ...`
    + __boolean:__ `true / false`
    + __undefined:__ absent or unknown value
    + __null:__ special keyword, meaning no value or empty
  + objects
    + everything not a "primitive data type"
    + a set of "predefined objects": arrays, functions, etc.
  + `null` still defined

+ [JavaScript data type](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-153-js-data-types)
  + weakly typed programming language
  + not declaring w/ the type of variable
  + `typeof` operator: showing the type of a variable depending on its value
  + possible values of `typeof` operator: `number`, `string`, `boolean`, `undefined`, `object`, or `function`




## Numbers

+ [Number values in JS](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-154-numbers)
  + __integer__: `1`, `23865`; not starting w/ `0` but `089 = 89`
  + __signed integer__: `-17`
  + __decimal__: `3.46`, `-466.877`
  + __scientific notation__: `3.46e4`, `5.3e+6`, `5344000e-5`
  + __octal__: `010 = 8`, `0456 = 4 * 8^2 + 5 * 8^1 + 6 * 8^0`; starting w/ `0` w/ all numbers `0` ~ `7`
  + __hexadecimal__: `0xF3`
  + special values
    + `+Infinity`
      + all number values greater than `1.79769313486231570e+308`
      + `1/0` $\to$ `Infinity`, `-1/0` $\to$ `-Infinity`
      + `typeof Infinity` $\to$ number
    + `-Infinity`: all number values smaller than `-1.79769313486231570e+308`, `-1/0`
    + `NaN` (Not a Number): `0/0`

+ [Precision of numbers](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-154-numbers)
  + a double-precision 64-bit format
    + total bits: 64
    + sign: 1 bit
    + exponent: 11 bits
    + significant: 52 bits
  + following IEEE 754 standard
  + each number represented as a float
  + an integer:
    + $2^{52}$ relevenat bits
    + biggest number: $2^{53}$
    + smallest number: $-2^{53}$
  + some arithmetic function only w/ 32-bit format

+ [Numeric operators](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-156-number-operators)
  + binary operators: `+`, `-` , `/`, `*`, `%`
  + unary operator
    + operators: `++`, `--`, `-` (opposite of a number, negative)
    + suffix `++`: adding one to the variable, then return the old value; eg, `x++`
    + prefix `++`: adding one tot he variable, then return the new value; eg, `+=x`
  + mixing assignment
    + binary operator used w/ a shorter syntax when assigning the resulting value to a variable
    + pre operators: `+=`, `-=`, `*=`, `/=`, `%=`


+ [Special values](../WebDev/Frontend-W3C/5-JavaScript/02b-Interact.md#221-boolean-values-and-logical-operators)
  + boolean values
    + two values: `true` and `false`
    + no quotation marks for these values
  + undefined
    + a variable not been assigned
    + part of the JS language
    + assigning a variable `undefined` allowed
    + `var foo;` and `var foo = undefined;`: equivalent but 1st recommended (shorter)
    + undeclared variable: `bar;`
      + accessing: raising `ReferenceError` msg
      + typeof operator: return `undefined`
  + `NaN` (Not-a-Number)
    + equal to nothing: `NaN == NaN; // false`, `NaN === NaN; // false`
    + checking w/ `isNaN(expr)`
      + examples: `isNaN(0/0); //true`, `isNaN(NaN); // true`, `isNaN(12); // false`
      + `X = NaN;` $\implies$ `X != X; // true`
    + possible ways to produce `NaN`
      + `(0/0) || 0` $\iff$ `NaN || 0` $\iff$ `false || 0`
      + `parseInt('foo');`: converting a String to a Number
      + `Math.sqrt(-1);`: returning `NaN`



## Strings

+ [Strings](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-157-strings-part-1)
  + text surrounded by single quote `'` or double quote `"`
  + no difference btw single quote and double quote
  + single and double quotes must be shown in pair
  + community preference: single quote for string
  + using double quote if text consisting at least a single quote

+ [String concatentation](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-158-string-operators)
  + concatenation operator: `+`
    + used to concatenate two strings
  + shorthand assignment operator `+=`
    + used to concatenate strings
  + method `concat()`: another way to concatentate strings

+ [String Number conversion](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-158-string-operators)
  + string number to number
    + String number in an arithmetic expression converted  to Number
  + converting number into a string: concatentate w/ an empty string at the beginning of expression

+ [Special characters](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-158-string-operators)
  + escaping special character: `\`
  + escaping the escape w/ double `\`: `\\`
  + special characters starting w/ `\`
    + `\n` for next line
    + `\r` for carriage return
    + `\t` for inserting a tabulation


+ [String as array](../WebDev/Frontend-W3C/5-JavaScript/03b-HTML5API.md#322-strings-are-arrays-of-characters)
  + "like" array of characters
    + behave like an array
    + w/ `length` property
    + able to access individual characters w/ indexes
  + limitations
    + unable to add elements to string using a non-existent index
    + unable to use `push/pop` methods for adding/removing characters at the end of string
    + unable to modify a character w/ an index
    + unable to remove a character w/ `splice` method

+ [String operation](../WebDev/Frontend-W3C/5-JavaScript/03b-HTML5API.md#322-strings-are-arrays-of-characters)
  + concatenation w/ `+` operator
    + prepend: `var s = 'Michel'; s = "Hello " + s; // "Hello Michel"`
    + append: `var s = 'Michel'; s += " Buffa"; // "Michel Buffa"`
  + removing substring w/ `substring()` method; e.g.,
    + removing last char (equivalent to `pop` method): `s = s.substring(0, s.length-1); // "Miche"`
    + removing a certain number of chars: `function removeChars(s, startIndex, numberOfCharsToRemove) { return s.substring(0, startIndex) + s.substring(startIndex + numberOfCharsToRemove); }` & `var s = 'Michel'; s = removeChars(s, 1, 3); console.log(s); // "Mel"`
  + replacing a char w/ index
    + `function replaceAt(s, index, character) { return s.substr(0, index) + character + s.substr(index+character.length); }`
    + `var s2 = "JavaScript"; s2 = replaceAt(s2, 1, "o"); console.log(s2); // "JovaScript"`
    + `s2 = replaceAt(s2, 0, "Coca"); console.log(s2); // Will display "CocaScript"`

+ [`str.substring()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring)
  + syntax: `str.substring(indexStart[, indexEnd])`
  + docstring: return the part of the string between the start and end indexes, or to the end of the string.
  + parameters
    + `indexStart`: the index of the first character to include in the returned substring
    + `indexEnd` (optional): the index of the first character to exclude from the returned substring
  + return: the part of the string between the start and end indexes, or to the end of the string



## Objects

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



## Arrays

+ [Arrays](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-1510-arrays-part-1)
  + definition: containers w/ indexes
  + declaration w/ `[]`
  + access using indexes
    + 1st element index: 0
    + accessing w/ `[#]` where `#` as the index
  + array length: `length` property
  + strings: arrays of characters
    + objects
    + w/ length property
    + using index to access individual character

+ [Elements in an array](../WebDev/Frontend-W3C/5-JavaScript/03b-HTML5API.md#321-arrays)
  + array: a collection of "things", including strings, integer values, decimal values, boolean values, or any objects
  + creating an array: putting elements btw "[" abd "]"
  + each element of an array w/ key/index and a value
  + type of an array: object
  + index beginning at "0"
  + properties and methods: `let a = [...];`
    + size of an array: `a.length`
    + sort an array: `a.sort([function_that_compares_two_elements]);`
      + numeric: return array object from lowest to highest
      + string: return array object w/ element alphabetically
      + object: depending on `function_that_compares_two_elements`
    + remove n elements starting from idx: `a.splice(idx, n);`; e.g., `a.splice(2, 1); // remove 1 elt starting from idx=2 (3rd elt)`
  + type of elements: different types of element allowed in an array; e.g., `let a = [1, 2, "three"]`

+ [Adding element](../WebDev/Frontend-W3C/5-JavaScript/03b-HTML5API.md#321-arrays)
  + using a new index
    + not to leave a hole in the array; e.g., `let a = [1, 2, 3]; a[4] = 4; a; // a = [1, 2, 3, undefined x 1, 4]`
    + example: `let a = [1, 2, 3]; a[3] = "four"; a[a.length] = "five"; // a = [1, 2, 3, "four", "five"]`
  + adding a new element at the end w/ `push()` method, e.g., `a.push("five"); // a = [..., "five"]`
  + recommendation: using `push()` method

+ [Removing element](../WebDev/Frontend-W3C/5-JavaScript/03b-HTML5API.md#321-arrays)
  + `splice()` method
    + syntax:
      + `array.splice(start)`
      + `array.splice(start, deleteCount)`
    + examples: `a = [1, 2, 3, "four", "five", "six", undefined × 1, "height"];`
      + remove element at 6th index: `[undefined x 1]` & `a = [1, 2, 3, "four", "five", "six", "height"]`
      + remove the 1st three elements: `a.splice(0, 3); // [1, 2, 3]` & `a = ["four", "five", "six", "height"]`
      + remove the last element: `a.splice(a.length-1); // "height"` & `a = ["four", "five", "six"]`
  + `pop()` method
    + recommended method for removing the last element
    + example: `a = ["four", "five", "six"]`, `a.pop(); // "six"` & `a = ["four", "five"]`
  + `delete()` method
    + not good for removing an element from an array
    + example: `delete a[1]; // true` & `a = ["four", undefined × 1]`

+ [Arrays of arrays](../WebDev/Frontend-W3C/5-JavaScript/03b-HTML5API.md#321-arrays)
  + numerical array
    + a `n x m` matrix
    + examples
      + a matrix w/ 2 rows, 3 columns: `var a = [[1,2,3], [4,5,6]];`
      + accessing rows: `a[0]; // [1, 2, 3]` & `a[1]; // [4, 5, 6]`
      + element: `a[0][0]; // top left element` $\to$ 1; `a[0][1]; // second element, first line` $\to$ 2; `a[1][2]; // third element, second line` $\to$ 6
  + array w/ differnet types of arrays, e.g., `a[0] = [1, 2, 3, 4, 5]; a[1] = ['michel', 'henri', 'francois']; a; // [Array(5), Array(3)]`

+ [`array.push()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)
  + syntax: `arr.push([element1[, ...[, elementN]]])`
  + docstring: add one or more elements to the end of an array and return the new length of the array
  + parameters
    + `elementN`: the element(s) to add to the end of the array.
  + return: The `new` length property of the object upon which the method was called.

+ [`array.pop()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)
  + syntax: `arr.pop()`
  + docstring:
    + remove the __last__ element from an array and return that element
    + change the length of the array
  + return: the removed element from the array; `undefined` if the array is empty.

+ [`array.sort()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
  + syntax: `arr.sort([compareFunction])`
  + docstring:
    + sort the elements of an array in place and return the sorted array
    + default sort order: ascending, built upon converting the elements into strings, then comparing their sequences of UTF-16 code units values.
  + parameters
    + `compareFunction` (optional):
      + specify a function that defines the sort order.
      + omitted: the array elements are converted to strings, then sorted according to each character's Unicode code point value.
  + compare function

    ```js
    function compare(a, b) {
      if (a is less than b by some ordering criterion) {
        return -1;
      }
      if (a is greater than b by the ordering criterion) {
        return 1;
      }
      // a must be equal to b
      return 0;
    }
    ```

+ [`array.splice()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
  + syntax: `let arrDeletedItems = arr.splice(start[, deleteCount[, item1[, item2[, ...]]]])`
  + docstring: change the contents of an array by removing or replacing existing elements and/or adding new elements in place
  + parameters
    + `start`: the index at which to start changing the array
      + start &lt; array.length: `start` set to the length of the array. No element will be deleted but the method will behave as an adding function, adding as many element as item[n*] provided.
      + negative: begin that many elements from the end of the array (`-n` is the index of the nth last element)
      + array.length + start &lt; 0: begin from index `0`
    + `deleteCount` (optional)
      + an integer indicating the number of elements in the array to remove from start
      + omitted, or &ge; array.length - start: all the elements from start to the end of the array will be deleted
      + &le; 0: no elements removed
    + `item1, item2, ...` (optional):
      + the elements to be added to the array, beginning from start
      + not specifying any elements: only removing elements from the array
  + return:
    + an array containing the deleted elements
    + a one-element array if only one elemnet removed
    + an empty array if nothing removed


+ [Iteration of array](../WebDev/Frontend-W3C/5-JavaScript/03b-HTML5API.md#323-iterating-on-array-elements)
  + iterating w/ `forEach`
    + parameters of `forEach`
      + the current element of the array
      + (optional) the index of the current element in the array
      + (optional) the array itself
  + iterate using regular `for` loop
    + most common way to iterate over an array is to use a `for` loop from 0 to length-1
    + allowing element to be iterated step  other than 1 or broken in the middle w/ `break` instruction

+ [`array.forEach` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
  + syntax:

    ```js
    arr.forEach(callback(currentValue[, index[, array]]) {
      // execute something
    }[, thisArg]);
    ```
  
  + docstring: execute a provided function once for each array element
  + parameters
    + `callback`: function to execute on each element. It accepts between one and three arguments:
      + `currentValue`: The current element being processed in the array.
      + `index` (optional): The index of `currentValue` in the array.
      + `array` (optional): The array `forEach()` was called upon.
    + `thisArg` (optional): Value to use as `this` when executing `callback`.
  + return: `undefined`




## Functions

+ [JavaScript function](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-131-the-best-way-to-learn-javascript)
  + a piece of code defined somewhere else
  + accepting parameters to do something
  + function parameters: the data passed to the function

+ [Functions](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-1511-functions-part-1)
  + grouping code, providing name and accessing by calling the given name
  + always returning a value
    + explicitly, using the keyword `return` followed by the value
    + implicitly, returning value is `undefined`
  + declaring a function: `function sum() {...}`
  + calling a function: `var result = sum(1, 2);`, `console.log(result);` $\to$ `3`

+ [Function parameters](../WebDev/Frontend-W3C/5-JavaScript/01e-JSIntro.md#notes-for-1511-functions-part-1)
  + __arguments__
    + an array created automatically in each function
    + containing all the call parameters of the function
  + omitted during the call, JavaScript providing the value `undefined`
  + a various number of parameters

    ```js
    function f() {
      return arguments;
    }
    ...
    f();    // returns []
    ...
    f( 1, 2, 3, 4, true, 'Michel Buffa');
    // returns [1, 2, 3, 4, true, "Michel Buffa"]
    ```

+ [Functions](../WebDev/Frontend-W3C/5-JavaScript/02c-Interact.md#23-functions-part2-callbacks)
  + Syntax: two ways to declare function
    + standardard function declaration

      ```js
      function functionName(parameters) {
      // code to be executed
      }
      ```

    + using a function expression

      ```js
      var varName = function(parameters) {
        // code to be executed
      };
      ```

  + standard declaration
    + not an executable statement
    + w/o semicolon at the end of a function declaration
    + semicolon used to separate executable JS statements
  + function expression
    + used a variable to store a function expression
    + calling the functions using the variable name
    + adding a semicolon at the end as a JS instruction
    + giving a value to a variable
    + an anonymous function
      + a function w/o function name
      + representing a value able to be assigned to a variable
      + variable able to be used to execute the function
    + 1st class object: manipulated like any other object/value in JS

+ [Callback functions](../WebDev/Frontend-W3C/5-JavaScript/02c-Interact.md#23-functions-part2-callbacks)
  + functions: 1st class objects
    + used as an argument, a parameter to another function
    + executing the passed-in function or even returning it to be executed later
  + a function passed to another function and executed inside the function called
  + event listerners used callback functions



