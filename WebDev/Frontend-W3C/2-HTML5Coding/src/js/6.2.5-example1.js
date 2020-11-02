function sendForm() {
  console.log("in sendForm()");
  
  // SEND THE FORM USING AJAX
  
  // PERFORM CUSTOM VALIDATION
  
  return false;
}

// Called when the page is loaded
window.onload = init;

function init() {
  console.log("Adding input listener to all input fields");
  // add an input listener to all input fields
  var listOfInputsInForm = document.querySelectorAll("input");
   for(var i= 0; i < listOfInputsInForm.length; i++) {
     addInputListener(listOfInputsInForm[i]);
   }
  
  // restore form content with previously saved values
  restoreFormContent();
}

function addInputListener(inputField) {
  inputField.oninput = function(event) {
    localStorage.setItem(inputField.id, inputField.value);
  };
}

function restoreFormContent() {
  console.log("restoring form content from localStorage");
  
  // get the list of all input elements in the form
  var listOfInputsInForm = document.querySelectorAll("input");
  
  // For each input element, 
  //    - get its id (that is also the key for it's saved content 
  //      in the localStorage)
  //    - get the value associated with the id/key in the local
  //      storage
  //    - If the value is not undefined, restore the value
  //      of the input field
  for(var i= 0; i < listOfInputsInForm.length; i++) {
    var fieldToRestore = listOfInputsInForm[i];
    var id = fieldToRestore.id;
    var savedValue = localStorage.getItem(id);
    
    if(savedValue !== undefined) {
      fieldToRestore.value = savedValue;
    }
  }
}

