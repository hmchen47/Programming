# Week 4: HTML5 Animations


## 4.3 Canvas and user interaction


### 4.3.0 Lecture Notes

+ [DOM events](#431-events-input-and-output)
  + use the DOM JavaScript API to create event handlers
  + js: events made by users as an input and manipulating the DOM structure as an output
  + games/animations:
    + input: change state variables of moving objects
    + output: animation loop taking care of these variables to move the objects
  + ways to manage events in the DOM structure
    + declare event handlers in the HTML code
      + e.g., <prep><div id="someDiv" <strong>onclick="alert('clicked!')</strong>;"></prep>
      + not the recommended way to handle events
      + mixing the 'visual layer' (HTML) and the 'logic layer' (JavaScript) in one place
      + not the recommended way for full scale applications where a clean separation is the best
    + add an event handler to an HTML element in JavaScript
      + e.g., `document.getElementById('someDiv').onclick = function(evt) { alert('clicked!'); }`
      + unable to attach several listener functions
    + register a callback to the event listener with the `addEventListener` method
      + e.g.,: `document.getElementById('someDiv').addEventListener('click', function(evt) { alert('clicked!'); }, false);`
      + third parameter not important for now, just set it to false or ignore
  + DOM event and event listener function
    + create an EventListener and attach it to an element
    + an event object passed as a parameter to the callback
    + example:

      ```js
      element.addEventListener('click', function(event) {
        // now you can use the event object inside the callback
      }, false);
      ```

    + use different properties from the event object in order to get useful information



### 4.3.1 Events: input and output

In JavaScript, we treat events made by users as an input, and we manipulate the DOM structure as an output. Most of the time in games/animations, we will change state variables of moving objects, such as position or speed of an alien ship, and the animation loop will take care of these variables to move the objects.

The events are called DOM events, and we use the _DOM JavaScript API_ to create _event handlers_.


#### There are three ways to manage events in the DOM structure

__First way: declare event handlers in the HTML code__

You will often find this in examples on the Web:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"someDiv"</span><span class="pln"> </span><strong><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">alert</span><span class="pun">(</span><span class="str">'clicked!'</span><span class="pun">);</span><span class="atv">"</span></strong><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; content of the div </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/div&gt;</span></li>
</ol></div>

Note: this is not the recommended way to handle events, even if it's very easy to use. Mixing the 'visual layer' (HTML) and the 'logic layer' (JavaScript) in one place is ok for small examples (we have used this in some examples in this course) but is not the recommended way for full scale applications where a clean separation is best.


__Second way: add an event handler to an HTML element in JavaScript__

Here is an example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'someDiv'</span><span class="pun">).</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(evt)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; alert</span><span class="pun">(</span><span class="str">'clicked!'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

This method is fine, but  you will not be able to attach several listener functions. If you need to do this, the preferred version is the next one.


__Third way: register a callback to the event listener with the `addEventListener` method__

This is how we do it:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'someDiv'</span><span class="pun">).</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(evt)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">'clicked!'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
</ol></div>

The third parameter is not important for now, just set it to `false`, or simply do not add a third parameter.


#### The DOM event that is passed to the event listener function

When you create an EventListener and attach it to an element,  an event object will be passed as a parameter to your callback, just like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">element</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><strong><span class="kwd">event</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// now you can use the event object inside the callback</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
</ol></div>

Depending on the type of event you are listening to, we will use different properties from the event object in order to get useful information like: "what keys have been pressed down?", "what is the position of the mouse cursor?", "which mouse button is down?", etc.

Let's see next how to deal with the keyboard and the mouse. In the [W3Cx HTML5 Apps and Games](https://www.edx.org/course/html5-apps-and-games) course, we look at additional APIs such as the [gamePad API](https://www.w3.org/TR/gamepad/) for using USB or wireless gamepads/joysticks/game controllers.


#### Knowledge check 4.3.1

Source code for the knowledge check 4.3.1

