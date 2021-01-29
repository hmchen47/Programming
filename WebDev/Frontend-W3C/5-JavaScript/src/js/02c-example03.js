// Add a click event listener on the whole document
// the processClick function is a callback:
// a function called by the browser when a click event
// is detected
window.addEventListener('click', processClick);

function processClick(event) {
  document.body.innerHTML += "Button clicked<br>";
}

// We could have written this, with the body of the callback as an argument of the addEventListener function
window.addEventListener('click', function(evt) {
  document.body.innerHTML += "Button clicked version 2<br>";
});
