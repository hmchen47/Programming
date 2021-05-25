window.onload = function() {
    var videoElement = document.querySelector("#myVideo");
    var myIFrame = document.querySelector("#myIframe");
    var currentURLSpan = document.querySelector("#currentURL");

    var textTracks = videoElement.textTracks; // one for each track element
    var textTrack = textTracks[0]; // corresponds to the first track element
  
    // change mode so we can use the track
    textTrack.mode = "hidden";
    // Default position on the google map
    var centerpos = new google.maps.LatLng(48.579400,7.7519);
 
    // default options for the google map
    var optionsGmaps = {
       center:centerpos,
       navigationControlOptions: {style: google.maps.NavigationControlStyle.SMALL},
       mapTypeId: google.maps.MapTypeId.ROADMAP,
       zoom: 15
    };
 
    // Init map object
    var map = new google.maps.Map(document.getElementById("map"), optionsGmaps);
 
    // cue change listener, this is where the synchronization between
    // the HTML document and the video is done
    textTrack.oncuechange = function (){
       // we suppose that we have no overlapping cues
       var cue = this.activeCues[0];
       if(cue === undefined) return;
       // get cue content as a JavaScript object
       var cueContentJSON = JSON.parse(cue.text);
       // do different things depending on the type of sync (wikipedia, gmap)
       switch(cueContentJSON.type) {
         case'WikipediaPage':
            var myURL = cueContentJSON.url;
            var myLink = "<a href=\"" + myURL + "\">" + myURL + "</a>";
            currentURLSpan.innerHTML = myLink;
            myIFrame.src = myURL; // assign url to src property
            break;
         case 'LongLat':
            drawPosition(cueContentJSON.long, cueContentJSON.lat);
            break;
       }
   };
 
   function drawPosition(long, lat) {
      // Make new object LatLng for Google Maps
      var latlng = new google.maps.LatLng(lat, long);
 
      // Add a marker at position
      var marker = new google.maps.Marker({
          position: latlng,
          map: map,
          title:"You are here"
      });
      // center map on longitude and latitude
      map.panTo(latlng);
   }
};

