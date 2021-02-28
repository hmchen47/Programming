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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> pictures </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; {</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "albumId"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "id"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; author: {</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; "name":"michel",</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; "job": "Professor"</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; },</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "title"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Holidays in Roma"</span><span class="pun">,</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "url"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/600/92c952"</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "thumbnailUrl"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/150/92c952"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; },</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; {</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "albumId"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "id"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span></li>
<li class="L3"><span class="pun">&nbsp; &nbsp; author: {</span></li>
<li class="L3"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; "name":"Marie Claire",</span></li>
<li class="L3"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; "job": "Michel's Boss!"</span></li>
<li class="L3"><span class="pun">&nbsp; &nbsp; },</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "title"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Eating an ice cream at the Coliseum"</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "url"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/600/771796"</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "thumbnailUrl"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/150/771796"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">];</span></li>
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






