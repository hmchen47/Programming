var canvas = document.querySelector('#myCanvas');
var ctx = canvas.getContext('2d');

var contextX = 100;
var contextY = 10;
var endPointX = 200;
var endPointY = 120;
var controlPointX = 35;
var controlPointY = 70;

drawCurvedArrow(contextX, contextY,
                endPointX, endPointY,
                controlPointX, controlPointY,
                3, // arrowWidth, try 30 for example !
                20, // width of the arrow head, try smaller values, 10...
                'blue');


function drawCurvedArrow(startPointX, startPointY,
                         endPointX, endPointY,
                         quadPointX, quadPointY,
                         lineWidth,
                         arrowWidth, 
                         color) {
  // GOOD PRACTICE: the function changes color and lineWidth -> save context!
  ctx.save();
  ctx.strokeStyle = color;
  ctx.lineWidth = lineWidth;

  // angle of the end tangeant, useful for drawing the arrow head
  var arrowAngle = Math.atan2(quadPointX - endPointX, quadPointY - endPointY) + Math.PI;

  // start a new path
  ctx.beginPath();
  ctx.moveTo(startPointX, startPointY);

  ctx.quadraticCurveTo(quadPointX, quadPointY, endPointX, endPointY);

  ctx.moveTo(endPointX - (arrowWidth * Math.sin(arrowAngle - Math.PI / 6)), 
             endPointY - (arrowWidth * Math.cos(arrowAngle - Math.PI / 6)));

  ctx.lineTo(endPointX, endPointY);

  ctx.lineTo(endPointX - (arrowWidth * Math.sin(arrowAngle + Math.PI / 6)), 
             endPointY - (arrowWidth * Math.cos(arrowAngle + Math.PI / 6)));

  ctx.stroke();
  ctx.closePath();
  
  // GOOD PRACTICE -> restore the context as we saved it at the beginning
  // of the function
  ctx.restore();
}

