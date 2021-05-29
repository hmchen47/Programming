//buil an equalizer with multiple biquad filters

var audioCtx = window.AudioContext || window.webkitAudioContext;

var canvas;
var audioContext, canvasContext;
var analyser;
var width, height;

var dataArray, bufferLength;

window.onload = function() {
  audioContext= new audioCtx();
  
  canvas = document.querySelector("#myCanvas");
  width = canvas.width;
  height = canvas.height;
  canvasContext = canvas.getContext('2d');
  
  buildAudioGraph();
  
  requestAnimationFrame(visualize);
};

function buildAudioGraph() {
  var mediaElement = document.getElementById('player');
    mediaElement.onplay = (e)=>{audioContext.resume();}

      // fix for autoplay policy
  mediaElement.addEventListener('play',() => audioContext.resume());

  var sourceNode =   audioContext.createMediaElementSource(mediaElement);
  
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
  // clear the canvas
  // like this: canvasContext.clearRect(0, 0, width, height);
  
  // Or use rgba fill to give a slight blur effect
  canvasContext.fillStyle = 'rgba(0, 0, 0, 0.5)';
  canvasContext.fillRect(0, 0, width, height);
  
  // Get the analyser data
  analyser.getByteTimeDomainData(dataArray);

  canvasContext.lineWidth = 2;
  canvasContext.strokeStyle = 'lightBlue';

  // all the waveform is in one single path, first let's
  // clear any previous path that could be in the buffer
  canvasContext.beginPath();
  
  var sliceWidth = width / bufferLength;
  var x = 0;

  for(var i = 0; i < bufferLength; i++) {
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
  
  // call again the visualize function at 60 frames/s
  requestAnimationFrame(visualize);
  
}
