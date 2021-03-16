# Module 4: Structuring data


## 4.5 Exercises - Module 4


### 4.5.1 Exercises (1-6)

1. Who am I? (or what am I?)

  ```js
  var darkVador = ['villain', 'half human half machine'];
  ```

    Is the `darkVador` variable (as defined above) a JavaScript object? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, the type of arrays in JavaScript is "object", arrays are objects.


2. I prefer to use a dot!

  ```js
  var michel = {
    job: 'Your teacher',
    title: 'Professor',
    employer: 'University of Côte d\'Azur, France'
  };
  ```

  Which or these will display the name of Michel's employer? (3 correct answers.)

  a. `console.log("Michel's employer: " + michel.employer);`<br>
  b. `console.log("Michel's employer: " + michel['employer']);`<br>
  c. `console.log("Michel's employer: " + michel[employer]);`<br>
  d. `console.log("Michel's employer: " + michel["employer"]);`<br>
  e. `console.log("Michel's employer: " + michel[2]);`<br>

  Ans: abd<br>
  Explanation: `michel.employer` works, michel with 'employer' between brackets or michel with "employer" between brackets will work too. All the other answers are not correct, and they will either raise an error (michel with employer without quotes around the index between brackets), or will have an undefined value (with index = 2).


3. He he..., now what do you propose?

  ```js
  var michel = {
    job: 'Your teacher',
    title: 'Professor',
    employer: 'University of Côte d\'Azur, France'
  };

  // We put the name of a property of michel in the variable p
  var p = 'job';

  // we call a function that will display the value of the property p of the object
  // passed as the first argument
  displayPropertyValue(michel, p);

  function displayPropertyValue(object, prop) {
      // What would you put below instead of XXX?
    console.log("Value of the property named" + prop + ": " + XXX);
  }
  ```

  In the above code, what would you put instead of XXX in the instruction located in the body of the function named displayPropertyValue?

  a. `object['prop']`<br>
  b. `object[prop]`<br>
  c. `object.prop`<br>

  Ans: b<br>
  Explanation: This is a classic case where the name of a property is in a variable. In this situation, it is necessary to use the syntax with brackets and the variable inside without quotes (otherwise, "prop", which is the name of the variable, will be used; whereas what we want here it to use the value of the prop variable).


4. Properties and methods

  ```js
  var medor = {
      name: 'Benji',
      bark: function(){
          alert('Ouarf, Ouarf!');
      }
  };
  ```

  In this object (described above), we have one property and one method. Please check what is true below?

  a. `name` is the property and `bark` is a property and a method<br>
  b. `name` is the method, `bark` is a property<br>

  Ans: a<br>
  Explanation: A property can also be a function, in which case it is called a method. `bark` is the method and `name` the property.


__Source code for the next 2 questions (5 and 6):__

<div><ol>
<li value="1">var pictures = [</li>
<li>&nbsp; {</li>
<li>&nbsp; &nbsp; "albumId": 1,</li>
<li>&nbsp; &nbsp; "id": 1,</li>
<li>&nbsp; &nbsp; author: {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; "name":"michel",</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; "job": "Professor"</li>
<li>&nbsp; &nbsp; },</li>
<li>&nbsp; &nbsp; "title": "Holidays in Roma",</li>
<li>&nbsp; &nbsp; "url": "https://placehold.it/600/92c952",</li>
<li>&nbsp; &nbsp; "thumbnailUrl": "https://placehold.it/150/92c952"</li>
<li>&nbsp; },</li>
<li>&nbsp; {</li>
<li>&nbsp; &nbsp; "albumId": 1,</li>
<li>&nbsp; &nbsp; "id": 2,</li>
<li>&nbsp; &nbsp; author: {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; "name":"Marie Claire",</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; "job": "Michel's Boss!"</li>
<li>&nbsp; &nbsp; },</li>
<li>&nbsp; &nbsp; "title": "Eating an ice cream at the Coliseum",</li>
<li>&nbsp; &nbsp; "url": "https://placehold.it/600/771796",</li>
<li>&nbsp; &nbsp; "thumbnailUrl": "https://placehold.it/150/771796"</li>
<li>&nbsp; }</li>
<li>];</li>
</ol></div>

