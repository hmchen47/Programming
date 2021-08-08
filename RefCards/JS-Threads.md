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


## Web Workers Overview

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


