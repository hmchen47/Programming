# Module 3: Playing with HTML5 APIs
 
## 3.2 Arrays (part 2): iterators

### 3.2.1 Arrays

<a href="https://edx-video.net/W3CJSIXX2016-V003200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/2oemwc87)

<span style="color: brown; font-style: bold;">ERRATA in the above video:</span>

+ In the part that explains the splice method for removing element, I say "splice(0, 1) removed the element that was in the middle". This is a mistake, as it removes the FIRST element, the one that was at index 0. It is not the element that was "in the middle", as I say in the video (the element was in the middle of the array before we sorted it).

__Source code of the example in the video:__

The example shown in the video is available at CodePen

[CodePen Demo](https://codepen.io/w3devcampus/pen/owgeyJ)

[Local Demo](src/ls/03b-example01.js)


#### JavaScript arrays

In JavaScript, arrays represent a collection of "things", which may be strings, integer values, decimal values, boolean values, or any sort of JavaScript object.

<div><ol>
<li" value="1">&gt; var myarr = ['red', 'blue', 'yellow', 'purple'];</li>
<li">undefined</li>
<li">&nbsp;</li>
<li">&gt; myarr;</li>
<li">["red", "blue", "yellow", "purple"]</li>
<li">&nbsp;</li>
<li">&gt; myarr[0];</li>
<li">"red"</li>
<li">&nbsp;</li>
<li">&gt; myarr[3];</li>
<li"> "purple"</li>
<li">"purple"</li>
</ol></div>


Each element of an array has a key/index and a value. Here are the keys/indexes and values from the above example:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/19asezfy')"
    src    ="https://tinyurl.com/1ggh319d"
    alt    ="Table with key and values of the previous array example"
    title  ="Table with key and values of the previous array example"
  />
</figure>

Below is an another example with an array containing three integers. The first element is at index 0, and the last at the index equal to the number of elements-1.

<div><ol>
<li" value="1">&gt;&nbsp;var a = [];</li>
<li">&gt;&nbsp;typeof a;</li>
<li"> "object"</li>
<li">&gt;&nbsp;var a = [1,2,3];</li>
<li">&gt;&nbsp;a</li>
<li"> [1, 2, 3]</li>
<li">&gt;&nbsp;a[0]</li>
<li"> 1</li>
<li">&gt;&nbsp;a[1]</li>
<li"> 2</li>
</ol></div>

##### Properties and methods of array objects

JavaScript arrays are objects and have some useful properties and methods

Note that in JavaScript, arrays are "objects" (_lines 2-3_ in the above example), which means that they have properties and methods. You can access/call them using the "." operator. Here are the most common properties and methods.

<div><ol>
<li" value="1">&gt; var a = [1, 3, 2, 5, 7];</li>
<li">undefined</li>
<li">&nbsp;</li>
<li">&gt;<strong> a.length;</strong> // number of elements</li>
<li">5</li>
<li">&nbsp;</li>
<li">&gt;<strong> a.sort();</strong> // sorts element in a</li>
<li">[1, 2, 3, 5, 7]</li>
<li">&nbsp;</li>
<li">&gt;<strong> a.splice(2, 1);</strong> // remove 1 element starting from index=2 (3rd element)</li>
<li">[3]</li>
<li">&nbsp;</li>
<li">&gt; a; // the '3' has been removed from the array</li>
<li">[1, 2, 5, 7]</li>
</ol></div>

By default, the `sort()` method sorts elements alphabetically if they are strings, or from lowest to highest if they are numeric. If you want to sort objects like `{firstName:'michel', lastName:'Buffa', age:51}`, you will need to use another method passed as an argument to the sort method, for example to indicate the property you want to use for sorting (i.e., sort by age);

Example with an array of persons (each person is an object):

<div><ol>
<li" value="1">var persons = [ </li>
<li">&nbsp; &nbsp; {givenName: 'Michel',&nbsp;familyName: 'Buffa', age:51},</li>
<li">&nbsp; &nbsp; {<span style="color: #000000;">given<span style="color: #000000;">Name: 'Pig',&nbsp;<span style="color: #000000;">family<span style="background-color: #eeeeee;">Name: 'Bodine', age:20},</li>
<li">&nbsp; &nbsp; {<span style="color: #000000;">given<span style="background-color: #ffffff;">Name: 'Pirate',&nbsp;<span style="color: #000000;">familyName: 'Prentice', age:32}</li>
<li">];</li>
<li">&nbsp;</li>
<li">function compareByAge(a,b) { // comparison function, a and b are persons</li>
<li">&nbsp; if (a.age &lt; b.age) &nbsp; &nbsp; &nbsp; &nbsp; // compare by age</li>
<li">&nbsp; &nbsp; return -1;</li>
<li"> </li>
<li">&nbsp; if (a.age &gt; b.age)</li>
<li">&nbsp; &nbsp; return 1;</li>
<li"> </li>
<li">&nbsp; return 0;</li>
<li">}</li>
<li">&nbsp;</li>
<li"><strong>persons.sort(compareByAge); // this will call automatically compareByAge</strong></li>
<li"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // passing all persons from the array, compare</strong></li>
<li"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // them by age and sort the array.</strong></li>
</ol></div>

Explanations:

+ _Line 17_ calls `persons.sort(function_that_compares_two_elements)`, passing as an unique parameter a function that compares two people's ages. This function must return -1 if the first person is younger than the second person. It must return +1 if the first person is older than second person, and 0 if they are the same age.

We will see more methods in the other subsections of this page.

##### Types of elements in array

Elements can be of different types in a same array

<div><ol>
<li" value="1">&gt; var a = [1,2,3];</li>
<li">&nbsp;</li>
<li">&gt; a[2] = 'three'; </li>
<li"> "three" </li>
<li">&nbsp;</li>
<li">&gt; a </li>
<li"> [1, 2, "three"]</li>
</ol></div>


##### Adding elements to an array

We can add new elements using a new index, if you want to add a new element at the end, use the `push` method!

<div><ol>
<li" value="1">&gt; var a = [1,2,"three"];</li>
<li">undefined</li>
<li">&nbsp;</li>
<li">&gt; a[3] = 'four';</li>
<li"> "four"</li>
<li">&nbsp;</li>
<li">&gt; a;</li>
<li"> [1, 2, "three", "four"]</li>
<li">&nbsp;</li>
<li">&gt; a[a.length] = "five"; // adding at the end</li>
<li"> [1, 2, "three", "four", "five"]</li>
<li">&nbsp;</li>
<li">&gt;<strong> a.push("six"); // but usually we prefer using the push method for adding</strong></li>
<li"> [1, 2, 3, "four", "five", "six"] &nbsp;<strong>// a new element at the end</strong></li>
<li">&nbsp;</li>
<li">&nbsp;</li>
</ol></div>

When using indexes, be careful not to leave "holes" in the array:

<div><ol>
<li" value="1">&gt; a[7] = 'height';</li>
<li"> "height"</li>
<li">&nbsp;</li>
<li">&gt; a;</li>
<li"> [1, 2, 3, "four", "five", "six", <strong>undefined × 1</strong>, "height"]</li>
</ol></div>

This array is valid, but having a [6] equal to "undefined" is often prone to errors. Be careful when using absolute indexes for adding elements. We recommend using the `push` method instead.


##### Removing elements from an array

The recommended method is to use the `splice` method:

<div><ol>
<li" value="1">array.splice(start)</li>
<li">array.splice(start, deleteCount)</li>
</ol></div>

+ __start:__ index at which to start changing the array (with origin 0). 
+ __deleteCount (Optional):__ an integer indicating the number of old array elements to remove.  If deleteCount is greater than the number of elements left in the array starting at start, then all of the elements through the end of the array will be deleted. __If deleteCount is omitted,__ deleteCount will be equal to `(array.length - start)`, i.e., __all of the elements beginning with start index on through the end of the array will be deleted.__
+ __Return value:__ an array containing the deleted elements. If only one element is removed, an array of one element is returned. If no elements are removed, an empty array is returned.

Examples:

<div><ol>
<li" value="1">&gt; a;</li>
<li">[1, 2, 3, "four", "five", "six", undefined × 1, "height"]</li>
<li">&nbsp;</li>
<li">&gt;<strong> a.splice(6, 1); // remove element at the sixth index, the undefined one!</strong></li>
<li">[undefined × 1]</li>
<li">&nbsp;</li>
<li">&gt; a;</li>
<li">[1, 2, 3, "four", "five", "six", "height"] // it's no more here :-)</li>
<li">&nbsp;</li>
<li">&gt;<strong> a.splice(0, 3); // remove the three first elements</strong></li>
<li">[1, 2, 3]</li>
<li">&nbsp;</li>
<li">&gt; a;</li>
<li">["four", "five", "six", "height"]</li>
<li">&nbsp;</li>
<li">&gt;<strong> a.splice(a.length-1); // remove the last element</strong></li>
<li">"height"</li>
<li">&nbsp;</li>
<li">&gt; a;</li>
<li">["four", "five", "six"]</li>
</ol></div>


##### Removing element with `pop` method

Recommended method for removing the last element: the `pop` method!

<div><ol>
<li" value="1"><strong>&gt; a</strong></li>
<li">["four", "five", "six"]</li>
<li">&nbsp;</li>
<li">&gt;<strong> a.pop(); // remember push/pop = add / remove element at last position!</strong></li>
<li">"six"</li>
<li">&nbsp;</li>
<li">&gt; a</li>
<li">["four", "five"]</li>
</ol></div>

Trap: the delete method is not good for removing an element from an array!

<div><ol>
<li" value="1">&gt; <strong>delete a[1];</strong></li>
<li">true</li>
<li">&nbsp;</li>
<li">&gt; a;</li>
<li">["four", undefined × 1] <strong>// the element became undefined, </strong></li>
<li"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // but it's still in the array!</strong></li>
</ol></div>


#### Arrays of arrays

It is possible for an array to be an element within an array! This example shows an array made of two arrays of three elements each. It's a 2x3 matrix with two rows and three columns!

<div><ol>
<li" value="1">&gt; var a = [[1,2,3], [4,5,6]]; // a is a matrix: 2 rows, 3 columns.</li>
<li">undefined</li>
<li">&nbsp;</li>
<li">&gt; a[0]; // first row</li>
<li">[1, 2, 3]</li>
<li">&nbsp;</li>
<li">&gt; a[1]; // second row</li>
<li">[4, 5, 6]</li>
<li">&nbsp;</li>
<li">&gt; a[0][0]; // top left element</li>
<li">1</li>
<li">&nbsp;</li>
<li">&gt; a[0][1]; // second element, first line</li>
<li">2</li>
<li">&nbsp;</li>
<li">&gt; a[0][2]; // third element, first line</li>
<li">3</li>
<li">&nbsp;</li>
<li">&gt; a[1][0]; // first element, second line</li>
<li">4</li>
<li">&nbsp;</li>
<li">&gt; a[1][1]; // second element, second line</li>
<li">5</li>
<li">&nbsp;</li>
<li">&gt; a[1][2]; // third element, second line</li>
<li">6</li>
</ol></div>

It is possible to have different arrays with different lengths and different types of element in an array:

<div><ol>
<li" value="1">&gt; var a = [];</li>
<li">undefined</li>
<li">&nbsp;</li>
<li">&gt; a[0] = [1, 2, 3, 4, 5];</li>
<li">[1, 2, 3, 4, 5]</li>
<li">&nbsp;</li>
<li">&gt; a[1] = ['michel', 'henri', 'francois']</li>
<li">["michel", "henri", "francois"]</li>
<li">&nbsp;</li>
<li">&gt; a</li>
<li">[Array(5), Array(3)]</li>
</ol></div>


#### Notes for 3.2.1 Arrays

+ Elements in an array
  + array: a collection of "things", including strings, integer values, decimal values, boolean values, or any objects
  + creating an array: putting elements btw "[" abd "]", e.g., `var myarr = ['red', 'blue', 'yellow', 'purple'];`
  + each element of an array w/ key/index and a value
  + type of an array: object, e.g., `var a = []; typeof a; // "object"`
  + index beginning at "0"
  + properties and methods: `let a = [...];`
    + size of an array: `a.length`
    + sort an array: `a.sort([function_that_compares_two_elements]);`
      + numeric: return array object from lowest to highest
      + string: return array object w/ element alphabetically
      + object: depending on `function_that_compares_two_elements`, e.g., 

        ```js
        var persons = [
            {givenName: 'Michel', familyName: 'Buffa', age:51},
            {givenName: 'Pig', familyName: 'Bodine', age:20},
            {givenName: 'Pirate', familyName: 'Prentice', age:32}
        ];
        
        function compareByAge(a,b) { // comparison function, a and b are persons
          if (a.age < b.age)         // compare by age
            return -1;
          if (a.age > b.age)
            return 1;
          return 0;
        }

        persons.sort(compareByAge);
        ```

    + remove n elements starting from idx: `a.splice(idx, n);`; e.g., `a.splice(2, 1); // remove 1 elt starting from idx=2 (3rd elt)`
  + type of elements: different types of element allowed in an array; e.g., `let a = [1, 2, "three"]`

+ Adding element
  + using a new index
    + not to leave a hole in the array; e.g., `let a = [1, 2, 3]; a[4] = 4; a; // a = [1, 2, 3, undefined x 1, 4]`
    + example: `let a = [1, 2, 3]; a[3] = "four"; a[a.length] = "five"; // a = [1, 2, 3, "four", "five"]`
  + adding a new element at the end w/ `push()` method, e.g., `a.push("five"); // a = [..., "five"]`
  + recommendation: using `push()` method

+ Removing element
  + `splice()` method
    + syntax:
      + `array.splice(start)`
      + `array.splice(start, deleteCount)`
    + parameters
      + __start:__ index at which to start changing the array
      + __deleteCount:__  (optional)
        + an integer indicating the number of old array elements to remove
        + `deleteCount` > size of array left (from start to end): remove all elements
        + `deleteCount` omitted: `deleteCount = array.length - start`, delete all elements starting from `start` to end of array
    + return value:
      + an array containing the deleted elements
      + a one-element array if only one element removed
      + empty array if no element removed
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

+ Arrays of arrays
  + numerical array
    + a `n x m` matrix
    + examples
      + a matrix w/ 2 rows, 3 columns: `var a = [[1,2,3], [4,5,6]];`
      + accessing rows: `a[0]; // [1, 2, 3]` & `a[1]; // [4, 5, 6]`
      + element: `a[0][0]; // top left element` $\to$ 1; `a[0][1]; // second element, first line` $\to$ 2; `a[1][2]; // third element, second line` $\to$ 6
  + array w/ differnet types of arrays, e.g., `a[0] = [1, 2, 3, 4, 5]; a[1] = ['michel', 'henri', 'francois']; a; // [Array(5), Array(3)]`

+ [The `Array.prototype.push()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)

+ [The `Array.prototype.pop()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)

+ [The `Array.prototype.sort()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
  + syntax: `arr.sort([compareFunction])`
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

+ [The `Array.prototype.splice()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)


#### Knowledge check 3.2.1

```js
var a = [1, 2, 3, "four", "five", "six", "seven", "height"]
```

1. How would you remove elements "four" and "five" at once?

  a. `a.splice(3, 2);`<br>
  b. `a.delete(4, 5);`<br>
  c. `a.remove(3, 2);`<br>
  d. `a.splice(2, 4);`<br>

  Ans: a<br>
  Explanation: You must use the `splice` method. The arguments are two-fold: the starting index, and the number of elements to remove. "four" is at index 3, the number of elements to remove is 2. The correct answer is `a.splice(3, 2);`.


### 3.2.2 Strings are arrays of characters

Yes, they do look like arrays!

JavaScript strings are "like" arrays of characters, but they have some limitations, and some dedicated properties and methods:

<div><ol>
<li" value="1">&gt; var s = 'Michel';</li>
<li">undefined</li>
<li">&nbsp;</li>
<li">&gt; s[0];</li>
<li">"M"</li>
<li">&nbsp;</li>
<li">&gt; s[1];</li>
<li"> "i"</li>
<li">&nbsp;</li>
<li">&gt; s.length;</li>
<li">6</li>
</ol></div>

Indeed, the string `s` behaves like an array, it has the `length` property like an array, and we can access individual characters using indexes that go from 0 to `length-1`, like arrays...

However... they are not quite the same as arrays!

You cannot add elements to strings using a non-existent index, you cannot use the push/pop methods for adding/removing  characters at the end of the string:

<div><ol>
<li" value="1"><strong>s.push(' Buffa');</strong></li>
<li"><strong>&nbsp;</strong></li>
<li"><strong>ERROR: VM5748:1 Uncaught TypeError: s.push is not a function</strong></li>
<li"><strong> at &lt;anonymous&gt;:1:3</strong></li>
<li"><strong>(anonymous) @ VM5748:1</strong></li>
<li">&nbsp;</li>
<li">s[s.length] = 'B'; // add 'B' at the end?</li>
<li">"B"</li>
<li">&nbsp;</li>
<li">s[s.length] = 'u'; // add 'u' at the end?</li>
<li">"u"</li>
<li">&nbsp;</li>
<li">s[s.length] = 'f'; // add 'f' at the end?</li>
<li">"f"</li>
<li">&nbsp;</li>
<li"><strong>s; // s remained UNCHANGED!</strong></li>
<li"><strong>"Michel"</strong> </li>
</ol></div>

+ You cannot use push/pop as this raises an error "is not a function" (_lines 1-5_)
+ You can try to put elements out of the range of the string: nothing will happen and the string will remain unchanged (_lines 7-17_)

You can't even modify a character using an index. Strings are "read only" when using brackets to access individual characters!

<div><ol>
<li" value="1">&gt; var s = 'Michel';</li>
<li">undefined</li>
<li">&nbsp;</li>
<li">&gt; s[0] = "R"; // trying to change the 'M' into an 'R'</li>
<li">"R"</li>
<li">&nbsp;</li>
<li">s; // no luck!</li>
<li">"Michel"</li>
</ol></div>

You also can't remove characters using the array's splice method:

<div><ol>
<li" value="1">&gt; s.splice(0, 3);</li>
<li">&nbsp;</li>
<li">ERROR: VM716:1 Uncaught TypeError: s.splice is not a function</li>
<li"> at &lt;anonymous&gt;:1:3</li>
</ol></div>

So: how do we add characters to a string, how can we modify a string? How can we delete elements in a string ?

Strings come with a whole set of methods, which we'll come to in module 4 when we talk about JavaScript objects (in the section titled "JavaScript predefined objects"). Without going into detail just yet, here are some examples:

#### Concatenation with `+` operator

__Adding a string to the beginning of a string using the + operator:__

<div><ol>
<li" value="1">&gt; <strong>var s = 'Michel';</strong></li>
<li">undefined</li>
<li">&nbsp;</li>
<li">&gt;<strong> s = "Hello " + s;</strong></li>
<li">"Hello Michel"</li>
<li">&nbsp;</li>
<li">&gt;<strong> s = 'O' + s;</strong> // equivalent to push('0') with arrays</li>
<li"> "OHello Michel"</li>
</ol></div>

__Adding a string to the end of another one with the + operator:__

<div><ol>
<li" value="1"><strong>&gt;s = 'Michel';</strong></li>
<li">"Michel"</li>
<li">&nbsp;</li>
<li">&gt;<strong> s += ' Buffa';</strong></li>
<li">"Michel Buffa"</li>
<li">&nbsp;</li>
<li">&gt; s;</li>
<li">"Michel Buffa"</li>
</ol></div>


#### Removing substring

__Removing chars from a string using the `substring` method:__

Removing the last char (equivalent to the pop method from arrays):

<div><ol>
<li" value="1">&gt; var s = 'Michel';</li>
<li">undefined</li>
<li">&nbsp;</li>
<li">&gt;<strong>&nbsp;s = s.substring(0, s.length-1);</strong></li>
<li">"Miche"</li>
</ol></div>


__Removing a certain number of chars starting from a string, starting at a given index:__

<div><ol>
<li" value="1">var s = 'Michel';</li>
<li">&nbsp;</li>
<li"><strong>function removeChars(s, startIndex, numberOfCharsToRemove) {</strong></li>
<li"><strong>&nbsp; &nbsp;return s.substring(0, startIndex) +&nbsp; &nbsp;</strong></li>
<li"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; s.substring(startIndex&nbsp;+&nbsp;numberOfCharsToRemove);</strong></li>
<li"><strong>}</strong></li>
<li">&nbsp;</li>
<li">// remove 3 consecutive chars from s, starting at index = 1</li>
<li">s = removeChars(s, 1, 3);</li>
<li">&nbsp;</li>
<li">console.log(s); // will display "Mel" in the console</li>
</ol></div>


__Replacing a char at a given index:__

<div><ol>
<li" value="1">function replaceAt(s, index, character) {</li>
<li">&nbsp; &nbsp; return s.substr(0, index) + character + s.substr(index+character.length);</li>
<li">}</li>
<li">&nbsp;</li>
<li"><strong>var s2 = "JavaScript";</strong></li>
<li"><strong>s2 = replaceAt(s2, 1, "o");</strong></li>
<li">&nbsp;</li>
<li">console.log(s2); // will display "JovaScript"</li>
<li">&nbsp;</li>
<li"><strong>// it also works with a string instead of a simple char</strong></li>
<li"><strong>s2 = replaceAt(s2, 0, "Coca");</strong></li>
<li"><strong>console.log(s2); // Will display "CocaScript"</strong></li>
</ol></div>


#### Notes for 3.2.2 Strings are arrays of characters

+ String as array
  + "like" array of characters
    + behave like an array
    + w/ `length` property
    + able to access individual characters w/ indexes
    + example: `let s = 'Michel'; s[0]; // 'M'`, `s[1] // 'i'` & `s.length; // 6`
  + limitations
    + unable to add elements to string using a non-existent index
    + unable to use `push/pop` methods for adding/removing characters at the end of string
    + unable to modify a character w/ an index
    + unable to remove a character w/ `splice` method
    + examples
      + using `push` method: `s.push('Buffa); // ERROR: VM5748:1 Uncaught TypeError: s.push is not a function at <anonymous>:1:3 (anonymous) @ VM5748:1`
      + adding a character at the end but remaining UNCHANGED: `s[s.length] = 'B'; // "B"` but `s; // "Michel"`
      + changing a character in string: `s[0] = "R"; // "R"` & `s; // "Michel"`
      + using `splice` method: `s.splice(0, 3); // ERROR: VM716:1 Uncaught TypeError: s.splice is not a function at <anonymous>:1:3`

+ String operation
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


#### Knowledge check 3.2.2

1. What is the name of the function/method for removing a given number of chars from a string, starting at a given index?

  a. There is no built-in method/function for that, we need to build one.<br>
  b. `splice`, with the same syntax we used with JavaScript arrays<br>
  c. `substring`<br>

  Ans: <span style="color: brown;">a, xc<br>
  Explanation: Indeed, there is no built-in function for that. We presented in the course a `removeChars(s, startIndex, numberOfCharsToRemove)` function that uses the substring method.


### 3.2.3 Iterating on array elements


#### Live coding video: iterating on arrays

<a href="https://edx-video.net/W3CJSIXX2016-V003300_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y7dzppcz)

Get the source code of the example shown in the video:

[CodePen Demo](https://codepen.io/w3devcampus/pen/VWYMNK)

[Local Demo](src/03b-example02.html)

Let's study the different methods for iterating on array elements.


#### Method #1: iterating using `forEach`

The `forEach` method takes a single argument that is a function/callback that can have one, two or three parameters:

+ The first parameter is the current element of the array,
+ The second parameter (optional) is the index of the current element in the array,
+ The third element is the array itself

__Typical use with only one parameter (the current element):__

<div><ol>
<li" value="1"><strong>var a = ['Monday', 'Tuesday', 'Wednesday'];</strong></li>
<li">&nbsp;</li>
<li"><strong>a.forEach</strong>(function(day) {</li>
<li">&nbsp; &nbsp; // day is the current element</li>
<li">&nbsp; &nbsp; document.body.innerHTML += day + </li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "&lt;br&gt;"; // will display Monday, Tuesday, Wednesday</li>
<li">})</li>
</ol></div>

This is the most practical way to iterate on each individual element of a collection (array, string);

[CodePen Demo](https://codepen.io/w3devcampus/pen/QpRybG)

[Local Demo](src/03b-example03.html)


Now, let's iterate on an array of person, and use two parameters in the callback function in order to get the index of the current element:

[CodePen Demo](https://codepen.io/w3devcampus/pen/rygxpr)

[Local Demo](src/03b-example04.html)

<div><ol>
<li" value="1">var persons = [</li>
<li">&nbsp; &nbsp; &nbsp;{name:'Michel', age:51},</li>
<li">&nbsp; &nbsp; &nbsp;{name:'Henri', age:20},</li>
<li">&nbsp; &nbsp; &nbsp;{name:'Francois', age:29}</li>
<li">];</li>
<li">&nbsp;</li>
<li">persons.forEach(function(<strong>p, index</strong>) {</li>
<li">&nbsp; &nbsp; &nbsp;document.body.innerHTML += p.name + ", age " + p.age + </li>
<li"><span style="color: #000000;" color="#000000">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;", at index " + index + " in the array&lt;br&gt;";</li>
<li">});</li>
</ol></div>


__Finally, let's use three parameters, the last one being the array itself__

This can be useful if we need to know the length of the array, or do special things within the array (add/change/move elements during the iteration):

[CodePen Demo](https://codepen.io/w3devcampus/pen/ZKyMQj)

[Local Demo](src/03b-example05.html)

In this example, we used the third parameter (the array) to access its length inside the iteration loop.


#### Method #2: iterating on an array using regular loop statements

You can use any standard loop statement that we saw during in module 2. The most common way to iterate over an array is to use a `for` loop from 0 to length-1. 

Using this method allows elements to be iterated two by two, or the loop to be broken in the middle using the `break` instruction, etc.

__Iterating over all elements in an array, using a `for` loop__

[CodePen Demo](https://codepen.io/w3devcampus/pen/evaJKL)

[Local Demo](src/03b-example06.html)

Another example where we iterate two by two (just changed the increment in the for loop):

[CodePen Demo](https://codepen.io/w3devcampus/pen/zZQrme)

[Local Demo](src/03b-example07.html)


#### Notes for 3.2.3 Iterating on array elements

+ Iteration of array
  + iterating w/ `forEach`
    + parameters of `forEach`
      + the current element of the array
      + (optional) the index of the current element in the array
      + (optional) the array itself
    + examples:
  
      ```js
      var a = ['Monday', 'Tuesday', 'Wednesday'];

      a.forEach(function(day) { // day is the current element
          document.body.innerHTML += day + "<br>"; // will display Monday, Tuesday, Wednesday
      })

      persons.forEach(function(p, index) {
        document.body.innerHTML += p.name + ", age " + p.age +
                             ", at index " + index + " in the array<br>";
      });

      persons.forEach(function(p, index, theArray) {
        document.body.innerHTML += p.name + ", age " + p.age +
            ", at index " + index + " in the array of " + theArray.length + " elements<br>";
      });
      ```

  + iterate using regular `for` loop
    + most common way to iterate over an array is to use a `for` loop from 0 to length-1
    + allowing element to be iterated step  other than 1 or broken in the middle w/ `break` instruction
    + examples:

      ```js
      var persons = [
        {name:'Michel', age:51}, {name:'Henri', age:20}, {name:'Francois', age:29}
      ];

      for(var i = 0; i < persons.length; i++) {
        var p = persons[i]; // current element
        document.body.innerHTML += p.name + "<br>"; 
      }

      for(var i = 0; i < persons.length; i+=2) {
        var p = persons[i]; // current element
        document.body.innerHTML += p.name + "<br>"; 
      }
      ```

+ [`array.forEach` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)


#### Knowledge check 3.2.3

1. Can you iterate only on elements that have an odd index using the forEach iterator, without adding a test inside the instructions in the body of the loop? (No/Yes)

  Ans: No<br>
  Explanation: No, the forEach method iterates on all the elements of an array. You can use a for loop for iterating on odd indexes, like that: `for(var i = 1; i less than a.length; i += 2) {....}`


### 3.2.4 Discussion and projects

Please either post your comments/observations/questions or share your creations.

#### Suggested topics

+ Which syntax do you prefer for iterating arrays?
+ We decided not to explain all the things you can do with the `splice` method. It's a very powerful method, but showing all its features could be overwhelming. However, if you're curious, please look on the Web for more details. Do you think we've been right not to tell you all the possibilities of splice?

#### optional project: an interactive picture album browser

Let's start with an array variable like that:

<div><ol>
<li" value="1">let myPicturesArray = [</li>
<li"> {</li>
<li">&nbsp; &nbsp; "albumId": 1,</li>
<li">&nbsp; &nbsp; "id": 1,</li>
<li">&nbsp; &nbsp; "title": "accusamus beatae ad facilis cum similique qui sunt",</li>
<li">&nbsp; &nbsp; "url": "https://placehold.it/600/92c952",</li>
<li">&nbsp; &nbsp; "thumbnailUrl": "https://placehold.it/150/92c952"</li>
<li"> },</li>
<li"> {</li>
<li">&nbsp; &nbsp; "albumId": 1,</li>
<li">&nbsp; &nbsp; "id": 2,</li>
<li">&nbsp; &nbsp; "title": "reprehenderit est deserunt velit ipsam",</li>
<li">&nbsp; &nbsp; "url": "https://placehold.it/600/771796",</li>
<li">&nbsp; &nbsp; "thumbnailUrl": "https://placehold.it/150/771796"</li>
<li"> },</li>
<li"> {</li>
<li">&nbsp; &nbsp; "albumId": 2,</li>
<li">&nbsp; &nbsp; "id": 51,</li>
<li">&nbsp; &nbsp; "title": "non sunt voluptatem placeat consequuntur rem incidunt",</li>
<li">&nbsp; &nbsp; "url": "https://placehold.it/600/8e973b",</li>
<li">&nbsp; &nbsp; "thumbnailUrl": "https://placehold.it/150/8e973b"</li>
<li"> },</li>
<li"> {</li>
<li">&nbsp; &nbsp; "albumId": 2,</li>
<li">&nbsp; &nbsp; "id": 52,</li>
<li">&nbsp; &nbsp; "title": "eveniet pariatur quia nobis reiciendis laboriosam ea",</li>
<li">&nbsp; &nbsp; "url": "https://placehold.it/600/121fa4",</li>
<li">&nbsp; &nbsp; "thumbnailUrl": "https://placehold.it/150/121fa4"</li>
<li"> },</li>
<li"> {</li>
<li">&nbsp; &nbsp; "albumId": 3,</li>
<li">&nbsp; &nbsp; "id": 127,</li>
<li">&nbsp; &nbsp; "title": "magnam quia sed aspernatur",</li>
<li">&nbsp; &nbsp; "url": "https://placehold.it/600/74456b",</li>
<li">&nbsp; &nbsp; "thumbnailUrl": "https://placehold.it/150/74456b"</li>
<li"> },</li>
<li"> {</li>
<li">&nbsp; &nbsp; "albumId": 3,</li>
<li">&nbsp; &nbsp; "id": 128,</li>
<li">&nbsp; &nbsp; "title": "est facere ut nam repellat numquam quia quia eos",</li>
<li">&nbsp; &nbsp; "url": "https://placehold.it/600/b0931d",</li>
<li">&nbsp; &nbsp; "thumbnailUrl": "https://placehold.it/150/b0931d"</li>
<li"> }</li>
<li">];</li>
</ol></div>

+ It's an array of pictures, each picture having a URL, a URL for a tiny version of the picture, called a thumbnail, a title, and the name of the album it belongs to, that can be used as a picture description (HTML `alt` attribute) but also for displaying it next to the picture.
+ Here is a small example that iterates on the pictures and create `<img>` elements on the fly:

[CodePen Demo](https://codepen.io/w3devcampus/pen/KqzPOm)

[Local Demo](src/03b-example08.html)

What you will have to do:

1. __Improve the display, by adding margins (CSS), shadows, border, and changing the URLs for real pictures.__ Remember that you need to have a smaller versions of the pictures, i.e., thumbnails. You can use existing images (images.google.com is your friend) or images you upload somewhere.
1. __Use JavaScript for adding a click event listener on each image,__ then when clicked, you will show a bigger version of each picture. For the moment, just change the value of the src attribute of the clicked image (set it to the URL of the full size image from the array).
1. __Try to make something nicer: reserve a `<div>` on the right of the document so to display the clicked image with a bigger size.__ In that case, you will need to create an image (only once, after the first click), to set it to the size of the div (use the width and height attributes of the img element), and to append it to the div.
1. __Try to add more images, and find a way to display them per album.__ Create buttons entitled "album1", "album2", etc., and when clicked, you will only display images from the selected album.
1. __[Advanced] Add an option for deleting a picture.__ It should be removed from the document and from the array too...
1. __Feel free to add any interesting feature you think about ;-)__


