
function initPreferences() {
  console.log("Adding input listener to all input fields");
  // add an input listener to all input fields
  var listOfInputsInForm = document.querySelectorAll("input");
   for(var i= 0; i < listOfInputsInForm.length; i++) {
     addInputListener(listOfInputsInForm[i]);
   }
  
  // restore preferences
  restorePreferences();
  
  applyGUIvalues();
}

function addInputListener(inputField) {
  inputField.addEventListener('input', function(event) {
    localStorage.setItem(inputField.id, inputField.value);
  }, false);
}

function restorePreferences() {
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

function applyGUIvalues() {
  var sizeWidget = document.getElementById("size");
  size = Math.sign(incX)*parseInt(sizeWidget.value);
  document.getElementById("sizeValue").innerHTML = size;
  
  var colorWidget = document.getElementById("color");
  ctx.fillStyle = colorWidget.value;
  
  var speedWidget = document.getElementById("speed");
  incX = Math.sign(incX)*parseInt(speedWidget.value);
  document.getElementById("speedValue").innerHTML = Math.abs(incX);
  
  var lineWidthWidget = document.getElementById("lineWidth");
  ctx.lineWidth = parseInt(lineWidthWidget.value);
}


