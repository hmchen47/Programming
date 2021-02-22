function changePageBackgroundColor(color) {
document.body.style.backgroundColor = color;  
  // get the output div
  var output = document.querySelector('#choosedColor');
  // display the value typed in the div 
  output.innerHTML = "Color selected: " + color;
}
