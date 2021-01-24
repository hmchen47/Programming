function init() {
  console.log("Page loaded and DOM is ready");
  
  // Get the canvas graphics context
  context = document.getElementById('canvas').getContext('2d');
  // These variables are used for switching animations, just for illustration
  var animNo = 1, animNames = [
    'ButtWalk', 'BodyWalk', 'BodyAltWalk', 'Walk'
  ];
  // Initialize the SpriteMap
  spriteMap = new SpriteMap(
    'https://icecreamyou.github.io/Canvas-Sprite-Animations/centipede-sprite.png', // sprite image
    { // animation sequences
      ButtWalk: {startRow: 0, startCol: 0, endRow: 1, endCol: 3},
      BodyWalk: {startRow: 1, startCol: 5, endRow: 2, endCol: 8},
      BodyAltWalk: {startRow: 3, startCol: 1, endRow: 4, endCol: 4},
      Walk: {startRow: 4, startCol: 6, endRow: 6, endCol: 0},
    },
    { // options
      frameW: 52, // Width of each frame of the animation in pixels
      frameH: 60, // Height of each frame of the animation in pixels
      projectedW: 104, // Displayed width (in this case 200% size)
      projectedH: 120, // Displayed height (in this case 200% size)
      interval: 50, // Switch frames every 50ms
      useTimer: false, // Rely on requestAnimFrame to update frames instead of setInterval
      postInitCallback: function (sprite) {
        spriteMap.start('ButtWalk'); // Start running the animation
        animate(); // Animate the canvas
        setInterval(function() { // Switch animation sequence every 2.5 seconds for illustration
          animNo = (animNo + 1) % animNames.length;
          console.log(animNames[animNo])
          spriteMap.use(animNames[animNo]); // Switch animation sequences
        }, 2500);
      } // Do something when the sprite finishes loading
    }
  );
}

function animate() { // Animation loop that draws the canvas
  context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clear the canvas
  spriteMap.draw(context, 100, 100); // Draw the sprite
  requestAnimationFrame(animate); // Run the animation loop
}

