var audioCtx = window.AudioContext || window.webkitAudioContext;
var audioContext, canvasContext;

var filters = [];

var canvas;
var analyser;
var width, height;
var dataArray, bufferLength;
var masterGain, stereoPanner;

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

      // fix for autoplay policy
  mediaElement.addEventListener('play',() => audioContext.resume());

  var sourceNode =   audioContext.createMediaElementSource(mediaElement);
  
  // Create an analyser node
  analyser = audioContext.createAnalyser();
  
  // Try changing for lower values: 512, 256, 128, 64...
  analyser.fftSize = 512;
  bufferLength = analyser.frequencyBinCount;
  dataArray = new Uint8Array(bufferLength);
  
  // create the equalizer. It's a set of biquad Filters


    // Set filters
    [60, 170, 350, 1000, 3500, 10000].forEach(function(freq, i) {
      var eq = audioContext.createBiquadFilter();
      eq.frequency.value = freq;
      eq.type = "peaking";
      eq.gain.value = 0;
      filters.push(eq);
    });

   // Connect filters in serie
   sourceNode.connect(filters[0]);
   for(var i = 0; i < filters.length - 1; i++) {
      filters[i].connect(filters[i+1]);
    }
  
    // Master volume is a gain node
  masterGain = audioContext.createGain();
  masterGain.value = 1;
 

   // connect the last filter to the speakers
   filters[filters.length - 1].connect(masterGain);
  
  // for stereo balancing, split the signal
  stereoPanner = audioContext.createStereoPanner();
  // connect master volume output to the panner
  masterGain.connect(stereoPanner);
  
  // Connect the stereo panner to analyser and analyser to destination
  stereoPanner.connect(analyser);  
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


function changeGain(sliderVal,nbFilter) {
  var value = parseFloat(sliderVal);
  filters[nbFilter].gain.value = value;
  
  // update output labels
  var output = document.querySelector("#gain"+nbFilter);
  output.value = value + " dB";
}

function changeMasterGain(sliderVal) {
  var value = parseFloat(sliderVal);
  masterGain.gain.value =  value/10;
  
   // update output labels
  var output = document.querySelector("#masterGainOutput");
  output.value = value;
}

function changeBalance(sliderVal) {
  // between -1 and +1
  var value = parseFloat(sliderVal);
  
stereoPanner.pan.value = value;
   // update output labels
  var output = document.querySelector("#balanceOutput");
  output.value = value;
}

