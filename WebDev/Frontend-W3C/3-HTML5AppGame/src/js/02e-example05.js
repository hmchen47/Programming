// Inits
window.onload = function init() {
    var game = new GF();
    game.start();
};


// GAME FRAMEWORK STARTS HERE
var GF = function () {
// Vars relative to the canvas
    var canvas, ctx, w, h;

// vars for counting frames/s, used by the measureFPS function
    var frameCount = 0;
    var lastTime;
    var fpsContainer;
    var fps;

// vars for handling inputs
    var inputStates = {};

// The monster !
    var monster = {
        x: 80,
        y: 80,
        width: 100,
        height: 100,
        speed: 1,
        boundingCircleRadius: 70
    };

    var player = {
        x: 0,
        y: 0,
        boundingCircleRadius: 20
    };

    var measureFPS = function (newTime) {

// test for the very first invocation
        if (lastTime === undefined) {
            lastTime = newTime;
            return;
        }

//calculate the difference between last & current frame
        var diffTime = newTime - lastTime;

        if (diffTime >= 1000) {
            fps = frameCount;
            frameCount = 0;
            lastTime = newTime;
        }

//and display it in an element we appended to the 
// document in the start() function
        fpsContainer.innerHTML = 'FPS: ' + fps;
        frameCount++;
    };

// clears the canvas content
    function clearCanvas() {
        ctx.clearRect(0, 0, w, h);
    }

// Functions for drawing the monster and maybe other objects
    function drawMyMonster() {
// draw a big monster !
// head

// save the context
        ctx.save();

// translate the coordinate system, draw relative to it
        ctx.translate(monster.x - monster.width / 2, monster.y - monster.height / 2);

// (0, 0) is the top left corner of the monster.
        ctx.strokeRect(0, 0, monster.width, monster.height);

// eyes
        ctx.fillRect(20, 20, 10, 10);
        ctx.fillRect(65, 20, 10, 10);

// nose
        ctx.strokeRect(45, 40, 10, 40);

// mouth
        ctx.strokeRect(35, 84, 30, 10);

// teeth
        ctx.fillRect(38, 84, 10, 10);
        ctx.fillRect(52, 84, 10, 10);

// Draw bounding circle
        ctx.beginPath();
        ctx.arc(50, 50, monster.boundingCircleRadius, 0, 2 * Math.PI);
        ctx.stroke();

// restore the context
        ctx.restore();
    }

    var mainLoop = function (time) {
//main function, called each frame 
        measureFPS(time);

// Clear the canvas
        clearCanvas();

// draw the monster
        drawMyMonster();

// Check inputs and move the monster
        updateMonsterPosition();

        updatePlayer();

        checkCollisions();

// call the animation loop every 1/60th of second
        requestAnimationFrame(mainLoop);
    };


    function updatePlayer() {
// The player is just a square, drawn at the mouse position
// Just to test rectangle/rectangle collisions.

        if (inputStates.mousePos) {
            player.x = inputStates.mousePos.x;
            player.y = inputStates.mousePos.y;

// draws a rectangle centered on the mouse position
// we draw it as a square.
// We remove size/2 to the x and y position at drawing time in
// order to recenter the rectangle on the mouse pos (normally 
// the 0, 0 of a rectangle is at its top left corner)
            var size = player.boundingCircleRadius;
            ctx.fillRect(player.x - size / 2, player.y - size / 2, size, size);
        }
    }

    function checkCollisions() {
// Bounding rect position and size for the player. We need to translate
// it half the player size
        var playerSize = player.boundingCircleRadius;
        var playerXBoundingRect = player.x - playerSize / 2;
        var playerYBoundingRect = player.y - playerSize / 2;
// Same with the monster bounding rect
        var monsterXBoundingRect = monster.x - monster.width / 2;
        var monsterYBoundingRect = monster.y - monster.height / 2;


        if (rectsOverlap(playerXBoundingRect, playerYBoundingRect, playerSize, playerSize, monsterXBoundingRect, monsterYBoundingRect, monster.width, monster.height)) {
            ctx.fillText("Collision", 150, 20);
            ctx.strokeStyle = ctx.fillStyle = 'red';
        } else {
            ctx.fillText("No collision", 150, 20);
            ctx.strokeStyle = ctx.fillStyle = 'black';
        }
    }


// Collisions between aligned rectangles
    function rectsOverlap(x1, y1, w1, h1, x2, y2, w2, h2) {

        if ((x1 > (x2 + w2)) || ((x1 + w1) < x2))
            return false; // No horizontal axis projection overlap
        if ((y1 > (y2 + h2)) || ((y1 + h1) < y2))
            return false; // No vertical axis projection overlap
        return true;    // If previous tests failed, then both axis projections
// overlap and the rectangles intersect
    }
    function circleCollide(x1, y1, r1, x2, y2, r2) {
        var dx = x1 - x2;
        var dy = y1 - y2;
        return ((dx * dx + dy * dy) < (r1 + r2) * (r1 + r2));
    }

    function updateMonsterPosition() {
        monster.speedX = monster.speedY = 0;
// check inputStates
        if (inputStates.left) {
            ctx.fillText("left", 150, 20);
            monster.speedX = -monster.speed;
        }
        if (inputStates.up) {
            ctx.fillText("up", 150, 40);
            monster.speedY = -monster.speed;
        }
        if (inputStates.right) {
            ctx.fillText("right", 150, 60);
            monster.speedX = monster.speed;
        }
        if (inputStates.down) {
            ctx.fillText("down", 150, 80);
            monster.speedY = monster.speed;
        }
        if (inputStates.space) {
            ctx.fillText("space bar", 140, 100);
        }
        if (inputStates.mousePos) {
            ctx.fillText("x = " + inputStates.mousePos.x + " y = " + inputStates.mousePos.y, 5, 200);
        }
        if (inputStates.mousedown) {
            ctx.fillText("mousedown b" + inputStates.mouseButton, 5, 180);
            monster.speed = 5;
        } else {
// mouse up
            monster.speed = 1;
        }

        monster.x += monster.speedX;
        monster.y += monster.speedY;

    }


    function getMousePos(evt) {
// necessary to take into account CSS boudaries
        var rect = canvas.getBoundingClientRect();
        return {
            x: evt.clientX - rect.left,
            y: evt.clientY - rect.top
        };
    }

    var start = function () {
// adds a div for displaying the fps value
        fpsContainer = document.createElement('div');
        document.body.appendChild(fpsContainer);

// Canvas, context etc.
        canvas = document.querySelector("#myCanvas");

// often useful
        w = canvas.width;
        h = canvas.height;

// important, we will draw with this object
        ctx = canvas.getContext('2d');
// default police for text
        ctx.font = "20px Arial";

//add the listener to the main, window object, and update the states
        window.addEventListener('keydown', function (event) {
            if (event.keyCode === 37) {
                inputStates.left = true;
            } else if (event.keyCode === 38) {
                inputStates.up = true;
            } else if (event.keyCode === 39) {
                inputStates.right = true;
            } else if (event.keyCode === 40) {
                inputStates.down = true;
            } else if (event.keyCode === 32) {
                inputStates.space = true;
            }
        }, false);

//if the key will be released, change the states object 
        window.addEventListener('keyup', function (event) {
            if (event.keyCode === 37) {
                inputStates.left = false;
            } else if (event.keyCode === 38) {
                inputStates.up = false;
            } else if (event.keyCode === 39) {
                inputStates.right = false;
            } else if (event.keyCode === 40) {
                inputStates.down = false;
            } else if (event.keyCode === 32) {
                inputStates.space = false;
            }
        }, false);

// Mouse event listeners
        canvas.addEventListener('mousemove', function (evt) {
            inputStates.mousePos = getMousePos(evt);
        }, false);

        canvas.addEventListener('mousedown', function (evt) {
            inputStates.mousedown = true;
            inputStates.mouseButton = evt.button;
        }, false);

        canvas.addEventListener('mouseup', function (evt) {
            inputStates.mousedown = false;
        }, false);


// start the animation
        requestAnimationFrame(mainLoop);
    };

//our GameFramework returns a public API visible from outside its scope
    return {
        start: start
    };
};

