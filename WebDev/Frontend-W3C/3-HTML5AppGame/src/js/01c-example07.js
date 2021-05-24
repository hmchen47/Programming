var video, chapterMenuDiv;
var tracks, trackElems, tracksURLs = [];

window.onload = function() {
  console.log("init");
  // when the page is loaded
  video = document.querySelector("#myVideo");
  chapterMenuDiv = document.querySelector("#chapterMenu");
  
  // The tracks as HTML elements
  trackElems = document.querySelectorAll("track");
  for(var i = 0; i < trackElems.length; i++) {
    var currentTrackElem = trackElems[i];
    tracksURLs[i] = currentTrackElem.src;
  }
  
  // The tracks as JS objects
  tracks = video.textTracks;
  
  buildChapterMenu('en', 'chapters');
};

function buildChapterMenu(lang, kind) {
    // Locate the track with language = lang and kind="chapters"
  for(var i = 0; i < tracks.length; i++) {
    // current track
    var track = tracks[i];
    var trackAsHtmlElem = trackElems[i];
  
    if((track.language === lang) && (track.kind === kind)) {
      // the track must be active if we want to highlight the 
      // current chapter while the video is playing
      track.mode="showing"; 

      if(trackAsHtmlElem.readyState === 2) {
        // the track has already been loaded
        displayChapterMarkers(track);
      } else {
        displayChapterMarkersAfterTrackLoaded(trackAsHtmlElem, track);
      }
    }
  } 
}

function displayChapterMarkers(track) {
    var cues = track.cues;
  
    // We should not see the cues on the video.
    track.mode="hidden";
  
    // Iterate on cues
      for(var i=0, len = cues.length; i < len; i++) {
        var cue = cues[i];
        //addCueListeners(cue);

        var cueObject = JSON.parse(cue.text);
        var description = cueObject.description;
        var imageFileName = cueObject.image;
        var imageURL = "https://mainline.i3s.unice.fr/mooc/" + imageFileName;
        
        // add an image to the menu
        var figure = document.createElement('figure');
        figure.classList.add("img");
        
        figure.innerHTML = "<img onclick='jumpTo(" + cue.startTime + ");'  class='thumb' src='" + imageURL + "'><figcaption class='desc'>" + description + "</figcaption></figure>";
        chapterMenuDiv.insertBefore(figure, null);
      }
  }

function displayChapterMarkersAfterTrackLoaded(trackElem, track) {
  // Create a listener that will be called only when the track has
  // been loaded
  trackElem.addEventListener('load', function(e) {
      console.log("chapter track loaded");
      displayChapterMarkers(track);
   });
}

function jumpTo(time) {
  video.currentTime = time;
  video.play();
}

