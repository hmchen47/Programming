// 
// made by Sound Spinning: https://soundspinning.tumblr.com/
// 
// Collisions 'ball : ball' based on physics concepts
// Effects of heat losses at impact taken into account
// Random size & initial velocities generation
// 

// 
// GLOBAL variables
// ======

// canvas vars
// 
var canvas, canvasCtx, canvasW, canvasH, 
		canvasArea, fillArea, canvasRatio, canvaScale;
// measureFPS function (frames/s) vars
var frameCount = 0, lastTime, fpsContainer, fps;
// time based animation
var delta, oldTime = 0, nowTime = performance.now();
// array of balls to animate & their parameters
var ballArray = [], nBalls, diameter, maxVel, maxBallArea;
var nHits = 0, ballsContainer, addInfo;
var radScale, velScale, ballMode, pushMode;
// others
var eCoeff;
var allForms, allRadio, sliders;
var buttons, pauseBut, playBut;
var isRunning = true;




// INITIATE app after page load
// ========
window.onload = function init() {
	// new instance of mainApp
	var mainApp = new AF();
  addInfo = document.querySelector("#addInfo");

  // set up CANVAS
  canvas = document.querySelector("#myCanvas");
  canvasCtx = canvas.getContext('2d');
  // set width & height
  canvaScale = 1;
  // canvas.width = document.body.clientWidth;
  canvas.width = canvas.clientWidth;
  canvasW = canvas.width;
  canvasRatio = 16/9;  // 16:9 ratio
  canvas.height = canvasW/canvasRatio;
  canvasH = canvas.height;
  
  // canvasArea used to estimate number of balls further down
  canvasArea = canvasW * canvasH;

  // set default canvas font size, family
  canvasCtx.font = "16px Dosis";

  // balls' parameters
  // 
  velScale = 1.0;
  radScale = 1.0;
  diameter = 0.09*canvasW;
  maxBallArea = Math.PI*Math.pow(diameter/2,2);  // max possible ball area
  fillArea = 0.8;  // fraction of potential canvas area to fill with balls
  nBalls = Math.floor(fillArea*canvasArea / maxBallArea);
  maxVel = 20;  // max velocity (px/s) allowed in initial random balls

  // 'coefficient of restitution' to account for energy losses/gains at impact.
  // between 0 (no bounce, balls stay together) & 1 (elastic bounce)
  eCoeff = 1.0;

  // set default collision mode
  ballMode = "Push 1";

  // Launch the app
  mainApp.start();
};


