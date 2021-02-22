window.onload = init;

function init() {
  // page has been loaded
  canvas = document.querySelector('#myCanvas');
  
  canvas.addEventListener('mousemove', processMouseMouve)
}

function processMouseMouve(evt) {
  var mousePositions = document.querySelector('#mousePositions');
  
  mousePositions.innerHTML = "mouse pos X: " + evt.clientX +
                              " mouse pos Y: " + evt.clientY + 
                              "<br>" 
 }

