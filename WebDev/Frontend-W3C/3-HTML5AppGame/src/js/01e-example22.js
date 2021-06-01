	var canvas;
	var context2D;
	var mousePos;

	var particles = [];
	
	function randomFloat (min, max)
	{
		return min + Math.random()*(max-min);
	}

function removeFromArray(array, object) {
    var idx = array.indexOf(object);
    if (idx !== -1) {
        array.splice(idx, 1);
    }
    return array;
}
	
	/*
	 * A single explosion particle
	 */
	function Particle ()
	{
		this.scale = 1.0;
		this.x = 0;
		this.y = 0;
		this.radius = 20;
		this.color = "#000";
		this.velocityX = 0;
		this.velocityY = 0;
		this.scaleSpeed = 0.5;
		this.useGravity = false;
      
		this.update = function(ms)
		{
			// shrinking
          
			this.scale -= this.scaleSpeed * ms / 1000.0;
          
			if (this.scale <= 0)
			{
              // particle is dead, remove it
              removeFromArray(particles, this);
              
			}
			
			// moving away from explosion center
			this.x += this.velocityX * ms/1000.0;
			this.y += this.velocityY * ms/1000.0;
          
          // and then later come downwards when our
		  // gravity is added to it. We should add parameters 
          // for the values that fake the gravity
          if(this.useGravity) {
              this.velocityY += Math.random()*4 +4;
          }
		};
		
		this.draw = function(context2D)
		{
			// translating the 2D context to the particle coordinates
			context2D.save();
			context2D.translate(this.x, this.y);
			context2D.scale(this.scale, this.scale);
			
			// drawing a filled circle in the particle's local space
			context2D.beginPath();
			context2D.arc(0, 0, this.radius, 0, Math.PI*2, true);
			//context2D.closePath();
			
			context2D.fillStyle = this.color;
			context2D.fill();
			
			context2D.restore();
		};
	}
	
	/*
	 * Basic Explosion, all particles move and shrink at the same speed.
	 * 
	 * Parameter : explosion center
	 */
	function createBasicExplosion(x, y)
	{
		// creating 4 particles that scatter at 0, 90, 180 and 270 degrees
		for (var angle=0; angle<360; angle+=90)
		{
			var particle = new Particle();
			
			// particle will start at explosion center
			particle.x = x;
			particle.y = y;
			
			particle.color = "#FF0000";
			
			var speed = 50.0;
			
			// velocity is rotated by "angle"
			particle.velocityX = speed * Math.cos(angle * Math.PI / 180.0);
			particle.velocityY = speed * Math.sin(angle * Math.PI / 180.0);
			
			// adding the newly created particle to the "particles" array
			particles.push(particle);
		}
	}
	
	/*
	 * Advanced Explosion effect
	 * Each particle has a different size, move speed and scale speed.
	 * 
	 * Parameters:
	 * 	x, y - explosion center
	 * 	color - particles' color
	 */
	function createExplosion(x, y, color)
	{
		var minSize = 10;
		var maxSize = 30;
		var count = 10;
		var minSpeed = 60.0;
		var maxSpeed = 200.0;
		var minScaleSpeed = 1.0;
		var maxScaleSpeed = 4.0;
		
		for (var angle=0; angle<360; angle += Math.round(360/count))
		{
			var particle = new Particle();
			
			particle.x = x;
			particle.y = y;
			
            // size of particle
			particle.radius = randomFloat(1, 3);
			
			particle.color = color;
			
            // life time, the higher the value the faster particle 
            // will die
			particle.scaleSpeed = randomFloat(0.3, 0.5);
          
            // use gravity
          particle.useGravity = true;
			
			var speed = randomFloat(minSpeed, maxSpeed);
			
			particle.velocityX = speed * Math.cos(angle * Math.PI / 180.0);
			particle.velocityY = speed * Math.sin(angle * Math.PI / 180.0);
			
			particles.push(particle);
		}
    
	}

// Delta = time between two consecutive frames,
// for time-based animation
function updateAndDrawParticules(delta) {
   for (var i = 0; i < particles.length; i++) {
	  var particle = particles[i];
			
	  particle.update(delta);
	  particle.draw(context2D);
   }
}

//------------- ANIMATION PART -------------------------
var delta, oldTime=0;

  function timer(currentTime) {
    var delta = currentTime - oldTime;
    oldTime = currentTime;
    return delta;
 
  }

	function animationLoop (time)
	{
       // number of ms since last frame draw
        delta = timer(time);
       
		// Clear canvas
		context2D.clearRect(0, 0, canvas.width, canvas.height);
		
      // Move and draw particles
      updateAndDrawParticules(delta);
      
      
      // call again the animation loop at 60f/s, i.e in about 16,6ms
      requestAnimationFrame(animationLoop);
	}
	
	
	window.addEventListener("load", function()
	{
		// canvas and 2D context initialization
		canvas = document.getElementById("canvas");
		context2D = canvas.getContext("2d");
		
		// Button click : BOOM !
		var button1 = document.getElementById("explosion");
       button1.addEventListener("click", function() {
			       var x = randomFloat(100, 400);
			       var y = randomFloat(100, 400);
			startDoubleExplosion(x, y);
		});
		
		// Button click : basic effect
		var button2 = document.getElementById("basic_explosion");
      
                button2.addEventListener("click", function() {
			      createBasicExplosion(250, 200);
           sound.play('laser');
		});
      
        canvas.addEventListener("mousedown" , function(evt) {
          mousePos = getMousePos(canvas, evt);
          startDoubleExplosion(mousePos.x, mousePos.y);
        }, false);
      		
		// starting the game loop at 60 frames per second
	    requestAnimationFrame(animationLoop);					
	});
function getMousePos(canvas, evt) {
   // necessary to take into account CSS boudaries
   var rect = canvas.getBoundingClientRect();
   return {
      x: evt.clientX - rect.left,
      y: evt.clientY - rect.top
   };
}
function startDoubleExplosion(x, y) {
  		        createExplosion(x, y, "#525252");
			    // On peut multiplier la densité en générant plusieurs 
                // explositons de couleurs différentes...
			    createExplosion(x, y, "#FFA318");
                //createExplosion(x, y, "green");
          sound.play('blast');

}
// SOUND WITH HOWLER JS
var sound = new Howl({
  urls: ['http://goldfirestudios.com/proj/howlerjs/sounds.mp3', 'http://goldfirestudios.com/proj/howlerjs/sounds.ogg'],
  sprite: {
    blast: [0, 2000],
    laser: [3000, 700],
    winner: [5000, 9000]
  }, 
  onload: function() { console.log("Sound loaded");}
});


