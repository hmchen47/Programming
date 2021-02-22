# Module 2: Adding interactivity to HTML documents


## 2.7 Exercises - Module 2


### 2.7.1 Exercises (1-6)

1. Are we all equal?

  ```js
  var x = 2;
  var y = '2';

  console.log((x == y));
  console.log((x === y));
  ```

  In JavaScript we can make comparisons using `==` or `===`. What will the code above display in the devtool console when executed?

  a. `false` and on the next line `true`<br/>
  b. `true` and on the next line `false`<br/>
  c. `true` and on the next line `true`<br/>

  Ans: b<br/>
  Explanation: 
    + Equal (`==`), returns true if the operands are strictly equal with type conversion.
    + Strict equal (`===`) returns true if the operands are strictly equal with no type conversion.
    + The triple-equals operator never does type coercion. It returns true if both operands reference the same object, or in the case of value types, have the same value. So, with `==`, 2 and '2' are the same object, not with `===`.
    + The correct answer is `true`, then `false`.
    + WE RECOMMEND THAT YOU USE `===` when beginning coding in JavaScript, this will save you from making many errors.


2. And so...?

  ```js
  var a = 3;
  var b = 10;
  
  if ((a === 5) && (b === 6))  { 
      console.log('a is equal to 5 and b is equal to 6');
  }
  ```

  When will the expression `(b === 6)` be evaluated?

  a. never<br/>
  a. before `(a === 5)`<br/>
  a. after `(a === 5)`<br/>

  Ans: a<br/>
  Explanation: As a equals 3, the `(a === 5)` expression will be false. With the && binary operator, if the left part is false, then the right part is never evaluated. false && something (an expression) is evaluated to false, and the part to the right of the && operator is not tested.


3. Switch me!

  ```js
  var gear = '';
  var cloudColor = 'yellow';

  switch(cloudColor) {
      case 'yellow': gear += 'psychedelic swimmnig suit,';
      case 'black': gear += ' boots, '; break;
      case 'grey': gear += ' umbrella, ';
      case 'white': gear += ' jacket, ';
      default: gear += ' watch';
  }

  console.log('gear: ' + gear);
  ```

Check the gear that will be printed to the devtool console (2 correct answers.)

  a. psychedelic swimming suit<br/>
  b. boots<br/>
  c. umbrella<br/>
  d. jacket<br/>
  e. watch<br/>

  Ans: ab<br/>
  Explanation: `cloudColor` is yellow, so the first switch statement will be `true` and 'psychedelic swimming suit' will be added to the gear variable. `gear` will be of type string because of this value. The statement's block of instructions does not end with a `break;` so the next statement will not be tested and 'boots' will be added to the `gear` variable that has not the value 'psychedelic swimming suit, boots'.


4. Switch me again!

  ```js
  var score = 69;
  var message='';
  
  switch(score) {
    case (score === 69):
      message += 'Not bad!';
      break;
    case (100): 
        message += 'Great, perfect score!';
  }

  console.log(message);
  ```

  Will the message be assigned the value 'Not Bad!'? (No/Yes)

  Ans: No<br/>
  Explanation:
    + With the `switch` statement, if the value of an expression equals one of the cases (the equality operator evaluated is `===`), all the statements next to this case block are executed sequentially until the keyword `break` is reached.
    + Look at the first case: the (`score === 69`) expression will be evaluated to `true`. Then the test (`score === true`) will be performed. And it will be `false` (as score has the value 69), then the block of instruction that assign 'Not Bad!' to message will NEVER be executed.


5. This is false!

  ```js
  var x = ...;

  if(x) { console.log("Evaluated as true!!!"); }
  ```

  When tested, which of these values for x will be evaluated as true? (3 correct answers.)

  a. `""` (empty string)<br/>
  b. `"Hello"`<br/>
  c. `undefined`<br/>
  d. `"false"`<br/>
  e. `1`<br/>
  f. `0`<br/>
  g. `NaN`<br/>

  Ans: bde<br/>
  Explanation: The following values will evaluate to `false`: `false`, `undefined`, `null`, `0`, `NaN`, `""` (empty string). All the rest, including the string "false" will be evaluated as `true`.


6. Choose the right x

  ```js
  function choose(x, m1, m2) {
    return x <= m1 ? m1 : x >= m2 ? m2 : x; 
  }
  var result1 = choose(5, 10, 40);
  console.log("result1 = " + result1);

  var result2 = choose(20, 10, 40);
  console.log("result2 = " + result2);

  var result3 = choose(70, 10, 40);
  console.log("result3 = " + result3);
  ```

  What will be the values of the variables result1, result2 and result3 after the execution of the above code?

  a. 10, 20 and 40<br/>
  b. 10, 20 and 70<br/>
  c. 5, 10 and 20<br/>

  Ans: a<br/>
  Explanation: The `choose` function returns the first parameter if it's >= m1 and <= m2. It returns m1 if x < m1, and it returns m2 if x > m2.


