
var canvas, ctx, pattern1;

function init() {
  canvas = document.querySelector('#myCanvas');
  ctx = canvas.getContext('2d');
  
  // We need 1) to create an empty image object, 2) to set a callback function
  // that will be called when the image is fully loaded, 3) to create a 
  // pattern object, 4) to set the fillStyle or the strokeStyle property of 
  // the context with this pattern, 5) to draw something
  // WE CANNOT DRAW UNTIL THE IMAGE IS FULLY LOADED -> draw from inside the
  // onload callback only !
  
  
  // Allocate an image
  var imageObj = new Image();

  // callback called asynchronously, after the src attribute of imageObj is set
  imageObj.onload = function(){
	// We enter here only when the image has been loaded by the browser
	// Pattern creation using the image object
    // Instead of "repeat", try different values : repeat-x, repeat-y, 
    // or no-repeat, You may draw larger shapes in order to see 
    // different results
    // It is a good practice to leave this as a global variable if it
    // will be reused by other functions
    pattern1 = ctx.createPattern(imageObj, "repeat");
	
    // Draw a textured rectangle
	ctx.fillStyle = pattern1;
	ctx.fillRect(10, 10, 500, 800);
    
    // And a wireframe one
    ctx.lineWidth=50;
    ctx.strokeStyle=pattern1;
    ctx.strokeRect(650, 20, 300, 800);
};
  
  // This will tell the browser to send an asynchronous request.
  // When the browser will get an answer, the callback above will be called
  imageObj.src = "http://www.dreamstime.com/colourful-flowers-repeatable-pattern-thumb18692760.jpg"; 
}


      
