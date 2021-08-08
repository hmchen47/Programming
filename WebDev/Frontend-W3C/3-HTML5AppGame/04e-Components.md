# Module 4: Web components and other HTML5 APIs section


## 4.5 Final exam (37 Questions)


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


### 4.5.2 HTML5 templates (6-8)

6. Dead or alive?

  The code in HTML templates is:

  a. to be rendered, the content of a template needs to be cloned within JavaScript, and the cloned version inserted into the DOM of a document.<br>
  b. the same as any other unit of HTML code. When a page includes a template, it's rendered amongst the rest of the HTML code.<br>
  
  Ans: a<br>
  Explanation: Template code is inert: it cannot be rendered! If you practice object-oriented programming: it's similar to a "sort of class" that needs to be instantiated before use. The instantiation process consists of cloning the template's content and adding that to the DOM of a document.


<hr>

__Source code for the next 2 questions (7 and 8)__

HTML:

<div><ol>
<li value="1"> &lt;template id="mytemplate"&gt;</li>
<li>&nbsp; &nbsp;&lt;img src=""&nbsp;id="myImage"&nbsp;alt="a great image"&gt;</li>
<li>&nbsp; &nbsp;&lt;div class="comment"&gt;hello&lt;/div&gt;</li>
<li> &lt;/template&gt; </li>
</ol></div>

JavaScript:

<div><ol>
<li value="1">function instanciate() {</li>
<li>&nbsp; &nbsp;var t = document.querySelector('#mytemplate');</li>
<li> </li>
<li>&nbsp; &nbsp;<span style="color: #ff0000;"><strong style="color: #AA0000;">XXX</strong>.querySelector('#myImage').src =</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 'http://webcomponents.github.io/img/logo.svg';</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;var clone = document.<span style="color: #0000ff;"><strong style="color: #AA0000;">YYY</strong>(<span style="color: #ff0000;"><strong style="color: #AA0000;">XXX</strong>, true);</li>
<li> </li>
<li>&nbsp; &nbsp;// add it to the body of the HTML document</li>
<li>&nbsp; &nbsp;document.body.appendChild(clone); </li>
<li>}</li>
</ol></div>

7. Give me content!

  How would you complete the source code above to access the content of the template? Enter exactly what you would put instead of the __XXX__ placeholders!
  
  Ans: `t.content`<br>
  Explanation: In the above example, the right answer is `t.content`


8. Clone me!

  How would you clone the content of the template? Enter exactly what you would enter instead of the __YYY__ placeholder!
  
  Ans: `importNode`<br>
  Explanation: In the above example, the right answer is `importNode`



### 4.5.3Shadow DOM (9-13)

9. Really hidden?

  Only a few current browsers, e.g. Google or Chrome, offer native support for the shadow DOM API. Is it possible to use the devtools to inspect the HTML source of a Web component even if it's located in the shadow DOM? (Yes/No)

  Ans: Yes<br>
  Explanation: By default, the shadow DOM content is hidden, but on Chrome and Opera (which support the shadow DOM natively), it's possible to use a setting in the devtools to expose the shadow DOM for debugging purposes. This was shown in several videos during the course.


<hr>

__Source code for the next three questions (10, 11, and 12)__

<div><ol>
<li value="1">&lt;p&gt;Please&nbsp;show me!&lt;/p&gt;</li>
<li>&lt;script&gt;</li>
<li>&nbsp; &nbsp;&nbsp;var&nbsp;b&nbsp;= document.querySelector('p');</li>
<li>&nbsp; &nbsp;&nbsp;var&nbsp;c&nbsp;= b.<span color="#000000" style="color: #000000;">attachShadow({mode: 'open'});;</li>
<li>&nbsp; &nbsp;&nbsp;c.textContent = 'I am a nice paragraph!';</li>
<li>&lt;/script&gt;</li>
</ol></div>

10. Who am I?

  The paragraph b is called a "shadow __XXXX__". What is the correct term (instead of __XXXX__)?

  Ans: <font style="color: red">host</font>, xroot<br>
  Explanation: The paragraph b is called a _shadow host_


11. What is my name?

  The variable c is called a "shadow __YYYY__". What is the correct term (instead of __YYYY__)?

  Ans: host<br>
  Explanation: The variable c is called a _shadow root_


