
function displayListOfCheckedItems() {
  // all inputs that have been checked
  var listOfSelectedValues="";
  
  var list = document.querySelectorAll("#fruits input:checked");  
  list.forEach(function(elm) {
    listOfSelectedValues += elm.value + " ";
    
    // get the li parent of the current selected input
    var liParent = elm.parentNode;
    // add the CSS class .checked
    liParent.classList.add("checked");
  });
  document.body.append("You selected: " + listOfSelectedValues);
}

function reset() {
  var list = document.querySelectorAll("#fruits input");  
  list.forEach(function(elm) {
    // uncheck
    elm.checked = false;
    
    // remove CSS decoration
    var liParent = elm.parentNode;
    liParent.classList.remove("checked");
  });
}
