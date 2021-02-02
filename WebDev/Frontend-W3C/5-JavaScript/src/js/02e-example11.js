function add() {
  // get the current value of the input field
  var val = document.querySelector('#newNumber').value;
  
  if((val !== undefined) && (val !== "")) {
    // val exists and non empty
    
    // get the list of numbers. It's a <ul>
    var ul = document.querySelector("#numbers");
     
    ul.innerHTML += "<li>" + val + "</li>";
  }
}

function reset() {
  document.querySelector("#numbers").innerHTML = "";
}
