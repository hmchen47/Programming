# Module 5: Working with forms


## 5.6 Final exam


### 5.6.1 Exercises (1-6)

1. John or Michel?

  ```js
  let p1 = {
      name:'Michel',
      age: 52
  };

  let p2 = p1;
  p2.name = 'John';
  console.log('p1.name = ' + p1.name);
  ```

  What will be the value of `p1.name`?

  a. John<br>
  b. Michel<br>


  Ans: a<br>
  Explanation: `p1` and `p2` reference the same object. When we modify `p2.name`, it also modifies `p1.name`.


2. Don't make me older please!

  ```js
  var p1 = { 
      name:'Michel', 
      age:52
  }

  function tryToMakeOlder(a, b) {
      a.age += b;
  }

  tryToMakeOlder(p1, 3);
  console.log("New age of p1: " + p1.age);
  ```

  What will be the value of `p1.age`?

  a. 55<br>
  b. 52<br>


  Ans: a<br>
  Explanation: The first argument to the call `tryToMakeOlder(p1, 3);` is an object, so we pass its reference as a parameter to the `tryToMakeOlder` function. The a parameter of this function gets this reference and points to the same object as `p1`. Consequently, modifying the value of `a.age` is equivalent to modifying the value of `p1.age`. The final result is 55.


3. Original value?

  ```js
  let obj1 = { 
    x: 2 
  };

  function add(a, b) {
      var originalValue = a.x;
      
      return {
          x: originalValue + b
      }
  };
  let obj2 = add(obj1, 3);
  ```

  What will be the value of `obj2.x` and `obj1.x` after the execution of the above code?

  a. `obj1.x = 2` and `obj2.x = 2`<br>
  b. `obj1.x = 2` and `obj2.x = 5`<br>
  c. `obj1.x = 5` and `obj2.x = 5`<br>


  Ans: b<br>
  Explanation:
    + The function add is a factory function that returns an object. It does not modify the original object referenced by its a parameter.
    + `obj2` gets the returned value that is an object with a property `x` which takes the original value of `a.x` (equivalent to `obj1.x`) + 3 (the value of the `b` parameter).


4. Are we the same?

  ```js
  let obj1 = {
      x: 2
  }

  let obj2 = {
      x: 2
  }
  ```

  The expression `(obj1 === obj2)` will be evaluated to: (true/false)


  Ans: false<br>
  Explanation: The two objects have the same value for their `x` property, but they are different objects that reference two distinct objects in memory. The `===` operator tests if the references are the same, not if all the property values are the same. The expression will be evaluated to false.


5. Are we the same object (oh no, again?)

```js
// obj1 and obj2 are global variables
var obj1 = {
    x: 2
}

let obj2 = {
    x: 2
}
```

  Which of these is true?

  a. obj1 and window.obj1 are the same objects<br>
  b. obj2 and window.obj2 are the same objects<br>


  Ans: a<br>
  Explanation:
    + The “global variables” defined with the keyword `var` are properties of this `window` object, and we can say the same for predefined functions like prompt, alert, etc.
    + However, at the top level of programs and functions, `let`, unlike var, does not create a property on the global window object.
    + So, obj1 and window.obj1 are the same objects, this not true with obj2.


6. Put a string on please!

  ```js
  var t = [1, 2, 3];
  ```

  `console.log("t = " + t)` is equivalent to:

  a. `console.log("t = " + t.toString());`<br>
  b. `console.log("t = " + t.join(' '));`<br>


  Ans: a<br>
  Explanation: `toString()` in JavaScript is rather similar to the `Object.toString()` method we find in the Java programming language: when we try to "display" an object, it is transformed into a string by calling `toString()` implicitly. In `console.log("t = " + t);`, the expression `"t = " + t` forces the t after the `+` to be converted to a string, as the left part of the `+` is a string.


### 5.6.2 Exercises (7-14)

7. Why do you want me to become bigger?

  ```js
  let days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
  ```

  What will the execution of `days.length = 7;` do?

  a. Make an error, the length is fixed and equal to the number of elements in the array. It changes only when we add or remove elements to the array.<br>
  b. Add two extra elements to the array, with an undefined value.<br>
  c. Add two extra elements to the array, with a value of zero (the number 0).<br>

  Ans: a<br>
  Explanation: If you give to the length property a value bigger than the number of elements in an array, it adds `undefined` elements to it.


8. Hybrid arrays are awful, believe me!

  ```js
  let days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

  days.description = 'days of the week';

  console.log("Description of the array:" + days.description + 
    ", its length is equal to " + days.length);
  ```

  What will the execution of the above code display to the devtool console?

  a. It raises an error because an array is not an object<br>
  b. Description of the array:days of the week, its length is equal to 5<br>
  c. Description of the array:days of the week, its length is equal to 6<br>

  Ans: b<br>
  Explanation: An array is an object, you can add a property to it. But the `length` property takes into account only elements that have a numerical index. Correct answer is "Description of the array:days of the week, its length is equal to 5".


