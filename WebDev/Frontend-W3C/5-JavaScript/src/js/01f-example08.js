var divElem;

function init() {
  console.log("page loaded and DOM is ready");
  
  // use the selection API to select the div
  divElem = document.querySelector("#theDiv");
}

var currentImage = 0;
var leftPos = 0;

function animateMario() {
  drawMario(currentImage);
  // next time, show next sprite/subimage
  currentImage = (currentImage +1) % 3;
  // next time, move mario 5 pixels to the right
  leftPos += 5;
  // And if he moved 100 pixels, start back from the left
  if(leftPos >= 100) 
    leftPos = 0;
}

function drawMario(indexImage) {
  // set the left pos of the div using the left margin
  divElem.style.marginLeft = leftPos + "px";
  // change the width and height of the div
  divElem.style.width = "22px";
  divElem.style.height = "32px";
  // remove the text inside the div
  divElem.innerHTML = "";
  // set the background image
  divElem.style.backgroundImage = "url(https://mainline.i3s.unice.fr/mooc/marioSprite.png)";
  // remove the background color
  divElem.style.backgroundColor = "transparent";
  // select the starting pos in the background image
  var offset = indexImage * 24;
  divElem.style.backgroundPosition  = offset + "px";
}
