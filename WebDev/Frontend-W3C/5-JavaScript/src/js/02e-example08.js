window.onload = init;

function init() {
  // DOM is ready
  var firstP = document.querySelector("#first");
  console.log(firstP.textContent);
  console.log(firstP.innerHTML);

  firstP.textContent = "Hello I'm the first paragraph";
  console.log(firstP.textContent);

  var secondP = document.querySelector("#second");
  console.log(secondP.textContent);
  console.log(secondP.innerHTML);
  
  secondP.textContent = "Hello I'm the second paragraph";
  console.log(secondP.textContent);
  console.log(secondP.innerHTML);
}