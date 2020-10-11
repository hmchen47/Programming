var canvas;
var context;

// Size of the histogram
var width = 150, height=150;
// The origin, bottom left corner, relative to the origin in the canvas
var x = 40, y = 190; 

// Data to be visualized
var values = [1, 10, 2, 7, 9, 2, 34, 100, 12, 14, 19];

//init function is launch when the page is loaded.
function init() {
    canvas = document.getElementById('canvas'); 
    context = canvas.getContext('2d'); 
  
    var list =  document.getElementById('sliders'); 
  
    // Create the sliders for changing the values.
    var max = getMax(values);
  
    for (i=0; i < values.length; i++) {
      var input = document.createElement('input');
      var li = document.createElement('li');
      var label = document.createElement('label');
      label.setAttribute('for', 'id'+i);
      label.textContent = 'value' + i + ' ';
      
      li.appendChild(label); 
      
      input.setAttribute('type', 'range');
      input.setAttribute('id', 'id' + i);
      // Set their value and max attributes correctly
      input.setAttribute('max', max);
      input.value = values[i]; 
      // Add an onchange event listener and pass the
      // index of the slider to the callback
      input.setAttribute('oninput', 'changeValue(' + i + ')');
      li.appendChild(input);
      
      list.appendChild(li);
    }
 
    makeHistogram(x, y, 
                  width, height, 
                  values);  
  // center of pie x and y, radius, values
  makePieChart(300, 100, 90, values); 
  
  // Draw broken lines chart
  makeBrokenLines(40, 370, width, height, values);
}

// callback for sliders' onchange events. 
function changeValue(index) {
    var value = document.getElementById("id"+index).value; 
  
    // put the slider value in the values array
    values[parseInt(index)] = parseInt(value); 
  
    // clear the canvas
    context.clearRect(0,0, canvas.width, canvas.height); 
    
    // redraw the charts
    makeHistogram(x, y, width, height, values);  
    makePieChart(300, 100, 90, values); 
    makeBrokenLines(40, 370, width, height, values);
}           
// returns the max from the elements of the values array.
function getMax(values) {
    var maxValue = 0;
  
    for (i=0; i<values.length; i++) {
        if (maxValue < values[i])
            maxValue = values[i];
    }
  return maxValue;
}




function drawAxis(width, height,  values, maxValue) {
	// remember: we have the origin of the coordinate system at bottom left
	// Y values above will be negative
	  
    context.strokeStyle = "black"; //We draw in black the outline.
    context.fillStyle = "black"; //We fill in black.
  
    //We define the vertical step unit. Is it 10 ? 20 ? 100 ? 1000 ? Depending on the
    // max unit value, we decide how the steps will be for the ticks
    var unit = 1; 
    while (maxValue / (unit*10) > 1) {
        unit *= 10; 
    }
  
   //We define the highest vertical step.
    var yMaxOnAxis = parseInt(maxValue) / unit;   
  
    // Everything is in a path, all drawing orders will be drawn by a final call
    // to context.stroke() at the end of the function.
    context.beginPath(); //Begin a new path.
  
    // Draw the axis' lines
    context.moveTo(0, 0); //We place the cursor to origin.
    context.lineTo(0, -height); //We draw the vertical line.
    context.moveTo(0, 0); //We place the cursor to origin.
    context.lineTo(width, 0); //We draw the horizontal line.


    // ticks/labels on the vertical line
    context.textAlign = "left";

    for (i=0; i <= yMaxOnAxis; i++) {
        // move to the next graduation. the y value is negative due to
        // the change of the origin by a call to translate(x,y) in the drawHistogram
        // function.
        context.moveTo(0, -height / yMaxOnAxis * i );
      
        // draw an horizontal line, 5 pixels long, on the left of the axis
        context.lineTo(-5, -height / yMaxOnAxis * i ); 
      
        // write the tick value, 25 pixels on the left of the axis
        context.fillText(i*unit, -25, -height / yMaxOnAxis * i ); 
    }

    // Ticks/labels on the horizontal line
    var counter = 0; 
    // text centered below the tick
    context.textAlign = "center"; 

  
    // graduation on the horizontal line.
    var rectanglesWidth = width / values.length;
    
    for (i=0; i <= values.length; i++) {
    	  // Move to the next horizontal position of the tick
        context.moveTo(i*rectanglesWidth , 0); 
        // draw a vertical line 5 pixels long: the tick
        context.lineTo(i*rectanglesWidth , 5); 
        // write tick label  15 pixels below the tick
        context.fillText(i, i*rectanglesWidth , 15); 
        counter++;
    }
    // Draw everything in the path
    context.stroke(); 
    
}