9. I'll take another slice, please!

  Which one of these methods modifies an array?

  a. The `splice` method<br>
  b. The `slice` method<br>

  Ans: a<br>
  Explanation: `slice`: returns a sub-array without modifying the original array. While `splice`: modifies the array, it removes “a slice” and it also adds new elements.



10. Give me a week-end!

  ```js
  let days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

  let weekEnd =  days.slice(XXX, YYY);
  ```

  What would you put instead of XXX and YYY in the call to `days.slice(XXX, YYY)` in order to get the weekend days (Saturday and Sunday)?

  a. `let weekEnd = days.slice(days.length-2, days.length);`<br>
  b. `let weekEnd = days.slice(6, 7);`<br>
  c. `let weekEnd = days.slice(5, 6);`<br>
  d. `let weekEnd = days.slice(7, 8);`<br>

  Ans: a<br>
  Explanation: `slice(begin, end)` returns the elements at index begin, begin + 1, begin+2 etc. until end __NOT INCLUDED__. The array `days` has 7 elements in it, `days.length` is equal to 7. So, in order to get the last two elements (at indexes 5 and 6), we should call `days.slice(5, 7)`. This corresponds to the answer: `days.slice(days.length-2, days.length);`


11. I don't want to work these days anymore!

  ```js
  let days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

  let weekEnd =  days.splice(1, 3);
  ```

  What will be the content of the array `days` after the execution of the above code?

  a. `days` is not modified.
  b. `['Monday', 'Friday', 'Saturday', 'Sunday']`<br>
  c. `['Thursday', 'Friday', 'Saturday', 'Sunday']`<br>
  d. `['Monday', 'Thursday', 'Friday', 'Saturday', 'Sunday']`<br>

  Ans: c<br>
  Explanation: The `splice(begin, nb)` method will remove `nb` elements starting from index equal to `begin`.


12. Two decimals only

  ```js
  let x = Math.PI/2;

  console.log("x= " + x.XXX); // expected 1.57, do not use Math. something here.
  ```

  What method and parameter value would you use to display the value of x with only 2 decimals? We want "x = 1.57" to be displayed in the devtool console. Type exactly what you would write instead of XXX in the code above.

  Ans: `toFixed(2)`<br>
  Explanation:
    + `toFixed`: sets the number of digits for the decimal part of a number. The correct answer is "`toFixed(2)`" where 2 is the number of decimals.
    + There is also another method, named `toPrecision`, that has a very similar behavior, and can also return numbers in scientific notation. However, this one would round the result to 1.6 if called with `toPrecision(2)`, as the argument is the total number of numbers in the result, we should call it with `toPrecision(3)` in order to get 2 decimals.
    + A correct answer to this exercise is `toPrecision(3)` or `toFixed(2)`.


13. Do I like my students?

  ```js
  let s = "Hello my dear students!";

  s[9] = "terrible";

  console.log(s);
  ```

  What will be printed in the devtool console?

  a. Hello my dear students!<br>
  b. Hello my terrible students!<br>

  Ans: a<br>
  Explanation: In JavaScript, like in any programming language, strings are not directly modifiable. In this example, s remains unchanged, it's not possible to change the content of a string using the bracket notation.


14. Change me this string!

  ```js
  let s = "Hello my friends!";
  ```

  Which of these will modify the string referenced by `s` after their execution? (2 correct answers!)

  a. `s.slice(11, 16);`<br>
  b. `s.substring(11, 16);`<br>
  c. `s += " I miss you";`<br>
  d. `s.split(' ').join('---');`<br>
  e. `s = s.slice(11, 16);`<br>

  Ans: ce<br>
  Explanation:
    + `s.slice` alone does not change the string, as well as split and join. The only answers that change `s` are the ones that start with "`s = s + ...`" or "`s +=...`".
    + Correct answers are `s += " I miss you";` and `s = s.slice(11, 16);`


### 5.6.3 Exercise (15-22)

15. Give me some maths now!

  ```js
  var x = new Math();

  console.log("Random number: " + x.random());
  ```

  What will the above code do?

  a. It does nothing - the Math class cannot be used to create instances with "new"<br>
  b. It displays a random number between 0 and 100<br>
  c. It displays a random number between 0 and 1<br>

  Ans: <span style="color: brown;">a</span>, c<br>
  Explanation: 


16. Please stop, I have a headache!

  ```js
  var x = 5*Math.round(Math.random());

  console.log("Random number: " + x);
  ```

  What will the above code do?

  a. Display a random number equal to 0, 1, 2, 3, 4 or 5<br>
  b. Display a random number equal to 0 or equal to 5<br>
  c. Display a random number between 0 and 5<br>

  Ans: b<br>
  Explanation: Indeed, `Math.random()` returns a random value between 0 and 1. If `Math.random()` returns a value above 0.5, `Math.round` of this value will return 1. If the returned value is below 0.5, `Math.round` will return 0. As we multiply this result by 5 before putting it into the variable x, then the above code will give either a value of 0 or a value of 5.



17. What day are we?

  ```js
  var date = new Date();
  ```

  A call to new Date() returns...

  a. The current date as an object<br>
  b. The current date as a string<br>

  Ans: a<br>
  Explanation: The returned value is actually an object, that has multiple methods such as `getMonth()`, `getDay()`, `getFullYear()`, etc.