// APP FRAMEWORK STARTS HERE
// =============
var AF = function(){
	// START: add elements, event listeners & kick things off
	// 
	var start = function(){
    // adds an element displaying the fps (frames/s) value
    fpsContainer = document.createElement('span');
    addInfo.appendChild(fpsContainer);
    // adds an element with Balls info
    ballsContainer = document.createElement('span');
    addInfo.appendChild(ballsContainer);

    // deal with buttons
    buttons = document.querySelectorAll('button');
    pauseBut = document.querySelector('.fa-pause');
    playBut = document.querySelector('.fa-play');
    // restart
    buttons[0].onclick = function(e) { 
      location.reload();
    };
    // pause / play
    buttons[1].onclick = function(e) {
      requestAnimationFrame(mainLoop);
      pauseBut.classList.toggle('no-show');
      playBut.classList.toggle('no-show');
      // toggle the value of isRunning
      isRunning = !isRunning;
    };

    // deal with all controls
    controlsAll();

    // We generate the balls
    addBalls(nBalls);
    
    // start the animation
    requestAnimationFrame(mainLoop);
  };


  // Main animation function, called each frame
  // 
  var mainLoop = function(time){
    if (isRunning) {
      // frames/s
      measureFPS(time);
      // number of ms since last animation frame
      delta = timer(time);
      // clear canvas
      clearCanvas();
      // update and draw balls
      updateBalls(ballMode);
  
      // call the animation loop every 1/60th of a second if not paused
      requestAnimationFrame(mainLoop);
    };
  };


  // 
  // call all main Ball functions to update balls
  // 
  // function updateBalls(delta) {
  //   // test each ball : ball : walls, then move & draw
  //   // 
  //   // 1) ball scaling wrt canvas vertical location
  //   // 2) test if each ball collides with a wall
  //   // 3) move the ball --> draw the ball
  //   // 4) test for collisions between balls for different modes
  //   bounceTestBalls(ballMode);
  // }


	// generate balls
	// 
  function addBalls(numberOfBalls) {
    for(var i=0; i < numberOfBalls; i++) {
      // Create balls with random parameters
      var angle = 2*Math.PI*Math.random();  // random angle in radians
      var ball =  new Ball(
				canvasW*Math.random(),      	// x
        canvasH*Math.random(),      	// y
        maxVel*Math.cos(angle),				// velocity X (px/s)
        maxVel*Math.sin(angle),     	// velocity Y (px/s)
        4+diameter*Math.random());  	// diameter >= 4
    // Add it to the array
    ballArray[i] = ball;
    }
  }

  // constructor function for balls
  // 
  function Ball(x, y, vx, vy, diameter) {
    this.x = x;
    this.y = y;
    this.vx = vx;
    this.vy = vy;
    this.radius = diameter/2;  // random radius >= 2px
    this.color = "black";
    this.initRad = diameter/2;
    // the area below is used as mass in impact calcs
    this.area = Math.PI * Math.pow(this.radius,2);
    
    this.draw = function() {
      canvasCtx.save();
      canvasCtx.beginPath();
      canvasCtx.fillStyle = this.color;
      canvasCtx.arc(this.x, this.y, this.radius, 0, 2*Math.PI);
      canvasCtx.fill();
      canvasCtx.restore();
    };
    
    this.move = function() {
      // add horizontal/vertical displacement to the ball centre
      this.x += calcDisplacement(delta, this.vx*velScale);
      this.y += calcDisplacement(delta, this.vy*velScale);
    };
  }

  // 
  // test collisions ball : ball : walls, then move & draw
  // 
  // 1) ball scaling wrt canvas vertical location
  // 2) test if each ball collides with a wall
  // 3) move the ball --> draw the ball
  // 4) test for collisions between balls for the different 4 modes
  function updateBalls(ballMode) {
    var jBalls = ballArray, iBalls = ballArray;
    for (var i = 0; i < iBalls.length; i++) {
      iBall = iBalls[i];
      // ball scaling wrt canvas vertical location
      scaleBalls(iBall);
      // test if each ball collides with a wall
      collisionTestWithWalls(iBall);
      // move the ball
      iBall.move();
      // draw the ball
      iBall.draw();

      for (var j = 0; j < jBalls.length; j++) {
        jBall = jBalls[j];
        if (j === i) { continue; };
        var dx = jBall.x - iBall.x;
        var dy = jBall.y - iBall.y;
        var target = jBall.radius + iBall.radius;

        // this tries to discard from the loop balls far enough from each other
        if (target > diameter*scaleBalls) { continue; };
        
        var nAxis = [dx, dy];  // normal axis array between ball centres
        var dist = magVect(nAxis);  // calculate vector magnitude
        // when contact occurs do something...
        // All interaction modes are here
        // if (dist <= target) {
        if (!(dist > target)) {
          // balls contact so push back...
          var nX = dx / dist;  // normal COS vector
          var nY = dy / dist;  // normal SIN vector
          // find coordinates for the contact point between balls i & j
          // this is used later on to plot gradients
          var contactX = iBall.x + iBall.radius*nX;
          var contactY = iBall.y + iBall.radius*nY;
          
          // switch 'interaction' mode between the balls
          switch (ballMode) {
            case "Push 1":
            // push 1
            //
              // relocate balls to push around each other
              iBall.x = contactX - (nX * iBall.radius);
              iBall.y = contactY - (nY * iBall.radius);
              jBall.x = contactX + (nX * jBall.radius);
              jBall.y = contactY + (nY * jBall.radius);

              canvasCtx.globalAlpha = 1;
              // reset hit counter when overlaps occur
              if (dist < target-1) {
                nHits --;
              }
              // hit counter
              nHits++;
              ballsContainer.innerHTML = '| Balls: ' + nBalls + 
                ' | Aprox Hits: ' + formatNumber(Math.floor(nHits/fps));
              break;

            case "Push 2":
            // push 2
            // 
              // relocate balls to push around each other
              iBall.x = contactX - (nX * iBall.radius);
              iBall.y = contactY - (nY * iBall.radius);
              jBall.x = contactX + (nX * jBall.radius);
              jBall.y = contactY + (nY * jBall.radius);
              // update balls more often than case "Push 1"
              iBall.move(); jBall.move();

              canvasCtx.globalAlpha = 1;

              // reset hit counter when overlaps occur
              if (dist < target-1) {
                nHits --;
              }
              // hit counter
              nHits++;
              ballsContainer.innerHTML = '| Balls: ' + nBalls + 
                ' | Aprox Hits: ' + formatNumber(Math.floor(nHits/fps));
              break;

            case "Through":
            // passive, see thru, only gradients change
            // 
              // unit 'normal' axis vector
              var nAxisUnit = [nX, nY];
              // rotate normal contact axis 90deg
              var tAxis = [-nAxis[1], nAxis[0]];  // 'tangential' axis
              // unit 'tangential' axis vector
              var tAxisUnit = [-nY, nX];
              // use vectorial dot product to calculate ball velocities
              // in the 'normal' & 'tangential' directions to the contact point
              var iBallVel = [iBall.vx, iBall.vy];  // velocity vector for i
              var jBallVel = [jBall.vx, jBall.vy];  // velocity vector for j
              // vectorial dot products to find components 
              // in 'normal' & 'tangential' directions
              var niBallDot = dotProduct(iBallVel, nAxis);
              var tiBallDot = dotProduct(iBallVel, tAxis);
              var njBallDot = dotProduct(jBallVel, nAxis);
              var tjBallDot = dotProduct(jBallVel, tAxis);
              iBall.vx = (nAxisUnit[0]*niBallDot + tAxisUnit[0]*tiBallDot)/dist;
              iBall.vy = (nAxisUnit[1]*niBallDot + tAxisUnit[1]*tiBallDot)/dist;
              jBall.vx = (nAxisUnit[0]*njBallDot + tAxisUnit[0]*tjBallDot)/dist;
              jBall.vy = (nAxisUnit[1]*njBallDot + tAxisUnit[1]*tjBallDot)/dist;

              // reset hit counter when overlaps occur
              if (dist < target-1) {
                canvasCtx.globalAlpha = 0.8;
                nHits --;
              }
              // hit counter
              nHits++;
              ballsContainer.innerHTML = '| Balls: ' + nBalls + 
                ' | Aprox Crossings: ' + formatNumber(Math.floor(nHits/fps));
              break;

            case "Impact":
            // impacts based on physics laws
            // 
              // the check below is to undo ball overlaps at the switch to 'Impact'
              if (dist < target) { 
                // relocate balls to push around each other
                iBall.x = contactX - (nX * iBall.radius);
                iBall.y = contactY - (nY * iBall.radius);
                jBall.x = contactX + (nX * jBall.radius);
                jBall.y = contactY + (nY * jBall.radius);
              };
              // reset hit counter when overlaps occur
              if (dist < target-1) {
                nHits --;
              }

              // unit 'normal' axis vector
              var nAxisUnit = [nX, nY];
              // rotate 'normal' contact axis 90deg to get the 'tangential' axis
              var tAxis = [-nAxis[1], nAxis[0]];
              // unit 'tangential' axis vector
              var tAxisUnit = [-nY, nX];
              // use vectorial dot product to calculate ball velocities
              // in the 'normal' & 'tangential' directions wrt the contact point
              var iBallVel = [iBall.vx, iBall.vy];  // velocity vector for i
              var jBallVel = [jBall.vx, jBall.vy];  // velocity vector for j
              // vectorial dot products to find components 
              // in 'normal' & 'tangential' directions
              var niBallDot = dotProduct(iBallVel, nAxis);
              var tiBallDot = dotProduct(iBallVel, tAxis);
              var njBallDot = dotProduct(jBallVel, nAxis);
              var tjBallDot = dotProduct(jBallVel, tAxis);
              // 
              // The calculation of velocities after impact for different masses
              // was done by applying conservation of momentum & kinetic energy
              // in the 'normal' axis direction. 
              // The velocities in the 'tangential' direction do NOT change 
              // before:after the impact.
              // NOTE that the calculation of velocities after the impact 
              // for balls with different masses (radius) is not trivial.
              // Final velocities formulae in the 'normal' direction after impact 
              // can be found here: 
              // http://hyperphysics.phy-astr.gsu.edu/hbase/elacol2.html#c3
              // 
              // Below is the combination of 'normal' & 'tangential' components 
              // transformed back to the global (canvas) system, 
              // and including energy loss/gain.
              // [good luck to me getting these right ...]

              // initial vels projected onto the 'normal' axis (dot products)
              var iBallnVx = nAxisUnit[0]*niBallDot;
              var iBallnVy = nAxisUnit[1]*niBallDot;
              var jBallnVx = nAxisUnit[0]*njBallDot;
              var jBallnVy = nAxisUnit[1]*njBallDot;
              // ball masses (based on area)
              var iM = iBall.area, jM = jBall.area;

              // Calculate 'normal' velocities after the impact:
              // [...deep breath here, it gets a bit heavy when accounting 
              // for different masses and energy losses]
              var iBallnVxAfter = (iBallnVx*(iM-eCoeff*jM))/(iM+jM) + (jBallnVx*(1+eCoeff)*jM)/(iM+jM);
              var iBallnVyAfter = (iBallnVy*(iM-eCoeff*jM))/(iM+jM) + (jBallnVy*(1+eCoeff)*jM)/(iM+jM);
              var jBallnVxAfter = (jBallnVx*(jM-eCoeff*iM))/(iM+jM) + (iBallnVx*(1+eCoeff)*iM)/(iM+jM);
              var jBallnVyAfter = (jBallnVy*(jM-eCoeff*iM))/(iM+jM) + (iBallnVy*(1+eCoeff)*iM)/(iM+jM);
              // add components 'normal' & 'tangential' in the global system
              iBall.vx = (iBallnVxAfter + tAxisUnit[0]*tiBallDot)/dist;
              iBall.vy = (iBallnVyAfter + tAxisUnit[1]*tiBallDot)/dist;
              jBall.vx = (jBallnVxAfter + tAxisUnit[0]*tjBallDot)/dist;
              jBall.vy = (jBallnVyAfter + tAxisUnit[1]*tjBallDot)/dist;

              // update balls
              canvasCtx.globalAlpha = 1;
              iBall.move(); jBall.move();
              iBall.draw(); jBall.draw();

              // hit counter
              nHits++;
              ballsContainer.innerHTML = '| Balls: ' + nBalls + 
                ' | Aprox Hits: ' + formatNumber(Math.floor(nHits));
              break;
          };

          // ball gradients when hit
          // 
          var iHitGrad = canvasCtx.createRadialGradient(
          contactX, contactY, iBall.radius/5,
          contactX, contactY, iBall.radius);
          iHitGrad.addColorStop(0, "peru");
          iHitGrad.addColorStop(0.5, "crimson");
          iHitGrad.addColorStop(1, "black");

          var jHitGrad = canvasCtx.createRadialGradient(
          contactX, contactY, jBall.radius/5,
          contactX, contactY, jBall.radius);
          jHitGrad.addColorStop(0, "dimgray");
          jHitGrad.addColorStop(0.1, "orange");
          jHitGrad.addColorStop(1, "black");

          iBall.color = iHitGrad;
          jBall.color = jHitGrad;
        }
      }
    }
  }


  // collision detection balls : walls
  // 
  function collisionTestWithWalls(ball) {
    // left
    if (ball.x < ball.radius) {
      	ball.x = ball.radius;
      	ball.vx *= -1;
    }
    // up
    if (ball.y < ball.radius) {
        ball.y = ball.radius;
        ball.vy *= -1;
    }
    // right
    if (ball.x > canvasW - ball.radius) {
      	ball.x = canvasW - ball.radius;
      	ball.vx *= -1; 
    }     
    // down
    if (ball.y > canvasH - ball.radius) {
      	ball.y = canvasH - ball.radius;
      	ball.vy *= -1;
    } 
  }


  // 
  // GENERAL functions
  // =================

  // get vector [array] magnitude value
  function magVect(vector) {
    var result = 0;
    for (var i = 0; i < vector.length; i++) {
      result += Math.pow(vector[i],2);
    }
    return Math.sqrt(result);
  }

  // get vectorial [arrays] dot product
  function dotProduct(vector1, vector2) {
    if (vector1.length != vector2.length) {
      console.log("Error: vectors are of different size");
    } else {
      var result = 0;
      for (var i = 0; i < vector1.length; i++) {
        result += vector1[i] * vector2[i];
      }
    }
    return result;
  }

  // scale balls radii wrt canvas height to give a sense of perspective
  function scaleBalls(ball) {
    ball.radius = radScale * ball.initRad *
    	(ball.y / (canvasH-(radScale * ball.initRad)));
    if (ball.radius < 2) { ball.radius = 2; };
  }


	// Canvas time based animation: speed in pixels/s (rendered at 60 frames/s)
  // The delay between frames should be 1/60=16.66ms, 
  // The displacement (px) applied = [speed(px/s) * delay(ms)/1000(ms/s)]
  var calcDisplacement = function(delta, speed) {
    return (speed * delta * 1e-3);
  };

  // calculate frames/s; i.e. rendering speed
  // 
  var measureFPS = function(newTime){
    // test for the very first call
    if (lastTime === undefined) {
      lastTime = newTime; 
      return;
    }
    // calculate the difference (ms) between last & current frames
    var diffTime = newTime - lastTime;
    if (diffTime >= 1000) {
      fps = frameCount;
      frameCount = 0;
      lastTime = newTime;
    }
    // display it in a HTML element created in the start() function
    fpsContainer.innerHTML = 'FPS: ' + fps + ' '; 
    frameCount++;
  };

  // calculate delta time between frames
  function timer(nowTime) {
    var delta = nowTime - oldTime;
    oldTime = nowTime;
    return delta;
  }

  // clear the canvas
  function clearCanvas() {
    canvasCtx.clearRect(0, 0, canvasW, canvasH);
  }

  // function to format numbers as ',' (1000's) & '.' (decimal)
  function formatNumber(num) {
  return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
	}


  // deal with slider changes
  // 
  function controlsAll() { 
    // general sliders
    // 
    allForms = document.querySelectorAll('.controls form');
    allRadio = document.querySelectorAll('input[type="radio"]');
    // this gets round a problem in Edge not remembering the default
    allRadio[0].checked = true;
    sliders = document.querySelectorAll('input[type="range"]');
    sliders[0].disabled = true;
    // add an ID per form
    for (var i = 0; i < allForms.length; i++) {
      allForms[i].id = "form" + i;
      if (i>0) {
        // the lines below is to reset sliders in Edge, as 'autofill=no' doesn't work.
        allForms[i].reset();
        allForms[i].querySelector('output').value = allForms[i].querySelector('input').defaultValue;
      };
    };
    
    allRadio.forEach((item) => {
      item.onclick = function(e) {
        nHits =0;
        for (var i = 0; i < allRadio.length; i++) {
          if (item.checked) {
            ballMode = item.value;
            if ( !(ballMode === "Impact") ) {
              sliders[0].disabled = true;
              allForms[1].style.opacity = "0.35";
            } else { 
                sliders[0].disabled = false;
                allForms[1].style.opacity = "1.0";
              }
          }
        }
      }
    });
    
    //  add event listeners to all sliders & update slider values when changed
    sliders.forEach((item) => {
      item.oninput = function(e) {
        var tmpId = this.parentNode.id;
        // get Index of slider
        var tmpIndex = Array.prototype.indexOf.call(sliders,this);
        // update slider value
        var tmpSlider = document.querySelector('#'+tmpId+' > input');
        tmpSlider.value = parseFloat(this.value);
        // update output labels
        var tmpOut = document.querySelector('#'+tmpId+' > output');
        tmpOut.innerHTML = tmpSlider.value;
        var tmpType = this.parentNode.dataset.type;
        // 
        // update slider values
        if (tmpType === "Loss") {
          eCoeff = 1 - tmpSlider.value/100;
        }
        if (tmpType === "Size") {
          radScale = tmpSlider.value;
        }
        if (tmpType === "Velocities") {
          velScale = tmpSlider.value;
        }
        if (tmpType === "canvasWidth") {
          canvaScale = tmpSlider.value;
          var docW = document.body.clientWidth;
          clearCanvas();
          canvas.style.width = canvaScale + "%";
        }
      };
    });
  }


  // AppFramework returns a public API visible from outside its scope
  // Here we only expose the start method, under the "start" property name.
  return {
    start: start
    // mainLoop: mainLoop
  };

};
// APP FRAMEWORK ENDS
// =============

