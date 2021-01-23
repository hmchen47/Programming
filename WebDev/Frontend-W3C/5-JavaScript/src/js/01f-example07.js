var divElem;

function init() {
  console.log("page loaded and DOM is ready");
  
  // use the selection API to select the div
  divElem = document.querySelector("#theDiv");
}

function addImageIntoBackground() {
  divElem.innerHTML = "";
  divElem.style.width= "100%";
  divElem.style.height = "300px";
  divElem.style.backgroundImage = "url(https://mainline.i3s.unice.fr/mooc/marioSprite.png)";
}

