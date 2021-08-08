# JavaScript Threads


## Threads

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




