var vgaButton, qvgaButton, hdButton, dimensions, video, stream;

function init() {
   vgaButton = document.querySelector('button#vga');
   qvgaButton = document.querySelector('button#qvga');
   hdButton = document.querySelector('button#hd');
   dimensions = document.querySelector('p#dimensions');
   video = document.querySelector('video');
  
  
  // Defines event listeners for the buttons that set the resolution
  qvgaButton.onclick = function() {
      getMedia(qvgaConstraints);
  };
  
  vgaButton.onclick = function() {
    getMedia(vgaConstraints);
  };
  
  hdButton.onclick = function() {
    getMedia(hdConstraints);
  };

  // Trick: check regularly the size of the video element and display it
  // When getUserMedia is called the video element changes it sizes but for 
  // a while its size is zero pixels... o we check every half a second
    video.addEventListener('play', function() {
       setTimeout(function() {
           displayVideoDimensions();
       }, 500);
    });
}


// The different values for the constraints on resolution
var qvgaConstraints = {
  video: {
    width: { max: 320 },
    height: { max: 180 }
  }
};

var vgaConstraints = {
    video: {
    width: { max: 640 },
    height: { max: 360 }
  }
};

var hdConstraints = {
  video: {
    width: { min: 1280 },
    height: { min: 720 }
  }
};

// The function that is called when a button has been clicked: starts the video
// with the preferred resolution
function getMedia(constraints) {
  if (!!stream) {
    video.srcObject = null;
    stream.getTracks()[0].stop();
  }
 navigator.mediaDevices.getUserMedia(constraints)
 .then((stream) => {
   video.srcObject = stream;
   video.play();
   window.stream = stream;
 })
 .catch((error) =>{
    console.log('navigator.getUserMedia error: ', error);
 });
}

// util function that is called by the setInterval(...) every 0.5s, for
// displaying the video dimensions
function displayVideoDimensions() {
  dimensions.innerHTML = 'Actual video dimensions: ' + video.videoWidth +
    'x' + video.videoHeight + 'px.';
}

