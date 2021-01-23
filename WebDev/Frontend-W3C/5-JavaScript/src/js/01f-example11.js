var canvas, ctx, painting = false, previousMousePos;

function getMousePos(canvas, evt) {
  // necessary to take into account CSS boudaries
  var rect = canvas.getBoundingClientRect();
  return {
    x: evt.clientX - rect.left,
    y: evt.clientY - rect.top
  };
}

function drawLineImmediate(x1, y1, x2, y2) {
  // a line is a path with a single draw order
  // we need to do that in this example otherwise
  // at each mouse event we would draw the whole path
  // since the beginning. Remember that lines
  // normally are only usable in path mode
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
}

function handleMouseMove(evt) {
  var mousePos = getMousePos(canvas, evt);

  // Let's draw some lines that follow the mouse pos
  if (painting) {
    drawLineImmediate(previousMousePos.x, previousMousePos.y,
                      mousePos.x, mousePos.y);

    previousMousePos = mousePos;
  }
}

function clicked(evt) {
  previousMousePos = getMousePos(canvas, evt);
  painting = true;
}

function released(evt) {
  painting = false;
}

window.onload = function () {
  canvas = document.getElementById('myCanvas');
  ctx = canvas.getContext('2d');
  painting = false;

  canvas.addEventListener('mousemove', handleMouseMove, false);
  canvas.addEventListener('mousedown', clicked);
  canvas.addEventListener('mouseup', released);
};
