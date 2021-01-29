# Module 2: Adding interactivity to HTML documents

## 2.4 Handling events

### 2.4.1 Introduction

Adding interactivity to a Web application can be achieved by using only CSS, such as by using the `:hover`2.4.1 Introduction pseudo CSS class.

For example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/gmvgxa)

[Local Demo](src/02d-example01.html)

However, firing a specific action when the button is clicked, knowing which mouse button has been used, computing the (x, y) mouse pointer position in the button system coordinate, or executing more complex tasks can only be done through JavaScript.

With JavaScript, a button click, a move of the mouse, a resized window, and many other interactions create what are called "events".  The timing and order of events cannot be predicted in advance. We say that "event processing" is asynchronous. Web browsers detect events as they occur, and may pass them to JavaScript code. They do this by allowing you to register functions as _event listeners_, also called _handlers_ or _callbacks_ for specific events.

Each time an event occurs, the browser puts it in a "queue of events".

Then the browser looks at a list of "Event Listeners" and calls the ones that correspond to the type of event "they listen to".

#### Notes for 2.4.1 Introduction

+ Interactivity of Web application
  + CSS:
    + limited w/ pseudo CSS class
    + example. `.hover`
  + JavaScript:
    + extended features
    + examples: mouse button clicked
      + which mouse button used
      + mouse pointer position in button system coordinate
      + executing more complex tasks
  + events
    + interaction created, e.g., button clicked, mouse movement, window resized
    + timing and order unable to be predicted in advance
    + asynchronous event processing
    + event listerners
      + a.k.a. handlers or callbacks for special event
      + registered functions
      + web browser detecting events as they occur
      + pass these events to JavaScript code
    + events placed in "queue of events"
    + browser looks at a list of "Event Listerners" and calls the ones corresponding to the type of evenet listening to



