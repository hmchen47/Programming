var canvas, ctx;
var inputStates = {};

window.onload = function init() {
    canvas = document.getElementById('myCanvas');
    ctx = canvas.getContext('2d');

    canvas.addEventListener('mousemove', function (evt) {
        inputStates.mousePos = getMousePos(canvas, evt);
        var message = 'Mouse position: ' + inputStates.mousePos.x + ',' + inputStates.mousePos.y;
        writeMessage(canvas, message);
    }, false);

      canvas.addEventListener('mousedown', function (evt) {
        inputStates.mousedown = true;
        inputStates.mouseButton = evt.button;
        var message = "Mouse button " + evt.button + " down at position: " + inputStates.mousePos.x + ',' + inputStates.mousePos.y;
        writeMessage(canvas, message);
    }, false);

        canvas.addEventListener('mouseup', function (evt) {
        inputStates.mousedown = false;
        var message = "Mouse up at position: " + inputStates.mousePos.x + ',' + inputStates.mousePos.y;
        writeMessage(canvas, message);
    }, false);
};



function writeMessage(canvas, message) {
    var ctx = canvas.getContext('2d');
    ctx.save();
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.font = '18pt Calibri';
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