[Online example on JS Bin](http://jsbin.com/korele/edit)

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Click on button</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myButton"</span><span class="tag">&gt;</span><span class="pln">Click me!</span><span class="tag">&lt;/button&gt;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> button </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myButton'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;<strong>// Define a click listener on the button</strong></span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;button</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> processClick</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// callback</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> processClick</span><span class="pun">(</span><strong><span class="pln">event</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Button clicked"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><strong><span class="com">// What is the event parameter?</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


1. When you create an event listener like in the code above, what is the event parameter (line 15) passed to the callback function useful for?

  a. It will hold relevant data about the interaction (element that fired the event, key code, mouse button and position of the mouse cursor, etc.)<br/>
  b. It's not useful, it's just here for debug purposes.<br/>

  Ans: a<br/>
  Explanation: The event is useful for getting information about what fired the event, button, mouse, etc... The data it holds depends on the type of the event. This [example shows how we can get the id of the button that has been clicked and the value of the button label](https://jsbin.com/ruzofa/edit).



### 4.3.2 Keyboard interaction, key events

This has been a bit of a nightmare for years, as different browsers have had different ways of handling key events and key codes (read [this article](https://unixpapa.com/js/key.html) if you are fond of JavaScript archeology). Fortunately it's much better today, and we are able to rely on methods that should work on any browser.

When you listen to keyboard related events (`keydown`, `keyup` or `keypressed`), the event parameter passed to the listener function will contain the code of the key that fired the event. Then it is possible to test what key has been pressed or released, like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><strong><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">//left arrow was pressed</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
</ol></div>

At line 2, the value "37" is the key code that corresponds to the left arrow. It might be difficult to know the correspondences between real keyboard keys and codes, so here are handy pointers:

+ Try key codes with this [interactive test page](http://www.asquare.net/javascript/tests/KeyCode.html).
+ And find a list of keyCodes below (taken from this [CSS Tricks article](https://css-tricks.com/snippets/javascript/javascript-keycodes/)):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y333tfjx')"
    src    ="https://tinyurl.com/y5y53a2e"
    alt    ="JavaScript keycode table. This is a screenshot of the HTML table presented in https://css-tricks.com/snippets/javascript/javascript-keycodes/#keycode-values"
    title  ="JavaScript keycode table. This is a screenshot of the HTML table presented in https://css-tricks.com/snippets/javascript/javascript-keycodes/#keycode-values"
  />
</figure>



#### Examples

Example #1: adding a key listener to the window object
A lot of people think that the canvas element is not able to get key events. Many examples on the Web handle key events on canvas by adding a listener to the window object directly, like this:

[Online example](https://jsbin.com/boqumo/1/edit?html,output):  ([Local Example - Key Listener](src/4.3.2-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yx9ukm7g')"
    src    ="https://tinyurl.com/y572v8ul"
    alt    ="key detected"
    title  ="key detected"
  />
</figure>


Extract from source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"350"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"200"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/canvas&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// This will work when you press a key, anywhere on the document</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>window</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> handleKeydown</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> handleKeydown</span><span class="pun">(</span><span class="pln">e</span><span class="pun">){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">'keycode: '</span><span class="pun">+</span><span class="pln">e</span><span class="pun">.</span><span class="pln">keyCode</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
</ol></div>

Indeed this solution works well if you write a game, and want to detect events wherever the mouse cursor is, and without worrying about what HTML element has the focus, etc...


__Move the monster with the keyboard__

[Online example at JS Bin](https://jsbin.com/galebil/1/edit?html,output): ([Local Example - Move w/ Keyboard](src/4.3.2-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yx9ukm7g')"
    src    ="https://tinyurl.com/yx8zot2n"
    alt    ="monster moving with jeys"
    title  ="monster moving with jeys"
  />
</figure>


Extract from source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><strong><span class="pln"> monsterX</span><span class="pun">=</span><span class="lit">100</span></strong><span class="pun">,</span><span class="pln"> monsterY</span><span class="pun">=</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> monsterAngle</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><strong><span class="pln"> incrementX </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span></strong><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// This function is called after the page is loaded</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 1 - Get the canvas</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 2 - Get the context</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// 3 add key listeners to the window element</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>window</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> handleKeydown</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>window</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keyup'</span><span class="pun">,</span><span class="pln"> handleKeyup</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 4 - start the animation</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><strong><span class="pln"> handleKeydown</span><span class="pun">(evt</span><span class="pun">)</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><strong><span class="pln">evt</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="com">//left key </span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong>incrementX </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><strong><span class="pln">evt</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">39</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="com">// right key</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong>incrementX </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><strong><span class="pln"> handleKeyup</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>incrementX </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> animationLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 1 - Clear</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 2 Draw</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawMonster</span><span class="pun">(</span><span class="pln">monsterX</span><span class="pun">,</span><span class="pln"> monsterY</span><span class="pun">,</span><span class="pln"> monsterAngle</span><span class="pun">,</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'yellow'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// 3 Move</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>monsterX </strong></span><strong><span class="pun">+=</span><span class="pln"> incrementX</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// call again mainloop after 16.6 ms (60 frames/s)</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
</ol></div>


__Example #2: what if I want to listen to key events only in my canvas?__

If you add a key listener to a canvas element, the problem is that it will get events only when it has the focus. And by default, it will never have the focus!

The `tabindex` attribute of the canvas element makes it focusable. Without it, it will never get the focus!

The trick is to declare the canvas like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"350"</span><span class="pln"> </span><strong><span class="atn">tabindex</span><span class="pun">=</span><span class="atv">"1"</span></strong><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"200"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/canvas&gt;</span></li>
</ol></div>

And we force the canvas to get the focus with:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">canvas</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">canvas</span><span class="pun">.</span><span class="pln">focus</span><span class="pun">();</span></strong></li>
</ol></div>

Now, if we try an example with the above canvas declaration, we show when an HTML element has the focus: a border is added to it, as shown in this [JSBin code](https://jsbin.com/hobuni/1/edit?html,output). ([Local Example - Add Border](src/4.3.2-example3.html))

Note that the line that forces the focus to the canvas is commented by default. Try to click on the canvas, then press a key, then click out of the canvas, then press a key: this time nothing happens!

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yx9ukm7g')"
    src    ="https://tinyurl.com/y52m7baf"
    alt    ="a border appears when the canvas has the focus"
    title  ="a border appears when the canvas has the focus"
  />
</figure>


Extract from the code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;canvas</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// This will work only if the canvas has the focus </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> handleKeydown</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="com">// We can set the focus on the canvas like this:</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="com">//canvas.focus();</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// ... but it will stop working if we click somewhere else</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// in the document</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> handleKeydown</span><span class="pun">(</span><span class="pln">e</span><span class="pun">){</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'keycode: '</span><span class="pun">+</span><span class="pln">e</span><span class="pun">.</span><span class="pln">keyCode</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div>

Line 10 is useful to initially set the focus on the canvas, but this trick will not work if we click somewhere else in the HTML page.

__Example #3: a better way: set the focus when the mouse cursor enters the canvas__

A better way to manage key events on a canvas is to set the focus when the mouse is over the canvas, and to un-focus it otherwise.

Here is a modified version of the "move monster example" seen earlier. This time, you move the monster with the left and right arrow only when the mouse cursor is over the canvas. We added two mouse event listeners on the canvas: one for the `mouseenter` event and the other for the `mouseout` event.

When the mouse enters the canvas we call `canvas.focus()` to set the focus to the canvas, and when the mouse cursor goes out of the canvas, we call `canvas.blur()` to unset the focus.

[Online example at JS Bin](https://jsbin.com/koboniz/1/edit?html,output) ([Local Example - Mouse Hoover](src/4.3.2-example4.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yx9ukm7g')"
    src    ="https://tinyurl.com/y4ha3n96"
    alt    ="canvas gets focus only when mouse is over it..."
    title  ="canvas gets focus only when mouse is over it..."
  />
</figure>


Extract from the code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// This function is called after the page is loaded</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 1 - Get the canvas</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 2 - Get the context</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 3 - Add key listeners to the window element</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> handleKeydown</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keyup'</span><span class="pun">,</span><span class="pln"> handleKeyup</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mouseenter'</span><span class="pun">,</span><span class="pln"> setFocus</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mouseout'</span><span class="pun">,</span><span class="pln"> unsetFocus</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 4 - Start the animation</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> setFocus</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">focus</span><span class="pun">();</span></strong><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> unsetFocus</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">blur</span><span class="pun">();</span></strong><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pun">&nbsp; </span><span class="pun">&nbsp;</span><span style="color: #222222; font-family: 'Open Sans', Verdana, Geneva, sans-serif, sans-serif; font-size: 14px; line-height: 20.72px;">incrementX = 0; // stop the monster if the mouse exists the canvas</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div>

The third parameter (false) of _lines 12_ and _13_ means "we do not want to propagate the event to the ancestors of the canvas in the DOM." 


#### Knowledge check 4.3.2

1. Suppose we have defined a key event listener to a canvas: should this canvas have the focus in order to fire key events? (Yes/No)

  Ans: 








