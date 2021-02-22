function changeCSSStyle(id) {
  var p = document.querySelector("#p1");

  p.style.color = 'red';
  p.innerHTML = 'style.color used to change the color';

  p = document.querySelector("#p2");

  p.style.backgroundColor = 'lightGreen';
  p.innerHTML = 'style.backgroundColor used';

  p = document.querySelector("#p3");

  p.style.marginLeft = '100px';
  p.innerHTML = 'style.leftMargin used to shift this paragraph 100px to the right';
  
  p = document.querySelector("#p4");

  p.style.border = '2px solid blue';
  p.style.padding = "20px";
  p.innerHTML = 'style.border and style.padding (internal margins) used';


  p = document.querySelector("#p6");

  p.style.textAlign = 'center';
  p.style.border = "1px dashed red";
  // for boxShadow: h-shadow v-shadow blur spread color
  p.style.boxShadow = "2px 2px 5px 0px grey";
  p.innerHTML = 'style.textAlign, style.border, style.bowShadow used';

}