### 2.7.2 Exercises (7-9)

7. While loop...

  ```js
  var i = 1, j = 2;
  
  while ( i < 4 ) {
      j += 2;
      i += 1; 
  }
  console.log("i = " + i);
  console.log("j = " + j);
  ```

  After the while loop, what are the values of `i` and `j`?

  a. `i = 3` and `j = 5`<br/>
  b. `i = 4` and `j = 8`<br/>
  c. `i = 5` and `j = 10`<br/>

  Ans: b<br/>
  Explanation:
    + `i` starts with value 1. The while loop will be executed for `i = 1`, `i = 2`, `i = 3`. Then, during the third loop, `i` is incremented once more and becomes equal to 4. The condition (`i < 4`) becomes false and we continue after the loop block of instructions. `i = 4` at the end.
    + `j` starts with value 2, the loop is executed three times and each time 2 is added to `j`. Final value is `2 + (3 x 2) = 8`.


8. Do this question while you have time...

  ```js
  var i = 10;
  
  do {
    i+=2;
    console.log(i + " ");
  } while(i < 20);
  ```

  What will be printed to the devtool console?

  a. 10 14 18, each one on a different line<br/>
  b. 12 14 16 18, 20, each one on a different line<br/>
  c. 12 14 16 18, each one on a different line<br/>

  Ans: <span style="color: brown;">b</span>, xc<br/>
  Explanation:
    + `i` has value 10. The block of instruction in the 'do... while' is first executed before testing the condition. 2 is added to `i`. `i` has value 12 before the first call to `console.log`, then the loop is done again. Each time, we add 2 BEFORE testing the condition. So `i` will be equal to 12, 12, 16, 18.
    + Then it's incremented and it will be equal to 20. That will be displayed in the devtool console by console.log, then the condition (`i < 20`) is `false` (as `i = 20`), and we exit the loop. So... the correct answer is: 12 14 16 18, 20, each one on a different line


9. Give these property names!

  ```js
  var rect1 = {       // rect1 is an object
      x:10,
      y: 12,
      width: 50,
      height: 100
  }
  
  for(var property XXX rect1) {
      console.log(property);
  }
  ```

  What would you put instead of XXX in the above code, so that it will print the property names of the object rect1?

  Ans: `in`<br/>
  Explanation: The `for-in` statement is used to iterate through an object. The correct answer is 'in'.


### 2.7.3 Exercises (10-15)


10. Click me

  ```js
  function processClick(event) {
    console.log("Button clicked!");
  }
  ```

  Which of these syntaxes is ok for detecting a click on an HTML button?

  a. `<button id="myButton" click="processClick(event);">Click me!</button>`<br/>
  b. `<button id="myButton" onclick="processClick(event);">Click me!</button>`<br/>
  c. `<button id="myButton" onClick="processClick(event);">Click me!</button>`<br/>

  Ans: b<br/>
  Explanation: When using the "on" syntax for declaring event listeners as attributes of an HTML element, the correct syntax is to use "on" followed by the name of the event, in lowercase. The correct syntax is the one that uses `onclick="processClick(event);"`.


11. Click anywhere?

  ```js
  addEventListener('click', function(evt) {
      document.body.innerHTML += 'Clicked!';
  });
  ```

  The above code:

  a. Adds a click event listener to the whole document (any click on the page will trigger the event)<br>
  b. Adds a click event listener only to HTML buttons<br>

  Ans: a<br/>
  Explanation: This code registers an event listener that listens to "click" events on any part of the window (clicks anywhere on a Web document will be processed by this event handler).


Source code for the next question (12)

```html
...
<head>
...
</head>
<body>
   <button id="myButton">Click me!</button>
<script>
   var b = document.querySelector("#myButton");
   b.addEventListener('click', function(evt) {
      alert("Button clicked");
   });
</script>
</body>
```

12. Alert me!

  The above code will display an HTML page with an HTML button. What will happen when a user clicks on the button?

  a. It will display an alert dialog with the text "Button clicked"<br/>
  b. It will not work<br/>

  Ans: a


Source code for the next question (13)

