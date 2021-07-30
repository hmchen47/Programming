# Module 4: Web components and other HTML5 APIs section


## 4.3 Web Workers


### 4.3.1 Introduction

In the browser, 'normal' JavaScript code is run in a single thread (a thread is a light-weight CPU process, see [this Wikipedia page for details](https://en.wikipedia.org/wiki/Thread_(computing))). This means that the browser GUI, the JavaScript, and other tasks are competing for processor time. If you run an intensive CPU task, everything else is _blocked_, including the user interface. You have no doubt observed something like this during your Web browsing experiences:

With Internet  (left diagram) Or maybe (right diagram):

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3zNVry0" ismap target="_blank">
    <img style="margin: 0.1em;" height=130
      src   = "https://bit.ly/3iXPDv6"
      alt   = "ScriptNotResponding1"
      title = "ScriptNotResponding1"
    >
    <img style="margin: 0.1em;" height=130
      src   = "https://bit.ly/3rNeCoX"
      alt   = "script not responding2"
      title = "script not responding2"
    >
  </a>
</div>

A solution for this problem, offered by HTML5, is to run certain CPU-intensive tasks in separate threads from the one managing the graphical user interface. So, if you don't want to block the user interface, you can perform computationally intensive tasks in one or more background threads, using the HTML5 Web Workers. Web Workers = CPU threads, in JavaScript.

Terminology check: if the terms background and foreground and the concept of multi-tasking are new to you, please review [PC Mag's definition of foreground and background](https://www.pcmag.com/encyclopedia/term/foregroundbackground).


#### An example that does not use Web Workers

This example will block the user interface unless you close the tab. [Try it at JSBin](https://jsbin.com/qipegi/edit?html,output) but DO NOT CLICK ON THE BUTTON unless you are prepared to kill your browser/tab, because this routine will consume 100% of CPU time, completely blocking the user interface:

[Local Demo](src/04c-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3zNVry0')"
    src    = "https://bit.ly/3l3Tl9f"
    alt    = "Examples that eats all the cpu"
    title  = "Examples that eats all the cpu"
  />
</figure>


Code from the example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE HTML&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Worker example: One-core computation</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"startButton"</span><span class="tag">&gt;</span><span class="pln">Click to start discovering prime numbers</span><span class="tag">&lt;/button&gt;&lt;p&gt;</span><span class="pln">&nbsp;Note that this will make the page unresponsive, you will have to close the tab in order to get back your CPU!</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">The highest prime number discovered so far is: </span><span class="tag">&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"result"</span><span class="tag">&gt;&lt;/output&gt;&lt;/p&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">function</span><span class="pln"> computePrime</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> n </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; search</span><span class="pun">:</span><span class="pln"> </span><span style="color: #ff0000;"><strong><span class="kwd">while</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">true</span><span class="pun">)</span></strong></span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; n </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sqrt</span><span class="pun">(</span><span class="pln">n</span><span class="pun">);</span><span class="pln"> i </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">n </span><span class="pun">%</span><span class="pln"> i </span><span class="pun">==</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">continue</span><span class="pln"> search</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// found a prime!</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'result'</span><span class="pun">).</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> n</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#startButton"</span><span class="pun">).</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> computePrime</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

Notice the infinite loop in the function `computePrime` (_line 12_, in bold). This is guaranteed to block the user interface. If you are brave enough to click on the button that calls the `computePrime()` function, you will notice that the line 18 execution (that should normally modify the DOM of the page and display the prime number that has been found) does nothing visible. The UI is unresponsive. _This is **really, really, bad** JavaScript programming - and should be **avoided** at all costs._

Shortly we will see a "good version" of this example that uses Web Workers.

Thread safety problems? Not with Web Workers!

When programming with multiple threads, a common problem is "thread safety". This is related to the fact that several concurrent tasks may share the same resources (eg JavaScript variables) at the same time. If one task is modifying the value of a variable while another one is reading it, this may result in some strange behavior. Imagine that thread number 1 is changing the first bytes of a 4 byte variable, and thread number 2 is reading it at the same time: the read value will be wrong (1st byte that has been modified + 3 bytes not yet modified).

With `Web Workers`, the carefully controlled communication points with other threads mean that it's actually very hard to cause concurrency problems. There's no access in a worker to non-thread safe components or to the DOM. We must to pass specific data into and out of a thread through serialized objects. The separate threads _share different copies_ so the problem with the four bytes variable, explained in the previous paragraph, cannot occur.


#### Different kinds of Web Workers

There are two different kinds of Web Workers described in the specification:

1. __Dedicated Web Workers:__ threads that are dedicated to one single page/tab. Imagine a page with a given URL that runs a Web Worker that counts in the background 1-2-3- etc.  It will be duplicated if you open the same URL in two different tabs. So each independent thread will start counting from 1 at startup time (when the tab/page is loaded).
2. __Shared Web Workers:__ these are threads which may be shared between different pages of tabs (they must conform to the same-origin policy) on the same client/browser. These threads will be able to communicate, exchange messages, etc. For example, a shared worker, that counts in the background 1-2-3- etc. and communicates its current value.  All the pages/tabs which share its communication channel  will display the same value! Also, if you refresh each of those pages, they will return displaying the same value as each other. The pages don't need to be the same (with the same URL). However, they must conform to the "same origin" policy.

<font style="color: red;">Shared Web Workers are not studied in this course.</font> They are not yet supported by major browser vendors, and a proper study would require a whole module's worth of material. We may cover this topic in a future version of this course when implementations are more stable/available.


#### External resources:

+ [W3C specification about Web Workers](https://www.w3.org/TR/workers/)
+ [Web Workers concepts and usage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) (from MDN's documentation)
+ [Using Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) (from MDN's documentation)
+ Browser support:
  + [Web Workers' feature on CanIUse](https://caniuse.com/#feat=webworkers)
  + [Shared Web Workers on CanIUse](https://caniuse.com/#feat=sharedworkers) (not studied)


#### Notes for 4.3.1 Introduction

+ Threads in browser
  + normal JS code: a single thread
  + competing for processor time: the browser GUI, the JavaScript, and other tasks
  + intensive CPU task $\implies$ everything else blocked
  + solution:
    + running certain CPU-intensive tasks in separate threads from the one managing the graphical user interface
    + performing computationally intensive tasks in one or mroe background threads
    + using the HTML Web Workers
    + Web Workers = CPU threads, in JavaScript

+ Example: intensive task w/o Web Workers - bad JS programming
  + compute Prime: `function computePrime() {...}`
  + init iterative variable: `var n =1;`
  + loop to get  (infinite loop): `search: while (true) {...}`
    + increase iterative variable: `n += 1;`
    + iterate to check prime number: `for (var i=2; i<=Math.sqrt(n); i+=1) {if (n%i ==0) continue search; }`
    + display the prime number: `document.getElementById('result').textContent = n;`
  + add button click handler: `document.querySelector("#startButton").addEventListener('click', computePrime);`

+ Thread safety
  + a common problem when programming w/ multiple threads
  + several concurrent tasks share the same resources at the same time
  + modifying the value pf a variable while another one is reading it $\to$ probably result in some strange behavior
  + solution: Web Worker
    + carefully controlled communication points w/ other threads
    + very hard to cause concurrency problems
    + no access in worker to non-thread safe components or to the DOM
    + passing specific data into and out of a thread through serialized objects
    + the separate threads share different copies

+ Types of web workers
  + dedicated Web Works
    + threads dedicated to one single page/tab
    + example
      + a page w/ a given URL running a Web Worker that counts in the background 1-2-3-etc.
      + duplicated the Web Worker if opening the same URL in two different tabs
      + each independent thread starts counting from 1 at startup time
  + shared Web Worker
    + threads probably shared btw different pages of tabs on the same client/browser
    + theads able to communicate, exchange message, etc.
    + example:
      + a shared worker counting in the back grpound 1-2-3- etc.
      + communicating its current value
    + all the pages/tabs sharing its communication channel $\to$ display the same value
    + refreshing each of the pages $\to$ displaying the same value as each other
    + conforing to the "same-origin" policy
    + not supported by major browsers


### 4.3.2 Use cases

#### Creating workers from script

__Use case #1: a "parent HTML5 page" creates workers from a script__

The HTML5 Web Worker API provides the Worker JavaScript interface for loading and executing a script in the background, in a different thread from the UI. The following instruction  loads and creates a worker:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> worker </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Worker</span><span class="pun">(</span><span class="str">"worker0.js"</span><span class="pun">);</span></li>
</ol></div>

More than one worker can be created/loaded by a parent page. This is parallel computing after all :-)


#### Using messages to manage a worker

__Use case #2: you manage a worker by communicating with it using "messages"__

Messages can be strings or objects, as long as they can be serialized in JSON format (this is the case for most JavaScript objects, and is handled by the Web Worker implementation of recent browser versions).

Terminology check: serialized

(1) Messages can be sent by the parent page to a worker using this kind of code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> worker </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Worker</span><span class="pun">(</span><span class="str">"worker0.js"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// String message example</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">worker</span><span class="pun">.</span><span class="pln">postMessage</span><span class="pun">(</span><span class="str">"Hello"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// Object message example</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> personObject </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="str">'firstName'</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'lastName'</span><span class="pun">:</span><span class="str">'Buffa'</span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">worker</span><span class="pun">.</span><span class="pln">postMessage</span><span class="pun">(</span><span class="pln">personObject </span><span class="pun">);</span></li>
</ol></div>


(2) Messages (like the object message example, above) are received from a worker using this method (code located in the JavaScript file of the worker):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">onmessage </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// do something with event.data</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; alert</span><span class="pun">(</span><span class="str">'received '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">data</span><span class="pun">.</span><span class="pln">firstName</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div>

(3) The worker will then send messages back to the parent page (code located in the JavaScript file of the worker):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">postMessage</span><span class="pun">(</span><span class="str">"Message from a worker !"</span><span class="pun">);</span></li>
</ol></div>

(4) And the parent page can listen to messages from a worker like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">worker.onmessage </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="com">// do something with event.data</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div>


#### Complete example

__Use case #3: a complete example__

The "Parent HTML page" of a simplistic example using a dedicated Web Worker:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE HTML&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Worker example: One-core computation</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">The most simple example of Web Workers</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">// create a new worker (a thread that will be run in the background)</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> worker </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Worker</span><span class="pun">(</span><span class="str">"worker0.js"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">// Watch for messages from the worker</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; worker</span><span class="pun">.</span><span class="pln">onmessage </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Do something with the message from the client: e.data</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">"Got message that the background work is finished..."</span><span class="pun">)</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Send a message to the worker</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;worker</span><span class="pun">.</span><span class="pln">postMessage</span><span class="pun">(</span><span class="str">"start"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

The JavaScript code of the worker (worker0.js):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">onmessage </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">data </span><span class="pun">===</span><span class="pln"> </span><span class="str">"start"</span><span class="pln"> </span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// Do some computation that can last a few seconds...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// alert the creator of the thread that the job is finished</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">done</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> </span><span class="kwd">done</span><span class="pun">(){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="com">// Send back the results to the parent page</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; postMessage</span><span class="pun">(</span><span class="str">"done"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Error handling

__Use case #4: handling errors__

The parent page can handle errors that may occur inside its workers, by listening for an `onError` event from a worker object:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> worker </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Worker</span><span class="pun">(</span><span class="str">'worker.js'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> worker</span><span class="pun">.</span><span class="pln">onmessage </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="com">// do something with event.data</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> worker</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">message</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

See also the section "how to debug Web Workers" on next page.

#### Notes for 4.3.2 Use cases


+ Creating workers from script
  + HTML5 Web Worker API: providing the Worker JS interface for loading and executing a script in the background, in different thread from the UI
  + syntax: `var worker = new Worker("worker0.js");`
  + more than one worker probably created/loaded by a parenet page

+ Using "messages" to manage a worker
  + messages: strings or object
  + possibly serialized in JSON format, most used JS object
  + procedure of serialized:
    + messages sent by the parent page to a worker
      + create worker: `var worker = new Worker("worker0.js");`
      + set string message: `worker.postMessage("Hello");`
      + declare object: `var personObj = {'firstName': 'Michel', 'lastName': 'Buffa'};`
      + set message: `worker.postMessage(personObj);`
    + message received from a worker using this method - add message handler: `onmessage = function(evt) { // do sth. w/ evt.data; alert('received ' + evt.data.firstName); };`
    + worker sending message back to the parent page: `postMessage("Message from a worker!");`
    + the parent page able to listen to messages from a work: `worker.onmessage = function(evt) { // do sth. w/ evt.data };`

+ Example: web workers
  + Parent HTML page - body part
    + paragraph: `<p>The most simple example of Web Workers</p>`
    + embedded script: `<script> ...</script>`
      + create worker: `var worker = new Worker("worker0.js");`
      + watch for messages from the worker: `worker.onmessage = function(e) { // do sth. w/ the msg from the client, e.data; alert("Got message that the background work is finished...") };`
      + send a message to the worker: `worker.postMessage("start");`
  + JavaScript snippet of the worker: `worker0.js`
    + add message handler: `onmessage = function(e) { if (e.data === "start") { // do some computation and alert the creator of the thread that the job is finished; done(); } };`
    + send back the results to the parent page: `function done() { postMessage("done"); }`

+ Example: handling error
  + create worker: `var worker = new Worker('work.js');`
  + add message handler: `worker.onmessage = function(evt) { // do sth w/ evt.data };`
  + add error handler: `worker.onerror = fucntion(evt) { console.log(evt.message, evt); }`


### 4.3.3 Examples

Dedicated Workers are the simplest kind of Workers. Once created, they remain linked to their parent page (the HTML5 page that created them). An implicit "communication channel" is opened between the Workers and the parent page, so that messages can be exchanged.


#### Background task with user interface responsive

__Example #1: compute prime numbers in the background while keeping the page user interface responsive__

Let's look at [the first example, taken from the W3C specification](https://www.w3.org/TR/workers/#examples): 
> "The simplest use of workers is for performing a computationally expensive task without interrupting the user interface. In this example, the main document spawns a worker to (naïvely) compute prime numbers, and progressively displays the most recently found prime number."

This is the example we tried earlier, without Web Workers, and it froze the page. This time, we'll use a Web Worker. Now you will notice that the prime numbers it computes in the background are displayed as soon as the next prime number is found.

[Try this example online using CodePen](https://codepen.io/w3devcampus/project/editor/ZynNvX/). Note that we cannot run this example on JsBin as Workers need to be defined in a separate JavaScript file.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3yhfGnl')"
    src    = "https://bit.ly/3j4kjuS"
    alt    = "Prime number computation"
    title  = "Prime number computation"
  />
</figure>


The HTML5 page code from this example that uses a Web Worker:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE HTML&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Worker example: One-core computation</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">The highest prime number discovered so far is: </span><span class="tag">&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"result"</span><span class="tag">&gt;&lt;/output&gt;&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><strong><span class="kwd">var</span><span class="pln"> worker </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Worker</span><span class="pun">(</span><span class="str">'worker.js'</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; <strong>worker</strong></span><strong><span class="pun">.</span><span class="pln">onmessage </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'result'</span><span class="pun">).</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">data</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

__Explanations:__

+ the Web Worker is created at _line 9_
+ its code is in the `worker.js` file
+ _Lines 10-12_ process messages sent asynchronously by the worker
+ `event.data` is the message content.

Workers can only communicate with their parent page using messages. See the code of the worker below to see how the message has been sent.

The code of the worker (`worker.js`):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> n </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">search</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">while</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">true</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; n </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sqrt</span><span class="pun">(</span><span class="pln">n</span><span class="pun">);</span><span class="pln"> i </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">n </span><span class="pun">%</span><span class="pln"> i </span><span class="pun">==</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="kwd">continue</span><span class="pln"> search</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="com">// found a prime!</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;<strong> postMessage</strong></span><strong><span class="pun">(</span><span class="pln">n</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

There are a few interesting things to note here:

There is an infinite loop in the code at line 2 (while true...). This is not a problem as it runs in the background.
When a prime number is found, it is posted to the creator of the Web Worker (aka the parent HTML page), using the postMessage(...) function (line 8).
Computing prime numbers using such a weak algorithm is very CPU intensive. However, the Web page is still responsive: you can refresh it and the "script not responding"  error dialog box will not appear, etc. There is a demo in the next section of this course chapter in which some graphic animation has been added to this example, and you can verify that the animation is not affected by the computations in the background.

__Try an improved version of the first example yourself__

We can improve this example a little by testing whether the browser supports Web Workers, and by displaying some additional messages.

<p style="margin: 10px; padding: 10px; color: red"><strong>CAREFUL</strong>: for security reasons you cannot try the examples using a file:// URL. <strong>You need an HTTP web server that will serve the files</strong>. Here is what happens if you do not follow this constraint:</p>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3yhfGnl')"
    src    = "https://bit.ly/3BZdq6F"
    alt    = "using file URL does not work for security reasons"
    title  = "using file URL does not work for security reasons"
  />
</figure>


This occurs with Opera, Chrome and Firefox. With Chrome, Safari or Chromium, you can run the browser using some command line options to override these security constraints. Read, for example, [this blog post that explains this method in detail](https://suretalent.blogspot.fr/2011/04/javascript-web-workers-local-chrome.html).

Ok, back to our improved version! This time, we test if the browser supports Web Workers, and we also use a modified version of the worker.js code for displaying a message and have it wait 3 seconds before starting the computation of prime numbers.

You can download this example: [WebWorkersExample1.zip](https://bit.ly/2V4hh1u)

HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE HTML&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Worker example: One-core computation</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">The highest prime number discovered so far is: </span><span class="tag">&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"result"</span><span class="tag">&gt;&lt;/output&gt;&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pun">(</span><span class="pln">window</span><span class="pun">.</span><span class="typ">Worker</span><span class="pun">){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// web workers supported by the browser</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> worker</span><span class="pun">=</span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Worker</span><span class="pun">(</span><span class="str">"worker1.js"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; worker</span><span class="pun">.</span><span class="pln">onmessage</span><span class="pun">=</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">event</span><span class="pun">){</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'result'</span><span class="pun">).</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">data</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span><span class="kwd">else</span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// the browser does not support web workers</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert</span><span class="pun">(</span><span class="str">"Sorry, your browser does not support Web Workers"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

_Line 9_ shows how to test if the browser can run JavaScript code that uses the HTML5 Web Workers API.

Here is the `worker1.js` code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">postMessage</span><span class="pun">(</span><span class="str">"Hey, in 3s, I'll start to compute prime numbers..."</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">setTimeout</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="com">// The setTimeout is just useful for displaying the message in line 1 for 3 seconds and</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="com">// making it visible</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> n </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; search</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">while</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">true</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; n </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sqrt</span><span class="pun">(</span><span class="pln">n</span><span class="pun">);</span><span class="pln"> i </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">)</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">n </span><span class="pun">%</span><span class="pln"> i </span><span class="pun">==</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">continue</span><span class="pln"> search</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// found a prime!</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; postMessage</span><span class="pun">(</span><span class="pln">n</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="lit">3000</span><span class="pun">);</span></li>
</ol></div>

In this example, we just added a message that is sent to the "parent page" (_line 1_) and we use the standard JavaScript method `setTimeout()` to delay the beginning of the prime number computation by 3s.


#### Initiate and Kill worker

__Example #2: how to stop/kill a worker after a given amount of time__

So far we have created and used a worker. Now we will see how to kill it!

A worker is a thread, and a thread uses resources. If you no longer need its services, _it is best practice to release the used resources,_ especially since some browsers may run very badly when excessive memory consumption occurs. _Even if we unassign the variable that was used to create the worker, the worker itself continues to live_ - it does not stop! Worse: the worker continues in its task (therefore memory and other resources are still allocated) but it becomes inaccessible. In this situation, we cannot do anything but close the tab/page/browser.

The Web Worker API provides a `terminate()` method that we can use on any worker, to end its life. After a worker has been killed, it is not possible to undo its termination. The only option is to create a new worker.

HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE HTML&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Worker example: One-core computation</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">The highest prime number discovered so far is: </span><span class="tag">&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"result"</span><span class="tag">&gt;&lt;/output&gt;&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pun">(</span><span class="pln">window</span><span class="pun">.</span><span class="typ">Worker</span><span class="pun">){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// web workers supported by the browser</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> worker</span><span class="pun">=</span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Worker</span><span class="pun">(</span><span class="str">"worker2.js"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; worker</span><span class="pun">.</span><span class="pln">onmessage</span><span class="pun">=</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">event</span><span class="pun">){</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'result'</span><span class="pun">).</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">data</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span><span class="kwd">else</span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// the browser does not support web workers</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert</span><span class="pun">(</span><span class="str">"Sorry, your browser does not support Web Workers"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; setTimeout</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// After 10 seconds, we kill the worker</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong> worker</strong></span><strong><span class="pun">.</span><span class="pln">terminate</span><span class="pun">();</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">document</span><span class="pun">.</span><span class="pln">createTextNode</span><span class="pun">(</span><span class="str">"Worker killed, 10 seconds elapsed !"</span><span class="pun">)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pun">);},</span><span class="pln"> </span><span class="lit">10000</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

Notice at _line 22_ the call to `worker.terminate()`, that kills the worker after 10000ms.

`worker2.js` is the same as in the last example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE HTML&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Worker example: One-core computation</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">The highest prime number discovered so far is: </span><span class="tag">&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"result"</span><span class="tag">&gt;&lt;/output&gt;&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pun">(</span><span class="pln">window</span><span class="pun">.</span><span class="typ">Worker</span><span class="pun">){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// web workers supported by the browser</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> worker</span><span class="pun">=</span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Worker</span><span class="pun">(</span><span class="str">"worker2.js"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; worker</span><span class="pun">.</span><span class="pln">onmessage</span><span class="pun">=</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">event</span><span class="pun">){</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'result'</span><span class="pun">).</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">data</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span><span class="kwd">else</span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// the browser does not support web workers</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert</span><span class="pun">(</span><span class="str">"Sorry, your browser does not support Web Workers"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; setTimeout</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// After 10 seconds, we kill the worker</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong> worker</strong></span><strong><span class="pun">.</span><span class="pln">terminate</span><span class="pun">();</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">document</span><span class="pun">.</span><span class="pln">createTextNode</span><span class="pun">(</span><span class="str">"Worker killed, 10 seconds elapsed !"</span><span class="pun">)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pun">);},</span><span class="pln"> </span><span class="lit">10000</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

A Web worker can also kill itself by calling the `close()` method in the worker's JavaScript file:

__To sum up, there are 3 different ways to kill a Web Worker:__

1. Close the tab/window of the parent. This will kill all workers that have been created by this parent tab/window.
2. In the parent's JavaScript file: call the terminate() method on a worker instance. Example: worker.terminate();
3. Call the close() method in a Worker's JavaScript file. This will kill the current Worker that is running this code.

#### Web worker with external scripts

__A web worker can include external scripts__

External scripts can be loaded by workers using the `importScripts()` function.

`worker.js`:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pln">importScripts</span><span class="pun">(</span><span class="str">'script1.js'</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">importScripts</span><span class="pun">(</span><span class="str">'script2.js'</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// Other possible syntax</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">importScripts</span><span class="pun">(</span><span class="str">'script1.js'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'script2.js'</span><span class="pun">);</span></li>
</ol></div>

The included scripts must follow the [same-origin policy](https://mzl.la/2TKMGWh).

The scripts are loaded synchronously and the function `importScripts()` doesn’t return until all the scripts have been loaded and executed. If an error occurs during a script importing process, a `NETWORK_ERROR` is thrown by the `importScripts` function and the code that follows won’t be executed.


#### Limitations of Web Workers

Debugging threads may become a nightmare when working on the same object (see the "thread security" section at the beginning of this page). To avoid such a pain, the Web Workers API does several things:

1. When a message is sent, it is always a copy that is received: no more thread security problems.
2. Only predefined thread-safe objects are available in workers, this is a subset of those usually available in standard JS scripts.

__Objects available in Web Workers:__

+ The `navigator` object
+ The `location` object (read-only)
+ `XMLHttpRequest`
+ `setTimeout()/clearTimeout()` and `setInterval()/clearInterval()`
+ The [Application Cache](https://www.html5rocks.com/tutorials/appcache/beginner/)
+ Importing external scripts using the `importScripts()` method
+ [Spawning other Web Workers](https://bit.ly/3BWcLmp)

__Workers do NOT have access to:__

+ The DOM (it's not thread-safe)
+ The `window` object
+ The `document` object
+ The `parent` object

WOW! This is a lot! So, please be careful!

This is well illustrated below:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3yhfGnl')"
    src    = "https://bit.ly/2Wz4Qv3"
    alt    = "web worker scope"
    title  = "web worker scope"
  />
</figure>


__Note that:__

1. Chrome has already implemented a new way for transferring objects from/to Web Workers by reference, in addition to the standard "by copy" method. This is in the [HTML 5.1 draft specification from the W3C](https://bit.ly/2Vjc8m3) - look for "transferable" objects! 
2. The canvas is not usable from Web Workers, however, [HTML 5.1 proposes a canvas proxy](https://bit.ly/3yjiMaz). 

#### Debugging Web Workers

Like other multi-threaded applications, debugging Web Workers can be a tricky task, and having a good tool-kit makes this process much easier.

+ __Chrome__ provides tools for debugging Web Workers. See [Debug Background Services With Chrome DevTools](https://bit.ly/3rWjmsF).

  When you open a page with Web Workers, open the Chrome Dev Tools (F12), look on the right at the Workers tab, check the radio box and reload the page. This will pop-up a small window for tracing the execution of each worker. In these windows, you can set breakpoints, inspect variables, log messages, etc. Here is a screenshot of a debugging session with the prime numbers example:

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 4;"
      onclick= "window.open('https://bit.ly/3yhfGnl')"
      src    = "https://bit.ly/3C1oi40"
      alt    = "chrome debug web workers"
      title  = "chrome debug web workers"
    />
</figure>

+ __FireFox__ has similar tools, see Firefox developer tools.






