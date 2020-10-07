# Week 4: HTML5 Animations


## 4.3 Canvas and user interaction


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


__Third way: register a callback to the event listener with the addEventListener method__

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

  Ans: 
