// This line is a trick to initialize the AudioContext
// that will work on all recent browsers
var ctx = window.AudioContext || window.webkitAudioContext;
var audioContext;
var compressorExemple, gainSlider1, gainNode1, compressorNode;
var compressorButton;
var compressorOn = false;

window.onload = function() {
  
   // get the AudioContext
   audioContext = new ctx();

   // the audio element
   compressorExemple = document.querySelector('#compressorExample');
   gainSlider1 = document.querySelector('#gainSlider1');
   // button for turning on/off the compressor
   compressorButton = document.querySelector('#compressorButton');
  
   // fix for autoplay policy
   compressorExemple.addEventListener('play',() => audioContext.resume());

  buildAudioGraph();
  
  // input listener on the gain slider
  gainSlider1.oninput = function(evt) {
    gainNode1.gain.value = evt.target.value;
  }; 
  
  compressorButton.onclick = function(evt) {
      if(compressorOn) {
      // disconnect the compressor and make a 
      // direct route from gain to destination
      compressorNode.disconnect(audioContext.destination);
      gainNode1.disconnect(compressorNode);
      gainNode1.connect(audioContext.destination);
      compressorButton.innerHTML="Turn compressor: On";
    }  else {
      // compressor was off, we connect the gain to the compressor 
      // and the compressor to the destination
      gainNode1.disconnect(audioContext.destination);
      gainNode1.connect(compressorNode);
      compressorNode.connect(audioContext.destination);
      compressorButton.innerHTML="Turn compressor: Off";
    }
    compressorOn = !compressorOn;
  };    
};

function buildAudioGraph() {
    // create source and gain node
    var gainMediaElementSource = audioContext.createMediaElementSource(compressorExemple);
    gainNode1 = audioContext.createGain();
    gainNode1.gain.value = parseFloat(gainSlider1.value);
  
    // do not connect it yet
    compressorNode = audioContext.createDynamicsCompressor();
  
  
    // connect nodes together
    gainMediaElementSource.connect(gainNode1);
    gainNode1.connect(audioContext.destination);
}

