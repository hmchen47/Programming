var audioCtx = window.AudioContext || window.webkitAudioContext;

var canvas;
var audioContext, canvasContext;
var width, height;

var analyser, bufferLength, dataArray;

window.onload = function() {
  // we get the audio context
  audioContext = new audioCtx();
  
  // prepare eveything for the canvas
  canvas = document.querySelector("#myCanvas");
  width = canvas.width;
  height = canvas.height;
  canvasContext = canvas.getContext('2d');
  
  buildAudioGraph();
  
  // start the visualization
  requestAnimationFrame(visualize);
};


function buildAudioGraph() {
 var player = document.getElementById("player");
 var source = audioContext.createMediaElementSource(player);
  
 // fix for autoplay policy
  player.addEventListener('play',() => audioContext.resume());
  
  analyser = audioContext.createAnalyser();
 // set its properties
  analyser.fftSize = 1024;
  // its size is always the fftSize / 2
  bufferLength = analyser.frequencyBinCount;
  dataArray = new Uint8Array(bufferLength);
  
  // connect the nodes
  source.connect(analyser);
  analyser.connect(audioContext.destination);
}


function visualize() {
  // clear the canvas 
  canvasContext.clearRect(0, 0, width, height);
  
  // We will draw it as a path of connected lines
  // First, clear the previous path that was in the buffer
  canvasContext.beginPath();
  
  // draw the data as a waveform
  // Get the data from the analyser
  analyser.getByteTimeDomainData(dataArray);
  // values are between 0 and 255
  
  // slice width
  var sliceWidth = width / bufferLength;
  
  var x = 0;
  for(var i = 0; i < bufferLength; i ++) {
    var v = dataArray[i]; // between 0 and 255
     v = v / 255; // now between 0 and 1
    
    var y = v * height;
    if(i === 0) {
      canvasContext.moveTo(x, y);
    } else {
      canvasContext.lineTo(x, y);
    } 
    
    x += sliceWidth;
  }
  
  // draw the whole waveform (a path)
  canvasContext.stroke();
 
  // call again the visualize function at 60 frames/s
  requestAnimationFrame(visualize);
}
