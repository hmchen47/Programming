window.onload = init();

function init() {
  var a = ['Monday', 'Tuesday', 'Wednesday'];

  a.forEach(function(day) {
    document.body.innerHTML += day + "<br>"; // will display Monday, Tuesday, Wednesday
  });
}


