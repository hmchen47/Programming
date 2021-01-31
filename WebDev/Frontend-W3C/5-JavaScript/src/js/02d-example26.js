function doSomething(evt) {
  // this is the slider value
  var val = evt.target.value;  
  
  // get the output div
  var output = document.querySelector('#sliderValue');
  // display the value typed in the div 
  output.innerHTML = "Value selected: " + val;
}