```html
...
<head>
   <script>
       var b = document.querySelector("#myButton");
       b.addEventListener('click', function(evt) {
          alert("Button clicked");
       });
   </script>
</head>
<body>
   <button id="myButton">Click me!</button>
</body>
```

13. Try to click me!

  The above code will display an HTML page with an HTML button. What will happen when a user clicks on the button?

  a. It will do nothing, and there will be an error in the devtool console<br/>
  b. It will display an alert dialog with the text "Button Clicked"<br/>

  Ans: a<br/>
  Explanation: When the `querySelector` call is performed (line 4), the button has not yet been created in the DOM. The value of `b` will be `undefined`, and the execution of line 5 will give an error. It will not work.


Source code for the next question (14)


```html
...
<head>
   <script>
       function init() {
           var b = document.querySelector("#myButton");
           b.addEventListener('click', function(evt) {
              alert("Button clicked");
           });
       }
   </script>
</head>
<body onload="init();">
   <button id="myButton">Click me!</button>
</body>
```

14. Click me example, third variant!

  The above code will display an HTML page with an HTML button. What will happen when a user clicks on the button?

  a. It will display an alert dialog with the text "Button Clicked"<br/>
  b. It will do nothing, and there will be an error in the devtool console<br/>

  Ans: a<br/>
  Explanation: Because of the `<body onload="init();">`, the init function will be executed after the DOM is ready, after the button has been added to the DOM. It will work and display an alert dialog.


15. Who made this?

  ```js
  function processClick(evt) {
      alert("Button clicked!");
  }
  ```

  Each event listener callback function gets an event object as a parameter. We can use one property of the event object to get the HTML element that emitted the event. Which property is it?

  a. `evt.target`<br/>
  b. `evt.element`<br/>
  c. `evt.source`<br/>

  Ans: a<br/>
  Explanation: `evt.target` is the correct answer: its value is the HTML element that has fired the event. For example, with a click listener on a button, `evt.target` in the event listener is the button itself.



### 2.7.4 Exercises (16-19)


16. Did you get the key?

  ```js
  window.onkeydown = function(evt) {
    console.log("key = " + evt.XXX);
  }
  ```

  What would you write in the above code to get the key that has been pressed (for ex., if you press 'e' you want "key = e" to be printed by the console.log)??

  a. `code`<br>
  b. `key`<br>
  c. `keyCode`<br>

  Ans: b<br>
  Explanation: The correct answer is "key": when the pressed key is a printable character, you get the character in string form. When the pressed key is not a printable character (for example: Backspace, Control, but also Enter or Tab, which actually are printable characters), you get a multi-character descriptive string, like 'Backspace', 'Control', 'Enter', 'Tab'.


17. Make my game playable in all countries

  Reference keyboard:

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick="window.open('https://tinyurl.com/2uaxt6lc')"
      src    ="https://tinyurl.com/559zrbmn"
      alt    ="the reference keyboard from:https://www.w3.org/TR/uievents-code/#writing-system-keys"
      title  ="the reference keyboard from:https://www.w3.org/TR/uievents-code/#writing-system-keys"
    />
  </figure>

  What is the reference keyboard we talked about in the course, (also shown above), when we are speaking about key events?

  a. It's a reference layout that does not depend on your physical keyboard layout. The `keyCode` property of the key event object will have the value displayed on the keys of this keyboard which does not depend on your physical layout.<br>
  b. It's the reference keyboard only for the QWERTY keyboard layout.<br>

  Ans: a<br>
  Explanation: This reference keyboard does not depend on the layouts used in different countries. If you write a video game and want to use the zqsd or wasd keys, this will depend on the keyboard layout. If you use `keyCode`, then you may assume that in every layout, it will correspond to the same physical position of the keys on the keyboard.


18. Many buttons...

  ```js
  window.onmousedown = function(evt) {
    document.body.innerHTML += "button = " + evt.XXX + "<br>";

  }
  ```

  What is the property name for getting the mouse button number (e.g., what would you write instead of XXX in the above code)?

  a. `code`<br>
  b. `button`<br>
  c. `mouse.button`<br>

  Ans: b<br>
  Explanation: `evt.button` indicates which mouse button was pressed when the mouse event has been triggered.


19. Not mouse events

  Which of these are NOT mouse events? (3 correct answers.)

  a. `click`<br>
  b. `mouseclick`<br>
  c. `doubleclick`<br>
  d. `mouseup`<br>
  e. `mousemotion`<br>
  f. `mousedown`<br>

  Ans: bce<br>
  Explanation: `mouseclick`, `doubleclick` and `mousemotion` are not valid mouse event names. The correct ones are `click`, `dblclick` and `mousemove`.


