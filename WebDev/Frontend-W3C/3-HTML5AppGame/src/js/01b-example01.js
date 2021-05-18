var video, htmlTracks;
var trackStatusesDiv;

window.onload = function() {
  // called when the page has been loaded
  video = document.querySelector("#myVideo");
  trackStatusesDiv = document.querySelector("#trackStatusesDiv");
  
  // Get the tracks as HTML elements
  htmlTracks = document.querySelectorAll("track");
  
  // display their status in a div under the video
  displayTrackStatuses();
};

function displayTrackStatuses() {
  trackStatusesDiv.innerHTML ="";
  
    // display track info
  for(var i = 0; i < htmlTracks.length; i++) {
    var currentHtmlTrack = htmlTracks[i];
        
    var label = "<li>label = " + currentHtmlTrack.label + "</li>";
    var kind = "<li>kind = " + currentHtmlTrack.kind + "</li>";
    var lang = "<li>lang = " + currentHtmlTrack.srclang + "</li>";
    var readyState = "<li>readyState = " + currentHtmlTrack.readyState + "</li>";
    
    trackStatusesDiv.innerHTML += "<li><b>Track:" + i + ":</b></li>" + "<ul>" + label + kind + lang + readyState + "</ul>";   
  }
}
