var ctx;

var soundURL = 
 'https://mainline.i3s.unice.fr/mooc/shoot2.mp3';
var decodedSound;

window.onload = function init() {
  // To make it work even on browsers like Safari, that still
  // do not recognize the non prefixed version of AudioContext
var audioContext = window.AudioContext || window.webkitAudioContext;

 ctx = new audioContext();

  loadSoundUsingAjax(soundURL);
  
  playButton.onclick = function(evt) {
      playSound(decodedSound);
  };

};

function loadSoundUsingAjax(url) {
  var request = new XMLHttpRequest();
  
  request.open('GET', url, true);
  // Important: we're loading binary data
  request.responseType = 'arraybuffer';

  // Decode asynchronously
  request.onload = function() {
    console.log("Sound loaded");
    
    // Let's decode it. This is also asynchronous
    ctx.decodeAudioData(request.response, function(buffer) {
      console.log("Sound decoded");
      decodedSound = buffer;
      // we enable the button
      playButton.disabled = false;
    }, function(e) {
      console.log("error");});
  };
  
  // send the request. When the file will be loaded,
  // the request.onload callback will be called (above)
  request.send();
}

function playSound(buffer){
    var bufferSource = ctx.createBufferSource();
    bufferSource.buffer = buffer;
    bufferSource.connect(ctx.destination);
    bufferSource.start();
}

