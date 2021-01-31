window.onmousemove = moveElem;
window.onmouseup = stopMovingElem;
window.onload = init;

var selected = null; // element to be moved
var oldMouseX, oldMouseY; // Stores x & y coordinates of the mouse pointer
var elemX, elemY;

function init() {
    document.querySelector('.draggable').onmousedown = function (evt) {
        dragInit(evt);
    };
}
  
// Will be called when user starts dragging an element
function dragInit(evt) {
    // Store the elem
    selected = evt.target;
    elemX = selected.offsetLeft;
    elemY = selected.offsetTop;
  
    oldMouseX = evt.clientX;
    oldMouseY = evt.clientY;
}

// Will be called when user dragging an element
function moveElem(e) {
    // new mouse ps
    var newMouseX = e.clientX;
    var newMouseY = e.clientY;
  
    if(oldMouseX !== undefined) {
        // how many pixels did we move the mouse?
        var dx = newMouseX - oldMouseX;
        var dy = newMouseY - oldMouseY;
     }
    
    if (selected !== null) {  
        // move the selected element dx, dy pixels hozontally/vertically
        changePosOfSelectedElement(dx, dy);
    }
  
    // update the old position of the mouse
    oldMouseX = newMouseX;
    oldMouseY = newMouseY;
}

function changePosOfSelectedElement(dx, dy) {
  // update the old position of the selected element
  elemX += dx;
  elemY += dy;
  
  // change the pos on screen of the element
  // by modifying its CSS left/top properties
  selected.style.left = elemX + 'px';
  selected.style.top = elemY + 'px';
}

// Destroy the object when we are done
function stopMovingElem() {
    selected = null;
}

