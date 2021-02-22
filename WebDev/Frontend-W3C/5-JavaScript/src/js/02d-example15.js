window.onkeypress = processKeyPress;

/* or we could have written:
   window.addEventListener('keypress', processKeyPress);
*/

function processKeyPress(evt) {
  var keys = document.querySelector('#keys');
  keys.innerHTML += "keypress: " + evt.key + " code: " + evt.keyCode + "<br>";
}

