var video, htmlTracks;
var trackStatusesDiv;
var buttonLoadFirstTrack, buttonLoadThirdTrack;

window.onload = function() {
  // called when the page has been loaded
  video = document.querySelector("#myVideo");
  trackStatusesDiv = document.querySelector("#trackStatusesDiv");
  buttonLoadFirstTrack = document.querySelector("#buttonLoadFirstTrack");
       buttonLoadFirstTrack.disabled=false;                                         buttonLoadThirdTrack = document.querySelector("#buttonLoadThirdTrack");
       buttonLoadThirdTrack.disabled=false;           
  
  // Get the tracks as HTML elements
  htmlTracks = document.querySelectorAll("track");
  
  // displauy their status in a div under the video
  displayTrackStatuses(htmlTracks);
};



function displayTrackStatuses(htmlTracks) {
  trackStatusesDiv.innerHTML = "";
    // display track info
  for(var i = 0; i < htmlTracks.length; i++) {
    var currentHtmlTrack = htmlTracks[i];
    var currentTextTrack = currentHtmlTrack.track;
        
    var label = "<li>label = " + currentHtmlTrack.label + "</li>";
    var kind = "<li>kind = " + currentHtmlTrack.kind + "</li>";
    var lang = "<li>lang = " + currentHtmlTrack.srclang + "</li>";
    var readyState = "<li>readyState = " + currentHtmlTrack.readyState + "</li>";
    var mode = "<li>mode = " + currentTextTrack.mode + "</li>";
    
    trackStatusesDiv.innerHTML += "<li><b>Track:" + i + ":</b></li>" + "<ul>" + label + kind + lang + readyState + mode + "</ul>";   
  }
}

function readContent(track) {
  console.log("adding cue change listener to loaded track...");
  trackStatusesDiv.innerHTML = "";
  
  track.addEventListener("cuechange", function(e) {
   var cue = this.activeCues[0];
    if(cue !== undefined)
       trackStatusesDiv.innerHTML += "cue change: text = " + cue.text + "<br>";
 });
  
  video.play();

}

function getTrack(htmlTrack, callback) {
  var textTrack = htmlTrack.track;
  
  
  if(htmlTrack.readyState === 2) {
     console.log("text track already loaded");
     callback(textTrack);
  } else {
     // will force the track to be loaded
         console.log("Forcing the text track to be loaded");

     textTrack.mode = "hidden";
     htmlTrack.addEventListener('load', function(e) {
         callback(textTrack);
    });
  }
}

function forceLoadTrack(n) {
  getTrack(htmlTracks[n], readContent);
}

