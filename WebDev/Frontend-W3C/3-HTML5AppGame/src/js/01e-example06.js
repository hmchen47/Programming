// This line is a trick to initialize the AudioContext
// that will work on all recent browsers
var ctx = window.AudioContext || window.webkitAudioContext;
var audioContext;
var convolverSlider, convolverNode, convolverGain, directGain;
var impulseURL = "https://mainline.i3s.unice.fr/mooc/Scala-Milan-Opera-Hall.wav";
var decodedImpulse;

window.onload = function() {
  
   // get the AudioContext
   audioContext = new ctx();

    // the audio element
   playerConvolver = document.querySelector('#convolverPlayer');
   playerConvolver.onplay = (e) =>{audioContext.resume();}
      playerConvolver.onplay = (e) => {audioContext.resume();}

   convolverSlider = document.querySelector('#convolverSlider');

  loadImpulse(impulseURL, function() {
    // we get here only when the impulse has finished
    // loading
    buildAudioGraphConvolver();
  });
  
  
  // input listener on the gain slider
  convolverSlider.oninput = function(evt){
    // We set the gain at the output of the convolver (wet signal route) with the
    // slider value, and we set the gain between the source and dest
    // (dry signal route) to 1 - wet
    convolverGain.gain.value = parseFloat(evt.target.value);
    directGain.gain.value = 1 - convolverGain.gain.value;
  }; 
};

function buildAudioGraphConvolver() {
    // create source and gain node
    var source = audioContext.createMediaElementSource(playerConvolver);
    convolverNode = audioContext.createConvolver();
    convolverNode.buffer = decodedImpulse;
  
    convolverGain = audioContext.createGain();
    convolverGain.gain.value = 0;
  
    directGain = audioContext.createGain();
    directGain.gain.value = 1;
    
  
    // direct/dry route source -> directGain -> destination
    source.connect(directGain);
    directGain.connect(audioContext.destination);
  
    // wet route with convolver: source -> convolver 
    // -> convolverGain -> destination
    source.connect(convolverNode);
    convolverNode.connect(convolverGain);
    convolverGain.connect(audioContext.destination);
}

function loadImpulse(url, callback) {
  
  ajaxRequest = new XMLHttpRequest();
  ajaxRequest.open('GET', url, true);
  ajaxRequest.responseType = 'arraybuffer';

  ajaxRequest.onload = function() {
    var impulseData = ajaxRequest.response;

    audioContext.decodeAudioData(impulseData,  function(buffer) {
        decodedImpulse = buffer;
        callback();
    });
  };
  
  ajaxRequest.onerror = function(e) {
      console.log("Error with decoding audio data" + e.err);
  };
  
  ajaxRequest.send();
}
