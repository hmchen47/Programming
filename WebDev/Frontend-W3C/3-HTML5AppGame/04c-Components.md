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

<div><ol>
<li value="1">&lt;!DOCTYPE HTML&gt;</li>
<li>&lt;html&gt;</li>
<li> &lt;head&gt;</li>
<li> &lt;title&gt;Worker example: One-core computation&lt;/title&gt;</li>
<li> &lt;/head&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;button>> >>id>>=>>"startButton">>&gt;>>Click to start discovering prime numbers>>&lt;/button&gt;&lt;p&gt;>>&nbsp;Note that this will make the page unresponsive, you will have to close the tab in order to get back your CPU!></li>
<li>> >>&lt;p&gt;>>The highest prime number discovered so far is: >>&lt;output>> >>id>>=>>"result">>&gt;&lt;/output&gt;&lt;/p&gt;></li>
<li>> >>&lt;script&gt;></li>
<li>>&nbsp;&nbsp; >>function>> computePrime>>()>> >>{></li>
<li>>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >>var>> n >>=>> >>1>>;></li>
<li>>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; search>>:>> > style="color: #ff0000;"><strong style="color: red;">>while>> >>(>>true>>)></strong>>> >>{></li>
<li>>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; n >>+=>> >>1>;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for (var i = 2; i &lt;= Math.sqrt(n); i += 1)</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (n % i == 0)</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue search;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // found a prime!</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.getElementById('result').textContent = n;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } </li>
<li>&nbsp;&nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp;&nbsp; document.querySelector("#startButton").addEventListener('click', computePrime);</li>
<li> &lt;/script&gt;</li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
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
  + init incremental variable for prime number: `var n =1;`
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

<div><ol>
<li value="1">var worker = new Worker("worker0.js");</li>
</ol></div>

More than one worker can be created/loaded by a parent page. This is parallel computing after all :-)


#### Using messages to manage a worker

__Use case #2: you manage a worker by communicating with it using "messages"__

Messages can be strings or objects, as long as they can be serialized in JSON format (this is the case for most JavaScript objects, and is handled by the Web Worker implementation of recent browser versions).

Terminology check: serialized

(1) Messages can be sent by the parent page to a worker using this kind of code:

<div><ol>
<li value="1">var worker = new Worker("worker0.js");</li>
<li> </li>
<li>// String message example</li>
<li>worker.postMessage("Hello");</li>
<li> </li>
<li>// Object message example</li>
<li>var personObject = {'firstName': 'Michel', 'lastName':'Buffa'};</li>
<li>worker.postMessage(personObject );</li>
</ol></div>


(2) Messages (like the object message example, above) are received from a worker using this method (code located in the JavaScript file of the worker):

<div><ol>
<li value="1">onmessage = function (event) {</li>
<li>&nbsp; &nbsp;// do something with event.data</li>
<li>&nbsp; alert('received ' + event.data.firstName);</li>
<li>};</li>
</ol></div>

(3) The worker will then send messages back to the parent page (code located in the JavaScript file of the worker):

<div><ol>
<li value="1">postMessage("Message from a worker !");</li>
</ol></div>

(4) And the parent page can listen to messages from a worker like this:

<div><ol>
<li value="1">worker.onmessage = function(event){</li>
<li>&nbsp;&nbsp;&nbsp; // do something with event.data</li>
<li>};</li>
</ol></div>


#### Complete example

__Use case #3: a complete example__

The "Parent HTML page" of a simplistic example using a dedicated Web Worker:

<div><ol>
<li value="1">&lt;!DOCTYPE HTML&gt;</li>
<li>&lt;html&gt;</li>
<li> &lt;head&gt;</li>
<li> &lt;title&gt;Worker example: One-core computation&lt;/title&gt;</li>
<li> &lt;/head&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;p&gt;The most simple example of Web Workers&lt;/p&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp;&nbsp; // create a new worker (a thread that will be run in the background)</li>
<li>&nbsp;&nbsp; var worker = new Worker("worker0.js");</li>
<li> </li>
<li>&nbsp;&nbsp; // Watch for messages from the worker</li>
<li>&nbsp;&nbsp; worker.onmessage = function(e){</li>
<li>&nbsp; &nbsp; &nbsp;// Do something with the message from the client: e.data</li>
<li>&nbsp; &nbsp; &nbsp;alert("Got message that the background work is finished...")</li>
<li>&nbsp; &nbsp;};</li>
<li> </li>
<li>&nbsp; &nbsp;// Send a message to the worker</li>
<li>&nbsp; &nbsp;worker.postMessage("start");</li>
<li> &lt;/script&gt;</li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

The JavaScript code of the worker (worker0.js):

<div><ol>
<li value="1">onmessage = function(e){</li>
<li>&nbsp;&nbsp; if ( e.data === "start" ) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // Do some computation that can last a few seconds...</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // alert the creator of the thread that the job is finished</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; done();</li>
<li>&nbsp;&nbsp;&nbsp; }</li>
<li>};</li>
<li> </li>
<li>function done(){</li>
<li>&nbsp;&nbsp;&nbsp; // Send back the results to the parent page</li>
<li>&nbsp;&nbsp;&nbsp; postMessage("done");</li>
<li>}</li>
</ol></div>


