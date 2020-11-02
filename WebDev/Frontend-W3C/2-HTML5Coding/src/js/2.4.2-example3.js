//--------------------
// GET USER MEDIA CODE
//--------------------
let video;
let webcamStream;

function startWebcam() {
    // request video and audio stream from the user's webcam
  navigator.mediaDevices.getUserMedia({
    audio: true,
    video: true
  }).then((stream) => {
    video = document.querySelector('#video');
    video.srcObject = stream;
    video.play();

    webcamStream = stream;
  }).catch((error) => {
    console.log('navigator.getUserMedia error: ', error);
  });
}

function stopWebcam() {
    webcamStream.getTracks()[0].stop(); // audio
    webcamStream.getTracks()[1].stop(); // video
} 


//---------------------
// TAKE A SNAPSHOT CODE
//---------------------
var canvas, ctx;

function init() {
  // Get the canvas and obtain a context for
  // drawing in it
  canvas = document.getElementById("myCanvas");
  ctx = canvas.getContext('2d');
}

function snapshot() {
   // Draws current image from the video element into the canvas
  ctx.drawImage(video, 0,0, canvas.width, canvas.height);
}

