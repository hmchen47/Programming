var canvas, ctx, grdFrenchFlag;

function init() {
  // Good practice 1: set global vars  canvas, ctx, gradients, etc here
   canvas = document.querySelector('#myCanvas1');
   ctx = canvas.getContext('2d');
  
   // The gradient we create is also a global variable, we
   // will be able to reuse it for drawing different shapes
   // in different functions
  grdFrenchFlag = ctx.createLinearGradient(0, 0, 300, 200);
              
  // Try adding colors with first parameter between 0 and 1
  grdFrenchFlag.addColorStop(0, "blue"); 
  grdFrenchFlag.addColorStop(0.5, "white");
  grdFrenchFlag.addColorStop(1, "red"); 

  draw();
}

function draw() {
  ctx.fillStyle = grdFrenchFlag;
  ctx.fillRect(0, 0, 300, 200);
}

