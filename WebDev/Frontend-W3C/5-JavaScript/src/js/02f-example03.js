// useful to have them as global variables
var canvas, ctx, w, h; 


window.onload = function init() {
    // called AFTER the page has been loaded
    canvas = document.querySelector("#myCanvas");
  
    // often useful
    w = canvas.width; 
    h = canvas.height;  
  
    // important, we will draw with this object
    ctx = canvas.getContext('2d');
  
    // ready to go !
    // Try to change the parameter values to move
    // the monster
    drawMyMonster(10, 10);
};

function drawMyMonster(x, y) {
    // draw a big monster !
    // head
  
    // GOOD practice: save the context, use 2D trasnformations
    ctx.save();
  
    // translate the coordinate system, draw relative to it
    ctx.translate(x, y);
  
    // (0, 0) is the top left corner of the monster.
    ctx.strokeRect(0, 0, 100, 100);
  
    // eyes, x=20, y=20 is relative to the top left corner
    // of the previous rectangle
    ctx.fillRect(20, 20, 10, 10);
    ctx.fillRect(65, 20, 10, 10);
  
    // nose
    ctx.strokeRect(45, 40, 10, 40);
  
    // mouth
   ctx.strokeRect(35, 84, 30, 10);
  
   // teeth
   ctx.fillRect(38, 84, 10, 10);
   ctx.fillRect(52, 84, 10, 10);
  
   // GOOD practice: restore the context
   ctx.restore();
}
