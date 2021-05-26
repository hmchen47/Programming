// This line is a trick to initialize the AudioContext
// that will work on all recent browsers
var ctx = window.AudioContext || window.webkitAudioContext;
var audioContext;
var gainExample, gainSlider, gainNode;

window.onload = function() {
  
   // get the AudioContext
   audioContext = new ctx();

   // the audio element
   gainExample = document.querySelector('#gainExample');
   gainSlider = document.querySelector('#gainSlider');

   // fix for autoplay policy
  gainExample.addEventListener('play',() => audioContext.resume());
  
  buildAudioGraph();
  
  // input listener on the gain slider
  gainSlider.oninput = function(evt){
    gainNode.gain.value = evt.target.value;
  }; 
};

function buildAudioGraph() {
    // create source and gain node
    var gainMediaElementSource = audioContext.createMediaElementSource(gainExample);
    gainNode = audioContext.createGain();
  
    // connect nodes together
    gainMediaElementSource.connect(gainNode);
    gainNode.connect(audioContext.destination);


}

