window.onload = function init() {
   requestAnimationFrame(mainloop);
};  

function mainloop(timestamp) {
   document.body.innerHTML += "*";
  
   // call back itself every 60th of second
   requestAnimationFrame(mainloop);
}

