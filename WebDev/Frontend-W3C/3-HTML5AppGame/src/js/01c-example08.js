var video, transcriptDiv, chapterMenuDiv;
var tracks, trackElems, tracksURLs = [];
var buttonEnglish, buttonDeutsch, buttonEnglishChapters;

window.onload = function() {
  console.log("init");
  // when the page is loaded
  video = document.querySelector("#myVideo");
  transcriptDiv = document.querySelector("#transcript");
  chapterMenuDiv = document.querySelector("#chapterMenu");
  
  // The tracks as HTML elements
  trackElems = document.querySelectorAll("track");
  for(var i = 0; i < trackElems.length; i++) {
    var currentTrackElem = trackElems[i];
    tracksURLs[i] = currentTrackElem.src;
  }
  
  buttonEnglish = document.querySelector("#buttonEnglish");
  buttonDeutsch = document.querySelector("#buttonDeutsch");
  buttonEnglishChapters =   document.querySelector("#buttonEnglishChapters");
  
  // we enable the buttons and show transcript
  buttonEnglish.disabled = false;
  buttonDeutsch.disabled = false;
    buttonEnglishChapters.disabled = false;
  // The tracks as JS objects
  tracks = video.textTracks;
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

function displayChapters(track) {
    var cues = track.cues;
    
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
      displayChapters(track);
   });
}


function loadTranscript(lang, kind) {
  // clear current transcript
  clearTranscriptDiv();
  
  // set all track mode to disabled. We will only activate the
  // one whose content will be displayed as transcript
  if(kind !== 'chapters')
      disableAllTracks(); // if displaying chapters, do not
                          // disable all tracks
  
  // Locate the track with language = lang
  for(var i = 0; i < tracks.length; i++) {
    // current track
    var track = tracks[i];
    var trackAsHtmlElem = trackElems[i];
  
    if((track.language === lang) && (track.kind === kind)) {
      track.mode="showing";

      if(trackAsHtmlElem.readyState === 2) {
        // the track has already been loaded
        displayCues(track);
      } else {
        displayCuesAfterTrackLoaded(trackAsHtmlElem, track);
      }
      
/*      track.addEventListener("cuechange", function(e) {
        var cue = this.activeCues[0];
        console.log("cue change");
        var transcriptText = document.getElementById(cue.id);
        transcriptText.classList.add("current");
      });
      */
    }
  } 
}
  

function displayCuesAfterTrackLoaded(trackElem, track) {
  // Create a listener that will be called only when the track has
  // been loaded
  trackElem.addEventListener('load', function(e) {
      console.log("track loaded");
      displayCues(track);
   });
}
function disableAllTracks() {
    for(var i = 0; i < tracks.length; i++) 
      tracks[i].mode = "disabled";
}

function displayCues(track) {
    var cues = track.cues;
    
    //append all the subtitle texts to 
      for(var i=0, len = cues.length; i < len; i++) {
        var cue = cues[i];
        addCueListeners(cue);

        var voices = getVoices(cue.text);
        var transText="";
        if (voices.length > 0) {
            for (var j = 0; j < voices.length; j++) { // how many voices ?
                transText += voices[j].voice + ': ' + removeHTML(voices[j].text);
            }
          } else 
             transText = cue.text; // not a voice text
        var clickableTransText = "<li class='cues' id=" + cue.id +  " onclick='jumpTo(" + cue.startTime + ");'" + ">" + transText + "</li>";

        addToTranscriptDiv(clickableTransText);
      }
  }

function getVoices(speech) {  // takes a text content and check if there are voices 
  var voices = [];            // inside
  var pos = speech.indexOf('<v'); // voices are like <v michel> ....
  while (pos != -1) {
    endVoice = speech.indexOf('>');
    var voice = speech.substring(pos + 2, endVoice).trim();
    var endSpeech = speech.indexOf('</v>');
    var text = speech.substring(endVoice + 1, endSpeech);
    voices.push({
       'voice': voice,
       'text': text
    });
    speech = speech.substring(endSpeech + 4);
    pos = speech.indexOf('<v');
  }
  return voices;
}

function removeHTML(text) {
  var div = document.createElement('div');
  div.innerHTML = text;
  return div.textContent || div.innerText || '';
}
function jumpTo(time) {
  video.currentTime = time;
  video.play();
}

function clearTranscriptDiv() {
  transcriptDiv.innerHTML = "";
}

function addToTranscriptDiv(htmlText) {
  transcriptDiv.innerHTML += htmlText;
}

function addCueListeners(cue) {
  cue.onenter = function(){
    console.log('enter id=' + this.id);
    var transcriptText = document.getElementById(this.id);
    transcriptText.classList.add("current");
  };

  cue.onexit = function(){
    console.log('exit id=' + cue.id);
   var transcriptText = document.getElementById(this.id); transcriptText.classList.remove("current");
  };
}