18. Add a new row

  ```js
  let myTable = document.createElement("table");

  let row = myTable.XXX;
  row.innerHTML = "<td>Michel</td><td>Buffa</td>";
  ```

  Instead of XXX in the above code, what method would you call for adding a row at the end of the table object myTable?

  a. `addRow()`<br>
  b. `insertRow()`<br>
  c. `createElement("tr");`<br>

  Ans: b<br>
  Explanation: The HTML5 table JavaScript API has an `insertRow` method that can be used on Table objects such as the one returned by a call to `document.createElement("table");`. Without arguments, it adds a row at the end of the table.


19. Submission going down, down, dragging me down...

  ```html
  <form onXXX=" return submitted();">
    // here labels, input fields, etc.
    
    <button>Submit</button>
  </form>

  <script>
      function submitted(evt) {
        // get input fields values, etc
        
        // return false = do not submit the form
        // return true = let the browser submit the form and reload the page
        return false;
    }
  </script>
  ```

  What event name would you put instead of XXX at the line 1 of this code, in order to make the callback function `submitted` called when the form is submitted (by clicking on the HTML button at the end of the form)?

  a. `keydown`<br>
  b. `submit`<br>
  c. `click`<br>

  Ans: <span style="color: brown;">b</span>, xc<br>
  Explanation:
    + As shown in the contact manager example, we can call a callback function when an HTML form is submitted using the '`submit`' event.
    + We should have `onsubmit="return submitted();"` at the first line of this code.


20. Local Storage does not like objects...

  ```js
  let p1 = {
    name:'Michel',
    email: 'michel@w3cxgreatmoocmakers.com'
  }

  // Save to Local Storage in JSON

  let a = XXX;
  localStorage.michel = a;
  ```

  What would you put instead of XXX in the above code?

  a. `JSON.stringify(p1);`<br>
  b. `JSON.parse(p1);`<br>
  c. `p1;`<br>

  Ans: a<br>
  Explanation: In Local Storage, only pairs of key/values, where values are strings, can be stored. As `p1` is an object, not a string, we must transform `p1` into a string using the JSON format. To do this we need to call `JSON.stringify(p1);`


21. In and out

  Let's suppose that the object `p1` from the previous question has been saved in JSON in the local storage of your browser, with the key "michel". How do you restore it as a JavaScript object?

  a. `p1 = JSON.stringify(localStorage.michel);`<br>
  b. `p1 = JSON.parse(localStorage.michel);`<br>
  c. `p1 = localStorage.michel`<br>

  Ans: b<br>
  Explanation: `localStorage.michel` is an object in the JSON notation. To turn it back into an object, you must use `JSON.parse`. The correct answer is: `p1 = JSON.parse(localStorage.michel);`


22. Xhr2 and fetch

  `Xhr2` and fetch are standard JavaScript APIs. What are they useful for?

  a. They can send asynchronous HTTP requests to retrieve remote data, often in JSON format<br>
  b. They allow you to control a remote HTTP server<br>
  c. They allow to manipulate data saved locally by the browser<br>

  Ans: a<br>
  Explanation: They can send asynchronous HTTP requests to retrieve remote data, often in JSON format. Asynchronous means that a request may take some time to complete, and that the answer will arrive after a given amount of time. This is why, with Xhr2, we need an `xhr.onload = function(evt) {...}` callback that will be called by the browser when the response arrives. With fetch, we do `fetch(url) ... then....` and while we're waiting for the response to arrive, the browser can do other things. When the response comes in, we execute the `then(...)` method.


### 5.6.4 Exercises (23-28)

23. Strings or numbers?

  ```js
  let x = "10";
  let y = 2;

  let z = x * y;
  ```

The value of `z` is:

  a. `"20"` (as a string)
  b. `20`
  c. `NaN`

  Ans: <br>
  Explanation: 


24. Are we the same?

In JavaScript, are classes and types the same thing? (Yes/No)

  Ans: <br>
  Explanation: 


25. Which scope for me?

  Which variables have a function scope?

  a. The ones declared in a function, with the keyword var<br>
  b. The ones declared in a function, with the keyword let<br>

  Ans: <br>
  Explanation: 


26. Parameters and arguments

  Can we pass a variable number of arguments to a function? (Yes/No)

  Ans: <br>
  Explanation: 


27. Let's play with indexes!

  ```js
  let a = [ 'michel', 'buffa', [5+6, 'buffa'] ];
  ```

  How is this expression evaluated: `(a[1] === a[2, 1])`?

  a. It is evaluated to `true`<br>
  b. It is evaluated to `false`<br>

  Ans: <br>
  Explanation: 


28. Not old yet

  ```js
  var myAge = 52;

  if ((myAge >= 0 && myAge < 3) ||  (myAge > 90)) {
    console.log("WOW!");
  } else {
    console.log("Ah...");
  }
  ```

  What will be printed by the above code?

  a. Ah...<br>
  b. WOW!<br>

  Ans: <br>
  Explanation: 




