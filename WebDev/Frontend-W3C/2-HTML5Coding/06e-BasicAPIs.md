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

  Ans: <br/>
  Explanation: 


2. Help the Beatles!

  Check the correct syntaxes for writing data in localStorage: (3 correct answers.)

  a. `localStorage.name = "John Lennon";`<br/>
  b. `localStorage.setItem("Paul McCartney");`<br/>
  c. `localStorage['name'] = "George Harrison";`<br/>
  d. `localStorage.setItem("Full Name","Ringo Starr");`<br/>

  Ans: <br/>
  Explanation: 


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

  Ans: <br/>
  Explanation: 


4. Store arrays or objects?

  How can we store JavaScript arrays and objects in localStorage or sessionStorage?

  a. We can use the JSON format, together with the JSON.stringify and JSON.parse methods.<br/>
  b. We can't.<br/>

  Ans: <br/>
  Explanation: 



