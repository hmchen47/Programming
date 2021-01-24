// support webkit-prefix for chrome (and friends)
if (window.webkitAudioontext !== undefined) {
  AudioContext = webkitAudioContext;
}
// support moz-prefix for Firefox (and friends)
if (window.mozAudioContext !== undefined) {
  AudioContext = mozAudioContext;
}

var context = new AudioContext();
var player = new ChiptunePlayer(context.destination);

window.onload = function() {
  document.getElementById("play").onclick = function() {
    player.play();
  }
  document.getElementById("pause").onclick = function() {
    player.pause();
  }
  document.getElementById("loop").onclick = function() {
    player.setLooping(this.checked);
  }

  var fileaccess = document.querySelector("*");
  fileaccess.ondrop = function(e) {
    var file = e.dataTransfer.files[0];
    try { player.unload(); } catch(err) {};

    var loop = document.getElementById("loop").checked;
    player.load(file, loop, function() {
      document.querySelector(".loadedfile").innerHTML = file.name;
    });
    e.preventDefault();
  }
  fileaccess.ondragenter = function(e){e.preventDefault();}
  fileaccess.ondragover = function(e){e.preventDefault();}

  var demolink = document.querySelector("#demosong");
  demolink.onclick = function() {
    try { player.unload(); } catch(err) {};

    var loop = document.getElementById("loop").checked;
    player.load("https://deskjet.github.io/chiptune.js/tunes/mysteristerium.mod", loop, function() {
      document.querySelector(".loadedfile").innerHTML = "mysteristerium.mod";
    });
  }
}