5. Who took this picture?

  ```js
  console.log("Name of the author of the second picture: " + XXX);
  ```

  Enter below what you would put in the above console.log instruction instead of __XXX__ (you need to type the JavaScript code, not the string result. __If needed, use simple quotes and not double quotes as they confuse the quiz tool__):

  Ans: `pictures[1].author.name` or `pictures[1].author.name;` or `pictures[1].author['name']` or `pictures[1].author['name'];` or `pictures[1].author[ "name"]` or `pictures[1].author[ "name"];` or `pictures[1]['author']['name']` or `pictures[1]['author']['name'];` or `pictures[1]["author"]["name"]` or `pictures[1]["author"]["name"];` or `pictures[1]['author'].name` or `pictures[1]['author'].name;` or `pictures[1]["author"].name` or `pictures[1]["author"].name;`<br>
  Explanation: The second picture is at index 1, and `author` is an embedded object that has a property named `name`. The correct answer is "pictures followed by brackets with index 1 inside, followed by .author.name".


6. Give me its length!

  How would you print the number of characters of the first picture's title?

  a. `pictures[0].length.title`<br>
  b. `pictures[0].title.length`<br>
  c. `pictures[1].length`<br>
  d. `pictures[1].title.length`<br>

  Ans: b<br>
  Explanation: pictures is an array, and the first picture is at index 0. title is a property, and it's a string, and strings have a length property.



### 4.5.2 Exercises (7-12)

7. Is this my property?

  ```js
  var player = {
    x:10,
    y:10,
    
    move: function(xNew, yNew) {
      x = xNew;
      y = yNew;
    }
  }
  ```

  Will the execution of `player.move(10, 10);` change the values of the player's x and y properties? (Yes/No)

  Ans: No<br>
  Explanation: No, this code is incorrect. From a method such as `move`, we access the properties of an object using the "this" keyword. We should have written `this.x = xNew;` and `this.y = yNew;` instead of `x = xNew;` and `y = yNew;`.


8. I'll do it later...

  ```js
  var player = {};
  player.x = 10;
  player.y = 10;
  ```

  Is the above code valid? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, unlike other object-oriented languages, it is possible in JavaScript to add or remove properties after an object has been created. The above code is equivalent to:

    ```js
    var player = {
        x:10,
        y:10
    };
    ```


9. Make a lot of them!

  ```js
  function Person(name, age) {
      this.name = name;
      this.age = age;
      this.describe = function() {
          console.log("I'm " + this.name + ", my age is " + this.age);
      }
  }

  var p1 = new Person("Michel", 52);
  p1.describe();
  var p2 = new Person("Marie Claire", "unknown, a lady never gives its age");
  p2.describe();
  ```

  In the above code, Person is:

  a. A constructor function<br>
  b. A JavaScript 6/ES6 class<br>

  Ans: a<br>
  Explanation:
    + With JavaScript version 5 (and previous versions), you can define a pseudo-class template called "a constructor function". The syntax is the same as for creating a function, except that, by convention, its name is Capitalized. The first letter of the function name is in uppercase. It is a good way to know, when you read someone else's code, that this is not a regular function, but a constructor function. Its name is a noun, the name of the class of objects you are going to build. Example: Person, Vehicle, Enemy, Product, Circle, Ball, Player, Hero, etc.
    + You also build new objects using the `new` keyword.


10. Marie or John?

  ```js
  function Person(name, age) {
      this.name = name;
      this.age = age;
      this.describe = function() {
          console.log("I'm " + name + ", my age is " + this.age);
      }
  }

  var p1 = new Person("Michel", 52);
  var p2 = new Person("Marie-Claire", "unknown, a lady never gives her age");
  p1.name = "John";
  p1.age = 22;
  p2.describe();
  ```

  In the above code, what will be displayed in the devtool console?

  a. I'm John, my age is 22<br>
  b. I'm Marie-Claire, my age is unknown, a lady never gives her age<br>

  Ans: b<br>
  Explanation: p1 and p2 are two different objects, each with its own properties. Changing the name and age of p1 will have no effect on p2's name and age. The correct answer is "I'm Marie-Claire, my age is unknown, a lady never gives her age".


11. Please fix me!

  ```js
  class Hero {
      this.name = name; // property
      this.side = side; // property

      function speak() { // method, no more "function"
          return "<p>My name is " + this.name +
                ", I'm with the " + this.side + ".</p>";
      }
  }
  
  var darkVador = new Hero("Dark Vador", "empire");
  ```

  There are two errors in the code of the class Hero above. Indicate which ones in the list below: (2 correct answers.)

  a. There are no arguments passed to the `speak` method<br>
  b. The method speak should not be preceded by the keyword `function`<br>
  c. There is no `constructor`<br>
  d. There are missing parentheses after the name of the class with two arguments inside: `Hero(name, side)`<br>
  e. A method cannot return a value<br>

  Ans: bc<br>
  Explanation: A method in ES6 classes should not be declared with the keyword `function`. In order to set a value to the `name` and `side` properties, the Hero class should have a `constructor`.


