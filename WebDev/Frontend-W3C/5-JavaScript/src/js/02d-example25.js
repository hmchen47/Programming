function validateName(field) {
  // this is the input field text content
  var name = field.value;  
  
  // get the output div
  var output = document.querySelector('#nameTyped');
  // display the value typed in the div 
  output.innerHTML = "Valid name: " + name;
  
  // You can do validation here, set the input field to
  // invalid is the name contains forbidden characters
  // or is too short
  // for example, let's forbid names with length < 5 chars
  if(name.length < 5) {
    output.innerHTML = "This name is too short (at least 5 chars)";
  }
}
