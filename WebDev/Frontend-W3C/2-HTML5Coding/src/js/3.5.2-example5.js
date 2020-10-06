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

  drawCheckboard(5);
}

// n = number of cells per row/column
function drawCheckboard(n) {
  ctx.strokeStyle = grdFrenchFlag;
  ctx.lineWidth=10;
  
  var l = canvas.width;
  var h = canvas.height;

  var cellWidth = l / n;
  var cellHeight = h / n;
  
  for(i = 0; i < n; i++) {
    for(j = i % 2; j < n; j+=2) {
      ctx.strokeRect(cellWidth*(i), cellHeight*j, cellWidth, cellHeight); 
    }  
  }
}

