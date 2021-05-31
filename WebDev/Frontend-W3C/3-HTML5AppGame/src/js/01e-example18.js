//buil an equalizer with multiple biquad filters

var audioCtx = window.AudioContext || window.webkitAudioContext;

var canvas;
var audioContext, canvasContext;
var gradient;
var analyser;
var width, height;

var dataArray, bufferLength;

window.onload = function() {
  audioContext= new audioCtx();
  
  canvas = document.querySelector("#myCanvas");
  width = canvas.width;
  height = canvas.height;
  canvasContext = canvas.getContext('2d');
  
  // create a vertical gradient of the height of the canvas
  gradient = canvasContext.createLinearGradient(0,0,0, height);
  gradient.addColorStop(1,'#000000');
  gradient.addColorStop(0.75,'#ff0000');
  gradient.addColorStop(0.25,'#ffff00');
  gradient.addColorStop(0,'#ffffff');
  
  buildAudioGraph();
  
  requestAnimationFrame(visualize);
};

function buildAudioGraph() {
  var mediaElement = document.getElementById('player');
  var sourceNode =   audioContext.createMediaElementSource(mediaElement);
  mediaElement.onplay = function() {
     audioContext.resume();
  }
  // Create an analyser node
  analyser = audioContext.createAnalyser();
  
  // Try changing for lower values: 512, 256, 128, 64...
  analyser.fftSize = 1024;
  bufferLength = analyser.frequencyBinCount;
  dataArray = new Uint8Array(bufferLength);
  
  sourceNode.connect(analyser);
  analyser.connect(audioContext.destination);
}

function visualize() {
  
  clearCanvas();
  
  drawVolumeMeter();
  drawWaveform();

  // call again the visualize function at 60 frames/s
  requestAnimationFrame(visualize);
  
}

function drawWaveform() {
  canvasContext.save();
  // Get the analyser data
  analyser.getByteTimeDomainData(dataArray);

  canvasContext.lineWidth = 2;
  canvasContext.strokeStyle = 'lightBlue';

  // all the waveform is in one single path, first let's
  // clear any previous path that could be in the buffer
  canvasContext.beginPath();
  
  var sliceWidth = width / bufferLength;
  var x = 0;
  
      // values go from 0 to 256 and the canvas heigt is 100. Let's rescale
      // before drawing. This is the scale factor
      heightScale = height/128;

  for(var i = 0; i < bufferLength; i++) {
     // dataArray[i] between 0 and 255
     var v = dataArray[i] / 255;
     var y = v * height;
    
     if(i === 0) {
        canvasContext.moveTo(x, y);
     } else {
        canvasContext.lineTo(x, y);
     }

     x += sliceWidth;
  }

  canvasContext.lineTo(canvas.width, canvas.height/2);
  
  // draw the path at once
  canvasContext.stroke();    
  canvasContext.restore();
}

function clearCanvas() {
   canvasContext.save();
  
   // clear the canvas
   // like this: canvasContext.clearRect(0, 0, width, height);
  
   // Or use rgba fill to give a slight blur effect
  canvasContext.fillStyle = 'rgba(0, 0, 0, 0.5)';
  canvasContext.fillRect(0, 0, width, height);
  
  canvasContext.restore();
}


function drawVolumeMeter() {
  canvasContext.save();
  
  analyser.getByteFrequencyData(dataArray);
  var average = getAverageVolume(dataArray);
  
  // set the fill style to a nice gradient
  canvasContext.fillStyle=gradient;
 
  // draw the vertical meter
  canvasContext.fillRect(0,height-average,25,height);
  
  canvasContext.restore();
}

function getAverageVolume(array) {
    var values = 0;
    var average;
 
    var length = array.length;
 
    // get all the frequency amplitudes
    for (var i = 0; i < length; i++) {
        values += array[i];
    }
 
    average = values / length;
    return average;
}