#### Error handling

__Use case #4: handling errors__

The parent page can handle errors that may occur inside its workers, by listening for an `onError` event from a worker object:

<div><ol>
<li value="1">var worker = new Worker('worker.js');</li>
<li> worker.onmessage = function (event) {</li>
<li>&nbsp;&nbsp;&nbsp; // do something with event.data</li>
<li> };</li>
<li> </li>
<li> worker.onerror = function (event) {</li>
<li>&nbsp;&nbsp;&nbsp; console.log(event.message, event);</li>
<li> };</li>
<li>}</li>
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
  + add error handler: `worker.onerror = function(evt) { console.log(evt.message, evt); }`


### 4.3.3 Examples

Dedicated Workers are the simplest kind of Workers. Once created, they remain linked to their parent page (the HTML5 page that created them). An implicit "communication channel" is opened between the Workers and the parent page, so that messages can be exchanged.


#### Background task with user interface responsive

__Example #1: compute prime numbers in the background while keeping the page user interface responsive__

Let's look at [the first example, taken from the W3C specification](https://html.spec.whatwg.org/#workers): 
> "The simplest use of workers is for performing a computationally expensive task without interrupting the user interface. In this example, the main document spawns a worker to (naïvely) compute prime numbers, and progressively displays the most recently found prime number."

This is the example we tried earlier, without Web Workers, and it froze the page. This time, we'll use a Web Worker. Now you will notice that the prime numbers it computes in the background are displayed as soon as the next prime number is found.

