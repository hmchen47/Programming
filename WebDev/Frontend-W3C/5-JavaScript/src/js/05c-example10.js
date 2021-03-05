function validateName(evt) {
  // this is the input field text content
  var key = evt.key;  
  
  // get the output div
  var output = document.querySelector('#keyTyped');
  // display the value typed in the div 
  output.innerHTML = "Valid key: " + key;
  
  // You can do validation here, set the input field to
  // invalid is the name contains forbidden characters
  // or is too short
  // for example, let's forbid names with length < 5 chars
  if(key === "!") {
    output.innerHTML = "This key is forbidden!";
    // remove the forbidden char
    // current typed value
    var name = evt.target.value;
    // we use the substring JavaScript function
    // to remove the last character
    // first parameter = start index
    // second = last index
    evt.target.value = name.substring(0, name.length-1);
  }
}

