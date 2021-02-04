var canvas, ctx, mousePos, mouseButton;

window.onload = function init() {
    canvas = document.getElementById('myCanvas');
    ctx = canvas.getContext('2d');

    canvas.addEventListener('mousemove', function (evt) {
        mousePos = getMousePos(canvas, evt);
        var message = 'Mouse position: ' + mousePos.x + ',' + mousePos.y;
        writeMessage(canvas, message);
    }, false);

      canvas.addEventListener('mousedown', function (evt) {
        mouseButton = evt.button;
        var message = "Mouse button " + evt.button + " down at position: " + mousePos.x + ',' + mousePos.y;
        writeMessage(canvas, message);
    }, false);

    canvas.addEventListener('mouseup', function (evt) {
        var message = "Mouse up at position: " + mousePos.x + ',' + mousePos.y;
        writeMessage(canvas, message);
    }, false);
};



function writeMessage(canvas, message) {
    ctx.save();
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.font = '12pt Calibri';
    ctx.fillStyle = 'black';
    ctx.fillText(message, 10, 25);
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


