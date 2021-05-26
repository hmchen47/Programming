// This line is a trick to initialize the AudioContext
// that will work on all recent browsers
var ctx = window.AudioContext || window.webkitAudioContext;
var audioContext;
var player, pannerSlider, pannerNode;

window.onload = function() {
  
   // get the AudioContext
   audioContext = new ctx();

    // the audio element
   playerPanner = document.querySelector('#pannerPlayer');
    playerPanner.onplay = (e) => {audioContext.resume();}

   pannerSlider = document.querySelector('#pannerSlider');

  buildAudioGraphPanner();
  
  // input listener on the gain slider
  pannerSlider.oninput = function(evt){
    pannerNode.pan.value = evt.target.value;
  }; 
};

function buildAudioGraphPanner() {
    // create source and gain node
    var source = audioContext.createMediaElementSource(playerPanner);
    pannerNode = audioContext.createStereoPanner();
  
    // connect nodes together
    source.connect(pannerNode);
    pannerNode.connect(audioContext.destination);

}

