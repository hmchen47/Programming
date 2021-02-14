window.onload = init;

function init() {
   navigator.mediaDevices.getUserMedia({audio: true,video: true})
     .then(function (stream) {
	       var video = document.querySelector('#video');
	       video.srcObject = stream;
	       video.play();
      })
     .catch(function(err) {
        alert("something went wrong: " + err)
   });
}


