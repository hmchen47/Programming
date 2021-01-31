window.onmousemove = processMouseMouve;

function processMouseMouve(evt) {
  var mousePositions = document.querySelector('#mousePositions');
  mousePositions.innerHTML = "clientX: " + evt.clientX +
                              " clientY: " + evt.clientY + "<br>" +
                             " pageX : " + evt.pageX +
                              "  pageY : " + evt.pageY +
                              "<br>";

  var mouseScreenPositions = document.querySelector('#mouseScreenPositions');
  mouseScreenPositions.innerHTML = "screenX: " + evt.screenX +
                             " screenY: " + evt.screenY + 
                             "<br>";
 }

