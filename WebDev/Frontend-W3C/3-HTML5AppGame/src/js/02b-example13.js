window.addEventListener("gamepadconnected", function(e) {
   var gamepad = e.gamepad;
   var index = gamepad.index;
   var id = gamepad.id;
   var nbButtons = gamepad.buttons.length;
   var nbAxes = gamepad.axes.length;
   console.log("Gamepad No " + index +
               ", with id " + id + " is connected. It has " +
               nbButtons + " buttons and " +
               nbAxes + " axes");
});

window.addEventListener("gamepaddisconnected", function(e) {
   var gamepad = e.gamepad;
   var index = gamepad.index;
   console.log("Gamepad No " + index + " has been disconnected");
});

