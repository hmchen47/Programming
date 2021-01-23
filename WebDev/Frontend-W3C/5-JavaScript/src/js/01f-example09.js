var field, theDiv;

function init() {
  console.log("page loaded and DOM is ready");
  field = document.querySelector("#inputField");
  theDiv = document.querySelector("#theDiv");
}

// The next function is called each type a key has been
// typed in the input field
function showWhatWeTyped() {
  // fill the div with the content of the input field
  theDiv.innerHTML = field.value;
}
