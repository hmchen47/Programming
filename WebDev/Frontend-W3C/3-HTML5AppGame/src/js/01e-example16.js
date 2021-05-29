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
  
  requestAnimationFrame(visualize2);
};

function buildAudioGraph() {
  var mediaElement = document.getElementById('player');
  mediaElement.onplay = (e)=>{audioContext.resume();}
  var sourceNode =   audioContext.createMediaElementSource(mediaElement);

  // fix for autoplay policy
  mediaElement.addEventListener('play',() => audioContext.resume());

  // Create an analyser node
  analyser = audioContext.createAnalyser();
  
  // Try changing for lower values: 512, 256, 128, 64...
  analyser.fftSize = 256;
  bufferLength = analyser.frequencyBinCount;
  dataArray = new Uint8Array(bufferLength);
  
  sourceNode.connect(analyser);
  analyser.connect(audioContext.destination);
}

function visualize2() {
    canvasContext.save();
    canvasContext.fillStyle = "rgba(0, 0, 0, 0.05)";
    canvasContext.fillRect (0, 0, width, height);

    analyser.getByteFrequencyData(dataArray);
    var nbFreq = dataArray.length;
    
    var SPACER_WIDTH = 5;
    var BAR_WIDTH = 2;
    var OFFSET = 100;
    var CUTOFF = 23;
    var HALF_HEIGHT = height/2;
    var numBars = 1.7*Math.round(width / SPACER_WIDTH);
    var magnitude;
  
    canvasContext.lineCap = 'round';

    for (var i = 0; i < numBars; ++i) {
       magnitude = 0.3*dataArray[Math.round((i * nbFreq) / numBars)];
        
       canvasContext.fillStyle = "hsl( " + Math.round((i*360)/numBars) + ", 100%, 50%)";
       canvasContext.fillRect(i * SPACER_WIDTH, HALF_HEIGHT, BAR_WIDTH, -magnitude);
       canvasContext.fillRect(i * SPACER_WIDTH, HALF_HEIGHT, BAR_WIDTH, magnitude);

    }
    
    // Draw animated white lines top
    canvasContext.strokeStyle = "white";
    canvasContext.beginPath();

    for (i = 0; i < numBars; ++i) {
        magnitude = 0.3*dataArray[Math.round((i * nbFreq) / numBars)];
          if(i > 0) {
            //console.log("line lineTo "  + i*SPACER_WIDTH + ", " + -magnitude);
            canvasContext.lineTo(i*SPACER_WIDTH, HALF_HEIGHT-magnitude);
        } else {
            //console.log("line moveto "  + i*SPACER_WIDTH + ", " + -magnitude);
            canvasContext.moveTo(i*SPACER_WIDTH, HALF_HEIGHT-magnitude);
        }
    }
    for (i = 0; i < numBars; ++i) {
        magnitude = 0.3*dataArray[Math.round((i * nbFreq) / numBars)];
          if(i > 0) {
            //console.log("line lineTo "  + i*SPACER_WIDTH + ", " + -magnitude);
            canvasContext.lineTo(i*SPACER_WIDTH, HALF_HEIGHT+magnitude);
        } else {
            //console.log("line moveto "  + i*SPACER_WIDTH + ", " + -magnitude);
            canvasContext.moveTo(i*SPACER_WIDTH, HALF_HEIGHT+magnitude);
        }
    }    
    canvasContext.stroke();
    
    canvasContext.restore();
  
  requestAnimationFrame(visualize2);
}