// MakeHistogram building a bar plot. x, y is the bottom left position of the
// histogram. Easier to reason with this coordonate system
function makeHistogram(x, y, width, height, values) {
    context.save();
    // Change the origin at bottom left. If we draw "above", Y values will be negative.
    // y=0 is the horizontal line at bottom
    context.translate(x, y);
    
    // Compute the max of the values array
    var maxValue = getMax(values);
  
    // step in pixels between two horizontal values for bar plot.
    var rectWidth = width / parseFloat(values.length); 

    // step in pixels between two vertical values for bar plot.
    var vStep = -height / parseFloat(maxValue); 
   
    //Set fill color to red and stroke color to black.
    context.fillStyle = "red"; 
    context.strokeStyle = "black";
 
    // Draw the histogram rectangles
    for(i=0; i < values.length; i++) {       
        //We draw a filled red rectangle to represent the current value.
        context.fillRect(i * rectWidth, 0, 
                         rectWidth, vStep * values[i]); 
      
       //We draw the outline of rectangle.
        context.strokeRect(i * rectWidth, 0, 
                           rectWidth, vStep * values[i]); 
    }
  
  // draw the axis
  drawAxis(width, height, values, maxValue); 
  
  context.restore();
}

//makePieChart draw a circle graph with values table.
function makePieChart(cx, cy, radius, values) {
  context.save();
  
    // Compute the sum of all values
    var sum=0;
    for(var n=0; n < values.length; n++) {
      sum += values[n];
    }
  
    //Initialization of red green blue colors.
    var red = 0;
    var green = 0;
    var blue = 0;

  //starting and ending angles of each pie section
    var startingAngle = 0; 
    var endAngle = 0; 
   //The percentage the current value represents, compare to the total,
  // we are in a closed circle, the sum is 100%
    var percentage;

  //We draw in grey the outline of the section.
  context.strokeStyle = "grey"; 
  
  // Draw the pie chart, clockwise, à la HTML5
  //for (var i=values.length-1; i> 0; i--) { // for ccw display 
  for(var i = 0; i < values.length; i++) {
        context.beginPath(); //Begin a new path.

        // We change the colors depending on the i-value. Just a trick based
        // on the modulo. Will produce different colors for the pie sections
        switch (i%3) {
            case 0: //If i modulo 3 equals 0:
                red += 80; //We add red.
                break;
            case 1: //If i modulo 3 equals 1:
                green += 80; //We add green.
                break;
            case 2: //If i modulo 3 equals 2:
                blue += 80; //We add blue.
                break;
            default: //If there is an error.
                alert("we have encountered an error");
                return ; //and we stop makePieChart.
        }
        context.fillStyle = "rgb(" + red + "," + green + "," + blue +")"; 
    
        // percentage of the circle for current section, will give the angles
        percentage = values[i] / parseFloat(sum); 
        endAngle = startingAngle + Math.PI*2*percentage; 

        // draw an arc between starting angle and end angle.
        context.arc(cx, cy, radius, startingAngle, endAngle); 
       // draw a line between end angle and center of circle.
        context.lineTo(cx, cy); 
    
        //The next starting angle is the current end angle.
        startingAngle = endAngle; 

        context.fill();      // draw pie section
        context.stroke();    // draw the outline.
        context.closePath(); // Close the path.
      
        context.restore();
    }
}
  
// draw a broken line chart
function makeBrokenLines(x, y, width, height, values) {
    context.save();
    // Move origin of the coordinate system at x, y, bottom left corner
    context.translate(x, y);
  
    var maxValue = getMax(values);
  
    // distance between two horizontal values, in pixels
    var hStep = width / parseFloat(values.length); 
  
    // step between two vertical values, in pixels
    var vStep = -height / parseFloat(maxValue); 

    // set fill color to black, for drawing the circle plots
    context.fillStyle = "black"; 
    // thickness of the lines
    context. lineWidth = 1; 
  
    // set the cursor to origin.
    context.moveTo(0 , 0); 

    // All lines are drawn into a path
    context.beginPath();
    for(i=0; i<values.length; i++) { 
        context.lineTo(i * hStep, vStep * values[i]);        
    }
    context.stroke(); // draw the path with all the lines

    // Draw the filled black circles at each value's coordinate
    for(i=0; i<values.length; i++) { 
        context.beginPath(); 
        context.arc(i * hStep, vStep * values[i], 3, 0, 2*Math.PI); 
        context.fill(); //We fill all circles.
    }
  // draw the X and Y axis
  drawAxis(width, height, values, maxValue); 
  
  context.restore();
}


