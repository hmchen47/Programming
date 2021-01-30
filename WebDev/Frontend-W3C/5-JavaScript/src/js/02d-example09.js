// Good practice: have an function
window.onload = init;

function init(evt) {
  // called when the page is loaded
  
  console.log("page loaded");
  
  let span = document.querySelector("#pageStatus");
  span.innerHTML = "PAGE LOADED"; 
  
  let b = document.querySelector("#myButton");
  b.addEventListener('mousemove', function(evt) {
    console.log("x = " + evt.clientX);
  });
} 
