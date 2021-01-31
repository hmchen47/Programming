window.onclick = processClick;

function processClick(evt) {
  var clicks = document.querySelector('#clicks');

  var target = evt.target.id;
  
  if(target === "") {
    clicks.innerHTML += "You clicked on the window, not on a particular element!<br>";
  } else {
    clicks.innerHTML += "Element clicked id: " + target + "<br>";
   
  }
  
  
  evt.stopPropagation(); // try commenting it and click on the button or div
}

