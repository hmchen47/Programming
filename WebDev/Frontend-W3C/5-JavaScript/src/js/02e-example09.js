function resetName() {
  var inputField = document.querySelector("#name");
  inputField.value = "";
}

function setToGreen() {
  var colorChooser = document.querySelector("#color");
  colorChooser.value = "#00FF00";
}

function changeStep() {
  var number = document.querySelector("#number");
  number.value = 10;
  number.step = "0.1";
  number.max = 11;
}

function changeAndResize(img) {
    img.src="https://pbs.twimg.com/profile_images/110455194/n666194627_2302_400x400.jpg";
  img.width=250;
  img.style.border = "4px solid red";
}