12. Please show me!

  What is going to be rendered on the page?

  a. "I am a nice paragraph!"<br>
  a. "Please show me!"<br>

  Ans: a<br>
  Explanation: When an element has a shadow root, the content of the shadow DOM is rendered: in this case, it is "I am a nice paragraph!"


13. The shadow of robots?

What relationship exists between Isaac Asimov and the Shadow DOM?

  a. Isaac Asimov wrote "The Three Laws of Robotics", and the shadow DOM is also governed by three rules.<br>
  a. Isaac Asimov was born in a small Russian house called DOMA.<br>
  a. No relationship.<br>

  Ans: <font style="color: red">a</font>, xc<br>
  Explanation: Three rules do govern the shadow DOM: 1) With Shadow DOM, elements are associated with a new kind of node: a shadow root; 2) An element that has a shadow root associated with it is called a shadow host; 3) The content of a shadow host isn’t rendered; the content of the shadow root is rendered in its place.


### 4.5.4 Shadow DOM encapsulation (14-17)

14. The red and the black

  A page uses a Web component: a nice custom calendar. In this Web component's shadow DOM there are some buttons for rendering the calendar dates. Within the shadow DOM, CSS styles buttons to have a black background.

  On the page that uses the calendar Web component, we also have some buttons and a CSS style directing a red background for buttons.

  Which color will be applied to which buttons?

  a. The buttons on the page will be black, and the ones in the calendar will be red<br>
  b. The buttons on the page and those in the calendar will all be black<br>
  c. The buttons on the page will be red, and the ones in the calendar will be black<br>
  d. The buttons on the page and those in the calendar will all be red<br>
  
  Ans: c<br>
  Explanation: By default, CSS styles do not cross the boundaries of the Web component. The CSS from the shadow DOM of the Web component will not affect the buttons in the page, and the same is true for the CSS styles defined globally: they will affect buttons defined in the page but not those in Web Components. The buttons on the page will be red, and the ones in the calendar will be black.


15. Incompatible designs

  Is it possible to clone a template into a Web component's shadow DOM? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, and this is a very powerful feature! The template will be the HTML/CSS/JS skeleton of the Web component.


<hr>

__Source code for the next two questions (16 and 17)__

HTML:

<div><ol>
<li value="1">&lt;head&gt;</li>
<li>&nbsp; &lt;style&gt;</li>
<li>&nbsp; &nbsp; span {</li>
<li>&nbsp; &nbsp; &nbsp; color:green;</li>
<li>&nbsp; &nbsp; }</li>
<li>&nbsp; &lt;/style&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;template id="mytemplate"&gt;</li>
<li>&nbsp; &lt;style&gt;</li>
<li>&nbsp; &nbsp; h1 {</li>
<li>&nbsp; &nbsp; &nbsp; color:red;</li>
<li>&nbsp; &nbsp; }</li>
<li>&nbsp; &nbsp; span {</li>
<li>&nbsp; &nbsp; &nbsp; background-color:lightblue; </li>
<li>&nbsp; &nbsp; }</li>
<li>&nbsp; &lt;/style&gt;</li>
<li>&nbsp; &lt;h1&gt;Magnificient title&lt;/h1&gt;</li>
<li>&nbsp; &lt;span&gt;And I'm a span in the shadow DOM&lt;/span&gt;</li>
<li>&nbsp; &lt;p&gt;</li>
<li>&nbsp; &lt;slot name="my-text"&gt;My default text&lt;/slot&gt;</li>
<li>&lt;/template&gt;</li>
<li> </li>
<li>&lt;body&gt;</li>
<li>&nbsp; &lt;h1&gt;Hello my friends&lt;/h1&gt;</li>
<li>&nbsp; &lt;p id="myWidget"&gt;</li>
<li>&nbsp; &nbsp; &lt;span slot="my-text"&gt;Injected content&lt;/span&gt;</li>
<li>&nbsp; &lt;/p&gt;</li>
<li> </li>
<li>&nbsp; &lt;p&gt;This is not in the previous paragraph...&lt;/p&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>

JavaScript:

<div><ol>
<li value="1">// Instanciate the template</li>
<li>var t = document.querySelector('#mytemplate');</li>
<li>&nbsp;</li>
<li>// Create a root node under our h1 title</li>
<li>var host = document.querySelector('#myWidget');</li>
<li>const shadowRoot = host.attachShadow({mode: 'open'});</li>
<li>&nbsp;</li>
<li>&nbsp;</li>
<li>shadowRoot.appendChild(document.importNode(t.content, true));</li>
</ol></div>