12. How do you use me?

  ```js
  function getHero(name, side) {
      return { 
          name: name,
          side: side
      }
  }

  let luke = getHero("Luke", "Rebels");
  console.log("Luke's side is " + XXX);
  ```

  In the above code, what would you write instead of __XXX__, to display Luke's side on the devtool console?

  Ans: `luke.side`<br>
  Explanation: JavaScript objects can also be created by functions that return objects (factories), such as the `getHero` function in this example. The returned object has two properties: `name` and `side`, so, the correct answer is `luke.side`.


### 4.5.3 Exercises (13-18)

13. Order is important (part 1)

  ```js
  let x = sum(3, 5);

  function sum(x, y) {
      return (x + y);
  }
  ```

  The function `sum` is declared after we called it at the first line of the above code. Is this correct? Will it work? (Yes/No)

  Ans: Yes<br>
  Explanation: In JavaScript, you can call a function BEFORE it has been declared in your source code. This is called "hoisting": it's like if all function declarations were moved to the top before being executed. It works and it's correct.
  

14. Order is important (part 2)

  ```js
  var p = new Person(); 
  
  class Person {...}
  ```

  The class `Person` is declared after being used at the first line of the above code. Is this correct? Will it work? (Yes/No)

  Ans: No<br>
  Explanation:
    + Unlike functions, classes must be declared BEFORE using them.
    + An important difference between function declarations and class declarations is that function declarations are "hoisted" and class declarations are not. It means that you can call a function BEFORE it has been declared in your source code. This is not the case with ES6 classes!
    + You first need to declare your class and then access it, otherwise a line of code, such as the one shown in the example, will give a ReferenceError.
  

15. How do you call me?

  ```js
  function f(name, side) {
      return { 
          name: name.toUpperCase(),
          side: side.toLowerCase()
      }
  }
  let luke = f("Luke Skywalker", "Rebels");
  ```

  How do we call the above function?

  a. It's just a function that returns an object, nothing special<br>
  b. A factory<br>
  c. A builder<br>

  Ans: b<br>
  Explanation: Objects can also be created by functions that return objects, we call them "factories".
  

16. Show me that you read the course!

  When you create an ES6 class, which of these is true? (3 correct answers.)

  a. You declare methods using the keyword "function" followed by the name of the method<br>
  b. You must have a unique constructor method<br>
  c. You declare the class using the keyword "class" followed by the name of the Class<br>
  d. You must call the constructor explicitly in order to build objects instances of the Class<br>
  e. The constructor is called when you create objects using the "new" keyword followed by the name of the class<br>

  Ans: bce<br>
  Explanation:
    + A class is simply defined using the keyword "class" followed by the name of the class.
    + The unique constructor is defined using the "constructor" keyword followed by the parameters.
    + The constructor is executed when an object is created using the keyword "`new`". Example: `let h1 = new Hero('Ian Solo', 'rebels');` It calls `constructor(name, side)`.
    + A method is simply defined by its name followed by its parameters (we no more use the keyword "`function`").
  

17. Class property vs. instance property

  A class property defines a characteristic of the ES6 class itself, not of the objects instances of this class. Only one of the following is true, check it!

  a. Class properties are useless and should be avoided -- in the course we don't recommend to use them.<br>
  b. An ES6 class property should be declared after the class, using the name of the class followed by the . operator<br/>
  c. An ES6 class property can be used only in class methods, not in instance methods<br/>
  d. An ES6 class property is declared in the class, like any other properties, but we use the keyword "static" before declaring it<br/>

  Ans: b<br>
  Explanation:
    + Class properties should be defined after the class definition, and declared using the name of the class followed by the . operator and the name of the property.
    + Example: `Point.nbPointsCreated` in the example below. A best practice is to ALWAYS use them this way.
  

18. Class method vs. instance method

  A class method defines a behavior of the ES6 class itself, not of the objects' instances of this class. Only one of the following is true, check it!

  a. An ES6 class method can be called using the name of an instance followed by the . operator, followed by the name of the method<br>
  b. An ES6 class method is declared in the class, like any other method, but we use the keyword "static" before declaring it<br>
  c. An ES6 class method can work with class properties and with instance properties<br>

  Ans: b<br>
  Explanation:
    + The static keyword defines a static method for a class.
    + Static methods are called without instantiating their class and cannot be called through a class instance.
    + Consequence: do not use instance properties in their body!
    + Static methods are often used to create utility functions for an application (source: MDN).




