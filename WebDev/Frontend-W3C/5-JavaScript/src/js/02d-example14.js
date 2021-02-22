window.onkeyup = processKeyUp;
window.onkeydown = processKeyDown;

/* or we could have written:
   window.addEventListener('keyup', processKeyUp);
   window.addEventListener('keydown', processKeyDown);
*/

function processKeyUp(evt) {
  var keys = document.querySelector('#keys');
  keys.innerHTML += "keyup: " + evt.key + " code: " + evt.keyCode + "<br>";
}

function processKeyDown(evt) {
  var keys = document.querySelector('#keys');
  keys.innerHTML += "keydown: " + evt.key + " code: " + evt.keyCode + "<br>";
}

