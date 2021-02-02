// useful to have them as global variables
var canvas, ctx;

window.onload = function init() {
    // called AFTER the page has been loaded
    canvas = document.querySelector("#myCanvas");
    // important, we will draw with this object
    ctx = canvas.getContext('2d');
  
    // ready to go !
    // filled rectangle
    ctx.fillStyle = 'red';
    ctx.fillRect(10, 10, 30, 30);
  
    // wireframe rectangle
    ctx.strokeStyle = 'green';
    ctx.lineWidth = 4;
    ctx.strokeRect(100, 40, 40, 40);
  
    // fill circle, will use current ctx.fillStyle
    ctx.beginPath();
    ctx.arc(60, 60, 10, 0, 2*Math.PI);
    ctx.fill();
  
    // some text
    ctx.fillStyle = "purple";
    ctx.font = "20px Arial";
    ctx.fillText("Hello!", 60, 20);
}

