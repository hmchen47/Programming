
function displayListOfCheckedItems() {
  // all inputs that have been checked
  var listOfSelectedValues="";
  
  var list = document.querySelectorAll("#fruits input:checked");  
  list.forEach(function(elm) {
    listOfSelectedValues += elm.value + " ";
    
    // Put the li in red.
    // the li is the parent of the current input elem stored
    // in the elm variable
    elm.parentNode.style.color = 'green';
  });
  document.body.append("You selected: " + listOfSelectedValues);
}
