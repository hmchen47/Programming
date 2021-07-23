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

+ [`data-*` attributes](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-334-a-few-words-about-data--attributes)
  + metadata: a powerful way to add structured data into HTML code
  + HTML5 adding the possibility of adding arbitrary data to an HTML element
    + attributes starting w/ `data-` followed by any string literal (w/o uppercase)
    + treated as a storage area for private data
  + some classic attributes, including `alt`, `rel` and `title`, misused for storing arbitrary data
  + official way to add arbitrary data to HTML elements
  + custom data attributes: intended to store customer data private to the page or application
  + creating and accessing data attributes by the `dataset` property
  + `attr()` function: taking an attribute name as a parameter and return its value
  + examples:
    + invalid: <code>&lt;img src="photo.jpg" <span style="color: #ff0000;">photographer="Michel Buffa"</span> date="14July2020"&gt;</span></strong></code>
    + valid: <code>&lt;img src="photo.jpg" <span style="color: #ff0000;">data-photographer="Michel Buffa"</span> date="14July2020"&gt;</code>

+ Example: [accessing dataset property](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-334-a-few-words-about-data--attributes)
  + task: access `data-` attributes w/ `dataset` property

+ Example: [adding `data-` attributes w/ CSS](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-334-a-few-words-about-data--attributes)
  + task: using `attr()` in CSS to take an attribute name as a parameter and return its value


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




## Drop Detection

+ [Procedure to handle drop](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-333-drop-detection)
  <ol style="list-style-type: decimal;">
    <li> in the `dragstart` handler, copy a value in the drag and drop clipboard for later use</li>
    <li> define a "drop zone"</li>
    <li> write a <code>drop</code> handler, fetch content from the clipboard , and do something with it</li>
  </ol>

+ [Utilizing drag and drop clipboard](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-333-drop-detection)
  + get the value of the data-value attribute from the dragged element w/ `dragStart` handler
  + copy the obtained value into "drag and drop clipboard"
  + data as key/value pair
  + example: `function dragStartHandler(evt) { evt.dataTransfer.setData("Fruit", evt.target.dataset.value); }`

+ [Defining drop zone](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-333-drop-detection)
  + any visible element if `drop` event listener attached
  + listen for `dragover` or `dragend` events and stop their propagation
  + mouse moving over any drop zone triggering `dragover` event
  + a few `dragover` events to be handled before the element finally dropped
  + `ondragover` handler used to avoid propagating `dragover` events
  + example: `<div ondragover="return false" ondrop="dropHandler(event);">...</div>`

+ [Processing fetched content w/ `drop` handler](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-333-drop-detection)
  + `drop` event triggered once the dragged element placed
  + acquiring data from "drag and drop clipboard"
  + example: `function dropHandler(evt) { var data = evt.dataTransfer.getData("Fruit"); // do sth. w/ the data }`

+ Example: [handling drag and drop](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-333-drop-detection)
  + tasks
    + define drop zone and prevent event propagation
    + copy `data-value` of dragged element into drag'n'drop clipboard
    + handle `drop` event to fetch data and add dropped-item as a listed item



## Visual Feedback

+ [Visual feedback for drag & drop](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-335-add-visual-feedback)
  + scenarios
    + when drag something
    + when mouse enters a drop zone
    + etc.
  + associating CSS styling w/ the lifecycle of a drag and drop

+ [Events related to draggable object](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-335-add-visual-feedback)
  + `dragstart`:
    + used on draggable elements
    + used to get a value from the dragged element
    + copying value to the clipboard
    + good practice: visual feedback on draggable elements
  + `dragend`:
    + launched as the drag ended
    + on a drop or if the user releases the mouse button outside a drop zone
    + best practice: reset the style of the draggable object to default
  + `dragenter`:
    + binding the event to the drop zone
    + occurred when a dragged object enters a drop zone
    + good practice: change the appearance of the drop zone
  + `dragleave`:
    + used in relation to the drop zone
    + good practice: set appearance back to normal once leaving the drop zone
  + `dragover`:
    + generally bound to elements corresponding to a drop zone
    + best practice: preventing the propagation of the event and the default behavior of the browser
  + `drop`:
    + on the drop zone and processing the the drop, such as getting the value from the clipboard, etc.
    + good practice: reset the look of the drop zone to default

