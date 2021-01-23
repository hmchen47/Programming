var divElem;

function init() {
  console.log("page loaded and DOM is ready");
  
  // use the selection API to select the div
  divElem = document.querySelector("#theDiv");
}

function changeStyle() {
  console.log("add border");
  divElem.style.border = "5px dashed purple";
  divElem.style.padding = "10px";
  divElem.style.backgroundColor = "lightGreen";
}