16. Choose the nicest one!

  How will `<p id="myWidget">...</p>` be rendered? (Beware: 3 points are awarded for this problem.)

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://bit.ly/3xtUqJR" ismap target="_blank">
      a. <img style="margin: 0.1em;" width=200
        src   = "img/4.5.2-img2.jpg"
        alt   = "a. image showing 3 lines of text: the first one is a red title, below is a text in black, and the final text below is green"
        title = "a. image showing 3 lines of text: the first one is a red title, below is a text in black, and the final text below is green"
      >
      b. <img style="margin: 0.1em;" width=200
        src   = "img/4.5.2-img1.jpg"
        alt   = "b. image showing 3 lines of text: first one is a red title, second one is a text in black highlighted in blue, and the third one is a text in green"
        title = "b. image showing 3 lines of text: first one is a red title, second one is a text in black highlighted in blue, and the third one is a text in green"
      >
      c. <img style="margin: 0.1em;" width=150
        src   = "img/4.5.2-img4.jpg"
        alt   = "c. image showing only one line of text in green"
        title = "c. image showing only one line of text in green"
      >
    </a>
    <a href="https://bit.ly/3xtUqJR" ismap target="_blank">
      d. <img style="margin: 0.1em;" width=200
        src   = "img/4.5.2-img5.jpg"
        alt   = "d. image showing 3 lines of text: the first one is a red title, and the two other ones are made of text in black"
        title = "d. image showing 3 lines of text: the first one is a red title, and the two other ones are made of text in black"
      >
      e. <img style="margin: 0.1em;" width=200
        src   = "img/4.5.2-img3.jpg"
        alt   = "e. image showing a red big title, below a text highlighted in blue, and below again, a line of text in black"
        title = "e. image showing a red big title, below a text highlighted in blue, and below again, a line of text in black"
      >
    </a>
  </div>

  Ans: b<br>
  Explanation:
    + The JavaScript code associates a shadow root (a shadow DOM) with the host (the `<p id="myWidget">` element). So the text "Injected content" alone is not the correct answer as the content of the shadow DOM (a cloned template) will be rendered.
    + Let's look at the CSS styles. The H1 will be red, for sure. The injected span belongs to the main page, it's just "moved inside the shadow DOM" but will not belong to it. So the global style on spans will apply and it will be green. The other span is defined in the template but there is an internal CSS rule that applies to templates: only CSS rules defined in the template will target elements inside the shadow DOM. In this case this rule will apply to all spans in the shadow DOM of the host and the span will have a light blue background color.
    + Check with [this JsBin](https://jsbin.com/sirepaq/edit).
    + [Local Demo](src/04e-example01.html)


__Additional code for the next question (17)__

<div><ol>
<li value="1">&lt;template id="mytemplate"&gt;</li>
<li>&nbsp; &lt;style&gt;</li>
<li>&nbsp; &nbsp; <strong style="color: #AA0000;">:</strong><strong style="color: #AA0000;">host(:hover){</strong></li>
<li><strong style="color: #AA0000;">&nbsp; &nbsp; &nbsp; background-color:pink;</strong></li>
<li><strong style="color: #AA0000;">&nbsp; &nbsp; }</strong></li>
<li>&nbsp; &nbsp; h1 {</li>
<li>&nbsp; &nbsp; &nbsp; color:red;</li>
<li>&nbsp; &nbsp; }</li>
<li>&nbsp; &nbsp; span {</li>
<li>&nbsp; &nbsp; &nbsp; background-color:lightblue; </li>
<li>&nbsp; &nbsp; }</li>
<li> &lt;/style&gt;</li>
<li>...</li>
<li>&lt;/template&gt;</li>
</ol></div>

17. Pink fairies ...

  From the additional code above, a CSS rule in the template code changes the background color to pink whenever the mouse cursor hovers over selected elements...

  What will this do when we roll the mouse over `<p id='myWidget'>`?

  a. It will only change the background color of the content in the shadow DOM of the `<p id="myWidget">` element.<br>
  b. It will only change the background color of the content rendered corresponding to `<p id="myWidget">` (shadow DOM + injected content).<br>
  c. It will change the background color of all the text rendered in the page.<br>

  Ans:b<br>
  Explanation: 
    + All the text rendered for `<p id='myWidget'>` (the shadow host) will react to the mouse hover event and you will see its background color changed to pink. Try out [this JsBin](https://jsbin.com/kiluris/edit?html). The rest of the page (the H1 and the P after `<p id='myWidget'>`) remains unchanged.
    + [Local Demo](src/04e-example02.html)


### 4.5.5 Custom elements and importing WebComponents (18-20)

18. Give me a name!

  Do custom elements extend other HTML elements (or more precisely, extend the generic element type called HTMLElement)? (Yes/No)

  Ans: Yes<br>
  Explanation: In JavaScript, to create element A that extends element B, element A must inherit the prototype of element B. By default, custom elements inherit from `HTMLElement`. But you can also inherit from pre-existing elements, for example from `HTMLButton`.


19. Custom elements

  In this code : `customElements.define('my-widget', MyWidget);`, what is the second parameter?

  a. The host element<br>
  b. A JavaScript class<br>
  c. A template<br>

  Ans: b<br>
  Explanation: The second parameter is a JavaScript class object that defines the behavior of the element.


20. Are HTML imports obsolete?

  How do you import Web Components into a Web page or a Web application?

  a. Using JavaScript module import (typically `<script type="module" src="./mycomponent/index.js"></script>`)<br>
  b. Using HTML imports (typically `<link rel="import" href="myComponent/index.html">`)<br>

  Ans: <font style="color: red;">a</font>, xb<br>
  Explanation: HTML imports was intended to be the packaging mechanism for Web components. Now, the preferred way is to use JavaScript modules.


### 4.5.6 Orientation and Motion APIs (21-26)

__Source code for the next 4 questions (21, 22, 23 and 24)__

<div><ol>
<li value="1">...</li>
<li> &lt;h2&gt;Device Orientation with HTML5&lt;/h2&gt;</li>
<li>You need to be on a mobile device or use a laptop with </li>
<li>accelerometer/orientation&nbsp;device.</li>
<li> &lt;p&gt;</li>
<li> &lt;div id="LR"&gt;&lt;/div&gt;</li>
<li> &lt;div id="FB"&gt;&lt;/div&gt;</li>
<li> &lt;div id="DIR"&gt;&lt;/div&gt;</li>
<li> &lt;script type="text/javascript"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;if (window.DeviceOrientationEvent) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log("DeviceOrientation is supported");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;window.addEventListener(<span style="color: #ff0000;"><strong style="color: #AA0000;"><span style="color: #008800;">XXX</strong>, function(eventData) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// front/back inclination</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var FB = eventData.<strong style="color: #AA0000;">ZZZ</strong>;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// orientation</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var DIR = eventData.<strong style="color: #AA0000;">TTT</strong>;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// left/right inclination</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var LR = eventData.<strong style="color: #AA0000;">YYY</strong>;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// display values on screen</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;deviceOrientationHandler(FB, DIR,&nbsp;LR);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}, false);</li>
<li>&nbsp; } else {</li>
<li>&nbsp; &nbsp; &nbsp; alert("Device orientation not supported on your device or browser. Sorry.");</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;function deviceOrientationHandler(FB, DIR,&nbsp;LR) {</li>
<li>&nbsp; &nbsp; document.querySelector("#LR").innerHTML &nbsp;<span style="color: #666600;" color="#666600">=&nbsp;"" + Math.round(LR);</li>
<li>&nbsp; &nbsp; document.querySelector("#FB").innerHTML &nbsp;= "" + Math.round(FB);</li>
<li>&nbsp; &nbsp; document.querySelector("#DIR").innerHTML = "" + Math.round(DIR);</li>
<li>&nbsp;&nbsp;}</li>
<li> &lt;/script&gt;</li>
</ol></div>

21. What is it called... I can't remember...

  We would like to display a smartphone's angles of orientation.

  What is the name of the event we must to listen for? What would you enter instead of the XXX placeholder in the above code?

  Ans: `deviceotientation`<br>
  Explanation: The correct name is `deviceorientation`


22. Sometimes I feel like a....

  We would like to display a smartphone's angles of orientation.

  What is the name of the property for the front/back angle? What would you put instead of the ZZZ placeholder in the above code?

  Ans: `beta`<br>
  Explanation: The correct name is `beta`.


23. Left or right?

  We would like to display a smartphone's angles of orientation.

  What is the name of the property for the left/right angle? What would you put instead of the YYY placeholder in the above code?

  Ans: `gamma`<br>
  Explanation: The correct name is `gamma`.


24. Give me the orientation!

  We would like to display a smartphone's angles of orientation.

  What is the name of the property for the horizontal orientation angle? What would you put instead of the TTT placeholder in the above code?

  Ans:`alpha`<br>
  Explanation: The correct name is `alpha`.


25. Degrees or radians?

  Returned angles are in?

  a. Degrees<br>
  b. Radians<br>

  Ans: a<br>
  Explanation: The returned angles are the diffence between normal and current orientation, in degrees.


26. Motion or orientation, make a choice!

  What is the difference between the Device Motion API and the Orientation API?

  a. The Orientation API is the only one that can tell if the device is oriented to the sky.<br>
  b. The DeviceMotion API deals with accelerations as well as orientations.<br>
  c. One works only when the device is stable, the other one when it's in motion.<br>

  Ans: b<br>
  Explanation: The deviceMotion API deals with accelerations as well as orientations. It can also be used to tell if the device is oriented to the sky.


### 4.5.7 Potpourri of questions (27-37)

27. HTML track or TextTrack?

  ```js
      <video id="myVideo" ...>
    <source ...>
    <track ...>
    <track ...>
  </video>

  // method 1
  var videoElement = document.querySelector("#myVideo");

  var textTracks = videoElement.textTracks; // one TextTrack for each HTML track element
  // get the TextTrack property of the first HTML track element
  var textTrack = textTracks[0]; // corresponds to the first track element

  // method 2
  var htmlTracks = document.querySelectorAll("track");
  
  // The TextTrack object associated with the first HTML track
  var textTrack = htmlTracks[0].track;
  ```

  Can we do the same things with the `<track>` HTML element as we can with the textTrack property/object we get from the JavaScript API? (Yea/No)

  Ans: No<br>
  Explanation: 
    + No, the TextTrack object you can get from the HTML track or from the video is NOT the same element/object/node as the HTML track object.
    + The `<track>` and the var you can get with a `document.getElementById(...)` represent the same DOM element. Using this "DOM/HTML view" of the track you can check if it's been loaded, get the attribute values, etc. But you cannot read the track content or change its mode and force it to load. For this you must use the "twin brother" `textTrack` property from the html track (`track.textTrack`) or from the video DOM element (`video.tracks` is a collection of these `TextTrack` objects). This `TextTrack` is not a DOM node and is not the HTML track element.


28. Hidden but alive?

  If a track has been loaded and the corresponding TextTrack mode property set to "hidden", will track and cue events be fired when the video is played (assume that the browser supports cue and track events)? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, a hidden track will not be displayed, but unlike tracks with mode=disabled, it will fire events.


29. Stream or not?

  Can Web Audio work with both streamed sounds and sound samples loaded in memory? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, with Web Audio, you can load sound samples in memory and process them in real time (filter, pitch, etc), and you can do the same with a stream coming from an audio or video element.


30. Fire and forget

  Once played, can a `BufferSource` node (corresponding to a sound sample loaded in memory) be played again without re-creating it? (Yes/No)

  Ans: No<br>
  Explanation: No, `BufferSource` nodes can only be played once. After that, you must re-create them. This fire-and-forget philosophy may seem bizarre but the API is highly optimized for it.


31. Visualizer node

  What is the name of the Web Audio node useful for retrieving frequency domain and time domain analysis data, in order to display a waveform or frequencies that dance with the music?

  a. A canvas node<br>
  b. An analyser node<br>
  c. A waveform node<br>
  d. An FFT node<br>

  Ans: b<br>
  Explanation: The analyser node is useful for retrieving frequency domain and time domain analysis data.


32. Why did we use a Black Box model?

  Why is it 'good practice' to use a Black Box model for the game framework?

  a. It allows us to have private and public properties and methods, which is good for encapsulation.<br>
  b. It's the best approach when we need to split the project into separate files<br>
  c. It gives better performance<br>

  Ans: a<br>
  Explanation:
    + It allows us to have private and public properties methods, this is good for encapsulation.
    + When we do: `var game = new GF(); game.start();`, start is a method from the API we defined. We cannot call `game.mainloop` or use `game.monster`. `mainloop` and monster are "private" objects/methods and may only be used from inside the game framework.


33. Time based animation... again!

  ```js
  requestAnimationFrame(callback);
  ```

  What is the relationship between time based animation and `requestAnimationFrame`?

  a. The callback function has a parameter that is a hi-res timer passed by the browser, and we use it to measure deltas of time for time-based animation.<br/>
  b. The callback function runs at a perfect 60 frames per second rate, so the time between two executions of the callback is exactly 1/60th of a second. We use this value (16.66ms) for time-based animation.<br>

  Ans: a<br>
  Explanation: The hi-res time parameter passed to the callback function is important as we cannot know the exact time elapsed since the last frame of animation. Time-based animation uses this hi-res time to compute deltas.


34. Game hero (bonus question, infinite attempts)

  A Christmas game was developed by students during a previous run of this course. It uses an animal as the main character. What animal is it? (Haven't you tried this game yet? [Check it now!](https://mainline.i3s.unice.fr/mooc/SkywardBound))

  a. A reindeer<br>
  b. A rabbit<br>
  c. A cat<br>
  d. A llama<br>

  Ans: b<br>
  Explanation: It's a green bunny that can fly!!


35. Selected text is a pain (or is plain) text!

  Drag and drop a selection of text...

  a. is possible (without doing anything special for the drag, just manage the drop in a drop handler)<br>
  b. is not possible<br>
  c. is possible, but we must enclose the text with ...<br>

  Ans: <font style="color: red;">a</font>, xc<br>
  Explanation: Selected text is automatically copied to the drag and drop clipboard. Nothing special is required. In the drop handler, just do `event.dataTransfert.getData("text/plain");` to retrieve the selected text.


<hr>

__Source code for the next question (36)__

<div><ol>
<li value="1">var t0 = null, t1 = null, r = null;</li>
<li> </li>
<li>function downloadSoundFile(url) {</li>
<li>&nbsp; &nbsp;var xhr = new XMLHttpRequest();</li>
<li>&nbsp; &nbsp;xhr.open('GET', url, true);</li>
<li>&nbsp; &nbsp;xhr.responseType = 'arraybuffer'; // THIS IS NEW WITH HTML5!</li>
<li> </li>
<li>&nbsp; &nbsp;xhr.onloadstart = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; console.log("download started");</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: #aa0000;"> t0 </strong><strong style="color: #aa0000;">= performance.now();</strong></li>
<li>&nbsp; &nbsp;};</li>
<li> </li>
<li>&nbsp; &nbsp;xhr.onload = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; console.log("Download complete");</li>
<li>&nbsp; &nbsp;};</li>
<li> </li>
<li>&nbsp; &nbsp;xhr.onprogress = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var bytes = e.loaded;</li>
<li>&nbsp; &nbsp; &nbsp; <strong style="color: #aa0000;">t1 </strong><strong style="color: #aa0000;">= performance.now();</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: #aa0000;"> r </strong><strong style="color: #aa0000;">= bytes / (t1 -t0);</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong style="color: #aa0000;">console</strong><strong style="color: #aa0000;">.log("value = " + r);</strong></li>
<li>&nbsp;&nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp;xhr.onerror = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; console.log("error downloading file");</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;xhr.send();</li>
<li>&nbsp; &nbsp;console.log("Ajax request sent... wait until it downloads completely");</li>
<li>} </li>
</ol></div>

36. Now, now, now. We need `performance.now()`!

  What does _line 21_ display?

  a. It displays the current download speed.<br/>
  b. It displays how long the download is taking.<br/>

  Ans: a<br>
  Explanation: Indeed, it displays the current download speed!


37. Index or KeyPath?

  With indexedDB, what is the difference between a KeyPath and an index?

  a. We can have multiple objects with the same index value. This not possible with KeyPaths, which must be unique<br>
  b. No difference: a KeyPath is an index<br>

  Ans: a<br>
  Explanation: Multiple indexes are possible (during the creation of an index we can indicate if its values must be unique or if multiple indexes with the same value will be allowed). KeyPaths must be unique, they are like primary keys in relational databases.