+ Example: [visualizing the drag and ](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-335-add-visual-feedback)

+ Example: [visual feedback on draggable object and the drop zone](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-335-add-visual-feedback)



## The `dropEffect` Property

+ [The `dropEffect` property](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-336-the-dropeffect-property)
  + changing the cursor's shape during the drag process
  + turning cursor into a "copy", "move" or "link" icon, depending on the semantic of the drag and drop
    + copy icon: copying an object into the drop zone
    + moving icon: moving an object
    + link icon: making a link or shortcut
  + alternative: using any customized image/icon
  + visual feedback:
    + using the `effectAllowed` and `dropEffect` properties of the `dataTransfer` object
    + specifying an effect in the `dragStart` handler by setting one of the possible predefined cursors
    + specifying the effect (to "copy", "move", etc.) in the `dragEnter` and `dragOver` handlers

+ [Possible values for `dropEffect` and `effectAllowed` properties](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-336-the-dropeffect-property)
  + `dataTransfer.effectAllowed`: `none`, `copy`, `copyLink`, `copyMove`, `link`, `linkMove`, `move`, `all`, `uninitialized`
  + `dataTransfer.dropEffect`: `none`, `copy`, `link`, `move`

+ [Syntax of visual effect for drag and drop](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-336-the-dropeffect-property)
  + allow a copy cursor effect: `function dragStartHandler(evt) { evt.dataTransfer.effecctAllowed = 'copy'; ... }`
  + change the cursor shape to a '+': `function dragEnterHandler(evt) { evt.dataTransfer.dropEffect = 'copy'; ... }`

+ Example: [customerized image](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-336-the-dropeffect-property)
  + add drag start handler: `function dragStartHandler(evt) {...}`
  + allow cursor effect: `evt.dataTransfer.effectAllowed = 'copy';`
  + load and create image: `var dragIcon = document.createElement('img'); dragIcon.src = 'anImage.png'; dragIcon.width = 100;`
  + set the cursor to this image: `evt.dataTransfer.setDragImage(dragIcon, -10, -10);`
  + ...


## HTML Elements for Drag and Drop

+ [Drag and drop HTML elements](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-337-drag-and-drop-html-elements)
  + copy and past to/from the clipboard
  + clipboard accessed through the `dataTransfer` property of the different evnets
    + copy data into the clipboard: `event.dataTransfer.setData("Fruit", event.targte.dataset.value);`
    + past data from the clipboard: `var data = event.dataTransfer.getData("Fruit");`
  + `<img>` elements all draggable by default

+ Example: [moving images as an HTML subtree](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-337-drag-and-drop-html-elements)
  + tasks
    + only work on the DOM directly
    + move icon from child of `<body>` to child of selected container


## Text Drag and Drop

+ [Moving selected text](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-338-drag-and-drop-a-text-selection)
  + no need to add a `dragstart` handler on an element containing text
  + selected text automatically added to the clipboard w/ a name/key equal to "text/plain"
  + adding a `drop` event handler on the drop zone
  + "text/plain" as the access key to fetch the data from the clipboard
  + typical syntax: `function drop(target, event) { event.preventDefault(); target.innerHTML = event.dataTransfer.getData('text/plain'); }`

+ Example: [moving selected text to the drop zone](../WebDev/Frontend-W3C/3-HTML5AppGame/03c-Online.md#notes-for-338-drag-and-drop-a-text-selection)
  + tasks:
    + use a CSS trick to make a paragraph non-selectable
    + move selected text to a drop zone