[Try this example online using CodePen](https://codepen.io/w3devcampus/project/editor/ZynNvX/). Note that we cannot run this example on JsBin as Workers need to be defined in a separate JavaScript file.

[Local Demo](src/04c-example02.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3yhfGnl')"
    src    = "https://bit.ly/3j4kjuS"
    alt    = "Prime number computation"
    title  = "Prime number computation"
  />
</figure>


The HTML5 page code from this example that uses a Web Worker:

<div><ol>
<li value="1">&lt;!DOCTYPE HTML&gt;</li>
<li>&lt;html&gt;</li>
<li> &lt;head&gt;</li>
<li> &lt;title&gt;Worker example: One-core computation&lt;/title&gt;</li>
<li> &lt;/head&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;p&gt;The highest prime number discovered so far is: &lt;output id="result"&gt;&lt;/output&gt;&lt;/p&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp;&nbsp;&nbsp; <strong style="color: red;">var worker = new Worker('worker.js');</strong></li>
<li>&nbsp;&nbsp;&nbsp; <strong style="color: red;">worker</strong><strong style="color: red;">.onmessage = function (event)</strong> {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; document.getElementById('result').textContent = event.data;</li>
<li> };</li>
<li> &lt;/script&gt;</li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

__Explanations:__

+ the Web Worker is created at _line 9_
+ its code is in the `worker.js` file
+ _Lines 10-12_ process messages sent asynchronously by the worker
+ `event.data` is the message content.

Workers can only communicate with their parent page using messages. See the code of the worker below to see how the message has been sent.

The code of the worker (`worker.js`):

<div><ol>
<li value="1">var n = 1;</li>
<li>search: while (true) {</li>
<li>&nbsp;&nbsp;&nbsp; n += 1;</li>
<li>&nbsp;&nbsp;&nbsp; for (var i = 2; i &lt;= Math.sqrt(n); i += 1)</li>
<li>&nbsp;&nbsp;&nbsp; if (n % i == 0)</li>
<li>&nbsp;&nbsp;&nbsp; continue search;</li>
<li>&nbsp;&nbsp;&nbsp; // found a prime!</li>
<li>&nbsp;&nbsp;&nbsp;<strong style="color: red;"> postMessage</strong><strong style="color: red;">(n);</strong></li>
<li>}</li>
</ol></div>

There are a few interesting things to note here:

There is an infinite loop in the code at _line 2_ (while true...). This is not a problem as it runs in the background.
When a prime number is found, it is posted to the creator of the Web Worker (aka the parent HTML page), using the `postMessage(...)` function (_line 8_).

Computing prime numbers using such a weak algorithm is very CPU intensive. However, the Web page is still responsive: you can refresh it and the "script not responding"  error dialog box will not appear, etc. There is a demo in the next section of this course chapter in which some graphic animation has been added to this example, and you can verify that the animation is not affected by the computations in the background.

__Try an improved version of the first example yourself__

We can improve this example a little by testing whether the browser supports Web Workers, and by displaying some additional messages.

<p style="margin: 10px; padding: 10px; color: red"><strong style="color: red;">CAREFUL</strong>: for security reasons you cannot try the examples using a file:// URL. <strong style="color: red;">You need an HTTP web server that will serve the files</strong>. Here is what happens if you do not follow this constraint:</p>

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

<div><ol>
<li value="1">&lt;!DOCTYPE HTML&gt;</li>
<li>&lt;html&gt;</li>
<li> &lt;head&gt;</li>
<li> &lt;title&gt;Worker example: One-core computation&lt;/title&gt;</li>
<li> &lt;/head&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;p&gt;The highest prime number discovered so far is: &lt;output id="result"&gt;&lt;/output&gt;&lt;/p&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp;&nbsp;&nbsp; if(window.Worker){</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // web workers supported by the browser</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var worker=new Worker("worker1.js");</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; worker.onmessage=function(event){</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.getElementById('result').textContent = event.data;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; };</li>
<li>&nbsp;&nbsp;&nbsp; }else{</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // the browser does not support web workers</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert("Sorry, your browser does not support Web Workers");</li>
<li>&nbsp;&nbsp;&nbsp; }</li>
<li> &lt;/script&gt;</li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

_Line 9_ shows how to test if the browser can run JavaScript code that uses the HTML5 Web Workers API.

Here is the `worker1.js` code:

<div><ol>
<li value="1">postMessage("Hey, in 3s, I'll start to compute prime numbers...");</li>
<li> </li>
<li>setTimeout(function() {</li>
<li>&nbsp;&nbsp;&nbsp; // The setTimeout is just useful for displaying the message in line 1 for 3 seconds and</li>
<li>&nbsp;&nbsp;&nbsp; // making it visible</li>
<li>&nbsp;&nbsp;&nbsp; var n = 1;</li>
<li>&nbsp;&nbsp;&nbsp; search: while (true) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; n += 1;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for (var i = 2; i &lt;= Math.sqrt(n); i += 1)</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (n % i == 0)</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue search;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // found a prime!</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; postMessage(n);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li>}, 3000);</li>
</ol></div>

In this example, we just added a message that is sent to the "parent page" (_line 1_) and we use the standard JavaScript method `setTimeout()` to delay the beginning of the prime number computation by 3s.


#### Stop/kill a worker

__Example #2: how to stop/kill a worker after a given amount of time__

So far we have created and used a worker. Now we will see how to kill it!

A worker is a thread, and a thread uses resources. If you no longer need its services, _it is best practice to release the used resources,_ especially since some browsers may run very badly when excessive memory consumption occurs. _Even if we unassign the variable that was used to create the worker, the worker itself continues to live_ - it does not stop! Worse: the worker continues in its task (therefore memory and other resources are still allocated) but it becomes inaccessible. In this situation, we cannot do anything but close the tab/page/browser.

The Web Worker API provides a `terminate()` method that we can use on any worker, to end its life. After a worker has been killed, it is not possible to undo its termination. The only option is to create a new worker.

HTML code:

<div><ol>
<li value="1">&lt;!DOCTYPE HTML&gt;</li>
<li>&lt;html&gt;</li>
<li> &lt;head&gt;</li>
<li> &lt;title&gt;Worker example: One-core computation&lt;/title&gt;</li>
<li> &lt;/head&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;p&gt;The highest prime number discovered so far is: &lt;output id="result"&gt;&lt;/output&gt;&lt;/p&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp;&nbsp;&nbsp; if(window.Worker){</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // web workers supported by the browser</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var worker=new Worker("worker2.js");</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; worker.onmessage=function(event){</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.getElementById('result').textContent = event.data;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; };</li>
<li>&nbsp;&nbsp;&nbsp; }else{</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // the browser does not support web workers</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert("Sorry, your browser does not support Web Workers");</li>
<li>&nbsp;&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp; setTimeout(function(){</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // After 10 seconds, we kill the worker</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong style="color: red;"> worker</strong><strong style="color: red;">.terminate();</strong></li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.body.appendChild(document.createTextNode("Worker killed, 10 seconds elapsed !")</li>
<li>&nbsp;&nbsp;&nbsp; );}, 10000);</li>
<li> &lt;/script&gt;</li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

Notice at _line 22_ the call to `worker.terminate()`, that kills the worker after 10000ms.

`worker2.js` is the same as in the last example:

<div><ol>
<li value="1">&lt;!DOCTYPE HTML&gt;</li>
<li>&lt;html&gt;</li>
<li> &lt;head&gt;</li>
<li> &lt;title&gt;Worker example: One-core computation&lt;/title&gt;</li>
<li> &lt;/head&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;p&gt;The highest prime number discovered so far is: &lt;output id="result"&gt;&lt;/output&gt;&lt;/p&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp;&nbsp;&nbsp; if(window.Worker){</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // web workers supported by the browser</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var worker=new Worker("worker2.js");</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; worker.onmessage=function(event){</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.getElementById('result').textContent = event.data;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; };</li>
<li>&nbsp;&nbsp;&nbsp; }else{</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // the browser does not support web workers</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert("Sorry, your browser does not support Web Workers");</li>
<li>&nbsp;&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp; setTimeout(function(){</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // After 10 seconds, we kill the worker</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong style="color: red;"> worker</strong><strong style="color: red;">.terminate();</strong></li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.body.appendChild(document.createTextNode("Worker killed, 10 seconds elapsed !")</li>
<li>&nbsp;&nbsp;&nbsp; );}, 10000);</li>
<li> &lt;/script&gt;</li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
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

<div><ol>
<li value="1"><strong style="color: red;">importScripts('script1.js');</strong></li>
<li><strong style="color: red;">importScripts('script2.js');</strong></li>
<li> </li>
<li>// Other possible syntax</li>
<li>importScripts('script1.js', 'script2.js');</li>
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
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
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

+ __FireFox__ has similar tools, see [Firefox developer tools](https://developer.mozilla.org/en-US/docs/Tools).


#### Notes for 4.3.3 Examples

+ Dedicated workers
  + the simplest kind of Workers
  + remaining linked to the parent page once created
  + implicit communication channel opened btw the Workers and the parent page $\to$ message exchanged
  + simplest use of workers for performing a computationally experience task w/o interrupting the user interface
  + processing messages sent asynchronously by the worker: `worker.onmessage = function(event) {...}`
  + `event.data`: the message content
  + workers only communciating w/ their parent page using
  + a worker = a thread
  + thread using resources
  + best pratice: a work no longer required $\to$ releasing the used resources
  + using `terminate()` method on any worker to end the workera nd unable to 
  + web worker able to kill itself by calling the `close()` method in worker's JS file

+ Example: backgroundtask and user interface responsive - simple version
  + HTML inline script: `<script>...</script>`
    + create worker: `var worker = new Worker("worker.js")`
    + process messages sent asynchronously by the worker: `worker.onmessage = function(evt) { document.getElementById('result').textContent = evt.data; };`
  + Javascript snippet for `worker.js`
    + tasks:
      + infinite loop to compute prime numbers
      + post found prime numbers using `postMessage(...)`
    + init incremental variable for prime number<a name="initNum"></a>: `var n = 1;`
    + create infinite loop to compute prime<a name="primeNum"></a>: `search: while(true) {...}`
      + increase variable: `n += 1;`
      + iterate to check prime number: `for (var i=2; i<=Math.sqrt(n); i++) { if (n % i == 0) {continue search; } else { postMessage(n); } }`

+ Example: Web workers
  + HTML snippet for prime number: <a name="output"></a>: `<p>The highest prime number discovered so far is: <output id="result"></output></p>`
  + HTML inline script: `<script>...</script>`
    + check browser supporting web worker<a name="chkSupport"></a>: `if (window.Worker) { // compute and display prime number } else { // not support msg }`
    + browser support<a name="support"></a>: `var worker = new Worker("worker1.js"); worker.onmessage = function(evt) { document.getElementById("result").textContent = evt.data; };`
    + browser not support<a name="notSupport"></a>: `alert("Sorry, your browser does not support Web Workers");`
  + JavaScript snippet: `worker1.js`
    + add message sent to the parent page: `postMessage("hey, in 3s, I'll start to compute prime numbers...");`
    + set time out: `setTimeout( function() {...}, 3000);`
    + [init incremental variable for prime number](#initNum)
    + create infinite loop to [compute prime](#primeNum)

+ Example: terminating web worker
  + HTML snippet for [prime number](#output)
  + HTML inline script: `<script>...</script>`
    + check [browser supporting](#chkSupport) web worker
    + [browser support](#support)
    + browser [not support](#notSupport)
    + set time out: `setTimeout(function() {...}, 10000);`
    + terminate worker: `worker.terminate();`
    + addpend displayed msg on page: `document.body.appendChild(document.createTextNode("Worker killed, 10 seconds elapsed!"));`

+ Web worker w/ external scripts
  + loading external scripts by works using the `importScripts()` function
  + included scripts following the same-origin policy
  + external scripts loaded asynchronously
  + function `importScripts()` not returning until all the scripts loaded and executed
  + error occurred during a script importing process
    + a `NETWORK_ERROR` thrown by the `importScripts` function
    + following code not executed

+ Limitations of Web Workers
  + debugging threads probably becoming a nightmare
  + solutions in the Web Workers API
    + when a message is sent, it is always a copy that is received: no more thread security problem
    + only pre-defined thread-safe objects are available in workers, this iis a subset of those usually available in stnadard JS scripts
  + objects available in Web Workers
    + the `navigator` object
    + the `location` object (read-only)
    + `XMLHttpRequest`
    + `setTimeout()/clearTimeout()` and `setInterval()/clearInterval()`
    + the [Application Cache](https://www.html5rocks.com/tutorials/appcache/beginner/)
    + importing external scripts using the `importScripts()` method
    + [Spawning other Web Workers](https://bit.ly/3BWcLmp)
  + Worker unable to access to
    + the DOM (not thread-safe)
    + the `window` object
    + the `document` object
    + the `parent` object

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open('https://bit.ly/3yhfGnl')"
      src    = "https://bit.ly/2Wz4Qv3"
      alt    = "web worker scope"
      title  = "web worker scope"
    />
  </figure>

+ Debugging Web Workers
  + Chrome providing tools
    + Chrome developers, [Debug background services](https://developer.chrome.com/docs/devtools/javascript/background-services/)
    + devtools setting: devtools > Workers tab > check 'Pause on stop'
    + poping up small window for tracing the execution of each worker
    + able to check breakpoints, inspect variables, log message, etc.
  + FireFox: [Firefox developer tools](https://developer.mozilla.org/en-US/docs/Tools)


### 4.3.4 Demos


#### Demo #1

This is a variation of the prime number example (previous lecture) which shows that an interaction in the parent page is not affected by the background computation of prime numbers. Try it [online](https://michaeltreat.github.io/Web-Worker-Demo/html/no-web-worker.html). Open the devtool console, click the BEGIN button , then the CHANGE COLOR button. Without the use of Workers, the color will change only after the computations are completed and the page GUI is not reactive. Click the WITH WORKERS button: this will run the code that computes prime numbers in a Web Worker. Now, try to change the color of the button, it reacts instantly...

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/2TKd9TK')"
    src    = "https://bit.ly/3rMGwRX"
    alt    = "Demo screenshot"
    title  = "Demo screenshot"
  />
</figure>


#### Demo #2

Do ray tracing using a variable number of Workers, and try it [online](https://nerget.com/rayjs-mt/rayjs.html) (if you've not heard of it before, [here's an explanation](https://www.cs.unc.edu/~rademach/xroads-RT/RTarticle.html) that tells you more than you will ever want to know about ray tracing!)

In this demo, you can select the number of Web Workers which will compute parts of the image (pixels). If you use too many Web Workers, the performance decreases because too much time is spent exchanging data between workers and their creator, instead of computing in parallel.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2TKd9TK')"
    src    = "https://bit.ly/3zV8uOj"
    alt    = "ray tracer with web workers"
    title  = "ray tracer with web workers"
  />
</figure>


#### Other demos

[Try these other impressive demos at the MDN demo repository!](https://mzl.la/3ykdlbn)


### 4.3.5 Discussion and projects

Here is the discussion forum for this part of the course. Please post your comments/observations/questions and share your creations.

#### Suggested topics of discussion:

+ Did you try the demos from the last lesson? Do you understand why using Web Workers can be a savior in some situations?
+ Can you find some explanations on the Web about multi core architectures and Web Workers (e.g., about threads/workers benefiting from multi core processors, leading to greater performance). Please share any relevant articles in the forum!


#### Optional projects:

+ Please write a small Web app. that uses Web Workers.
+ There is a wonderful demonstration of a [fountain animation](https://testdrive-archive.azurewebsites.net/Graphics/WorkerFountains/Default.html) using particles, made by Microsoft. Can you write something similar, but perhaps with fewer options? The idea was the following: compute _particle movements_ in separate _workers_, and when a new array of _particles_ is ready to be drawn, post it from the Web Worker. The main page has a mainloop for animating at 60 frames per second. When a new set of _particles_ is ready (posted by a _Worker_), it is drawn and animated. The demo had up to 10 _workers_ operating in _parallel_, in the _background_.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3ll9sQ0')"
    src    = "https://bit.ly/3ifFZ7S"
    alt    = "IE 10 web worker fountain demo"
    title  = "IE 10 web worker fountain demo"
  />
</figure>



