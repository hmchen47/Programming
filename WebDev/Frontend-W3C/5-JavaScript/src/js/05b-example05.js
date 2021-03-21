var canvas, ctx, width, height;
var rect = {x:40, y:40, radius: 30, width:40, height:40, v:3};
var mousepos = {x:0, y:0};

function init() {
  canvas = document.querySelector("#myCanvas");
  ctx = canvas.getContext('2d');
  width = canvas.width;
  height = canvas.height; 
  
  canvas.addEventListener('mousemove', function (evt) {
        mousepos = getMousePos(canvas, evt);
     }, false); 
 
  mainloop();
}


function mainloop() {
    // 1) clear screen
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  
    // 2) move object
    var dx = rect.x - mousepos.x;
    var dy = rect.y - mousepos.y;
    var angle = Math.atan2(dy, dx);
  
    rect.x -= rect.v*Math.cos(angle);   
    rect.y -= rect.v*Math.sin(angle); 
  
    // 3) draw object
    drawRectangle(angle);
  
    // 4) request new frame
     window.requestAnimationFrame(mainloop);
}
 
function drawRectangle(angle) {
  ctx.save();
  
  // These two lines move the coordinate system
  ctx.translate(rect.x, rect.y);
  ctx.rotate(angle);
  // recenter the coordinate system in the middle
  // the rectangle. Like that it will rotate around
  // this point instead of top left corner
  ctx.translate(-rect.width/2, -rect.height/2);
  
  ctx.fillRect(0, 0, rect.width, rect.height);
  ctx.restore();
}

function getMousePos(canvas, evt) {
  // necessary to take into account CSS boudaries
  var rect = canvas.getBoundingClientRect();
  return {
     x: evt.clientX - rect.left,
     y: evt.clientY - rect.top
  };
}
