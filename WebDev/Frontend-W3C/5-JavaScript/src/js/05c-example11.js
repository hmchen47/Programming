 function checkPasswords() {
    var password1 = document.querySelector('#password1');
    var password2 = document.querySelector('#password2');
   
    // Use HTML5 form validation API
    if (password1.value !== password2.value) {
       // password2 input field is invalid
       password2.setCustomValidity('Passwords are different');
    } else {
      // call to setCustomValidity with an empty arguments
      // indicates that the input field is valid
       password2.setCustomValidity('');
    }
}

function submitForm() {
  document.body.append("We can submit, the form is valid!");
  
  // Here, for example, we can do what we want with the data
  // Send to a server using Ajax,
  // show the data in a table,
  // save data client-side, etc.
  
  // returning false will not submit the form
  return false;
}

