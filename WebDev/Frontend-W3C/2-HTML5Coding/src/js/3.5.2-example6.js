var canvas, ctx, grdFrenchFlag;

function init() {
  // Good practice 1: set global vars  canvas, ctx, gradients, etc here
   canvas = document.querySelector('#myCanvas1');
   ctx = canvas.getContext('2d');

  drawCheckboard(5);
}

function setGradient(x, y, width, height) {
    grdFrenchFlag = ctx.createLinearGradient(x, y, width, height);
              
  grdFrenchFlag.addColorStop(0, "blue"); 
  grdFrenchFlag.addColorStop(0.5, "white");
  grdFrenchFlag.addColorStop(1, "red"); 
  ctx.fillStyle = grdFrenchFlag;

}

// n = number of cells per row/column
function drawCheckboard(n) {
  
  var l = canvas.width;
  var h = canvas.height;

  var cellWidth = l / n;
  var cellHeight = h / n;
  
  for(i = 0; i < n; i+=2) {
    for(j = 0; j < n; j++) {
      var x = cellWidth*(i+j%2);
      var y = cellHeight*j;
      setGradient(x, y, x+cellWidth, y+cellHeight);
      ctx.fillRect(x, y, cellWidth, cellHeight); 
    }  
  }
}

