window.onkeydown = processKeyDown;

/* or we could have written:
   window.addEventListener('keypress', processKeyPress);
*/

function processKeyDown(evt) {
  var keys = document.querySelector('#keys');
  
   keys.innerHTML += "keypress: " + evt.key + 
                   " code: " + evt.keyCode + " Modifiers : ";

  var modifiers = "";
  
  if(evt.shiftKey)
    modifiers += "SHIFT ";

  if(evt.altKey)
    modifiers += "ALT ";

  if(evt.ctrlKey)
    modifiers += "CTRL ";

  if(modifiers === "")
    modifiers = "NONE";
  
  keys.innerHTML += modifiers + "<br>";
}

