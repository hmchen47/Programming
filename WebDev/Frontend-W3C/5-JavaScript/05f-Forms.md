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








