# Module 4: Web components and other HTML5 APIs section


## 4.5 Final exam (26 Questions)


### 4.5.1 Web components (1-5)

1. Were you aware?

  While reading the course' Module 1 content, were we using Web components without realising it? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, as we discussed during Module 4, the `<video>` and `<audio>` elements are Web components created by the browsers' developers.


2. Valid or invalid?

  ```html
  <x-gif src="http://i.imgur.com/iKXH4E2.gif" ping-pong></x-gif>
  ```

  Is this code valid HTML5 code, if the `<x-gif>` element has been created using the Custom Elements API? (yes/No)

  Ans: Yes<br>
  Explanation: Yes, any custom element created with the Custom Elements API is valid HTML.


3. Import me!

  ```html
  <script type="module" src="mycomponent.js"></script>
  ```

  What does the above line do?

  a. We cannot use this syntax to import WebComponents. The correct way is to use HTML imports.<br>
  b. This is how a JavaScript module can be loaded in a HTML page. This is the modern way to import WebComponents.<br>

  Ans: b<br>
  Explanation: HTML imports are obsolete now. The preferred way to import WebComponents is to load them as JavaScript/EcmaScript modules.


4. Am I well supported?

  Is it possible to properly render a page that uses Web components on modern browsers?

  a. Most browsers support WebComponents, and good polyfills are available to run on old browsers.<br>
  b. Unfortunately, Web components use APIs that are not well supported by many of the major browsers, even the most recent versions<br>

  Ans: a<br>
  Explanation: Most browsers now support the three main WebComponents API (HTML template, Shadow DOM, Custom Elements) and importing Web Components relies on JavaScript Imports that are also well supported. To maximize support, polyfills are also available.


5. Am I made of Web components?

  Which of the following frameworks are based on Web components? (2 correct answers.)

  a. jQuery<br>
  b. AngularJS<br>
  c. Lit-HTML<br>
  d. X-Tags<br>
  e. Bower<br>

  Ans: <font style="color: red;">cd</font>, xad<<br>
  Explanation: Lit-HTML (by Google) and X-Tags (by Mozilla) are frameworks built on Web components.






