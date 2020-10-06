var canvas, ctx, grd;

function init() {
  // Good practice 1: set global vars  canvas, ctx, gradients, etc here
   canvas = document.querySelector('#myCanvas1');
   ctx = canvas.getContext('2d');
  
   grd = ctx.createRadialGradient(150, 100, 30, 210, 100, 100);
   grd.addColorStop(0, "red");
   grd.addColorStop(0.17, "orange");
   grd.addColorStop(0.33, "yellow");
   grd.addColorStop(0.5, "green");
   grd.addColorStop(0.666, "blue");
   grd.addColorStop(1, "violet");

  draw();
}

function draw() {
  ctx.fillStyle = grd;
  ctx.fillRect(0, 0, 300, 200);
}
