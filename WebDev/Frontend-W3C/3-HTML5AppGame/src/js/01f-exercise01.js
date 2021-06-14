var video, htmlTracks;
 
window.onload = function() {
   // Called when the page has been loaded
   video = document.querySelector("#myVideo");
   // Get the tracks as HTML elements
   htmlTracks = document.querySelectorAll("track");
 
   var firstTrack = htmlTracks[0];
 
   // do something with this track...
   // access properties etc.
   // Question 1~3
   console.log('first track type (firstTrack.kind): ' + firstTrack.kind);
   console.log('first track language (firstTrack.srclang): ' + firstTrack.srclang);
   console.log('first track status (firstTrack.readyState): ' + firstTrack.readyState);
   console.log('first tract contents (firstTrack.cues): ' + firstTrack.cues);

};

