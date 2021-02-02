function add() {
  // get the current value of the input field
  var val = document.querySelector('#newNumber').value;
  if((val !== undefined) && (val !== "")) {
    // val exists and non empty
    // get the list of numbers. It's a <ul>
    var ul = document.querySelector("#numbers");
    // add it to the list as a new <li>
    var newNumber = document.createElement("li");
    newNumber.textContent = val;
    // or newNumber.innerHTML = val
    ul.append(newNumber);
  }
}
 
function reset() {
  // get the list of numbers. It's a <ul>
  var ul = document.querySelector("#numbers");
  // reset it: no children
  ul.innerHTML = ""; 
}
