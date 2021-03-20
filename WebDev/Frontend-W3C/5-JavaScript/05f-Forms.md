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


  Ans: <br>
  Explanation: 


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


  Ans: <br>
  Explanation: 


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


  Ans: <br>
  Explanation: 


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


  Ans: <br>
  Explanation: 


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


  Ans: <br>
  Explanation: 


6. Put a string on please!

  ```js
  var t = [1, 2, 3];
  ```

  `console.log("t = " + t)` is equivalent to:

  a. `console.log("t = " + t.toString());`<br>
  b. `console.log("t = " + t.join(' '));`<br>


  Ans: <br>
  Explanation: 






