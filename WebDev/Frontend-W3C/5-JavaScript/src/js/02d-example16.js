window.onkeydown = processKeyDown;

/* or we could have written:
   window.addEventListener('keypress', processKeyPress);
*/

function processKeyDown(evt) {
  var keys = document.querySelector('#keys');
  
   keys.innerHTML += "keypress: " + evt.key + 
                   " code: " + evt.keyCode + " Modifiers : ";

  var modifiers = "";
  
  if(event.shiftKey)
    modifiers += "SHIFT ";

  if(event.altKey)
    modifiers += "ALT ";

  if(event.ctrlKey)
    modifiers += "CTRL ";

  if(modifiers === "")
    modifiers = "NONE";
  
  keys.innerHTML += modifiers + "<br>";
}

