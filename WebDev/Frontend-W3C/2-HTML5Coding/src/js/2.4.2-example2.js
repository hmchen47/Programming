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
        let video = document.querySelector('#video');
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
//------------------------------
// CODE FOR CHANGING CSS FILTERS
//------------------------------
let idx = 0;
  let filters = [
    'grayscale',
    'sepia',
    'blur',
    'brightness',
    'contrast',
    'hue-rotate', 'hue-rotate2', 'hue-rotate3',
    'saturate',
    'invert'
  ];
  
  function changeFilter(el) {
    // Remove all CSS classes for element el
    el.className = '';
    
    // Choose a CSS class name
        console.log("toggling effect: " + filters[idx % filters.length]);
    
    let effect = filters[idx++ % filters.length];  
    el.classList.add(effect);

}
 
 