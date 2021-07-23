# Drag and Drop 

## Overview

+ [Drag and drop API](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-331-introduction)
  + defining an event-based drag-and-drop machansim
  + not defining what a drag-and-drop operation
  + often used for dragging and dropping files
  + resources
    + MDN article about [HTML Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API).
    + Medium article entitled "[How to Drag & Drop HTML Elements and Files using Javascript](https://bit.ly/3wfFqif)"
    + Nice [shopping cart demo](https://bit.ly/3xiKp36).
  + ref: E. Bidelman and R. Andrew, [Using the HTML5 Drag and Drop API](https://web.dev/drag-and-drop/), 2020


## `data-*` Attribute

+ [`data` attribute](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)
  + storing extra info on standard elements w/o other hacks
  + html syntax: `data` attribute: any attribute started w/ `data-`
  + Javascrip access
    + using `getAttribute()` w/ their full HTML name to read
    + alternative: reading out via a `dataset` property




## Drag Detection

+ [Draggable attribute](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-332-drag-detection)
  + making any visible element draggable w/ `true` value
  + some elements draggable by default, such as `<img>`
  + example: `<li draggable=true data-value="fruit-apple">Apple</li>`

+ [`dragstart` event](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-332-drag-detection)
  + add listener to detect a drag
  + `ondragstart` for HTML event handler
  + inheritance of handler: each of its children triggering the event
  + example: `<ol ondragstart="dragStartHandler(evt)"> ... </ol>`

+ Example: [draggable attribute and event handler](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-332-drag-detection)




## 

