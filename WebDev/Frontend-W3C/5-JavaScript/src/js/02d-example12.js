window.onload = resize;
window.onresize = resize;

function resize(evt) {
  console.log("resize");
  var pageSizeSpan = document.querySelector('#pageSize');
  pageSizeSpan.innerHTML = "Width: " + window.innerWidth + " Height: " + window.innerHeight;
  
 // screen size
var screenSizeSpan = document.querySelector('#screenSize');
  screenSizeSpan.innerHTML = "Width: " + screen.width + " Height: " + screen.height;
  
}

