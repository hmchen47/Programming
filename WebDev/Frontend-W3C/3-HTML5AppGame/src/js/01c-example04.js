var video, transcriptDiv;
var tracks, trackElems, tracksURLs = [];
var buttonEnglish, buttonDeutsch;

window.onload = function() {
  console.log("init");
  // when the page is loaded
  video = document.querySelector("#myVideo");
  transcriptDiv = document.querySelector("#transcript");
  
  // The tracks as HTML elements
  trackElems = document.querySelectorAll("track");
  for(var i = 0; i < trackElems.length; i++) {
    var currentTrackElem = trackElems[i];
    tracksURLs[i] = currentTrackElem.src;
  }
  
  buttonEnglish = document.querySelector("#buttonEnglish");
  buttonDeutsch = document.querySelector("#buttonDeutsch");
  
  // we enable the buttons and show transcript
  buttonEnglish.disabled = false;
  buttonDeutsch.disabled = false;
    
  // The tracks as JS objects
  tracks = video.textTracks;
};

function loadTranscript(lang) {
  // clear current transcript
  clearTranscriptDiv();
  
  // set all track mode to disabled. We will only activate the
  // one whose content will be displayed as transcript
  disableAllTracks();
  
  // Locate the track with language = lang
  for(var i = 0; i < tracks.length; i++) {
    // current track
    var track = tracks[i];
    var trackAsHtmlElem = trackElems[i];
  
    if((track.language === lang) && (track.kind !== "chapters")) {
      track.mode="showing";

      if(trackAsHtmlElem.readyState === 2) {
        // the track has already been loaded
        displayCues(track);
      } else {
        displayCuesAfterTrackLoaded(trackAsHtmlElem, track);
      }
      
/*      FOR FIREFOX....
        track.addEventListener("cuechange", function(e) {
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

