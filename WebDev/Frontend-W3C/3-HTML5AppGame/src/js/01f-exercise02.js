var video;
 
window.onload = function() {
  video = document.querySelector("#myVideo");
  var firstTrack = video.textTracks[0];
  readContent(firstTrack);
};
 
function readContent(track) {
  console.log("adding cue change listener to loaded track...");
  track.addEventListener("cuechange", function(e) {
     var cue = this.activeCues[0];
     if(cue !== undefined)
        console.log( "cue change: text = " + cue.text);
     });
     video.play();
}

