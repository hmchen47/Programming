// Inits
window.onload = function init() {
    var game = new GF();
    game.start();
};

// GAME FRAMEWORK STARTS HERE
var GF = function () {
    // Vars relative to the canvas
    var canvas, ctx, w, h;

    // vars for handling inputs
    var inputStates = {};

    // game states
    var gameStates = {
        mainMenu: 0,
        gameRunning: 1,
        gameOver: 2
    };
    var currentGameState = gameStates.gameRunning;
    var currentLevel = 1;
    var TIME_BETWEEN_LEVELS = 5000; // 5 seconds
    var currentLevelTime = TIME_BETWEEN_LEVELS;
    var plopSound; // Sound of a ball exploding

    // The monster !
    var monster = {
        dead: false,
        x: 10,
        y: 10,
        width: 50,
        height: 50,
        speed: 100 // pixels/s this time !
    };

    // array of balls to animate
    var ballArray = [];
    var nbBalls = 5;

    // clears the canvas content
    function clearCanvas() {
        ctx.clearRect(0, 0, w, h);
    }

    // Functions for drawing the monster and maybe other objects
    function drawMyMonster(x, y) {
        // draw a big monster !
        // head

        // save the context
        ctx.save();

        // translate the coordinate system, draw relative to it
        ctx.translate(x, y);
        ctx.scale(0.5, 0.5);

        // (0, 0) is the top left corner of the monster.
        ctx.strokeRect(0, 0, 100, 100);

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

        // restore the context
        ctx.restore();
    }

    
    var mainLoop = function (time) {
        //main function, called each frame 
        measureFPS(time);

        // number of ms since last frame draw
        delta = timer(time);

        // Clear the canvas
        clearCanvas();

        if (monster.dead) {
            currentGameState = gameStates.gameOver;
        }

        switch (currentGameState) {
            case gameStates.gameRunning:

                // draw the monster
                drawMyMonster(monster.x, monster.y);

                // Check inputs and move the monster
                updateMonsterPosition(delta);

                // update and draw balls
                updateBalls(delta);

                // display Score
                displayScore();

                // decrease currentLevelTime. 
                // When < 0 go to next level
                currentLevelTime -= delta;

                if (currentLevelTime < 0) {
                    goToNextLevel();
                }

                break;
            case gameStates.mainMenu:
                // TO DO !
                break;
            case gameStates.gameOver:
                ctx.fillText("GAME OVER", 50, 100);
                ctx.fillText("Press SPACE to start again", 50, 150);
                ctx.fillText("Move with arrow keys", 50, 200);
                ctx.fillText("Survive 5 seconds for next level", 50, 250);
                if (inputStates.space) {
                    startNewGame();
                }
                break;
        }

        // call the animation loop every 1/60th of second
        requestAnimationFrame(mainLoop);
    };

    function startNewGame() {
        monster.dead = false;
        currentLevelTime = 5000;
        currentLevel = 1;
        nbBalls = 5;
        createBalls(nbBalls);
        currentGameState = gameStates.gameRunning;
    }

    function goToNextLevel() {
        // reset time available for next level
        // 5 seconds in this example
        currentLevelTime = 5000;
        currentLevel++;
        // Add two balls per level
        nbBalls += 2;
        createBalls(nbBalls);
    }

    function displayScore() {
        ctx.save();
        ctx.fillStyle = 'Green';
        ctx.fillText("Level: " + currentLevel, 300, 30);
        ctx.fillText("Time: " + (currentLevelTime / 1000).toFixed(1), 300, 60);
        ctx.fillText("Balls: " + nbBalls, 300, 90);
        ctx.restore();
    }
    function updateMonsterPosition(delta) {
        monster.speedX = monster.speedY = 0;
        // check inputStates
        if (inputStates.left) {
            monster.speedX = -monster.speed;
        }
        if (inputStates.up) {
            monster.speedY = -monster.speed;
        }
        if (inputStates.right) {
            monster.speedX = monster.speed;
        }
        if (inputStates.down) {
            monster.speedY = monster.speed;
        }
        if (inputStates.space) {
        }
        if (inputStates.mousePos) {
        }
        if (inputStates.mousedown) {
            monster.speed = 500;
        } else {
            // mouse up
            monster.speed = 100;
        }

        // Compute the incX and inY in pixels depending
        // on the time elasped since last redraw
        monster.x += calcDistanceToMove(delta, monster.speedX);
        monster.y += calcDistanceToMove(delta, monster.speedY);
    }

    function updateBalls(delta) {
        // Move and draw each ball, test collisions, 
        for (var i = 0; i < ballArray.length; i++) {
            var ball = ballArray[i];

            // 1) move the ball
            ball.move();

            // 2) test if the ball collides with a wall
            testCollisionWithWalls(ball, w, h);

            // Test if the monster collides
            if (circRectsOverlap(monster.x, monster.y,
                    monster.width, monster.height,
                    ball.x, ball.y, ball.radius)) {

                //change the color of the ball
                ball.color = 'red';
                monster.dead = true;
                // Here, a sound effect greatly improves
                // the experience!
                plopSound.play();
            }

            // 3) draw the ball
            ball.draw(ctx);
        }
    }

 

    function createBalls(numberOfBalls) {
        // Start from an empty array
        ballArray = [];

        for (var i = 0; i < numberOfBalls; i++) {
            // Create a ball with random position and speed. 
            // You can change the radius
            var ball = new Ball(w * Math.random(),
                    h * Math.random(),
                    (2 * Math.PI) * Math.random(),
                    (80 * Math.random()),
                    30);

            // Do not create a ball on the player. We augmented the ball radius 
            // to sure the ball is created far from the monster. 
            if (!circRectsOverlap(monster.x, monster.y,
                    monster.width, monster.height,
                    ball.x, ball.y, ball.radius * 3)) {
                // Add it to the array
                ballArray[i] = ball;
            } else {
                i--;
            }


        }
    }

    function loadAssets(callback) {
        // here we should load the souds, the sprite sheets etc.
        // then at the end call the callback function

        // simple example that loads a sound and then calls the callback. We used the howler.js WebAudio lib here.
        // Load sounds asynchronously using howler.js
        plopSound = new Howl({
            urls: ['http://mainline.i3s.unice.fr/mooc/plop.mp3'],
            autoplay: false,
            volume: 1,
            onload: function () {
                console.log("all sounds loaded");
                // We're done!
                callback();
            }
        });
    }
    var start = function () {
        initFPSCounter();

        // Canvas, context etc.
        canvas = document.querySelector("#myCanvas");

        // often useful
        w = canvas.width;
        h = canvas.height;

        // important, we will draw with this object
        ctx = canvas.getContext('2d');
        // default police for text
        ctx.font = "20px Arial";

        // Create the different key and mouse listeners
        addListeners(inputStates, canvas);

        // We create tge balls: try to change the parameter
        createBalls(nbBalls);

        loadAssets(function () {
            // all assets (images, sounds) loaded, we can start the animation
            requestAnimationFrame(mainLoop);
        });
    };

    //our GameFramework returns a public API visible from outside its scope
    return {
        start: start
    };
};


