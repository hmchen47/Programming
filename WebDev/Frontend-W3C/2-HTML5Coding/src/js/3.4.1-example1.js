
var canvas, ctx, w, h;
 
function init() {
  canvas = document.getElementById('myCanvas');
  ctx = canvas.getContext('2d');
  
  w = canvas.width;
  h = canvas.height;
  
  console.time("time to draw");
  
  for(var i=0; i < 1000; i++) {
    var x = Math.random() * w;
    var y = Math.random() * h;
    var width = Math.random() * w;
    var height = Math.random() * h;
    
    ctx.strokeRect(x, y, width, height); 
  }
  console.timeEnd("time to draw");
}


