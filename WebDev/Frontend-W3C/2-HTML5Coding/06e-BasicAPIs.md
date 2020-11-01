# Week 6: HTML5 Basic APIs


## 6.5 Final exam


### 6.5.1 Intro final exam

The final exam consists of 28 questions (multiple choice, checkboxes, etc.) covering the entirety of the course.

As stated in the grading policy page, this final exam counts towards 25% of the final grade.


### 6.5.2 Exercises (1-4)

1. localStorage vs sessionStorage

  What is the difference between localStorage and sessionStorage?

  a. With localStorage, the data will remain until deleted. With sessionStorage, the data is erased when the tab/browser is closed.<br/>
  b. Session storage uses cookies and HTTP sessions similar to PHP or Java Servlets. Data is stored on the memory of a remote server, and only the session ID is stored locally.<br/>

  Ans: a<br/>
  Explanation: Web storage provides two interfaces called sessionStorage and localStorage, whose main difference is data longevity. This specification defines an API for persistent data storage of key-value pair data in Web clients.


2. Help the Beatles!

  Check the correct syntaxes for writing data in localStorage: (3 correct answers.)

  a. `localStorage.name = "John Lennon";`<br/>
  b. `localStorage.setItem("Paul McCartney");`<br/>
  c. `localStorage['name'] = "George Harrison";`<br/>
  d. `localStorage.setItem("Full Name","Ringo Starr");`<br/>

  Ans: acd<br/>
  Explanation: The first answer is correct. The third answer is correct as localStorage.name is equivalent in JavaScript to the proposed syntax with brackets. The fourth answer is correct as the setItem method takes the key as the first parameter, and the value as the second parameter. The key can contain spaces. This is why setItem is useful: for storing data whose key contains spaces. Correct answers are 1, 3 and 4.


3. localStorage for all or just for me?

  Important note: the domain buffa.org does not actually exist in real life, but for the sake of this exercise, we'll pretend that it does.

  <pre>for (var i = 0, n = localStorage.length; i &lt; n; i++) {
      var k = localStorage.key(i);
      console.log(k + ": " + localStorage[k]); 
  }
  </pre>

  I visit `http://buffa.org/index.html`. The page contains the above code: what does it do?

  a. It prints in the dev. tools console all the keys and values for all visited Web sites that used localStorage for storing data.<br/>
  b. It prints in the dev. tools console all the keys and values for the domain buffa.org (following the "same origin policy").<br/>
  c. It prints in the dev. tools console all the keys and values for the page http://buffa.org/index.html<br/>

  Ans: <span style="color: magenta;">b</span>, xa<br/>
  Explanation: The data written in local storage is "per domain", following the same origin policy.


4. Store arrays or objects?

  How can we store JavaScript arrays and objects in localStorage or sessionStorage?

  a. We can use the JSON format, together with the JSON.stringify and JSON.parse methods.<br/>
  b. We can't.<br/>

  Ans: a<br/>
  Explanation: JSON provides a great way of encoding and decoding data that is a really good match for JavaScript. We saw this in the course examples that store JavaScript objects as JSON.



