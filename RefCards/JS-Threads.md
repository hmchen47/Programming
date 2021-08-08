# JavaScript Threads


## Overview

+ [Threads in browser](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#431-introduction)
  + normal JS code: a single thread
  + competing for processor time: the browser GUI, the JavaScript, and other tasks
  + intensive CPU task $\implies$ everything else blocked
  + solution:
    + running certain CPU-intensive tasks in separate threads from the one managing the graphical user interface
    + performing computationally intensive tasks in one or more background threads
    + using the HTML Web Workers
    + Web Workers = CPU threads, in JavaScript

+ Example: [intensive task w/o Web Workers - bad JS programming](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#431-introduction)

+ [Thread safety](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#431-introduction)
  + a common problem when programming w/ multiple threads
  + several concurrent tasks share the same resources at the same time
  + modifying the value pf a variable while another one is reading it $\to$ probably result in some strange behavior
  + solution: Web Worker
    + carefully controlled communication points w/ other threads
    + very hard to cause concurrency problems
    + no access in worker to non-thread safe components or to the DOM
    + passing specific data into and out of a thread through serialized objects
    + the separate threads share different copies


## Web Workers

+ [Types of web workers](..)/WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#431-introduction
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
    + comforming to the "same-origin" policy
    + not supported by major browsers

+ [Creating workers from script](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#432-use-cases)
  + HTML5 Web Worker API: providing the Worker JS interface for loading and executing a script in the background, in different thread from the UI
  + syntax: `var worker = new Worker("worker0.js");`
  + more than one worker probably created/loaded by a parenet page

+ Example: [web workers](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#432-use-cases)

+ Example: [handling error](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#432-use-cases)



## Managing Web Workers

+ [Using "messages" to manage a worker](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#432-use-cases)
  + messages: strings or object
  + possibly serialized in JSON format, most used JS object
  + procedure of serialization:
    + messages sent by the parent page to a worker
      + create worker: `var worker = new Worker("worker0.js");`
      + set string message: `worker.postMessage("Hello");`
      + declare object: `var personObj = {'firstName': 'Michel', 'lastName': 'Buffa'};`
      + set message: `worker.postMessage(personObj);`
    + message received from a worker by adding message handler: `onmessage = function(evt) { // do sth. w/ evt.data; alert('received ' + evt.data.firstName); };`
    + worker sending message back to the parent page: `postMessage("Message from a worker!");`
    + the parent page able to listen to messages from a work: `worker.onmessage = function(evt) { // do sth. w/ evt.data };`


## Dedicated Workers

+ [Dedicated workers](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#433-examples)
  + the simplest kind of Workers
  + remaining link to the parent page once created
  + implicit communication channel opened btw the Workers and the parent page $\to$ message exchanged
  + simplest use of workers for performing a computationally experienced task w/o interrupting the user interface
  + processing messages sent asynchronously by the worker: `worker.onmessage = function(event) {...}`
  + `event.data`: the message content
  + workers only communciating w/ their parent page using messages
  + a worker = a thread
  + thread using resources
  + best pratice: a work no longer required $\to$ releasing the used resources
  + using `terminate()` method on any worker to end the worker
  + web worker able to kill itself by calling the `close()` method in worker's JS file

+ Example: [backgroundtask and user interface responsive - simple version](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#433-examples)

+ Example: [Web workers](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#433-examples)

+ Example: [terminating web worker](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#433-examples)

+ [Web worker w/ external scripts](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#433-examples)
  + loading external scripts by works using the `importScripts()` function
  + included scripts following the same-origin policy
  + external scripts loaded asynchronously
  + function `importScripts()` not returning until all the scripts loaded and executed
  + error occurred during a script importing process
    + a `NETWORK_ERROR` thrown by the `importScripts()` function
    + following code not executed


## Limtations

+ [Limitations of Web Workers](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#433-examples)
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


## Debugging

+ [Debugging Web Workers](../WebDev/Frontend-W3C/3-HTML5AppGame/04c-Components.md#433-examples)
  + Chrome providing tools
    + Chrome developers, [Debug background services](https://developer.chrome.com/docs/devtools/javascript/background-services/)
    + devtools setting: devtools > Workers tab > check 'Pause on stop'
    + poping up small window for tracing the execution of each worker
    + able to check breakpoints, inspect variables, log message, etc.
  + FireFox: [Firefox developer tools](https://developer.mozilla.org/en-US/docs/Tools)


