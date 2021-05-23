var langButtonDiv, currentLangSpan, video;

function init() {
   langButtonDiv = document.querySelector("#langButtonDiv");
   currentLangSpan = document.querySelector("#currentLang");
   video = document.querySelector("#myVideo");
   console.log("Number of tracks = " + video.textTracks.length);
   // Updates the display of the current track activated
   currentLangSpan.innerHTML = activeTrack();
   // Build the buttons for choosing a track
   buildButtons();
}


function activeTrack() {
   for (var i = 0; i < video.textTracks.length; i++) {
     if(video.textTracks[i].mode === 'showing') {
       return video.textTracks[i].label + " (" + video.textTracks[i].language + ")";
     }
   }
  return "no subtitles/caption selected";
}


function buildButtons() {
  if (video.textTracks) {

   // for each track, create a button
   for (var i = 0; i < video.textTracks.length; i++) {
      // We create buttons only for the caption and subtitle tracks
     var track = video.textTracks[i];
  if((track.kind !== "subtitles") && (track.kind !== "captions")) continue;
     
     createButton(video.textTracks[i]);
   }
  }
}
  
function createButton(track) {
    var b = document.createElement("button");
    b.value=track.label;
    b.setAttribute("lang", track.language); 
  
    b.addEventListener('click', function(e) {
      // check which track is the track with the language we're
      // looking for
      var lang = this.getAttribute('lang');
	  for (var i = 0; i < video.textTracks.length; i++) {
			if (video.textTracks[i].language == lang) {
				video.textTracks[i].mode = 'showing';
			} else {
				video.textTracks[i].mode = 'hidden';
			}
	  }
      // update the span so that it displays the new active track
      currentLangSpan.innerHTML = activeTrack();
    });
    b.appendChild(document.createTextNode(track.label));
  langButtonDiv.appendChild(b);
}
  

